"""One-shot cleanup after the P83 publication integration.

This script repairs historical attribution in the website reader guide, normalizes
the recommended reading order, and restores the missing v0.82.0 archival release
record. It is removed by the branch-only workflow after successful application.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def save(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, *, path: str) -> str:
    if old not in text:
        raise RuntimeError(f"required cleanup anchor missing in {path}: {old[:120]!r}")
    return text.replace(old, new, 1)


def repair_website_start_here() -> None:
    path = "website/start-here.html"
    text = load(path)
    bad = """    <section class="dark-section">
      <p class="eyebrow">Current theorem frontier</p>
      <h2>P83 strengthens full-law model separation without adding a consciousness assumption</h2>
      <p>P78 introduced exact-rational branch-and-bound for the continuous P75 model family. P80 enforced probability normalization, and P81 added exact constraints for every nonempty projected cylinder event. P83 now adds exact residual-event constraints from nested parent-child cylinders. Because the parent and newly fixed views use disjoint response coordinates inside each P75 latent branch, the P83 residual interval is computed exactly rather than by subtracting two separate P81 intervals.</p>
      <p>The logical direction remains one-sided: P83 can strengthen rejection of the declared target-measurement model. Its 256 new contrasts include a strict exact-rational witness with P80 = 0, P81 = 1/16, and P83 = 1/12. It does not identify the latent state with consciousness and does not close the physical-to-experiential bridge.</p>
      <div class="hero-actions">
        <a class="button primary" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_83_exact_nested_projection_contrast.md">Read P83</a>
        <a class="button" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p83_equation_provenance.md">P83 provenance</a>
        <a class="button" href="visual-atlas.html">See theorem visuals</a>
      </div>
    </section>"""
    good = """    <section class="dark-section">
      <p class="eyebrow">Previous certified frontier</p>
      <h2>P82 strengthens full-law model separation with exact nested projection contrasts</h2>
      <p>P78 introduced exact-rational branch-and-bound for the continuous P75 model family. P80 enforced probability normalization, and P81 added exact constraints for every nonempty projected cylinder event. P82 then added exact residual-event constraints from nested parent-child cylinders. Because the parent and newly fixed views use disjoint response coordinates inside each P75 latent branch, the P82 residual interval is computed exactly rather than by subtracting two separate P81 intervals.</p>
      <p>The logical direction remains one-sided: P82 can strengthen rejection of the declared target-measurement model. Its 256 new contrasts include a strict exact-rational witness with P80 = 0, P81 = 1/16, and P82 = 1/12. It does not identify the latent state with consciousness and does not close the physical-to-experiential bridge.</p>
      <div class="hero-actions">
        <a class="button primary" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_82_exact_nested_projection_contrast.md">Read P82</a>
        <a class="button" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p82_equation_provenance.md">P82 provenance</a>
        <a class="button" href="visual-atlas.html">See theorem visuals</a>
      </div>
    </section>"""
    text = replace_once(text, bad, good, path=path)
    save(path, text)


def normalize_research_navigation() -> None:
    path = "docs/research_navigation.md"
    text = load(path)
    replacements = {
        "17. [P81 projection-event continuous P75 separation]": "17. [P81 projection-event continuous P75 separation]",
        "19. [P82 exact nested projection-contrast separation]": "18. [P82 exact nested projection-contrast separation]",
        "19. [P83 exact projection-parity separation]": "19. [P83 exact projection-parity separation]",
        "18. [P11-P18 and P25-P37 operational physical structure]": "20. [P11-P18 and P25-P37 operational physical structure]",
        "20. [P38-P44 quantum foundations and bridge tests]": "21. [P38-P44 quantum foundations and bridge tests]",
        "21. [P45-P60 adaptive experiment design and scheduling]": "22. [P45-P60 adaptive experiment design and scheduling]",
        "22. [P61-P70 Calibration and Optimization Frontier]": "23. [P61-P70 Calibration and Optimization Frontier]",
        "23. [Equation and citation map]": "24. [Equation and citation map]",
        "24. [P72 equation and provenance record]": "25. [P72 equation and provenance record]",
        "25. [P73 equation and provenance record]": "26. [P73 equation and provenance record]",
        "26. [P74 equation and provenance record]": "27. [P74 equation and provenance record]",
        "27. [P75 equation and provenance record]": "28. [P75 equation and provenance record]",
        "28. [Falsification program]": "29. [Falsification program]",
        "29. [P78 equation and provenance record]": "30. [P78 equation and provenance record]",
        "30. [P80 equation and provenance record]": "31. [P80 equation and provenance record]",
        "31. [Citation guide]": "32. [Citation guide]",
    }
    for old, new in replacements.items():
        if old != new and old not in text:
            raise RuntimeError(f"navigation numbering anchor missing: {old}")
        text = text.replace(old, new, 1)

    p83_provenance = "33. [P83 equation and provenance record](p83_equation_provenance.md) for exact parity identities, multi-affine box extrema, the strict P83 > P82 witness, and the scientific interpretation boundary."
    citation_line = "32. [Citation guide](../CITATION.md) for citing the whole research program or a specific proposition, figure, algorithm, or implementation."
    if p83_provenance not in text:
        text = replace_once(text, citation_line, citation_line + "\n" + p83_provenance, path=path)
    save(path, text)


def add_v082_release_archive() -> None:
    release_path = ROOT / "docs/releases/v0.82.0.md"
    release_text = """# v0.82.0 - P82 Exact Nested Projection-Contrast Certification

