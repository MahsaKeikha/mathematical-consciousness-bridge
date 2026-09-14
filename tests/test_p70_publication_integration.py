from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")




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
