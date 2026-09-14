"""Temporary migration helper for the balanced three-stage Overview.

The Overview now gives Research I, Research II, and Research III comparable
reader-facing depth. This helper updates permanent publication contracts so
historical Research II frontiers remain in specialist surfaces rather than
being required on the Overview page.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(path: str, old: str, new: str) -> None:
    text = read(path)
    if old not in text:
        if new in text:
            return
        raise RuntimeError(f"{path}: expected migration marker not found")
    write(path, text.replace(old, new, 1))


def replace_between(path: str, start: str, end: str, replacement: str) -> None:
    text = read(path)
    start_pos = text.index(start)
    end_pos = text.index(end, start_pos)
    write(path, text[:start_pos] + replacement + text[end_pos:])


def patch_promoter() -> None:
    path = "scripts/promote_p88_public_frontier.py"
    text = read(path)
    start = text.index("P88_HOME = f'''"
    end = text.index("\n\nP88_ATLAS = f'''", start)
    home = '''P88_HOME = f\'''<!-- current-frontier-home: P88 -->
<section id="p88-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head">
    <p class="eyebrow">Research II · Current theorem frontier · P88</p>
    <h2>Radius-three bounded primitive four-event parity certificate</h2>
    <p>Research II is the bridge-sufficiency and falsification layer. P88 enlarges the complete primitive four-event coefficient box from |c_i| at most 2 to |c_i| at most 3. Its 208,560-function exact audit strictly strengthens the complete P87 certificate on the same rational witness.</p>
  </div>
  <div class="theorem-figure-shell">
    <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/{P88_FIGURE}" aria-label="Open the full P88 theorem figure">
      <img loading="eager" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/{P88_FIGURE}" alt="P88 radius-three bounded primitive four-event parity certificate showing L87 equals one over 96 and L88 equals one over 64" />
    </a>
  </div>
  <div class="frontier-summary-grid">
    <article class="frontier-summary-card"><h3>Expanded exact family</h3><p>632 primitive sign-normalized coefficient patterns per four-event subset yield 208,560 exact P88 functionals.</p></article>
    <article class="frontier-summary-card"><h3>Strict hierarchy</h3><p>The exact witness has <strong>L85 = 0 &lt; L86 = 1/192 &lt; L87 = 1/96 &lt; L88 = 1/64</strong>.</p></article>
    <article class="frontier-summary-card"><h3>Reproducible record</h3><p>The proof, equation provenance, exact implementation, exhaustive tests, and theorem SVG are source controlled.</p></article>
  </div>
  <div class="boundary"><p><strong>Scientific boundary:</strong> P88 is a conditional exact model-separation theorem for the declared P75 family. It does not identify consciousness, establish nonphysicality, or close the physical-to-experiential bridge.</p></div>
  <p><a href="research-map.html">Research II map</a> · <a href="visual-atlas.html">Historical theorem figures</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P88_PROOF}">P88 theorem</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P88_PROVENANCE}">Equation provenance</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/{P88_IMPLEMENTATION}">Implementation</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/{P88_TEST}">Exact tests</a></p>
</section>

\'''\'''
    text = text[:start] + home + text[end:]
    text = text.replace(
        'text = upsert_section(text, "p88-frontier", P88_HOME, "p87-frontier")',
        'text = upsert_section(text, "p88-frontier", P88_HOME, "research-iii-overview")',
        1,
    )
    old_order = '''    if index.index('id="p88-frontier"') > index.index('id="p87-frontier"'):
        raise RuntimeError("homepage does not lead with P88")
    if atlas.index('id="p88-frontier"') > atlas.index('id="p87-frontier"'):
        raise RuntimeError("Visual Atlas does not lead with P88")
'''
    new_order = '''    research_i = index.index('id="research-i-overview"')
    p88_home = index.index('id="p88-frontier"')
    research_iii = index.index('id="research-iii-overview"')
    reader_paths = index.index('id="reader-paths"')
    if not (index.index('id="project-journey"') < research_i < p88_home < research_iii < reader_paths):
        raise RuntimeError("homepage must present Research I, Research II/P88, and Research III in balanced stage order")
    for historical_id in ('id="p87-frontier"', 'id="p86-frontier"', 'id="p85-frontier"'):
        if historical_id in index:
            raise RuntimeError("historical Research II theorem frontiers belong in the specialist archive, not the Overview")
    if atlas.index('id="p88-frontier"') > atlas.index('id="p87-frontier"'):
        raise RuntimeError("Visual Atlas does not lead with P88")
'''
    if old_order not in text:
        if new_order not in text:
            raise RuntimeError("promoter homepage ordering contract not found")
    else:
        text = text.replace(old_order, new_order, 1)
    required_anchor = '''            'id="project-journey"',
            "The whole research program in three stages",
            "None of these stages by itself establishes the final physical-to-experiential bridge.",
'''
    required_balanced = '''            'id="project-journey"',
            'id="research-i-overview"',
            'id="research-iii-overview"',
            'id="reader-paths"',
            "The whole research program in three stages",
            "Two implemented fusion regimes",
            "None of these stages by itself establishes the final physical-to-experiential bridge.",
'''
    if required_anchor in text:
        text = text.replace(required_anchor, required_balanced, 1)
    elif required_balanced not in text:
        raise RuntimeError("promoter required-marker contract not found")
    write(path, text)


def patch_figure_sync() -> None:
    path = "scripts/sync_figure_publication.py"
    text = read(path)
    old_required = '''    required_home = (
        "Explore all 88 results",
        "Research I · Physical-system identification",
        "<strong>58</strong><span>proposition-level statements</span>",
        "Research II · Bridge sufficiency and falsification",
        "<strong>88</strong><span>proposition-level results</span>",
        "P88 current theorem frontier · v0.82.0",
        "Research III · Consciousness measurement science",
        "<strong>34</strong><span>tests in each CI job</span>",
        "Open</strong><span>physical-to-experiential bridge",
        'id="p88-frontier"',
        "Current theorem frontier · P88",
        "Previous theorem frontier · P87",
    )
'''
    new_required = '''    required_home = (
        "Explore all 88 results",
        "Research I · Physical-system identification",
        "<strong>58</strong><span>proposition-level statements</span>",
        'id="research-i-overview"',
        "physics_pipeline.svg",
        "Research II · Bridge sufficiency and falsification",
        "<strong>88</strong><span>proposition-level results</span>",
        "P88 current theorem frontier · v0.82.0",
        'id="p88-frontier"',
        "Current theorem frontier · P88",
        "Research III · Consciousness measurement science",
        "<strong>34</strong><span>tests in each CI job</span>",
        'id="research-iii-overview"',
        "measurement_architecture.svg",
        "Two implemented fusion regimes",
        "Open</strong><span>physical-to-experiential bridge",
    )
'''
    if old_required in text:
        text = text.replace(old_required, new_required, 1)
    elif new_required not in text:
        raise RuntimeError("figure sync homepage marker contract not found")
    old_order = '''    if home.index('class="research-dashboard"') > home.index('id="p88-frontier"'):
        raise RuntimeError("homepage must orient readers to the full research program before P88")
    if home.index('id="p88-frontier"') > home.index('id="p87-frontier"'):
        raise RuntimeError("homepage does not lead with P88")
    if atlas.index('id="p88-frontier"') > atlas.index('id="p87-frontier"'):
        raise RuntimeError("Visual Atlas does not lead with P88")
'''
    new_order = '''    research_i = home.index('id="research-i-overview"')
    p88_home = home.index('id="p88-frontier"')
    research_iii = home.index('id="research-iii-overview"')
    if home.index('class="research-dashboard"') > research_i:
        raise RuntimeError("homepage must orient readers to the full research program before stage details")
    if not (research_i < p88_home < research_iii):
        raise RuntimeError("homepage must balance Research I, Research II/P88, and Research III in stage order")
    for historical_id in ('id="p87-frontier"', 'id="p86-frontier"', 'id="p85-frontier"'):
        if historical_id in home:
            raise RuntimeError("historical Research II frontiers must remain off the Overview")
    if atlas.index('id="p88-frontier"') > atlas.index('id="p87-frontier"'):
        raise RuntimeError("Visual Atlas does not lead with P88")
'''
    if old_order in text:
        text = text.replace(old_order, new_order, 1)
    elif new_order not in text:
        raise RuntimeError("figure sync homepage ordering contract not found")
    write(path, text)


def patch_reader_surface_test() -> None:
    path = "tests/test_p88_reader_surface_coherence.py"
    text = read(path)
    start = text.index("def test_overview_is_canonical_88_p88_state():")
    end = text.index("\ndef test_plain_language_is_canonical_88_p88_state():", start)
    replacement = '''def test_overview_is_canonical_88_p88_state():
    text = _page("index.html")
    research_i = text.index('id="research-i-overview"')
    p88 = text.index('id="p88-frontier"')
    research_iii = text.index('id="research-iii-overview"')
    reader_paths = text.index('id="reader-paths"')

    assert text.count('id="p88-frontier"') == 1
    assert "Explore all 88 results" in text
    assert "Current record:</strong> 88 proposition-level results through P88" in text
    assert "The 88 results form several dependency branches." in text
    assert "The 88-result program" in text
    assert "all 88 propositions" in text
    assert "Research II · Current theorem frontier · P88" in text
    assert research_i < p88 < research_iii < reader_paths
    assert "physics_pipeline.svg" in text[research_i:p88]
    assert "measurement_architecture.svg" in text[research_iii:reader_paths]
    assert "Two implemented fusion regimes" in text[research_iii:reader_paths]

    for historical_id in ('id="p87-frontier"', 'id="p86-frontier"', 'id="p85-frontier"'):
        assert historical_id not in text
    assert "Current record:</strong> 87 proposition-level results through P87" not in text
    assert "Current theorem frontier · P87" not in text

'''
    write(path, text[:start] + replacement + text[end + 1 :])


def patch_figure_test() -> None:
    path = "tests/test_figure_publication_sync.py"
    text = read(path)
    start = text.index("def test_homepage_leads_with_p88_before_historical_frontiers() -> None:")
    end = text.index("\ndef test_figure_publication_synchronizer_reports_zero_drift()", start)
    replacement = '''def test_homepage_balances_three_research_stages_and_keeps_history_specialist() -> None:
    text = HOME.read_text(encoding="utf-8")
    research_i = text.index('id="research-i-overview"')
    p88 = text.index('id="p88-frontier"')
    research_iii = text.index('id="research-iii-overview"')
    reader_paths = text.index('id="reader-paths"')

    assert research_i < p88 < research_iii < reader_paths
    current = text[p88:research_iii]
    assert "Current theorem frontier · P88" in current
    assert P88_FIGURE in current
    assert "L85 = 0 &lt; L86 = 1/192 &lt; L87 = 1/96 &lt; L88 = 1/64" in current
    assert "radius_three_bounded_primitive_quad_projection_parity_functional_separation.py" in current
    assert "test_radius_three_bounded_primitive_quad_projection_parity_functional_separation.py" in current
    assert "physics_pipeline.svg" in text[research_i:p88]
    assert "measurement_architecture.svg" in text[research_iii:reader_paths]
    for historical_id in ('id="p87-frontier"', 'id="p86-frontier"', 'id="p85-frontier"'):
        assert historical_id not in text
    assert "The 88 results form several dependency branches." in text
    assert "all 88 propositions" in text

'''
    text = text[:start] + replacement + text[end + 1 :]
    old_tail = '''    assert home.index('id="p88-frontier"') < home.index('id="plain-language"')
    assert home.index('id="p88-frontier"') < home.index('id="p87-frontier"')
'''
    new_tail = '''    research_i = home.index('id="research-i-overview"')
    p88 = home.index('id="p88-frontier"')
    research_iii = home.index('id="research-iii-overview"')
    reader_paths = home.index('id="reader-paths"')
    assert research_i < p88 < research_iii < reader_paths < home.index('id="plain-language"')
    for historical_id in ('id="p87-frontier"', 'id="p86-frontier"', 'id="p85-frontier"'):
        assert historical_id not in home
'''
    if old_tail in text:
        text = text.replace(old_tail, new_tail, 1)
    elif new_tail not in text:
        raise RuntimeError("figure test deployed-home contract not found")
    write(path, text)


def append_balance_contracts() -> None:
    publication = "tests/test_publication_contract_v2.py"
    text = read(publication)
    marker = "def test_overview_balances_all_three_research_stages() -> None:"
    if marker not in text:
        addition = '''

def test_overview_balances_all_three_research_stages() -> None:
    overview = _read(WEBSITE / "index.html")
    journey = overview.index('id="project-journey"')
    research_i = overview.index('id="research-i-overview"')
    research_ii = overview.index('id="p88-frontier"')
    research_iii = overview.index('id="research-iii-overview"')
    paths = overview.index('id="reader-paths"')
    assert journey < research_i < research_ii < research_iii < paths
    for token in (
        "physics_pipeline.svg",
        "Research II · Current theorem frontier · P88",
        "measurement_architecture.svg",
        "Two implemented fusion regimes",
        "Non-identification is a result",
        "Physical-to-experiential bridge remains open",
    ):
        assert token in overview
    for historical_id in ('id="p87-frontier"', 'id="p86-frontier"', 'id="p85-frontier"'):
        assert historical_id not in overview
'''
        write(publication, text.rstrip() + addition.rstrip() + "\n")

    reader = "tests/test_reader_experience.py"
    text = read(reader)
    marker = "def test_overview_gives_each_research_stage_substantive_reader_depth() -> None:"
    if marker not in text:
        addition = '''

def test_overview_gives_each_research_stage_substantive_reader_depth() -> None:
    overview = _text("website/index.html")
    research_i = overview.index('id="research-i-overview"')
    research_ii = overview.index('id="p88-frontier"')
    research_iii = overview.index('id="research-iii-overview"')
    reader_paths = overview.index('id="reader-paths"')
    assert research_i < research_ii < research_iii < reader_paths
    assert "world-tube" in overview[research_i:research_ii]
    assert "208,560" in overview[research_ii:research_iii]
    assert "partial identification" in overview[research_iii:reader_paths]
    assert "physics_pipeline.svg" in overview[research_i:research_ii]
    assert "measurement_architecture.svg" in overview[research_iii:reader_paths]
'''
        write(reader, text.rstrip() + addition.rstrip() + "\n")


def patch_figures_workflow() -> None:
    path = ".github/workflows/figures.yml"
    text = read(path)
    old = '''          python -c "from pathlib import Path; t=Path('_site/index.html').read_text(encoding='utf-8'); p=t.index('id=\\\"p88-frontier\\\"'); assert p < t.index('id=\\\"plain-language\\\"'); assert p < t.index('id=\\\"p87-frontier\\\"'); assert p < t.index('id=\\\"p86-frontier\\\"'); assert 'Current theorem frontier · P87' not in t"
'''
    new = '''          python -c "from pathlib import Path; t=Path('_site/index.html').read_text(encoding='utf-8'); r1=t.index('id=\\\"research-i-overview\\\"'); p=t.index('id=\\\"p88-frontier\\\"'); r3=t.index('id=\\\"research-iii-overview\\\"'); paths=t.index('id=\\\"reader-paths\\\"'); assert r1 < p < r3 < paths < t.index('id=\\\"plain-language\\\"'); assert all(x not in t for x in ('id=\\\"p87-frontier\\\"','id=\\\"p86-frontier\\\"','id=\\\"p85-frontier\\\"'))"
'''
    if old in text:
        text = text.replace(old, new, 1)
    elif new not in text:
        raise RuntimeError("figures workflow homepage contract not found")
    write(path, text)


def patch_research_map_link() -> None:
    replace_once("website/research-map.html", "index.html#p87-frontier", "index.html#p88-frontier")
    replace_once("tests/test_website_research_orientation.py", "'index.html#p87-frontier'", "'index.html#p88-frontier'")


def verify_overview_shape() -> None:
    index = read("website/index.html")
    expected_order = [
        'id="project-journey"',
        'id="research-i-overview"',
        'id="p88-frontier"',
        'id="research-iii-overview"',
        'id="reader-paths"',
        'id="plain-language"',
    ]
    positions = [index.index(marker) for marker in expected_order]
    if positions != sorted(positions):
        raise RuntimeError("Overview stage order is not balanced and sequential")
    if index.count("<!-- current-frontier-home: P88 -->") != 1:
        raise RuntimeError("Overview must contain exactly one P88 publication marker")
    if index.count('id="p88-frontier"') != 1:
        raise RuntimeError("Overview must contain exactly one P88 section")
    for historical_id in ('id="p87-frontier"', 'id="p86-frontier"', 'id="p85-frontier"'):
        if historical_id in index:
            raise RuntimeError("historical Research II frontiers must not dominate the Overview")


def main() -> None:
    patch_promoter()
    patch_figure_sync()
    patch_reader_surface_test()
    patch_figure_test()
    append_balance_contracts()
    patch_figures_workflow()
    patch_research_map_link()
    verify_overview_shape()


if __name__ == "__main__":
    main()
