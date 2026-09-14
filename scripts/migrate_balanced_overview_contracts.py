"""Temporarily migrate publication contracts to the balanced three-stage Overview.

The Overview owns one substantive section for Research I, one current Research II
frontier section, and one substantive section for Research III. Historical
Research II theorem frontiers remain on specialist surfaces such as the Visual
Atlas and Research Map.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text.rstrip() + "\n", encoding="utf-8")


def replace_once(text: str, old: str, new: str, *, label: str) -> str:
    if new in text:
        return text
    if old not in text:
        raise RuntimeError(f"missing migration marker: {label}")
    return text.replace(old, new, 1)


def patch_promoter() -> None:
    path = "scripts/promote_p88_public_frontier.py"
    text = read(path)

    text = replace_once(
        text,
        '    <p class="eyebrow">Current theorem frontier · P88</p>',
        '    <p class="eyebrow">Research II · Current theorem frontier · P88</p>',
        label="P88_HOME eyebrow",
    )
    text = replace_once(
        text,
        '    <p>P88 enlarges the complete primitive four-event coefficient box from |c_i| at most 2 to |c_i| at most 3. Its 208,560-function exact audit strictly strengthens the complete P87 certificate on the same rational witness.</p>',
        '    <p>Research II is the bridge-sufficiency and falsification layer. P88 enlarges the complete primitive four-event coefficient box from |c_i| at most 2 to |c_i| at most 3. Its 208,560-function exact audit strictly strengthens the complete P87 certificate on the same rational witness.</p>',
        label="P88_HOME Research II context",
    )
    text = replace_once(
        text,
        '  <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P88_PROOF}">Open the P88 theorem</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P88_PROVENANCE}">Equation provenance</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/{P88_IMPLEMENTATION}">Implementation</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/{P88_TEST}">Exact tests</a></p>',
        '  <p><a href="research-map.html">Research II map</a> · <a href="visual-atlas.html">Historical theorem figures</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P88_PROOF}">P88 theorem</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P88_PROVENANCE}">Equation provenance</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/{P88_IMPLEMENTATION}">Implementation</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/{P88_TEST}">Exact tests</a></p>',
        label="P88_HOME specialist links",
    )
    text = replace_once(
        text,
        '    text = upsert_section(text, "p88-frontier", P88_HOME, "p87-frontier")',
        '    text = upsert_section(text, "p88-frontier", P88_HOME, "research-iii-overview")',
        label="P88_HOME insertion anchor",
    )

    old_order = """    if index.index('id=\"p88-frontier\"') > index.index('id=\"p87-frontier\"'):
        raise RuntimeError(\"homepage does not lead with P88\")
    if atlas.index('id=\"p88-frontier\"') > atlas.index('id=\"p87-frontier\"'):
        raise RuntimeError(\"Visual Atlas does not lead with P88\")
"""
    new_order = """    research_i = index.index('id=\"research-i-overview\"')
    p88_home = index.index('id=\"p88-frontier\"')
    research_iii = index.index('id=\"research-iii-overview\"')
    reader_paths = index.index('id=\"reader-paths\"')
    if not (index.index('id=\"project-journey\"') < research_i < p88_home < research_iii < reader_paths):
        raise RuntimeError(\"homepage must present Research I, Research II/P88, and Research III in balanced stage order\")
    for historical_id in ('id=\"p87-frontier\"', 'id=\"p86-frontier\"', 'id=\"p85-frontier\"'):
        if historical_id in index:
            raise RuntimeError(\"historical Research II theorem frontiers belong in the specialist archive, not the Overview\")
    if atlas.index('id=\"p88-frontier\"') > atlas.index('id=\"p87-frontier\"'):
        raise RuntimeError(\"Visual Atlas does not lead with P88\")
"""
    text = replace_once(text, old_order, new_order, label="promoter Overview ordering")

    old_required = """            'id=\"project-journey\"',
            \"The whole research program in three stages\",
            \"None of these stages by itself establishes the final physical-to-experiential bridge.\",
"""
    new_required = """            'id=\"project-journey\"',
            'id=\"research-i-overview\"',
            'id=\"research-iii-overview\"',
            'id=\"reader-paths\"',
            \"The whole research program in three stages\",
            \"Two implemented fusion regimes\",
            \"None of these stages by itself establishes the final physical-to-experiential bridge.\",
"""
    text = replace_once(text, old_required, new_required, label="promoter balanced required markers")
    write(path, text)


def patch_figure_sync() -> None:
    path = "scripts/sync_figure_publication.py"
    text = read(path)

    old_required = """    required_home = (
        \"Explore all 88 results\",
        \"Research I · Physical-system identification\",
        \"<strong>58</strong><span>proposition-level statements</span>\",
        \"Research II · Bridge sufficiency and falsification\",
        \"<strong>88</strong><span>proposition-level results</span>\",
        \"P88 current theorem frontier · v0.82.0\",
        \"Research III · Consciousness measurement science\",
        \"<strong>34</strong><span>tests in each CI job</span>\",
        \"Open</strong><span>physical-to-experiential bridge\",
        'id=\"p88-frontier\"',
        \"Current theorem frontier · P88\",
        \"Previous theorem frontier · P87\",
    )
"""
    new_required = """    required_home = (
        \"Explore all 88 results\",
        \"Research I · Physical-system identification\",
        \"<strong>58</strong><span>proposition-level statements</span>\",
        'id=\"research-i-overview\"',
        \"physics_pipeline.svg\",
        \"Research II · Bridge sufficiency and falsification\",
        \"<strong>88</strong><span>proposition-level results</span>\",
        \"P88 current theorem frontier · v0.82.0\",
        'id=\"p88-frontier\"',
        \"Current theorem frontier · P88\",
        \"Research III · Consciousness measurement science\",
        \"<strong>34</strong><span>tests in each CI job</span>\",
        'id=\"research-iii-overview\"',
        \"measurement_architecture.svg\",
        \"Two implemented fusion regimes\",
        \"Open</strong><span>physical-to-experiential bridge\",
    )
"""
    text = replace_once(text, old_required, new_required, label="figure sync required markers")

    old_order = """    if home.index('class=\"research-dashboard\"') > home.index('id=\"p88-frontier\"'):
        raise RuntimeError(\"homepage must orient readers to the full research program before P88\")
    if home.index('id=\"p88-frontier\"') > home.index('id=\"p87-frontier\"'):
        raise RuntimeError(\"homepage does not lead with P88\")
    if atlas.index('id=\"p88-frontier\"') > atlas.index('id=\"p87-frontier\"'):
        raise RuntimeError(\"Visual Atlas does not lead with P88\")
"""
    new_order = """    research_i = home.index('id=\"research-i-overview\"')
    p88_home = home.index('id=\"p88-frontier\"')
    research_iii = home.index('id=\"research-iii-overview\"')
    if home.index('class=\"research-dashboard\"') > research_i:
        raise RuntimeError(\"homepage must orient readers to the full research program before stage details\")
    if not (research_i < p88_home < research_iii):
        raise RuntimeError(\"homepage must balance Research I, Research II/P88, and Research III in stage order\")
    for historical_id in ('id=\"p87-frontier\"', 'id=\"p86-frontier\"', 'id=\"p85-frontier\"'):
        if historical_id in home:
            raise RuntimeError(\"historical Research II frontiers must remain off the Overview\")
    if atlas.index('id=\"p88-frontier\"') > atlas.index('id=\"p87-frontier\"'):
        raise RuntimeError(\"Visual Atlas does not lead with P88\")
"""
    text = replace_once(text, old_order, new_order, label="figure sync Overview ordering")
    write(path, text)


def replace_function(path: str, start_marker: str, next_marker: str, replacement: str) -> None:
    text = read(path)
    if replacement.strip() in text:
        return
    start = text.index(start_marker)
    end = text.index(next_marker, start)
    write(path, text[:start] + replacement.rstrip() + "\n\n" + text[end:])


def patch_tests() -> None:
    replace_function(
        "tests/test_p88_reader_surface_coherence.py",
        "def test_overview_is_canonical_88_p88_state():",
        "def test_plain_language_is_canonical_88_p88_state():",
        """def test_overview_is_canonical_88_p88_state():
    text = _page(\"index.html\")
    research_i = text.index('id=\"research-i-overview\"')
    p88 = text.index('id=\"p88-frontier\"')
    research_iii = text.index('id=\"research-iii-overview\"')
    reader_paths = text.index('id=\"reader-paths\"')

    assert text.count('id=\"p88-frontier\"') == 1
    assert \"Explore all 88 results\" in text
    assert \"Current record:</strong> 88 proposition-level results through P88\" in text
    assert \"The 88 results form several dependency branches.\" in text
    assert \"The 88-result program\" in text
    assert \"all 88 propositions\" in text
    assert \"Research II · Current theorem frontier · P88\" in text
    assert research_i < p88 < research_iii < reader_paths
    assert \"physics_pipeline.svg\" in text[research_i:p88]
    assert \"measurement_architecture.svg\" in text[research_iii:reader_paths]
    assert \"Two implemented fusion regimes\" in text[research_iii:reader_paths]

    for historical_id in ('id=\"p87-frontier\"', 'id=\"p86-frontier\"', 'id=\"p85-frontier\"'):
        assert historical_id not in text
    assert \"Current record:</strong> 87 proposition-level results through P87\" not in text
    assert \"Current theorem frontier · P87\" not in text
""",
    )

    replace_function(
        "tests/test_figure_publication_sync.py",
        "def test_homepage_leads_with_p88_before_historical_frontiers() -> None:",
        "def test_figure_publication_synchronizer_reports_zero_drift() -> None:",
        """def test_homepage_balances_three_research_stages_and_keeps_history_specialist() -> None:
    text = HOME.read_text(encoding=\"utf-8\")
    research_i = text.index('id=\"research-i-overview\"')
    p88 = text.index('id=\"p88-frontier\"')
    research_iii = text.index('id=\"research-iii-overview\"')
    reader_paths = text.index('id=\"reader-paths\"')

    assert research_i < p88 < research_iii < reader_paths
    current = text[p88:research_iii]
    assert \"Current theorem frontier · P88\" in current
    assert P88_FIGURE in current
    assert \"L85 = 0 &lt; L86 = 1/192 &lt; L87 = 1/96 &lt; L88 = 1/64\" in current
    assert \"radius_three_bounded_primitive_quad_projection_parity_functional_separation.py\" in current
    assert \"test_radius_three_bounded_primitive_quad_projection_parity_functional_separation.py\" in current
    assert \"physics_pipeline.svg\" in text[research_i:p88]
    assert \"measurement_architecture.svg\" in text[research_iii:reader_paths]
    for historical_id in ('id=\"p87-frontier\"', 'id=\"p86-frontier\"', 'id=\"p85-frontier\"'):
        assert historical_id not in text
    assert \"The 88 results form several dependency branches.\" in text
    assert \"all 88 propositions\" in text
""",
    )

    path = "tests/test_figure_publication_sync.py"
    text = read(path)
    old = """    assert home.index('id=\"p88-frontier\"') < home.index('id=\"plain-language\"')
    assert home.index('id=\"p88-frontier\"') < home.index('id=\"p87-frontier\"')
"""
    new = """    research_i = home.index('id=\"research-i-overview\"')
    p88 = home.index('id=\"p88-frontier\"')
    research_iii = home.index('id=\"research-iii-overview\"')
    reader_paths = home.index('id=\"reader-paths\"')
    assert research_i < p88 < research_iii < reader_paths < home.index('id=\"plain-language\"')
    for historical_id in ('id=\"p87-frontier\"', 'id=\"p86-frontier\"', 'id=\"p85-frontier\"'):
        assert historical_id not in home
"""
    text = replace_once(text, old, new, label="deployed Overview balance test")
    write(path, text)

    path = "tests/test_website_research_orientation.py"
    text = read(path)
    text = replace_once(text, "'index.html#p87-frontier'", "'index.html#p88-frontier'", label="Research Map P88 link test")
    write(path, text)


def patch_research_map_link() -> None:
    path = "website/research-map.html"
    text = read(path)
    text = replace_once(text, "index.html#p87-frontier", "index.html#p88-frontier", label="Research Map current Overview link")
    write(path, text)


def patch_figures_workflow() -> None:
    path = ".github/workflows/figures.yml"
    text = read(path)
    old = """          python -c \"from pathlib import Path; t=Path('_site/index.html').read_text(encoding='utf-8'); p=t.index('id=\\\"p88-frontier\\\"'); assert p < t.index('id=\\\"plain-language\\\"'); assert p < t.index('id=\\\"p87-frontier\\\"'); assert p < t.index('id=\\\"p86-frontier\\\"'); assert 'Current theorem frontier · P87' not in t\"
"""
    new = """          python -c \"from pathlib import Path; t=Path('_site/index.html').read_text(encoding='utf-8'); r1=t.index('id=\\\"research-i-overview\\\"'); p=t.index('id=\\\"p88-frontier\\\"'); r3=t.index('id=\\\"research-iii-overview\\\"'); paths=t.index('id=\\\"reader-paths\\\"'); assert r1 < p < r3 < paths < t.index('id=\\\"plain-language\\\"'); assert all(x not in t for x in ('id=\\\"p87-frontier\\\"','id=\\\"p86-frontier\\\"','id=\\\"p85-frontier\\\"'))\"
"""
    text = replace_once(text, old, new, label="figures workflow Overview contract")
    write(path, text)


def verify_shape() -> None:
    text = read("website/index.html")
    markers = [
        'id="project-journey"',
        'id="research-i-overview"',
        'id="p88-frontier"',
        'id="research-iii-overview"',
        'id="reader-paths"',
        'id="plain-language"',
    ]
    positions = [text.index(marker) for marker in markers]
    if positions != sorted(positions):
        raise RuntimeError("Overview stage order is not balanced")
    if text.count('id="p88-frontier"') != 1 or text.count("<!-- current-frontier-home: P88 -->") != 1:
        raise RuntimeError("Overview must contain exactly one canonical P88 frontier")
    for historical_id in ('id="p87-frontier"', 'id="p86-frontier"', 'id="p85-frontier"'):
        if historical_id in text:
            raise RuntimeError("historical Research II frontiers must remain off the Overview")


def main() -> None:
    patch_promoter()
    patch_figure_sync()
    patch_tests()
    patch_research_map_link()
    patch_figures_workflow()
    verify_shape()


if __name__ == "__main__":
    main()
