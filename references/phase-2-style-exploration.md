# Phase 2: Three-Way Visual Exploration

## Prerequisite

Require an explicitly approved outline or valid content lock. Resolve contradictions before generating visuals.

## Select Directions

Analyze the theme, audience, industry, information density, narrative rhythm, and chart needs. Select exactly three structurally distinct directions from the approved pool in `SKILL.md`. Generate the three montages in the same phase; the user selects a direction after seeing them.

Use task-wide direction labels from `artifact-versioning.md`: A/B/C for the first round, D/E/F for the second, and so on. A refinement keeps its label and increments its revision.

## Plan the Deck

For every slide, record its communication purpose, dominant visual evidence, likely image/native split during later reconstruction, and image pollution risk. This slide media plan guides exploration without forcing a native chart, a fixed image count, or the same composition on every page.

## Generate Text-Inclusive Montages

After confirming the prerequisite:

1. Give ImageGen the exact locked content and generate the complete slide design as a text-inclusive composition; typography, charts, imagery, and layout should be designed together.
2. Produce one complete montage per direction. Every montage contains every slide in correct order, with each thumbnail representing a 16:9 page.
3. Make the directions differ in density, title treatment, module organization, chart language, image use, visual emphasis, and page rhythm—not merely color.
4. Keep one coherent system inside each montage: typography hierarchy, palette, background, charts, icons, modules, footer, and page numbers.
5. Keep titles, key figures, main chart relationships, and page structure legible enough to compare. Regenerate material garbling or incorrect content; the content lock remains authoritative.
6. Do not add unapproved data, brands, logos, people, products, or sources.

Use `scripts/build_montage.py` only when independently generated thumbnails need deterministic assembly; do not substitute a generic native layout merely to make text easier to render.

## Quality Gate

Reject unrelated image stacks, decorative fragments without information value, repeated near-identical imagery, inconsistent visual languages, or imagery that competes with the core message.

Confirm all three montages contain the same full page sequence and are legible enough to compare hierarchy, charts, image density, and rhythm. Deliver the three current direction labels with minimal explanation, then stop for explicit selection.
