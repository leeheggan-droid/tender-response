"""Check the shipped skill, not only its optional counter."""

from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree
import zipfile

ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_skill_has_required_metadata(self):
        source = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        header = re.match(r"\A---\n(.*?)\n---\n", source, re.DOTALL)
        self.assertIsNotNone(header, "SKILL.md needs a closed frontmatter block")
        for key in ("name", "description"):
            values = re.findall(rf"^{key}:[ \t]*(.*)$", header[1], re.MULTILINE)
            self.assertEqual(len(values), 1, f"one nonempty {key} is required")
            self.assertTrue(values[0].strip(" '\""), f"{key} cannot be empty")
            if key == "name":
                self.assertEqual(values[0], "tender-response")

    def test_local_markdown_resources_exist_inside_package(self):
        for document in ROOT.rglob("*.md"):
            if any(part in {".git", ".venv", "dist"} for part in document.parts):
                continue
            for target in re.findall(r"\]\(([^)]+)\)", document.read_text(encoding="utf-8")):
                link = urlsplit(target.strip("<>"))
                if link.scheme or link.netloc or not link.path:
                    continue
                resource = (document.parent / unquote(link.path)).resolve()
                with self.subTest(document=document.relative_to(ROOT), target=target):
                    self.assertTrue(resource.is_relative_to(ROOT), "resource leaves package")
                    self.assertTrue(resource.exists(), "linked resource is missing")

    def test_distribution_has_license_and_counter(self):
        for resource in ("LICENSE", "README.md", "scripts/check_limits.py"):
            with self.subTest(resource=resource):
                self.assertTrue((ROOT / resource).is_file())
                self.assertGreater((ROOT / resource).stat().st_size, 0)

    def test_mixed_format_office_files_are_readable_archives(self):
        folder = ROOT / "evals" / "mixed-format"
        documents = list(folder.rglob("*.docx")) + list(folder.rglob("*.xlsx"))
        self.assertTrue(documents, "mixed-format assessment files are missing")
        for document in documents:
            with self.subTest(document=document.relative_to(ROOT)):
                with zipfile.ZipFile(document) as archive:
                    self.assertIsNone(archive.testzip())
                    part = "word/document.xml" if document.suffix == ".docx" else "xl/workbook.xml"
                    ElementTree.fromstring(archive.read(part))
                    ElementTree.fromstring(archive.read("[Content_Types].xml"))


if __name__ == "__main__":
    unittest.main()
