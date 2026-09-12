from pathlib import Path
import re


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    Path(path).write_text(text, encoding="utf-8")


def replace_section(text: str, section_id: str, replacement: str) -> str:
    start_token = f'<section id="{section_id}"'
    start = text.find(start_token)
    if start < 0:
        raise RuntimeError(f"missing section {section_id}")
    end = text.find("</section>", start)
    if end < 0:
        raise RuntimeError(f"unclosed section {section_id}")
    end += len("</section>")
    return text[:start] + replacement.strip() + text[end:]


# Responsive image protection and theorem-frontier layout.
path = "website/styles.css"
css = read(path)
marker = "/* Publication-safe theorem figures */"
if marker not in css:
    css += r'''

/* Publication-safe theorem figures */
img {
  max-width: 100%;
  height: auto;
}

.two-col > *,
.figure-card > * {
  min-width: 0;
}

.two-col img,
.figure-card img {
  display: block;
  width: 100%;
  max-width: 100%;
  height: auto;
}

.theorem-frontier {
  scroll-margin-top: 92px;
}

.theorem-frontier .section-head {
  max-width: 900px;
}

.theorem-figure-shell {
  width: 100%;
  margin-top: 26px;
  padding: 16px;
  overflow: hidden;
  border: 1px solid var(--line);
  border-radius: 18px;
  background: var(--paper);
}

.theorem-figure-shell a {
  display: block;
  min-width: 0;
}

.theorem-figure-shell img {
  display: block;
  width: 100%;
  max-width: 100%;
  height: auto;
  margin: 0 auto;
  border-radius: 12px;
  background: #ffffff;
}

.frontier-summary-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 14px;
  margin-top: 18px;
}

.frontier-summary-card {
  min-width: 0;
  padding: 19px 20px;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--paper);
}

.frontier-summary-card h3 {
  margin: 0 0 0.45em;
  font-size: 1rem;
  line-height: 1.35;
}

.frontier-summary-card p {
  margin-bottom: 0.7em;
  color: var(--muted);
  font-size: 0.9rem;
  line-height: 1.62;
}

.frontier-summary-card p:last-child {
  margin-bottom: 0;
}

.frontier-metrics {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 12px;
}

.frontier-metrics span {
  display: inline-block;
  padding: 5px 8px;
  border-radius: 7px;
  background: var(--soft);
  color: var(--accent);
  font-size: 0.77rem;
  font-weight: 700;
  line-height: 1.35;
}

.frontier-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 18px;
}

@media (max-width: 900px) {
  .frontier-summary-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 680px) {
  .theorem-figure-shell {
    padding: 8px;
    border-radius: 13px;
  }

  .frontier-summary-card {
    padding: 17px;
  }
}
'''
write(path, css)


