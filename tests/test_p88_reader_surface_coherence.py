from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEBSITE = ROOT / "website"


def _page(name: str) -> str:
    return (WEBSITE / name).read_text(encoding="utf-8")


def test_overview_is_canonical_88_p88_state():
    text = _page("index.html")
    p88 = text.index('id="p88-frontier"')
    p87 = text.index('id="p87-frontier"')

    assert "Explore all 88 results" in text
    assert "Current record:</strong> 88 proposition-level results through P88" in text
    assert "The 88 results form several dependency branches." in text
    assert "The 88-result program" in text
    assert "all 88 propositions" in text
    assert "Current theorem frontier · P88" in text[p88:p87]
    assert p88 < p87

    assert "Current record:</strong> 87 proposition-level results through P87" not in text
    assert "The 87 results form several dependency branches." not in text
    assert "The 87-result program" not in text
    assert "Current theorem frontier · P87" not in text


def test_plain_language_is_canonical_88_p88_state():
    text = _page("plain-language.html")
    assert "<strong>88</strong><span>proposition-level results</span>" in text
    assert "<strong>P88</strong><span>current theorem frontier</span>" in text
    assert "What the 88 results are doing" in text
    assert "Current exact frontier · P88" in text
    assert "<strong>P87</strong><span>current theorem frontier</span>" not in text
    assert "What the 87 results are doing" not in text


def test_start_here_is_canonical_88_p88_state():
    text = _page("start-here.html")
    assert "the 88-result theorem program and current P88 frontier" in text
    assert "<strong>88</strong><span>proposition-level results</span>" in text
    assert "<strong>P88</strong><span>current theorem frontier</span>" in text
    assert "You do not need to read 88 proofs in order" in text
    assert "complete 88-result dependency structure" in text

    assert "the 87-result theorem program and current P87 frontier" not in text
    assert "<strong>P87</strong><span>current theorem frontier</span>" not in text
    assert "You do not need to read 87 proofs in order" not in text


def test_research_map_is_canonical_88_p88_state():
    text = _page("research-map.html")
    assert "through Proposition 88" in text
    assert "Eighty-eight results, one dependency-aware scientific program" in text
    assert "<strong>88</strong><span>proposition-level results</span>" in text
    assert "P88: Does the next complete coefficient radius expose a stronger incompatibility?" in text
    assert "208,560 exact functionals" in text

    assert "Eighty-seven results, one dependency-aware scientific program" not in text
    assert "<div><strong>87</strong><span>proposition-level results</span></div>" not in text


def test_visual_atlas_has_one_current_frontier_and_it_is_p88():
    text = _page("visual-atlas.html")
    p88 = text.index('id="p88-frontier"')
    p87 = text.index('id="p87-frontier"')
    p86 = text.index('id="p86-frontier"')

    assert "<!-- current-frontier-visual: P88 -->" in text
    assert 'id="p88-frontier" class="theorem-frontier current-frontier-visual"' in text
    assert "L85 = 0 &lt; L86 = 1/192 &lt; L87 = 1/96 &lt; L88 = 1/64" in text[p88:p87]
    assert "radius_three_bounded_primitive_quad_projection_parity_functional_separation.py" in text[p88:p87]
    assert "test_radius_three_bounded_primitive_quad_projection_parity_functional_separation.py" in text[p88:p87]
    assert p88 < p87 < p86

    assert "<!-- current-frontier-visual: P87 -->" not in text
    assert '<section id="p87-frontier" class="theorem-frontier current-frontier-visual">' not in text
    assert '<section id="p86-frontier" class="theorem-frontier current-frontier-visual">' not in text
    assert "P86 is the current exact continuous-model frontier." not in text
