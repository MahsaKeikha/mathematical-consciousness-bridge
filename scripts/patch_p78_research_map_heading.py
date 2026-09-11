from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "website" / "research-map.html"
WORKFLOW = ROOT / ".github" / "workflows" / "patch-p78-research-map-heading.yml"
SELF = Path(__file__)

text = MAP.read_text(encoding="utf-8")
old = "<h2>P78: How is P77 made rigorous for the continuous P75 family?</h2>"
new = (
    "<h2>P78: Certified continuous P75 model separation</h2>"
    "<p class=\"lede\">How is P77 made rigorous for the continuous P75 family?</p>"
)
if old not in text:
    raise SystemExit("Expected P78 heading was not found")
text = text.replace(old, new, 1)
MAP.write_text(text, encoding="utf-8")

SELF.unlink()
WORKFLOW.unlink()
