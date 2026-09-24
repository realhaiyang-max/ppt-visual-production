---
name: ppt-visual-production
description: Use when source material or approved slide content must become a presentation and the work needs staged approval, visual exploration, editable PPTX construction, high-resolution slide assets, or mixed image-and-native production.
---

# PPT Visual Production

## Purpose

Run an approval-gated presentation workflow while keeping approved content separate from visual treatment. Choose production media by content: images may provide scene evidence or a polished visual shell, while native PowerPoint objects preserve exact and editable information. Use existing document-reading, `imagegen`, and `Presentations` skills for their respective operations; this skill controls routing, handoffs, artifacts, and stop conditions.

## Start or Resume

Determine the requested phase and inspect available inputs before acting:

| Phase | Required input | Read |
|---|---|---|
| 1. Content planning | Source material | [Phase 1](references/phase-1-content.md) |
| 2. Visual exploration | User-approved outline or content-lock manifest | [Phase 2](references/phase-2-style-exploration.md) |
| 3. Visual production | Approved content plus selected direction montage | [Phase 3](references/phase-3-slide-rendering.md) |
| 4. PPTX construction | Locked content plus approved visual-system contract, representative slides, or slide visuals | [Phase 4](references/phase-4-pptx-reconstruction.md) |

For a full workflow, read only the current phase reference. For a resumed workflow, validate prerequisites before proceeding. Ask only for missing information that materially changes the result; reuse facts already supplied.

Before any phase writes or resumes local artifacts, read [Artifact versioning and paths](references/artifact-versioning.md). It defines the minimum collision-safe directory layout, task-wide direction labels, revisions, provenance, and delivery binding.

## Shared Rules

- Confirm slide count for every project; never assume nine pages. Confirm whether the cover is included.
- Phase transitions require explicit user approval. Never interpret silence or delivery of an artifact as approval.
- Treat the approved content as the source of truth. Do not recover exact copy from generated images when locked content exists.
- Never alter approved story, order, facts, or wording unless the user reopens them.
- Never invent data, brands, logos, people, products, interfaces, or sources.
- Reject missing pages, duplicate or incorrect page numbers, garbled text, overflow, overlap, and text ghosting.
- ImageGen handles visual composition and complex assets. Use deterministic text layout for exact titles, body copy, numbers, labels, and page numbers.
- Do not impose a deck-wide rule such as images only on the cover, native shapes on every content slide, or a fixed image count. Choose the medium from the communication need of each slide.
- Reject image pollution: unrelated image stacks, fragmented image tiles, decorative imagery without information value, repeated near-identical imagery, inconsistent visual styles, or imagery that competes with the main message.
- Visual exploration always produces exactly three structurally distinct alternatives. Differences must extend beyond color.
- Resolve required fonts before slide layout begins. Require a legitimate font source and explicit user approval before installing fonts; otherwise use a documented compatible substitute.
- Record every approval gate against an exact artifact or version, including the selected direction, production route, slide media plan, and permitted next phase. Interpret short replies only against the active gate and restate the resolved choice.
- Treat completed artifacts as immutable. A rerun or revision receives a new artifact ID and path; it does not overwrite the earlier candidate.

## Production Routes

Select the route after visual-direction approval:

| Route | Use when | Required approval artifact |
|---|---|---|
| **image-first** | Composition, atmosphere, illustration, or scene fidelity dominates | Complete individual high-resolution slide set |
| **native-first** | Editable matrices, roadmaps, processes, architecture, or management content dominates | Approved visual-system contract plus representative slides |
| **hybrid** | Slides need both a polished visual shell and editable exact information | Slide media plan plus representative slides and any generated visual assets |

The route may vary by slide. High-resolution slide images are not a mandatory intermediate for native-first or hybrid slides.

## Visual Direction Policy

Recommend three directions from this pool according to content, audience, density, and context:

- 明亮咨询报告风
- 高管战略汇报风
- 工程研发战略风
- 经营管理简报风
- 战略蓝图风

Exclude 制造业高层汇报风、专业研究报告风、现代企业年报风 and all dark-tech, cyberpunk, neon, HUD, dashboard, black-background, blue-purple glow, futuristic-city, data-stream, cosmic-grid, or glowing-wireframe directions.

## Artifact Names and Gates

Use these names precisely:

- **direction montage:** a contact sheet of ordered thumbnails used only to compare visual directions.
- **individual high-resolution slide:** one independent 16:9 image for one slide.
- **PPTX readback preview:** an image rendered from the actual PPTX after construction or finalization.

Do not call a direction montage an individual high-resolution slide set. Do not claim an artifact exists until its files have been checked and the user receives an accessible path or attachment.

Use stable slide IDs and preserve page order across artifacts:

1. `outline` and `content-lock.json` → stop for outline approval.
2. Three complete direction montages → stop for visual-direction selection.
3. Production route, slide media plan, and route-appropriate visual proof → stop for visual-system approval.
4. Complete draft PPTX and PPTX readback preview → stop for whole-deck approval.
5. One current delivery PPTX, final PPTX readback preview, and editability report → final delivery.

When files are available, use the bundled scripts to validate manifests, assemble montages, and check slide-image sequences. A successful export is not completion; inspect the rendered result.
