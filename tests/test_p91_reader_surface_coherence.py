from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p91_proof_remains_historically_auditable() -> None:
    text = _read("docs/proposition_91_mixed_prevalence_rank_two_flattening_separation.md")
    assert "1/42" in text
    assert "1/24" in text
    assert "rank at most two" in text.lower()
    assert "physical-to-experiential bridge remains open" in text.lower()


def test_p91_visual_record_is_preserved_below_p92() -> None:
    text = _read("website/visual-atlas.html")
    p92 = text.index('id="p92-frontier"')
    p91 = text.index('id="p91-frontier"')
    p90 = text.index('id="p90-frontier"')
    assert p92 < p91 < p90
    assert "p91_mixed_prevalence_rank_two_flattening_separation.svg" in text[p91:p90]


def test_p91_is_not_still_declared_current() -> None:
    for path in ("README.md", "docs/research_navigation.md", "docs/theorem_roadmap.md", "website/index.html"):
        text = _read(path)
        assert "current public theorem frontier is **P91**" not in text
        assert "Current theorem frontier · P91" not in text


def test_p91_scientific_boundary_is_preserved() -> None:
    for path in ("docs/proposition_91_mixed_prevalence_rank_two_flattening_separation.md", "website/research-map.html", "website/visual-atlas.html"):
        text = _read(path).lower()
        assert "p91" in text
        assert "physical-to-experiential bridge" in text or "model" in text
