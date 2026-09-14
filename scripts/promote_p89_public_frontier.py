"""Promote the reader-facing publication state to the P89 frontier.

P89 closes the complete real linear-functional class over the eleven canonical
P83 parity coordinates on a fixed rational P75 box. This promoter keeps that
Research II result visible without allowing the public entry pages to collapse
the larger program into Research II alone: Overview, Plain Language, and Start
Here must all preserve Research I -> Research II -> Research III as the primary
scientific architecture.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

P89_FIGURE = "p89_complete_linear_parity_duality.svg"
P89_PROOF = "proposition_89_complete_linear_parity_duality.md"
P89_PROVENANCE = "p89_equation_provenance.md"
P89_IMPLEMENTATION = "complete_linear_parity_duality.py"
P89_TEST = "test_complete_linear_parity_duality.py"

P89_HOME = f'''<!-- current-frontier-home: P89 -->
<section id="p89-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head">
    <p class="eyebrow">Research II · Current theorem frontier · P89</p>
    <h2>Complete linear parity-functional duality certificate</h2>
    <p>P89 removes the finite coefficient-radius and four-observable support restrictions of P88. It considers every real linear functional of all eleven canonical P83 parity coordinates and proves the exact optimum by matching a functional lower certificate to a convex-vertex plus zero-mass perturbation upper certificate.</p>
  </div>
  <div class="theorem-figure-shell">
    <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/{P89_FIGURE}" aria-label="Open the full P89 theorem figure">
      <img loading="eager" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/{P89_FIGURE}" alt="P89 complete linear parity-functional duality certificate showing the exact complete-linear optimum five over one hundred sixty-eight, strictly stronger than P88 one over sixty-four" />
    </a>
  </div>
  <div class="frontier-summary-grid">
    <article class="frontier-summary-card"><h3>No coefficient-radius ceiling</h3><p>The coefficient vector ranges over all of R<sup>11</sup> except zero, so P89 closes the complete real linear-functional class on the eleven declared parity coordinates.</p></article>
    <article class="frontier-summary-card"><h3>Matching exact certificates</h3><p>The strict witness gives a lower bound of <strong>5/168</strong>, and an exact rational convex-vertex plus zero-mass perturbation certificate gives the same universal upper bound.</p></article>
    <article class="frontier-summary-card"><h3>Strict improvement over P88</h3><p><strong>L88 = 1/64 &lt; L89 = 5/168</strong>. Larger coefficient radii or denser real linear combinations of the same eleven observables cannot improve the P89 value on this witness.</p></article>
  </div>
  <div class="boundary"><p><strong>Scientific boundary:</strong> P89 is complete only for the declared real linear parity-functional class on the stated P75 box. It does not exhaust nonlinear model constraints, identify consciousness, establish nonphysicality, or close the physical-to-experiential bridge.</p></div>
  <p><a href="research-map.html">Research II map</a> · <a href="visual-atlas.html">Historical theorem figures</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P89_PROOF}">P89 theorem</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P89_PROVENANCE}">Equation provenance</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/{P89_IMPLEMENTATION}">Implementation</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/{P89_TEST}">Exact tests</a></p>
</section>

'''

P89_ATLAS = f'''<!-- current-frontier-visual: P89 -->
<section id="p89-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head">
    <p class="eyebrow">Current theorem frontier · P89</p>
    <h2>Complete linear parity-functional duality certificate</h2>
    <p>P89 optimizes over every real linear combination of all eleven canonical parity coordinates and proves an exact complete-linear optimum of 5/168 on the established rational witness.</p>
  </div>
  <div class="theorem-figure-shell">
    <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/{P89_FIGURE}" aria-label="Open the full P89 theorem figure">
      <img loading="eager" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/{P89_FIGURE}" alt="P89 exact complete linear parity-functional duality certificate" />
    </a>
  </div>
  <div class="frontier-summary-grid">
    <article class="frontier-summary-card"><h3>Complete linear class</h3><p>All real coefficient vectors on all eleven canonical parity coordinates are allowed; there is no support-size or coefficient-radius cutoff.</p></article>
    <article class="frontier-summary-card"><h3>Exact duality</h3><p>A lower functional witness and a universal signed-perturbation upper certificate meet exactly at <strong>5/168</strong>.</p></article>
    <article class="frontier-summary-card"><h3>Strict witness</h3><p>The published direction has coefficients (0, −2, −1, 1, 1, 1, −2, −1, −3, 2, −3), empirical value −13/6, P75 interval [−51/8, −3], gap 5/6, and centered norm 28.</p></article>
  </div>
  <div class="boundary"><p><strong>Scientific boundary:</strong> complete linear parity separation is not complete model separation and does not identify the latent state with conscious experience.</p></div>
  <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P89_PROOF}">Open the P89 theorem</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P89_PROVENANCE}">Equation provenance</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/{P89_IMPLEMENTATION}">Implementation</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/{P89_TEST}">Exact tests</a></p>
</section>

'''

PLAIN_BALANCED_SECTION = '''<section id="three-stage-progress">
      <div class="section-head">
        <p class="eyebrow">What the whole research program is doing</p>
        <h2>Three stages answer three different scientific questions</h2>
        <p>The proposition sequence belongs to Research II. It is one stage of a larger program, not the entire project. Research I identifies the physical system; Research II tests whether a declared physical description is sufficient and falsifiable; Research III asks what the available evidence can actually identify about an experiential target.</p>
      </div>
      <div class="flow">
        <div class="flow-node"><span>Research I</span><h3>Identify the physical system</h3><p>Specify the subsystem, its persistence through time, the measurable dynamics, the interventions, and the boundary of the physical object whose description will later be tested.</p><p><a href="https://github.com/MahsaKeikha/spatiotemporal-observer-math">Open Research I →</a></p></div>
        <div class="flow-node"><span>Research II</span><h3>Test sufficiency and falsifiability</h3><p>The 89-result proposition program asks whether a declared physical description preserves the distinctions required by an independently specified target, protects the target from circularity, and rejects inadequate measurement models. The current theorem frontier is P89.</p><p><a href="research-map.html">Explore Research II →</a></p></div>
        <div class="flow-node"><span>Research III</span><h3>Make experiential evidence measurable</h3><p>Combine reports, behavior, neural and physiological signals, interventions, context, uncertainty, and dependence without pretending that weak evidence identifies more than it really does.</p><p><a href="measurement-science.html">Open Research III →</a></p></div>
      </div>
      <div class="boundary">
        <h3>How to interpret progress</h3>
        <p>A stronger Research II theorem does not replace Research I or Research III. The stages constrain different failure modes, and the final physical-to-experiential bridge remains open until the system definition, bridge test, and measurement evidence all support the same claim.</p>
      </div>
    </section>'''

START_PROGRAM_SECTION = '''<section id="program-stages">
      <div class="section-head">
        <p class="eyebrow">The whole research program</p>
        <h2>Start with the three stages before entering the proposition chronology</h2>
        <p>The 89 propositions are the formal theorem record of Research II. They should be read between Research I, which defines the physical system, and Research III, which develops the measurement science needed to connect observable evidence to experiential targets under uncertainty.</p>
      </div>
      <div class="result-grid">
        <article class="result"><span>Research I</span><h3>Physical-system identification</h3><p>Define the persistent subsystem, its world-tube, dynamics, interventions, observables, and boundary before asking what any descriptor means for experience.</p><p><a href="https://github.com/MahsaKeikha/spatiotemporal-observer-math">Open Research I →</a></p></article>
        <article class="result"><span>Research II</span><h3>Bridge sufficiency and falsification</h3><p>P1-P89 build the mathematical conditions for testing whether a declared physical description is sufficient for an independently specified target and whether the declared target-measurement model can survive exact and finite-data rejection tests.</p><p><a href="research-map.html">Open Research II →</a></p></article>
        <article class="result"><span>Research III</span><h3>Consciousness measurement science</h3><p>Ask what multimodal observations, interventions, reports, behavior, neural and physiological signals can identify when measurement noise and dependence are made explicit.</p><p><a href="measurement-science.html">Open Research III →</a></p></article>
      </div>
    </section>'''


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_many(text: str, replacements: tuple[tuple[str, str], ...]) -> str:
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def remove_section(text: str, section_id: str) -> str:
    pattern = re.compile(
        rf'(?:<!--\s*current-frontier-(?:home|visual):\s*P\d+\s*-->\s*)?'
        rf'<section id="{re.escape(section_id)}"(?=[\s>]).*?</section>\s*',
        flags=re.DOTALL,
    )
    return pattern.sub("", text)


def insert_before_section(text: str, before_id: str, insertion: str) -> str:
    marker = f'<section id="{before_id}"'
    if marker not in text:
        raise RuntimeError(f"missing insertion marker {before_id}")
    return text.replace(marker, insertion + marker, 1)


def promote_index() -> None:
    path = "website/index.html"
    text = read(path)
    text = replace_many(
        text,
        (
            ("Explore all 88 results", "Explore all 89 results"),
            ("<strong>88</strong><span>proposition-level results</span>", "<strong>89</strong><span>proposition-level results</span>"),
            ("P88 current theorem frontier · v0.82.0", "P89 current theorem frontier · v0.82.0"),
            ("88 proposition-level results through P88", "89 proposition-level results through P89"),
            ("The 88 results form several dependency branches.", "The 89 results form several dependency branches."),
            ("The 88-result program", "The 89-result program"),
            ("all 88 propositions", "all 89 propositions"),
            ("all 88 results", "all 89 results"),
            ("P71-P88", "P71-P89"),
            ("P73-P88", "P73-P89"),
            ("P74-P88", "P74-P89"),
            ("P75 → P88", "P75 → P89"),
            ("P75-P88", "P75-P89"),
            ("P1-P88", "P1-P89"),
            ("P88 certification ladder", "P89 certification ladder"),
            ("P88 sources", "P89 sources"),
            ("sources.html#p88-source", "sources.html#p89-source"),
            ("current P88 frontier", "current P89 frontier"),
            ("<!-- Current theorem asset: docs/figures/p88_exact_radius_three_bounded_primitive_quad_projection_parity.svg -->", f"<!-- Current theorem asset: docs/figures/{P89_FIGURE} -->"),
        ),
    )
    text = remove_section(text, "p89-frontier")
    text = remove_section(text, "p88-frontier")
    text = insert_before_section(text, "research-iii-overview", P89_HOME)
    write(path, text)


def promote_visual_atlas() -> None:
    path = "website/visual-atlas.html"
    text = read(path)
    text = remove_section(text, "p89-frontier")
    text = re.sub(r'<!--\s*current-frontier-visual:\s*P88\s*-->\s*', "", text)
    text = text.replace(
        '<section id="p88-frontier" class="theorem-frontier current-frontier-visual">',
        '<section id="p88-frontier" class="theorem-frontier">',
    )
    text = text.replace("Current theorem frontier · P88", "Previous theorem frontier · P88")
    text = text.replace("Current frontier · P88", "Previous frontier · P88")
    marker = '<section id="p88-frontier"'
    if marker not in text:
        raise RuntimeError("Visual Atlas P88 historical section is missing")
    text = text.replace(marker, P89_ATLAS + marker, 1)
    text = text.replace("P1-P88", "P1-P89").replace("88 results", "89 results")
    write(path, text)


def promote_plain_language() -> None:
    path = "website/plain-language.html"
    text = read(path)
    status = re.compile(
        r'<div class="status-grid" aria-label="Current research status">.*?</div>\s*</section>',
        re.DOTALL,
    )
    replacement = '''<div class="status-grid" aria-label="Current research status">
        <div><strong>Research I</strong><span>physical-system identification</span></div>
        <div><strong>Research II</strong><span>89 results · current frontier P89</span></div>
        <div><strong>Research III</strong><span>measurement science under uncertainty</span></div>
        <div><strong>Open</strong><span>final physical-to-experiential bridge</span></div>
      </div>
    </section>'''
    text, count = status.subn(replacement, text, count=1)
    if count != 1:
        raise RuntimeError("Plain Language status grid was not found")
    text = replace_many(
        text,
        (
            ("This is the 88-result theorem program currently reaching P88.", "This is the 89-result Research II theorem program currently reaching P89."),
            ("An 88-result sufficiency and falsification architecture", "A 89-result sufficiency and falsification architecture"),
            ("currently through P88", "currently through P89"),
            ("P75-P88", "P75-P89"),
            ("88-result", "89-result"),
            ("88 results", "89 results"),
        ),
    )
    section_pattern = re.compile(
        r'<section>\s*<div class="section-head">\s*<p class="eyebrow">What the (?:88|89) results are doing</p>.*?</section>',
        re.DOTALL,
    )
    text, count = section_pattern.subn(PLAIN_BALANCED_SECTION, text, count=1)
    if count != 1 and 'id="three-stage-progress"' not in text:
        raise RuntimeError("Plain Language Research-II-only progress section was not found")
    text = re.sub(
        r'<section class="boundary" id="p(?:88|89)-reader-frontier">.*?</section>',
        '''<section class="boundary" id="p89-reader-frontier"><div class="section-head"><p class="eyebrow">Research II · Current exact frontier · P89</p><h2>Complete linear parity-functional duality</h2><p>P89 removes P88's finite coefficient-radius and four-observable support restrictions. Across all real linear combinations of all eleven canonical parity coordinates, the strict exact-rational witness has <strong>L88 = 1/64 &lt; L89 = 5/168</strong>, and a matching universal upper certificate proves that 5/168 is the exact complete-linear optimum on that box.</p><p>This closes the declared linear parity-functional class only. It does not replace Research I or Research III, exhaust nonlinear P75 constraints, or close the physical-to-experiential bridge.</p></div></section>''',
        text,
        count=1,
        flags=re.DOTALL,
    )
    write(path, text)


def promote_start_here() -> None:
    path = "website/start-here.html"
    text = read(path)
    text = replace_many(
        text,
        (
            ("the 88-result theorem program and current P88 frontier", "the three-stage research program and current Research II P89 frontier"),
            ("Open all 88 results", "Open all 89 Research II results"),
            ("You do not need to read 88 proofs in order", "You do not need to read 89 Research II proofs in order"),
            ("complete 88-result dependency structure", "complete 89-result Research II dependency structure"),
            ("P75-P88", "P75-P89"),
            ("P78-P88", "P78-P89"),
            ("P71-P88", "P71-P89"),
            ("P74-P88", "P74-P89"),
            ("The 88 propositions by scientific role", "The 89 Research II propositions by scientific role"),
            ("The 88 propositions", "The 89 Research II propositions"),
        ),
    )
    status = re.compile(
        r'<div class="status-grid" aria-label="Current research status">.*?</div>\s*'
        r'<p class="small-note"><strong>Formal repository release:</strong>.*?</p>\s*</section>',
        re.DOTALL,
    )
    replacement = '''<div class="status-grid" aria-label="Current research status">
        <div><strong>Research I</strong><span>physical-system identification</span></div>
        <div><strong>Research II</strong><span>89 results · current frontier P89</span></div>
        <div><strong>Research III</strong><span>measurement science under uncertainty</span></div>
        <div><strong>Open</strong><span>physical-to-experiential bridge</span></div>
      </div>
      <p class="small-note"><strong>Formal repository release:</strong> v0.82.0. The documented theorem frontier can advance independently of the packaged release.</p>
    </section>'''
    text, count = status.subn(replacement, text, count=1)
    if count != 1:
        raise RuntimeError("Start Here status grid was not found")
    if 'id="program-stages"' not in text:
        marker = '<section id="chain">'
        if marker not in text:
            raise RuntimeError("Start Here chain marker is missing")
        text = text.replace(marker, START_PROGRAM_SECTION + "\n\n    " + marker, 1)
    text = text.replace(
        '<p class="eyebrow">Program architecture</p>\n        <h2>The 89 Research II propositions by scientific role</h2>',
        '<p class="eyebrow">Inside Research II</p>\n        <h2>The 89 Research II propositions by scientific role</h2>',
    )
    text = text.replace(
        '<p class="eyebrow">Current certified frontier</p>\n      <h2>P78-P89 progressively tighten global separation from the declared continuous model family</h2>',
        '<p class="eyebrow">Research II · Current certified frontier</p>\n      <h2>P78-P89 progressively tighten global separation from the declared continuous model family</h2>',
    )
    if "P89 closes the complete real linear parity-functional class" not in text:
        needle = "</section>\n\n    <section>\n      <div class=\"section-head\">\n        <p class=\"eyebrow\">What the mathematics does not prove</p>"
        p89_paragraph = '''      <p><strong>P89 closes the complete real linear parity-functional class.</strong> It removes P88's finite coefficient-radius and four-observable support restrictions. On the established exact-rational witness, a matching lower and upper certificate proves <strong>L89 = 5/168</strong>, strictly above <strong>L88 = 1/64</strong>. This is complete only for the declared linear parity observables; nonlinear P75 constraints and the physical-to-experiential bridge remain open.</p>\n'''
        frontier_start = text.find('<section class="dark-section">')
        frontier_end = text.find('</section>', frontier_start)
        if frontier_start == -1 or frontier_end == -1:
            raise RuntimeError("Start Here frontier section is missing")
        text = text[:frontier_end] + p89_paragraph + text[frontier_end:]
    write(path, text)


def promote_research_map() -> None:
    path = "website/research-map.html"
    text = read(path)
    text = replace_many(
        text,
        (
            ("88 proposition-level results", "89 proposition-level results"),
            ("P1-P88", "P1-P89"),
            ("P71-P88", "P71-P89"),
            ("P75-P88", "P75-P89"),
            ("current P88", "current P89"),
            ("Current theorem frontier · P88", "Current theorem frontier · P89"),
        ),
    )
    text = remove_section(text, "p89-research-map")
    section = f'''<section id="p89-research-map"><div class="section-head"><p class="eyebrow">IV-R · Complete linear parity-functional duality</p><h2>P89: What is the strongest possible real linear certificate from the eleven canonical parity observables?</h2></div><div class="result-grid"><article class="result"><span>P89</span><h3>Exact complete real linear optimum</h3><p>P89 removes both the finite coefficient-radius restriction and the four-observable support restriction. Finite-dimensional duality matches a real linear-functional lower certificate to a convex P75 box-vertex plus zero-mass signed-perturbation upper certificate. On the established rational witness the exact optimum is <strong>5/168</strong>, strictly stronger than P88 = 1/64.</p></article></div><div class="figure-card"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/{P89_FIGURE}" alt="P89 complete linear parity-functional duality certificate"/><div><h3>P89 complete real linear certificate</h3><p>The matching rational certificates prove that no other real linear combination of the same eleven parity coordinates can improve the 5/168 bound on the stated box.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P89_PROOF}">Read Proposition 89</a></div></div></section>\n'''
    text = text.replace("</main>", section + "</main>", 1)
    text = text.replace("index.html#p88-frontier", "index.html#p89-frontier")
    write(path, text)


def promote_misc_website() -> None:
    replacements = (
        ("88 proposition-level results", "89 proposition-level results"),
        ("<strong>88</strong><span>proposition-level results</span>", "<strong>89</strong><span>proposition-level results</span>"),
        ("<strong>P88</strong><span>current theorem frontier</span>", "<strong>P89</strong><span>current theorem frontier</span>"),
        ("P88 current theorem frontier", "P89 current theorem frontier"),
        ("P75-P88", "P75-P89"),
        ("P77-P88", "P77-P89"),
        ("index.html#p88-frontier", "index.html#p89-frontier"),
    )
    for path in (
        "website/research-lineage.html",
        "website/implementation.html",
        "website/sources.html",
    ):
        if (ROOT / path).is_file():
            write(path, replace_many(read(path), replacements))

    sources_path = ROOT / "website/sources.html"
    if sources_path.is_file():
        source_text = read("website/sources.html")
        p89_source = f'''<section id="p89-source"><div class="section-head"><p class="eyebrow">Current theorem source · P89</p><h2>Complete real linear parity-functional duality certificate</h2><p>P89 removes the finite coefficient-radius and four-observable support restrictions of P88. It optimizes over every real linear functional of all eleven canonical P83 parity coordinates. On the established exact rational witness, the lower functional certificate and the universal convex-vertex plus zero-mass perturbation upper certificate meet at <strong>5/168</strong>, strictly above <strong>L88 = 1/64</strong>.</p></div><div class="source-grid"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P89_PROOF}"><h3>Proposition 89</h3><p>Formal statement, finite-dimensional duality, exact lower and upper certificates, and scientific boundary.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P89_PROVENANCE}"><h3>P89 provenance</h3><p>Separates inherited parity algebra and convex analysis from the repository-original complete real linear certificate.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/{P89_IMPLEMENTATION}"><h3>P89 implementation</h3><p>Exact rational computation of the complete linear lower certificate and matching dual upper certificate.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/{P89_TEST}"><h3>P89 exact tests</h3><p>Exact witness, dual certificate, dominance over P88, and scientific-boundary regression tests.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/{P89_FIGURE}"><h3>P89 theorem figure</h3><p>Source-controlled visual summary synchronized with the theorem and publication manifest.</p></a></div><div class="boundary"><p><strong>Scientific boundary:</strong> P89 closes only the declared real linear parity-functional class on the stated P75 box. It does not exhaust nonlinear P75 constraints, identify consciousness, establish nonphysicality, or close the physical-to-experiential bridge.</p></div></section>

'''
        source_text = remove_section(source_text, "p89-source")
        p88_marker = '<section id="p88-source">'
        if p88_marker not in source_text:
            raise RuntimeError("P88 source section is missing from website/sources.html")
        source_text = source_text.replace(
            '<p class="eyebrow">Current theorem source · P88</p>',
            '<p class="eyebrow">Previous theorem source · P88</p>',
            1,
        )
        source_text = source_text.replace(p88_marker, p89_source + p88_marker, 1)
        write("website/sources.html", source_text)


def assert_balanced_reader_state() -> None:
    home = read("website/index.html")
    plain = read("website/plain-language.html")
    start = read("website/start-here.html")
    atlas = read("website/visual-atlas.html")
    for label, source in (("Overview", home), ("Plain Language", plain), ("Start Here", start)):
        for marker in ("Research I", "Research II", "Research III", "physical-to-experiential bridge"):
            if marker not in source:
                raise RuntimeError(f"{label} is missing balanced-program marker {marker!r}")
    if not (home.index('id="research-i-overview"') < home.index('id="p89-frontier"') < home.index('id="research-iii-overview"')):
        raise RuntimeError("Overview does not preserve Research I -> Research II/P89 -> Research III order")
    if 'id="p88-frontier"' in home:
        raise RuntimeError("historical P88 frontier must remain off the Overview")
    if atlas.index('id="p89-frontier"') > atlas.index('id="p88-frontier"'):
        raise RuntimeError("Visual Atlas must lead with P89 before historical P88")
    if 'id="three-stage-progress"' not in plain:
        raise RuntimeError("Plain Language lacks the balanced three-stage progress section")
    if 'id="program-stages"' not in start:
        raise RuntimeError("Start Here lacks the balanced three-stage program section")
    if "89 results · current frontier P89" not in plain or "89 results · current frontier P89" not in start:
        raise RuntimeError("reader entry pages do not expose the current Research II record")


def main() -> None:
    promote_index()
    promote_visual_atlas()
    promote_plain_language()
    promote_start_here()
    promote_research_map()
    promote_misc_website()
    assert_balanced_reader_state()
    print("[P89] promoted balanced public reader surfaces to Research II frontier P89")


if __name__ == "__main__":
    main()
