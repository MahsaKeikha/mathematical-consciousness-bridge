from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_p59_is_visible_on_main_page():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    for token in (
        "P59 - optimal transition-calibration allocation",
        "p59_optimal_transition_calibration.svg",
        "optimal_transition_calibration.py",
        "test_optimal_transition_calibration.py",
    ):
        assert token in text


def test_p59_is_in_public_research_maps():
    roadmap = (ROOT / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")
    navigation = (ROOT / "docs" / "research_navigation.md").read_text(encoding="utf-8")
    equations = (ROOT / "docs" / "equation_and_citation_map.md").read_text(encoding="utf-8")
    assert "[P59](proposition_59_optimal_transition_calibration.md)" in roadmap
    assert "| P59 | [Optimal transition-calibration allocation]" in navigation
    assert "P59 optimal transition-calibration allocation" in equations
