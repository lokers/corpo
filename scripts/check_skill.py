#!/usr/bin/env python3
"""Structure check for the Corpo Translator skill. Stdlib only."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "corpo"
SKILL = SKILL_DIR / "SKILL.md"
GLOSSARY = SKILL_DIR / "glossary.md"
EXAMPLES = SKILL_DIR / "examples.md"
README = ROOT / "README.md"
LICENSE = ROOT / "LICENSE"

DISCLAIMER_HEADING = "For fun, not for the record"
DISCLAIMER_SENTENCE = (
    "The authors and contributors are not responsible for translations made with this skill"
)

failures = []


def fail(message):
    failures.append(message)


def read(path):
    if not path.is_file():
        fail(f"missing file: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        fail("SKILL.md has no YAML frontmatter")
        return {}, []
    end = None
    for index, line in enumerate(lines[1:], start=1):
        if line == "---":
            end = index
            break
    if end is None:
        fail("SKILL.md frontmatter is not closed")
        return {}, []
    fields = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        key, sep, value = line.partition(":")
        if not sep:
            fail(f"SKILL.md frontmatter line is not key: value ({line})")
            continue
        fields[key.strip()] = value.strip().strip("\"'")
    return fields, lines[end + 1 :]


def linked_targets(text):
    return re.findall(r"\[[^\]]*\]\(([^)]+)\)", text)


def sections(text, marker):
    parts = re.split(rf"(?m)^{re.escape(marker)} ", text)
    return [part for part in parts[1:]]


def main():
    skill_text = read(SKILL)
    glossary_text = read(GLOSSARY)
    examples_text = read(EXAMPLES)
    readme_text = read(README)
    license_text = read(LICENSE)

    fields, body = parse_frontmatter(skill_text)
    name = fields.get("name", "")
    description = fields.get("description", "")
    if name != "corpo":
        fail(f"name is {name!r}, expected 'corpo'")
    if not description:
        fail("description is empty")
    elif len(description) > 1024:
        fail(f"description is {len(description)} characters (max 1024)")
    elif description.startswith("I ") or description.startswith("You "):
        fail("description must be third person")
    if fields.get("disable-model-invocation") != "true":
        fail("disable-model-invocation must be true")
    if len(body) >= 500:
        fail(f"SKILL.md body is {len(body)} lines (max 499)")

    if not GLOSSARY.is_file() or not EXAMPLES.is_file():
        fail("glossary.md and examples.md must sit beside SKILL.md")
    targets = linked_targets(skill_text)
    if "glossary.md" not in targets or "examples.md" not in targets:
        fail("SKILL.md must link to glossary.md and examples.md")
    extra = [target for target in targets if target not in {"glossary.md", "examples.md"}]
    if extra:
        fail(f"SKILL.md links outside glossary.md and examples.md: {extra}")

    entries = sections(glossary_text, "###")
    if len(entries) < 40:
        fail(f"glossary has {len(entries)} entries (need at least 40)")
    for entry in entries:
        title = entry.splitlines()[0].strip() if entry.splitlines() else "(blank)"
        if not re.search(r"(?m)^- Corpo:", entry):
            fail(f"glossary entry missing Corpo line: {title}")
        if not re.search(r"(?m)^- Colloquial:", entry):
            fail(f"glossary entry missing Colloquial line: {title}")

    cases = sections(examples_text, "##")
    if len(cases) < 8:
        fail(f"examples have {len(cases)} cases (need at least 8)")

    readme_cases = [case for case in cases if re.search(r"(?m)^README: yes\s*$", case)]
    if len(readme_cases) < 1:
        fail("no README cases marked README: yes")

    kept_a_fact = False
    for case in readme_cases:
        kept = re.search(r"(?m)^Must keep:\n((?:- .+\n?)+)", case)
        if kept:
            kept_a_fact = True
        input_match = re.search(r'(?m)^Input: "(.*)"\s*$', case)
        if not input_match:
            fail("a README case is missing Input: \"...\"")
            continue
        sample = input_match.group(1)
        if sample not in readme_text:
            fail(f"README is missing demo input: {sample}")

    all_directions = []
    for case in cases:
        direction = re.search(r"(?m)^Direction: (.+)$", case)
        if direction:
            all_directions.append(direction.group(1).strip())
    if not any(re.search(r"→\s*colloquial\b", item) for item in all_directions):
        fail("examples do not cover a colloquial flip")
    if not any(re.search(r"→\s*corpo\b", item) for item in all_directions):
        fail("examples do not cover a corpo flip")
    if not kept_a_fact:
        fail("README cases do not include a Must keep fact")

    if DISCLAIMER_HEADING not in readme_text:
        fail(f"README is missing the heading {DISCLAIMER_HEADING!r}")
    if DISCLAIMER_SENTENCE not in readme_text:
        fail("README is missing the not-responsible sentence")
    if "MIT" not in readme_text:
        fail("README does not mention MIT")
    if "MIT License" not in license_text:
        fail("LICENSE is not the MIT license")

    if failures:
        for message in failures:
            print(f"fail: {message}", file=sys.stderr)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
