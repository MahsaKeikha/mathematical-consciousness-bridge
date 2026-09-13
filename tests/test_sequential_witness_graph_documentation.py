from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "proposition_47_anytime_sequential_witness_graph.md"
FIGURE = ROOT / "docs" / "figures" / "p47_sequential_graph_refinement.svg"


def test_p47_documentation_exposes_core_theorem_objects():
    text = DOC.read_text(encoding="utf-8")
    for phrase in (
        "Proposition 47A",
        "Proposition 47B",
        "Proposition 47C",
        "Proposition 47D",
        "Proposition 47E",
        "Proposition 47F",
        "adaptive local-count substitution",
        "safe elimination",
        "Scientific boundary",
    ):
        assert phrase in text


def test_p47_layered_publication_route() -> None:
    root = Path(__file__).resolve().parents[1]
    proof = root / "docs" / "proposition_47_anytime_sequential_witness_graph.md"
    figure = root / "docs" / "figures" / "p47_sequential_graph_refinement.svg"
    source = root / "src" / "consciousness_bridge" / "sequential_witness_graph.py"
    algorithm_test = root / "tests" / "test_sequential_witness_graph.py"
    record = (root / "docs" / "detailed_proposition_record.md").read_text(encoding="utf-8")
    catalog = (root / "docs" / "figure_catalog.md").read_text(encoding="utf-8")
    readme = (root / "README.md").read_text(encoding="utf-8")

    for artifact in (proof, figure, source, algorithm_test):
        assert artifact.is_file(), artifact
    assert proof.name in record
    assert figure.name in catalog
    assert "docs/detailed_proposition_record.md" in readme
    assert "docs/figure_catalog.md" in readme
