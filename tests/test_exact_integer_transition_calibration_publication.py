from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_p61_is_visible_on_calibration_frontier_page():
    text = (ROOT / "docs/calibration_optimization_frontier_p61_p70.md").read_text(encoding="utf-8")
    for token in (
        "P61 exact integer calibration",
        "p61_exact_integer_transition_calibration.svg",
        "exact_integer_transition_calibration.py",
        "test_exact_integer_transition_calibration.py",
    ):
        assert token in text


def test_p61_is_in_public_research_maps():
    roadmap = (ROOT / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")
    navigation = (ROOT / "docs" / "research_navigation.md").read_text(encoding="utf-8")
    equations = (ROOT / "docs" / "equation_and_citation_map.md").read_text(encoding="utf-8")
    assert "[P61](proposition_61_exact_integer_transition_calibration.md)" in roadmap
    assert "| P61 | [Exact integer transition-calibration allocation]" in navigation
    assert "# 50. P61 exact integer transition-calibration allocation" in equations
