"""Repair the P85 reader/publication contract after frontier promotion.

This temporary maintenance helper restores the complete P84 historical figure
presentation, removes stale P84-era counts from first-reader pages, and updates
the repository verifier/tests to enforce the P85 frontier. It is intentionally
idempotent and is removed after the synchronized commit is created.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    if "\u2013" in text or "\u2014" in text:
        raise RuntimeError(f"forbidden en/em dash in {path}")
    target = ROOT / path
    old = target.read_text(encoding="utf-8")
    if old != text:
        target.write_text(text, encoding="utf-8")
        print(f"updated {path}")


P84_HOME = '''<section id="p84-frontier" class="theorem-frontier">
  <div class="section-head">
    <p class="eyebrow">Previous theorem frontier · P84</p>
    <h2>P84 in plain language: two tests can pass separately and still fail together</h2>
    <p>P83 checks parity observables one at a time. P84 asks the stronger question: can two of those observations be produced at the same time by one shared P75 parameter assignment? The answer can be no even when both individual checks pass.</p>
  </div>
  <div class="theorem-figure-shell">
    <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p84_exact_joint_projection_parity_contrast.svg" aria-label="Open the full P84 theorem figure">
      <img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p84_exact_joint_projection_parity_contrast.svg?v=3" alt="P84 joint parity compatibility certificate: separate P83 compatibility can fail under one shared P75 parameter assignment" />
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
</section>'''

P84_ATLAS = '''<section id="p84-frontier" class="theorem-frontier">
  <div class="section-head">
    <p class="eyebrow">Previous theorem frontier · P84</p>
    <h2>Joint parity compatibility under one shared parameter assignment</h2>
    <p>Read this figure from left to right: first keep two P83 parity observables coupled, then compute their exact common-parameter contrast range, then compare the empirical contrast with that range.</p>
  </div>
  <div class="theorem-figure-shell">
    <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p84_exact_joint_projection_parity_contrast.svg" aria-label="Open the full P84 theorem figure">
      <img loading="lazy" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p84_exact_joint_projection_parity_contrast.svg?v=3" alt="P84 exact joint projection-parity contrast certificate" />
    </a>
  </div>
  <div class="frontier-summary-grid">
    <article class="frontier-summary-card"><h3>Read the left panel</h3><p>P83 can accept two parity events separately. P84 refuses to optimize them independently when they share underlying P75 response parameters.</p></article>
    <article class="frontier-summary-card"><h3>Read the middle panel</h3><p>The joint contrast is multi-affine, so its exact box extrema occur at common endpoint vertices. The implementation uses exact rational arithmetic rather than a floating-point local optimizer.</p></article>
    <article class="frontier-summary-card"><h3>Read the right panel</h3><p>The strict witness has L83 = 0 but L84 = 1/32. This is a model-family separation result, not an experiential identification claim.</p></article>
  </div>
  <div class="frontier-actions"><a class="button" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_84_exact_projection_parity_contrast.md">Open the P84 theorem</a></div>
</section>'''


def restore_p84_history() -> None:
    path = "website/index.html"
    text = read(path)
    pattern = re.compile(r'<section id="p84" class="theorem-frontier">.*?</section>', re.DOTALL)
    if pattern.search(text):
        text = pattern.sub(P84_HOME, text, count=1)
    elif '<section id="p84-frontier" class="theorem-frontier">' not in text:
        raise RuntimeError("homepage P84 historical section not found")
    if text.count('id="p84-frontier"') != 1:
        raise RuntimeError("homepage must contain exactly one P84 historical section")
    write(path, text)

    path = "website/visual-atlas.html"
    text = read(path)
    pattern = re.compile(r'<section id="p84">.*?</section>', re.DOTALL)
    if pattern.search(text):
        text = pattern.sub(P84_ATLAS, text, count=1)
    elif '<section id="p84-frontier" class="theorem-frontier">' not in text:
        raise RuntimeError("atlas P84 historical section not found")
    if text.count('id="p84-frontier"') != 1:
        raise RuntimeError("atlas must contain exactly one P84 historical section")
    write(path, text)


def promote_start_here() -> None:
    path = "website/start-here.html"
    text = read(path)
    replacements = {
        "Open all 84 results": "Open all 85 results",
        "<strong>84</strong><span>proposition-level results</span>": "<strong>85</strong><span>proposition-level results</span>",
        "<strong>P84</strong><span>current theorem frontier</span>": "<strong>P85</strong><span>current theorem frontier</span>",
        "P75-P84": "P75-P85",
        "The 84 propositions by scientific role": "The 85 propositions by scientific role",
        "P78-P84 progressively tighten": "P78-P85 progressively tighten",
        "You do not need to read 84 proofs in order": "You do not need to read 85 proofs in order",
        "complete 84-result dependency structure": "complete 85-result dependency structure",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    old = '<p><strong>P84 now preserves shared-parameter compatibility between pairs of P83 parity events.</strong> Its 220 exact joint contrasts can reject a P75 box even when every individual P83 parity interval is compatible; the strict exact-rational witness has L83 = 0 and L84 = 1/32.</p>'
    new = old + '\n      <p><strong>P85 now tests exact three-event shared-parameter compatibility beyond the complete P84 pairwise certificate.</strong> Its 660 sign-normalized functionals include an exact-rational witness with L84 = 0, empirical value 5/8, exact P75 interval [1,2], centered coefficient norm 12, and L85 = 1/32.</p>'
    if old in text and "P85 now tests exact three-event" not in text:
        text = text.replace(old, new, 1)

    text = text.replace(
        'href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_84_exact_projection_parity_contrast.md">Read P84</a>',
        'href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_85_exact_triple_projection_parity_functional.md">Read P85</a>',
        1,
    )

    required = (
        "Open all 85 results",
        "<strong>85</strong><span>proposition-level results</span>",
        "<strong>P85</strong><span>current theorem frontier</span>",
        "The 85 propositions by scientific role",
        "P75-P85",
        "P78-P85 progressively tighten",
        "P85 now tests exact three-event",
        "physical-to-experiential bridge",
    )
    for token in required:
        if token not in text:
            raise RuntimeError(f"start-here missing {token!r}")
    stale = (
        "Open all 84 results",
        "The 84 propositions by scientific role",
        "P78-P84 progressively tighten",
        "<strong>P84</strong><span>current theorem frontier</span>",
    )
    for token in stale:
        if token in text:
            raise RuntimeError(f"start-here still contains stale token {token!r}")
    write(path, text)


def promote_research_map() -> None:
    path = "website/research-map.html"
    text = read(path)
    replacements = {
        "through Proposition 84": "through Proposition 85",
        "Eighty-four results": "Eighty-five results",
        "<strong>84</strong><span>proposition-level results</span>": "<strong>85</strong><span>proposition-level results</span>",
        "P73-P84": "P73-P85",
        "P77-P84": "P77-P85",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    old = "and P84 tests whether pairs of those parity observations remain jointly compatible under one shared P75 parameter assignment."
    new = "and P84 tests whether pairs of those parity observations remain jointly compatible under one shared P75 parameter assignment, while P85 tests exact three-event shared-parameter parity functionals beyond that complete pairwise certificate."
    if old in text:
        text = text.replace(old, new, 1)

    text = text.replace(
        "culminating in P84 shared-parameter parity compatibility.",
        "culminating in P85 exact three-event shared-parameter parity-functional separation.",
    )

    required = (
        "through Proposition 85",
        "Eighty-five results",
        "<strong>85</strong><span>proposition-level results</span>",
        "P73-P85",
        "P85 tests exact three-event shared-parameter parity functionals",
        "physical-to-experiential bridge remains open",
    )
    for token in required:
        if token not in text:
            raise RuntimeError(f"research-map missing {token!r}")
    stale = (
        "through Proposition 84",
        "Eighty-four results",
        "<strong>84</strong><span>proposition-level results</span>",
        "P73-P84",
    )
    for token in stale:
        if token in text:
            raise RuntimeError(f"research-map still contains stale token {token!r}")
    write(path, text)


def update_verifier() -> None:
    path = "scripts/verify_repository.py"
    text = read(path)
    text = text.replace('CURRENT_FRONTIER = "P84"', 'CURRENT_FRONTIER = "P85"')
    text = text.replace(
        '    "docs/proposition_84_exact_projection_parity_contrast.md",\n',
        '    "docs/proposition_84_exact_projection_parity_contrast.md",\n'
        '    "docs/proposition_85_exact_triple_projection_parity_functional.md",\n'
        '    "docs/p85_equation_provenance.md",\n',
        1,
    )
    text = text.replace("for number in range(1, 85):", "for number in range(1, 86):")
    text = text.replace(
        '        "Eighty-three results",\n',
        '        "Eighty-three results",\n'
        '        "current P84 frontier",\n'
        '        "through Proposition 84",\n'
        '        "Eighty-four results",\n',
        1,
    )
    p85_core = (
        '    "docs/proposition_85_exact_triple_projection_parity_functional.md",\n'
        '    "docs/p85_equation_provenance.md",\n'
    )
    while p85_core + p85_core in text:
        text = text.replace(p85_core + p85_core, p85_core)
    p84_stale = (
        '        "current P84 frontier",\n'
        '        "through Proposition 84",\n'
        '        "Eighty-four results",\n'
    )
    while p84_stale + p84_stale in text:
        text = text.replace(p84_stale + p84_stale, p84_stale)
    if 'CURRENT_FRONTIER = "P85"' not in text or "range(1, 86)" not in text:
        raise RuntimeError("verifier frontier promotion failed")
    write(path, text)


def update_reader_test() -> None:
    path = "tests/test_reader_experience.py"
    text = read(path)
    replacements = {
        "test_first_reader_surfaces_match_p84_frontier": "test_first_reader_surfaces_match_p85_frontier",
        '"The 84 propositions by scientific role"': '"The 85 propositions by scientific role"',
        '"You do not need to read 84 proofs in order"': '"You do not need to read 85 proofs in order"',
        '"complete 84-result dependency structure"': '"complete 85-result dependency structure"',
        '"through Proposition 84"': '"through Proposition 85"',
        '"Eighty-four results"': '"Eighty-five results"',
        '"<strong>84</strong>"': '"<strong>85</strong>"',
        '"P73-P84"': '"P73-P85"',
        "test_repository_verifier_tracks_p84_and_all_84_propositions": "test_repository_verifier_tracks_p85_and_all_85_propositions",
        "'CURRENT_FRONTIER = \"P84\"'": "'CURRENT_FRONTIER = \"P85\"'",
        '"for number in range(1, 85):"': '"for number in range(1, 86):"',
        "'\"docs/proposition_84_exact_projection_parity_contrast.md\"'": "'\"docs/proposition_85_exact_triple_projection_parity_functional.md\"'",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    for token in (
        "test_first_reader_surfaces_match_p85_frontier",
        "The 85 propositions by scientific role",
        "through Proposition 85",
        'CURRENT_FRONTIER = "P85"',
        "range(1, 86)",
        "proposition_85_exact_triple_projection_parity_functional.md",
    ):
        if token not in text:
            raise RuntimeError(f"reader test missing {token!r}")
    write(path, text)


def main() -> None:
    restore_p84_history()
    promote_start_here()
    promote_research_map()
    update_verifier()
    update_reader_test()
    print("P85 reader contract repaired")


if __name__ == "__main__":
    main()
