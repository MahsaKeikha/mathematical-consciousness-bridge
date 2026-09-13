from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "proposition_51_heterogeneous_service_rate_stopping.md"
FIGURE = ROOT / "docs" / "figures" / "p51_heterogeneous_service_rate_stopping.svg"


def test_p51_documentation_exposes_core_results():
    text = DOC.read_text(encoding="utf-8")
    for phrase in (
        "Proposition 51A",
        "Proposition 51B",
        "Proposition 51C",
        "P50 is an exact special case",
        "Finite-window rate interpretation",
        "Scientific boundary",
    ):
        assert phrase in text


def test_p51_layered_publication_route() -> None:
    root = Path(__file__).resolve().parents[1]
    proof = root / "docs" / "proposition_51_heterogeneous_service_rate_stopping.md"
    figure = root / "docs" / "figures" / "p51_heterogeneous_service_rate_stopping.svg"
    source = root / "src" / "consciousness_bridge" / "heterogeneous_service_stopping.py"
    algorithm_test = root / "tests" / "test_heterogeneous_service_stopping.py"
    record = (root / "docs" / "detailed_proposition_record.md").read_text(encoding="utf-8")
    catalog = (root / "docs" / "figure_catalog.md").read_text(encoding="utf-8")
    readme = (root / "README.md").read_text(encoding="utf-8")

    for artifact in (proof, figure, source, algorithm_test):
        assert artifact.is_file(), artifact
    assert proof.name in record
    assert figure.name in catalog
    assert "docs/detailed_proposition_record.md" in readme
    assert "docs/figure_catalog.md" in readme
