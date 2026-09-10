from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "proposition_46_budget_constrained_witness_graph.md"
FIGURE = ROOT / "docs" / "figures" / "p46_budget_constrained_witness_graph.svg"


def test_p46_document_exposes_core_theorem_chain():
    text = DOC.read_text(encoding="utf-8")
    for token in (
        "P46A: monotonicity and supermodularity",
        "P46B: computational hardness",
        "P46C: weighted-degree upper bound",
        "P46D: a posteriori optimality certificate",
        "P46E: exact small-instance solution",
        "P46 budgeted witness selection is NP-hard",
        "fractional degree knapsack",
        "does not establish that quantum mechanics is incomplete",
    ):
        assert token in text


def test_p46_publication_map_exists_and_preserves_boundary():
    text = FIGURE.read_text(encoding="utf-8")
    assert "P46 Budget-Constrained Witness-Graph Selection" in text
    assert "NP-hard optimization" in text
    assert "P45 precision allocation" in text
    assert "Scientific scope remains descriptor-relative" in text
