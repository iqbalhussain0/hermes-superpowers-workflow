#!/usr/bin/env python3
"""Structural validation for the portable Hermes skill package."""
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
skills_root = ROOT / "skills"
errors = []
skills = {}
for path in sorted(skills_root.glob("*/SKILL.md")):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{path}: missing YAML frontmatter")
        continue
    try:
        _, front, _ = text.split("---", 2)
        data = yaml.safe_load(front) or {}
    except Exception as exc:
        errors.append(f"{path}: invalid frontmatter: {exc}")
        continue
    name = data.get("name")
    description = data.get("description")
    if not name or not description:
        errors.append(f"{path}: name and description are required")
    if name in skills:
        errors.append(f"duplicate skill name: {name}")
    skills[name] = path
    related = ((data.get("metadata") or {}).get("hermes") or {}).get("related_skills", [])
    for ref in related:
        if ref not in skills_root.joinpath(ref, "SKILL.md").parents and not (skills_root / ref / "SKILL.md").exists():
            errors.append(f"{path}: missing related skill {ref}")

if errors:
    for error in errors:
        print(f"ERROR {error}")
    print(f"VALIDATION=FAIL errors={len(errors)}")
    sys.exit(1)
print(f"SKILLS={len(skills)}")
print("VALIDATION=PASS")
