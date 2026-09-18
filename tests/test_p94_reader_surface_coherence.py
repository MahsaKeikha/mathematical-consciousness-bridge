from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p94_formal_record_is_complete() -> None:
    proof = _read("docs/proposition_94_finite_range_dependent_sign_coherence.md")
    assert "common marginal" in proof.lower()
    assert "3246" in proof and "4869" in proof
    assert r"-\frac{2145}{281474976710656}" in proof
    assert "physical-to-experiential bridge" in proof.lower()
    for path in (
        "docs/p94_equation_provenance.md",
        "docs/figures/p94_finite_range_dependent_sign_coherence.svg",
        "src/consciousness_bridge/finite_range_dependent_sign_coherence.py",
        "src/consciousness_bridge/finite_range_dependent_sign_coherence_threshold.py",
        "tests/test_finite_range_dependent_sign_coherence.py",
    ):
        assert (ROOT / path).is_file()


def test_p94_remains_visible_below_later_frontiers() -> None:
    home = _read("website/index.html")
    atlas = _read("website/visual-atlas.html")
    plain = _read("website/plain-language.html")
    start = _read("website/start-here.html")
    research = _read("website/research-map.html")
    assert 'id="p94-frontier"' not in home
    assert atlas.index('id="p99-frontier"') < atlas.index('id="p98-frontier"')
    assert atlas.index('id="p98-frontier"') < atlas.index('id="p97-frontier"')
    assert atlas.index('id="p97-frontier"') < atlas.index('id="p96-frontier"')
    assert atlas.index('id="p96-frontier"') < atlas.index('id="p95-frontier"')
    assert atlas.index('id="p95-frontier"') < atlas.index('id="p94-frontier"')
    assert "Historical theorem frontier · P94" in atlas
    assert 'id="p94-reader-frontier"' not in plain
    assert 'id="p94-reader-frontier"' in start
    assert 'id="p94-research-map"' in research
    assert "100 linked results · technical endpoint P100" in plain
    assert "100 results · current frontier P100" in start


def test_p94_drift_boundary_is_preserved_on_historical_surfaces() -> None:
    for path in (
        "docs/proposition_94_finite_range_dependent_sign_coherence.md",
        "website/start-here.html",
        "website/research-map.html",
    ):
        text = _read(path).lower()
        assert "p94" in text
        assert "drift" in text
        assert "physical-to-experiential bridge" in text
