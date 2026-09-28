---
name: ppt-visual-production
description: Use when source material or approved slide content must become a presentation and the work needs staged approval, ImageGen visual exploration, high-resolution slide references, or fidelity-first editable PPTX reconstruction.
---

# PPT Visual Production

## Purpose

Run an approval-gated workflow from source content to a polished PPTX. Keep approved content authoritative while allowing ImageGen to design text, charts, imagery, and composition together. During reconstruction, preserve visual fidelity first and make the main text editable without forcing complex visuals into low-quality native PowerPoint objects.

## Start or Resume

Identify the active phase and read only its reference:

| Phase | Required input | Reference |
|---|---|---|
| 1. Content planning | Source material | [Phase 1](references/phase-1-content.md) |
| 2. Visual exploration | Approved outline or content lock | [Phase 2](references/phase-2-style-exploration.md) |
| 3. Visual production | Locked content and selected montage | [Phase 3](references/phase-3-slide-rendering.md) |
| 4. PPTX reconstruction | Approved visual proof and locked content | [Phase 4](references/phase-4-pptx-reconstruction.md) |

Before writing or resuming artifacts, read [Artifact versioning and paths](references/artifact-versioning.md). Validate prerequisites and reuse confirmed facts; ask only about missing choices that materially change the result.

## Invariants

- Confirm the slide count for each project and whether it includes the cover.
- Stop at every phase gate for explicit approval. Bind approval to an exact artifact version.
- The approved outline and `content-lock.json` control words, facts, order, and page count. Generated images are visual references, not a copy source.
- ImageGen may create text-inclusive slides and charts so typography and visual composition develop together. Validate generated words against the content lock instead of trusting OCR.
- Prefer visual fidelity over blanket editability. Do not force photographs, illustrations, complex charts, diagrams, textures, or effects into native PowerPoint objects when quality would materially decline.
- Rebuild main titles, subtitles, body copy, slogans, key statements, figures, keywords, conclusions, notes, footers, and page numbers as editable native text. Only bounded small text inside inseparable complex visuals may remain image-based and must be disclosed.
- Never invent data, brands, logos, people, products, interfaces, or sources.
- Reject missing pages, wrong order, duplicate page numbers, garbled text, overflow, overlap, ghosting, and inconsistent visual systems.
- Visual exploration produces exactly three structurally distinct alternatives; differences must go beyond palette.
- Avoid image pollution: unrelated image stacks, fragmented decorative tiles, repeated near-identical imagery, or visuals that compete with the message.
- Resolve required fonts before slide layout begins. Require explicit user approval before installing fonts from a legitimate source; otherwise document a compatible substitute.
- Completed artifacts are immutable. Revisions receive new IDs and paths.

## Production Routes

Choose after a visual direction is approved:

| Route | Use when | Approval proof |
|---|---|---|
| **visual-first (image-first)** | The selected design's composition and finish should control reconstruction; this is the default fidelity route | Complete high-resolution visual reference set |
| **native-first** | The user explicitly prioritizes deep editability and native construction can retain the approved quality | Visual-system contract and representative slides |
| **hybrid** | Some slides need complete visual references while others can be built directly from native and image assets | Slide media plan and route-appropriate representative slides or references |

Routes may vary by slide. Native reconstruction is a quality decision, not a requirement imposed by content type.

## Visual Direction Policy

Select three directions suited to the topic, audience, density, and narrative from:

- 明亮咨询报告风
- 高管战略汇报风
- 工程研发战略风
- 经营管理简报风
- 战略蓝图风

Exclude dark-tech, cyberpunk, neon, HUD, dashboard, black-background, blue-purple glow, futuristic-city, data-stream, cosmic-grid, glowing-wireframe, and similar technology-show directions. Do not use 制造业高层汇报风、专业研究报告风、现代企业年报风 as separate named directions.

## Artifact Names and Gates

- **direction montage:** ordered thumbnails of the complete deck used to select a visual direction.
- **individual high-resolution slide:** one independently generated 16:9 visual reference for one slide.
- **complete high-resolution visual reference set:** one independently generated 16:9 reference image per slide.
- **PPTX readback preview:** images rendered from the actual PPTX after construction or finalization.

Do not confuse these artifacts or claim one exists before its files are checked and delivered through an accessible path or attachment.

Use stable slide IDs and preserve page order:

1. `outline` and `content-lock.json` → outline approval.
2. Three complete direction montages → visual-direction selection.
3. Route, slide media plan, and route-appropriate visual proof → visual-system approval.
4. Complete draft PPTX and PPTX readback preview → whole-deck approval.
5. One current delivery PPTX, final readback preview, and editability report → final delivery.

Use the bundled validators and montage tools when applicable. Export alone is not completion; inspect the rendered result.
