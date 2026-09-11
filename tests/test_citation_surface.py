import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
CFF = ROOT / "CITATION.cff"
BIB = ROOT / "CITATION.bib"
GUIDE = ROOT / "CITATION.md"
PYPROJECT = ROOT / "pyproject.toml"


def _project_version() -> str:
    text = PYPROJECT.read_text(encoding="utf-8")
    match = re.search(r'^version\s*=\s*"([^"]+)"', text, flags=re.MULTILINE)
    assert match is not None
    return match.group(1)


def _frontier() -> int:
    numbers = []
    for path in (ROOT / "docs").glob("proposition_*_*.md"):
        match = re.match(r"proposition_(\d+)_", path.name)
        if match:
            numbers.append(int(match.group(1)))
    assert numbers
    return max(numbers)


def test_main_page_ends_with_professional_citation_section() -> None:
    text = README.read_text(encoding="utf-8")
    version = _project_version()
    assert "# Citation" in text
    assert "## Preferred scholarly citation" in text
    assert "## BibTeX" in text
    assert "Keikha, M. (2026)" in text
    assert f"Version {version}" in text
    assert "CITATION.md" in text
    assert "CITATION.cff" in text
    assert "CITATION.bib" in text
    assert text.rstrip().endswith("**[BibTeX](CITATION.bib)**")


def test_machine_readable_citation_metadata_has_preferred_research_citation() -> None:
    text = CFF.read_text(encoding="utf-8")
    version = _project_version()
    frontier = _frontier()
    assert "cff-version: 1.2.0" in text
    assert f"version: {version}" in text
    assert "license: MIT" in text
    assert "family-names: Keikha" in text
    assert "given-names: Mahsa" in text
    assert "preferred-citation:" in text
    assert "type: generic" in text
    assert "year: 2026" in text
    assert "Physical-to-Experiential Bridge Problem" in text
    assert "lower-bounded heterogeneous calibration" in text
    assert "primal-dual gap decomposition" in text
    assert f"Current documented theorem frontier: P{frontier}" in text
    assert 'url: "https://github.com/MahsaKeikha/mathematical-consciousness-bridge"' in text


def test_bibtex_and_citation_guide_are_present_and_version_aligned() -> None:
    bib = BIB.read_text(encoding="utf-8")
    guide = GUIDE.read_text(encoding="utf-8")
    version = _project_version()
    frontier = _frontier()
    assert "keikha2026mathematicalconsciousnessbridge" in bib
    assert f"version      = {{{version}}}" in bib
    assert "@misc" in bib
    assert "## Preferred scholarly citation" in guide
    assert "## Version-specific reproducibility" in guide
    assert "## DOI and archival status" in guide
    assert f"P{frontier}" in guide
