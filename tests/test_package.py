import json
import sys
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from build_skill import build
from validate_skill import validate


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write("SKILL.md", "---\nname: sample\ndescription: Review product design\n---\n"
                   "Read [guide](references/guide.md).\n")
        self.write("references/guide.md", "# Guide\nUseful guidance.\n")
        self.write("agents/openai.yaml", 'interface:\n  display_name: "Sample"\n'
                   '  short_description: "Review interfaces with useful evidence"\n'
                   '  default_prompt: "Use $sample to review this screen."\n')
        self.write("LICENSE", "Example license")
        self.write("NOTICE", "Example notice")
        self.cases = {"cases": [{"id": "example", "prompt": "Review this", "fixtures": [],
                                  "criteria": ["Give evidence for the recommendation"]}]}
        self.save_cases()

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def save_cases(self):
        self.write("evals/cases.json", json.dumps(self.cases))

    def test_valid_repository(self):
        self.assertEqual(validate(self.root, repository=True), [])

    def test_broken_reference(self):
        (self.root / "references/guide.md").unlink()
        self.assertTrue(any("missing link" in e for e in validate(self.root)))

    def test_unreachable_reference(self):
        self.write("references/orphan.md", "# Unrouted instructions")
        self.assertTrue(any("unreachable" in e for e in validate(self.root)))

    def test_escaping_link(self):
        self.write("references/guide.md", "[outside](../../outside.md)")
        self.assertTrue(any("escapes package" in e for e in validate(self.root)))

    def test_malformed_frontmatter(self):
        self.write("SKILL.md", "---\n[not: valid\n---\nText")
        self.assertTrue(validate(self.root))

    def test_empty_description(self):
        self.write("SKILL.md", "---\nname: sample\ndescription: ''\n---\nText")
        self.assertTrue(any("invalid description" in e for e in validate(self.root)))

    def test_wrong_invocation(self):
        path = self.root / "agents/openai.yaml"
        path.write_text(path.read_text(encoding="utf-8").replace("$sample", "$wrong"), encoding="utf-8")
        self.assertTrue(any("must mention" in e for e in validate(self.root)))

    def test_duplicate_case(self):
        self.cases["cases"].append(self.cases["cases"][0].copy())
        self.save_cases()
        self.assertTrue(any("duplicate" in e for e in validate(self.root, repository=True)))

    def test_missing_fixture(self):
        self.cases["cases"][0]["fixtures"] = ["fixtures/missing"]
        self.save_cases()
        self.assertTrue(any("invalid fixture" in e for e in validate(self.root, repository=True)))

    def test_escaping_fixture(self):
        self.cases["cases"][0]["fixtures"] = ["../SKILL.md"]
        self.save_cases()
        self.assertTrue(any("invalid fixture" in e for e in validate(self.root, repository=True)))

    def test_package_is_self_contained_and_excludes_tests(self):
        archive_path = build(self.root)
        target = self.root / "unpacked"
        with ZipFile(archive_path) as archive:
            self.assertNotIn("apple-design-coach/evals/cases.json", archive.namelist())
            archive.extractall(target)
        self.assertEqual(validate(target / "apple-design-coach"), [])

    def test_package_rejects_broken_repository(self):
        (self.root / "references/guide.md").unlink()
        with self.assertRaises(ValueError):
            build(self.root)


if __name__ == "__main__":
    unittest.main()
