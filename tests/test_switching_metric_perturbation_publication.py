from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_p57_layered_publication_route() -> None:
    root = Path(__file__).resolve().parents[1]
    proof = root / "docs" / "proposition_57_switching_metric_perturbation.md"
    figure = root / "docs" / "figures" / "p57_switching_metric_perturbation.svg"
    source = root / "src" / "consciousness_bridge" / "switching_metric_perturbation.py"
    algorithm_test = root / "tests" / "test_switching_metric_perturbation.py"
    record = (root / "docs" / "detailed_proposition_record.md").read_text(encoding="utf-8")
    catalog = (root / "docs" / "figure_catalog.md").read_text(encoding="utf-8")
    readme = (root / "README.md").read_text(encoding="utf-8")

    for artifact in (proof, figure, source, algorithm_test):
        assert artifact.is_file(), artifact
    assert proof.name in record
    assert figure.name in catalog
    assert "docs/detailed_proposition_record.md" in readme
    assert "docs/figure_catalog.md" in readme
