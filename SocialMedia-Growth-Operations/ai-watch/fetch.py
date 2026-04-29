#!/usr/bin/env python3
"""
ai-watch fetch.py

读取 feeds.opml -> 拉每个 RSS 源 -> 过滤近 N 天 -> 按 4 大栏目关键词归类
-> 输出 Markdown 候选稿 output/YYYY-WXX.md
-> 同时把每条候选 POST 到飞书多维表格 webhook（可选）

用法:
    .venv/bin/pip install feedparser
    .venv/bin/python fetch.py                # 正常出周报 + 推飞书
    .venv/bin/python fetch.py --no-feishu    # 只出 Markdown，不推飞书
    .venv/bin/python fetch.py --test-feishu  # 只发一条测试数据到飞书（用于联路自检）

环境变量（可写在同目录 .env）:
    FEISHU_WEBHOOK_URL    飞书 webhook 地址
    MAX_PER_CATEGORY      每栏推飞书最多多少条（默认 8）
    PUSH_DELAY_SECONDS    每条推送间隔（默认 0.5 秒）
    WINDOW_DAYS           时间窗口（默认 7 天）
"""

from __future__ import annotations

import os
import re
import sys
import json
import time
import socket
import logging
import argparse
import datetime as dt
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from pathlib import Path

try:
    import feedparser
except ImportError:
    print("[ERR] 请先安装依赖: .venv/bin/pip install feedparser", file=sys.stderr)
    sys.exit(1)

socket.setdefaulttimeout(15)

ROOT = Path(__file__).resolve().parent
OPML_PATH = ROOT / "feeds.opml"
ENV_PATH = ROOT / ".env"
OUTPUT_DIR = ROOT / "output"
LOG_DIR = ROOT / "logs"
STATE_DIR = ROOT / "state"
OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)
STATE_DIR.mkdir(exist_ok=True)


def load_env(path: Path) -> None:
    """简易 .env 加载，不依赖 python-dotenv。"""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


load_env(ENV_PATH)

WINDOW_DAYS = int(os.environ.get("WINDOW_DAYS", "7"))
MAX_PER_CATEGORY = int(os.environ.get("MAX_PER_CATEGORY", "8"))
PUSH_DELAY_SECONDS = float(os.environ.get("PUSH_DELAY_SECONDS", "0.5"))
FEISHU_WEBHOOK_URL = os.environ.get("FEISHU_WEBHOOK_URL", "").strip()

NOW = dt.datetime.now(dt.timezone.utc)
CUTOFF = NOW - dt.timedelta(days=WINDOW_DAYS)

LOG_FILE = LOG_DIR / f"{NOW.strftime('%Y-%m-%d')}.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("ai-watch")

CATEGORY_KEYWORDS: dict[str, list[str]] = {
    "01 AI 模型 / 产品动态": [
        "gpt", "claude", "gemini", "llama", "mistral", "qwen",
        "openai", "anthropic", "deepmind", "model release", "frontier model",
        "foundation model", "agentic", "mcp", "ai agent", "llm",
        "reasoning model", "multimodal", "ai infrastructure", "ai chip",
    ],
    "02 AI + 设计": [
        "design", "figma", "adobe", "canva", "ux", "ui", "prototype",
        "design system", "vibe design", "design token", "creative",
        "designer", "interaction", "wireframe",
    ],
    "03 AI + 海外营销": [
        "marketing", "saas", "growth", "b2b", "paid media", "performance",
        "brand", "content marketing", "seo", "geo", "aeo", "ai search",
        "ai overview", "perplexity", "llm citation", "localization",
        "going global", "retention", "pmf", "loops",
    ],
    "04 创始人观点": [
        "founder", "ceo", "co-founder", "interview", "essay",
        "stratechery", "lenny", "andrew chen", "scaling", "moat",
        "distribution", "ai strategy", "leadership",
    ],
}

CATEGORY_HINT_BY_OPML = {
    "01 ai 模型 / 产品动态": "01 AI 模型 / 产品动态",
    "02 ai + 设计": "02 AI + 设计",
    "03 ai + 海外营销 (含 seo/geo/aeo)": "03 AI + 海外营销",
    "04 创始人观点": "04 创始人观点",
}

