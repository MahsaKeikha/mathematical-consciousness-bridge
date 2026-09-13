from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "proposition_50_bounded_starvation_asynchronous_sampling.md"
FIGURE = ROOT / "docs" / "figures" / "p50_bounded_starvation_asynchronous_sampling.svg"


def test_p50_documentation_exposes_core_results():
    text = DOC.read_text(encoding="utf-8")
    for phrase in (
        "Proposition 50A",
        "Proposition 50B",
        "Proposition 50C",
        "Bounded-starvation condition",
        "Dynamic pruning is compatible",
        "Scientific interpretation boundary",
    ):
        assert phrase in text


def test_p50_layered_publication_route() -> None:
    root = Path(__file__).resolve().parents[1]
    proof = root / "docs" / "proposition_50_bounded_starvation_asynchronous_sampling.md"
    figure = root / "docs" / "figures" / "p50_bounded_starvation_asynchronous_sampling.svg"
    source = root / "src" / "consciousness_bridge" / "bounded_starvation_sampling.py"
    algorithm_test = root / "tests" / "test_bounded_starvation_sampling.py"
    record = (root / "docs" / "detailed_proposition_record.md").read_text(encoding="utf-8")
    catalog = (root / "docs" / "figure_catalog.md").read_text(encoding="utf-8")
    readme = (root / "README.md").read_text(encoding="utf-8")

    for artifact in (proof, figure, source, algorithm_test):
        assert artifact.is_file(), artifact
    assert proof.name in record
    assert figure.name in catalog
    assert "docs/detailed_proposition_record.md" in readme
    assert "docs/figure_catalog.md" in readme
