#!/usr/bin/env python3
"""Validate skill packages, frontmatter, linked local docs, eval JSON, and local links."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parent.parent
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
NAME_RE = re.compile(r"^name:\s*['\"]?([^\s'\"]+)['\"]?\s*$", re.MULTILINE)
LICENSE_RE = re.compile(r"^license:\s*MIT\s*$", re.MULTILINE)
DESCRIPTION_RE = re.compile(r"^description:\s*\S", re.MULTILINE)
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
PACKAGE_DOC_DIRS = ("references", "assets")


def check_skill_packages(errors: list[str], root: Path = ROOT) -> None:
    skills_dir = root / "skills"
    skill_files = sorted(skills_dir.glob("*/SKILL.md"))
    if not skill_files:
        errors.append("skills/: no */SKILL.md entrypoints found")
        return

    for skill_file in skill_files:
        relative = skill_file.relative_to(root)
        content = skill_file.read_text(encoding="utf-8")
        frontmatter = FRONTMATTER_RE.match(content)
        if not frontmatter:
            errors.append(f"{relative}: missing YAML frontmatter")
            continue
        frontmatter_text = frontmatter.group(1)
        name = NAME_RE.search(frontmatter_text)
        if not name:
            errors.append(f"{relative}: frontmatter has no simple name field")
            continue
        if name.group(1) != skill_file.parent.name:
            errors.append(
                f"{relative}: directory name {skill_file.parent.name!r} "
                f"does not match frontmatter name {name.group(1)!r}"
            )
        if not LICENSE_RE.search(frontmatter_text):
            errors.append(f"{relative}: frontmatter must include 'license: MIT'")
        if not DESCRIPTION_RE.search(frontmatter_text):
            errors.append(f"{relative}: frontmatter must include a non-empty description")
        check_linked_package_docs(errors, skill_file, content, root)

        eval_file = skill_file.parent / "evals" / "evals.json"
        if eval_file.is_file():
            try:
                parsed = json.loads(eval_file.read_text(encoding="utf-8"))
                if not isinstance(parsed, list):
                    errors.append(f"{eval_file.relative_to(root)}: expected a JSON array")
            except (OSError, json.JSONDecodeError) as exc:
                errors.append(f"{eval_file.relative_to(root)}: invalid JSON: {exc}")


def check_linked_package_docs(
    errors: list[str], skill_file: Path, content: str, root: Path
) -> None:
    """Require each local reference or asset to be linked from its SKILL.md."""
    for folder in PACKAGE_DOC_DIRS:
        base = skill_file.parent / folder
        if not base.is_dir():
            continue
        for doc in sorted(base.rglob("*.md")):
            rel = doc.relative_to(skill_file.parent).as_posix()
            if rel not in content:
                errors.append(
                    f"{skill_file.relative_to(root)}: {rel} is not linked from the skill entrypoint"
                )


def check_markdown_links(errors: list[str], root: Path = ROOT) -> None:
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
                local_path = unquote(parsed.path)
                if not local_path:
                    continue
                resolved = (source.parent / local_path).resolve()
                if not resolved.exists():
                    errors.append(f"{relative}:{line_number}: local link target not found: {local_path}")


def collect_errors(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for required in (root / "README.md", root / "AGENTS.md", root / "agent/README.md"):
        if not required.is_file():
            errors.append(f"missing required file: {required.relative_to(root)}")
    check_skill_packages(errors, root)
    check_markdown_links(errors, root)
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "Repository validation passed "
        "(entrypoints, names, license, descriptions, package docs, eval JSON, local Markdown links)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
