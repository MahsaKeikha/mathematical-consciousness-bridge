from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_p60_is_visible_on_main_page():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    for token in (
        "**Proposition 60**",
        "p60_integer_transition_calibration.svg",
        "integer_transition_calibration.py",
        "test_integer_transition_calibration.py",
    ):
        assert token in text


def test_p60_is_in_public_research_maps():
    roadmap = (ROOT / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")
    navigation = (ROOT / "docs" / "research_navigation.md").read_text(encoding="utf-8")
    equations = (ROOT / "docs" / "equation_and_citation_map.md").read_text(encoding="utf-8")
    assert "[P60](proposition_60_integer_transition_calibration.md)" in roadmap
    assert "| P60 | [Integer transition-calibration allocation]" in navigation
    assert "P60 integer transition-calibration allocation" in equations
