"""Repair escaped newlines in the Visual Atlas generator block.

This file is a one-time migration trigger and removes itself after success.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "scripts" / "enrich_figure_documentation.py"


def main() -> None:
    text = TARGET.read_text(encoding="utf-8")
    broken_start = "        '\n<section class=\"boundary\"><h2>How to read every figure</h2>'"
    fixed_start = "        '\\n<section class=\"boundary\"><h2>How to read every figure</h2>'"
    if broken_start not in text:
        raise RuntimeError("broken reading-key opening string not found")
    text = text.replace(broken_start, fixed_start, 2)

    broken_end = "</a>.</p></section>\n'\n    )"
    fixed_end = "</a>.</p></section>\\n'\n    )"
    count = text.count(broken_end)
    if count < 2:
        raise RuntimeError(f"expected at least two broken reading-key endings, found {count}")
    text = text.replace(broken_end, fixed_end, 2)
    TARGET.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
