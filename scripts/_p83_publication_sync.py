"""One-time synchronization helper for the P83 / v0.83.0 publication candidate.

This script is intentionally strict and idempotent. It updates only reader-facing,
release, citation, website, verifier, and deterministic artifact metadata surfaces.
It is removed before the P83 pull request is merged.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_required(text: str, old: str, new: str, *, path: str) -> str:
    if old not in text:
        if new in text:
            return text
        raise RuntimeError(f"{path}: required marker not found: {old[:100]!r}")
    return text.replace(old, new)


def insert_once(text: str, marker: str, addition: str, *, sentinel: str, path: str) -> str:
    if sentinel in text:
        return text
    if marker not in text:
        raise RuntimeError(f"{path}: insertion marker not found: {marker[:100]!r}")
    return text.replace(marker, marker + addition, 1)


def append_once(text: str, addition: str, *, sentinel: str) -> str:
    if sentinel in text:
        return text
    return text.rstrip() + "\n\n" + addition.strip() + "\n"


P83_README = r'''

P83 asks what remains hidden when P81 and P82 test observable events one at a time. Two cylinder probabilities can each lie inside their exact P75 parameter-box intervals while their **difference is impossible for any common parameter vector**. P83 therefore introduces signed non-nested cylinder contrasts

\[
\phi_{A,B}(x)=\mathbf 1_A(x)-\mathbf 1_B(x).
\]

For any probability laws \(p,q\),

\[
|E_p\phi_{A,B}-E_q\phi_{A,B}|
\le
|A\triangle B|\,\|p-q\|_\infty,
\]

so an empirical signed-contrast mismatch yields the certified lower bound

\[
\|\widehat p-q_\theta\|_\infty
\ge
\frac{d\!\left(\widehat c_{A,B},[\ell_{A,B},u_{A,B}]\right)}{|A\triangle B|}.
\]

Inside each P75 latent branch the contrast is multi-affine in at most four response coordinates, so its exact rational box extrema occur at at most sixteen endpoint vertices. Affine prevalence mixing is then extremized exactly at the prevalence endpoints. P83 audits all **2,696 genuinely new unordered non-nested cylinder pairs** and defines

\[
\boxed{L_{83}(B)=\max\{L_{82}(B),L_{\mathrm{signed}}(B)\}},
\]

hence

\[
\boxed{L_{83}\ge L_{82}\ge L_{81}\ge L_{80}\ge L_{78}}.
\]

The strict exact-rational witness is deliberately stronger than a relaxation-only example:

\[
L_{80}=L_{81}=L_{82}=0,
\qquad
L_{83}=\frac{5}{128}.
\]

For the same witness box an explicit admissible model at prevalence \(\pi=5/16\) is exactly \(5/128\) away from the empirical law, so P83 closes the true witness-box model distance while P82 reports zero.

![P83 exact signed cylinder-contrast certificate](docs/figures/p83_signed_cylinder_contrast_separation.svg)

**Figure: P83 exact signed cylinder-contrast certificate.** Read the three panels from left to right: construct a non-nested signed event difference, extremize that common-parameter functional exactly over the P75 box, then transfer its mismatch to full-law \(L_\infty\) distance. The figure is a theorem diagram, not empirical evidence about consciousness. The physical-to-experiential bridge remains open.

Direct audit paths: [P83 proof](docs/proposition_83_signed_cylinder_contrast_separation.md), [equation/provenance record](docs/p83_equation_provenance.md), [implementation](src/consciousness_bridge/signed_cylinder_contrast_separation.py), and [tests](tests/test_signed_cylinder_contrast_separation.py).
'''

P83_RECORD = r'''
## P83: Exact Signed Cylinder-Contrast Certificate for Continuous P75 Separation

**P83** strengthens P82 by retaining shared-parameter compatibility across pairs of non-nested cylinder events. For

\[
\phi_{A,B}=\mathbf1_A-\mathbf1_B,
\]

the full-law transfer inequality is

\[
|E_p\phi-E_q\phi|\le\|\phi\|_1\|p-q\|_\infty,
\qquad
\|\phi_{A,B}\|_1=|A\triangle B|.
\]

Inside each latent branch of P75, \(P_s(A)-P_s(B)\) is multi-affine in at most four response coordinates. Its exact box extrema are therefore attained at endpoint vertices, and the final latent-mixture interval is obtained by exact affine prevalence-endpoint extremization. Of the \({80\choose2}=3160\) unordered distinct cylinder pairs, 464 are nested and already represented by P81/P82, leaving **2696 genuinely new non-nested P83 contrasts**.

P83 defines

\[
L_{83}(B)=\max\{L_{82}(B),L_{\mathrm{signed}}(B)\},
\]

so \(L_{83}\ge L_{82}\ge L_{81}\ge L_{80}\ge L_{78}\). On the exact strict witness,

\[
L_{80}=L_{81}=L_{82}=0,
\qquad
L_{83}=5/128.
\]

An explicit admissible model at \(\pi=5/16\) has full-law distance exactly \(5/128\), proving that P83 closes the true witness-box distance while P82 certifies zero.

Direct proof: [Proposition 83](proposition_83_signed_cylinder_contrast_separation.md). Equation classification: [P83 equation and provenance record](p83_equation_provenance.md). Implementation: [`signed_cylinder_contrast_separation.py`](../src/consciousness_bridge/signed_cylinder_contrast_separation.py). Tests: [`test_signed_cylinder_contrast_separation.py`](../tests/test_signed_cylinder_contrast_separation.py).
'''

P83_ROADMAP = r'''
## Current frontier: P83 signed cylinder-contrast certification

P83 is the next dependency-aware tightening of the P77-P82 continuous P75 separation branch:

\[
P77\rightarrow P78\rightarrow P80\rightarrow P81\rightarrow P82\rightarrow P83,
\qquad
P79\rightarrow\text{finite-sample rejection gate}.
\]

P83 does not replace the earlier results. It adds exact signed differences between **non-nested** cylinder events while retaining the complete P82 lower bound. Its standard family contains 2,696 new pairs, and its exact witness satisfies

\[
L_{80}=L_{81}=L_{82}=0<L_{83}=5/128.
\]

The matching admissible upper witness at \(\pi=5/16\) gives distance \(5/128\), so the P83 lower certificate is tight on that example.

- [P83 proof](proposition_83_signed_cylinder_contrast_separation.md)
- [P83 equation provenance](p83_equation_provenance.md)
- [P83 implementation](../src/consciousness_bridge/signed_cylinder_contrast_separation.py)
- [P83 tests](../tests/test_signed_cylinder_contrast_separation.py)
- [P83 theorem figure](figures/p83_signed_cylinder_contrast_separation.svg)

Scientific boundary: this is a model-distance theorem for the declared P75 family. It does not identify the latent variable with consciousness and does not close the physical-to-experiential bridge.
'''

P83_NAV = r'''
## P83 current frontier: when separately compatible events are jointly incompatible

**Question.** Can two projected event probabilities each pass P81/P82 while their common-parameter relationship is impossible under the P75 family?

**Answer.** Yes. [P83](proposition_83_signed_cylinder_contrast_separation.md) tests exact signed differences of non-nested cylinder events. It uses the dual inequality

\[
|E_p\phi-E_q\phi|\le\|\phi\|_1\|p-q\|_\infty
\]

and exact multi-affine box extremization to produce a new rational lower bound. The standard family has 2,696 genuinely new pairs. The strict witness has \(L_{82}=0\) and \(L_{83}=5/128\), with a matching explicit P75 upper witness, so the certificate is exact on that example.

Audit path: [proof](proposition_83_signed_cylinder_contrast_separation.md) → [equation provenance](p83_equation_provenance.md) → [source](../src/consciousness_bridge/signed_cylinder_contrast_separation.py) → [tests](../tests/test_signed_cylinder_contrast_separation.py) → [figure](figures/p83_signed_cylinder_contrast_separation.svg).
'''

P83_EQMAP = r'''
## P83: exact signed cylinder-contrast separation

| P83 ingredient | Equation / object | Provenance role |
| --- | --- | --- |
| Signed cylinder observable | \(\phi_{A,B}=\mathbf1_A-\mathbf1_B\) | P83 repository construction using standard linear functionals. |
| Full-law transfer | \(|E_p\phi-E_q\phi|\le\|\phi\|_1\|p-q\|_\infty\) | Standard finite-dimensional \(\ell_1\)-\(\ell_\infty\) dual inequality. |
| Indicator norm | \(\|\phi_{A,B}\|_1=|A\triangle B|\) | Elementary set algebra. |
| Branch contrast | \(g_s=P_s(A)-P_s(B)\) | P75 conditional-independence products combined by P83. |
| Exact branch interval | extrema of \(g_s\) at endpoint vertices | Standard multi-affine endpoint principle, inherited computational logic from P78 and specialized by P83. |
| Exact mixture interval | prevalence endpoint extremization of branch minima/maxima | Elementary affine extremization plus disjoint P75 branch coordinates. |
| New finite family | \(|\mathcal S_{83}|=2696\) | Repository-original predeclared non-nested cylinder-pair audit. |
| P83 certificate | \(L_{83}=\max\{L_{82},L_{\mathrm{signed}}\}\) | New P83 theorem construction. |
| Strict witness | \(L_{80}=L_{81}=L_{82}=0<L_{83}=5/128\) | Repository-original exact-rational witness. |
| Tight upper witness | \(\pi=5/16\Rightarrow d_\infty=5/128\) | Repository-original exact closure of the witness-box distance. |

Full classification and scientific boundary: [P83 equation and provenance record](p83_equation_provenance.md).
'''

P83_CITATION_PARAGRAPH = (
    " Cite [Proposition 83](docs/proposition_83_signed_cylinder_contrast_separation.md) "
    "when relying on exact non-nested signed cylinder-contrast intervals, the 2,696-pair audit, "
    "the P83 never-weaker-than-P82 certificate, or the exact 5/128 strict-and-tight witness."
)

P83_WEBSITE_SECTION = '''
<section id="p83-frontier">
  <div class="section-head">
    <p class="eyebrow">Current theorem frontier · P83</p>
    <h2>Exact signed cylinder-contrast certification</h2>
    <p>P83 tests whether pairs of non-nested projected events are jointly compatible with one common P75 parameter vector. Each branch contrast is multi-affine, so exact rational extrema occur at endpoint vertices; prevalence is then extremized at its endpoints. The result preserves every P82 bound and adds 2,696 genuinely new signed contrasts.</p>
  </div>
  <div class="figure-card">
    <img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p83_signed_cylinder_contrast_separation.svg" alt="P83 exact signed cylinder-contrast certificate" />
    <div>
      <h3>P83: shared-parameter compatibility beyond one-event tests</h3>
      <p>The exact witness has P80 = P81 = P82 = 0 while P83 = 5/128. An admissible model at prevalence 5/16 attains distance 5/128, so P83 closes the true witness-box distance rather than merely improving a relaxation.</p>
      <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_83_signed_cylinder_contrast_separation.md">Read the P83 proof →</a></p>
      <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p83_equation_provenance.md">Audit equation provenance →</a></p>
      <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/signed_cylinder_contrast_separation.py">Open implementation →</a></p>
      <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_signed_cylinder_contrast_separation.py">Open tests →</a></p>
    </div>
  </div>
  <div class="boundary"><strong>Scientific boundary.</strong> P83 is a conditional exact model-distance theorem for the declared P75 target-measurement family. It does not identify a latent variable with consciousness, does not validate a non-rejected model, and does not close the physical-to-experiential bridge.</div>
</section>
'''


def update_readme() -> None:
    path = "README.md"
    text = read(path)
    text = text.replace("version-0.82.0", "version-0.83.0")
    text = text.replace("P1-P82 program map, and the current P82 frontier", "P1-P83 program map, and the current P83 frontier")
    p82_paragraph = "P82 asks what nested projected events can reveal that separate P81 event tests still discard. For a parent cylinder and a stricter child cylinder, their difference is a generally non-cylinder residual event. Under the declared P75 conditional-independence model, P82 derives the exact parameter-box range of that residual directly from disjoint parent and added-view response coordinates, rather than conservatively subtracting two separate event intervals. The resulting certificate retains all of P81 and adds 256 genuinely new nested contrasts. An exact-rational witness gives P80 = 0, P81 = 1/16, and P82 = 1/12. This is a stronger model-distance certificate, not evidence that the latent state is consciousness."
    text = insert_once(text, p82_paragraph, P83_README, sentinel="P83 asks what remains hidden", path=path)
    text = text.replace(
        "The research currently contains **82 proposition-level results** and **70 equation-driven quantitative figures**. The theorem frontier is P82.",
        "The research currently contains **83 proposition-level results** and **71 equation-driven quantitative figures**. The theorem frontier is P83.",
    )
    text = text.replace("P71-P82", "P71-P83")
    text = text.replace("P75-P82", "P75-P83")
    write(path, text)


def update_start_here() -> None:
    # Already rewritten manually on the P83 branch. Assert the synchronized state.
    text = read("START_HERE.md")
    for marker in ("83 proposition-level results", "P83", "71 paper-facing", "5}{128"):
        if marker not in text:
            raise RuntimeError(f"START_HERE.md missing P83 marker: {marker}")


def update_release_metadata() -> None:
    path = "pyproject.toml"
    text = read(path)
    text = replace_required(text, 'version = "0.82.0"', 'version = "0.83.0"', path=path)
    if "signed cylinder-contrast certification" not in text:
        text = text.replace(
            "exact nested projection-contrast certification, exact residual-event box bounds,",
            "exact nested projection-contrast certification, exact residual-event box bounds, signed cylinder-contrast certification, exact non-nested event-difference box bounds,",
        )
    write(path, text)

    path = "CITATION.cff"
    text = read(path)
    text = replace_required(text, "version: 0.82.0", "version: 0.83.0", path=path)
    if "signed cylinder contrasts" not in text:
        text = text.replace("  - projection-event certification\n", "  - projection-event certification\n  - signed cylinder contrasts\n")
    p82 = "Proposition 82 adds exact nested projection-contrast residual intervals for the same P75 family, audits 256 genuinely new residual events, and yields a never-weaker certificate with an exact-rational strict witness improving P81 from one sixteenth to one twelfth."
    p83 = " Proposition 83 adds exact signed contrasts between 2,696 genuinely new non-nested cylinder pairs, computes their common-parameter P75 box intervals by exact multi-affine vertex extremization and prevalence-endpoint mixing, and yields a never-weaker certificate with a strict exact-rational witness satisfying P80=P81=P82=0 and P83=5/128; an admissible model at prevalence 5/16 attains the same distance, making the witness tight."
    if "Proposition 83 adds exact signed contrasts" not in text:
        if p82 not in text:
            raise RuntimeError("CITATION.cff: P82 abstract marker missing")
        text = text.replace(p82, p82 + p83)
    text = text.replace("Current documented theorem frontier: P82.", "Current documented theorem frontier: P83.")
    text = text.replace("Version 0.82.0.", "Version 0.83.0.")
    write(path, text)

    path = "CITATION.bib"
    text = read(path).replace("version      = {0.82.0}", "version      = {0.83.0}")
    text = text.replace("Current documented theorem frontier: P82.", "Current documented theorem frontier: P83.")
    write(path, text)

    path = "CITATION.md"
    text = read(path)
    text = text.replace("Version 0.82.0", "Version 0.83.0")
    text = text.replace("version      = {0.82.0}", "version      = {0.83.0}")
    text = text.replace("current documented frontier, P82", "current documented frontier, P83")
    text = text.replace("Current documented theorem frontier: P82.", "Current documented theorem frontier: P83.")
    text = text.replace("Version **0.82.0** and theorem frontier **P82**", "Version **0.83.0** and theorem frontier **P83**")
    p82_cite = "Cite [Proposition 82](docs/proposition_82_exact_nested_projection_contrast.md) when relying on exact nested residual-event parameter-box intervals, the 256-contrast audit, the P82 never-weaker-than-P81 certificate, the direct residual extremization theorem, or the exact 1/12 versus 1/16 strict-improvement witness."
    if P83_CITATION_PARAGRAPH.strip() not in text:
        text = text.replace(p82_cite, p82_cite + P83_CITATION_PARAGRAPH)
    text = text.replace("None of P78-P82 turns non-rejection", "None of P78-P83 turns non-rejection")
    p82_scope = "P82 strengthens that chain again by retaining exact common-parameter structure for residual events formed from nested projected cylinders. It computes each residual interval directly from the P75 branchwise factorization rather than by subtracting separate P81 event intervals, audits 256 genuinely new residual events, and preserves the one-sided model-rejection interpretation. Its exact witness gives P80 = 0, P81 = 1/16, and P82 = 1/12. This is a stronger certificate against the declared P75 family, not evidence that its latent variable is consciousness."
    p83_scope = "\n\nP83 strengthens the chain by retaining common-parameter compatibility across two non-nested cylinder events. It computes exact signed event-difference intervals by branchwise multi-affine vertex enumeration and affine prevalence-endpoint extremization, audits 2,696 new pairs, and preserves the one-sided interpretation. Its strict witness gives P80 = P81 = P82 = 0 and P83 = 5/128, with a matching admissible upper witness at prevalence 5/16. This is a model-distance theorem for the declared P75 family, not an experiential identification."
    if "P83 strengthens the chain" not in text:
        text = text.replace(p82_scope, p82_scope + p83_scope)
    text = text.replace("P1 through P82 chronological theorem record", "P1 through P83 chronological theorem record")
    p82_resource = "- [P82 equation and provenance record](docs/p82_equation_provenance.md): exact nested residual-event intervals, direct residual extremization, dominance, and the P79 rejection handoff."
    if "P83 equation and provenance record" not in text:
        text = text.replace(p82_resource, p82_resource + "\n- [P83 equation and provenance record](docs/p83_equation_provenance.md): exact signed cylinder-contrast intervals, non-nested pair audit, dominance, tight witness, and the P79 rejection handoff.")
    p83_bottom = '''\n## Proposition 83\n\nFor the exact signed cylinder-contrast certificate, cite the repository together with [Proposition 83](docs/proposition_83_signed_cylinder_contrast_separation.md) and its [equation provenance record](docs/p83_equation_provenance.md). P83 is a conditional exact-rational model-distance theorem for the declared P75 family. It should not be cited as an identification of consciousness.\n\n## P83 frontier citation note\n\nP83 strengthens P82 through exact common-parameter signed contrasts of non-nested cylinder events. The strict witness has P80=P81=P82=0 and P83=5/128, with a matching explicit P75 upper witness. The physical-to-experiential bridge remains open.\n'''
    text = append_once(text, p83_bottom, sentinel="## Proposition 83")
    write(path, text)


def update_changelog() -> None:
    path = "CHANGELOG.md"
    text = read(path)
    if not text.startswith("# 0.83.0"):
        prefix = '''# 0.83.0 - 2026-09-12

- Added Proposition 83, Exact Signed Cylinder-Contrast Certificate for Continuous P75 Separation.
- Added exact-rational parameter-box intervals for signed differences of non-nested projected cylinder events using branchwise multi-affine endpoint enumeration and affine prevalence-endpoint extremization.
- Audited 2,696 genuinely new unordered non-nested cylinder pairs while retaining all P82 lower bounds.
- Defined `L83(B) = max(L82(B), L_signed(B))` and proved `L83(B) >= L82(B) >= L81(B) >= L80(B) >= L78(B)`.
- Added a strict exact-rational witness with `L80=L81=L82=0` and `L83=5/128`.
- Added a matching admissible P75 model at prevalence `5/16`, proving that P83 equals the true witness-box model distance `5/128`.
- Retained the P78 mesh-width upper certificate and P79 one-sided sampling-radius rejection handoff without claiming a new P83 convergence theorem.
- Added implementation, proof, equation provenance, regression tests, theorem figure, reader documentation, website integration, and v0.83.0 metadata.
- Preserved the scientific boundary that stronger target-model rejection is not an experiential ontology and the physical-to-experiential bridge remains open.

# 0.82.0 - 2026-09-12

- Added Proposition 82, Exact Nested Projection-Contrast Certificate for Continuous P75 Separation.
- Added exact-rational parameter-box ranges for 256 genuinely new nested residual events and direct residual extremization that preserves shared P75 parameter structure.
- Defined `L82(B) = max(L81(B), L_nest(B))` and proved the never-weaker dominance chain through P82.
- Added the exact strict witness `L80=0`, `L81=1/16`, `L82=1/12`.
- Added proof, provenance, implementation, tests, theorem figure, public reader navigation, website integration, deterministic reproducibility updates, and the formal v0.82.0 release.
- Preserved one-sided model-rejection interpretation and the open physical-to-experiential bridge.

'''
        text = prefix + text
    write(path, text)


def update_docs() -> None:
    path = "docs/detailed_proposition_record.md"
    text = read(path)
    text = text.replace("Complete P1 to P82 chronology", "Complete P1 to P83 chronology")
    text = append_once(text, P83_RECORD, sentinel="## P83: Exact Signed Cylinder-Contrast Certificate")
    write(path, text)

    path = "docs/theorem_roadmap.md"
    text = read(path)
    text = text.replace("P1-P82", "P1-P83")
    text = text.replace("P71-P82", "P71-P83")
    text = text.replace("P75-P82", "P75-P83")
    text = append_once(text, P83_ROADMAP, sentinel="## Current frontier: P83 signed cylinder-contrast certification")
    write(path, text)

    path = "docs/research_navigation.md"
    text = read(path)
    text = text.replace("P1-P82", "P1-P83")
    text = text.replace("P71-P82", "P71-P83")
    text = text.replace("P75-P82", "P75-P83")
    text = append_once(text, P83_NAV, sentinel="## P83 current frontier")
    write(path, text)

    path = "docs/equation_and_citation_map.md"
    text = read(path)
    text = text.replace("P1-P82", "P1-P83")
    text = append_once(text, P83_EQMAP, sentinel="## P83: exact signed cylinder-contrast separation")
    write(path, text)

    path = "docs/figure_catalog.md"
    text = read(path)
    text = text.replace("**Current catalog:** 140 SVG figures: 17 architecture/conceptual visuals, 18 foundational quantum-physics visuals, 65 proposition/theorem visuals, and 40 quantitative figures.", "**Current catalog:** 141 SVG figures: 17 architecture/conceptual visuals, 18 foundational quantum-physics visuals, 66 proposition/theorem visuals, and 40 quantitative figures.")
    row = "| [P83 exact signed cylinder-contrast certificate](figures/p83_signed_cylinder_contrast_separation.svg) | What this figure shows: P83 couples two non-nested cylinder events through the signed observable 1_A-1_B, computes its exact P75 box interval by multi-affine endpoint extremization, and transfers mismatch through the symmetric-difference L1 norm. The strict witness has P80=P81=P82=0 and P83=5/128, with a matching explicit upper witness. | Conditional exact-rational computational-certification theorem. It is not an identification of consciousness and the physical-to-experiential bridge remains open. | [Proposition 83](proposition_83_signed_cylinder_contrast_separation.md) |"
    text = append_once(text, "## P83 current-frontier theorem figure\n\n" + row, sentinel="P83 current-frontier theorem figure")
    write(path, text)

    path = "figures/CURRENT_FRONTIER.md"
    text = read(path)
    text = text.replace("# Current visual frontier: P71-P82", "# Current visual frontier: P71-P83")
    text = text.replace("## P75-P81: target-model adequacy and certified separation", "## P75-P83: target-model adequacy and certified separation")
    p82 = '''\n### P82: exact nested projection-contrast separation\n\nP82 retains shared-parameter structure for 256 nested residual events and strictly strengthens P81 on an exact rational witness.\n\n![P82 nested contrast separation](../docs/figures/p82_exact_nested_projection_contrast.svg)\n\n[Read the P82 proposition](../docs/proposition_82_exact_nested_projection_contrast.md)\n\n[Open the P82 equation provenance](../docs/p82_equation_provenance.md)\n'''
    if "### P82: exact nested projection-contrast separation" not in text:
        anchor = "[Open the P81 figure geometry tests](../tests/test_p81_figure_geometry.py)"
        if anchor not in text:
            raise RuntimeError("figures/CURRENT_FRONTIER.md: P81 anchor missing")
        text = text.replace(anchor, anchor + p82)
    p83 = '''\n### P83: exact signed cylinder-contrast separation\n\nP83 tests 2,696 genuinely new non-nested cylinder-pair differences. Exact multi-affine box extremization preserves common P75 parameter dependence that separate event tests can miss. The strict witness has `L80=L81=L82=0`, `L83=5/128`, and a matching explicit upper witness at `pi=5/16`.\n\n![P83 signed cylinder contrast separation](../docs/figures/p83_signed_cylinder_contrast_separation.svg)\n\n[Read the P83 proposition](../docs/proposition_83_signed_cylinder_contrast_separation.md)\n\n[Open the P83 equation provenance](../docs/p83_equation_provenance.md)\n\n[Open the P83 implementation](../src/consciousness_bridge/signed_cylinder_contrast_separation.py)\n\n[Open the P83 numerical tests](../tests/test_signed_cylinder_contrast_separation.py)\n\n[Open the P83 figure geometry tests](../tests/test_p83_figure_geometry.py)\n'''
    text = append_once(text, p83, sentinel="### P83: exact signed cylinder-contrast separation")
    text = text.replace("P71-P82 derives consciousness", "P71-P83 derives consciousness")
    write(path, text)

    for path in ("figures/README.md", "docs/figures/README.md"):
        text = read(path)
        text = text.replace("P82", "P83") if "current frontier" in text.lower() else text
        if "141" not in text and "140" in text:
            text = text.replace("140", "141")
        text = append_once(
            text,
            "### P83 theorem figure\n\n- [`p83_signed_cylinder_contrast_separation.svg`](../docs/figures/p83_signed_cylinder_contrast_separation.svg) — exact signed non-nested cylinder-contrast certificate, 2,696-pair audit, and tight 5/128 witness.\n" if path == "figures/README.md" else "### P83 theorem figure\n\n- [`p83_signed_cylinder_contrast_separation.svg`](p83_signed_cylinder_contrast_separation.svg) — exact signed non-nested cylinder-contrast certificate, 2,696-pair audit, and tight 5/128 witness.\n",
            sentinel="### P83 theorem figure",
        )
        write(path, text)


def update_website() -> None:
    path = "website/start-here.html"
    text = read(path)
    text = text.replace("the 82 proposition-level results, the current P82 frontier", "the 83 proposition-level results, the current P83 frontier")
    text = text.replace("See the 82-result research map", "See the 83-result research map")
    text = text.replace("<strong>82</strong><span>proposition-level results</span>", "<strong>83</strong><span>proposition-level results</span>")
    text = text.replace("<strong>P82</strong><span>current theorem frontier</span>", "<strong>P83</strong><span>current theorem frontier</span>")
    text = text.replace("<strong>v0.82.0</strong><span>documented release</span>", "<strong>v0.83.0</strong><span>publication candidate</span>")
    text = text.replace("P75-P82", "P75-P83")
    text = text.replace("P71-P82", "P71-P83")
    text = text.replace("82 proofs", "83 proofs")
    text = text.replace("The 82 propositions", "The 83 propositions")
    text = text.replace("full 82-result dependency structure", "full 83-result dependency structure")
    old_dark = '''<section class="dark-section">\n      <p class="eyebrow">Current theorem frontier</p>\n      <h2>P82 strengthens full-law model separation without adding a consciousness assumption</h2>'''
    if old_dark in text:
        start = text.index(old_dark)
        end = text.index("    </section>", start) + len("    </section>")
        new_dark = '''<section class="dark-section">\n      <p class="eyebrow">Current theorem frontier</p>\n      <h2>P83 preserves cross-event parameter compatibility that one-event certificates can miss</h2>\n      <p>P83 retains every P82 lower bound and adds exact signed differences between 2,696 non-nested cylinder pairs. Inside each P75 latent branch the signed contrast is multi-affine in at most four response coordinates, so exact rational extrema occur at endpoint vertices; prevalence is then extremized at its endpoints.</p>\n      <p>The strict witness is exact: P80 = P81 = P82 = 0 while P83 = 5/128, and an admissible model at prevalence 5/16 is exactly 5/128 away. This strengthens rejection of the declared target-measurement family without identifying its latent state with consciousness.</p>\n      <div class="hero-actions">\n        <a class="button primary" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_83_signed_cylinder_contrast_separation.md">Read P83</a>\n        <a class="button" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p83_equation_provenance.md">P83 provenance</a>\n        <a class="button" href="visual-atlas.html#p83-frontier">See P83 theorem visual</a>\n      </div>\n    </section>'''
        text = text[:start] + new_dark + text[end:]
    write(path, text)

    path = "website/index.html"
    text = read(path)
    text = text.replace("an 82-result mathematical-physics research program", "an 83-result mathematical-physics research program")
    text = text.replace("Explore all 82 results", "Explore all 83 results")
    text = text.replace("<strong>82</strong><span>proposition-level results</span>", "<strong>83</strong><span>proposition-level results</span>")
    text = text.replace("<strong>P82</strong><span>current theorem frontier</span>", "<strong>P83</strong><span>current theorem frontier</span>")
    text = text.replace("<strong>v0.82.0</strong><span>current documented release</span>", "<strong>v0.83.0</strong><span>publication candidate</span>")
    text = text.replace("82 proposition-level results through P82", "83 proposition-level results through P83")
    text = text.replace("<strong>Current version:</strong> v0.82.0", "<strong>Publication candidate:</strong> v0.83.0")
    text = text.replace("P73-P82", "P73-P83")
    text = text.replace("P75-P82", "P75-P83")
    text = text.replace("The 82 results", "The 83 results")
    text = text.replace("82 proofs", "83 proofs")
    text = text.replace("P71-P82", "P71-P83")
    text = text.replace("P74-P82", "P74-P83")
    text = text.replace("The 82-result program", "The 83-result program")
    text = insert_once(text, "</main>", P83_WEBSITE_SECTION, sentinel='id="p83-frontier"', path=path)
    write(path, text)

    path = "website/research-map.html"
    text = read(path)
    text = text.replace("through Proposition 82", "through Proposition 83")
    text = text.replace("Eighty-two results", "Eighty-three results")
    text = text.replace("P71-P82", "P71-P83")
    text = text.replace("<strong>82</strong><span>proposition-level results</span>", "<strong>83</strong><span>proposition-level results</span>")
    text = text.replace("None of P71-P82", "None of P71-P83")
    text = text.replace("P77-P82: from full-law rejection to exact nested-contrast certification", "P77-P83: from full-law rejection to exact dependency-aware contrast certification")
    text = text.replace("P77-P82", "P77-P83")
    p82_card = '<article class="result"><span>P82</span><h3>Exact nested residual contrasts</h3><p>Use exact ranges of 256 genuinely new residual events from nested cylinders. The concrete exact witness improves the lower bound from P81 = 1/16 to P82 = 1/12.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_82_exact_nested_projection_contrast.md">Open P82 →</a></article>'
    p83_card = '<article class="result"><span>P83</span><h3>Exact signed non-nested contrasts</h3><p>Use exact common-parameter ranges for 2,696 signed non-nested cylinder pairs. The strict witness has P80=P81=P82=0 and P83=5/128, with a matching explicit P75 upper witness.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_83_signed_cylinder_contrast_separation.md">Open P83 →</a></article>'
    text = insert_once(text, p82_card, p83_card, sentinel="Exact signed non-nested contrasts", path=path)
    text = text.replace("Audit P82 equation provenance", "Audit P83 equation provenance")
    text = text.replace("docs/p82_equation_provenance.md", "docs/p83_equation_provenance.md")
    text = text.replace("See the P82 theorem figure", "See the P83 theorem figure")
    text = text.replace("nested_projection_contrast_separation.py", "signed_cylinder_contrast_separation.py")
    text = text.replace("test_nested_projection_contrast_separation.py", "test_signed_cylinder_contrast_separation.py")
    write(path, text)

    path = "website/visual-atlas.html"
    text = read(path)
    text = text.replace("Current theorem frontier · P82", "Previous continuous-model tightening · P82")
    text = insert_once(text, "</main>", P83_WEBSITE_SECTION, sentinel='id="p83-frontier"', path=path)
    write(path, text)


def update_verifier_and_generators() -> None:
    path = "scripts/verify_repository.py"
    text = read(path)
    text = text.replace('CURRENT_VERSION = "0.82.0"', 'CURRENT_VERSION = "0.83.0"')
    text = text.replace('CURRENT_FRONTIER = "P82"', 'CURRENT_FRONTIER = "P83"')
    text = text.replace("for number in range(1, 83):", "for number in range(1, 84):")
    if '"docs/proposition_83_signed_cylinder_contrast_separation.md"' not in text:
        text = text.replace('    "docs/falsification_program.md",', '    "docs/falsification_program.md",\n    "docs/proposition_83_signed_cylinder_contrast_separation.md",\n    "docs/p83_equation_provenance.md",\n    "docs/figures/p83_signed_cylinder_contrast_separation.svg",\n    "src/consciousness_bridge/signed_cylinder_contrast_separation.py",\n    "tests/test_signed_cylinder_contrast_separation.py",')
    write(path, text)

    for path in ("scripts/generate_quantitative_atlas.py", "scripts/generate_quantum_foundations_atlas.py"):
        text = read(path).replace("v0.82.0", "v0.83.0")
        write(path, text)


def update_current_release_tests() -> None:
    replacements = {
        "0.82.0": "0.83.0",
        "P1-P82": "P1-P83",
        "P71-P82": "P71-P83",
        "P75-P82": "P75-P83",
        "82 proposition-level results": "83 proposition-level results",
        "70 paper-facing equation-driven": "71 paper-facing equation-driven",
        "140 SVG": "141 SVG",
    }
    current_release_test_names = {
        "test_release_metadata_consistency.py",
        "test_reader_documentation_consistency.py",
        "test_public_reader_navigation_frontier.py",
        "test_readme_research_orientation.py",
        "test_research_website_integrity.py",
        "test_website_research_orientation.py",
        "test_website_build.py",
        "test_figure_documentation_integrity.py",
        "test_documentation_integrity.py",
        "test_repository_structure.py",
    }
    for test_path in (ROOT / "tests").glob("test_*.py"):
        if test_path.name not in current_release_test_names:
            continue
        text = test_path.read_text(encoding="utf-8")
        original = text
        for old, new in replacements.items():
            text = text.replace(old, new)
        # Current-frontier assertions in these files should move one proposition.
        text = text.replace('"P82"', '"P83"') if "frontier" in text.lower() else text
        if text != original:
            test_path.write_text(text, encoding="utf-8")


def main() -> None:
    update_readme()
    update_start_here()
    update_release_metadata()
    update_changelog()
    update_docs()
    update_website()
    update_verifier_and_generators()
    update_current_release_tests()
    print("[p83-sync] synchronized P83/v0.83.0 publication surfaces")


if __name__ == "__main__":
    main()
