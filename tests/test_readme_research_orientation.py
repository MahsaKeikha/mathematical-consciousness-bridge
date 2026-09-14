from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DETAIL = ROOT / "docs" / "detailed_proposition_record.md"
ROADMAP = ROOT / "docs" / "theorem_roadmap.md"
VERIFY = ROOT / "scripts" / "verify_repository.py"


def _text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _frontier() -> int:
    match = re.search(r'CURRENT_FRONTIER = "P(\d+)"', _text(VERIFY))
    assert match
    return int(match.group(1))


def test_readme_follows_reader_first_scientific_order() -> None:
    text = _text(README)
    question = text.index("## The question")
    minute = text.index("## The idea in one minute")
    why = text.index("## Why this matters")
    built = text.index("## What has been built")
    visual = text.index("## Visual architecture")
    paths = text.index("## Choose your path")
    boundaries = text.index("## What this project does not claim")
    foundation = text.index("## Related physical foundation")
    citation = text.index("## Citation and license")
    assert question < minute < why < built < visual < paths < boundaries < foundation < citation


def test_front_door_explains_goal_without_pretending_to_be_the_full_paper() -> None:
    text = _text(README)
    required = (
        "Can a physical description ever be enough to explain a difference related to experience?",
        "how would we know whether a physical description is actually enough",
        "rather than merely being correlated with it",
        "does not begin by declaring a brain pattern",
        "builds a framework for testing proposed connections carefully enough that they can fail",
        "The goal is not to make the strongest possible claim",
        "The bridge remains an open scientific problem.",
    )
    for marker in required:
        assert marker in text


def test_reader_routes_cover_plain_language_visual_formal_and_audit_paths() -> None:
    text = _text(README)
    required = (
        "START_HERE.md",
        "docs/research_map.md",
        "docs/figure_catalog.md",
        "docs/research_architecture.md",
        "docs/theorem_roadmap.md",
        "docs/detailed_proposition_record.md",
        "docs/equation_and_citation_map.md",
        "docs/reproducibility.md",
        "docs/glossary.md",
    )
    for marker in required:
        assert marker in text


def test_detailed_record_preserves_complete_chronology_off_main_page() -> None:
    readme = _text(README)
    detail = _text(DETAIL)
    frontier = _frontier()
    assert "docs/detailed_proposition_record.md" in readme
    assert f"Complete P1 to P{frontier} chronology" in detail
    for number in range(1, frontier + 1):
        assert re.search(rf"\bP{number}\b", detail), f"P{number} missing from detailed record"


def test_theorem_roadmap_preserves_dependency_aware_research_structure() -> None:
    roadmap = _text(ROADMAP)
    frontier = _frontier()
    required = (
        "P1-P10",
        "P11-P18",
        "P19-P24",
        "P25-P37",
        "P38-P44",
        "P45-P60",
        "P61-P70",
        f"P71-P{frontier}",
    )
    for marker in required:
        assert marker in roadmap


def test_front_page_reports_current_frontier_and_release() -> None:
    text = _text(README)
    frontier = _frontier()
    assert f"current public theorem frontier is **P{frontier}**" in text
    assert f"**Public theorem frontier:** P{frontier}" in text
    assert "**Formal release:** v0.82.0" in text
    assert "**Final bridge from physical description to experience:** open" in text
