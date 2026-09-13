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


def test_first_reader_layers_stay_compact() -> None:
    assert len(read(README)) < 12_000
    assert len(read(START_HERE)) < 14_000
    assert len(read(RESEARCH_MAP)) < 20_000
    assert len(read(HOME)) < 16_000


def test_readme_does_not_become_a_proposition_archive() -> None:
    text = read(README)
    proposition_mentions = re.findall(r"\bP\d{1,3}\b", text)
    assert len(proposition_mentions) <= 4
    assert "Detailed Proposition Record" in text
    assert "Research Map" in text
    assert "Start Here" in text


def test_start_here_hands_off_to_the_research_map() -> None:
    text = read(START_HERE)
    assert "Research Map" in text
    assert "Technical Research Architecture" in text
    assert "Detailed Proposition Record" in text
    assert "You do not need to read 87 propositions" in text


def test_research_map_organizes_by_questions_not_full_history() -> None:
    text = read(RESEARCH_MAP)
    lowered = text.lower()
    for chapter in range(1, 7):
        assert f"Chapter {chapter}:" in text
    assert "Detailed proposition record" in text
    assert "Theorem Roadmap" in text
    assert "final bridge remains open" in lowered


def test_home_page_offers_clear_depth_choices() -> None:
    text = read(HOME)
    for phrase in (
        "Start Here",
        "Research Map",
        "Physics and Mathematics",
        "Visual Atlas",
        "The final bridge remains open",
    ):
        assert phrase in text
