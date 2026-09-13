"""Promote the restored rich website from P87 to P88 without redesigning it.

This is intentionally a narrow migration. It updates theorem-frontier facts,
counts, ranges, and current-frontier blocks in the already-restored HTML. It
does not replace page bodies, navigation architecture, CSS, JavaScript, or the
reader-first explanatory structure.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEBSITE = ROOT / "website"

P88_FIGURE = "p88_exact_radius3_bounded_primitive_quad_projection_parity.svg"
P88_PROPOSITION = "proposition_88_exact_radius3_bounded_primitive_quad_projection_parity_functional.md"
P88_SOURCE = "bounded_primitive_radius3_quad_projection_parity_functional_separation.py"
P88_TEST = "test_bounded_primitive_radius3_quad_projection_parity_functional_separation.py"

P88_HOME_BLOCK = f'''<!-- current-frontier-home: P88 -->
<section id="p88-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head">
    <p class="eyebrow">Current theorem frontier · P88</p>
    <h2>Radius-3 bounded primitive four-event parity certificate</h2>
    <p>P88 keeps the same four-event order as P87 and completes the nonzero primitive coefficient box with |c_i| at most 3. Its 208,560-function exact audit strictly strengthens P87 on the same rational witness.</p>
  </div>
  <div class="theorem-figure-shell">
    <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/{P88_FIGURE}" aria-label="Open the full P88 theorem figure">
      <img loading="eager" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/{P88_FIGURE}" alt="P88 radius-3 bounded primitive four-event parity certificate showing L87 equals one over 96 and L88 equals one over 64" />
    </a>
  </div>
  <div class="frontier-summary-grid">
    <article class="frontier-summary-card"><h3>Complete radius-3 family</h3><p>632 primitive sign-normalized coefficient patterns per four-event subset yield 208,560 exact P88 functionals.</p></article>
    <article class="frontier-summary-card"><h3>Strict hierarchy</h3><p>The exact witness has <strong>L85 = 0 &lt; L86 = 1/192 &lt; L87 = 1/96 &lt; L88 = 1/64</strong>.</p></article>
    <article class="frontier-summary-card"><h3>Reproducible record</h3><p>The proof, equation provenance, exact implementation, exhaustive tests, theorem SVG, and figure manifest are source controlled.</p></article>
  </div>
  <div class="boundary"><p><strong>Scientific boundary:</strong> P88 is a conditional exact model-separation theorem for the declared P75 family. It does not identify consciousness, establish nonphysicality, validate another ontology, or close the physical-to-experiential bridge.</p></div>
  <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P88_PROPOSITION}">Open the P88 theorem</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p88_equation_provenance.md">Equation provenance</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/{P88_SOURCE}">Implementation</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/{P88_TEST}">Exact tests</a></p>
</section>
'''

P88_ATLAS_BLOCK = P88_HOME_BLOCK.replace(
    "<!-- current-frontier-home: P88 -->", "<!-- current-frontier-visual: P88 -->"
)

P88_READER_BLOCK = '''<section class="boundary" id="p88-reader-frontier"><div class="section-head"><p class="eyebrow">Current exact frontier · P88</p><h2>Radius-3 bounded primitive four-event parity audit</h2><p>P88 keeps the same four-event order as P87 but exhausts every nonzero primitive integer coefficient vector with magnitude at most three. The exact family contains 208,560 functionals and the strict rational hierarchy is <strong>L85 = 0 &lt; L86 = 1/192 &lt; L87 = 1/96 &lt; L88 = 1/64</strong>.</p><p>This is a conditional model-separation result for the declared P75 family; the physical-to-experiential bridge remains open.</p></div></section>'''

P88_SOURCE_BLOCK = f'''<section id="p88-source"><div class="section-head"><p class="eyebrow">Current theorem source · P88</p><h2>Exact radius-3 bounded primitive four-event projection-parity certificate</h2><p>P88 completes every nonzero primitive four-event coefficient vector with magnitude at most three, yielding 632 sign-normalized primitive patterns per subset, 208,560 exact functionals, and the strict hierarchy <strong>L87 = 1/96 &lt; L88 = 1/64</strong>.</p></div><div class="source-grid"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P88_PROPOSITION}"><h3>Proposition 88</h3><p>Formal statement, exact finite-family count, interval proof, transfer bound, strict witness, and scientific boundary.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p88_equation_provenance.md"><h3>P88 provenance</h3><p>Separates inherited parity algebra and endpoint arguments from the repository-original radius-3 construction and exact witness.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/{P88_SOURCE}"><h3>P88 implementation</h3><p>Exact rational exhaustive enumeration of the complete 208,560-function radius-3 family.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/{P88_TEST}"><h3>P88 exact tests</h3><p>Family count, exact interval, centered norm, strict witness, dominance, and interpretation-boundary regression tests.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/{P88_FIGURE}"><h3>P88 theorem figure</h3><p>Source-controlled visual summary synchronized with the exact theorem and figure publication manifest.</p></a></div></section>

'''


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")
    print(f"[p88-site] updated {path.relative_to(ROOT)}")


def replace_once(text: str, old: str, new: str, *, label: str) -> str:
    if old == new:
        return text
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one source marker, found {count}")
    return text.replace(old, new, 1)


def replace_all_required(text: str, old: str, new: str, *, label: str) -> str:
    count = text.count(old)
    if count < 1:
        raise RuntimeError(f"{label}: expected at least one source marker")
    return text.replace(old, new)


def replace_reader_frontier(text: str, *, label: str) -> str:
    pattern = re.compile(
        r'<section class="boundary" id="p87-reader-frontier">.*?</section>',
        flags=re.DOTALL,
    )
    if len(pattern.findall(text)) != 1:
        raise RuntimeError(f"{label}: expected one P87 reader-frontier block")
    return pattern.sub(P88_READER_BLOCK, text, count=1)


def promote_index() -> None:
    path = WEBSITE / "index.html"
    text = read(path)
    if "What would a scientifically testable bridge from physical description to experience actually require?" not in text:
        raise RuntimeError("homepage is not the restored rich generation")

    text = replace_once(text, "Explore all 87 results", "Explore all 88 results", label="home result button")
    text = replace_once(text, "<div><strong>87</strong><span>proposition-level results</span></div>", "<div><strong>88</strong><span>proposition-level results</span></div>", label="home status count")
    text = replace_once(text, "<div><strong>P87</strong><span>current theorem frontier</span></div>", "<div><strong>P88</strong><span>current theorem frontier</span></div>", label="home status frontier")

    marker = "<!-- current-frontier-home: P87 -->"
    if "<!-- current-frontier-home: P88 -->" not in text:
        if marker not in text:
            raise RuntimeError("homepage P87 frontier marker missing")
        text = text.replace(marker, P88_HOME_BLOCK + "\n<!-- previous-frontier-home: P87 -->", 1)
        text = replace_once(text, "Current theorem frontier · P87", "Previous theorem frontier · P87", label="home demote P87")

    substitutions = (
        ("The 87 results form", "The 88 results form"),
        ("all 87 propositions", "all 88 propositions"),
        ("The 87-result program", "The 88-result program"),
        ("P75-P87", "P75-P88"),
        ("P71-P87", "P71-P88"),
        ("P74-P86", "P74-P88"),
    )
    for old, new in substitutions:
        if old in text:
            text = text.replace(old, new)
    write(path, text)


def promote_plain_language() -> None:
    path = WEBSITE / "plain-language.html"
    text = read(path)
    for required in (
        "What are we actually trying to find out?",
        "Explain it in 60 seconds",
        "Seven questions have to be kept separate",
    ):
        if required not in text:
            raise RuntimeError(f"plain-language rich marker missing: {required}")

    text = replace_once(text, "<div><strong>87</strong><span>proposition-level results</span></div>", "<div><strong>88</strong><span>proposition-level results</span></div>", label="plain count")
    text = replace_once(text, "<div><strong>P87</strong><span>current theorem frontier</span></div>", "<div><strong>P88</strong><span>current theorem frontier</span></div>", label="plain frontier")
    text = text.replace("What the 87 results are doing", "What the 88 results are doing")
    text = text.replace("P75-P87", "P75-P88")
    text = text.replace("actual P87 research frontier", "actual P88 research frontier")
    text = text.replace("all 87 results connect", "all 88 results connect")
    text = replace_reader_frontier(text, label="plain-language")
    write(path, text)


def promote_start_here() -> None:
    path = WEBSITE / "start-here.html"
    text = read(path)
    if "From the simple question to the actual mathematics" not in text:
        raise RuntimeError("start-here is not the restored rich generation")

    text = text.replace("87-result theorem program and current P87 frontier", "88-result theorem program and current P88 frontier")
    text = text.replace("Open all 87 results", "Open all 88 results")
    text = replace_once(text, "<div><strong>87</strong><span>proposition-level results</span></div>", "<div><strong>88</strong><span>proposition-level results</span></div>", label="start count")
    text = replace_once(text, "<div><strong>P87</strong><span>current theorem frontier</span></div>", "<div><strong>P88</strong><span>current theorem frontier</span></div>", label="start frontier")
    text = text.replace("P75-P87", "P75-P88")
    text = text.replace("The 87 propositions by scientific role", "The 88 propositions by scientific role")
    text = text.replace("P78-P87 progressively tighten", "P78-P88 progressively tighten")
    text = text.replace("P73-P87 test", "P73-P88 test")

    text = text.replace("<strong>P86 is the previous exact frontier.</strong>", "<strong>P86 is an earlier exact frontier.</strong>")
    p87_current = '<p><strong>P87 is the current exact frontier.</strong> It exhausts every nonzero primitive integer four-event coefficient vector with |c_i| at most 2, modulo one global sign. The family contains 39,600 exact functionals, and on the same rational witness it gives <strong>L86 = 1/192 &lt; L87 = 1/96</strong>.</p>'
    p87_previous_and_p88 = '<p><strong>P87 is the previous exact frontier.</strong> It exhausts every nonzero primitive integer four-event coefficient vector with |c_i| at most 2, modulo one global sign. The family contains 39,600 exact functionals, and on the shared rational witness it gives <strong>L86 = 1/192 &lt; L87 = 1/96</strong>.</p>\n      <p><strong>P88 is the current exact frontier.</strong> It keeps the same four-event order and exhausts every nonzero primitive integer coefficient vector with |c_i| at most 3, modulo one global sign. The family contains 632 sign-normalized patterns per subset and 208,560 exact functionals, and on the same rational witness it gives <strong>L87 = 1/96 &lt; L88 = 1/64</strong>.</p>'
    text = replace_once(text, p87_current, p87_previous_and_p88, label="start P87/P88 frontier paragraph")

    old_link = 'href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md">Read P87</a>'
    new_link = f'href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P88_PROPOSITION}">Read P88</a>'
    text = replace_once(text, old_link, new_link, label="start frontier proof link")
    write(path, text)


def promote_research_map() -> None:
    path = WEBSITE / "research-map.html"
    text = read(path)
    if "Eighty-seven results, one dependency-aware scientific program" not in text:
        raise RuntimeError("research-map is not the expected rich P87 generation")

    text = text.replace("through Proposition 87", "through Proposition 88")
    text = text.replace("Eighty-seven results, one dependency-aware scientific program", "Eighty-eight results, one dependency-aware scientific program")
    text = text.replace("P71-P87 return", "P71-P88 return")
    text = text.replace(
        "while P87 completes every nonzero primitive four-event coefficient vector with magnitude at most two and strictly strengthens the P86 certificate.",
        "while P87 completes every nonzero primitive four-event coefficient vector with magnitude at most two and strictly strengthens the P86 certificate, and P88 completes the next primitive radius-three coefficient box and strengthens the same exact witness to L88 = 1/64.",
    )
    text = replace_once(text, "<div><strong>87</strong><span>proposition-level results</span></div>", "<div><strong>88</strong><span>proposition-level results</span></div>", label="map count")
    text = text.replace("P73-P87", "P73-P88")
    text = text.replace("culminating in P87 exact bounded primitive four-event shared-parameter parity-functional separation", "culminating in P88 exact radius-3 bounded primitive four-event shared-parameter parity-functional separation")
    text = text.replace("None of P71-P87 is a consciousness ontology.", "None of P71-P88 is a consciousness ontology.")
    text = text.replace("P77-P87: from full-law rejection", "P77-P88: from full-law rejection")
    text = text.replace("Continue to the current P87 frontier", "Continue to the current P88 frontier")
    text = text.replace('href="index.html#p87-frontier">Continue to the current P88 frontier', 'href="index.html#p88-frontier">Continue to the current P88 frontier')
    text = replace_reader_frontier(text, label="research-map")
    write(path, text)


def promote_visual_atlas() -> None:
    path = WEBSITE / "visual-atlas.html"
    text = read(path)
    if "Figures as navigational aids to the mathematics" not in text:
        raise RuntimeError("visual atlas is not the restored rich generation")
    marker = "<!-- current-frontier-visual: P87 -->"
    if "<!-- current-frontier-visual: P88 -->" not in text:
        if marker not in text:
            raise RuntimeError("visual atlas P87 frontier marker missing")
        text = text.replace(marker, P88_ATLAS_BLOCK + "\n<!-- previous-frontier-visual: P87 -->", 1)
        text = replace_once(text, "Current theorem frontier · P87", "Previous theorem frontier · P87", label="atlas demote P87")
    write(path, text)


def promote_implementation() -> None:
    path = WEBSITE / "implementation.html"
    text = read(path)
    if "How the research actually works" not in text:
        raise RuntimeError("implementation page rich marker missing")
    text = text.replace("P1-P87 proposition record", "P1-P88 proposition record")
    text = text.replace("P73-P87", "P73-P88")
    text = text.replace("P77-P87", "P77-P88")
    text = text.replace("P86 current four-event exact parity-functional implementation", "P86 minimally weighted four-event exact parity-functional implementation")
    if P88_SOURCE not in text:
        p87_link = '<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/bounded_primitive_quad_projection_parity_functional_separation.py"><strong>bounded_primitive_quad_projection_parity_functional_separation.py</strong><small>P87 exact 39,600-function bounded primitive four-event separation</small></a>'
        p88_link = f'<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/{P88_SOURCE}"><strong>{P88_SOURCE}</strong><small>P88 exact 208,560-function radius-3 bounded primitive four-event separation</small></a>'
        text = replace_once(text, p87_link, p87_link + "\n    " + p88_link, label="implementation P88 source link")
    old_frontier = '<p class="scientific-boundary"><strong>Frontier continuation:</strong> P77-P86 strengthen this branch from individual adequacy constraints to certified separation from the complete continuous model family. P84 adds pairwise shared-parameter parity compatibility, P85 adds three-event functionals, and the current P87 frontier adds 10,560 minimally weighted four-event functionals with the strict exact hierarchy <strong>L85 = 0 &lt; L86 = 1/192</strong>. See the <a href="index.html#p86-frontier">current P87 frontier</a> and the <a href="research-map.html">Research Map</a> for the full lineage.</p>'
    new_frontier = '<p class="scientific-boundary"><strong>Frontier continuation:</strong> P77-P88 strengthen this branch from individual adequacy constraints to certified separation from the complete continuous model family. P84 adds pairwise shared-parameter parity compatibility, P85 adds three-event functionals, P86 adds minimally weighted four-event functionals, P87 completes the primitive radius-two box, and the current P88 frontier completes the primitive radius-three box with the shared exact hierarchy <strong>L85 = 0 &lt; L86 = 1/192 &lt; L87 = 1/96 &lt; L88 = 1/64</strong>. See the <a href="index.html#p88-frontier">current P88 frontier</a> and the <a href="research-map.html">Research Map</a> for the full lineage.</p>'
    text = replace_once(text, old_frontier, new_frontier, label="implementation frontier boundary")
    write(path, text)


def promote_sources() -> None:
    path = WEBSITE / "sources.html"
    text = read(path)
    if "A visible provenance path for mathematics, physics, empirical evidence, and local results" not in text:
        raise RuntimeError("sources page rich marker missing")
    if 'id="p88-source"' not in text:
        marker = '<section id="p87-source">'
        if marker not in text:
            raise RuntimeError("P87 source section missing")
        text = text.replace(marker, P88_SOURCE_BLOCK + '<section id="p87-source">', 1)
        text = replace_once(text, "Current theorem source · P87", "Previous theorem source · P87", label="sources demote P87")
        text = text.replace("Previous theorem source · P86", "Earlier theorem source · P86", 1)
    write(path, text)


def promote_prepare_website() -> None:
    path = ROOT / "scripts" / "prepare_website.py"
    text = read(path)
    text = replace_once(text, 'CURRENT_FRONTIER_FIGURE = "p87_exact_bounded_primitive_quad_projection_parity.svg"', f'CURRENT_FRONTIER_FIGURE = "{P88_FIGURE}"', label="prepare frontier figure")
    text = replace_once(text, 'ASSET_VERSION = "20260913-mobile17-p87"', 'ASSET_VERSION = "20260913-mobile18-p88"', label="prepare asset version")
    text = text.replace("Require P87 to be the primary visual frontier in the canonical website.", "Require P88 to be the primary visual frontier in the canonical website.")
    text = text.replace("current P87 theorem figure", "current P88 theorem figure")
    text = text.replace("bundled P87 theorem figure", "bundled P88 theorem figure")
    text = text.replace("p87_atlas = visual_atlas.index('id=\"p87-frontier\"')", "p88_atlas = visual_atlas.index('id=\"p88-frontier\"')")
    text = text.replace("if p87_atlas >= visual_atlas.index(marker):", "if p88_atlas >= visual_atlas.index(marker):")
    text = text.replace('for marker in (\'id="p86-frontier"\', \'id="p85-frontier"\'):', 'for marker in (\'id="p87-frontier"\', \'id="p86-frontier"\'):' )
    text = text.replace("Visual Atlas does not present P87 before", "Visual Atlas does not present P88 before")
    text = text.replace("p87 = homepage.index('id=\"p87-frontier\"')", "p88 = homepage.index('id=\"p88-frontier\"')")
    text = text.replace("if p87 >= homepage.index(marker):", "if p88 >= homepage.index(marker):")
    text = text.replace("'id=\"p84-frontier\"',\n        'id=\"p85-frontier\"',\n        'id=\"p86-frontier\"',", "'id=\"p87-frontier\"',\n        'id=\"p86-frontier\"',")
    text = text.replace("Homepage P87 frontier appears too late", "Homepage P88 frontier appears too late")
    text = text.replace("stale pre-P87 reader text", "stale pre-P88 reader text")
    # P88-specific stale-current tokens: P87 may remain historically, but never as current.
    old_stale = '''    stale_tokens = (\n        "Current theorem frontier · P86",\n        "The 86 results form several dependency branches.",\n        "all 86 propositions",\n        "P71-P86, then read the falsification program",\n    )'''
    new_stale = '''    stale_tokens = (\n        "Current theorem frontier · P87",\n        "Current exact frontier · P87",\n        "current theorem frontier</span></div>\\n        <div><strong>v0.82.0",\n        "Explore all 87 results",\n        "The 87 results form several dependency branches.",\n        "all 87 propositions",\n    )'''
    text = replace_once(text, old_stale, new_stale, label="prepare stale tokens")
    write(path, text)


def promote_pages_workflow() -> None:
    path = ROOT / ".github" / "workflows" / "pages.yml"
    text = read(path)
    text = replace_once(text, "grep -q 'Explore all 87 results' _site/index.html", "grep -q 'Explore all 88 results' _site/index.html", label="pages index count")
    text = replace_once(text, "grep -q 'What the 87 results are doing' _site/plain-language.html", "grep -q 'What the 88 results are doing' _site/plain-language.html", label="pages plain count")
    text = replace_once(text, "grep -q 'P87' _site/plain-language.html", "grep -q 'Current exact frontier · P88' _site/plain-language.html\n          grep -q '208,560' _site/plain-language.html\n          grep -q 'p88_exact_radius3_bounded_primitive_quad_projection_parity.svg' _site/index.html\n          grep -q 'p88_exact_radius3_bounded_primitive_quad_projection_parity.svg' _site/visual-atlas.html", label="pages frontier checks")
    write(path, text)


def validate_source_state() -> None:
    index = read(WEBSITE / "index.html")
    plain = read(WEBSITE / "plain-language.html")
    start = read(WEBSITE / "start-here.html")
    research_map = read(WEBSITE / "research-map.html")
    atlas = read(WEBSITE / "visual-atlas.html")
    implementation = read(WEBSITE / "implementation.html")
    sources = read(WEBSITE / "sources.html")

    required = {
        "index": (index, "Explore all 88 results", 'id="p88-frontier"', "208,560"),
        "plain": (plain, "What the 88 results are doing", "Current exact frontier · P88", "L88 = 1/64"),
        "start": (start, "Open all 88 results", "P88 is the current exact frontier", "L88 = 1/64"),
        "map": (research_map, "Eighty-eight results", "P77-P88", "Current exact frontier · P88"),
        "atlas": (atlas, 'id="p88-frontier"', "Current theorem frontier · P88", "208,560"),
        "implementation": (implementation, "P73-P88", P88_SOURCE, "L88 = 1/64"),
        "sources": (sources, 'id="p88-source"', "Current theorem source · P88", "208,560"),
    }
    for label, values in required.items():
        page, *markers = values
        for marker in markers:
            if marker not in page:
                raise RuntimeError(f"{label}: missing promoted marker {marker!r}")

    # Protect the restored rich-generation identity.
    for marker in (
        "What are we actually trying to find out?",
        "Explain it in 60 seconds",
        "Seven questions have to be kept separate",
        "Pass, fail, and inconclusive mean different things",
    ):
        if marker not in plain:
            raise RuntimeError(f"plain-language rich content lost: {marker}")
    if "What would a scientifically testable bridge from physical description to experience actually require?" not in index:
        raise RuntimeError("homepage rich hero lost")

    if index.index('id="p88-frontier"') >= index.index('id="p87-frontier"'):
        raise RuntimeError("homepage does not present P88 before P87")
    if atlas.index('id="p88-frontier"') >= atlas.index('id="p87-frontier"'):
        raise RuntimeError("visual atlas does not present P88 before P87")

    for page_name, page in (("index", index), ("plain", plain), ("start", start), ("atlas", atlas)):
        if "Current theorem frontier · P87" in page or "Current exact frontier · P87" in page:
            raise RuntimeError(f"{page_name}: stale P87 current-frontier label")


def main() -> None:
    promote_index()
    promote_plain_language()
    promote_start_here()
    promote_research_map()
    promote_visual_atlas()
    promote_implementation()
    promote_sources()
    promote_prepare_website()
    promote_pages_workflow()
    validate_source_state()
    print("[p88-site] guarded P88 website promotion complete; layout/assets preserved")


if __name__ == "__main__":
    main()
