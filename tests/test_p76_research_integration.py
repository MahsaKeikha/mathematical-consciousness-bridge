from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DOCS = ROOT / "docs"
WEBSITE = ROOT / "website"
CHANGELOG = ROOT / "CHANGELOG.md"




def test_p76_release_and_provenance_history_is_preserved() -> None:
    changelog = CHANGELOG.read_text(encoding="utf-8")
    equation_map = (DOCS / "equation_and_citation_map.md").read_text(encoding="utf-8")
    provenance = (DOCS / "p76_equation_provenance.md").read_text(encoding="utf-8")

    assert "# 0.76.0 - 2026-09-10" in changelog
    assert "# P76 finite-sample target-model adequacy rejection" in equation_map
    assert "## Repository-specific contribution" in provenance




def test_p76_publication_contains_only_permanent_artifacts() -> None:
    assert not (ROOT / ".github" / "workflows" / "p76-publication-patch.yml").exists()
    assert not (ROOT / "scripts" / "p76_publication_patch.py").exists()
