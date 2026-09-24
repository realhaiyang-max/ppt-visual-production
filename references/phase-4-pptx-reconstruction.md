# Phase 4: Hybrid Editable PPTX Reconstruction

## Prerequisites

Require locked content plus an approved visual-system contract and route-appropriate proof: a complete high-resolution slide set for image-first work, or approved representative slides and slide media plan for native-first or hybrid work. Use the `Presentations` skill and its template-following, visual-design, native-evidence, and finalization guidance.

## Layer Strategy

For each slide, separate:

- **Editable information layer:** titles, subtitles, paragraphs, quotations, key figures, keywords, conclusions, notes, section names, footers, page numbers, simple shapes, dividers, tables, and basic charts.
- **Complex visual layer:** photographs, illustrations, textures, visual baseplates, complex diagrams or charts, material effects, and other areas whose native reconstruction would materially reduce quality.

Do not flatten the whole slide. Remove or cover source-image text before adding native text so no ghosting remains. Use the content lock rather than OCR for exact copy.

## Font Preflight Gate

Complete font preflight before rebuilding slide layouts:

1. Inventory fonts declared by any source template and identify the font character, family, weight, width, and script needs visible in the approved slide references.
2. Check installed families and weights plus glyph coverage for all required Chinese, Latin, numeric, punctuation, and symbol text.
3. Create a font mapping from each intended role to the actual family and weight used in the PPTX.
4. If an exact font is already installed and licensed for the work, use it. If the user provides a legitimate source or an authorized public source exists, request explicit user approval before installing the font.
5. When the exact font is unavailable or its license is unclear, choose an installed substitute with similar metrics and visual character. Do not download or install a font from an unverified source.
6. Resolve installation or substitution before positioning text. A later font change requires text reflow and layout review.
7. Re-render the complete deck after any font installation or substitution; check line breaks, overflow, title width, numeric alignment, mixed-language text, and whether requested bold or italic styles actually exist.
8. When font or application compatibility remains uncertain and the relevant app is available, inspect the rendered result in PowerPoint or WPS. Computer Use is conditional for this check, not a mandatory dependency.

## Reconstruction and Review

1. Match the approved composition, proportions, visual emphasis, colors, crops, spacing, hierarchy, and reading order.
2. Rebuild required text as native PowerPoint text and preserve emphasis, punctuation, units, and line breaks.
3. Rebuild simple evidence as editable objects when quality is preserved.
4. Retain complex visual regions as high-resolution image assets when editability would materially reduce fidelity.
5. Render the PPTX and compare every slide with the approved reference at a consistent size.
6. Fix material differences, overflow, overlap, incorrect fonts, ghosting, missing elements, and page-number errors.

## Diagram and Alignment QA

For matrices, process diagrams, organization charts, architecture diagrams, and timelines, inspect at full size or magnified view:

- connector endpoints attach to the intended objects;
- lines intended as horizontal and vertical are geometrically straight;
- peer modules align and use consistent spacing;
- arrows follow the intended reading order;
- connectors do not cross text or unintended shapes;
- visual baseplate cells and native text align to the same grid;
- layering does not hide labels, markers, or connectors.

## Post-Finalization Readback

After every finalization, font change, package rewrite, or conversion, render the complete actual PPTX again. Check every slide, with special attention to short labels, years, numbers, units, title line counts, changed text wrapping, connector movement, missing elements, and page order. A preview rendered before the finalization step is not final evidence.

## Delivery

Embed all required image assets in the PPTX; the delivered file must not depend on absolute local paths. Reopen the final PPTX after saving to confirm that it is readable and retains its slide count and embedded assets.

Deliver one current delivery file, its post-finalization PPTX readback preview, and a concise editability report listing native text/shapes/charts, image-based assets and visual baseplates, any text retained inside complex images, intentional editability trade-offs, fonts used and substitutions, substitution reasons, recipient font requirements, and known PowerPoint/WPS compatibility caveats. Record the final PPTX SHA-256 as `source_pptx_sha256` in the readback artifact manifest. Move superseded candidates to an intermediate or archive location so multiple files cannot plausibly appear to be the current final. Do not claim completion from export alone.
