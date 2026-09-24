# Phase 2: Three-Way Visual Exploration

## Prerequisite

Require an explicitly approved outline or valid content-lock manifest. Resolve contradictions before generating visuals.

## Direction Selection

Analyze theme, audience, industry, information density, narrative rhythm, and chart needs. Recommend exactly three structurally distinct directions from the approved style pool in `SKILL.md`. Briefly state why each fits, then stop for user approval of the proposed directions.

Assign the current round's three task-wide direction labels according to `artifact-versioning.md`: A/B/C for the first round, D/E/F for the second, and so on. Do not restart the labels at A when the same task opens a new exploration round.

For each direction, state the intended balance among photography, illustration, native diagrams, charts, and hybrid composition. Do not encode a blanket rule such as cover-only imagery or imagery on every slide.

## Provisional Slide Media Plan

Before producing montages, create a provisional slide media plan for every slide. Record:

- communication purpose and visual evidence needed;
- proposed medium: photograph, product image, illustration, chart, native diagram, visual baseplate, or hybrid;
- information that must remain native and editable;
- the role of any image asset;
- image pollution risk and how the layout keeps one clear visual hierarchy.

The plan is provisional until a direction is selected, but the three directions must reveal materially different media use when appropriate.

## Montage Generation

After approval:

1. Use `imagegen` for composition, complex imagery, and visual language only where it improves the communication purpose.
2. Create one complete montage for each direction; each must contain every slide in correct order as a 16:9 thumbnail.
3. Make the alternatives differ in density, title treatment, module organization, chart language, image use, and visual emphasis—not merely palette.
4. Keep one coherent system within each montage: typography hierarchy, palette, background, charts, icons, modules, footer, and page numbers.
5. Overlay exact approved text deterministically. Do not rely on generated Chinese text for titles, numbers, labels, or page numbers.
6. Do not add unapproved data, brands, logos, people, products, or sources.
7. Use `scripts/build_montage.py` when individual thumbnails need deterministic assembly.

## Image Pollution Gate

Reject a direction when it depends on unrelated image stacks, fragmented image tiles, decorative imagery without information value, repeated near-identical imagery, inconsistent photography or illustration styles, or images that compete with the slide's core message. A coherent single visual baseplate is not image pollution merely because it is image-based.

## Validation and Gate

Confirm that all three montages contain the same complete page sequence and remain legible enough to compare hierarchy, key charts, image density, and editability intent. Deliver the current round's three task-wide direction labels with minimal explanation, then stop for explicit selection of one direction.
