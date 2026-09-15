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


def test_p91_start_here_has_no_stale_current_frontier_language() -> None:
    text = _read("website/start-here.html")
    assert "current Research II P91 frontier" in text
    assert "Open all 91 Research II results" in text
    assert "The 91 propositions are the formal theorem record of Research II" in text
    assert "P1-P91 build the mathematical conditions" in text
    assert "P75-P91 test the declared target-measurement model" in text
    assert "<span>P75-P91</span>" in text
    assert "P91 extends the nonlinear result to arbitrary latent prevalence" in text
    assert "Read P91 theorem" in text
    assert "You do not need to read 91 Research II proofs in order" in text

    stale = (
        "current Research II P90 frontier",
        "Open all 90 Research II results",
        "The 90 propositions are the formal theorem record of Research II",
        "P1-P90 build the mathematical conditions",
        "P75-P90 test the declared target-measurement model",
        "<span>P75-P90</span>",
        "P78-P90 progressively tighten global separation",
        "Read P90 theorem",
        "You do not need to read 89 Research II proofs in order",
    )
    for marker in stale:
        assert marker not in text


def test_p91_plain_language_has_current_program_count_and_checkpoint() -> None:
    text = _read("website/plain-language.html")
    assert "This is the 91-result Research II theorem program currently reaching P91." in text
    assert "A 91-result sufficiency and falsification architecture" in text
    assert "The 91-result proposition program" in text
    assert "The current theorem frontier is P91." in text
    assert "P91 is the current checkpoint, not the destination" in text
    assert "P91 is the current mathematical checkpoint" in text
    assert "shows how all 91 Research II results connect" in text
    assert 'id="p91-reader-frontier"' in text
    assert 'id="p90-reader-frontier"' in text

    stale = (
        "This is the 90-result Research II theorem program currently reaching P90.",
        "A 90-result sufficiency and falsification architecture",
        "The 90-result proposition program",
        "The current theorem frontier is P90.",
        "P90 is the current checkpoint, not the destination",
        "P90 is the current mathematical checkpoint inside a much larger research program.",
        "shows how all 90 Research II results connect",
    )
    for marker in stale:
        assert marker not in text


def test_p91_research_map_top_level_orientation_is_current() -> None:
    text = _read("website/research-map.html")
    assert 'content="Scientific dependency map of the Mathematical Consciousness Bridge through Proposition 91."' in text
    assert "Ninety-one results, one dependency-aware scientific program" in text
    assert "<strong>91</strong><span>proposition-level results</span>" in text
    assert "<span>6 · P73-P91</span>" in text
    assert "culminating in P91 mixed-prevalence rank-two flattening separation" in text
    assert 'id="p91-research-map"' in text

    stale = (
        "through Proposition 88",
        "Eighty-eight results, one dependency-aware scientific program",
        "<strong>88</strong><span>proposition-level results</span>",
        "<span>6 · P73-P88</span>",
        "culminating in P88 exact radius-three bounded primitive four-event shared-parameter parity-functional separation",
    )
    for marker in stale:
        assert marker not in text


def test_p91_reader_surfaces_preserve_scientific_boundary() -> None:
    for path in (
        "README.md",
        "website/index.html",
        "website/plain-language.html",
        "website/start-here.html",
        "website/research-map.html",
    ):
        text = _read(path).lower()
        assert "p91" in text
        assert "physical-to-experiential bridge" in text
