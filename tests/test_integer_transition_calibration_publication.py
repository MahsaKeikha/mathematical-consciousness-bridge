from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_p60_layered_publication_route() -> None:
    root = Path(__file__).resolve().parents[1]
    proof = root / "docs" / "proposition_60_integer_transition_calibration.md"
    figure = root / "docs" / "figures" / "p60_integer_transition_calibration.svg"
    source = root / "src" / "consciousness_bridge" / "integer_transition_calibration.py"
    algorithm_test = root / "tests" / "test_integer_transition_calibration.py"
    record = (root / "docs" / "detailed_proposition_record.md").read_text(encoding="utf-8")
    catalog = (root / "docs" / "figure_catalog.md").read_text(encoding="utf-8")
    readme = (root / "README.md").read_text(encoding="utf-8")

    for artifact in (proof, figure, source, algorithm_test):
        assert artifact.is_file(), artifact
    assert proof.name in record
    assert figure.name in catalog
    assert "docs/detailed_proposition_record.md" in readme
    assert "docs/figure_catalog.md" in readme