# 来源重要性评分（5=旗舰一手；4=主流厂商/垂直媒体；3=个人/二手解读）
SOURCE_IMPORTANCE: dict[str, int] = {
    "OpenAI": 5,
    "Anthropic News": 5,
    "Google DeepMind Blog": 5,
    "AWS News": 5,
    "Microsoft AI Blog": 5,
    "Hugging Face Blog": 5,
    "Figma Blog": 5,
    "Adobe Blog": 5,
    "Stratechery": 5,
    "Lenny's Newsletter": 5,
    "The Verge AI": 4,
    "TechCrunch AI": 4,
    "MIT Technology Review AI": 4,
    "UX Collective": 4,
    "Smashing Magazine": 4,
    "Frame.io Insider": 4,
    "A List Apart": 4,
    "Nielsen Norman Group": 4,
    "SaaStr": 4,
    "Marketing Brew": 4,
    "HubSpot Marketing Blog": 4,
    "Search Engine Land": 4,
    "Search Engine Journal": 4,
    "Ahrefs Blog": 4,
    "Backlinko": 4,
    "Aleyda Solis": 4,
    "MozBlog": 4,
    "a16z": 4,
    "Not Boring": 4,
    "First Round Review": 4,
    "Reforge": 4,
    "Andrew Chen": 4,
}


def parse_opml(opml_path: Path) -> list[tuple[str, str, str]]:
    tree = ET.parse(opml_path)
    root = tree.getroot()
    feeds: list[tuple[str, str, str]] = []
    for group in root.iter("outline"):
        if group.get("xmlUrl"):
            continue
        group_text = (group.get("text") or "").strip().lower()
        category = CATEGORY_HINT_BY_OPML.get(group_text)
        for item in group.findall("outline"):
            url = item.get("xmlUrl")
            if not url:
                continue
            name = item.get("text") or item.get("title") or url
            feeds.append((category or "", name, url))
    return feeds


def entry_datetime(entry) -> dt.datetime | None:
    for key in ("published_parsed", "updated_parsed", "created_parsed"):
        t = entry.get(key)
        if t:
            try:
                return dt.datetime(*t[:6], tzinfo=dt.timezone.utc)
            except Exception:
                pass
    return None


def classify(title: str, summary: str, hint_category: str) -> str | None:
    text = f"{title} {summary}".lower()
    if hint_category and hint_category in CATEGORY_KEYWORDS:
        return hint_category
    for cat, kws in CATEGORY_KEYWORDS.items():
        if any(k in text for k in kws):
            return cat
    return None


def clean_summary(html: str, max_len: int = 240) -> str:
    if not html:
        return ""
    text = re.sub(r"<[^>]+>", "", html)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > max_len:
        text = text[:max_len].rstrip() + "…"
    return text


def fetch_one(url: str, name: str) -> list[dict]:
    log.info("fetch %s (%s)", name, url)
    try:
        feed = feedparser.parse(url)
    except Exception as e:
        log.warning("  failed: %s", e)
        return []
    items: list[dict] = []
    for e in feed.entries[:25]:
        published = entry_datetime(e)
        if not published or published < CUTOFF:
            continue
        items.append({
            "title": (e.get("title") or "").strip(),
            "link": e.get("link") or "",
            "summary": clean_summary(e.get("summary") or e.get("description") or ""),
            "published": published,
            "source": name,
        })
    log.info("  +%d entries within %dd window", len(items), WINDOW_DAYS)
    return items


def iso_week_label(date: dt.datetime) -> str:
    iso = date.isocalendar()
    return f"{iso.year}-W{iso.week:02d}"


def render_markdown(buckets: dict[str, list[dict]], generated_at: dt.datetime) -> str:
    lines: list[str] = []
    lines.append(f"# 易点事务所 AI 观察 · 候选素材 {iso_week_label(generated_at)}")
    lines.append("")
    lines.append(f"> 自动生成于 {generated_at.astimezone().strftime('%Y-%m-%d %H:%M %Z')}")
    lines.append(f"> 时间窗口：最近 {WINDOW_DAYS} 天")
    lines.append("> 仅为 AI 编辑的候选素材，**未筛选未翻译未润色**。")
    lines.append("")

    for cat in (
        "01 AI 模型 / 产品动态",
        "02 AI + 设计",
        "03 AI + 海外营销",
        "04 创始人观点",
    ):
        items = buckets.get(cat, [])
        items.sort(key=lambda x: (-SOURCE_IMPORTANCE.get(x["source"], 3), -x["published"].timestamp()))
        lines.append(f"## {cat}（候选 {len(items)} 条）")
        lines.append("")
        if not items:
            lines.append("_本周窗口内未抓到候选条目，需 AI 用 WebSearch 兜底。_")
            lines.append("")
            continue
        for it in items:
            d = it["published"].astimezone().strftime("%-m/%-d")
            lines.append(f"### {it['title']} · {d}")
            lines.append(f"- 来源：{it['source']}")
            lines.append(f"- 链接：{it['link']}")
            if it["summary"]:
                lines.append(f"- 摘要：{it['summary']}")
            lines.append("")
    return "\n".join(lines)


