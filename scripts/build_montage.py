#!/usr/bin/env python3
import argparse
import math
import re
import sys
from pathlib import Path

from PIL import Image


EXTENSIONS = {".png", ".jpg", ".jpeg"}


def natural_key(path):
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", path.name)]


def main():
    parser = argparse.ArgumentParser(description="Assemble slide images into a montage.")
    parser.add_argument("input_dir", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--columns", type=int, default=3)
    args = parser.parse_args()
    if args.columns < 1:
        parser.error("--columns must be at least 1")
    if args.output.exists():
        print(f"output already exists: {args.output}", file=sys.stderr)
        return 1
    paths = sorted(
        (path for path in args.input_dir.iterdir() if path.suffix.lower() in EXTENSIONS),
        key=natural_key,
    )
    if not paths:
        print("no PNG or JPEG slide images found", file=sys.stderr)
        return 1

    with Image.open(paths[0]) as first:
        tile_size = first.size
    rows = math.ceil(len(paths) / args.columns)
    montage = Image.new("RGB", (tile_size[0] * args.columns, tile_size[1] * rows), "white")
    for index, path in enumerate(paths):
        with Image.open(path) as source:
            tile = source.convert("RGB")
            if tile.size != tile_size:
                tile = tile.resize(tile_size, Image.Resampling.LANCZOS)
            x = (index % args.columns) * tile_size[0]
            y = (index // args.columns) * tile_size[1]
            montage.paste(tile, (x, y))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    montage.save(args.output)
    print(f"Montage created: {args.output} ({len(paths)} slides)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
