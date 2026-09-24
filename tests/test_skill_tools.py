import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


def run_script(name, *args):
    return subprocess.run(
        [sys.executable, str(SCRIPTS / name), *map(str, args)],
        capture_output=True,
        text=True,
        check=False,
    )


def manifest(slides):
    return {"title": "Example", "slide_count": len(slides), "slides": slides}


def slide(slide_id, page, title="Title"):
    return {
        "id": slide_id,
        "page": page,
        "title": title,
        "core_viewpoint": "Viewpoint",
        "body_points": ["Point"],
        "visual_recommendation": "Visual",
        "protected_facts": [],
    }


class ValidateManifestTests(unittest.TestCase):
    def test_accepts_valid_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "manifest.json"
            path.write_text(json.dumps(manifest([slide("s01", 1)])), encoding="utf-8")
            result = run_script("validate_manifest.py", path)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("valid", result.stdout.lower())

    def test_rejects_duplicate_slide_ids_and_pages(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "manifest.json"
            data = manifest([slide("s01", 1), slide("s01", 1)])
            path.write_text(json.dumps(data), encoding="utf-8")
            result = run_script("validate_manifest.py", path)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("duplicate", result.stderr.lower())


class BuildMontageTests(unittest.TestCase):
    def test_builds_variable_count_montage_in_natural_order(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "slides"
            source.mkdir()
            for name, color in [("slide-10.png", "blue"), ("slide-2.png", "green"), ("slide-1.png", "red")]:
                Image.new("RGB", (160, 90), color).save(source / name)
            output = Path(tmp) / "montage.png"
            result = run_script("build_montage.py", source, output, "--columns", "2")
            self.assertEqual(result.returncode, 0, result.stderr)
            with Image.open(output) as image:
                self.assertEqual(image.size, (320, 180))
                self.assertEqual(image.getpixel((80, 45)), (255, 0, 0))
                self.assertEqual(image.getpixel((240, 45)), (0, 128, 0))
                self.assertEqual(image.getpixel((80, 135)), (0, 0, 255))

    def test_refuses_to_overwrite_an_existing_montage(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "slides"
            source.mkdir()
            Image.new("RGB", (160, 90), "blue").save(source / "slide-01.png")
            output = Path(tmp) / "montage.png"
            Image.new("RGB", (160, 90), "red").save(output)

            result = run_script("build_montage.py", source, output)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("already exists", result.stderr.lower())
            with Image.open(output) as image:
                self.assertEqual(image.getpixel((80, 45)), (255, 0, 0))


class CheckSlideOutputsTests(unittest.TestCase):
    def test_accepts_complete_16_by_9_sequence(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp)
            for page in range(1, 4):
                Image.new("RGB", (1600, 900), "white").save(source / f"slide-{page:02}.png")
            result = run_script("check_slide_outputs.py", source, "--expected", "3")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("valid", result.stdout.lower())

    def test_rejects_count_gap_and_non_16_by_9_image(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp)
            Image.new("RGB", (1600, 900), "white").save(source / "slide-01.png")
            Image.new("RGB", (1000, 1000), "white").save(source / "slide-03.png")
            result = run_script("check_slide_outputs.py", source, "--expected", "3")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("count", result.stderr.lower())
            self.assertIn("sequence", result.stderr.lower())
            self.assertIn("16:9", result.stderr)


class SkillGuidanceTests(unittest.TestCase):
    def test_routes_source_plugins_and_requires_font_preflight(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        phase1 = (ROOT / "references" / "phase-1-content.md").read_text(encoding="utf-8")
        phase4 = (ROOT / "references" / "phase-4-pptx-reconstruction.md").read_text(encoding="utf-8")

        self.assertIn("Resolve required fonts before slide layout begins", skill)
        self.assertIn("explicit user approval before installing fonts", skill)
        self.assertIn("Word or DOCX | Documents", phase1)
        self.assertIn("PDF | PDF", phase1)
        self.assertIn("XLSX, XLS, CSV, or TSV | Spreadsheets", phase1)
        self.assertIn("## Font Preflight Gate", phase4)
        self.assertIn("glyph coverage", phase4)
        self.assertIn("font mapping", phase4)
        self.assertIn("legitimate source", phase4)
        self.assertIn("Re-render the complete deck", phase4)
        self.assertIn("PowerPoint or WPS", phase4)
        self.assertIn("fonts used and substitutions", phase4)

    def test_routes_production_by_content_instead_of_forcing_slide_images(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        phase3 = (ROOT / "references" / "phase-3-slide-rendering.md").read_text(encoding="utf-8")
        phase4 = (ROOT / "references" / "phase-4-pptx-reconstruction.md").read_text(encoding="utf-8")

        self.assertIn("image-first", skill)
        self.assertIn("native-first", skill)
        self.assertIn("hybrid", skill)
        self.assertIn("representative slides", phase3)
        self.assertIn("approved visual-system contract", phase4)

    def test_defines_media_plan_hybrid_baseplates_and_image_pollution(self):
        phase2 = (ROOT / "references" / "phase-2-style-exploration.md").read_text(encoding="utf-8")
        phase3 = (ROOT / "references" / "phase-3-slide-rendering.md").read_text(encoding="utf-8")
        phase4 = (ROOT / "references" / "phase-4-pptx-reconstruction.md").read_text(encoding="utf-8")

        self.assertIn("slide media plan", phase2)
        self.assertIn("image pollution", phase2)
        self.assertIn("visual baseplate", phase3)
        self.assertIn("text-safe zones", phase3)
        self.assertIn("two times", phase3)
        self.assertIn("must not contain exact text", phase3)
        self.assertIn("visual baseplate", phase4)

    def test_distinguishes_preview_artifacts_and_requires_visible_delivery(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("direction montage", skill)
        self.assertIn("individual high-resolution slide", skill)
        self.assertIn("PPTX readback preview", skill)
        self.assertIn("accessible path or attachment", skill)

    def test_requires_diagram_qa_post_finalization_readback_and_one_current_delivery(self):
        phase4 = (ROOT / "references" / "phase-4-pptx-reconstruction.md").read_text(encoding="utf-8")

        self.assertIn("connector endpoints", phase4)
        self.assertIn("horizontal and vertical", phase4)
        self.assertIn("short labels", phase4)
        self.assertIn("After every finalization", phase4)
        self.assertIn("one current delivery file", phase4)

    def test_routes_repeated_runs_to_versioned_artifact_guidance(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        phase2 = (ROOT / "references" / "phase-2-style-exploration.md").read_text(encoding="utf-8")
        versioning = (ROOT / "references" / "artifact-versioning.md").read_text(encoding="utf-8")

        self.assertIn("artifact-versioning.md", skill)
        self.assertIn("round-01", versioning)
        self.assertIn("A/B/C", versioning)
        self.assertIn("D/E/F", versioning)
        self.assertIn("G/H/I", versioning)
        self.assertIn("revision-01", versioning)
        self.assertIn("must not overwrite", versioning)
        self.assertIn("work/", versioning)
        self.assertIn("approved/", versioning)
        self.assertIn("delivery/current/", versioning)
        self.assertIn("archive/", versioning)
        self.assertIn("task-wide direction labels", phase2)
        self.assertNotIn("Deliver A, B, and C", phase2)

    def test_tracks_content_and_readback_provenance(self):
        phase1 = (ROOT / "references" / "phase-1-content.md").read_text(encoding="utf-8")
        phase4 = (ROOT / "references" / "phase-4-pptx-reconstruction.md").read_text(encoding="utf-8")
        versioning = (ROOT / "references" / "artifact-versioning.md").read_text(encoding="utf-8")

        self.assertIn("immutable content-lock version", phase1)
        self.assertIn("content_lock_sha256", versioning)
        self.assertIn("source_pptx_sha256", versioning)
        self.assertIn("embed", phase4.lower())
        self.assertIn("reopen", phase4.lower())


if __name__ == "__main__":
    unittest.main()