# Homepage: figure first, explanation below, never overlapping.
path = "website/index.html"
html = read(path)
new_home = r'''
<section id="p84-frontier" class="theorem-frontier">
  <div class="section-head">
    <p class="eyebrow">Current theorem frontier · P84</p>
    <h2>P84 in plain language: two tests can pass separately and still fail together</h2>
    <p>P83 checks parity observables one at a time. P84 asks the stronger question: can two of those observations be produced at the same time by one shared P75 parameter assignment? The answer can be no even when both individual checks pass.</p>
  </div>

  <div class="theorem-figure-shell">
    <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p84_exact_joint_projection_parity_contrast.svg" aria-label="Open the full P84 theorem figure">
      <img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p84_exact_joint_projection_parity_contrast.svg?v=2" alt="P84 joint parity compatibility certificate: separate P83 compatibility can fail under one shared P75 parameter assignment" />
    </a>
  </div>

  <div class="frontier-summary-grid">
    <article class="frontier-summary-card">
      <h3>What P84 is testing</h3>
      <p>Imagine two measurements that each look possible when checked separately. P84 keeps their shared model parameters tied together and asks whether one parameter choice can explain both simultaneously.</p>
      <p>This closes a specific gap left by P83: separate interval compatibility is weaker than joint shared-parameter compatibility.</p>
    </article>

    <article class="frontier-summary-card">
      <h3>What was proved</h3>
      <p>The standard P84 audit contains 220 exact coupled parity-event contrasts. For the strict exact-rational witness, every P83 check remains compatible while one P84 joint contrast does not.</p>
      <div class="frontier-metrics" aria-label="P84 key results">
        <span>220 coupled contrasts</span>
        <span>L83 = 0</span>
        <span>L84 = 1/32</span>
        <span>Exact rational arithmetic</span>
      </div>
    </article>

    <article class="frontier-summary-card">
      <h3>What this does not mean</h3>
      <p>P84 is a stronger rejection certificate for the declared P75 latent measurement model under its stated assumptions.</p>
      <p>It does not identify the latent variable with consciousness, does not prove consciousness is nonphysical, and does not close the physical-to-experiential bridge.</p>
    </article>
  </div>

  <div class="frontier-actions">
    <a class="button primary" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_84_exact_projection_parity_contrast.md">Read Proposition 84</a>
    <a class="button" href="implementation.html#stage-06">See the implementation</a>
    <a class="button" href="visual-atlas.html#p84-frontier">Open in the Visual Atlas</a>
  </div>
</section>'''
html = replace_section(html, "p84-frontier", new_home)
write(path, html)


# Visual Atlas: same hierarchy and reading order.
path = "website/visual-atlas.html"
atlas = read(path)
new_atlas = r'''
<section id="p84-frontier" class="theorem-frontier">
  <div class="section-head">
    <p class="eyebrow">Current theorem frontier · P84</p>
    <h2>Joint parity compatibility under one shared parameter assignment</h2>
    <p>Read this figure from left to right: first keep two P83 parity observables coupled, then compute their exact common-parameter contrast range, then compare the empirical contrast with that range.</p>
  </div>
  <div class="theorem-figure-shell">
    <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p84_exact_joint_projection_parity_contrast.svg" aria-label="Open the full P84 theorem figure">
      <img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p84_exact_joint_projection_parity_contrast.svg?v=2" alt="P84 exact joint projection-parity contrast certificate" />
    </a>
  </div>
  <div class="frontier-summary-grid">
    <article class="frontier-summary-card"><h3>Read the left panel</h3><p>P83 can accept two parity events separately. P84 refuses to optimize them independently when they share underlying P75 response parameters.</p></article>
    <article class="frontier-summary-card"><h3>Read the middle panel</h3><p>The joint contrast is multi-affine, so its exact box extrema occur at common endpoint vertices. The implementation uses exact rational arithmetic rather than a floating-point local optimizer.</p></article>
    <article class="frontier-summary-card"><h3>Read the right panel</h3><p>The strict witness has L83 = 0 but L84 = 1/32. This is a model-family separation result, not an experiential identification claim.</p></article>
  </div>
  <div class="frontier-actions"><a class="button primary" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_84_exact_projection_parity_contrast.md">Open the P84 theorem</a></div>
</section>'''
atlas = replace_section(atlas, "p84-frontier", new_atlas)
atlas = atlas.replace("This figure is the visual entry point to the current theorem frontier.", "This figure records an earlier step in the theorem frontier.")
write(path, atlas)


# Implementation page: Stage 06 now states the whole P73-P84 chain.
path = "website/implementation.html"
impl = read(path)
impl = impl.replace("<strong>6 · P73-P76</strong>Channel recovery & adequacy", "<strong>6 · P73-P84</strong>Channel recovery, adequacy & certified separation")
impl = impl.replace("Stage 06 · P73-P76", "Stage 06 · P73-P84")
impl = impl.replace("P73-P76 separate four questions that are easy to conflate:", "P73-P84 build a continuous chain from channel recovery to certified model-family separation. P73-P76 separate four questions that are easy to conflate:")
impl = impl.replace("Three- or four-view binary observations and a declared latent conditional-independence model.", "Three- or four-view binary observations, a declared latent conditional-independence model, and the parameter boxes used for certified full-law separation.")
impl = impl.replace("Recover moments/channel parameters, apply nondegeneracy gates, reconstruct the observed law, and test adequacy constraints with finite-sample intervals.", "Recover channel parameters, test model adequacy, certify full-law distance, and progressively retain simplex, projection, nested-event, parity, and joint shared-parameter constraints.")
write(path, impl)


