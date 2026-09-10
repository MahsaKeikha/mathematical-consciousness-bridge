"""Normalize repository typography to the project's ASCII dash policy.

The public research record does not use Unicode en dash or em dash characters.
Use an ASCII hyphen when a dash is required, or rewrite the sentence with
commas, colons, semicolons, or parentheses when editing prose manually.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN = ("\u2013", "\u2014")


def tracked_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return [ROOT / item.decode() for item in result.stdout.split(b"\0") if item]


def normalize_text(text: str) -> str:
    return text.replace("\u2013", "-").replace("\u2014", "-")


def main() -> None:
    changed: list[str] = []
    for path in tracked_files():
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        normalized = normalize_text(text)
        if normalized != text:
            path.write_text(normalized, encoding="utf-8")
            changed.append(str(path.relative_to(ROOT)))

    for path in changed:
        print(path)
    print(f"Normalized {len(changed)} tracked UTF-8 files.")


if __name__ == "__main__":
    main()
