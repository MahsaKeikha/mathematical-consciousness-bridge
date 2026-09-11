from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_p58_is_visible_on_main_page():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    for token in (
        "**Proposition 58**",
        "p58_finite_data_metric_uncertainty.svg",
        "finite_data_metric_uncertainty.py",
        "test_finite_data_metric_uncertainty.py",
    ):
        assert token in text


def test_p58_is_in_public_research_maps():
    roadmap = (ROOT / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")
    navigation = (ROOT / "docs" / "research_navigation.md").read_text(encoding="utf-8")
    equations = (ROOT / "docs" / "equation_and_citation_map.md").read_text(encoding="utf-8")
    assert "[P58](proposition_58_finite_data_metric_uncertainty.md)" in roadmap
    assert "| P58 | [Finite-data switching-metric uncertainty]" in navigation
    assert "# 47. P58 finite-data switching-metric uncertainty" in equations
