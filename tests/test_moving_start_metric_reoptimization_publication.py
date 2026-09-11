from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_p56_is_visible_on_main_page():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    for token in (
        "**Proposition 56**",
        "p56_moving_start_metric_reoptimization_stability.svg",
        "moving_start_metric_reoptimization.py",
        "test_moving_start_metric_reoptimization.py",
    ):
        assert token in text


def test_p56_is_in_public_research_maps():
    roadmap = (ROOT / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")
    navigation = (ROOT / "docs" / "research_navigation.md").read_text(encoding="utf-8")
    equations = (ROOT / "docs" / "equation_and_citation_map.md").read_text(encoding="utf-8")
    assert "[P56](proposition_56_moving_start_metric_reoptimization_stability.md)" in roadmap
    assert "| P56 | [Moving-start metric reoptimization stability]" in navigation
    assert "# 45. P56 moving-start metric reoptimization stability" in equations
