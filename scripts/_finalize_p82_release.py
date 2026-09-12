"""One-time release helper for the P82 / v0.82.0 publication candidate."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_all(path: str, replacements: tuple[tuple[str, str], ...]) -> None:
    text = read(path)
    for old, new in replacements:
        text = text.replace(old, new)
    write(path, text)


def update_release_metadata() -> None:
    replace_all(
        "pyproject.toml",
        (
            ('version = "0.81.0"', 'version = "0.82.0"'),
            (
                "projection-event model-distance certification, exact-rational marginal and cylinder-event box bounds,",
                "projection-event model-distance certification, exact-rational marginal and cylinder-event box bounds, exact nested projection-contrast certification, exact residual-event box bounds,",
            ),
        ),
    )
    replace_all(
        "README.md",
        (
            ("version-0.81.0-2563eb", "version-0.82.0-2563eb"),
            ("v0.81.0", "v0.82.0"),
        ),
    )
    replace_all("START_HERE.md", (("v0.81.0", "v0.82.0"), ("0.81.0", "0.82.0")))

    cff = read("CITATION.cff")
    cff = cff.replace("version: 0.81.0", "version: 0.82.0")
    cff = cff.replace("date-released: 2026-09-11", "date-released: 2026-09-12")
    cff = cff.replace("Version 0.81.0", "Version 0.82.0")
    write("CITATION.cff", cff)

    bib = read("CITATION.bib")
    bib = bib.replace("version      = {0.81.0}", "version      = {0.82.0}")
    bib = re.sub(
        r"note\s*=\s*\{[^\n]*\}",
        "note         = {Ongoing research program. Current documented theorem frontier: P82.}",
        bib,
        count=1,
    )
    write("CITATION.bib", bib)

    citation = read("CITATION.md")
    citation = citation.replace("0.81.0", "0.82.0")
    citation = citation.replace("Current documented theorem frontier: P81", "Current documented theorem frontier: P82")
    citation = citation.replace("theorem frontier **P81**", "theorem frontier **P82**")
    citation = citation.replace("P1 through P81", "P1 through P82")
    citation = citation.replace("None of P78-P81", "None of P78-P82")
    p81_sentence = (
        "Cite [Proposition 81](docs/proposition_81_projection_event_model_separation.md) when relying on exact projected-event parameter-box intervals, the event-size transfer to full-law L-infinity distance, the P81 never-weaker-than-P80 certificate, or its strict-improvement witness."
    )
    p82_sentence = (
        " Cite [Proposition 82](docs/proposition_82_exact_nested_projection_contrast.md) when relying on exact nested residual-event parameter-box intervals, the 256-contrast audit, the P82 never-weaker-than-P81 certificate, the direct residual extremization theorem, or the exact 1/12 versus 1/16 strict-improvement witness."
    )
    if p81_sentence in citation and p82_sentence.strip() not in citation:
        citation = citation.replace(p81_sentence, p81_sentence + p82_sentence, 1)
    p81_scope = (
        "P81 further tightens the declared continuous-family test by retaining exact parameter-box ranges for every nonempty projected binary event. Event-level mismatch is divided by the number of full observed cells in that event to obtain a sound full-law L-infinity lower bound. The combined P81 certificate is never weaker than P80 and can be strictly stronger. None of P78-P82 turns non-rejection into model validation or identifies the latent state with consciousness."
    )
    p82_scope = (
        "\n\nP82 strengthens that chain again by retaining exact common-parameter structure for residual events formed from nested projected cylinders. It computes each residual interval directly from the P75 branchwise factorization rather than by subtracting separate P81 event intervals, audits 256 genuinely new residual events, and preserves the one-sided model-rejection interpretation. Its exact witness gives P80 = 0, P81 = 1/16, and P82 = 1/12. This is a stronger certificate against the declared P75 family, not evidence that its latent variable is consciousness."
    )
    if p81_scope in citation and p82_scope.strip() not in citation:
        citation = citation.replace(p81_scope, p81_scope + p82_scope, 1)
    if "## Proposition 82" not in citation:
        marker = "## P82 frontier citation note"
        section = (
            "## Proposition 82\n\n"
            "For the exact nested projection-contrast certificate, cite the repository together with "
            "[Proposition 82](docs/proposition_82_exact_nested_projection_contrast.md) and its "
            "[equation provenance record](docs/p82_equation_provenance.md). P82 is a conditional computational "
            "model-distance theorem for the declared P75 family. It should not be cited as an identification of consciousness.\n\n"
        )
        if marker in citation:
            citation = citation.replace(marker, section + marker, 1)
        else:
            citation += "\n" + section
    provenance_marker = (
        "- [P81 equation and provenance record](docs/p81_equation_provenance.md): projected-event box intervals, event-size distance transfer, dominance, and the P79 rejection handoff."
    )
    provenance_p82 = (
        "\n- [P82 equation and provenance record](docs/p82_equation_provenance.md): exact nested residual-event intervals, direct residual extremization, dominance, and the P79 rejection handoff."
    )
    if provenance_marker in citation and provenance_p82.strip() not in citation:
        citation = citation.replace(provenance_marker, provenance_marker + provenance_p82, 1)
    citation = citation.replace(
        "The current citation metadata identify Version **0.82.0** and theorem frontier **P81**.",
        "The current citation metadata identify Version **0.82.0** and theorem frontier **P82**.",
    )
    write("CITATION.md", citation)

    changelog = read("CHANGELOG.md")
    changelog = changelog.replace(
        "## Unreleased - P82 exact nested projection-contrast certificate",
        "## 0.82.0 - 2026-09-12 - P82 exact nested projection-contrast certificate",
    )
    write("CHANGELOG.md", changelog)


def update_deterministic_artifacts() -> None:
    for path in (
        "scripts/generate_quantitative_atlas.py",
        "scripts/generate_quantum_foundations_atlas.py",
    ):
        replace_all(path, (("v0.81.0", "v0.82.0"),))

    verifier = read("scripts/verify_repository.py")
    verifier = verifier.replace('CURRENT_VERSION = "0.81.0"', 'CURRENT_VERSION = "0.82.0"')
    verifier = verifier.replace('CURRENT_FRONTIER = "P81"', 'CURRENT_FRONTIER = "P82"')
    verifier = verifier.replace("for number in range(1, 82):", "for number in range(1, 83):")
    write("scripts/verify_repository.py", verifier)


def update_website() -> None:
    for path in ("website/index.html", "website/start-here.html"):
        replace_all(path, (("v0.81.0", "v0.82.0"), ("Version 0.81.0", "Version 0.82.0")))

    research_map = read("website/research-map.html")
    research_map = research_map.replace(
        "Scientific dependency map of the Mathematical Consciousness Bridge through Proposition 80.",
        "Scientific dependency map of the Mathematical Consciousness Bridge through Proposition 82.",
    )
    research_map = research_map.replace(
        "Eighty results, one dependency-aware scientific program",
        "Eighty-two results, one dependency-aware scientific program",
    )
    research_map = research_map.replace(
        "<strong>80</strong><span>proposition-level results</span>",
        "<strong>82</strong><span>proposition-level results</span>",
    )
    old_lede = (
        "P71-P82 return to the P19 bridge-sufficiency lineage after the P61-P70 calibration branch: P71 protects target provenance, P72 protects the target-observation interface, P73 identifies target channels under one explicit latent model, P74 certifies finite-data recovery, P75 introduces independent model-adequacy restrictions, P76 turns those restrictions into finite-sample rejection tests, P77 lifts rejection to the complete declared model set, P78 certifies continuous-family distance lower bounds, P79 certifies the sampling-radius upper bound, and P80 tightens the continuous lower bound by enforcing probability normalization inside each parameter-box relaxation."
    )
    new_lede = (
        "P71-P82 return to the P19 bridge-sufficiency lineage after the P61-P70 calibration branch: P71 protects target provenance, P72 protects the target-observation interface, P73 identifies target channels under one explicit latent model, P74 certifies finite-data recovery, P75 introduces independent model-adequacy restrictions, P76 turns those restrictions into finite-sample rejection tests, P77 lifts rejection to the complete declared model set, P78 certifies continuous-family distance lower bounds, P79 certifies the sampling-radius upper bound, P80 adds probability-simplex coupling, P81 adds exact projected-event constraints, and P82 adds exact nested residual-event constraints that preserve common-parameter structure beyond separate event tests."
    )
    research_map = research_map.replace(old_lede, new_lede)
    if 'id="continuous-model-frontier"' not in research_map:
        marker = "</main>"
        frontier = """