# P84 proof: add an accessible interpretation before formal details.
path = "docs/proposition_84_exact_projection_parity_contrast.md"
prop = read(path)
if "## Plain-language meaning" not in prop:
    anchor = "P84 is a model-distance certification result. It does not establish that the P75 latent state is consciousness, does not validate the P75 model when rejection fails, and does not close the physical-to-experiential bridge.\n\n---"
    block = """P84 is a model-distance certification result. It does not establish that the P75 latent state is consciousness, does not validate the P75 model when rejection fails, and does not close the physical-to-experiential bridge.\n\n## Plain-language meaning\n\nP83 asks whether each parity-based observation is individually compatible with a parameter box. P84 asks a stricter question: **can the same parameter choice explain two such observations at once?**\n\nThis matters because separate tests can hide a contradiction. One observation may be explainable by one point in the parameter box and a second observation by another point, even though no single point explains both together. P84 keeps the shared parameters coupled and tests that joint requirement directly.\n\nThe strict witness makes the difference concrete: the complete P83 certificate is zero, while P84 certifies the positive lower bound `1/32`. The conclusion is narrow and precise: the declared P75 model family is farther from the empirical law than P83 alone can prove on that box.\n\n---"""
    if anchor not in prop:
        raise RuntimeError("P84 proposition insertion anchor missing")
    prop = prop.replace(anchor, block, 1)
write(path, prop)


# Roadmap and navigation: explain the new theorem before technical details.
path = "docs/theorem_roadmap.md"
roadmap = read(path)
frontier_heading = "## P84 frontier: exact joint projection-parity contrast separation\n\n"
if frontier_heading in roadmap and "**Plain-language interpretation.**" not in roadmap[roadmap.find(frontier_heading):]:
    roadmap = roadmap.replace(frontier_heading, frontier_heading + "**Plain-language interpretation.** P83 can say that two observations are each possible somewhere inside the same parameter box. P84 asks whether they are possible **together at one common parameter choice**. Its strict witness shows that these are not equivalent requirements.\n\n", 1)
write(path, roadmap)

path = "docs/research_navigation.md"
nav = read(path)
nav = nav.replace("for the 220 coupled parity-event contrasts, common-vertex exact box intervals, P84 >= P83 dominance, and the strict `1/32` versus zero witness.", "for the stronger shared-parameter question: whether two individually compatible P83 parity observations can be realized simultaneously. It covers 220 exact coupled contrasts, P84 >= P83 dominance, and the strict `L83 = 0 < L84 = 1/32` witness.")
write(path, nav)


# Figure wording: shorter title, same mathematics and panel geometry.
path = "docs/figures/p84_exact_joint_projection_parity_contrast.svg"
svg = read(path)
svg = svg.replace("P84 Exact Joint Projection-Parity Contrast Certificate</text>", "P84 Joint Parity Compatibility Certificate</text>")
svg = svg.replace("Separate parity compatibility does not guarantee joint compatibility with one shared P75 parameter assignment</text>", "Two parity checks can pass separately yet fail under one shared P75 parameter assignment</text>")
svg = svg.replace("P84 exact joint projection-parity contrast certificate</title>", "P84 joint parity compatibility certificate</title>")
write(path, svg)


# Force fresh website assets in browsers.
path = "scripts/prepare_website.py"
prep = read(path)
prep = re.sub(r'ASSET_VERSION = "[^"]+"', 'ASSET_VERSION = "20260912-nav11-p84"', prep, count=1)
write(path, prep)
