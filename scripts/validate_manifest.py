#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path


REQUIRED_SLIDE_FIELDS = (
    "id",
    "page",
    "title",
    "core_viewpoint",
    "body_points",
    "visual_recommendation",
)


def validate(data):
    errors = []
    slides = data.get("slides")
    declared = data.get("slide_count")
    if not isinstance(slides, list) or not slides:
        return ["slides must be a non-empty list"]
    if declared != len(slides):
        errors.append(f"slide_count {declared!r} does not match {len(slides)} slides")

    ids = []
    pages = []
    for index, item in enumerate(slides, start=1):
        if not isinstance(item, dict):
            errors.append(f"slide {index} must be an object")
            continue
        for field in REQUIRED_SLIDE_FIELDS:
            value = item.get(field)
            if value is None or value == "" or value == []:
                errors.append(f"slide {index} is missing required field {field}")
        ids.append(item.get("id"))
        pages.append(item.get("page"))

    duplicate_ids = sorted({value for value in ids if value is not None and ids.count(value) > 1})
    duplicate_pages = sorted({value for value in pages if value is not None and pages.count(value) > 1})
    if duplicate_ids:
        errors.append(f"duplicate slide IDs: {duplicate_ids}")
    if duplicate_pages:
        errors.append(f"duplicate page numbers: {duplicate_pages}")
    expected_pages = list(range(1, len(slides) + 1))
    if pages != expected_pages:
        errors.append(f"page sequence must be {expected_pages}, got {pages}")
    return errors


def main():
    parser = argparse.ArgumentParser(description="Validate a PPT content-lock manifest.")
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"manifest read error: {exc}", file=sys.stderr)
        return 1
    errors = validate(data)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Manifest valid: {len(data['slides'])} slides")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

