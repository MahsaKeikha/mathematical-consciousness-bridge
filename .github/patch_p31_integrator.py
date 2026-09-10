from pathlib import Path

path = Path(__file__).with_name("integrate_p31_release.py")
text = path.read_text(encoding="utf-8")
old = '  <text x="265" y="3599" class="body">Merging labels is valid only when retained response laws descend through the quotient.</text>'
new = '  <text x="265" y="3599" class="body">Labels may merge only when response laws descend through the quotient.</text>'
if text.count(old) != 1:
    raise RuntimeError(f"P31 roadmap-copy patch expected one marker, found {text.count(old)}")
path.write_text(text.replace(old, new, 1), encoding="utf-8")
