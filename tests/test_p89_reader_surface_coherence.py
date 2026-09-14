from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEBSITE = ROOT / "website"


def _page(name: str) -> str:
    return (WEBSITE / name).read_text(encoding="utf-8")


def test_overview_balances_three_stages_at_p89():
    text = _page("index.html")
    research_i = text.index('id="research-i-overview"')
    p89 = text.index('id="p89-frontier"')
    research_iii = text.index('id="research-iii-overview"')
    reader_paths = text.index('id="reader-paths"')

    assert text.count('id="p89-frontier"') == 1
    assert "Explore all 89 results" in text
    assert "Research II · Current theorem frontier · P89" in text
    assert "P89 current theorem frontier · v0.82.0" in text
    assert "The 89 results form several dependency branches." in text
    assert "all 89 propositions" in text
    assert research_i < p89 < research_iii < reader_paths
    assert "physics_pipeline.svg" in text[research_i:p89]
    assert "p89_complete_linear_parity_duality.svg" in text[p89:research_iii]
    assert "measurement_architecture.svg" in text[research_iii:reader_paths]

    for historical_id in (
        'id="p88-frontier"',
        'id="p87-frontier"',
        'id="p86-frontier"',
        'id="p85-frontier"',
    ):
        assert historical_id not in text


def test_plain_language_keeps_all_three_research_stages_primary():
    text = _page("plain-language.html")

    assert '<strong>Research I</strong><span>physical-system identification</span>' in text
    assert '<strong>Research II</strong><span>89 results · current frontier P89</span>' in text
    assert '<strong>Research III</strong><span>measurement science under uncertainty</span>' in text
    assert 'id="three-stage-progress"' in text
    assert "What the whole research program is doing" in text
    assert text.index("Research I") < text.index("Research II") < text.index("Research III")
    assert "The proposition sequence belongs to Research II. It is one stage of a larger program" in text
    assert 'id="p89-reader-frontier"' in text
    assert "Research II · Current exact frontier · P89" in text
    assert "L88 = 1/64 &lt; L89 = 5/168" in text

    assert "What the 88 results are doing" not in text
    assert "<strong>88</strong><span>Research II proposition-level results</span>" not in text
    assert "<strong>P88</strong><span>current Research II theorem frontier</span>" not in text


def test_start_here_orients_to_three_stages_before_research_ii_chronology():
    text = _page("start-here.html")

    assert '<strong>Research I</strong><span>physical-system identification</span>' in text
    assert '<strong>Research II</strong><span>89 results · current frontier P89</span>' in text
    assert '<strong>Research III</strong><span>measurement science under uncertainty</span>' in text
    assert 'id="program-stages"' in text
    assert "Start with the three stages before entering the proposition chronology" in text
    assert "The 89 Research II propositions by scientific role" in text
    assert "Inside Research II" in text
    assert "Research II · Current certified frontier" in text
    assert "P78-P89 progressively tighten global separation" in text
    assert "P89 closes the complete real linear parity-functional class" in text
    assert "Formal repository release:</strong> v0.82.0" in text

    program_stages = text.index('id="program-stages"')
    chain = text.index('id="chain"')
    assert program_stages < chain

    assert "the 88-result theorem program and current P88 frontier" not in text
    assert "The 88 propositions by scientific role" not in text


def test_research_map_exposes_p89_as_current_research_ii_frontier():
    text = _page("research-map.html")
    assert text.count('id="p89-research-map"') == 1
    assert "P89: What is the strongest possible real linear certificate" in text
    assert "5/168" in text
    assert "1/64" in text
    assert "complete real linear" in text.lower()


def test_visual_atlas_leads_with_p89_and_keeps_p88_historical():
    text = _page("visual-atlas.html")
    p89 = text.index('id="p89-frontier"')
    p88 = text.index('id="p88-frontier"')
    p87 = text.index('id="p87-frontier"')

    assert text.count('id="p89-frontier"') == 1
    assert "<!-- current-frontier-visual: P89 -->" in text
    assert 'id="p89-frontier" class="theorem-frontier current-frontier-visual"' in text
    assert "Current theorem frontier · P89" in text[p89:p88]
    assert "p89_complete_linear_parity_duality.svg" in text[p89:p88]
    assert "5/168" in text[p89:p88]
    assert p89 < p88 < p87
    assert "Previous theorem frontier · P88" in text[p88:p87]
    assert '<section id="p88-frontier" class="theorem-frontier current-frontier-visual">' not in text
