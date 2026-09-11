from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p70_remains_integrated_as_historical_calibration_frontier():
    required = {
        "README.md": [
            "docs/calibration_optimization_frontier_p61_p70.md",
            "# Research at a glance",
            "# Detailed proposition record",
            "docs/quantum_foundations_and_bridge_test.md",
        ],
        "docs/calibration_optimization_frontier_p61_p70.md": [
            "Proposition 70: exact primal-dual gap decomposition",
            "p70_primal_dual_gap_decomposition.svg",
            "primal_dual_gap_decomposition.py",
            "test_primal_dual_gap_decomposition.py",
        ],
        "docs/theorem_roadmap.md": [
            "[P70](proposition_70_primal_dual_gap_decomposition.md)",
            "p70_primal_dual_gap_decomposition.svg",
            "proved primal-dual diagnostic decomposition",
        ],
        "docs/research_navigation.md": [
            "proposition_70_primal_dual_gap_decomposition.md",
            "P61-P70",
        ],
        "docs/equation_and_citation_map.md": [
            "# 59. P70 exact primal-dual gap decomposition",
            "r_e(k_e;\\lambda)",
            "U(k)-q(\\lambda)",
            "P67 sufficient global-optimality certificate conditions",
        ],
        "CHANGELOG.md": [
            "# 0.70.0 - 2026-09-10",
            "P70 exact primal-dual gap decomposition",
        ],
    }

    for path, tokens in required.items():
        text = _read(path)
        for token in tokens:
            assert token in text, f"{path} missing historical P70 token: {token}"


def test_p70_permanent_proof_code_visual_and_tests_exist():
    for path in [
        "docs/proposition_70_primal_dual_gap_decomposition.md",
        "docs/figures/p70_primal_dual_gap_decomposition.svg",
        "src/consciousness_bridge/primal_dual_gap_decomposition.py",
        "tests/test_primal_dual_gap_decomposition.py",
        "tests/test_p70_figure_geometry.py",
        "tests/test_readme_research_orientation.py",
    ]:
        assert (ROOT / path).exists(), path


def test_temporary_p70_publication_readme_and_recovery_machinery_is_absent():
    for path in [
        "scripts/publish_p70.py",
        ".github/workflows/publish-p70.yml",
        "scripts/organize_readme_p70.py",
        ".github/workflows/organize-readme-p70.yml",
        "scripts/restore_readme_after_link_fix.py",
        ".github/workflows/restore-readme-after-link-fix.yml",
    ]:
        assert not (ROOT / path).exists(), path
