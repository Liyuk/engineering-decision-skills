#!/usr/bin/env python3
"""Check current repository inventory and metadata consistency."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def classify_case(case: dict) -> set[str]:
    text = f"{case.get('id', '')} {case.get('prompt', '')}".lower()
    categories: set[str] = set()
    if re.search(r"normal|no-blocker|evidence-backed", text):
        categories.add("normal")
    if re.search(r"missing|no-data|no-baseline|unconfirmed|deadline-pressure", text):
        categories.add("missing-information")
    if re.search(r"conflict|counterevidence|denominator", text):
        categories.add("conflicting-information")
    return categories


def local_link_errors(root: Path) -> list[str]:
    errors: list[str] = []
    for source in root.rglob("*.md"):
        relative = source.relative_to(root)
        if any(part.startswith(".") for part in relative.parts):
            continue
        for line_number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
            for match in LINK_RE.finditer(line):
                target = match.group(1).strip().split(maxsplit=1)[0].strip("<>")
                parsed = urlparse(target)
                if parsed.scheme or target.startswith("//") or target.startswith("#"):
                    continue
                path = unquote(parsed.path)
                if not path:
                    continue
                resolved = (source.parent / path).resolve()
                if not resolved.exists():
                    errors.append(f"{relative}:{line_number}: local link target not found: {path}")
    return errors


def collect_errors(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    inventory_path = root / "scripts/repository_inventory.json"
    try:
        inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"scripts/repository_inventory.json: cannot read inventory: {exc}"]

    skill_files = sorted((root / "skills").glob("*/SKILL.md"))
    expected_skill_count = inventory.get("skill_count")
    if len(skill_files) != expected_skill_count:
        errors.append(f"expected {expected_skill_count} skills, found {len(skill_files)}")

    total_evals = 0
    observed_categories: set[str] = set()
    for skill_file in skill_files:
        eval_path = skill_file.parent / "evals/evals.json"
        try:
            cases = json.loads(eval_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{eval_path.relative_to(root)}: cannot read evals: {exc}")
            continue
        if not isinstance(cases, list):
            errors.append(f"{eval_path.relative_to(root)}: expected a JSON array")
            continue
        total_evals += len(cases)
        skill_categories: set[str] = set()
        for case in cases:
            if not isinstance(case, dict):
                errors.append(f"{eval_path.relative_to(root)}: every case must be an object")
                continue
            skill_categories.update(classify_case(case))
        observed_categories.update(skill_categories)
        required = set(inventory.get("required_eval_categories", []))
        missing = required - skill_categories
        if missing:
            errors.append(
                f"{eval_path.relative_to(root)}: missing eval categories: {', '.join(sorted(missing))}"
            )

    if total_evals != inventory.get("eval_count"):
        errors.append(f"expected {inventory.get('eval_count')} eval cases, found {total_evals}")

    errors.extend(local_link_errors(root))
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        print("Consistency check failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Consistency check passed (current skill/eval inventory and local links).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
