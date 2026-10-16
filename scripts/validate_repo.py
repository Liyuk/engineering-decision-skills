#!/usr/bin/env python3
"""Validate skill packages, frontmatter, linked local docs, eval JSON, and local links."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.sync_skill_contract import contract_copy_errors


ROOT = Path(__file__).resolve().parent.parent
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
NAME_RE = re.compile(r"^name:\s*['\"]?([^\s'\"]+)['\"]?\s*$", re.MULTILINE)
LICENSE_RE = re.compile(r"^license:\s*MIT\s*$", re.MULTILINE)
DESCRIPTION_RE = re.compile(r"^description:\s*\S", re.MULTILINE)
H2_RE = re.compile(r"^## ", re.MULTILINE)
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
PACKAGE_LINK_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)|(?<!!)\[[^\]]*\]\(([^)]+)\)")
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


def local_link_target(target: str) -> str | None:
    """Return a local path from a Markdown link target, or None for external and anchor links."""
    cleaned = target.strip().split(maxsplit=1)[0].strip("<>")
    parsed = urlparse(cleaned)
    if parsed.scheme or cleaned.startswith("//") or cleaned.startswith("#"):
        return None
    local_path = unquote(parsed.path)
    return local_path or None


def check_skill_package_links(errors: list[str], root: Path = ROOT) -> None:
    """Fail when a skill package links to a file outside its own directory."""
    for skill_file in sorted((root / "skills").glob("*/SKILL.md")):
        skill_dir = skill_file.parent.resolve()
        for source in sorted(skill_dir.rglob("*.md")):
            relative = source.relative_to(root)
            for line_number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
                for match in PACKAGE_LINK_RE.finditer(line):
                    raw_target = match.group(1) or match.group(2)
                    local_path = local_link_target(raw_target)
                    if local_path is None:
                        continue
                    resolved = (source.parent / local_path).resolve()
                    try:
                        resolved.relative_to(skill_dir)
                    except ValueError:
                        errors.append(
                            f"{relative}:{line_number}: link points outside the skill package: {local_path}"
                        )


def check_markdown_links(errors: list[str], root: Path = ROOT) -> None:
    for source in root.rglob("*.md"):
        relative = source.relative_to(root)
        if any(part.startswith(".") for part in relative.parts):
            continue
        for line_number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
            for match in LINK_RE.finditer(line):
                local_path = local_link_target(match.group(1))
                if local_path is None:
                    continue
                resolved = (source.parent / local_path).resolve()
                if not resolved.exists():
                    errors.append(f"{relative}:{line_number}: local link target not found: {local_path}")


def readme_pair_errors(root: Path = ROOT) -> list[str]:
    """Require an English default README and a Chinese twin with the same sections."""
    errors: list[str] = []
    english = root / "README.md"
    chinese = root / "README.zh-CN.md"
    for path in (english, chinese):
        if not path.is_file():
            errors.append(f"missing required file: {path.relative_to(root)}")
    if errors:
        return errors
    english_text = english.read_text(encoding="utf-8")
    chinese_text = chinese.read_text(encoding="utf-8")
    if not english_text.startswith("[Chinese](README.zh-CN.md)"):
        errors.append("README.md: first line must link to README.zh-CN.md")
    if not chinese_text.startswith("[英文](README.md)"):
        errors.append("README.zh-CN.md: first line must link to README.md")
    english_sections = len(H2_RE.findall(english_text))
    chinese_sections = len(H2_RE.findall(chinese_text))
    if english_sections != chinese_sections:
        errors.append(
            "README section count differs: "
            f"README.md has {english_sections} level-2 headings, "
            f"README.zh-CN.md has {chinese_sections}"
        )
    return errors


def collect_errors(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for required in (root / "AGENTS.md", root / "agent/README.md"):
        if not required.is_file():
            errors.append(f"missing required file: {required.relative_to(root)}")
    errors.extend(readme_pair_errors(root))
    check_skill_packages(errors, root)
    check_skill_package_links(errors, root)
    check_markdown_links(errors, root)
    errors.extend(contract_copy_errors(root))
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
        "(entrypoints, names, license, descriptions, package docs, "
        "in-package links, contract copies, eval JSON, local Markdown links, "
        "English and Chinese READMEs)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
