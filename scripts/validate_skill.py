#!/usr/bin/env python3
"""Offline package checks. These do not evaluate design-coaching quality."""

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


def read_yaml(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def local_links(path):
    """Read inline Markdown links (the link format used by this repository)."""
    content = path.read_text(encoding="utf-8")
    content = re.sub(r"```.*?```", "", content, flags=re.S)
    for target in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", content):
        target = target.strip().strip("<>")
        parsed = urlsplit(target)
        if not parsed.scheme and not parsed.netloc and parsed.path:
            yield unquote(parsed.path)


def validate(root, repository=False):
    root = Path(root).resolve()
    errors = []
    skill = root / "SKILL.md"
    try:
        content = skill.read_text(encoding="utf-8")
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", content, re.S)
        if not match:
            raise ValueError("missing YAML frontmatter")
        meta = yaml.safe_load(match.group(1))
        if not isinstance(meta, dict):
            raise ValueError("frontmatter must be a mapping")
        name = meta.get("name")
        if (not isinstance(name, str) or len(name) > 64
                or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)):
            errors.append("SKILL.md: invalid name")
        desc = meta.get("description")
        if (not isinstance(desc, str) or not desc.strip() or len(desc) > 1024
                or any(char in desc for char in "<>")):
            errors.append("SKILL.md: invalid description")
        if not content[match.end():].strip():
            errors.append("SKILL.md: empty instructions")
    except (OSError, ValueError, yaml.YAMLError) as exc:
        errors.append(f"SKILL.md: {exc}")
        name = None

    try:
        config = read_yaml(root / "agents" / "openai.yaml")
        interface = config.get("interface", {}) if isinstance(config, dict) else {}
        if not isinstance(interface, dict):
            raise ValueError("interface must be a mapping")
        for field in ("display_name", "short_description", "default_prompt"):
            if not isinstance(interface.get(field), str) or not interface[field].strip():
                errors.append(f"agents/openai.yaml: missing {field}")
        short = interface.get("short_description", "")
        if isinstance(short, str) and not 25 <= len(short) <= 64:
            errors.append("agents/openai.yaml: short_description must have 25–64 characters")
        prompt = interface.get("default_prompt", "")
        if name and (not isinstance(prompt, str) or f"${name}" not in prompt):
            errors.append("agents/openai.yaml: default_prompt must mention $skill-name")
    except (OSError, ValueError, yaml.YAMLError) as exc:
        errors.append(f"agents/openai.yaml: {exc}")

    # Avoid traversing virtual environments, git internals, or build output.
    markdown = list(root.glob("*.md"))
    for folder in ("references", "examples", "docs", "evals"):
        markdown.extend((root / folder).rglob("*.md"))
    graph = {}
    for path in markdown:
        graph[path.resolve()] = []
        for target in local_links(path):
            resolved = (path.parent / target).resolve()
            if not resolved.is_relative_to(root):
                errors.append(f"{path.relative_to(root)}: link escapes package: {target}")
            elif not resolved.exists():
                errors.append(f"{path.relative_to(root)}: missing link target: {target}")
            else:
                graph[path.resolve()].append(resolved)
    reached, pending = set(), [skill.resolve()]
    while pending:
        current = pending.pop()
        if current not in reached:
            reached.add(current)
            pending.extend(graph.get(current, []))
    for ref in (root / "references").glob("*.md"):
        if ref.resolve() not in reached:
            errors.append(f"{ref.relative_to(root)}: unreachable from SKILL.md")

    if repository:
        try:
            manifest = json.loads((root / "evals" / "cases.json").read_text(encoding="utf-8"))
            cases = manifest.get("cases") if isinstance(manifest, dict) else None
            if not isinstance(cases, list) or not cases:
                raise ValueError("cases must be a nonempty list")
            seen = set()
            for case in cases:
                if not isinstance(case, dict):
                    raise ValueError("each case must be an object")
                case_id = case.get("id")
                if not isinstance(case_id, str) or not re.fullmatch(r"[a-z0-9-]+", case_id):
                    raise ValueError("invalid case id")
                if case_id in seen:
                    errors.append(f"evals: duplicate case id {case_id}")
                seen.add(case_id)
                if not isinstance(case.get("prompt"), str) or not case["prompt"].strip():
                    errors.append(f"evals: {case_id} needs a prompt")
                criteria = case.get("criteria")
                if (not isinstance(criteria, list) or not criteria
                        or any(not isinstance(c, str) or not c.strip() for c in criteria)):
                    errors.append(f"evals: {case_id} needs behavioral criteria")
                fixtures = case.get("fixtures")
                if not isinstance(fixtures, list) or any(not isinstance(f, str) for f in fixtures):
                    raise ValueError(f"{case_id}: fixtures must be a list of paths")
                for fixture in fixtures:
                    resolved = (root / "evals" / fixture).resolve()
                    if (not resolved.is_relative_to(root / "evals" / "fixtures")
                            or not resolved.exists()):
                        errors.append(f"evals: {case_id} invalid fixture: {fixture}")
        except (OSError, ValueError) as exc:
            errors.append(f"evals/cases.json: {exc}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--package-only", action="store_true", help="Skip repository evaluation-manifest checks")
    args = parser.parse_args()
    errors = validate(args.path, repository=not args.package_only)
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print("PASS: package structure, metadata, and local references" +
          ("" if args.package_only else "; evaluation manifest"))
    print("Not evaluated: model behavior, remote source freshness, or real product usability.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