<section id="continuous-model-frontier">
  <div class="section-head">
    <p class="eyebrow">Current continuous-model frontier</p>
    <h2>P77-P82: from full-law rejection to exact nested-contrast certification</h2>
    <p>Read this sequence in order. Each proposition closes one specific gap in the same declared four-view target-measurement model. The direction is deliberately one-sided: these results can certify incompatibility with the model, but non-rejection is not model validation and no latent state is identified with consciousness.</p>
  </div>
  <div class="result-grid">
    <article class="result"><span>P77</span><h3>Full-law decision rule</h3><p>Reject only when the finite-sample confidence region is certified disjoint from the complete declared model family.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_77_full_law_model_set_separation.md">Open P77 →</a></article>
    <article class="result"><span>P78</span><h3>Continuous-family lower bound</h3><p>Use exact-rational parameter-box enclosures and branch-and-bound to certify a global lower bound on model distance.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_78_certified_continuous_model_separation.md">Open P78 →</a></article>
    <article class="result"><span>P79</span><h3>Certified sampling radius</h3><p>Upper-bound the finite-sample radius with exact-rational one-sided numerical enclosures so the final comparison has the correct direction.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_79_certified_sampling_radius.md">Open P79 →</a></article>
    <article class="result"><span>P80</span><h3>Simplex coupling</h3><p>Intersect exact cell intervals with probability normalization to obtain a never-weaker box certificate.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_80_simplex_coupled_model_separation.md">Open P80 →</a></article>
    <article class="result"><span>P81</span><h3>Projected-event constraints</h3><p>Use exact ranges of all 80 nonempty cylinder events and transfer event mismatch into full-law distance.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_81_projection_event_model_separation.md">Open P81 →</a></article>
    <article class="result"><span>P82</span><h3>Exact nested residual contrasts</h3><p>Use exact ranges of 256 genuinely new residual events from nested cylinders. The concrete exact witness improves the lower bound from P81 = 1/16 to P82 = 1/12.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_82_exact_nested_projection_contrast.md">Open P82 →</a></article>
  </div>
  <div class="hero-actions">
    <a class="button primary" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p82_equation_provenance.md">Audit P82 equation provenance</a>
    <a class="button" href="visual-atlas.html">See the P82 theorem figure</a>
    <a class="button" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/nested_projection_contrast_separation.py">Open implementation</a>
    <a class="button" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_nested_projection_contrast_separation.py">Open tests</a>
  </div>
