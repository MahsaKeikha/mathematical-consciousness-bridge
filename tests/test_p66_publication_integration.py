from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")




def test_p66_permanent_proof_code_visual_and_tests_exist():
    for path in [
        "docs/proposition_66_residual_exact_calibration_augmentation.md",
        "docs/figures/p66_residual_exact_calibration_augmentation.svg",
        "src/consciousness_bridge/residual_exact_calibration_augmentation.py",
        "tests/test_residual_exact_calibration_augmentation.py",
        "tests/test_p66_figure_geometry.py",
    ]:
        assert (ROOT / path).exists(), path


def test_temporary_p66_publication_machinery_is_absent():
    assert not (ROOT / "scripts/publish_p66.py").exists()
    assert not (ROOT / ".github/workflows/publish-p66.yml").exists()
