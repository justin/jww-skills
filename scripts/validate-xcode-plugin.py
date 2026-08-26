#!/usr/bin/env python3
"""Validate the Xcode Agent Plugins packaging used by this repository."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


MANIFEST_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
REQUIRED_MANIFEST_FIELDS = {"$schema", "name", "version", "description", "author"}
FRONT_MATTER = re.compile(r"\A---\n(?P<body>.*?)\n---\n", re.DOTALL)
YAML_NAME = re.compile(r"^name:\s*(?P<name>.+?)\s*$", re.MULTILINE)
ICON = re.compile(r"^\s*icon_(?:small|large):\s*[\"']?(?P<path>[^\"'#\s]+)", re.MULTILINE)


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)


def front_matter_name(skill_file: Path) -> str | None:
    match = FRONT_MATTER.match(skill_file.read_text(encoding="utf-8"))
    if match is None:
        fail(f"{skill_file}: missing YAML front matter")
        return None

    name = YAML_NAME.search(match.group("body"))
    if name is None:
        fail(f"{skill_file}: front matter is missing name")
        return None

    return name.group("name").strip("\"'")


def validate_skill(skill_directory: Path) -> bool:
    valid = True
    skill_file = skill_directory / "SKILL.md"
    if not skill_file.is_file():
        fail(f"{skill_directory}: missing SKILL.md")
        return False

    name = front_matter_name(skill_file)
    if name != skill_directory.name:
        fail(f"{skill_file}: name must match {skill_directory.name}")
        valid = False

    if any((skill_directory / directory).is_dir() for directory in ("hooks", "prompts")):
        install_file = skill_directory / "INSTALL.md"
        if not install_file.is_file():
            fail(f"{skill_directory}: hooks or prompts require INSTALL.md")
            valid = False

    metadata_file = skill_directory / "agents" / "openai.yaml"
    if metadata_file.is_file():
        for icon in ICON.findall(metadata_file.read_text(encoding="utf-8")):
            if not (skill_directory / icon).is_file():
                fail(f"{metadata_file}: missing referenced asset {icon}")
                valid = False

    return valid


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--release-version", help="version intended for a release")
    parser.add_argument("root", nargs="?", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    manifest_file = root / "plugin.json"

    try:
        manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"{manifest_file}: missing plugin manifest")
        return 1
    except json.JSONDecodeError as error:
        fail(f"{manifest_file}: invalid JSON ({error.msg})")
        return 1

    valid = True
    missing_fields = REQUIRED_MANIFEST_FIELDS - manifest.keys()
    if missing_fields:
        fail(f"{manifest_file}: missing required fields: {', '.join(sorted(missing_fields))}")
        valid = False
    if manifest.get("$schema") != MANIFEST_SCHEMA:
        fail(f"{manifest_file}: schema must be {MANIFEST_SCHEMA}")
        valid = False
    if manifest.get("name") != "jww-skills":
        fail(f"{manifest_file}: name must be jww-skills")
        valid = False
    if not isinstance(manifest.get("author"), dict) or not manifest["author"].get("name"):
        fail(f"{manifest_file}: author must provide a name")
        valid = False
    if args.release_version and manifest.get("version") != args.release_version:
        fail("plugin version does not match --release-version")
        valid = False

    skills_directory = root / "skills"
    skill_directories = sorted(path for path in skills_directory.iterdir() if path.is_dir()) if skills_directory.is_dir() else []
    if not skill_directories:
        fail(f"{skills_directory}: no skills to package")
        valid = False
    for skill_directory in skill_directories:
        valid = validate_skill(skill_directory) and valid

    if not valid:
        return 1
    print(f"validated {manifest['name']} {manifest['version']} ({len(skill_directories)} skills)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
