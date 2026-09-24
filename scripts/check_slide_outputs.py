#!/usr/bin/env python3
import argparse
import re
import sys
from pathlib import Path

from PIL import Image, UnidentifiedImageError


EXTENSIONS = {".png", ".jpg", ".jpeg"}


def natural_key(path):
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", path.name)]


def page_number(path):
    matches = re.findall(r"\d+", path.stem)
    return int(matches[-1]) if matches else None


def main():
    parser = argparse.ArgumentParser(description="Check a numbered set of 16:9 slide images.")
    parser.add_argument("input_dir", type=Path)
    parser.add_argument("--expected", type=int, required=True)
    parser.add_argument("--ratio-tolerance", type=float, default=0.002)
    args = parser.parse_args()
    paths = sorted(
        (path for path in args.input_dir.iterdir() if path.suffix.lower() in EXTENSIONS),
        key=natural_key,
    )
    errors = []
    if len(paths) != args.expected:
        errors.append(f"count mismatch: expected {args.expected}, found {len(paths)}")
    actual_pages = [page_number(path) for path in paths]
    expected_pages = list(range(1, args.expected + 1))
    if actual_pages != expected_pages:
        errors.append(f"page sequence mismatch: expected {expected_pages}, found {actual_pages}")

    target_ratio = 16 / 9
    for path in paths:
        try:
            with Image.open(path) as image:
                width, height = image.size
                image.verify()
        except (OSError, UnidentifiedImageError) as exc:
            errors.append(f"unreadable image {path.name}: {exc}")
            continue
        if height == 0 or abs(width / height - target_ratio) > args.ratio_tolerance:
            errors.append(f"16:9 aspect ratio required: {path.name} is {width}x{height}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Slide outputs valid: {len(paths)} images")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
