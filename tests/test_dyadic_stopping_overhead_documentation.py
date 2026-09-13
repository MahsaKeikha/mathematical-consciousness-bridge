from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "proposition_49_dyadic_stopping_overhead.md"
FIGURE = ROOT / "docs" / "figures" / "p49_dyadic_stopping_overhead.svg"


def test_p49_documentation_exposes_core_results():
    text = DOC.read_text(encoding="utf-8")
    for phrase in (
        "Proposition 49A",
        "Proposition 49B",
        "Proposition 49C",
        "Zero-gap boundary is preserved",
        "Certification-look complexity",
        "Scientific boundary",
    ):
        assert phrase in text


def test_p49_layered_publication_route() -> None:
    root = Path(__file__).resolve().parents[1]
    proof = root / "docs" / "proposition_49_dyadic_stopping_overhead.md"
    figure = root / "docs" / "figures" / "p49_dyadic_stopping_overhead.svg"
    source = root / "src" / "consciousness_bridge" / "dyadic_stopping_overhead.py"
    algorithm_test = root / "tests" / "test_dyadic_stopping_overhead.py"
    record = (root / "docs" / "detailed_proposition_record.md").read_text(encoding="utf-8")
    catalog = (root / "docs" / "figure_catalog.md").read_text(encoding="utf-8")
    readme = (root / "README.md").read_text(encoding="utf-8")

    for artifact in (proof, figure, source, algorithm_test):
        assert artifact.is_file(), artifact
    assert proof.name in record
    assert figure.name in catalog
    assert "docs/detailed_proposition_record.md" in readme
    assert "docs/figure_catalog.md" in readme
