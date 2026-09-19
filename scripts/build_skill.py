#!/usr/bin/env python3
"""Build a portable skill zip containing only runtime resources and notices."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from validate_skill import validate


def build(root):
    root = Path(root).resolve()
    errors = validate(root, repository=True)
    if errors:
        raise ValueError("Cannot package invalid skill:\n" + "\n".join(errors))
    output = root / "dist" / "apple-design-coach.zip"
    output.parent.mkdir(exist_ok=True)
    files = [root / name for name in ("SKILL.md", "LICENSE", "NOTICE")]
    for folder in ("agents", "references"):
        files.extend(p for p in (root / folder).rglob("*") if p.is_file())
    with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
        for path in sorted(files):
            archive.write(path, "apple-design-coach/" + path.relative_to(root).as_posix())
    return output


if __name__ == "__main__":
    print(build(Path(__file__).resolve().parents[1]))
