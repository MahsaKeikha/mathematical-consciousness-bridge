from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_p64_layered_publication_route() -> None:
    root = Path(__file__).resolve().parents[1]
    proof = root / "docs" / "proposition_64_fast_heterogeneous_integer_approximation.md"
    figure = root / "docs" / "figures" / "p64_fast_heterogeneous_integer_approximation.svg"
    source = root / "src" / "consciousness_bridge" / "fast_heterogeneous_integer_approximation.py"
    algorithm_test = root / "tests" / "test_fast_heterogeneous_integer_approximation.py"
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
