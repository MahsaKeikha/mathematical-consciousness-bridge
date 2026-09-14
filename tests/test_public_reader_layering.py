from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
START_HERE = ROOT / "START_HERE.md"
RESEARCH_MAP = ROOT / "docs" / "research_map.md"
DETAILED_RECORD = ROOT / "docs" / "detailed_proposition_record.md"
HOME = ROOT / "website" / "index.html"
PLAIN = ROOT / "website" / "plain-language.html"
VERIFY = ROOT / "scripts" / "verify_repository.py"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def frontier() -> int:
    match = re.search(r'CURRENT_FRONTIER = "P(\d+)"', read(VERIFY))
    assert match
    return int(match.group(1))


def test_readme_is_a_front_door_not_the_complete_archive() -> None:
    text = read(README)
    required = (
        "Start here",
        "Research map",
        "Visual atlas",
        "Technical record",
        "Reproduce the work",
        "Detailed Proposition Record",
        "Theorem Roadmap",
        "Figure Catalog",
        "Equation and Citation Map",
    )
    for marker in required:
        assert marker in text
    assert "You do **not** need to read the propositions in order" in text


def test_complete_proposition_chain_lives_in_detailed_record() -> None:
    text = read(DETAILED_RECORD)
    current = frontier()
    assert f"Complete P1 to P{current} chronology" in text
    for number in range(1, current + 1):
        assert re.search(rf"\bP{number}\b", text), f"P{number} missing"


def test_start_here_hands_off_to_deeper_research_surfaces() -> None:
    text = read(START_HERE)
    for marker in (
        "Research Map",
        "Technical Research Architecture",
        "Detailed Proposition Record",
        "Theorem Roadmap",
    ):
        assert marker in text


def test_research_map_organizes_the_program_by_scientific_questions() -> None:
    text = read(RESEARCH_MAP)
    lowered = text.lower()
    for chapter in range(1, 7):
        assert f"Chapter {chapter}:" in text
    assert "Detailed proposition record" in text
    assert "Theorem Roadmap" in text
    assert "final bridge remains open" in lowered


def test_website_offers_multiple_reader_depths_without_hiding_boundaries() -> None:
    home = read(HOME)
    plain = read(PLAIN)
    for phrase in (
        "Start Here",
        "Research Map",
        "Physics and Mathematics",
        "Visual Atlas",
    ):
        assert phrase in home
    assert "The final bridge remains open" in home
    assert "No technical background required" in plain
    assert "Research I" in plain
    assert "Research II" in plain
    assert "Research III" in plain
    assert "final physical-to-experiential bridge" in plain
