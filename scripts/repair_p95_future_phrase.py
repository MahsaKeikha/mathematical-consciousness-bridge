"""Remove the last stale P94 future-work trigger after P95 promotion."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "docs" / "theorem_roadmap.md"

text = PATH.read_text(encoding="utf-8")
text = text.replace(
    "The P95 continuation beyond P94 closes a separately stated statistical gap",
    "P95 closes the separately stated drift-aware statistical gap left by P94",
)
PATH.write_text(text, encoding="utf-8")
print("[p95] removed stale P94 future-work trigger")
