from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")




def test_p68_permanent_proof_code_visual_and_tests_exist():
    for path in [
        "docs/proposition_68_lagrangian_optimality_gap.md",
        "docs/figures/p68_lagrangian_optimality_gap.svg",
        "src/consciousness_bridge/lagrangian_optimality_gap.py",
        "tests/test_lagrangian_optimality_gap.py",
        "tests/test_p68_figure_geometry.py",
    ]:
        assert (ROOT / path).exists(), path


def test_temporary_p68_publication_machinery_is_absent():
    assert not (ROOT / "scripts/publish_p68.py").exists()
    assert not (ROOT / ".github/workflows/publish-p68.yml").exists()
