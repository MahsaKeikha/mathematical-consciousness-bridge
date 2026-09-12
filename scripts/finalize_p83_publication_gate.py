"""One-shot P83 publication-gate finalizer.

Repairs the final reader-facing and CI consistency gaps before P83 review:
- adds an explicit README research-status table,
- sharpens the P83 source interpretation boundary,
- restores the missing v0.82.0 changelog archive,
- integrates P83 inside the research-map continuous-model frontier,
- updates the website-orientation regression test to the P83 frontier.

The calling workflow removes this script after successful application.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, *, path: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"expected exactly one anchor in {path}, found {count}: {old[:100]!r}")
    return text.replace(old, new, 1)


def update_readme() -> None:
    path = "README.md"
    text = read(path)
    row = "| Public theorem frontier | **P83** |"
    if row in text:
        return

    anchor = "> **What mathematical and physical conditions would be required for a complete physical description of a system to support a scientifically testable claim about consciousness?**"
    table = """| Research status | Current value |
| --- | --- |
| Formal release | **v0.82.0** |
| Public theorem frontier | **P83** |
| Proposition-level results | **83** |
| Physical-to-experiential bridge | **Open** |

"""
    text = replace_once(text, anchor, table + anchor, path=path)
    write(path, text)


def sharpen_p83_source_boundary() -> None:
    path = "src/consciousness_bridge/projection_parity_model_separation.py"
    text = read(path)
    old = """This is a computational certificate for the declared P75 latent model. It does
not validate that model, identify a latent state with consciousness, or close the
physical-to-experiential bridge."""
    new = """This certificate does not validate the P75 model, does not identify a latent
state with consciousness, and does not close the physical-to-experiential bridge."""
    text = replace_once(text, old, new, path=path)
    write(path, text)


def restore_v082_changelog() -> None:
    path = "CHANGELOG.md"
    text = read(path)
    heading = "# 0.82.0 - 2026-09-12"
    if heading in text:
        return

    marker = "# 0.81.0 - 2026-09-11"
    section = """# 0.82.0 - 2026-09-12

- Added Proposition 82, Exact Nested Projection-Contrast Certificate for Continuous P75 Separation.
- Added 256 genuinely new nested residual-event contrasts while retaining every P81 projection-event lower bound.
- Computed residual-event parameter-box ranges directly from the common P75 latent-branch factorization rather than subtracting separate P81 intervals.
- Defined `L82(B) = max(L81(B), L_nested(B))`, establishing `L82 >= L81 >= L80 >= L78` on every parameter box.
- Added an exact-rational strict-improvement witness with `L80=0`, `L81=1/16`, and `L82=1/12`.
- Preserved the proved P78 mesh-width upper certificate and the P79 one-sided exact-rational sampling-radius rejection gate.
- Added exact implementation, regression tests, proof, equation provenance, theorem figure, reader navigation, website integration, and archival release documentation.
- Published v0.82.0 with 82 proposition-level results, 70 paper-facing equation-driven figures, and 140 SVG assets in the complete visual record.
- Preserved the interpretation boundary that P82 is a conditional model-distance theorem and does not identify a latent state with consciousness or close the physical-to-experiential bridge.

