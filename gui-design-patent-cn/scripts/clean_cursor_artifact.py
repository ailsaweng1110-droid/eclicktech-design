#!/usr/bin/env python3
"""
通用截图清理 — 把官网/App 截图里的鼠标光标、悬停残影、重复按钮等"瞬时 UI 噪点"
用同色背景采样无缝覆盖，避免污染 GUI 外观设计专利的状态图。

典型用法：

  ## 模式 1：从外部 JSON 配置批量清理
  适合一次性需要清掉多处残影：

      python clean_cursor_artifact.py \
        --input  ./assets/原图.png \
        --patches ./clean-patches.json \
        --output ./assets/原图-clean.png

  patches.json 示例：
  {
    "patches": [
      {
        "name": "navbar_cursor",
        "target":  [3035, 50, 3110, 135],   # x0,y0,x1,y1 要替换的区域
        "sample":  [1800, 50, 1875, 135]    # 同尺寸的干净采样区域
      }
    ]
  }

  ## 模式 2：单次命令行清理
  适合临时只清一处：

      python clean_cursor_artifact.py \
        --input ./assets/原图.png \
        --target 3035,50,3110,135 \
        --sample 1800,50,1875,135 \
        --output ./assets/原图-clean.png

依赖：Pillow（见 ../requirements.txt）。
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

from PIL import Image


@dataclass(frozen=True)
class Patch:
    name: str
    target: tuple[int, int, int, int]
    sample: tuple[int, int, int, int]


def _parse_box(text: str) -> tuple[int, int, int, int]:
    parts = [int(x.strip()) for x in text.split(",")]
    if len(parts) != 4:
        raise ValueError(f"box 必须形如 'x0,y0,x1,y1'，收到：{text!r}")
    x0, y0, x1, y1 = parts
    if x1 <= x0 or y1 <= y0:
        raise ValueError(f"box 必须满足 x1>x0 且 y1>y0，收到：{parts}")
    return (x0, y0, x1, y1)


def load_patches(config_path: Path) -> list[Patch]:
    raw = json.loads(config_path.read_text(encoding="utf-8"))
    items = raw.get("patches")
    if not isinstance(items, list) or not items:
        raise ValueError("配置必须包含非空数组 patches[]")
    out: list[Patch] = []
    for i, p in enumerate(items, start=1):
        if not isinstance(p, dict):
            raise ValueError(f"patches[{i-1}] 必须是对象")
        name = str(p.get("name") or f"patch{i}")
        t = p.get("target")
        s = p.get("sample")
        if not isinstance(t, list) or len(t) != 4 or not isinstance(s, list) or len(s) != 4:
            raise ValueError(f"patches[{i-1}] target/sample 必须各是 4 元素整型数组")
        out.append(Patch(name=name, target=tuple(int(x) for x in t), sample=tuple(int(x) for x in s)))  # type: ignore[arg-type]
    return out


def apply_patches(im: Image.Image, patches: list[Patch], *, verbose: bool = True) -> Image.Image:
    """对图像应用所有 patch；返回新图像（不修改输入）。"""
    out = im.copy()
    for p in patches:
        sample = im.crop(p.sample)
        tw = p.target[2] - p.target[0]
        th = p.target[3] - p.target[1]
        if sample.size != (tw, th):
            sample = sample.resize((tw, th), Image.LANCZOS)
        out.paste(sample, (p.target[0], p.target[1]))
        if verbose:
            print(f"  + patch '{p.name}'  target={p.target}  sample={p.sample}", file=sys.stderr)
    return out


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="截图残影清理（鼠标光标 / 悬停态 / 重复按钮）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument("--input", required=True, help="源截图路径")
    p.add_argument("--output", required=True, help="清理后输出路径")

    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--patches", help="JSON 配置（批量模式）")
    g.add_argument("--target", help="单次模式：要替换的区域 'x0,y0,x1,y1'")

    p.add_argument("--sample", help="单次模式：干净采样区域 'x0,y0,x1,y1'（与 --target 同尺寸或可缩放）")
    p.add_argument("--name", default="patch1", help="单次模式：patch 名（仅用于日志）")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    src = Path(args.input).expanduser().resolve()
    out_path = Path(args.output).expanduser().resolve()
    if not src.is_file():
        print(f"找不到源图：{src}", file=sys.stderr)
        return 2

    if args.patches:
        patches = load_patches(Path(args.patches).expanduser().resolve())
    else:
        if not args.sample:
            print("--target 必须配合 --sample", file=sys.stderr)
            return 2
        patches = [Patch(name=args.name, target=_parse_box(args.target), sample=_parse_box(args.sample))]

    im = Image.open(src).convert("RGB")
    out = apply_patches(im, patches)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out.save(out_path, "PNG", optimize=True)
    print(f"已写：{out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
