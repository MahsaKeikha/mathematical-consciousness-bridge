"""Apply runner-only corrections to the one-shot P85 publication script."""

from pathlib import Path

path = Path(__file__).with_name("promote_p85_publication.py")
text = path.read_text(encoding="utf-8")
old = '        before = "## After P85"\n'
new = '        before = "## 5. Current open frontier"\n'
if old not in text:
    raise SystemExit("expected roadmap insertion marker code not found")
text = text.replace(old, new, 1)
text = text.replace(
    '            raise RuntimeError("roadmap After P85 marker missing")',
    '            raise RuntimeError("roadmap current-open-frontier marker missing")',
    1,
)
path.write_text(text, encoding="utf-8")
print("patched one-shot P85 promotion runner")
