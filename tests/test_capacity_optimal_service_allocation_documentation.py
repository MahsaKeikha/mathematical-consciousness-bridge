from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "proposition_52_capacity_optimal_service_allocation.md"
FIGURE = ROOT / "docs" / "figures" / "p52_capacity_optimal_service_allocation.svg"


def test_p52_documentation_exposes_exact_results():
    text = DOC.read_text(encoding="utf-8")
    for phrase in (
        "Proposition 52A",
        "Proposition 52B",
        "Proposition 52C",
        "Exact discrete unit-capacity result",
        "Scientific boundary",
    ):
        assert phrase in text


def test_p52_layered_publication_route() -> None:
    root = Path(__file__).resolve().parents[1]
    proof = root / "docs" / "proposition_52_capacity_optimal_service_allocation.md"
    figure = root / "docs" / "figures" / "p52_capacity_optimal_service_allocation.svg"
    source = root / "src" / "consciousness_bridge" / "capacity_optimal_service_allocation.py"
    algorithm_test = root / "tests" / "test_capacity_optimal_service_allocation.py"
    record = (root / "docs" / "detailed_proposition_record.md").read_text(encoding="utf-8")
    catalog = (root / "docs" / "figure_catalog.md").read_text(encoding="utf-8")
    readme = (root / "README.md").read_text(encoding="utf-8")

    for artifact in (proof, figure, source, algorithm_test):
        assert artifact.is_file(), artifact
    assert proof.name in record
    assert figure.name in catalog
    assert "docs/detailed_proposition_record.md" in readme
    assert "docs/figure_catalog.md" in readme
