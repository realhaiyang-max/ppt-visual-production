# Phase 3: Visual Production

## Prerequisites

Require locked content and an explicitly selected direction montage. The montage controls the visual system; the content lock controls exact words and facts.

## Freeze the Visual System

Record palette, font character and hierarchy, margins, grid, module geometry, chart and icon language, background treatment, footer, page numbers, density, and recurring motifs. Finalize the slide media plan and select visual-first, native-first, or hybrid for the deck or each slide.

For later reconstruction, create a text-role map for each slide. Record every text item as a title, slogan, key statement, emphasized word, key figure, body, chart label, note, footer, or page number, together with its exact locked copy, approximate position, alignment, and styling cues.

## Route Rules

- **visual-first:** Recreate every montage page as one complete high-resolution visual reference. Generate each page independently at 16:9; do not enlarge or crop a montage thumbnail. Include the approved text, charts, labels, and page number so the single-page reference preserves the intended typography and composition.
- **native-first:** Build three to five representative slides with native PowerPoint objects only when that route can retain the approved finish.
- **hybrid:** Produce complete visual references for slides whose composition needs them and only the required image assets or representative slides for the rest.

Every output reconstructs the selected direction rather than redesigning it. Preserve deliberate page-to-page variation inside one coherent system. If montage detail is unclear, follow the locked content and visible relationships without inventing precise data.

## Reconstruction Inputs

The complete high-resolution visual reference is the comparison master for a visual-first slide. It may contain all approved text and complex charts. It is not the final editable layer and must not become the sole flattened slide in the PPTX.

When practical, generate a coordinated clean visual asset or text-free variant from the same reference. This is optional at this phase because Phase 4 may instead remove or cover text locally during reconstruction.

## Validation and Gate

For every complete reference set, run `scripts/check_slide_outputs.py` and check sequence, count, 16:9 ratio, exact titles, key figures, chart relationships, page numbers, text fit, and style continuity. Review the set as a whole rather than approving isolated pages.

For native-first work, deliver the visual-system contract and representative slide readbacks. For hybrid work, deliver the route-appropriate combination of references and representative slides. Stop until the user explicitly approves the proof for PPTX construction.
