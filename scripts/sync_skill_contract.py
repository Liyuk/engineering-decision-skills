#!/usr/bin/env python3
"""Copy the canonical evidence contract into every skill package.

The source of truth is ``agent/decision-and-review-contract.md``. Each skill
receives an identical copy at ``references/decision-and-review-contract.md``
so the package can be installed without files outside its own directory.

Edit the canonical file, then run this script. Do not edit the copies by hand.
``--check`` fails when a copy is missing or different.
"""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CANONICAL_RELATIVE = Path("agent/decision-and-review-contract.md")
COPY_RELATIVE = Path("references/decision-and-review-contract.md")


def canonical_path(root: Path = ROOT) -> Path:
    return root / CANONICAL_RELATIVE


def copy_paths(root: Path = ROOT) -> list[Path]:
    return [
        skill_file.parent / COPY_RELATIVE
        for skill_file in sorted((root / "skills").glob("*/SKILL.md"))
    ]


def contract_copy_errors(root: Path = ROOT) -> list[str]:
    """Return errors when skill copies are missing or differ from the canonical file."""
    source = canonical_path(root)
    if not source.is_file():
        return [f"{CANONICAL_RELATIVE.as_posix()}: canonical evidence contract is missing"]
    canonical = source.read_bytes()
    errors: list[str] = []
    for dest in copy_paths(root):
        relative = dest.relative_to(root).as_posix()
        if not dest.is_file():
            errors.append(
                f"{relative}: missing synced copy of the evidence contract; "
                "run python3 scripts/sync_skill_contract.py"
            )
            continue
        if dest.read_bytes() != canonical:
            errors.append(
                f"{relative}: differs from {CANONICAL_RELATIVE.as_posix()}; "
                "run python3 scripts/sync_skill_contract.py"
            )
    return errors


def sync_contract_copies(root: Path = ROOT) -> list[Path]:
    source = canonical_path(root)
    if not source.is_file():
        raise FileNotFoundError(f"{CANONICAL_RELATIVE.as_posix()} is missing")
    canonical = source.read_bytes()
    written: list[Path] = []
    for dest in copy_paths(root):
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.is_file() or dest.read_bytes() != canonical:
            dest.write_bytes(canonical)
            written.append(dest)
    return written


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if args not in ([], ["--check"]):
        print("用法: sync_skill_contract.py [--check]", file=sys.stderr)
        return 2
    if args == ["--check"]:
        errors = contract_copy_errors()
        if errors:
            print("Evidence-contract copies are out of sync:")
            for error in errors:
                print(f"- {error}")
            return 1
        print(
            "Evidence-contract copies match "
            f"{CANONICAL_RELATIVE.as_posix()} ({len(copy_paths())} skills)."
        )
        return 0
    written = sync_contract_copies()
    if written:
        print("Updated evidence-contract copies:")
        for path in written:
            print(f"- {path.relative_to(ROOT).as_posix()}")
    else:
        print(
            "Evidence-contract copies already match "
            f"{CANONICAL_RELATIVE.as_posix()} ({len(copy_paths())} skills)."
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