def push_to_feishu(payload: dict, webhook_url: str) -> bool:
    try:
        req = urllib.request.Request(
            webhook_url,
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            return 200 <= resp.status < 300
    except urllib.error.HTTPError as e:
        log.warning("  feishu HTTP %s: %s", e.code, e.reason)
    except Exception as e:
        log.warning("  feishu error: %s", e)
    return False


def make_payload(item: dict, category: str, week_label: str) -> dict:
    return {
        "issue": f"#{week_label}",
        "category": category,
        "title": item["title"][:180],
        "published_at": item["published"].astimezone().strftime("%Y-%m-%d"),
        "summary": item["summary"],
        "url": item["link"],
        "source": item["source"],
        "importance": SOURCE_IMPORTANCE.get(item["source"], 3),
    }


def load_pushed(week_label: str) -> set[str]:
    p = STATE_DIR / f"{week_label}.json"
    if p.exists():
        try:
            return set(json.loads(p.read_text(encoding="utf-8")))
        except Exception:
            return set()
    return set()


def save_pushed(week_label: str, urls: set[str]) -> None:
    p = STATE_DIR / f"{week_label}.json"
    p.write_text(json.dumps(sorted(urls), ensure_ascii=False, indent=2), encoding="utf-8")


def push_buckets(buckets: dict[str, list[dict]], webhook_url: str, week_label: str) -> tuple[int, int, int]:
    if not webhook_url:
        log.info("FEISHU_WEBHOOK_URL not set, skip push")
        return 0, 0, 0
    pushed = load_pushed(week_label)
    sent, failed, skipped = 0, 0, 0
    for cat, items in buckets.items():
        items_sorted = sorted(
            items,
            key=lambda x: (-SOURCE_IMPORTANCE.get(x["source"], 3), -x["published"].timestamp()),
        )[:MAX_PER_CATEGORY]
        cat_sent = 0
        for it in items_sorted:
            link = it["link"]
            if link in pushed:
                skipped += 1
                continue
            payload = make_payload(it, cat, week_label)
            ok = push_to_feishu(payload, webhook_url)
            if ok:
                sent += 1
                cat_sent += 1
                pushed.add(link)
                save_pushed(week_label, pushed)
            else:
                failed += 1
            time.sleep(PUSH_DELAY_SECONDS)
        log.info("  %s pushed %d new (%d candidates, %d already in state)",
                 cat, cat_sent, len(items_sorted), len(items_sorted) - cat_sent - 0)
    return sent, failed, skipped


def cmd_test_feishu() -> int:
    if not FEISHU_WEBHOOK_URL:
        log.error("FEISHU_WEBHOOK_URL not set in .env")
        return 1
    payload = {
        "issue": f"#{iso_week_label(NOW)}",
        "category": "01 AI 模型 / 产品动态",
        "title": "[联路自检] Claude Code 4.6 发布：把 IDE 变成自动驾驶座舱",
        "published_at": NOW.astimezone().strftime("%Y-%m-%d"),
        "summary": "这是一条测试数据，由 ai-watch fetch.py --test-feishu 发出，用于验证 webhook 联路是否走通。可在飞书表中删除。",
        "url": "https://www.anthropic.com/news/claude-code-4-6",
        "source": "Anthropic News",
        "importance": 5,
    }
    ok = push_to_feishu(payload, FEISHU_WEBHOOK_URL)
    if ok:
        log.info("test push OK -> 去飞书表里看一条 [联路自检] 开头的记录")
        return 0
    log.error("test push FAILED")
    return 2


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-feishu", action="store_true", help="不推飞书，只出 Markdown")
    parser.add_argument("--test-feishu", action="store_true", help="只发一条测试数据到飞书")
    args = parser.parse_args()

    if args.test_feishu:
        return cmd_test_feishu()

    if not OPML_PATH.exists():
        log.error("OPML not found: %s", OPML_PATH)
        return 1

    feeds = parse_opml(OPML_PATH)
    log.info("loaded %d feeds from OPML", len(feeds))

    buckets: dict[str, list[dict]] = {k: [] for k in CATEGORY_KEYWORDS}
    seen_urls: set[str] = set()

    for hint_cat, name, url in feeds:
        for it in fetch_one(url, name):
            link = it["link"].split("#")[0]
            if link in seen_urls:
                continue
            seen_urls.add(link)
            cat = classify(it["title"], it["summary"], hint_cat)
            if not cat:
                continue
            buckets[cat].append(it)

    week_label = iso_week_label(NOW)
    output_path = OUTPUT_DIR / f"{week_label}.md"
    output_path.write_text(render_markdown(buckets, NOW), encoding="utf-8")
    log.info("wrote %s", output_path)
    log.info(
        "summary: %s",
        ", ".join(f"{k.split()[0]}={len(v)}" for k, v in buckets.items()),
    )

    if not args.no_feishu:
        sent, failed, skipped = push_buckets(buckets, FEISHU_WEBHOOK_URL, week_label)
        log.info("feishu push: sent=%d failed=%d skipped(dedup)=%d", sent, failed, skipped)

    return 0


if __name__ == "__main__":
    sys.exit(main())
