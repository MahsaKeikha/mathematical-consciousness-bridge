from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "proposition_55_pruning_aware_switching_monotonicity.md"
FIGURE = ROOT / "docs" / "figures" / "p55_pruning_aware_switching_monotonicity.svg"


def test_p55_documentation_exposes_core_results():
    text = DOC.read_text(encoding="utf-8")
    for phrase in (
        "Proposition 55A",
        "Proposition 55B",
        "Proposition 55C",
        "Proposition 55D",
        "exact optimal cost-release decomposition",
        "Scientific boundary",
    ):
        assert phrase in text


def test_p55_visual_and_proof_to_code_path_are_public():
    text = DOC.read_text(encoding="utf-8")
    for token in (
        "pruning_aware_switching_monotonicity.py",
        "test_pruning_aware_switching_monotonicity.py",
        "p55_pruning_aware_switching_monotonicity.svg",
    ):
        assert token in text
    assert FIGURE.exists()


def test_p55_layered_publication_route() -> None:
    root = Path(__file__).resolve().parents[1]
    proof = root / "docs" / "proposition_55_pruning_aware_switching_monotonicity.md"
    figure = root / "docs" / "figures" / "p55_pruning_aware_switching_monotonicity.svg"
    source = root / "src" / "consciousness_bridge" / "pruning_aware_switching_monotonicity.py"
    algorithm_test = root / "tests" / "test_pruning_aware_switching_monotonicity.py"
    record = (root / "docs" / "detailed_proposition_record.md").read_text(encoding="utf-8")
    catalog = (root / "docs" / "figure_catalog.md").read_text(encoding="utf-8")
    readme = (root / "README.md").read_text(encoding="utf-8")

    for artifact in (proof, figure, source, algorithm_test):
        assert artifact.is_file(), artifact
    assert proof.name in record
    assert figure.name in catalog
    assert "docs/detailed_proposition_record.md" in readme
    assert "docs/figure_catalog.md" in readme
