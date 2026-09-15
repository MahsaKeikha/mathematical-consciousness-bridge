from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p98_formal_record_is_complete() -> None:
    proof = _read("docs/proposition_98_cross_fitted_selection_valid_certification.md")
    lower = proof.lower()
    assert "cross-fitted" in lower
    assert "independent" in lower
    assert "union bound" in lower
    assert "4045" in proof and "4056" in proof
    assert "16180" in proof and "16224" in proof
    for path in (
        "docs/p98_equation_provenance.md",
        "docs/figures/p98_cross_fitted_selection_valid_certification.svg",
        "src/consciousness_bridge/cross_fitted_selection_valid_certification.py",
        "tests/test_cross_fitted_selection_valid_certification.py",
    ):
        assert (ROOT / path).is_file()


def test_p98_is_current_reader_frontier() -> None:
    verifier = _read("scripts/verify_repository.py")
    home = _read("website/index.html")
    atlas = _read("website/visual-atlas.html")
    plain = _read("website/plain-language.html")
    start = _read("website/start-here.html")
    research = _read("website/research-map.html")

    assert 'CURRENT_FRONTIER = "P98"' in verifier
    assert '<!-- current-frontier-home: P98 -->' in home
    assert 'id="p98-frontier"' in home
    assert "Current theorem frontier · P98" in home
    assert "Explore all 98 results" in home
    assert '<!-- current-frontier-visual: P98 -->' in atlas
    assert atlas.index('id="p98-frontier"') < atlas.index('id="p97-frontier"')
    assert "Previous theorem frontier · P97" in atlas
    assert 'id="p98-reader-frontier"' in plain
    assert 'id="p98-reader-frontier"' in start
    assert "98 results · current frontier P98" in plain
    assert "98 results · current frontier P98" in start
    assert 'id="p98-research-map"' in research
    assert research.index('id="p98-research-map"') < research.index('id="p97-research-map"')
    assert "Current Research II model-audit range: P75-P98." in research
    assert "The current theorem frontier is P98." in research


def test_p98_repository_audit_surfaces_are_synchronized() -> None:
    readme = _read("README.md")
    roadmap = _read("docs/theorem_roadmap.md")
    navigation = _read("docs/research_navigation.md")
    reproducibility = _read("docs/reproducibility.md")
    citation = _read("CITATION.md")

    assert "The current public theorem frontier is **P98**." in readme
    assert "docs/proposition_98_cross_fitted_selection_valid_certification.md" in readme
    assert "The current documented theorem frontier is **P98**." in roadmap
    assert "P1 through P98 with explicit dependency branches" in roadmap
    assert "## P98: cross-fitted selection-valid certification" in roadmap
    assert "## After P98" in roadmap
    assert "The current documented theorem frontier is **P98**." in navigation
    assert "**Results:** P75 through P98" in navigation
    assert "For P98:" in navigation
    assert "p98_cross_fitted_selection_valid_certification.svg" in navigation
    assert "The current public theorem frontier is **P98**." in reproducibility
    assert "## 5. Focused audit of the current P98 frontier" in reproducibility
    assert "docs/figures/p98_cross_fitted_selection_valid_certification.svg" in reproducibility
    assert "## Current theorem frontier: P98" in citation


def test_p98_scientific_boundary_is_visible() -> None:
    for path in (
        "README.md",
        "docs/proposition_98_cross_fitted_selection_valid_certification.md",
        "docs/p98_equation_provenance.md",
        "website/index.html",
        "website/plain-language.html",
        "website/start-here.html",
        "website/research-map.html",
    ):
        text = _read(path).lower()
        assert "p98" in text
        assert "independent" in text
        assert "physical-to-experiential bridge" in text


def test_p98_keeps_own_fold_leakage_and_dependent_split_outside_theorem() -> None:
    combined = "\n".join(
        _read(path).lower()
        for path in (
            "docs/proposition_98_cross_fitted_selection_valid_certification.md",
            "docs/p98_equation_provenance.md",
            "README.md",
        )
    )
    assert "own" in combined and "fold" in combined
    assert "dependent" in combined and "stream" in combined
