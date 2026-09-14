from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

README = ROOT / "README.md"
START_HERE = ROOT / "START_HERE.md"
RESEARCH_MAP = ROOT / "docs" / "research_map.md"
HOME = ROOT / "website" / "index.html"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")








def test_research_map_organizes_by_questions_not_full_history() -> None:
    text = read(RESEARCH_MAP)
    lowered = text.lower()
    for chapter in range(1, 7):
        assert f"Chapter {chapter}:" in text
    assert "Detailed proposition record" in text
    assert "Theorem Roadmap" in text
    assert "final bridge remains open" in lowered