"""
    text = replace_once(text, marker, section + marker, path=path)
    write(path, text)


def integrate_p83_research_map() -> None:
    path = "website/research-map.html"
    text = read(path)

    text = replace_once(
        text,
        "<h2>P77-P82: from full-law rejection to exact nested-contrast certification</h2>",
        "<h2>P77-P83: from full-law rejection to exact dependency-aware certification</h2>",
        path=path,
    )

    p82_card = """    <article class=\"result\"><span>P82</span><h3>Exact nested residual contrasts</h3><p>Use exact ranges of 256 genuinely new residual events from nested cylinders. The concrete exact witness improves the lower bound from P81 = 1/16 to P82 = 1/12.</p><a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_82_exact_nested_projection_contrast.md\">Open P82 →</a></article>"""
    p83_card = """    <article class=\"result\" id=\"p83-frontier\"><span>P83</span><h3>Exact projection-parity constraints</h3><p>Use 22 exact two-, three-, and four-view parity events to expose dependence incompatibility that the complete P82 event family can leave compatible. The exact witness has L82 = 0 and L83 = 1/16.</p><a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_83_exact_projection_parity.md\">Open P83 →</a></article>"""
    if "Open P83 →" not in text.split("</main>", 1)[0]:
        text = replace_once(text, p82_card, p82_card + "\n" + p83_card, path=path)

    old_actions = """  <div class=\"hero-actions\">
    <a class=\"button primary\" href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p82_equation_provenance.md\">Audit P82 equation provenance</a>
    <a class=\"button\" href=\"visual-atlas.html\">See the P82 theorem figure</a>
    <a class=\"button\" href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/nested_projection_contrast_separation.py\">Open implementation</a>
    <a class=\"button\" href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_nested_projection_contrast_separation.py\">Open tests</a>
  </div>"""
    new_actions = """  <div class=\"hero-actions\">
    <a class=\"button primary\" href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p83_equation_provenance.md\">Audit P83 equation provenance</a>
    <a class=\"button\" href=\"visual-atlas.html\">See the P83 theorem figure</a>
    <a class=\"button\" href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/projection_parity_model_separation.py\">Open P83 implementation</a>
    <a class=\"button\" href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_projection_parity_model_separation.py\">Open P83 tests</a>
  </div>"""
    text = replace_once(text, old_actions, new_actions, path=path)

    appended = """<section id=\"p83-frontier\"><div class=\"section-head\"><p class=\"eyebrow\">IV-M · Dependency-aware parity separation</p><h2>P83: Can a parity constraint reject a P75 box that every P82 event leaves compatible?</h2></div><div class=\"result-grid\"><article class=\"result\"><span>P83A</span><h3>Exact branch parity identity</h3><p>Conditional independence gives a closed product formula for every two-, three-, and four-view parity probability.</p></article><article class=\"result\"><span>P83B</span><h3>Exact rational box extremization</h3><p>The product is multi-affine, so branch extrema occur at response-coordinate vertices; prevalence is then extremized at its endpoints.</p></article><article class=\"result\"><span>P83C</span><h3>Strict strengthening of P82</h3><p>The 22-event family is combined with the complete P82 certificate. An exact witness has L82 = 0 while L83 = 1/16.</p></article></div><div class=\"figure-card\"><img src=\"https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p83_exact_projection_parity.svg\" alt=\"P83 exact projection-parity certificate\"/><div><h3>P83 exact projection parity</h3><p>Parity makes an interaction constraint explicit without treating it as a consciousness variable. The full derivation, exact witness, code, and interpretation boundary are auditable from the proposition record.</p><a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_83_exact_projection_parity.md\">Read Proposition 83 →</a></div></div><p><a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p83_equation_provenance.md\">Open P83 equation provenance →</a></p></section>

"""
    if appended in text:
        text = text.replace("</main>\n" + appended, "</main>\n", 1)
    elif text.count('id="p83-frontier"') != 1:
        raise RuntimeError("research-map P83 structure is not uniquely integrated")

    write(path, text)


def update_website_orientation_test() -> None:
    path = "tests/test_website_research_orientation.py"
    text = read(path)
    text = replace_once(
        text,
        'hero = text.index("Eighty-two results, one dependency-aware scientific program")',
        'hero = text.index("Eighty-three results, one dependency-aware scientific program")',
        path=path,
    )
    text = replace_once(
        text,
        '        "proposition_81_projection_event_model_separation.md",\n',
        '        "proposition_81_projection_event_model_separation.md",\n        "p83_equation_provenance.md",\n        "proposition_83_exact_projection_parity.md",\n',
        path=path,
    )
    text = replace_once(
        text,
        "def test_research_map_presents_p77_through_p82_in_dependency_order():",
        "def test_research_map_presents_p77_through_p83_in_dependency_order():",
        path=path,
    )
    text = replace_once(
        text,
        '    assert "through Proposition 82" in text',
        '    assert "through Proposition 83" in text',
        path=path,
    )
    text = replace_once(
        text,
        '    p82 = text.index("Open P82 →", frontier)\n    assert p77 < p78 < p79 < p80 < p81 < p82',
        '    p82 = text.index("Open P82 →", frontier)\n    p83 = text.index("Open P83 →", frontier)\n    assert p77 < p78 < p79 < p80 < p81 < p82 < p83',
        path=path,
    )
    text = replace_once(
        text,
        '    assert "P81 = 1/16 to P82 = 1/12" in text\n',
        '    assert "P81 = 1/16 to P82 = 1/12" in text\n    assert "L82 = 0 and L83 = 1/16" in text\n    assert text.index(\'id="p83-frontier"\') < text.index("</main>")\n',
        path=path,
    )
    write(path, text)


def main() -> None:
    update_readme()
    sharpen_p83_source_boundary()
    restore_v082_changelog()
    integrate_p83_research_map()
    update_website_orientation_test()
    print("P83 publication gate finalized")


if __name__ == "__main__":
    main()
