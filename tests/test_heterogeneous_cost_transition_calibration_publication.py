from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_p62_is_visible_on_calibration_frontier_page():
    text = (ROOT / "docs/calibration_optimization_frontier_p61_p70.md").read_text(encoding="utf-8")
    for token in (
        "# P62. Heterogeneous-cost transition calibration",
        "p62_heterogeneous_cost_transition_calibration.svg",
        "heterogeneous_cost_transition_calibration.py",
        "test_heterogeneous_cost_transition_calibration.py",
    ):
        assert token in text


def test_p62_layered_publication_route() -> None:
    root = Path(__file__).resolve().parents[1]
    proof = root / "docs" / "proposition_62_heterogeneous_cost_transition_calibration.md"
    figure = root / "docs" / "figures" / "p62_heterogeneous_cost_transition_calibration.svg"
    source = root / "src" / "consciousness_bridge" / "heterogeneous_cost_transition_calibration.py"
    algorithm_test = root / "tests" / "test_heterogeneous_cost_transition_calibration.py"
    record = (root / "docs" / "detailed_proposition_record.md").read_text(encoding="utf-8")
    catalog = (root / "docs" / "figure_catalog.md").read_text(encoding="utf-8")
    readme = (root / "README.md").read_text(encoding="utf-8")

    for artifact in (proof, figure, source, algorithm_test):
        assert artifact.is_file(), artifact
    assert proof.name in record
    assert figure.name in catalog
    assert "docs/detailed_proposition_record.md" in readme
    assert "docs/figure_catalog.md" in readme

    calibration = root / "docs" / "calibration_optimization_frontier_p61_p70.md"
    calibration_text = calibration.read_text(encoding="utf-8")
    assert proof.name in calibration_text
    assert figure.name in calibration_text
