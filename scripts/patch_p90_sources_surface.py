"""Promote the website sources page from P89 to P90 without erasing history."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "website" / "sources.html"

P90_SECTION = '''<section id="p90-source"><div class="section-head"><p class="eyebrow">Current theorem source · P90</p><h2>Exact nonlinear rank-one slice separation</h2><p>P90 moves beyond the complete P89 linear parity-functional envelope by using an algebraic constraint of the actual strict P75 model image. With prevalence fixed at zero, the active observable law is one product Bernoulli component, so the canonical two-by-two slice must have determinant zero. The empirical determinant residual is <strong>5/192</strong>, the slice mass is <strong>3/8</strong>, and the exact lower and upper certificates meet at <strong>L90 = 5/72 = (7/3)L89</strong>.</p></div><div class="source-grid"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_90_exact_nonlinear_rank_one_separation.md"><h3>Proposition 90</h3><p>Formal nonlinear separation theorem, exact lower bound, rational attaining witness, and scientific boundary.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_90_equation_provenance.md"><h3>P90 provenance</h3><p>Separates inherited product-law and rank-one algebra from the repository-original exact P90 certificate.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/exact_nonlinear_rank_one_separation.py"><h3>P90 implementation</h3><p>Exact rational evaluation of the canonical slice, determinant residual, lower radius, and matching P75 model witness.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_exact_nonlinear_rank_one_separation.py"><h3>P90 exact tests</h3><p>Exact slice, lower certificate, attaining witness, dominance over P89, and scientific-boundary regression tests.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p90_exact_nonlinear_rank_one_separation.svg"><h3>P90 theorem figure</h3><p>Source-controlled visual summary synchronized with the theorem and publication manifest.</p></a></div><div class="boundary"><p><strong>Scientific boundary:</strong> P90 is an exact conditional model-separation theorem for the declared strict P75 box and fixed extreme-prevalence product-law image. It does not identify consciousness, establish nonphysicality, exhaust more general nonlinear mixture constraints, or close the physical-to-experiential bridge.</p></div></section>'''


def main() -> None:
    text = PATH.read_text(encoding="utf-8")
    if 'id="p90-source"' not in text:
        anchor = '<section id="p89-source">'
        if anchor not in text:
            raise RuntimeError("P89 sources section anchor missing")
        text = text.replace(anchor, P90_SECTION + "\n\n" + anchor, 1)
    text = text.replace(
        '<section id="p89-source"><div class="section-head"><p class="eyebrow">Current theorem source · P89</p>',
        '<section id="p89-source"><div class="section-head"><p class="eyebrow">Previous theorem source · P89</p>',
        1,
    )
    if 'Current theorem source · P90' not in text:
        raise RuntimeError("P90 sources section was not promoted")
    PATH.write_text(text, encoding="utf-8")
    print("website sources surface promoted to P90")


if __name__ == "__main__":
    main()
