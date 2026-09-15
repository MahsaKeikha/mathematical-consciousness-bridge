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


def test_p96_is_immediate_reader_predecessor_of_p97() -> None:
    verifier = _read("scripts/verify_repository.py")
    atlas = _read("website/visual-atlas.html")
    plain = _read("website/plain-language.html")
    start = _read("website/start-here.html")
    research = _read("website/research-map.html")

    assert 'CURRENT_FRONTIER = "P97"' in verifier
    assert atlas.index('id="p97-frontier"') < atlas.index('id="p96-frontier"')
    assert atlas.index('id="p96-frontier"') < atlas.index('id="p95-frontier"')
    assert "Previous theorem frontier · P96" in atlas
    assert 'id="p96-reader-frontier"' in plain
    assert 'id="p96-reader-frontier"' in start
    assert 'id="p96-research-map"' in research
    assert research.index('id="p97-research-map"') < research.index('id="p96-research-map"')
    assert research.index('id="p96-research-map"') < research.index('id="p95-research-map"')


def test_p96_repository_audit_surfaces_preserve_history() -> None:
    readme = _read("README.md")
    roadmap = _read("docs/theorem_roadmap.md")
    navigation = _read("docs/research_navigation.md")
    citation = _read("CITATION.md")

    assert "P96" in readme
    assert "proposition_96_selection_valid_holdout_stratification.md" in roadmap
    assert "## P96: selection-valid holdout stratification" in roadmap
    assert "For P96" in navigation
    assert "p96_selection_valid_holdout_stratification.svg" in navigation
    assert "P96" in citation
    assert "P97" in readme and "P97" in roadmap and "P97" in navigation


def test_p96_scientific_boundary_is_visible_on_historical_surfaces() -> None:
    for path in (
        "docs/proposition_96_selection_valid_holdout_stratification.md",
        "docs/p96_equation_provenance.md",
        "website/visual-atlas.html",
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
