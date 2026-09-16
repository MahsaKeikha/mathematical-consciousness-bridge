from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def test_p100_is_current_across_reader_and_publication_surfaces() -> None:
    verifier = _read("scripts/verify_repository.py")
    home = _read("website/index.html")
    atlas = _read("website/visual-atlas.html")
    plain = _read("website/plain-language.html")
    start = _read("website/start-here.html")
    research = _read("website/research-map.html")
    implementation = _read("website/implementation.html")
    readme = _read("README.md")
    roadmap = _read("docs/theorem_roadmap.md")
    navigation = _read("docs/research_navigation.md")
    reproducibility = _read("docs/reproducibility.md")
    citation = _read("CITATION.md")

    assert 'CURRENT_FRONTIER = "P100"' in verifier
    assert '<!-- current-frontier-home: P100 -->' in home
    assert 'id="p100-frontier"' in home
    assert "Current theorem frontier · P100" in home
    assert "Explore all 100 results" in home
    assert '<!-- current-frontier-visual: P100 -->' in atlas
    assert atlas.index('id="p100-frontier"') < atlas.index('id="p99-frontier"')
    assert "Previous theorem frontier · P99" in atlas
    assert 'id="p100-reader-frontier"' in plain
    assert 'id="p100-reader-frontier"' in start
    assert "100 results · current frontier P100" in plain
    assert "100 results · current frontier P100" in start
    assert 'id="p100-research-map"' in research
    assert "Current Research II model-audit range: P75-P100." in research
    assert "The current theorem frontier is P100." in research
    assert "Stage 06 · P73-P100" in implementation
    assert "P73-P100 build a continuous chain" in implementation
    assert "current P100 frontier" in implementation
    assert "P100 compounds fresh P99 round evidence" in implementation
    assert "The current public theorem frontier is **P100**." in readme
    assert "docs/proposition_100_anytime_sequential_eprocess.md" in readme
    assert "The current documented theorem frontier is **P100**." in roadmap
    assert "P1 through P100 with explicit dependency branches" in roadmap
    assert "## P100: anytime-valid sequential e-process" in roadmap
    assert "## After P100" in roadmap
    assert "The current documented theorem frontier is **P100**." in navigation
    assert "**Results:** P75 through P100" in navigation
    assert "For P100:" in navigation
    assert "p100_anytime_sequential_eprocess.svg" in navigation
    assert "The current public theorem frontier is **P100**." in reproducibility
    assert "## 5. Focused audit of the current P100 frontier" in reproducibility
    assert "docs/figures/p100_anytime_sequential_eprocess.svg" in reproducibility
    assert "## Current theorem frontier: P100" in citation


def test_p100_exact_checkpoint_and_scientific_boundary_are_visible() -> None:
    theorem = _read("docs/proposition_100_anytime_sequential_eprocess.md")
    provenance = _read("docs/p100_equation_provenance.md")
    source = _read("src/consciousness_bridge/anytime_sequential_eprocess.py")
    home = _read("website/index.html")
    start = _read("website/start-here.html")

    for token in ("25}{2", "27}{4", "729}{16", "30192", "30336"):
        assert token in theorem
    assert "Ville" in theorem
    assert "nonnegative supermartingale" in theorem
    assert "physical-to-experiential bridge" in theorem
    assert "standard" in provenance.lower()
    assert "repository-specific" in provenance.lower()
    assert "physical-to-experiential bridge" in source
    assert "729 / 16" in home
    assert "Exact P100 checkpoint:" in start
