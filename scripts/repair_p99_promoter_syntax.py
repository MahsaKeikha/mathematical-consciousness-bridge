"""Temporary syntax repair for the one-time P99 publication promoter."""

from __future__ import annotations

import re
from pathlib import Path

PATH = Path(__file__).with_name("promote_p99_public_frontier.py")
text = PATH.read_text(encoding="utf-8")
pattern = re.compile(r'(    block = """<section[^\n]*?</section>)\\\\n"\n')
text, count = pattern.subn(lambda match: match.group(1) + '\n"""\n', text)
if count != 2:
    raise RuntimeError(f"expected to repair 2 malformed HTML blocks, repaired {count}")
PATH.write_text(text, encoding="utf-8")
print("[P99] repaired two temporary promoter HTML blocks")
