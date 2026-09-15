"""Temporary syntax repair for the one-time P99 publication promoter."""

from __future__ import annotations

from pathlib import Path

PATH = Path(__file__).with_name("promote_p99_public_frontier.py")
text = PATH.read_text(encoding="utf-8")
needle = '</section>\\n"\n    text = text.replace(marker, block + marker, 1)'
replacement = '</section>\\n"""\n    text = text.replace(marker, block + marker, 1)'
count = text.count(needle)
if count == 2:
    text = text.replace(needle, replacement)
    PATH.write_text(text, encoding="utf-8")
    print("[P99] repaired two temporary promoter HTML block endings")
elif count == 0:
    print("[P99] promoter HTML block endings are already valid")
else:
    raise RuntimeError(f"expected 0 or 2 malformed HTML block endings, found {count}")
