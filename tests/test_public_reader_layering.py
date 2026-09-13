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


def test_first_reader_markdown_layers_stay_compact_and_route_deeper() -> None:
    # The public website is intentionally a richer visual experience, so its byte
    # length is not used as a proxy for reader quality. The markdown entry layers
    # remain concise and hand off to deeper records deliberately.
    assert len(read(README)) < 15_000
    assert len(read(START_HERE)) < 15_000
    assert len(read(RESEARCH_MAP)) < 20_000

    readme = read(README)
    start = read(START_HERE)
    research_map = read(RESEARCH_MAP)
    assert "Choose your path" in readme
    assert "Choose how deep you want to go" in start
    assert "Detailed Proposition Record" in readme
    assert "Detailed Proposition Record" in start
    assert "Theorem Roadmap" in research_map


def test_readme_does_not_become_a_proposition_archive() -> None:
    text = read(README)
    proposition_mentions = re.findall(r"\bP\d{1,3}\b", text)
    assert len(proposition_mentions) <= 8
    assert "88 proposition-level results" in text
    assert "Detailed Proposition Record" in text
    assert "Research Map" in text
    assert "Start Here" in text


def test_start_here_hands_off_to_the_research_map() -> None:
    text = read(START_HERE)
    assert "Research Map" in text
    assert "Technical Research Architecture" in text
    assert "Detailed Proposition Record" in text
    assert "You do not need to read 88 propositions" in text
    assert "The public theorem frontier is **P88**" in text
    assert "final bridge from physical description to experience remains **open**" in text


def test_research_map_organizes_by_questions_not_full_history() -> None:
    text = read(RESEARCH_MAP)
    lowered = text.lower()
    for chapter in range(1, 7):
        assert f"Chapter {chapter}:" in text
    assert "Detailed proposition record" in text
    assert "Theorem Roadmap" in text
    assert "final bridge remains open" in lowered


def test_home_page_preserves_rich_reader_first_identity_and_depth_choices() -> None:
    text = read(HOME)
    assert "What would a scientifically testable bridge from physical description to experience actually require?" in text
    assert "Explore all 88 results" in text
    assert "Current theorem frontier · P88" in text
    assert "Previous theorem frontier · P87" in text
    assert "Every public page has one job" in text
    for phrase in (
        "Start Here",
        "Research Map",
        "Physics and Mathematics",
        "Visual Atlas",
        "The final bridge remains open",
    ):
        assert phrase in text
