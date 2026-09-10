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


def test_p47_publication_visual_exists_and_is_linked():
    assert FIGURE.exists()
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "p47_sequential_graph_refinement.svg" in readme
    assert "P47 sequential graph refinement and stopping" in readme
