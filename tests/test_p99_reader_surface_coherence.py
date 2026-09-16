from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def test_p99_is_preserved_as_the_immediate_historical_predecessor() -> None:
    home = _read("website/index.html")
    atlas = _read("website/visual-atlas.html")
    plain = _read("website/plain-language.html")
    start = _read("website/start-here.html")
    research = _read("website/research-map.html")
    roadmap = _read("docs/theorem_roadmap.md")
    navigation = _read("docs/research_navigation.md")

    assert '<!-- current-frontier-home: P100 -->' in home
    assert 'id="p100-frontier"' in atlas
    assert 'id="p99-frontier"' in atlas
    assert atlas.index('id="p100-frontier"') < atlas.index('id="p99-frontier"')
    assert "Immediate predecessor · P99" in atlas
    assert 'id="p99-reader-frontier"' in plain
    assert 'id="p99-reader-frontier"' in start
    assert 'id="p99-research-map"' in research
    assert research.index('id="p99-research-map"') < research.index('id="p100-research-map"')
    assert "## P99: cross-fitted e-value aggregation" in roadmap
    assert "For P99:" in navigation
    assert "p99_cross_fitted_evalue_aggregation.svg" in navigation


def test_p99_exact_checkpoint_and_boundary_remain_auditable() -> None:
    theorem = _read("docs/proposition_99_cross_fitted_evalue_aggregation.md")
    source = _read("src/consciousness_bridge/cross_fitted_evalue_aggregation.py")
    tests = _read("tests/test_cross_fitted_evalue_aggregation.py")

    assert "3774" in theorem and "3792" in theorem
    assert "15096" in theorem and "15168" in theorem
    assert "physical-to-experiential bridge" in theorem
    assert "aggregate_e_value" in source
    assert "3774" in tests and "3792" in tests