**Release date:** 12 September 2026
**Research frontier:** P82
**Project status:** ongoing mathematical-physics research; the physical-to-experiential bridge remains open.

## Release summary

Version 0.82.0 advances the documented theorem frontier to **Proposition 82: Exact Nested Projection-Contrast Certificate for Continuous P75 Separation**.

P82 strengthens the continuous four-view P75 target-measurement model-separation chain by using residual events formed from nested projected cylinders. For a parent cylinder $A$ and a stricter child cylinder $B$, the residual event $A\\setminus B$ is generally not itself a cylinder. Under the declared P75 conditional-independence model, P82 computes its parameter-box range directly from the branchwise factorization rather than conservatively subtracting two separate P81 event intervals.

The release adds **256 genuinely new nested residual contrasts** while retaining every P81 lower bound. The certified dominance chain is

\[
L_{82} \ge L_{81} \ge L_{80} \ge L_{78}.
\]

A concrete exact-rational witness gives

\[
L_{80}=0,\qquad L_{81}=\frac{1}{16},\qquad L_{82}=\frac{1}{12}.
\]

This is a genuine strict strengthening of the certified model-distance lower bound on the declared witness.

## Exact certification and implementation

- exact-rational P82 implementation in `src/consciousness_bridge/nested_projection_contrast_separation.py`
- exact vertex-enumeration audit of residual-event extrema
- regression tests for dominance, exactness, direct residual extremization, and the strict P82 > P81 witness
- retention of the already-proved P78 mesh-width upper certificate for global branch-and-bound
- retention of the P79 one-sided exact-rational sampling-radius handoff

## Publication record

The formal v0.82.0 release records:

- 82 proposition-level results
- 70 paper-facing equation-driven quantitative figures
- 140 SVG assets in the complete visual record
- synchronized P82 proof, provenance, README, reader guide, theorem roadmap, research navigation, citation surfaces, figure catalog, changelog, and website

## Reproducibility

The publication candidate passed the pinned reference validation stack reported in the GitHub release record:

- 1081 tests
- Ruff
- repository publication verifier
- deterministic byte-stable figure regeneration
- exact end-to-end reproducibility audit under Ubuntu 24.04 and Python 3.12.14
- Python 3.10, 3.11, and 3.12 compatibility CI

## Scientific boundary

P82 is a conditional computational theorem about separation from the **declared P75 target-measurement model family**. It does not identify the latent state with consciousness, does not turn non-rejection into model validation, and does not establish that consciousness is a scalar, state of matter, quantum variable, or additional spacetime dimension. The physical-to-experiential bridge remains an open research problem.

**Release tag:** `v0.82.0`
**Release commit:** `071fc42d25ebc0b14bee77619600e9d04d4e8824`
"""
    release_path.write_text(release_text, encoding="utf-8")

    path = "CHANGELOG.md"
    text = load(path)
    heading = "# Release v0.82.0 - P82 Exact Nested Projection-Contrast Certification"
    if heading not in text:
        marker = "# Release v0.81.0"
        if marker not in text:
            raise RuntimeError("v0.81.0 changelog anchor missing")
        section = """# Release v0.82.0 - P82 Exact Nested Projection-Contrast Certification

- Advanced the formal release frontier to P82 with 82 proposition-level results.
- Added exact nested residual-event ranges for 256 genuinely new parent-child projection contrasts in the P75 model family.
- Established the never-weaker chain `L82 >= L81 >= L80 >= L78` on each parameter box.
- Added an exact-rational strict witness with `L80 = 0`, `L81 = 1/16`, and `L82 = 1/12`.
- Retained the proved P78 mesh-width upper certificate and the P79 one-sided sampling-radius rejection gate.
- Published 70 paper-facing equation-driven quantitative figures and 140 SVG assets in the complete visual record.
- Passed 1081 tests, Ruff, deterministic figure regeneration, repository verification, and the exact pinned reproducibility audit before release.
- Preserved the interpretation boundary that P82 is a conditional model-distance theorem and does not identify a latent state with consciousness.

See `docs/releases/v0.82.0.md` and the immutable GitHub release tagged `v0.82.0` for the archival release record.

"""
        text = text.replace(marker, section + marker, 1)
        save(path, text)


def main() -> None:
    repair_website_start_here()
    normalize_research_navigation()
    add_v082_release_archive()
    print("P83 publication cleanup applied")


if __name__ == "__main__":
    main()
