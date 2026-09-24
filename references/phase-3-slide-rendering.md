# Phase 3: Route Selection and Visual Production

## Prerequisites

Require locked content and an explicitly selected direction montage. The montage controls the visual direction; locked content controls words and facts.

## Visual-System Contract

Before generating pages, record the selected system: palette, font character and hierarchy, margins, grid, module geometry, chart and icon style, background treatment, footer, page numbers, density, and recurring motifs.

Finalize the slide media plan and choose image-first, native-first, or hybrid for the deck or for each slide. Record which elements are native, image-based, or mixed.

## Route Rules

- **image-first:** generate every page as one independent high-resolution 16:9 image in page order, then obtain whole-set approval before PPTX reconstruction.
- **native-first:** build representative slides with native PowerPoint objects; do not create full-slide images merely to satisfy a stage artifact.
- **hybrid:** create only the image assets or visual baseplates required by the slide media plan, then combine them with native information layers in representative slides.

For native-first and hybrid routes, produce three to five representative slides covering the cover, a normal content slide, a complex diagram or matrix, a dense slide, and an image-plus-native slide when applicable. Stop for approval before full-deck construction.

Treat each proof as a reconstruction of the selected direction, not a fresh redesign. Preserve deliberate page-to-page variation while maintaining the shared visual system. If a montage detail is unclear, follow the locked content and visual relationships without inventing precise data.

## Hybrid Visual Baseplates

A visual baseplate may provide matrix shells, architecture frames, materials, depth, lighting, textures, or illustration that native shapes cannot reproduce at the required quality.

- A visual baseplate must not contain exact text, labels, numbers, business data, page numbers, or other content that must remain accurate or editable.
- Reserve explicit text-safe zones and align them to the PowerPoint placement grid.
- Generate the baseplate at least two times the final displayed pixel dimensions.
- Use one coherent baseplate rather than many unrelated image fragments when that preserves the intended composition.
- Keep titles, labels, figures, conclusions, and frequently changed markers in the native information layer.
- Record the intentional editability trade-off for delivery.

## Validation and Gate

For image-first work, run `scripts/check_slide_outputs.py`; check sequence, count, 16:9 ratio, page numbers, exact titles, key numbers, text fit, and style continuity. Deliver the complete individual high-resolution slide set through an accessible path or attachment.

For native-first or hybrid work, deliver the representative slides and their readback previews. Stop until the user explicitly approves the visual-system contract and route-appropriate proof for full PPTX construction.
