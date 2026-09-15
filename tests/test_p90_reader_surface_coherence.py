from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEBSITE = ROOT / "website"
DOCS = ROOT / "docs"


def _page(name: str) -> str:
    return (WEBSITE / name).read_text(encoding="utf-8")


def test_p90_exact_theorem_record_remains_preserved() -> None:
    proof = (DOCS / "proposition_90_exact_nonlinear_rank_one_separation.md").read_text(
        encoding="utf-8"
    )
    provenance = (DOCS / "p90_equation_provenance.md").read_text(encoding="utf-8")

    assert "5/72" in proof
    assert "5/192" in proof
    assert "rank-one" in proof.lower()
    assert "5/72" in provenance
    assert (ROOT / "src/consciousness_bridge/exact_nonlinear_rank_one_separation.py").is_file()
    assert (ROOT / "tests/test_exact_nonlinear_rank_one_separation.py").is_file()
    assert (DOCS / "figures/p90_exact_nonlinear_rank_one_separation.svg").is_file()


def test_p90_is_historical_after_p91_on_visual_atlas() -> None:
    text = _page("visual-atlas.html")
    p91 = text.index('id="p91-frontier"')
    p90 = text.index('id="p90-frontier"')
    p89 = text.index('id="p89-frontier"')

    assert p91 < p90 < p89
    historical = text[p90:p89]
    assert "Previous theorem frontier · P90" in historical
    assert "p90_exact_nonlinear_rank_one_separation.svg" in historical
    assert "5/72" in historical
    assert "5/168" in historical
    assert "nonlinear" in historical.lower()
    assert "rank-one" in historical.lower()


def test_p90_remains_explicitly_distinct_from_p91_model_family() -> None:
    p91 = (DOCS / "proposition_91_mixed_prevalence_rank_two_flattening_separation.md").read_text(
        encoding="utf-8"
    )
    assert "P90 proves the exact value" in p91
    assert "single latent component" in p91
    assert "P91 allows the full two-component mixture family" in p91
    assert "must not be compared as if they optimized over the same model set" in p91


def test_p90_scientific_boundary_remains_visible() -> None:
    proof = (DOCS / "proposition_90_exact_nonlinear_rank_one_separation.md").read_text(
        encoding="utf-8"
    ).lower()
    assert "consciousness" in proof
    assert "nonphysical" in proof
    assert "physical-to-experiential bridge" in proof
