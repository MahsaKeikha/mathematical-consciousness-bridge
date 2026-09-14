from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")




def test_p65_permanent_proof_code_visual_and_tests_exist():
    for path in [
        "docs/proposition_65_lower_bounded_heterogeneous_calibration.md",
        "docs/figures/p65_lower_bounded_heterogeneous_calibration.svg",
        "src/consciousness_bridge/lower_bounded_heterogeneous_calibration.py",
        "tests/test_lower_bounded_heterogeneous_calibration.py",
        "tests/test_p65_figure_geometry.py",
    ]:
        assert (ROOT / path).exists(), path


def test_temporary_p65_publication_machinery_is_absent():
    assert not (ROOT / "scripts/publish_p65.py").exists()
    assert not (ROOT / ".github/workflows/publish-p65.yml").exists()
