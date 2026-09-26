import json
import tempfile
import unittest
from pathlib import Path

from scripts.check_consistency import collect_errors


ROOT = Path(__file__).resolve().parent.parent


class ConsistencyChecksTest(unittest.TestCase):
    def test_current_repository_has_no_consistency_errors(self):
        self.assertEqual(collect_errors(ROOT), [])

    def test_historical_archive_numbers_do_not_count_as_current_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_fixture(root, [
                {"id": "normal-example", "prompt": "normal"},
                {"id": "missing-data", "prompt": "missing"},
                {"id": "conflicting-evidence", "prompt": "conflicting"},
            ])
            (root / "docs/archive/old.md").parent.mkdir(parents=True)
            (root / "docs/archive/old.md").write_text("38 prompts and four skills", encoding="utf-8")
            self.assertEqual(collect_errors(root), [])

    def test_reports_missing_required_case_category(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_fixture(root, [
                {"id": "normal-example", "prompt": "normal"},
                {"id": "missing-data", "prompt": "missing"},
            ])
            errors = collect_errors(root)
            self.assertTrue(any("conflicting-information" in error for error in errors))

    def test_reports_broken_current_link(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_fixture(root, [
                {"id": "normal-example", "prompt": "normal"},
                {"id": "missing-data", "prompt": "missing"},
                {"id": "conflicting-evidence", "prompt": "conflicting"},
            ])
            (root / "README.md").write_text("[missing](missing.md)", encoding="utf-8")
            errors = collect_errors(root)
            self.assertTrue(any("README.md" in error and "missing.md" in error for error in errors))

    def _write_fixture(self, root: Path, cases: list[dict]) -> None:
        eval_path = root / "skills/example/evals/evals.json"
        eval_path.parent.mkdir(parents=True)
        eval_path.write_text(json.dumps(cases), encoding="utf-8")
        (root / "skills/example/SKILL.md").write_text("---\nname: example\n---\n", encoding="utf-8")
        (root / "scripts/repository_inventory.json").parent.mkdir(parents=True, exist_ok=True)
        (root / "scripts/repository_inventory.json").write_text(
            json.dumps(
                {
                    "skill_count": 1,
                    "eval_count": len(cases),
                    "required_eval_categories": [
                        "normal",
                        "missing-information",
                        "conflicting-information",
                    ],
                }
            ),
            encoding="utf-8",
        )
        (root / "README.md").write_text("current", encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
