"""Finalize P88 reader contracts after the publication-metadata migration.

This maintenance step fixes residual reader-facing P87 assumptions without
reverting the compact README architecture. It also makes the current P88 audit
path explicit on the public Research Map and corrects the Start Here frontier
summary so it describes P88 rather than P87.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def write(relative: str, text: str) -> None:
    (ROOT / relative).write_text(text, encoding="utf-8")


def replace_required(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"{label}: expected text not found: {old!r}")
    return text.replace(old, new, 1)


def fix_start_here_frontier() -> None:
    path = "website/start-here.html"
    text = read(path)
    old = '''      <p><strong>P86 is the previous exact frontier.</strong> It audits 10,560 sign-normalized four-event functionals with primitive coefficient magnitudes {1,1,1,2}. Its strict exact-rational witness satisfies <strong>L85 = 0 &lt; L86 = 1/192</strong>, so the minimally weighted four-event family can separate a P75 parameter box that remains compatible with the complete P85 certificate.</p>
      <p><strong>P88 is the current exact frontier.</strong> It exhausts every nonzero primitive integer four-event coefficient vector with |c_i| at most 2, modulo one global sign. The family contains 39,600 exact functionals, and on the same rational witness it gives <strong>L86 = 1/192 &lt; L87 = 1/96</strong>.</p>'''
    new = '''      <p><strong>P86 is an earlier exact frontier.</strong> It audits 10,560 sign-normalized four-event functionals with primitive coefficient magnitudes {1,1,1,2}. Its strict exact-rational witness satisfies <strong>L85 = 0 &lt; L86 = 1/192</strong>.</p>
      <p><strong>P87 is the previous exact frontier.</strong> It completes every nonzero primitive integer four-event coefficient vector with |c_i| at most 2, modulo one global sign. The family contains 39,600 exact functionals and strengthens the hierarchy to <strong>L86 = 1/192 &lt; L87 = 1/96</strong>.</p>
      <p><strong>P88 is the current exact frontier.</strong> It enlarges the complete primitive coefficient radius from 2 to 3. There are 632 sign-normalized primitive patterns per four-event subset and 208,560 exact functionals in total. On the established rational witness, the empirical value is -11/8, the exact P75 interval is [-1,2], the mismatch is 3/8, the centered norm is 24, and the certified lower bound strengthens to <strong>L87 = 1/96 &lt; L88 = 1/64</strong>.</p>'''
    text = replace_required(text, old, new, path)
    text = replace_required(
        text,
        '<a class="button primary" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md">Read P87</a>',
        '<a class="button primary" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md">Read P88</a>',
        path,
    )
    write(path, text)


def fix_research_map_frontier() -> None:
    path = "website/research-map.html"
    text = read(path)
    text = text.replace(
        "P77-P87: from full-law rejection to exact dependency-aware certification",
        "P77-P88: from full-law rejection to exact dependency-aware certification",
        1,
    )
    text = text.replace(
        'href="index.html#p87-frontier">Continue to the current P88 frontier</a>',
        'href="index.html#p88-frontier">Continue to the current P88 frontier</a>',
        1,
    )
    text = text.replace(
        '<section class="boundary" id="p87-reader-frontier"><div class="section-head"><p class="eyebrow">Current exact frontier · P87</p>',
        '<section class="boundary" id="p87-reader-frontier"><div class="section-head"><p class="eyebrow">Previous exact frontier · P87</p>',
        1,
    )
    old = '''<section id="p88-research-map"><div class="section-head"><p class="eyebrow">IV-Q · Radius-three primitive parity-functional separation</p><h2>P88: Does the next complete coefficient radius expose a stronger incompatibility?</h2></div><div class="result-grid"><article class="result"><span>P88</span><h3>Exact radius-three bounded primitive four-event certificate</h3><p>P88 keeps the four-event order fixed and enlarges the primitive integer coefficient box from |c_i| ≤ 2 to |c_i| ≤ 3. The complete family contains 632 sign-normalized coefficient patterns per four-event subset and 208,560 exact functionals. On the established rational witness it strictly improves the certified full-law bound from L87 = 1/96 to L88 = 1/64.</p></article></div><div class="figure-card"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p88_exact_radius_three_bounded_primitive_quad_projection_parity.svg" alt="P88 exact radius-three bounded primitive four-event certificate"/><div><h3>P88 radius-three certificate</h3><p>The strict functional uses coefficients (1, −1, −3, 2), empirical value −11/8, exact P75 interval [−1, 2], mismatch 3/8, and centered norm 24.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md">Read Proposition 88</a></div></div></section>'''
    new = '''<section id="p88-research-map"><div class="section-head"><p class="eyebrow">IV-Q · Radius-three primitive parity-functional separation</p><h2>P88: Does the next complete coefficient radius expose a stronger incompatibility?</h2></div><div class="result-grid"><article class="result"><span>P88</span><h3>Exact radius-three bounded primitive four-event certificate</h3><p>P88 keeps the four-event order fixed and enlarges the primitive integer coefficient box from |c_i| &lt;= 2 to |c_i| &lt;= 3. The complete family contains 632 sign-normalized coefficient patterns per four-event subset and 208,560 exact functionals. On the established rational witness it strictly improves the certified full-law bound through <strong>L85 = 0 &lt; L86 = 1/192 &lt; L87 = 1/96 &lt; L88 = 1/64</strong>.</p></article></div><div class="figure-card"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p88_exact_radius_three_bounded_primitive_quad_projection_parity.svg" alt="P88 exact radius-three bounded primitive four-event certificate"/><div><h3>P88 radius-three certificate</h3><p>The strict functional uses coefficients (1, -1, -3, 2), empirical value -11/8, exact P75 interval [-1, 2], mismatch 3/8, and centered norm 24.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md">Read Proposition 88</a></div></div><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p88_equation_provenance.md">Audit P88 provenance</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/radius_three_bounded_primitive_quad_projection_parity_functional_separation.py">implementation</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_radius_three_bounded_primitive_quad_projection_parity_functional_separation.py">exact tests</a> · <a href="index.html#p88-frontier">current-frontier overview</a></p></section>'''
    text = replace_required(text, old, new, path)
    write(path, text)


def fix_generated_contract_tests() -> None:
    path = "tests/test_readme_research_orientation.py"
    text = read(path).replace('assert "**P1**" in detail', 'assert "Propositions **P1-P10**" in detail')
    write(path, text)

    path = "tests/test_public_reader_layering.py"
    text = read(path).replace('    assert \'href="measurement-science.html"\' in text\n', "")
    write(path, text)

    path = "tests/test_reader_experience.py"
    text = read(path)
    first_pattern = re.compile(
        r"def test_first_reader_surfaces_match_p88_frontier\(\) -> None:.*?\n\ndef test_no_reader_facing_html_page_advertises_pre_p86_as_current",
        flags=re.DOTALL,
    )
    first_replacement = '''def test_first_reader_surfaces_match_p88_frontier() -> None:
    start = _text("website/start-here.html")
    research_map = _text("website/research-map.html")
    plain = _text("website/plain-language.html")
    assert "88-result theorem program and current P88 frontier" in start
    assert "P78-P88 progressively tighten global separation" in start
    assert "P88 is the current exact frontier." in start
    assert "208,560" in start
    assert "L87 = 1/96 &lt; L88 = 1/64" in start
    assert ">Read P88</a>" in start
    assert 'id="research-origin"' in start
    assert "10.1016/j.chaos.2015.03.014" in start
    assert "The 88 propositions by scientific role" in start
    assert "You do not need to read 88 proofs in order" in start
    assert "complete 88-result dependency structure" in start
    assert "Physical descriptor" in start
    assert "Observation channel" in start
    assert "through Proposition 88" in research_map
    assert "Eighty-eight results" in research_map
    assert "<strong>88</strong>" in research_map
    assert "P73-P88" in research_map
    assert "p88_equation_provenance.md" in research_map
    assert "<strong>88</strong><span>proposition-level results</span>" in plain
    assert "<strong>P88</strong><span>current theorem frontier</span>" in plain
    assert "What the 88 results are doing" in plain
    assert "P75-P88" in plain
    assert "actual P88 research frontier" in plain
    assert "shows how all 88 results connect" in plain


def test_no_reader_facing_html_page_advertises_pre_p86_as_current'''
    text, count = first_pattern.subn(first_replacement, text, count=1)
    if count != 1:
        raise RuntimeError("reader-experience current-frontier test block not found")

    verifier_pattern = re.compile(
        r"def test_repository_verifier_tracks_p86_and_all_86_propositions\(\) -> None:.*\Z",
        flags=re.DOTALL,
    )
    verifier_replacement = '''def test_repository_verifier_tracks_p88_and_all_88_propositions() -> None:
    verifier = _text("scripts/verify_repository.py")
    assert 'CURRENT_FRONTIER = "P88"' in verifier
    assert "for number in range(1, 89):" in verifier
    assert '"docs/reader_experience_and_visual_standard.md"' in verifier
    assert '"docs/proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md"' in verifier
'''
    text, count = verifier_pattern.subn(verifier_replacement, text, count=1)
    if count != 1:
        raise RuntimeError("reader-experience verifier test block not found")
    write(path, text)


def main() -> None:
    fix_start_here_frontier()
    fix_research_map_frontier()
    fix_generated_contract_tests()
    print("Finalized P88 reader contracts and audit surfaces.")


if __name__ == "__main__":
    main()
