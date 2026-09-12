"""One-time reader-experience and visual-presentation polish.

This script makes the public website and core documentation consistent with the
P84 frontier, adds a first-reader primer, fixes the P81 Visual Atlas path, and
installs shared figure sizing rules that keep figures readable without allowing
them to dominate the page.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def _write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def _replace_once(path: str, old: str, new: str) -> None:
    text = _read(path)
    if new in text:
        return
    if old not in text:
        raise RuntimeError(f"expected text not found in {path}: {old[:120]!r}")
    _write(path, text.replace(old, new, 1))


def _replace_all(path: str, old: str, new: str) -> None:
    text = _read(path)
    if old not in text:
        if new in text:
            return
        raise RuntimeError(f"expected text not found in {path}: {old[:120]!r}")
    _write(path, text.replace(old, new))


def _write_if_changed(path: str, text: str) -> None:
    target = ROOT / path
    if target.exists() and target.read_text(encoding="utf-8") == text:
        return
    target.write_text(text, encoding="utf-8")


READER_CSS = r'''/* Reader experience v2: publication-safe image sizing and first-reader structure. */

:root {
  --figure-reading-max: 980px;
  --figure-card-media-max: 720px;
  --figure-card-height-max: 500px;
  --figure-theorem-height-max: 640px;
}

/* Images should be large enough to inspect, but never dominate the page. */
.figure-card {
  grid-template-columns: minmax(0, 1.42fr) minmax(250px, 0.58fr);
  align-items: center;
}

.figure-card > *,
.theorem-figure-shell > *,
.result,
.evidence-card,
.reader-primer-card,
.reader-step-card {
  min-width: 0;
}

.figure-card img {
  display: block;
  width: min(100%, var(--figure-card-media-max));
  max-width: 100%;
  height: auto;
  max-height: min(64vh, var(--figure-card-height-max));
  margin: 0 auto;
  object-fit: contain;
}

.theorem-figure-shell {
  width: min(100%, var(--figure-reading-max));
  margin: 24px auto 0;
  padding: clamp(8px, 1.4vw, 16px);
}

.theorem-figure-shell img {
  display: block;
  width: 100%;
  max-width: 100%;
  height: auto;
  max-height: min(72vh, var(--figure-theorem-height-max));
  margin: 0 auto;
  object-fit: contain;
}

.atlas-thumb,
.result .atlas-thumb {
  width: 100%;
  height: clamp(205px, 21vw, 250px);
  max-height: 250px;
  object-fit: contain;
}

.evidence-card img {
  height: clamp(205px, 20vw, 245px);
  max-height: 245px;
  object-fit: contain;
}

.figure-card a:has(img),
.theorem-figure-shell a,
.panel a:has(img) {
  display: block;
  min-width: 0;
}

.figure-display-note {
  max-width: 78ch;
  margin: 14px 0 0;
  color: var(--muted);
  font-size: 0.86rem;
  line-height: 1.58;
}

.reader-primer-grid,
.reader-step-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 13px;
  margin-top: 24px;
}

.reader-step-grid {
  grid-template-columns: repeat(4, minmax(0, 1fr));
}

.reader-primer-card,
.reader-step-card {
  padding: 19px 20px;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--paper);
}

.reader-primer-card strong,
.reader-step-card strong {
  display: block;
  margin-bottom: 6px;
  color: var(--ink);
  font-size: 0.95rem;
  line-height: 1.35;
}

.reader-primer-card p,
.reader-step-card p {
  margin: 0;
  color: var(--muted);
  font-size: 0.86rem;
  line-height: 1.58;
}

.reader-step-card span {
  display: inline-grid;
  width: 26px;
  height: 26px;
  margin-bottom: 10px;
  place-items: center;
  border-radius: 999px;
  background: var(--soft);
  color: var(--accent);
  font-size: 0.72rem;
  font-weight: 800;
}

/* Long equations and labels may wrap or scroll, but may never widen a card. */
.equation,
pre,
code,
.figure-card,
.frontier-summary-card,
.reader-primer-card,
.reader-step-card {
  overflow-wrap: anywhere;
}

@media (max-width: 900px) {
  .figure-card,
  .reader-primer-grid,
  .reader-step-grid {
    grid-template-columns: 1fr;
  }

  .figure-card img {
    width: min(100%, 820px);
    max-height: min(66vh, 540px);
  }

  .reader-primer-grid,
  .reader-step-grid {
    gap: 10px;
  }
}

@media (max-width: 680px) {
  .theorem-figure-shell img {
    max-height: min(62vh, 500px);
  }

  .atlas-thumb,
  .result .atlas-thumb,
  .evidence-card img {
    height: auto;
    max-height: 230px;
  }

  .reader-primer-card,
  .reader-step-card {
    padding: 16px 17px;
  }
}
'''

READER_STANDARD = r'''# Reader Experience and Visual Presentation Standard

## Purpose

The Mathematical Consciousness Bridge is intended to be auditable by specialists and understandable to a technically curious first-time reader. The public website and documentation therefore use progressive disclosure: intuition first, formal statement second, proof and implementation third, and provenance plus scientific boundaries throughout.

This standard governs the website, README-level narrative, proposition documentation, figures, and reader navigation.

## First-reader path

A new reader should be able to move through the project in this order without already knowing the proposition chronology:

1. **Question:** What is the physical-to-experiential bridge problem?
2. **Vocabulary:** What do descriptor, target, latent state, observation channel, compatibility, rejection, and bridge claim mean here?
3. **Architecture:** Which scientific assumptions are tested at each layer?
4. **Current frontier:** What does P84 add beyond P83, in plain language?
5. **Formal theorem:** What is actually proved and under which assumptions?
6. **Implementation:** Which source module computes the declared certificate?
7. **Verification:** Which tests, provenance records, and reproducibility checks protect the result?
8. **Boundary:** What stronger interpretation is explicitly not justified?

No page should require a first-time reader to infer this ordering from proposition numbers alone.

## Progressive disclosure rule

Every mature result should expose four layers of explanation.

| Layer | Reader question | Required content |
| --- | --- | --- |
| Orientation | Why does this result exist? | Plain-language scientific question and failure mode |
| Formal result | What is proved? | Assumptions, definitions, theorem statement, proof route |
| Audit | Can I inspect it? | Implementation, tests, equation provenance, figure provenance |
| Interpretation | What may I conclude? | Exact scientific boundary and unresolved questions |

A page may be mathematically dense, but it should not be conceptually opaque.

## Visual size standard

Figures must remain readable at ordinary laptop and tablet widths without occupying an excessive fraction of the page.

- **Theorem and architecture figures:** preferred reading width 760 to 980 CSS pixels, with a normal maximum display height near 640 pixels or 72 percent of the viewport height. Full-resolution source remains one click away.
- **Figure-and-text cards:** figure area should normally resolve to roughly 520 to 720 CSS pixels on desktop, with a normal maximum display height near 500 pixels.
- **Atlas thumbnails:** use a reading height around 205 to 250 CSS pixels for simple plots and diagrams. Complex theorem figures should not be forced into thumbnail treatment.
- **Mobile:** use the full available content width, preserve aspect ratio, and cap vertical dominance rather than shrinking labels below readable size.
- **Never solve overflow by making text tiny.** If labels are not readable at the intended display size, rewrap, simplify, or split the figure.
- **Never crop mathematical content.** `object-fit: contain` or equivalent behavior is required for reader-facing theorem figures.

The goal is balanced visual hierarchy: a figure should be easy to inspect without becoming a poster that pushes the surrounding explanation off screen.

## Figure reading contract

Every important figure must answer:

1. What am I looking at?
2. How should I read the panels, arrows, axes, or regions?
3. What is the precise takeaway?
4. What is the scientific status of the visual?
5. What conclusion must not be inferred?
6. Where can I open the proof, implementation, tests, or source record?

The [Figure Caption and Description Standard](figure_caption_and_description_standard.md) gives the full figure-level requirements.

## Scientific language standard

Reader-friendly language must not weaken scientific precision.

- Say **compatible with the declared model**, not "proved true."
- Say **certified rejection**, not "disproved consciousness" or any broader ontological conclusion.
- Say **latent state**, not "conscious state," unless an independent semantic bridge has been established.
- Say **physical descriptor is insufficient for the declared target**, not "physics is insufficient."
- Say **non-rejection is inconclusive**, not "the model passed."

The physical-to-experiential bridge remains open unless independently formulated and empirically established.

## Cross-linking standard

A first reader should never reach a theorem or figure dead end. Mature surfaces should link to the nearest relevant items among:

- Start Here
- Research Map
- Visual Atlas
- theorem/proposition proof
- implementation module
- regression tests
- equation and citation provenance
- figure catalog
- reproducibility guide

## Maintenance and regression testing

Reader experience is part of repository quality. Regression tests should catch at least:

- stale proposition counts or stale frontier labels;
- broken public figure paths;
- missing shared visual styles in the Pages build;
- theorem figures without responsive containment;
- figure-display rules that can reintroduce clipping or extreme page dominance;
- missing first-reader explanations on the main orientation surfaces.

This standard does not replace scientific review. It makes the scientific record easier to inspect and harder to misunderstand.
'''

READER_TEST = r'''from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_shared_reader_experience_style_is_built_into_pages() -> None:
    css = _text("website/reader-experience-v2.css")
    prepare = _text("scripts/prepare_website.py")
    assert "--figure-reading-max: 980px" in css
    assert "max-height: min(72vh" in css
    assert ".reader-primer-grid" in css
    assert "READER_EXPERIENCE_STYLE_TAG" in prepare
    assert '"reader-experience-v2.css"' in prepare


def test_first_reader_surfaces_match_p84_frontier() -> None:
    start = _text("website/start-here.html")
    research_map = _text("website/research-map.html")
    assert "The 84 propositions by scientific role" in start
    assert "You do not need to read 84 proofs in order" in start
    assert "complete 84-result dependency structure" in start
    assert "Physical descriptor" in start
    assert "Observation channel" in start
    assert "through Proposition 84" in research_map
    assert "Eighty-four results" in research_map
    assert "<strong>84</strong>" in research_map
    assert "P73-P84" in research_map


def test_visual_atlas_uses_public_paths_and_readable_display_rules() -> None:
    atlas = _text("website/visual-atlas.html")
    assert "../docs/" not in atlas
    assert "Figures are intentionally capped at a readable page size" in atlas
    assert "p81_projection_event_model_separation.svg" in atlas
    assert 'loading="lazy"' in atlas
    assert "theorem-figure-shell" in atlas


def test_reader_and_figure_standards_are_documented() -> None:
    reader = _text("docs/reader_experience_and_visual_standard.md")
    figures = _text("docs/figure_caption_and_description_standard.md")
    assert "## Visual size standard" in reader
    assert "## Display-size standard" in figures
    assert "760 to 980 CSS pixels" in reader
    assert "Never solve overflow by making text tiny" in reader
'''


def main() -> None:
    _write_if_changed("website/reader-experience-v2.css", READER_CSS)
    _write_if_changed("docs/reader_experience_and_visual_standard.md", READER_STANDARD)
    _write_if_changed("tests/test_reader_experience.py", READER_TEST)

    # Shared Pages build: inject and cache-bust the reader-experience stylesheet.
    _replace_once(
        "scripts/prepare_website.py",
        'ASSET_VERSION = "20260912-nav12-p84"',
        'ASSET_VERSION = "20260912-nav13-reader"',
    )
    _replace_once(
        "scripts/prepare_website.py",
        "CONTRAST_STYLE_TAG = (\n    f'<link rel=\"stylesheet\" href=\"contrast-v2.css?v={ASSET_VERSION}\" />'\n)\n",
        "CONTRAST_STYLE_TAG = (\n    f'<link rel=\"stylesheet\" href=\"contrast-v2.css?v={ASSET_VERSION}\" />'\n)\nREADER_EXPERIENCE_STYLE_TAG = (\n    f'<link rel=\"stylesheet\" href=\"reader-experience-v2.css?v={ASSET_VERSION}\" />'\n)\n",
    )
    _replace_once(
        "scripts/prepare_website.py",
        "CONTRAST_STYLE_PATTERN = re.compile(\n    r'<link\\s+rel=\"stylesheet\"\\s+href=\"contrast-v2\\.css(?:\\?v=[^\"]+)?\"\\s*/?>'\n)\n",
        "CONTRAST_STYLE_PATTERN = re.compile(\n    r'<link\\s+rel=\"stylesheet\"\\s+href=\"contrast-v2\\.css(?:\\?v=[^\"]+)?\"\\s*/?>'\n)\nREADER_EXPERIENCE_STYLE_PATTERN = re.compile(\n    r'<link\\s+rel=\"stylesheet\"\\s+href=\"reader-experience-v2\\.css(?:\\?v=[^\"]+)?\"\\s*/?>'\n)\n",
    )
    _replace_once(
        "scripts/prepare_website.py",
        "    text = CONTRAST_STYLE_PATTERN.sub(CONTRAST_STYLE_TAG, text)\n    return text\n",
        "    text = CONTRAST_STYLE_PATTERN.sub(CONTRAST_STYLE_TAG, text)\n    text = READER_EXPERIENCE_STYLE_PATTERN.sub(READER_EXPERIENCE_STYLE_TAG, text)\n    return text\n",
    )
    _replace_once(
        "scripts/prepare_website.py",
        "        if CONTRAST_STYLE_TAG not in text:\n            additions.append(CONTRAST_STYLE_TAG)\n        if SCRIPT_TAG not in text:\n",
        "        if CONTRAST_STYLE_TAG not in text:\n            additions.append(CONTRAST_STYLE_TAG)\n        if READER_EXPERIENCE_STYLE_TAG not in text:\n            additions.append(READER_EXPERIENCE_STYLE_TAG)\n        if SCRIPT_TAG not in text:\n",
    )
    _replace_once(
        "scripts/prepare_website.py",
        '        "contrast-v2.css",\n    )',
        '        "contrast-v2.css",\n        "reader-experience-v2.css",\n    )',
    )

    # Public Start Here: remove stale counts and add a true first-reader primer.
    _replace_once(
        "website/start-here.html",
        "a progressive guide from plain-language intuition to the 84-result theorem program and current P83 frontier.",
        "a progressive guide from plain-language intuition to the 84-result theorem program and current P84 frontier.",
    )
    _replace_all("website/start-here.html", "The 83 propositions by scientific role", "The 84 propositions by scientific role")
    _replace_all("website/start-here.html", "You do not need to read 83 proofs in order", "You do not need to read 84 proofs in order")
    _replace_all("website/start-here.html", "complete 83-result dependency structure", "complete 84-result dependency structure")
    _replace_all("website/start-here.html", "P71-P83, then the falsification program", "P71-P84, then the falsification program")
    _replace_all("website/start-here.html", "P74-P83.", "P74-P84.")

    primer = '''    <section id="reader-primer">\n      <div class="section-head">\n        <p class="eyebrow">Before the equations</p>\n        <h2>Six terms that make the rest of the project easier to follow</h2>\n        <p>You do not need the proposition chronology to understand the logic. These six ideas recur throughout the research and are used consistently.</p>\n      </div>\n      <div class="reader-primer-grid">\n        <article class="reader-primer-card"><strong>Physical descriptor</strong><p>The declared physical information used by a bridge claim: variables, dynamics, interventions, scale, and system boundary.</p></article>\n        <article class="reader-primer-card"><strong>Target</strong><p>An independently specified distinction the physical description is being asked to explain. The target must not be manufactured from the tested descriptor and then treated as independent evidence.</p></article>\n        <article class="reader-primer-card"><strong>Latent state</strong><p>An unobserved variable introduced by a statistical model. A latent state has no experiential meaning merely because it is mathematically useful.</p></article>\n        <article class="reader-primer-card"><strong>Observation channel</strong><p>The measurement process connecting a latent target to reports, labels, behavior, or other observed variables. It can attenuate or erase information.</p></article>\n        <article class="reader-primer-card"><strong>Compatibility and rejection</strong><p>Compatibility means the declared model has not been ruled out by the current certificate. Rejection means the declared model is incompatible under stated assumptions. Neither statement identifies consciousness.</p></article>\n        <article class="reader-primer-card"><strong>Bridge claim</strong><p>The still-open scientific step connecting a sufficiently complete physical description to experiential structure. The repository studies obligations on such a claim without assuming that the bridge is already known.</p></article>\n      </div>\n    </section>\n\n    <section>\n      <div class="section-head">\n        <p class="eyebrow">How to read a proposition</p>\n        <h2>Use four passes instead of reading every proof linearly</h2>\n        <p>Each mature result is designed to support a fast orientation pass and a deeper audit pass.</p>\n      </div>\n      <div class="reader-step-grid">\n        <article class="reader-step-card"><span>1</span><strong>Question</strong><p>Identify the exact scientific failure mode the proposition is designed to prevent or detect.</p></article>\n        <article class="reader-step-card"><span>2</span><strong>Assumptions and theorem</strong><p>Read what is assumed, then what is proved. Do not import conclusions from neighboring propositions.</p></article>\n        <article class="reader-step-card"><span>3</span><strong>Audit trail</strong><p>Open the implementation, tests, equation provenance, and figure record when you want to verify the certificate.</p></article>\n        <article class="reader-step-card"><span>4</span><strong>Interpretation boundary</strong><p>Finish by reading what the result does not establish. This is part of the theorem record, not a disclaimer added afterward.</p></article>\n      </div>\n    </section>\n\n'''
    marker = '    <section id="chain">\n'
    start_text = _read("website/start-here.html")
    if "Six terms that make the rest of the project easier to follow" not in start_text:
        if marker not in start_text:
            raise RuntimeError("start-here chain marker not found")
        _write("website/start-here.html", start_text.replace(marker, primer + marker, 1))

    # Research Map: synchronize the frontier and make the latest model-adequacy branch explicit.
    _replace_once(
        "website/research-map.html",
        "Scientific dependency map of the Mathematical Consciousness Bridge through Proposition 83.",
        "Scientific dependency map of the Mathematical Consciousness Bridge through Proposition 84.",
    )
    _replace_once(
        "website/research-map.html",
        "Eighty-three results, one dependency-aware scientific program",
        "Eighty-four results, one dependency-aware scientific program",
    )
    _replace_all("website/research-map.html", "P71-P83", "P71-P84")
    _replace_once(
        "website/research-map.html",
        "and P83 adds exact projection-parity constraints that expose additional dependence structure.</p>",
        "P83 adds exact projection-parity constraints that expose additional dependence structure, and P84 tests whether pairs of those parity observations remain jointly compatible under one shared P75 parameter assignment.</p>",
    )
    _replace_once(
        "website/research-map.html",
        "<div><strong>83</strong><span>proposition-level results</span></div>",
        "<div><strong>84</strong><span>proposition-level results</span></div>",
    )
    _replace_once(
        "website/research-map.html",
        '<article class="result"><span>6 · P73-P76</span><h3>Channel recovery and model adequacy</h3><p>Identify the declared binary target channel, certify that recovery from finite data, test whether a fourth view supports the model assumptions, then ask whether finite data are strong enough to reject a tracked violation.</p></article>',
        '<article class="result"><span>6 · P73-P84</span><h3>Channel recovery, model adequacy, and certified separation</h3><p>Recover the declared binary target channel, test the model itself, then strengthen rejection from selected constraints to exact global separation of the continuous P75 family, culminating in P84 shared-parameter parity compatibility.</p></article>',
    )
    _replace_once(
        "website/research-map.html",
        '<article class="result" id="p83-frontier"><span>P83</span><h3>Exact projection-parity constraints</h3>',
        '<article class="result" id="p83"><span>P83</span><h3>Exact projection-parity constraints</h3>',
    )
    old_actions = '''  <div class="hero-actions">\n    <a class="button primary" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p83_equation_provenance.md">Audit P83 equation provenance</a>\n    <a class="button" href="visual-atlas.html">See the P83 theorem figure</a>\n    <a class="button" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/projection_parity_model_separation.py">Open P83 implementation</a>\n    <a class="button" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_projection_parity_model_separation.py">Open P83 tests</a>\n  </div>'''
    new_actions = '''  <div class="hero-actions">\n    <a class="button primary" href="#p84">Continue to the current P84 frontier</a>\n    <a class="button" href="visual-atlas.html#p83">See the P83 figure</a>\n    <a class="button" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p83_equation_provenance.md">Audit P83 provenance</a>\n  </div>'''
    _replace_once("website/research-map.html", old_actions, new_actions)

    p84_links = '<p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_84_exact_projection_parity_contrast.md">P84 proof</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/joint_projection_parity_contrast_separation.py">implementation</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_joint_projection_parity_contrast_separation.py">tests</a></p>'
    p84_figure = '''<div class="theorem-figure-shell">\n      <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p84_exact_joint_projection_parity_contrast.svg" aria-label="Open the full P84 theorem figure">\n        <img loading="lazy" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p84_exact_joint_projection_parity_contrast.svg?v=2" alt="P84 joint parity compatibility certificate" />\n      </a>\n    </div>\n    <p class="figure-display-note">The web figure is capped at a reading width so the explanation stays in view. Open the figure itself for the full-resolution SVG.</p>\n    <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_84_exact_projection_parity_contrast.md">P84 proof</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/joint_projection_parity_contrast_separation.py">implementation</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_joint_projection_parity_contrast_separation.py">tests</a></p>'''
    _replace_once("website/research-map.html", p84_links, p84_figure)

    # Visual Atlas: fix the broken Pages-relative P81 path and add display guidance.
    atlas_boundary_old = '''<section class="boundary"><h2>How to read every figure</h2><p><strong>What you are seeing:</strong> identify the mathematical objects, panels, axes, or regions. <strong>How to read it:</strong> follow arrows only as the declared logical, temporal, set-inclusion, or computational relation; compare plotted quantities using the labeled axes and legends. <strong>Main takeaway:</strong> use the accompanying text to identify the precise conclusion the visual supports. <strong>Scientific boundary:</strong> diagrams, synthetic examples, and simulations do not become empirical consciousness evidence merely because they are visually compelling.</p><p>For a direct index of every SVG, including figures not selected for this web page, open the <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figure_catalog.md">Complete Figure Catalog</a>. The repository-wide rules are in the <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figure_caption_and_description_standard.md">Figure Caption and Description Standard</a>.</p></section>'''
    atlas_boundary_new = '''<section class="boundary"><h2>How to read every figure</h2><p><strong>What you are seeing:</strong> identify the mathematical objects, panels, axes, or regions. <strong>How to read it:</strong> follow arrows only as the declared logical, temporal, set-inclusion, or computational relation; compare plotted quantities using the labeled axes and legends. <strong>Main takeaway:</strong> use the accompanying text to identify the precise conclusion the visual supports. <strong>Scientific boundary:</strong> diagrams, synthetic examples, and simulations do not become empirical consciousness evidence merely because they are visually compelling.</p><p>Figures are intentionally capped at a readable page size: large enough to inspect, but not so large that the explanatory text disappears below the fold. Complex theorem figures use a wider presentation than simple atlas thumbnails, and the full-resolution SVG remains available from the figure link.</p><p>For a direct index of every SVG, including figures not selected for this web page, open the <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figure_catalog.md">Complete Figure Catalog</a>. The repository-wide rules are in the <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figure_caption_and_description_standard.md">Figure Caption and Description Standard</a> and the <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/reader_experience_and_visual_standard.md">Reader Experience and Visual Presentation Standard</a>.</p></section>'''
    _replace_once("website/visual-atlas.html", atlas_boundary_old, atlas_boundary_new)

    p81_old = '''<section class="panel">\n  <h2>P81 projection-event model separation</h2>\n  <a href="../docs/proposition_81_projection_event_model_separation.md"><img src="../docs/figures/p81_projection_event_model_separation.svg" alt="P81 projection-event model separation theorem figure" /></a>\n  <p>Exact projected-event constraints can strengthen the P80 lower bound without changing the declared P75 model.</p>\n</section>'''
    p81_new = '''<section class="figure-card" id="p81">\n  <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p81_projection_event_model_separation.svg" aria-label="Open the full P81 theorem figure"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p81_projection_event_model_separation.svg" alt="P81 projection-event model separation theorem figure" /></a>\n  <div><p class="eyebrow">P81</p><h2>Projection-event model separation</h2><p>Exact projected-event constraints can strengthen the P80 lower bound without changing the declared P75 model. Read the figure together with the theorem to see how event mismatch is transferred back to a certified full-law distance.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_81_projection_event_model_separation.md">Open the P81 proof</a></div>\n</section>'''
    _replace_once("website/visual-atlas.html", p81_old, p81_new)
    atlas = _read("website/visual-atlas.html")
    atlas = re.sub(r'<img(?![^>]*\bloading=)', '<img loading="lazy" decoding="async"', atlas)
    _write("website/visual-atlas.html", atlas)

    # Implementation page: explain how a first reader should traverse the code/proof surface.
    implementation_marker = '<section class="boundary">\n'
    implementation_intro = '''<section id="implementation-reading-key">\n  <div class="section-head"><p class="eyebrow">First-reader key</p><h2>Read each implementation stage in the same four-part order</h2><p>You do not need to begin with source code. Start with the scientific question, then inspect the formal object, the executable routine, and finally the verification record.</p></div>\n  <div class="reader-step-grid">\n    <article class="reader-step-card"><span>1</span><strong>Scientific question</strong><p>What failure mode is this stage trying to detect, prevent, or quantify?</p></article>\n    <article class="reader-step-card"><span>2</span><strong>Formal object</strong><p>Which declared variables, assumptions, theorem, or optimization problem is being implemented?</p></article>\n    <article class="reader-step-card"><span>3</span><strong>Executable routine</strong><p>Which source module computes the certificate, bound, reconstruction, or decision rule?</p></article>\n    <article class="reader-step-card"><span>4</span><strong>Verification</strong><p>Which tests, proof record, provenance file, and reproducibility check protect the result?</p></article>\n  </div>\n</section>\n\n'''
    implementation = _read("website/implementation.html")
    if "Read each implementation stage in the same four-part order" not in implementation:
        if implementation_marker not in implementation:
            raise RuntimeError("implementation boundary marker not found")
        _write("website/implementation.html", implementation.replace(implementation_marker, implementation_intro + implementation_marker, 1))

    # Documentation: make visual sizing and reader expectations explicit.
    figure_marker = "The embedded description matters because figures are often opened directly, reused outside the README, viewed with assistive technology, or encountered through the visual atlas rather than through the paragraph that originally introduced them.\n\n---\n\n## Visual layout and connector standard"
    figure_insert = """The embedded description matters because figures are often opened directly, reused outside the README, viewed with assistive technology, or encountered through the visual atlas rather than through the paragraph that originally introduced them.\n\n## Display-size standard\n\nReader-facing figures must be sized for inspection rather than spectacle. The website uses three display classes: theorem/architecture figures at a preferred reading width of roughly 760 to 980 CSS pixels, figure-and-text cards with a typical figure area of roughly 520 to 720 CSS pixels, and simple atlas thumbnails around 205 to 250 CSS pixels high. On smaller screens, figures use the available width while preserving aspect ratio.\n\nNo theorem figure should normally consume more than about 72 percent of the viewport height when the surrounding explanation can remain visible. Full-resolution SVGs remain directly available from the figure link. If a figure becomes unreadable at these sizes, the correct fix is to rewrap labels, simplify the composition, or split the visual into panels. Shrinking text until it technically fits is not an acceptable layout repair.\n\nAll web figure containers must preserve the complete image with containment rather than cropping. Complex theorem figures should use the wider theorem presentation instead of being forced into a thumbnail slot. These display rules are mirrored in the [Reader Experience and Visual Presentation Standard](reader_experience_and_visual_standard.md).\n\n---\n\n## Visual layout and connector standard"""
    _replace_once("docs/figure_caption_and_description_standard.md", figure_marker, figure_insert)

    detail_marker = "The scientific status rule is strict throughout: a theorem is only a theorem under its declared assumptions, an implementation is not empirical evidence, a simulation is not an ontological result, and the physical-to-experiential bridge remains open unless separately established.\n"
    detail_insert = detail_marker + "\n### How to use this record\n\nA first-time reader should not read this page as 84 disconnected proofs. Use it as an audit index: identify the scientific role of a proposition, open its direct proof when needed, then follow implementation/tests/provenance links for verification. For the shortest conceptual path, begin with [Start Here](../START_HERE.md) and [Research Navigation](research_navigation.md). The [Reader Experience and Visual Presentation Standard](reader_experience_and_visual_standard.md) explains the repository-wide explanation and visual hierarchy.\n"
    _replace_once("docs/detailed_proposition_record.md", detail_marker, detail_insert)

    _replace_once(
        "docs/research_navigation.md",
        "**First-time reader:** begin with [Start Here](../START_HERE.md) for the shortest orientation, keep the [Glossary and Reader Vocabulary](glossary.md) nearby for terminology, and use the [Reproducibility Guide](reproducibility.md) when you want to run the code, tests, or generated figure atlases.",
        "**First-time reader:** begin with [Start Here](../START_HERE.md) for the shortest orientation, keep the [Glossary and Reader Vocabulary](glossary.md) nearby for terminology, use the [Reader Experience and Visual Presentation Standard](reader_experience_and_visual_standard.md) to understand how the public record is organized, and use the [Reproducibility Guide](reproducibility.md) when you want to run the code, tests, or generated figure atlases.",
    )

    start_marker = "The repository therefore makes a deliberate distinction between **mathematical correctness**, **empirical adequacy**, and **experiential interpretation**. They are not interchangeable.\n"
    start_insert = start_marker + """\n---\n\n## A ten-minute first read\n\nIf you want the shortest coherent path before opening proofs:\n\n1. Read the central question and project-in-one-picture above.\n2. Read the six recurring terms on the public [Start Here page](website/start-here.html#reader-primer), or keep the [Glossary](docs/glossary.md) open.\n3. Read P19 in plain language as the core sufficiency question.\n4. Read P71-P76 as target integrity and model-adequacy safeguards.\n5. Read P77-P84 as the progression from finite-data model-set separation to exact shared-parameter parity incompatibility.\n6. Finish with the scientific boundaries: rejection of a declared model is not an ontological conclusion about consciousness.\n\nFor the presentation rules used across the website and documentation, see the [Reader Experience and Visual Presentation Standard](docs/reader_experience_and_visual_standard.md).\n"""
    _replace_once("START_HERE.md", start_marker, start_insert)

    _replace_once(
        "START_HERE.md",
        "- **All curated visuals:** [Figure Catalog](docs/figure_catalog.md)\n",
        "- **All curated visuals:** [Figure Catalog](docs/figure_catalog.md)\n- **Reader and visual presentation standard:** [Reader Experience and Visual Presentation Standard](docs/reader_experience_and_visual_standard.md)\n",
    )

    readme_marker = "> **Visual reading standard.** Every reader-facing figure now has a clear title, an embedded SVG description, a nearby caption or atlas explanation, a scientific-status boundary, and a direct route to the proof or source context. Use the [Complete Figure Catalog](docs/figure_catalog.md) to understand every visual without searching the repository, and the [Figure Caption and Description Standard](docs/figure_caption_and_description_standard.md) for the enforced documentation rules.\n"
    readme_insert = readme_marker + "\n> **Reader experience standard.** The public record uses progressive disclosure: plain-language question, formal result, audit trail, and interpretation boundary. Figure sizes are capped for readability rather than page dominance, and complex theorem graphics always retain a full-resolution route. See the [Reader Experience and Visual Presentation Standard](docs/reader_experience_and_visual_standard.md).\n"
    _replace_once("README.md", readme_marker, readme_insert)


if __name__ == "__main__":
    main()
