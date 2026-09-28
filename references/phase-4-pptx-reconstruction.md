# Phase 4: Fidelity-First Editable PPTX Reconstruction

## Prerequisites

Require locked content, an approved visual-system contract, and route-appropriate proof: a complete high-resolution visual reference set for visual-first slides or approved representative slides and media plan for native-first or hybrid slides. Use the `Presentations` skill for PPTX construction and finalization.

## Three-Layer Reconstruction

Treat each visual-first slide as three coordinated layers:

1. **Reference master:** the approved complete slide image. Use it for proportions, placement, typography character, effects, and visual comparison; it is not a visible final slide layer.
2. **Text-free visual base layer:** preserve photography, illustration, complex chart geometry, diagrams, textures, depth, lighting, and effects while removing or covering text that will be rebuilt. Use image editing, regeneration, cropping, or local masks according to which method best preserves visual fidelity.
3. **Native text top layer:** rebuild the main text from the content lock at the mapped positions. Never use OCR or generated wording as the copy authority, and remove source text sufficiently to prevent ghosting.

If removing embedded text would visibly damage a complex region, keep that bounded region image-based and disclose any retained text. Do not flatten the whole slide merely because one region cannot be separated.

## Text Roles

Classify text by communication role, semantics, position, isolation, and visual emphasis, not by font size alone:

- **Display text:** title, slogan, key statement, quotation, and conclusion. Match font character, weight, width, tracking, line breaks, color, and spatial emphasis as closely as the available fonts allow.
- **Emphasis text:** key figure, emphasized word, short label, and status marker. Preserve size contrast, color, alignment, and relationship to the visual evidence.
- **Body text:** paragraphs and explanatory bullets. Microsoft YaHei may be the stable default unless the approved design requires another compatible installed font.
- **Auxiliary text:** chart label, note, section name, footer, and page number. Keep native when practical and align precisely with the visual base.

Use the content hierarchy and the Phase 3 text-role map to distinguish slogans and key statements from body copy. Ask only when an ambiguity would change meaning or materially alter the approved emphasis.

## Fidelity-Based Object Decisions

- Main titles, subtitles, body copy, slogans, key statements, figures, keywords, conclusions, notes, footers, and page numbers must be native and editable. The bounded complex-region exception applies only to small embedded text whose removal would materially damage the approved visual.
- Rebuild simple shapes, dividers, tables, or charts natively only when the result retains the approved visual fidelity.
- A photograph, illustration, complex chart, matrix, process, architecture diagram, texture, material effect, or composed visual region may remain image-based when native recreation would lower quality.
- Do not replace approved visual language with default PowerPoint icons, charts, shadows, or template cards merely to increase editability.
- Preserve the original composition, proportions, crops, spacing, hierarchy, reading order, contrast, and depth.

## Font Preflight Gate

Before positioning text:

1. Inventory intended font character, family, weight, width, and script needs from the approved references.
2. Check installed families, real weights, and glyph coverage for Chinese, Latin, numbers, punctuation, and symbols.
3. Create a font mapping for every text role.
4. Use an exact installed and licensed font when available. Installing a font from a legitimate source requires explicit user approval.
5. Otherwise choose an installed substitute with similar metrics and character; do not use an unverified source.
6. After any font installation or substitution, reflow the text and Re-render the complete deck. Check line breaks, overflow, title width, tracking, numeric alignment, mixed-language text, and actual bold or italic availability.
7. When compatibility remains uncertain and the app is available, inspect the result in PowerPoint or WPS.

## Reconstruction QA

Render every slide from the actual PPTX and compare it with the reference master at a consistent size. Correct material differences in scale, spacing, color, hierarchy, crops, font character, line breaks, layering, ghosting, and page numbers.

For any native or mixed matrix, process, organization chart, architecture diagram, or timeline, inspect at full size:

- connector endpoints attach to the intended objects;
- horizontal and vertical lines are geometrically straight;
- peer modules align with consistent spacing;
- arrows follow the intended reading order;
- connectors do not cross text or unrelated shapes;
- base-layer cells and native labels share one grid;
- layering does not hide labels, markers, or connectors.

## Post-Finalization and Delivery

After every finalization, font change, package rewrite, or conversion, render the complete actual PPTX again. Check short labels, years, numbers, units, title line counts, wrapping, connector movement, missing elements, and page order. A preview made before finalization is not final evidence.

Embed all assets; the delivered PPTX must not depend on absolute local paths. Reopen it after saving to confirm readability, slide count, and embedded assets.

Deliver one current delivery file, its post-finalization PPTX readback preview, and an editability report listing:

- native text, shapes, tables, and charts;
- image-based assets, complete or partial visual base layers, and any complex chart allowed to remain image-based;
- text retained inside complex images;
- intentional visual fidelity versus editability trade-offs;
- fonts used and substitutions, reasons, recipient requirements, and PowerPoint/WPS caveats.

Record the final PPTX SHA-256 as `source_pptx_sha256` in the readback manifest. Move superseded delivery candidates to the intermediate or archive location. Export alone is not completion.
