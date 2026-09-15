from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p96_formal_record_is_complete() -> None:
    proof = _read("docs/proposition_96_selection_valid_holdout_stratification.md")
    lower = proof.lower()
    assert "independent" in lower
    assert "holdout" in lower
    assert "frozen" in lower
    assert "3645" in proof and "3648" in proof
    for path in (
        "docs/p96_equation_provenance.md",
        "docs/figures/p96_selection_valid_holdout_stratification.svg",
        "src/consciousness_bridge/selection_valid_holdout_stratification.py",
        "tests/test_selection_valid_holdout_stratification.py",
    ):
        assert (ROOT / path).is_file()


def test_p96_is_current_reader_frontier() -> None:
    verifier = _read("scripts/verify_repository.py")
    home = _read("website/index.html")
    atlas = _read("website/visual-atlas.html")
    plain = _read("website/plain-language.html")
    start = _read("website/start-here.html")
    research = _read("website/research-map.html")

    assert 'CURRENT_FRONTIER = "P96"' in verifier
    assert '<!-- current-frontier-home: P96 -->' in home
    assert 'id="p96-frontier"' in home
    assert "Current theorem frontier · P96" in home
    assert "Explore all 96 results" in home
    assert '<!-- current-frontier-visual: P96 -->' in atlas
    assert atlas.index('id="p96-frontier"') < atlas.index('id="p95-frontier"')
    assert "Previous theorem frontier · P95" in atlas
    assert 'id="p96-reader-frontier"' in plain
    assert 'id="p96-reader-frontier"' in start
    assert "96 results · current frontier P96" in plain
    assert "96 results · current frontier P96" in start
    assert 'id="p96-research-map"' in research
    assert research.index('id="p96-research-map"') < research.index('id="p95-research-map"')
    assert "Current Research II model-audit range: P75-P96." in research
    assert "The current theorem frontier is P96." in research


def test_p96_repository_audit_surfaces_are_synchronized() -> None:
    readme = _read("README.md")
    roadmap = _read("docs/theorem_roadmap.md")
    navigation = _read("docs/research_navigation.md")
    reproducibility = _read("docs/reproducibility.md")
    citation = _read("CITATION.md")

    assert "The current public theorem frontier is **P96**." in readme
    assert "docs/proposition_96_selection_valid_holdout_stratification.md" in readme
    assert "The current documented theorem frontier is **P96**." in roadmap
    assert "P1 through P96 with explicit dependency branches" in roadmap
    assert "## P96: selection-valid holdout stratification" in roadmap
    assert "## After P96" in roadmap
    assert "The current documented theorem frontier is **P96**." in navigation
    assert "**Results:** P75 through P96" in navigation
    assert "For P96:" in navigation
    assert "p96_selection_valid_holdout_stratification.svg" in navigation
    assert "The current public theorem frontier is **P96**." in reproducibility
    assert "## 5. Focused audit of the current P96 frontier" in reproducibility
    assert "docs/figures/p96_selection_valid_holdout_stratification.svg" in reproducibility
    assert "The current documented theorem frontier is **P96**." in citation


def test_p96_scientific_boundary_is_visible() -> None:
    for path in (
        "README.md",
        "docs/proposition_96_selection_valid_holdout_stratification.md",
        "docs/p96_equation_provenance.md",
        "website/index.html",
        "website/plain-language.html",
        "website/start-here.html",
        "website/research-map.html",
    ):
        text = _read(path).lower()
        assert "p96" in text
        assert "holdout" in text
        assert "physical-to-experiential bridge" in text


def test_p96_does_not_hide_dependent_stream_split_boundary() -> None:
    combined = "\n".join(
        _read(path).lower()
        for path in (
            "docs/proposition_96_selection_valid_holdout_stratification.md",
            "docs/p96_equation_provenance.md",
            "README.md",
        )
    )
    assert "not automatically" in combined
    assert "dependent" in combined
    assert "independent holdout" in combined