</section>
"""
        if marker not in research_map:
            raise RuntimeError("research-map closing main marker missing")
        research_map = research_map.replace(marker, frontier + marker, 1)
    write("website/research-map.html", research_map)

    atlas = read("website/visual-atlas.html")
    if "p82_exact_nested_projection_contrast.svg" not in atlas:
        marker = '<section class="boundary"><h2>Figure reading rule</h2>'
        p82 = """
<section id="p82-frontier">
  <div class="section-head">
    <p class="eyebrow">Current theorem frontier · P82</p>
    <h2>Exact nested projection-contrast certificate</h2>
    <p>This figure is the visual entry point to the current theorem frontier. It shows the nested parent-child event geometry, the exact branchwise residual factorization, the finite 256-contrast audit, and the strict exact-rational improvement over P81.</p>
  </div>
  <div class="figure-card">
    <img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p82_exact_nested_projection_contrast.svg" alt="P82 exact nested projection-contrast certificate" />
    <div>
      <h3>P82: exact nested residual-event certification</h3>
      <p>For a parent cylinder A and nested child B, P82 evaluates the residual A\\B directly from the P75 branchwise factorization. The exact witness gives P80 = 0, P81 = 1/16, and P82 = 1/12. The result strengthens model rejection only; it does not identify the latent state with consciousness.</p>
      <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_82_exact_nested_projection_contrast.md">Read theorem and proof →</a></p>
      <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p82_equation_provenance.md">Audit equation provenance →</a></p>
      <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/nested_projection_contrast_separation.py">Open exact-rational implementation →</a></p>
      <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_nested_projection_contrast_separation.py">Open regression and strict-witness tests →</a></p>
    </div>
  </div>
</section>
"""
        if marker not in atlas:
            raise RuntimeError("visual-atlas reading-rule marker missing")
        atlas = atlas.replace(marker, p82 + marker, 1)
    write("website/visual-atlas.html", atlas)


def main() -> None:
    update_release_metadata()
    update_deterministic_artifacts()
    update_website()
    print("P82 / v0.82.0 release surfaces finalized")


if __name__ == "__main__":
    main()
