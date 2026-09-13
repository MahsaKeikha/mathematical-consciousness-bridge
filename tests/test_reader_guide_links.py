from pathlib import Path

README = Path(__file__).resolve().parents[1] / "README.md"


def test_reader_guide_routes_each_audience_to_the_correct_layer() -> None:
    text = README.read_text(encoding="utf-8")
    required = (
        "[Start here](START_HERE.md)",
        "[Research map](docs/research_map.md)",
        "[Visual atlas](docs/figure_catalog.md)",
        "[Technical record](docs/detailed_proposition_record.md)",
        "[Reproduce the work](docs/reproducibility.md)",
        "[Theorem Roadmap](docs/theorem_roadmap.md)",
        "[Equation and Citation Map](docs/equation_and_citation_map.md)",
        "[Research Navigation](docs/research_navigation.md)",
        "[Calibration and Optimization Frontier](docs/calibration_optimization_frontier_p61_p70.md)",
    )
    for link in required:
        assert link in text


def test_compact_homepage_does_not_duplicate_the_full_proposition_ledger() -> None:
    text = README.read_text(encoding="utf-8")
    assert "docs/detailed_proposition_record.md" in text
    assert text.count("proposition_88_exact_radius_three") == 1
    assert "The bridge remains an open scientific problem." in text
