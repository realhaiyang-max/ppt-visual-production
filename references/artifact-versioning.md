# Artifact Versioning and Paths

Read this before writing, revising, or resuming presentation artifacts. The objective is to prevent collisions without turning the workspace into a version-control system.

## Minimum Path Layout

Use short ASCII directory keys on Windows; keep human-readable names inside manifests when needed.

```text
work/
  round-01/
    A/
      revision-01/
        assets/
        slides/
        montage.png
        artifact.json
approved/
  content-lock-v01.json
  gates.json
delivery/current/
  deck.pptx
  readback.png
  editability.md
  artifact.json
archive/
```

Each revision directory contains only files produced for that artifact. Never assemble a montage or slide set from a shared directory containing files from another revision.

## Round, Direction, and Revision IDs

- A new three-way exploration uses the next task-wide labels: round 1 uses A/B/C, round 2 uses D/E/F, round 3 uses G/H/I. Continue alphabetically; after Z use AA, AB, and AC.
- A refinement of one existing direction keeps its label and increments the revision: `R01-B-v01`, `R01-B-v02`.
- A genuinely new set of three alternatives consumes the next three direction labels rather than reusing A/B/C.
- Reserve the round directory before writing. If the intended path already exists, allocate the next round or revision. Completed, reviewed, approved, or delivered artifacts must not overwrite earlier files.

## Artifact Manifest

Every approval candidate and delivery artifact needs an `artifact.json` containing at least:

```json
{
  "artifact_id": "R02-E-v01",
  "status": "complete",
  "content_lock_path": "approved/content-lock-v03.json",
  "content_lock_sha256": "...",
  "parent_artifacts": ["R01-B-v02"],
  "files": ["montage.png"],
  "source_pptx_sha256": null
}
```

Use `source_pptx_sha256` for a PPTX readback preview so the preview can be proven to come from the delivered deck. Keep it `null` for artifacts that are not derived from a PPTX.

## State and Approval Rules

- Write incomplete work inside its new revision directory and keep its status `incomplete`; only validated artifacts become `complete`.
- `approved/gates.json` records the exact artifact ID approved at each gate. A reply such as “E” resolves to the unique task-wide direction E and its displayed revision.
- A new content-lock version invalidates dependent downstream approvals. Reuse unaffected pages only after recording their parent artifact IDs under the new content-lock hash.
- Resume from the latest approved gate, not from the newest file timestamp.
- `delivery/current/` contains one current delivery set. Move superseded delivery candidates to `archive/`; do not delete approved history merely to avoid a naming collision.
