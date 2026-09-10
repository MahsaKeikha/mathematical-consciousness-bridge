from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p66_is_integrated_across_public_record():
    required = {
        "README.md": [
            "version-0.66.0-2563eb",
            "66 proposition-level results",
            "Proposition 66",
            "p66_residual_exact_calibration_augmentation.svg",
        ],
        "docs/theorem_roadmap.md": [
            "P66",
            "proposition_66_residual_exact_calibration_augmentation.md",
            "p66_residual_exact_calibration_augmentation.svg",
        ],
        "docs/research_navigation.md": [
            "P1 through P66",
            "proposition_66_residual_exact_calibration_augmentation.md",
        ],
        "docs/equation_and_citation_map.md": [
            "P66 residual-exact calibration augmentation",
            "R=B-\\sum_ec_ef_e",
            "r_{66}",
        ],
        "website/index.html": [
            "<strong>66</strong><span>proposition-level results</span>",
            "<strong>v0.66.0</strong><span>current documented release</span>",
            "P66",
        ],
        "website/research-map.html": [
            "P54-P66",
            "P62-P66",
        ],
        "CITATION.cff": [
            "version: 0.66.0",
            "residual-exact calibration augmentation",
        ],
        "pyproject.toml": [
            'version = "0.66.0"',
            "residual-exact calibration augmentation",
        ],
        "CHANGELOG.md": [
            "# 0.66.0 - 2026-09-10",
            "P66 residual-exact calibration augmentation",
        ],
    }

    for path, tokens in required.items():
        text = _read(path)
        for token in tokens:
            assert token in text, f"{path} missing P66 publication token: {token}"


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
