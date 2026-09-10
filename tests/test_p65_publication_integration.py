from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p65_remains_integrated_in_public_record():
    required = {
        "README.md": [
            "Proposition 65",
            "p65_lower_bounded_heterogeneous_calibration.svg",
            "lower-bounded heterogeneous calibration",
        ],
        "docs/theorem_roadmap.md": [
            "P65",
            "proposition_65_lower_bounded_heterogeneous_calibration.md",
            "p65_lower_bounded_heterogeneous_calibration.svg",
        ],
        "docs/research_navigation.md": [
            "proposition_65_lower_bounded_heterogeneous_calibration.md",
        ],
        "docs/equation_and_citation_map.md": [
            "P65 lower-bounded heterogeneous calibration",
            "n_e^*=\\max",
            "\\sqrt2",
        ],
        "website/index.html": [
            "P65",
            "Baseline-safe water filling",
        ],
        "website/research-map.html": [
            "P62-P68",
            "Heterogeneous-cost calibration",
        ],
        "CITATION.cff": ["lower-bounded heterogeneous calibration"],
        "pyproject.toml": ["lower-bounded heterogeneous calibration"],
        "CHANGELOG.md": [
            "# 0.65.0 - 2026-09-10",
            "P65 lower-bounded heterogeneous calibration",
        ],
    }

    for path, tokens in required.items():
        text = _read(path)
        for token in tokens:
            assert token in text, f"{path} missing historical P65 token: {token}"


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
