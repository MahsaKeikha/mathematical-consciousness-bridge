from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DOCS = ROOT / "docs"
WEBSITE = ROOT / "website"


def _plain_language_section(text: str) -> str:
    start = text.index("# What this project is trying to achieve, in plain language")
    end = text.index("# Abstract", start)
    return text[start:end]


def test_p78_core_artifacts_exist() -> None:
    required = (
        DOCS / "proposition_78_certified_continuous_model_separation.md",
        DOCS / "p78_equation_provenance.md",
        DOCS / "figures" / "p78_certified_continuous_model_separation.svg",
        ROOT / "src" / "consciousness_bridge" / "certified_continuous_model_separation.py",
        ROOT / "tests" / "test_certified_continuous_model_separation.py",
        ROOT / "tests" / "test_p78_figure_geometry.py",
    )
    for path in required:
        assert path.exists(), path


def test_p78_publication_contains_only_permanent_artifacts() -> None:
    assert not (ROOT / ".github" / "workflows" / "p78-publication-patch.yml").exists()
    assert not (ROOT / ".github" / "workflows" / "p78-readme-cleanup.yml").exists()
    assert not (ROOT / "scripts" / "p78_publication_patch.py").exists()
