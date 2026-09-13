from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "proposition_53_residual_demand_reoptimization.md"
FIGURE = ROOT / "docs" / "figures" / "p53_residual_demand_reoptimization.svg"


def test_p53_documentation_exposes_core_results():
    text = DOC.read_text(encoding="utf-8")
    for phrase in (
        "Proposition 53A",
        "Proposition 53B",
        "Proposition 53C",
        "Pruning-only release",
        "Dynamic reallocation law",
        "What P53 does not prove",
    ):
        assert phrase in text


def test_p53_layered_publication_route() -> None:
    root = Path(__file__).resolve().parents[1]
    proof = root / "docs" / "proposition_53_residual_demand_reoptimization.md"
    figure = root / "docs" / "figures" / "p53_residual_demand_reoptimization.svg"
    source = root / "src" / "consciousness_bridge" / "residual_demand_reoptimization.py"
    algorithm_test = root / "tests" / "test_residual_demand_reoptimization.py"
    record = (root / "docs" / "detailed_proposition_record.md").read_text(encoding="utf-8")
    catalog = (root / "docs" / "figure_catalog.md").read_text(encoding="utf-8")
    readme = (root / "README.md").read_text(encoding="utf-8")

    for artifact in (proof, figure, source, algorithm_test):
        assert artifact.is_file(), artifact
    assert proof.name in record
    assert figure.name in catalog
    assert "docs/detailed_proposition_record.md" in readme
    assert "docs/figure_catalog.md" in readme
