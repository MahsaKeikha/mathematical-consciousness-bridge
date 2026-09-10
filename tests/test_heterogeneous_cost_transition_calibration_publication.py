from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_p62_is_visible_on_calibration_frontier_page():
    text = (ROOT / "docs/calibration_optimization_frontier_p61_p70.md").read_text(encoding="utf-8")
    for token in (
        "P62 heterogeneous-cost calibration",
        "p62_heterogeneous_cost_transition_calibration.svg",
        "heterogeneous_cost_transition_calibration.py",
        "test_heterogeneous_cost_transition_calibration.py",
    ):
        assert token in text


def test_p62_is_in_public_research_maps():
    roadmap = (ROOT / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")
    navigation = (ROOT / "docs" / "research_navigation.md").read_text(encoding="utf-8")
    equations = (ROOT / "docs" / "equation_and_citation_map.md").read_text(encoding="utf-8")
    assert "[P62](proposition_62_heterogeneous_cost_transition_calibration.md)" in roadmap
    assert "| P62 | [Heterogeneous-cost transition-calibration allocation]" in navigation
    assert "# 51. P62 heterogeneous-cost transition-calibration allocation" in equations
