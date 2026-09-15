from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p99_formal_record_is_complete() -> None:
    proof = _read("docs/proposition_99_cross_fitted_evalue_aggregation.md")
    lower = proof.lower()
    assert "e-value" in lower
    assert "markov" in lower
    assert "3774" in proof and "3792" in proof
    assert "15096" in proof and "15168" in proof
    for path in (
        "docs/p99_equation_provenance.md",
        "docs/figures/p99_cross_fitted_evalue_aggregation.svg",
        "src/consciousness_bridge/cross_fitted_evalue_aggregation.py",
        "tests/test_cross_fitted_evalue_aggregation.py",
    ):
        assert (ROOT / path).is_file()


def test_p99_is_current_reader_frontier() -> None:
    verifier = _read("scripts/verify_repository.py")
    home = _read("website/index.html")
    atlas = _read("website/visual-atlas.html")
    plain = _read("website/plain-language.html")
    start = _read("website/start-here.html")
    research = _read("website/research-map.html")

    assert 'CURRENT_FRONTIER = "P99"' in verifier
    assert '<!-- current-frontier-home: P99 -->' in home
    assert 'id="p99-frontier"' in home
    assert "Current theorem frontier · P99" in home
    assert "Explore all 99 results" in home
    assert '<!-- current-frontier-visual: P99 -->' in atlas
    assert atlas.index('id="p99-frontier"') < atlas.index('id="p98-frontier"')
    assert "Previous theorem frontier · P98" in atlas
    assert 'id="p99-reader-frontier"' in plain
    assert 'id="p99-reader-frontier"' in start
    assert "99 results · current frontier P99" in plain
    assert "99 results · current frontier P99" in start
    assert 'id="p99-research-map"' in research
    assert research.index('id="p99-research-map"') < research.index('id="p98-research-map"')
    assert "Current Research II model-audit range: P75-P99." in research
    assert "The current theorem frontier is P99." in research


def test_p99_repository_audit_surfaces_are_synchronized() -> None:
    readme = _read("README.md")
    roadmap = _read("docs/theorem_roadmap.md")
    navigation = _read("docs/research_navigation.md")
    reproducibility = _read("docs/reproducibility.md")
    citation = _read("CITATION.md")

    assert "The current public theorem frontier is **P99**." in readme
    assert "docs/proposition_99_cross_fitted_evalue_aggregation.md" in readme
    assert "The current documented theorem frontier is **P99**." in roadmap
    assert "P1 through P99 with explicit dependency branches" in roadmap
    assert "## P99: cross-fitted e-value aggregation" in roadmap
    assert "## After P99" in roadmap
    assert "The current documented theorem frontier is **P99**." in navigation
    assert "**Results:** P75 through P99" in navigation
    assert "For P99:" in navigation
    assert "p99_cross_fitted_evalue_aggregation.svg" in navigation
    assert "The current public theorem frontier is **P99**." in reproducibility
    assert "## 5. Focused audit of the current P99 frontier" in reproducibility
    assert "docs/figures/p99_cross_fitted_evalue_aggregation.svg" in reproducibility
    assert "## Current theorem frontier: P99" in citation


def test_p99_distributed_evidence_and_boundary_are_visible() -> None:
    for path in (
        "README.md",
        "docs/proposition_99_cross_fitted_evalue_aggregation.md",
        "docs/p99_equation_provenance.md",
        "website/index.html",
        "website/plain-language.html",
        "website/start-here.html",
        "website/research-map.html",
    ):
        text = _read(path).lower()
        assert "p99" in text
        assert "e-value" in text
        assert "distributed" in text
        assert "physical-to-experiential bridge" in text


def test_p99_preserves_non_dominance_and_calibration_guards() -> None:
    combined = "\n".join(
        _read(path).lower()
        for path in (
            "docs/proposition_99_cross_fitted_evalue_aggregation.md",
            "docs/p99_equation_provenance.md",
            "README.md",
        )
    )
    assert "does not uniformly dominate" in combined
    assert "calibration" in combined
    assert "own-fold" in combined
