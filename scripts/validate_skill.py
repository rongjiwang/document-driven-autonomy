#!/usr/bin/env python3
"""Validate the repository's installable skill package."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FRONTMATTER_RE = re.compile(r"\A---\n(?P<body>.*?)\n---\n", re.DOTALL)
LINK_RE = re.compile(r"!?\[[^\]]+\]\(([^)]+)\)")
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,62}[a-z0-9]$")


def _frontmatter_fields(markdown: str) -> dict[str, str]:
    match = FRONTMATTER_RE.match(markdown)
    if not match:
        return {}

    fields: dict[str, str] = {}
    for line in match.group("body").splitlines():
        if ":" not in line or line.startswith((" ", "\t")):
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip("\"'")
    return fields


def _local_markdown_links(markdown: str) -> list[str]:
    links: list[str] = []
    for raw_target in LINK_RE.findall(markdown):
        target = raw_target.strip()
        if not target:
            continue
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        if " " in target:
            target = target.split(" ", 1)[0]
        links.append(target.split("#", 1)[0])
    return links


def validate_skill(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    skill_path = root / "SKILL.md"

    if not skill_path.is_file():
        return ["missing SKILL.md"]

    skill_markdown = skill_path.read_text(encoding="utf-8")
    fields = _frontmatter_fields(skill_markdown)

    name = fields.get("name")
    description = fields.get("description")

    if not name:
        errors.append("SKILL.md frontmatter must include name")
    elif not NAME_RE.match(name):
        errors.append("SKILL.md name must use lowercase letters, digits, and hyphens")

    if not description:
        errors.append("SKILL.md frontmatter must include description")
    elif len(description.split()) < 8:
        errors.append("SKILL.md description should be specific enough to guide triggering")

    if not skill_markdown.split("---", 2)[-1].strip():
        errors.append("SKILL.md must include body instructions after frontmatter")

    for target in _local_markdown_links(skill_markdown):
        if target and not (root / target).exists():
            errors.append(f"SKILL.md links to missing local file: {target}")

    agents_metadata = root / "agents" / "openai.yaml"
    if not agents_metadata.is_file():
        errors.append("missing agents/openai.yaml")
    else:
        metadata = agents_metadata.read_text(encoding="utf-8")
        for expected in ("display_name:", "short_description:", "default_prompt:"):
            if expected not in metadata:
                errors.append(f"agents/openai.yaml must include {expected.rstrip(':')}")

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", type=Path)
    args = parser.parse_args(argv)

    errors = validate_skill(args.root)
    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print("Skill package validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
