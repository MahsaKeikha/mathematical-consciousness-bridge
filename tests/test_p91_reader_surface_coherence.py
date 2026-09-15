from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p91_proof_states_exact_global_bracket_and_boundary() -> None:
    text = _read("docs/proposition_91_mixed_prevalence_rank_two_flattening_separation.md")
    assert "1/42" in text
    assert "1/24" in text
    assert "rank at most two" in text.lower()
    assert "does **not** prove that `1/24` is the exact distance" in text
    assert "physical-to-experiential bridge remains open" in text


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
