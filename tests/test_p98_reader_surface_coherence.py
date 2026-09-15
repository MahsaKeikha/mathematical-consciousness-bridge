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


def test_p98_is_preserved_below_p99() -> None:
    verifier = _read("scripts/verify_repository.py")
    atlas = _read("website/visual-atlas.html")
    plain = _read("website/plain-language.html")
    start = _read("website/start-here.html")
    research = _read("website/research-map.html")

    assert 'CURRENT_FRONTIER = "P100"' in verifier
    assert atlas.index('id="p99-frontier"') < atlas.index('id="p98-frontier"')
    assert "Previous theorem frontier · P98" in atlas
    assert 'id="p98-reader-frontier"' in plain
    assert 'id="p98-reader-frontier"' in start
    assert 'id="p98-research-map"' in research
    assert research.index('id="p99-research-map"') < research.index('id="p98-research-map"')
    assert "100 results · current frontier P100" in plain
    assert "100 results · current frontier P100" in start

def test_p98_repository_audit_surfaces_preserve_history() -> None:
    readme = _read("README.md")
    roadmap = _read("docs/theorem_roadmap.md")
    navigation = _read("docs/research_navigation.md")
    reproducibility = _read("docs/reproducibility.md")
    citation = _read("CITATION.md")

    assert "The current public theorem frontier is **P100**." in readme
    assert "P98" in readme
    assert "## P98: cross-fitted selection-valid certification" in roadmap
    assert "## P99: cross-fitted e-value aggregation" in roadmap
    assert "The current documented theorem frontier is **P100**." in navigation
    assert "For P98" in navigation
    assert "p98_cross_fitted_selection_valid_certification.svg" in navigation
    assert "The current public theorem frontier is **P100**." in reproducibility
    assert "## 5. Focused audit of the current P100 frontier" in reproducibility
    assert "P98" in citation and "P99" in citation

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
