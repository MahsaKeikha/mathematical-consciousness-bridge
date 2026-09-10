from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p65_is_integrated_across_public_record():
    required = {
        "README.md": [
            "version-0.65.0-2563eb",
            "65 proposition-level results",
            "Proposition 65",
            "p65_lower_bounded_heterogeneous_calibration.svg",
        ],
        "docs/theorem_roadmap.md": [
            "P65",
            "proposition_65_lower_bounded_heterogeneous_calibration.md",
            "p65_lower_bounded_heterogeneous_calibration.svg",
        ],
        "docs/research_navigation.md": [
            "P1 through P65",
            "proposition_65_lower_bounded_heterogeneous_calibration.md",
        ],
        "docs/equation_and_citation_map.md": [
            "P65 lower-bounded heterogeneous calibration",
            "n_e^*=\\max",
            "\\sqrt2",
        ],
        "website/index.html": [
            "<strong>65</strong><span>proposition-level results</span>",
            "<strong>v0.65.0</strong><span>current documented release</span>",
            "P65",
        ],
        "website/research-map.html": [
            "P54-P65",
            "P62-P65",
        ],
        "CITATION.cff": ["version: 0.65.0", "lower-bounded heterogeneous calibration"],
        "pyproject.toml": ['version = "0.65.0"', "lower-bounded heterogeneous calibration"],
        "CHANGELOG.md": ["# 0.65.0 - 2026-09-10", "P65 lower-bounded heterogeneous calibration"],
    }

    for path, tokens in required.items():
        text = _read(path)
        for token in tokens:
            assert token in text, f"{path} missing P65 publication token: {token}"


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
