from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p91_proof_states_exact_global_bracket_and_boundary() -> None:
    text = _read("docs/proposition_91_mixed_prevalence_rank_two_flattening_separation.md")
    lower = text.lower()
    assert "1/42" in text
    assert "1/24" in text
    assert "rank at most two" in lower
    assert "does **not** prove" in text
    assert "exact global" in lower or "exact distance" in lower
    assert "1/24" in text
    assert "physical-to-experiential bridge remains open" in lower


def test_p91_homepage_is_current_and_links_complete_record() -> None:
    text = _read("website/index.html")
    assert 'id="p91-frontier"' in text
    assert "Current theorem frontier · P91" in text
    assert "p91_mixed_prevalence_rank_two_flattening_separation.svg" in text
    assert "proposition_91_mixed_prevalence_rank_two_flattening_separation.md" in text
    assert "p91_equation_provenance.md" in text
    assert "mixed_prevalence_rank_two_flattening_separation.py" in text
    assert "test_mixed_prevalence_rank_two_flattening_separation.py" in text
    assert "1/42" in text and "1/24" in text


def test_visual_atlas_orders_p91_before_historical_p90_and_p89() -> None:
    text = _read("website/visual-atlas.html")
    p91 = text.index('id="p91-frontier"')
    p90 = text.index('id="p90-frontier"')
    p89 = text.index('id="p89-frontier"')
    assert p91 < p90 < p89
    assert "p91_mixed_prevalence_rank_two_flattening_separation.svg" in text[p91:p90]


def test_p91_reader_surfaces_preserve_scientific_boundary() -> None:
    for path in ("README.md", "website/index.html", "website/plain-language.html"):
        text = _read(path).lower()
        assert "p91" in text
        assert "physical-to-experiential bridge" in text


def test_p91_research_map_top_level_orientation_is_current() -> None:
    text = _read("website/research-map.html")
    summary = (
        "P89 closes the complete real linear parity-functional class, P90 adds exact "
        "nonlinear single-component separation, and P91 extends nonlinear separation "
        "to arbitrary latent mixing through a rank-two flattening certificate."
    )
    assert "Ninety-one results, one dependency-aware scientific program" in text
    assert "through Proposition 91" in text
    assert "P71-P91" in text
    assert "P73-P91" in text
    assert "P78-P91" in text
    assert "culminating in P91 mixed-prevalence rank-two flattening separation" in text
    assert "Current Research II model-audit range: P75-P91." in text
    assert "Historical P90 figure" in text
    assert "Historical exact frontier · P87" in text
    assert "Continuous-model certification lineage" in text
    assert "P77-P91: from full-law rejection to nonlinear mixed-prevalence certification" in text
    assert "Continue to the current P91 frontier" in text
    assert text.count(summary) == 1

    p90 = text.index('id="p90-research-map"')
    p91 = text.index('id="p91-research-map"')
    closing_main = text.index("</main>")
    closing_html = text.index("</html>")
    assert p90 < p91 < closing_main < closing_html

    stale = (
        "through Proposition 88.",
        "Eighty-eight results, one dependency-aware scientific program",
        "<strong>88</strong><span>proposition-level results</span>",
        "culminating in P88 exact radius-three bounded primitive four-event shared-parameter parity-functional separation",
        "Current Research II model-audit range: P75-P90.",
        '<a href="index.html#p90-frontier">Current frontier</a>',
        "Current exact frontier · P87",
        "Current continuous-model frontier",
        "P77-P87: from full-law rejection to exact dependency-aware certification",
        "Continue to the current P89 frontier",
    )
    for marker in stale:
        assert marker not in text


def test_p91_workflows_are_read_only_publication_gates() -> None:
    figures = _read(".github/workflows/figures.yml")
    validator = _read(".github/workflows/validate-research-three-website.yml")
    for text in (figures, validator):
        assert "contents: read" in text
        assert "contents: write" not in text
        assert "git push origin HEAD:p91-mixed-prevalence-rank-two-flattening" not in text
    assert "migrate-p91-reader-surfaces" not in figures
    assert "finalize-p91-reader-surface" not in figures
