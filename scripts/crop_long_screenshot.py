#!/usr/bin/env python3
"""
通用长图分段切片器 — 把官网/App/Web 整页长截图按"模块"拆成多张单张状态图，
直接套用 02界面说明.docx 的「变化状态图XX_<状态名>.jpg」命名规则。

两种调用模式：

  ## 模式 1：手动配置 — 推荐用法
  已知每个模块的 Y 起止区间和状态名，写到 crop-config.json，一键批量切。

      python crop_long_screenshot.py \
        --input  ./assets/官网长图.png \
        --segments ./crop-config.json \
        --output-dir ./dist/jpg

  ## 模式 2：自动检测 — 用于第一次摸索分界
  对长图按行采样平均色，找显著背景色突变作为候选分界点，输出一份带候选 y0/y1
  的 crop-config.draft.json，**必须由人工 review 后再切**。

      python crop_long_screenshot.py \
        --input  ./assets/官网长图.png \
        --auto-detect \
        --output-config ./crop-config.draft.json

依赖：Pillow（见 ../requirements.txt）。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from PIL import Image


# ---------- 数据结构 ----------

@dataclass(frozen=True)
class Segment:
    index: int
    name: str
    y0: int
    y1: int


def _sanitize_filename(name: str) -> str:
    name = re.sub(r'[\\/:*?"<>|\s]+', "_", name.strip())
    name = name.strip("._") or "state"
    return name[:120]


# ---------- 模式 1：按配置切片 ----------

def load_config(config_path: Path) -> tuple[list[Segment], dict[str, Any]]:
    raw = json.loads(config_path.read_text(encoding="utf-8"))
    segs_raw = raw.get("segments")
    if not isinstance(segs_raw, list) or not segs_raw:
        raise ValueError("crop-config 必须包含非空数组 segments[]")

    segments: list[Segment] = []
    for i, item in enumerate(segs_raw, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"segments[{i-1}] 必须是对象")
        idx = int(item.get("index", i))
        name = str(item.get("name", f"状态{idx:02d}")).strip()
        y0 = int(item["y0"])
        y1 = int(item["y1"])
        if y1 <= y0:
            raise ValueError(f"segments[{i-1}] '{name}' 的 y1({y1}) 必须大于 y0({y0})")
        segments.append(Segment(index=idx, name=name, y0=y0, y1=y1))

    options = {
        "target_width": int(raw.get("target_width", 1600)),
        "jpeg_quality": int(raw.get("jpeg_quality", 92)),
        "filename_prefix": str(raw.get("filename_prefix", "变化状态图")),
        "filename_separator": str(raw.get("filename_separator", "_")),
    }
    return segments, options


def crop_image(
    src_path: Path,
    segments: list[Segment],
    out_dir: Path,
    *,
    target_width: int = 1600,
    jpeg_quality: int = 92,
    filename_prefix: str = "变化状态图",
    filename_separator: str = "_",
    clear_existing: bool = True,
) -> list[Path]:
    im = Image.open(src_path).convert("RGB")
    w, h = im.size
    print(f"Source: {src_path.name}  size={w}x{h}", file=sys.stderr)

    out_dir.mkdir(parents=True, exist_ok=True)
    if clear_existing:
        for old in out_dir.glob(f"{filename_prefix}*.jpg"):
            old.unlink()

    exported: list[Path] = []
    for seg in segments:
        y0 = max(0, seg.y0)
        y1 = min(h, seg.y1)
        if y1 <= y0:
            print(f"  ! 跳过越界段 #{seg.index} '{seg.name}' y=({seg.y0},{seg.y1})", file=sys.stderr)
            continue
        crop = im.crop((0, y0, w, y1))
        if target_width and crop.width > target_width:
            ratio = target_width / crop.width
            new_size = (target_width, int(crop.height * ratio))
            crop = crop.resize(new_size, Image.LANCZOS)
        stem = _sanitize_filename(seg.name)
        fname = f"{filename_prefix}{seg.index:02d}{filename_separator}{stem}.jpg"
        out = out_dir / fname
        crop.save(out, "JPEG", quality=jpeg_quality, optimize=True)
        exported.append(out)
        print(f"  -> {fname}  ({crop.width}x{crop.height})", file=sys.stderr)

    return exported


# ---------- 模式 2：自动检测分界 ----------

def _avg_row_color(im: Image.Image, y: int, samples: int = 32) -> tuple[int, int, int]:
    w, _ = im.size
    px = im.load()
    step = max(1, w // samples)
    rs, gs, bs = 0, 0, 0
    cnt = 0
    for x in range(0, w, step):
        r, g, b = px[x, y]
        rs += r; gs += g; bs += b; cnt += 1
    return (rs // cnt, gs // cnt, bs // cnt)


def _color_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])


def detect_seams(
    src_path: Path,
    *,
    sample_step: int = 8,
    color_jump_threshold: int = 60,
    min_segment_height: int = 200,
) -> list[int]:
    """扫描行平均色，找显著背景色突变作为候选分界 Y 值。

    返回的 seam 值是"新背景色开始的那一行"——可直接作为下一段的 y0、上一段的 y1。
    """
    im = Image.open(src_path).convert("RGB")
    w, h = im.size

    seams: list[int] = [0]
    last_color = _avg_row_color(im, 0)
    last_seam = 0

    for y in range(sample_step, h, sample_step):
        c = _avg_row_color(im, y)
        if _color_distance(c, last_color) > color_jump_threshold and (y - last_seam) >= min_segment_height:
            seams.append(y)
            last_seam = y
            last_color = c
        else:
            last_color = tuple((last_color[i] * 3 + c[i]) // 4 for i in range(3))  # type: ignore[assignment]

    if seams[-1] < h - min_segment_height:
        seams.append(h)
    else:
        seams[-1] = h
    return seams


def seams_to_segments(seams: list[int]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for i in range(len(seams) - 1):
        out.append({
            "index": i + 1,
            "name": f"状态{i+1:02d}_待重命名",
            "y0": seams[i],
            "y1": seams[i + 1],
        })
    return out


def write_draft_config(out_path: Path, src_path: Path, seams: list[int]) -> None:
    config = {
        "_source_image": str(src_path),
        "_note": "自动检测的候选分界点。请人工 review 每段 y0/y1 和命名 name 后再用 --segments 切片。",
        "target_width": 1600,
        "jpeg_quality": 92,
        "filename_prefix": "变化状态图",
        "filename_separator": "_",
        "segments": seams_to_segments(seams),
    }
    out_path.write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8")


# ---------- 模式 3：分界预览图 ----------

def render_seam_preview(
    src_path: Path,
    seams: list[int],
    out_path: Path,
    *,
    thumb_width: int = 600,
) -> None:
    """生成低清预览图，在每条候选分界处画一条红线 + 序号，便于人工 review。"""
    from PIL import ImageDraw

    im = Image.open(src_path).convert("RGB")
    w, h = im.size
    ratio = thumb_width / w
    thumb = im.resize((thumb_width, int(h * ratio)), Image.LANCZOS)
    draw = ImageDraw.Draw(thumb)
    for i, y in enumerate(seams):
        y_thumb = int(y * ratio)
        draw.line([(0, y_thumb), (thumb_width, y_thumb)], fill=(255, 0, 0), width=2)
        draw.text((4, max(0, y_thumb - 12)), f"seam#{i} y={y}", fill=(255, 0, 0))
    thumb.save(out_path, "JPEG", quality=82)


# ---------- CLI ----------

def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="长图分段切片：手动配置切片 或 自动检测候选分界",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument("--input", required=True, help="源长图路径（PNG/JPG）")

    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--segments", help="crop-config.json 路径（手动配置模式）")
    g.add_argument("--auto-detect", action="store_true", help="自动检测分界并输出 draft 配置")

    p.add_argument("--output-dir", help="切片输出目录（手动模式必填）")
    p.add_argument("--output-config", help="auto-detect 模式：draft 配置写入路径")
    p.add_argument("--preview", help="可选：额外输出一张带红色分界线的预览图")

    p.add_argument("--target-width", type=int, default=1600, help="切片目标宽度（默认 1600，仅缩小不放大）")
    p.add_argument("--jpeg-quality", type=int, default=92)
    p.add_argument("--no-clear", action="store_true", help="不清理 output-dir 中已存在的同前缀文件")

    p.add_argument("--detect-threshold", type=int, default=60, help="auto-detect：背景色突变阈值（曼哈顿距离）")
    p.add_argument("--detect-min-height", type=int, default=200, help="auto-detect：最小段高度（像素）")

    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    src = Path(args.input).expanduser().resolve()
    if not src.is_file():
        print(f"找不到源图：{src}", file=sys.stderr)
        return 2

    if args.auto_detect:
        if not args.output_config:
            print("--auto-detect 需配合 --output-config", file=sys.stderr)
            return 2
        seams = detect_seams(
            src,
            color_jump_threshold=args.detect_threshold,
            min_segment_height=args.detect_min_height,
        )
        out_cfg = Path(args.output_config).expanduser().resolve()
        out_cfg.parent.mkdir(parents=True, exist_ok=True)
        write_draft_config(out_cfg, src, seams)
        print(f"已写 draft 配置：{out_cfg}")
        print(f"检测到 {len(seams)-1} 段，请人工 review 后修改 name 并精修 y0/y1。")
        if args.preview:
            preview_path = Path(args.preview).expanduser().resolve()
            render_seam_preview(src, seams, preview_path)
            print(f"已写预览图：{preview_path}")
        return 0

    if not args.segments or not args.output_dir:
        print("--segments 模式需要同时指定 --output-dir", file=sys.stderr)
        return 2

    cfg_path = Path(args.segments).expanduser().resolve()
    out_dir = Path(args.output_dir).expanduser().resolve()
    segments, options = load_config(cfg_path)

    target_width = args.target_width if args.target_width != 1600 else options["target_width"]
    jpeg_quality = args.jpeg_quality if args.jpeg_quality != 92 else options["jpeg_quality"]

    exported = crop_image(
        src,
        segments,
        out_dir,
        target_width=target_width,
        jpeg_quality=jpeg_quality,
        filename_prefix=options["filename_prefix"],
        filename_separator=options["filename_separator"],
        clear_existing=not args.no_clear,
    )
    print(f"已导出 {len(exported)} 张 -> {out_dir}")

    if args.preview:
        seams = [seg.y0 for seg in segments] + [segments[-1].y1]
        preview_path = Path(args.preview).expanduser().resolve()
        render_seam_preview(src, seams, preview_path)
        print(f"已写预览图：{preview_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
