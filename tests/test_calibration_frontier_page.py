from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")
FRONTIER = (ROOT / "docs" / "calibration_optimization_frontier_p61_p70.md").read_text(encoding="utf-8")




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
