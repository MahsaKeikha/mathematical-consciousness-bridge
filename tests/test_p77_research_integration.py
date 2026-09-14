import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DOCS = ROOT / "docs"
WEBSITE = ROOT / "website"


def _plain_language_section(text: str) -> str:
    start = text.index("# What this project is trying to achieve, in plain language")
    end = text.index("# Abstract", start)
    return text[start:end]


def _project_version(pyproject: str) -> tuple[int, int, int]:
    match = re.search(r'^version = "(\d+)\.(\d+)\.(\d+)"$', pyproject, re.MULTILINE)
    assert match is not None
    return tuple(int(value) for value in match.groups())


def test_p77_core_artifacts_exist() -> None:
    required = (
        DOCS / "proposition_77_full_law_model_set_separation.md",
        DOCS / "p77_equation_provenance.md",
        DOCS / "figures" / "p77_full_law_model_set_separation.svg",
        ROOT / "src" / "consciousness_bridge" / "full_law_model_set_separation.py",
        ROOT / "tests" / "test_full_law_model_set_separation.py",
        ROOT / "tests" / "test_p77_figure_geometry.py",
    )
    for path in required:
        assert path.exists(), path






def test_p77_release_history_survives_later_frontiers() -> None:
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

    assert _project_version(pyproject) >= (0, 77, 0)
    assert "# 0.77.0 - 2026-09-10" in changelog
    assert "Proposition 77" in changelog
    assert "full-law" in changelog




def test_p77_publication_contains_only_permanent_artifacts() -> None:
    assert not (ROOT / ".github" / "workflows" / "p77-publication-patch.yml").exists()
    assert not (ROOT / "scripts" / "p77_publication_patch.py").exists()
