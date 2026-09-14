"""Synchronize every public reader surface to the canonical P88 frontier.

Historical P87/P86 theorem material is preserved as history. Current-result counts,
frontier labels, navigation prose, and the P88 visual summary are made explicit and
idempotent so rerunning this script cannot recreate a split publication state.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

P88_FIGURE = "p88_exact_radius_three_bounded_primitive_quad_projection_parity.svg"
P88_PROOF = "proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md"
P88_PROVENANCE = "p88_equation_provenance.md"
P88_IMPLEMENTATION = "radius_three_bounded_primitive_quad_projection_parity_functional_separation.py"
P88_TEST = "test_radius_three_bounded_primitive_quad_projection_parity_functional_separation.py"

P88_HOME = f'''<!-- current-frontier-home: P88 -->
<section id="p88-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head">
    <p class="eyebrow">Current theorem frontier · P88</p>
    <h2>Radius-three bounded primitive four-event parity certificate</h2>
    <p>P88 enlarges the complete primitive four-event coefficient box from |c_i| at most 2 to |c_i| at most 3. Its 208,560-function exact audit strictly strengthens the complete P87 certificate on the same rational witness.</p>
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
  <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P88_PROOF}">Open the P88 theorem</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P88_PROVENANCE}">Equation provenance</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/{P88_IMPLEMENTATION}">Implementation</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/{P88_TEST}">Exact tests</a></p>
</section>

'''

P88_ATLAS = f'''<!-- current-frontier-visual: P88 -->
<section id="p88-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head">
    <p class="eyebrow">Current theorem frontier · P88</p>
    <h2>Radius-three bounded primitive four-event parity certificate</h2>
    <p>The complete radius-three primitive family contains 208,560 exact functionals and raises the established witness bound from 1/96 to 1/64.</p>
  </div>
  <div class="theorem-figure-shell">
    <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/{P88_FIGURE}" aria-label="Open the full P88 theorem figure">
      <img loading="eager" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/{P88_FIGURE}" alt="P88 exact radius-three bounded primitive four-event certificate" />
    </a>
  </div>
  <div class="frontier-summary-grid">
    <article class="frontier-summary-card"><h3>Complete radius-three family</h3><p>632 primitive sign-normalized coefficient patterns across 330 four-event subsets produce 208,560 exact functionals.</p></article>
    <article class="frontier-summary-card"><h3>Exact strict hierarchy</h3><p><strong>L85 = 0 &lt; L86 = 1/192 &lt; L87 = 1/96 &lt; L88 = 1/64</strong>.</p></article>
    <article class="frontier-summary-card"><h3>Strict witness</h3><p>Coefficients (1, −1, −3, 2), empirical value −11/8, P75 interval [−1, 2], gap 3/8, centered norm 24.</p></article>
  </div>
  <div class="boundary"><p><strong>Scientific boundary:</strong> conditional model separation inside the declared P75 family; the physical-to-experiential bridge remains open.</p></div>
  <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P88_PROOF}">Open the P88 theorem</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P88_PROVENANCE}">Equation provenance</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/{P88_IMPLEMENTATION}">Implementation</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/{P88_TEST}">Exact tests</a></p>
</section>

'''

P88_RESEARCH_MAP_SECTION = f'''
<section id="p88-research-map"><div class="section-head"><p class="eyebrow">IV-Q · Radius-three primitive parity-functional separation</p><h2>P88: Does the next complete coefficient radius expose a stronger incompatibility?</h2></div><div class="result-grid"><article class="result"><span>P88</span><h3>Exact radius-three bounded primitive four-event certificate</h3><p>P88 keeps the four-event order fixed and enlarges the primitive integer coefficient box from |c_i| ≤ 2 to |c_i| ≤ 3. The complete family contains 632 sign-normalized coefficient patterns per four-event subset and 208,560 exact functionals. On the established rational witness it strictly improves the certified full-law bound from L87 = 1/96 to L88 = 1/64.</p></article></div><div class="figure-card"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/{P88_FIGURE}" alt="P88 exact radius-three bounded primitive four-event certificate"/><div><h3>P88 radius-three certificate</h3><p>The strict functional uses coefficients (1, −1, −3, 2), empirical value −11/8, exact P75 interval [−1, 2], mismatch 3/8, and centered norm 24.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P88_PROOF}">Read Proposition 88</a></div></div></section>
'''


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_many(text: str, replacements: tuple[tuple[str, str], ...]) -> str:
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def upsert_section(text: str, section_id: str, replacement: str, before_id: str) -> str:
    pattern = re.compile(
        rf'(?:<!--\s*current-frontier-(?:home|visual):\s*P88\s*-->\s*)?'
        rf'<section id="{re.escape(section_id)}"(?=[\s>]).*?</section>\s*',
        flags=re.DOTALL,
    )
    matches = tuple(pattern.finditer(text))
    if matches:
        # Collapse inherited duplicate sections and any orphaned P88 frontier
        # comments before inserting one canonical marker + section pair.
        text = pattern.sub("", text)
        text = re.sub(
            r'<!--\s*current-frontier-(?:home|visual):\s*P88\s*-->\s*',
            "",
            text,
        )
        marker = f'<section id="{before_id}"'
        if marker not in text:
            raise RuntimeError(f"cannot place {section_id}: missing {before_id} marker")
        return text.replace(marker, replacement + marker, 1)
    marker = f'<section id="{before_id}"'
    if marker not in text:
        raise RuntimeError(f"cannot insert {section_id}: missing {before_id} marker")
    return text.replace(marker, replacement + marker, 1)


def promote_index() -> None:
    path = "website/index.html"
    text = read(path)
    text = replace_many(
        text,
        (
            ("Explore all 87 results", "Explore all 88 results"),
            ("<div><strong>87</strong><span>proposition-level results</span></div>", "<div><strong>88</strong><span>proposition-level results</span></div>"),
            ("<div><strong>P87</strong><span>current theorem frontier</span></div>", "<div><strong>P88</strong><span>current theorem frontier</span></div>"),
            ("<section id=\"p87-frontier\" class=\"theorem-frontier current-frontier-visual\">", "<section id=\"p87-frontier\" class=\"theorem-frontier\">"),
            ("Current theorem frontier · P87", "Previous theorem frontier · P87"),
            ("87 proposition-level results through P87", "88 proposition-level results through P88"),
            ("The 87 results form several dependency branches.", "The 88 results form several dependency branches."),
            ("The 87-result program", "The 88-result program"),
            ("all 87 propositions", "all 88 propositions"),
            ("all 87 results", "all 88 results"),
            ("P71-P87", "P71-P88"),
            ("P73-P87", "P73-P88"),
            ("P74-P87", "P74-P88"),
            ("P75 → P87", "P75 → P88"),
            ("P75-P87", "P75-P88"),
            ("P1-P87", "P1-P88"),
            ("P87 certification ladder", "P88 certification ladder"),
            ("<!-- Current theorem asset: docs/figures/p87_exact_bounded_primitive_quad_projection_parity.svg -->", f"<!-- Current theorem asset: docs/figures/{P88_FIGURE} -->"),
        ),
    )
    text = upsert_section(text, "p88-frontier", P88_HOME, "p87-frontier")
    write(path, text)


def promote_visual_atlas() -> None:
    path = "website/visual-atlas.html"
    text = read(path)
    text = replace_many(
        text,
        (
            ("<!-- current-frontier-visual: P87 -->\n", ""),
            ("<section id=\"p87-frontier\" class=\"theorem-frontier current-frontier-visual\">", "<section id=\"p87-frontier\" class=\"theorem-frontier\">"),
            ("<section id=\"p86-frontier\" class=\"theorem-frontier current-frontier-visual\">", "<section id=\"p86-frontier\" class=\"theorem-frontier\">"),
            ("P86 is the current exact continuous-model frontier.", "P86 is an earlier exact continuous-model frontier."),
            ("Current theorem frontier · P87", "Previous theorem frontier · P87"),
            ("Current frontier · P87", "Previous frontier · P87"),
            ("P1-P87", "P1-P88"),
            ("87 results", "88 results"),
        ),
    )
    text = upsert_section(text, "p88-frontier", P88_ATLAS, "p87-frontier")
    write(path, text)


def promote_plain_language() -> None:
    path = "website/plain-language.html"
    text = read(path)
    text = replace_many(
        text,
        (
            ("<div><strong>87</strong><span>proposition-level results</span></div>", "<div><strong>88</strong><span>Research II proposition-level results</span></div>"),
            ("<div><strong>P87</strong><span>current theorem frontier</span></div>", "<div><strong>P88</strong><span>current Research II theorem frontier</span></div>"),
            ("<div><strong>88</strong><span>proposition-level results</span></div>", "<div><strong>88</strong><span>Research II proposition-level results</span></div>"),
            ("<div><strong>P88</strong><span>current theorem frontier</span></div>", "<div><strong>P88</strong><span>current Research II theorem frontier</span></div>"),
            ("What the 87 results are doing", "What the 88 results are doing"),
            ("P75-P87", "P75-P88"),
            ("actual P87 research frontier", "actual P88 research frontier"),
            ("all 87 results", "all 88 results"),
            ("id=\"p87-reader-frontier\"", "id=\"p88-reader-frontier\""),
            ("Current exact frontier · P87", "Current exact frontier · P88"),
        ),
    )
    write(path, text)


def promote_start_here() -> None:
    path = "website/start-here.html"
    text = read(path)
    text = replace_many(
        text,
        (
            ("the 87-result theorem program and current P87 frontier", "the 88-result theorem program and current P88 frontier"),
            ("<div><strong>87</strong><span>proposition-level results</span></div>", "<div><strong>88</strong><span>proposition-level results</span></div>"),
            ("<div><strong>P87</strong><span>current theorem frontier</span></div>", "<div><strong>P88</strong><span>current theorem frontier</span></div>"),
            ("You do not need to read 87 proofs in order", "You do not need to read 88 proofs in order"),
            ("complete 87-result dependency structure", "complete 88-result dependency structure"),
            ("P78-P87 progressively tighten global separation", "P78-P88 progressively tighten global separation"),
            ("P74-P84.</p>", "P74-P88.</p>"),
            ("P87 is the current exact frontier", "P88 is the current exact frontier"),
        ),
    )
    write(path, text)


def promote_research_map() -> None:
    path = "website/research-map.html"
    text = read(path)
    text = replace_many(
        text,
        (
            ("through Proposition 87", "through Proposition 88"),
            ("Eighty-seven results, one dependency-aware scientific program", "Eighty-eight results, one dependency-aware scientific program"),
            ("<div><strong>87</strong><span>proposition-level results</span></div>", "<div><strong>88</strong><span>proposition-level results</span></div>"),
            ("culminating in P87 exact bounded primitive four-event shared-parameter parity-functional separation.", "culminating in P88 exact radius-three bounded primitive four-event shared-parameter parity-functional separation."),
            ("<article class=\"result\"><span>9 · P45-P53</span>", "<article class=\"result\"><span>9 · P45-P60</span>"),
            ("<article class=\"result\"><span>10 · P54-P70</span>", "<article class=\"result\"><span>10 · P61-P70</span>"),
            ("while P87 completes every nonzero primitive four-event coefficient vector with magnitude at most two and strictly strengthens the P86 certificate.", "while P87 completes every nonzero primitive four-event coefficient vector with magnitude at most two and strictly strengthens the P86 certificate, and P88 enlarges that complete primitive coefficient radius to three and raises the same exact witness bound from 1/96 to 1/64."),
        ),
    )
    section_pattern = re.compile(r'<section id="p88-research-map"(?=[\s>]).*?</section>\s*', re.DOTALL)
    if section_pattern.search(text):
        text = section_pattern.sub("", text)
        if "</main>" not in text:
            raise RuntimeError("website/research-map.html has no closing main marker")
        text = text.replace("</main>", P88_RESEARCH_MAP_SECTION + "\n</main>", 1)
    elif "P88: Does the next complete coefficient radius expose a stronger incompatibility?" not in text:
        if "</main>" not in text:
            raise RuntimeError("website/research-map.html has no closing main marker")
        text = text.replace("</main>", P88_RESEARCH_MAP_SECTION + "\n</main>", 1)
    write(path, text)


def promote_status_surfaces() -> None:
    files = (
        "website/implementation.html",
        "website/sources.html",
        "docs/research_map.md",
        "docs/research_navigation.md",
        "docs/theorem_roadmap.md",
        "docs/detailed_proposition_record.md",
        "docs/figure_catalog.md",
        "docs/reproducibility.md",
        "figures/CURRENT_FRONTIER.md",
        "figures/README.md",
    )
    replacements = (
        ("current exact frontier is P87", "current exact frontier is P88"),
        ("P87 is the current exact frontier", "P88 is the current exact frontier"),
        ("Current theorem source · P87", "Current theorem source · P88"),
        ("Current theorem frontier · P87", "Current theorem frontier · P88"),
        ("Current frontier · P87", "Current frontier · P88"),
        ("public theorem frontier is **P87**", "public theorem frontier is **P88**"),
        ("87 proposition-level results through P87", "88 proposition-level results through P88"),
        ("87 propositions", "88 propositions"),
        ("87 results", "88 results"),
        ("P1-P87", "P1-P88"),
        ("P71-P87", "P71-P88"),
        ("P73-P87", "P73-P88"),
        ("P74-P87", "P74-P88"),
        ("P75-P87", "P75-P88"),
        ("P75 → P87", "P75 → P88"),
    )
    for path in files:
        target = ROOT / path
        if target.exists():
            write(path, replace_many(read(path), replacements))


def append_navigation_records() -> None:
    record = ROOT / "docs/detailed_proposition_record.md"
    if not record.exists():
        return
    text = record.read_text(encoding="utf-8")
    if "Proposition 88:" in text:
        return
    text += (
        "\n\n## Proposition 88: Exact Radius-Three Bounded Primitive Four-Event Projection-Parity Functional Certificate\n\n"
        "P88 enlarges the completed P87 primitive coefficient box to `0 < |c_i| <= 3`, exhausts 632 sign-normalized primitive coefficient patterns across 330 four-event subsets (208,560 exact functionals), and on the established rational witness strengthens the full-law `L_infinity` lower bound from `1/96` to `1/64`.\n\n"
        f"- [Proof]({P88_PROOF})\n- [Equation provenance]({P88_PROVENANCE})\n"
        f"- Implementation: `src/consciousness_bridge/{P88_IMPLEMENTATION}`\n"
        f"- Tests: `tests/{P88_TEST}`\n- Figure: `figures/{P88_FIGURE}`\n\n"
        "**Boundary:** conditional model separation only; the physical-to-experiential bridge remains open.\n"
    )
    record.write_text(text, encoding="utf-8")


def verify_reader_coherence() -> None:
    texts = {
        path: read(path)
        for path in (
            "website/index.html",
            "website/plain-language.html",
            "website/start-here.html",
            "website/research-map.html",
            "website/visual-atlas.html",
        )
    }
    required = {
        "website/index.html": (
            "Explore all 88 results",
            "<strong>P88</strong><span>current theorem frontier</span>",
            'id="p88-frontier" class="theorem-frontier current-frontier-visual"',
            "The 88 results form several dependency branches.",
            "The 88-result program",
            "L85 = 0 &lt; L86 = 1/192 &lt; L87 = 1/96 &lt; L88 = 1/64",
        ),
        "website/plain-language.html": (
            "<strong>88</strong><span>Research II proposition-level results</span>",
            "<strong>P88</strong><span>current Research II theorem frontier</span>",
            "What the 88 results are doing",
            "Current exact frontier · P88",
        ),
        "website/start-here.html": (
            "the 88-result theorem program and current P88 frontier",
            "<strong>88</strong><span>proposition-level results</span>",
            "<strong>P88</strong><span>current theorem frontier</span>",
            "You do not need to read 88 proofs in order",
        ),
        "website/research-map.html": (
            "through Proposition 88",
            "Eighty-eight results, one dependency-aware scientific program",
            "<strong>88</strong><span>proposition-level results</span>",
            "P88: Does the next complete coefficient radius expose a stronger incompatibility?",
        ),
        "website/visual-atlas.html": (
            "<!-- current-frontier-visual: P88 -->",
            'id="p88-frontier" class="theorem-frontier current-frontier-visual"',
            "L85 = 0 &lt; L86 = 1/192 &lt; L87 = 1/96 &lt; L88 = 1/64",
            P88_IMPLEMENTATION,
            P88_TEST,
        ),
    }
    for path, markers in required.items():
        missing = [marker for marker in markers if marker not in texts[path]]
        if missing:
            raise RuntimeError(f"{path} missing P88 coherence markers: {missing}")

    forbidden = {
        "website/index.html": (
            "The 87 results form several dependency branches.",
            "The 87-result program",
            "Current theorem frontier · P87",
            "Current theorem asset: docs/figures/p87_exact_bounded_primitive_quad_projection_parity.svg",
        ),
        "website/plain-language.html": (
            "<strong>P87</strong><span>current theorem frontier</span>",
            "<strong>88</strong><span>proposition-level results</span>",
            "<strong>P88</strong><span>current theorem frontier</span>",
            "What the 87 results are doing",
        ),
        "website/start-here.html": (
            "the 87-result theorem program and current P87 frontier",
            "<strong>P87</strong><span>current theorem frontier</span>",
            "You do not need to read 87 proofs in order",
            "complete 87-result dependency structure",
        ),
        "website/research-map.html": (
            "through Proposition 87",
            "Eighty-seven results, one dependency-aware scientific program",
            "<div><strong>87</strong><span>proposition-level results</span></div>",
        ),
        "website/visual-atlas.html": (
            "<!-- current-frontier-visual: P87 -->",
            '<section id="p86-frontier" class="theorem-frontier current-frontier-visual">',
            "P86 is the current exact continuous-model frontier.",
        ),
    }
    for path, markers in forbidden.items():
        present = [marker for marker in markers if marker in texts[path]]
        if present:
            raise RuntimeError(f"{path} retains stale pre-P88 status markers: {present}")

    index = texts["website/index.html"]
    atlas = texts["website/visual-atlas.html"]
    research_map = texts["website/research-map.html"]
    if index.count('id="p88-frontier"') != 1:
        raise RuntimeError("homepage must contain exactly one P88 frontier section")
    if index.count("<!-- current-frontier-home: P88 -->") != 1:
        raise RuntimeError("homepage must contain exactly one P88 frontier marker")
    if atlas.count('id="p88-frontier"') != 1:
        raise RuntimeError("Visual Atlas must contain exactly one P88 frontier section")
    if atlas.count("<!-- current-frontier-visual: P88 -->") != 1:
        raise RuntimeError("Visual Atlas must contain exactly one P88 frontier marker")
    if research_map.count('id="p88-research-map"') != 1:
        raise RuntimeError("Research Map must contain exactly one P88 result section")
    if index.index('id="p88-frontier"') > index.index('id="p87-frontier"'):
        raise RuntimeError("homepage does not lead with P88")
    if atlas.index('id="p88-frontier"') > atlas.index('id="p87-frontier"'):
        raise RuntimeError("Visual Atlas does not lead with P88")


if __name__ == "__main__":
    promote_index()
    promote_visual_atlas()
    promote_plain_language()
    promote_start_here()
    promote_research_map()
    promote_status_surfaces()
    append_navigation_records()
    verify_reader_coherence()
    print("Promoted reader-facing publication surfaces to coherent 88/P88 state")
