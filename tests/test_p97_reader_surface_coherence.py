from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p97_formal_record_is_complete() -> None:
    proof = _read("docs/proposition_97_simultaneous_candidate_family_selection.md")
    lower = proof.lower()
    assert "same data" in lower
    assert "finite family" in lower
    assert "simultaneous" in lower
    assert "4045" in proof and "4056" in proof
    for path in (
        "docs/p97_equation_provenance.md",
        "docs/figures/p97_simultaneous_candidate_family_selection.svg",
        "src/consciousness_bridge/simultaneous_candidate_family_selection.py",
        "tests/test_simultaneous_candidate_family_selection.py",
    ):
        assert (ROOT / path).is_file()


def test_p97_is_preserved_below_p98() -> None:
    verifier = _read("scripts/verify_repository.py")
    atlas = _read("website/visual-atlas.html")
    plain = _read("website/plain-language.html")
    start = _read("website/start-here.html")
    research = _read("website/research-map.html")

    assert 'CURRENT_FRONTIER = "P98"' in verifier
    assert atlas.index('id="p98-frontier"') < atlas.index('id="p97-frontier"')
    assert atlas.index('id="p97-frontier"') < atlas.index('id="p96-frontier"')
    assert "Previous theorem frontier · P97" in atlas
    assert 'id="p97-reader-frontier"' in plain
    assert 'id="p97-reader-frontier"' in start
    assert 'id="p97-research-map"' in research
    assert research.index('id="p98-research-map"') < research.index('id="p97-research-map"')
    assert "98 results · current frontier P98" in plain
    assert "98 results · current frontier P98" in start


def test_p97_repository_audit_surfaces_preserve_history() -> None:
    readme = _read("README.md")
    roadmap = _read("docs/theorem_roadmap.md")
    navigation = _read("docs/research_navigation.md")
    reproducibility = _read("docs/reproducibility.md")
    citation = _read("CITATION.md")

    assert "The current public theorem frontier is **P98**." in readme
    assert "P97" in readme
    assert "## P97: simultaneous finite candidate-family selection" in roadmap
    assert "## P98: cross-fitted selection-valid certification" in roadmap
    assert "The current documented theorem frontier is **P98**." in navigation
    assert "For P97" in navigation
    assert "p97_simultaneous_candidate_family_selection.svg" in navigation
    assert "The current public theorem frontier is **P98**." in reproducibility
    assert "## 5. Focused audit of the current P98 frontier" in reproducibility
    assert "P97" in citation and "P98" in citation


def test_p97_scientific_boundary_is_visible_on_historical_surfaces() -> None:
    for path in (
        "docs/proposition_97_simultaneous_candidate_family_selection.md",
        "docs/p97_equation_provenance.md",
        "website/visual-atlas.html",
        "website/plain-language.html",
        "website/start-here.html",
        "website/research-map.html",
    ):
        text = _read(path).lower()
        assert "p97" in text
        assert "finite" in text
        assert "physical-to-experiential bridge" in text


def test_p97_keeps_post_inspection_candidate_generation_outside_theorem() -> None:
    combined = "\n".join(
        _read(path).lower()
        for path in (
            "docs/proposition_97_simultaneous_candidate_family_selection.md",
            "docs/p97_equation_provenance.md",
        )
    )
    assert "predeclared" in combined
    assert "same data" in combined
    assert "new" in combined and "candidate" in combined
