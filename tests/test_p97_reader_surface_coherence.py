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


def test_p97_is_current_reader_frontier() -> None:
    verifier = _read("scripts/verify_repository.py")
    home = _read("website/index.html")
    atlas = _read("website/visual-atlas.html")
    plain = _read("website/plain-language.html")
    start = _read("website/start-here.html")
    research = _read("website/research-map.html")

    assert 'CURRENT_FRONTIER = "P97"' in verifier
    assert '<!-- current-frontier-home: P97 -->' in home
    assert 'id="p97-frontier"' in home
    assert "Current theorem frontier · P97" in home
    assert "Explore all 97 results" in home
    assert '<!-- current-frontier-visual: P97 -->' in atlas
    assert atlas.index('id="p97-frontier"') < atlas.index('id="p96-frontier"')
    assert "Previous theorem frontier · P96" in atlas
    assert 'id="p97-reader-frontier"' in plain
    assert 'id="p97-reader-frontier"' in start
    assert "97 results · current frontier P97" in plain
    assert "97 results · current frontier P97" in start
    assert 'id="p97-research-map"' in research
    assert research.index('id="p97-research-map"') < research.index('id="p96-research-map"')
    assert "Current Research II model-audit range: P75-P97." in research
    assert "The current theorem frontier is P97." in research


def test_p97_repository_audit_surfaces_are_synchronized() -> None:
    readme = _read("README.md")
    roadmap = _read("docs/theorem_roadmap.md")
    navigation = _read("docs/research_navigation.md")
    reproducibility = _read("docs/reproducibility.md")
    citation = _read("CITATION.md")

    assert "The current public theorem frontier is **P97**." in readme
    assert "docs/proposition_97_simultaneous_candidate_family_selection.md" in readme
    assert "The current documented theorem frontier is **P97**." in roadmap
    assert "P1 through P97 with explicit dependency branches" in roadmap
    assert "## P97: simultaneous finite candidate-family selection" in roadmap
    assert "## After P97" in roadmap
    assert "The current documented theorem frontier is **P97**." in navigation
    assert "**Results:** P75 through P97" in navigation
    assert "For P97:" in navigation
    assert "p97_simultaneous_candidate_family_selection.svg" in navigation
    assert "The current public theorem frontier is **P97**." in reproducibility
    assert "## 5. Focused audit of the current P97 frontier" in reproducibility
    assert "docs/figures/p97_simultaneous_candidate_family_selection.svg" in reproducibility
    assert "## Current theorem frontier: P97" in citation


def test_p97_scientific_boundary_is_visible() -> None:
    for path in (
        "README.md",
        "docs/proposition_97_simultaneous_candidate_family_selection.md",
        "docs/p97_equation_provenance.md",
        "website/index.html",
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
            "README.md",
        )
    )
    assert "predeclared" in combined
    assert "same data" in combined
    assert "new" in combined and "candidate" in combined
