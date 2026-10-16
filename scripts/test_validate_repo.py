import tempfile
import unittest
from pathlib import Path

from scripts.sync_skill_contract import contract_copy_errors
from scripts.validate_repo import check_skill_package_links, collect_errors


ROOT = Path(__file__).resolve().parent.parent


class ValidateRepoTest(unittest.TestCase):
    def test_current_repository_passes(self):
        self.assertEqual(collect_errors(ROOT), [])

    def test_reports_missing_license_and_unlinked_reference(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = root / "skills" / "example"
            (skill / "references").mkdir(parents=True)
            (skill / "references" / "notes.md").write_text("note", encoding="utf-8")
            (skill / "SKILL.md").write_text(
                "---\nname: example\ndescription: Use when example.\n---\n# Example\n",
                encoding="utf-8",
            )
            (root / "README.md").write_text("readme", encoding="utf-8")
            (root / "AGENTS.md").write_text("agents", encoding="utf-8")
            (root / "agent").mkdir()
            (root / "agent" / "README.md").write_text("shared", encoding="utf-8")

            errors = collect_errors(root)

        self.assertTrue(any("license: MIT" in error for error in errors))
        self.assertTrue(any("references/notes.md" in error for error in errors))

    def test_reports_link_outside_skill_package(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = root / "skills" / "example"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text(
                "See [outside](../../README.md) and [web](https://example.com/doc).\n",
                encoding="utf-8",
            )
            (root / "README.md").write_text("readme", encoding="utf-8")
            errors: list[str] = []
            check_skill_package_links(errors, root)

        self.assertEqual(len(errors), 1)
        self.assertIn("link points outside the skill package", errors[0])
        self.assertIn("../../README.md", errors[0])

    def test_reports_contract_copy_drift(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "agent").mkdir()
            (root / "agent" / "decision-and-review-contract.md").write_text(
                "canonical\n", encoding="utf-8"
            )
            skill = root / "skills" / "example" / "references"
            skill.mkdir(parents=True)
            (root / "skills" / "example" / "SKILL.md").write_text("# Example\n", encoding="utf-8")
            (skill / "decision-and-review-contract.md").write_text("edited copy\n", encoding="utf-8")

            errors = contract_copy_errors(root)

        self.assertTrue(any("differs from agent/decision-and-review-contract.md" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
