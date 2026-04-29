#!/usr/bin/env python3
"""
ai-watch fetch.py
读取 feeds.opml -> 拉每个 RSS 源 -> 过滤近 7 天 -> 按 4 大栏目关键词归类
-> 输出 Markdown 候选稿 output/YYYY-WXX.md

用法:
    pip3 install --user feedparser
    python3 fetch.py
"""

from __future__ import annotations

import re
import sys
import socket
import logging
import datetime as dt
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

try:
    import feedparser
except ImportError:
    print("[ERR] 请先安装依赖: pip3 install --user feedparser", file=sys.stderr)
    sys.exit(1)

socket.setdefaulttimeout(15)

ROOT = Path(__file__).resolve().parent
OPML_PATH = ROOT / "feeds.opml"
OUTPUT_DIR = ROOT / "output"
LOG_DIR = ROOT / "logs"
OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

NOW = dt.datetime.now(dt.timezone.utc)
WINDOW_DAYS = 7
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
        # OPML 已分组：信任 OPML，但要验证是否最少 1 个关键词命中。
        kws = CATEGORY_KEYWORDS[hint_category]
        if any(k in text for k in kws):
            return hint_category
        # 即便没命中，也保留在 hint 类别下（OPML 是人工策展过的）
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
        items.sort(key=lambda x: x["published"], reverse=True)
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


def main() -> int:
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

    output_path = OUTPUT_DIR / f"{iso_week_label(NOW)}.md"
    output_path.write_text(render_markdown(buckets, NOW), encoding="utf-8")
    log.info("wrote %s", output_path)
    log.info(
        "summary: %s",
        ", ".join(f"{k.split()[0]}={len(v)}" for k, v in buckets.items()),
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
