from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")
FRONTIER = (ROOT / "docs" / "calibration_optimization_frontier_p61_p70.md").read_text(encoding="utf-8")


def test_main_page_links_frontier_without_embedding_p61_p70_ledger():
    assert "docs/calibration_optimization_frontier_p61_p70.md" in README
    assert "Latest proved extension: P70 exact primal-dual gap decomposition" not in README
    for figure in (
        "p61_exact_integer_transition_calibration.svg",
        "p62_heterogeneous_cost_transition_calibration.svg",
        "p63_exact_heterogeneous_integer_calibration.svg",
        "p64_fast_heterogeneous_integer_approximation.svg",
        "p65_lower_bounded_heterogeneous_calibration.svg",
        "p66_residual_exact_calibration_augmentation.svg",
        "p67_global_integer_optimality_certificate.svg",
        "p68_lagrangian_optimality_gap.svg",
        "p69_dual_optimal_multiplier.svg",
        "p70_primal_dual_gap_decomposition.svg",
    ):
        assert figure not in README
        assert figure in FRONTIER


def test_frontier_page_is_self_contained_and_auditable():
    required = (
        "# P61. Exact integer transition-calibration allocation",
        "# P62. Heterogeneous-cost transition calibration",
        "# P63. Exact heterogeneous-cost integer calibration",
        "# P64. Fast certified heterogeneous integer approximation",
        "# Proposition 65: lower-bounded heterogeneous calibration",
        "# Proposition 66: residual-exact calibration augmentation",
        "# Proposition 67: global integer optimality certificate",
        "# Proposition 68: Lagrangian optimality gap certificate",
        "# Proposition 69: certified dual-optimal multiplier search",
        "# Proposition 70: exact primal-dual gap decomposition",
        "# Interpretation boundary",
        "# P61-P70 audit table",
    )
    for token in required:
        assert token in FRONTIER
