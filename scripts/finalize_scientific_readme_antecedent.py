from pathlib import Path

path = Path("README.md")
text = path.read_text(encoding="utf-8")
old = "They may be discussed as speculative conceptual antecedents, but they are not used as assumptions in the theorem chain."
new = "They may be discussed only as a **speculative, falsifiable antecedent**, but they are not used as assumptions in the theorem chain."
if old not in text:
    raise SystemExit("Expected antecedent sentence not found")
path.write_text(text.replace(old, new, 1), encoding="utf-8")
