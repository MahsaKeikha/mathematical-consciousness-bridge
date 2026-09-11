from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
CFF = ROOT / "CITATION.cff"
BIB = ROOT / "CITATION.bib"
GUIDE = ROOT / "CITATION.md"


def test_main_page_ends_with_professional_citation_section() -> None:
    text = README.read_text(encoding="utf-8")
    assert "# Citation" in text
    assert "## Preferred scholarly citation" in text
    assert "## BibTeX" in text
    assert "Keikha, M. (2026)" in text
    assert "Version 0.70.0" in text
    assert "CITATION.md" in text
    assert "CITATION.cff" in text
    assert "CITATION.bib" in text
    assert text.rstrip().endswith("**[BibTeX](CITATION.bib)**")


def test_machine_readable_citation_metadata_has_preferred_research_citation() -> None:
    data = yaml.safe_load(CFF.read_text(encoding="utf-8"))
    assert data["cff-version"] == "1.2.0"
    assert data["version"] == "0.70.0"
    assert data["license"] == "MIT"
    assert data["authors"][0]["family-names"] == "Keikha"
    assert data["authors"][0]["given-names"] == "Mahsa"
    preferred = data["preferred-citation"]
    assert preferred["type"] == "generic"
    assert preferred["year"] == 2026
    assert "Physical-to-Experiential Bridge Problem" in preferred["title"]
    assert preferred["url"] == "https://github.com/MahsaKeikha/mathematical-consciousness-bridge"


def test_bibtex_and_citation_guide_are_present_and_version_aligned() -> None:
    bib = BIB.read_text(encoding="utf-8")
    guide = GUIDE.read_text(encoding="utf-8")
    assert "keikha2026mathematicalconsciousnessbridge" in bib
    assert "version      = {0.70.0}" in bib
    assert "@misc" in bib
    assert "## Preferred scholarly citation" in guide
    assert "## Version-specific reproducibility" in guide
    assert "## DOI and archival status" in guide
    assert "P70" in guide
