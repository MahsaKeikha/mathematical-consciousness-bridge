from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p66_is_preserved_in_public_record():
    required = {
        "docs/calibration_optimization_frontier_p61_p70.md": ["Proposition 66", "p66_residual_exact_calibration_augmentation.svg"],
        "docs/theorem_roadmap.md": ["P66", "proposition_66_residual_exact_calibration_augmentation.md"],
        "docs/research_navigation.md": ["proposition_66_residual_exact_calibration_augmentation.md"],
        "docs/equation_and_citation_map.md": ["P66 residual-exact calibration augmentation", "r_{66}"],
        "CHANGELOG.md": ["# 0.66.0 - 2026-09-10", "P66 residual-exact calibration augmentation"],
    }

    for path, tokens in required.items():
        text = _read(path)
        for token in tokens:
            assert token in text, f"{path} missing historical P66 token: {token}"


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
