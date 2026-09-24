# Phase 1: Content Planning

## Inputs

- Source documents or pasted material
- Purpose, audience, permitted scope, and any template or brand constraints
- User-confirmed slide count, including whether the cover counts

Use the relevant document skill to inspect source files read-only. Do not modify originals.

## Source Tool Routing

Use the matching available capability for each source type:

| Source | Preferred capability |
|---|---|
| Word or DOCX | Documents |
| PDF | PDF |
| XLSX, XLS, CSV, or TSV | Spreadsheets |

For pasted text, images, or another supported local format, use the most direct available reader. A missing optional plugin must not block the workflow when the source can be inspected safely through an existing capability.

## Work

1. Identify the narrative required by the source and audience.
2. Ask only for unresolved choices that would materially change the deck.
3. Produce one entry per slide with: stable ID, page number, title, core viewpoint, body points, and visual recommendation.
4. Keep evidence traceable to the provided material. Mark genuine gaps instead of inventing content.
5. Check that the cover is page 1 when requested and that the total matches the confirmed count.

## Approval Gate

Deliver only the outline and page-by-page content. State that no PPTX or visual montage has been created. Stop until the user explicitly approves or revises the outline.

After approval, save a new immutable content-lock version such as `content-lock-v01.json`. If approved content changes, increment the version instead of overwriting the existing file. Downstream artifacts must record the exact content-lock path and SHA-256 hash.

Use this minimum shape:

```json
{
  "title": "Deck title",
  "slide_count": 2,
  "slides": [
    {
      "id": "s01",
      "page": 1,
      "title": "Exact title",
      "core_viewpoint": "Exact approved viewpoint",
      "body_points": ["Exact approved point"],
      "visual_recommendation": "Cover composition",
      "protected_facts": []
    }
  ]
}
```

Run `scripts/validate_manifest.py` when a JSON manifest is created.
