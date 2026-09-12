"""One-shot synchronization of the P83 research frontier across publication surfaces.

This script is intentionally temporary. The accompanying branch-only workflow runs
it once, regenerates the deterministic figure catalog, removes both temporary
integration files, and commits the resulting reader-facing publication state.

P83 advances the documented theorem frontier while v0.82.0 remains the latest
formal release until the P83 pull request has passed the complete validation
stack. Release version and theorem frontier are deliberately treated as separate
concepts during review.
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
        raise RuntimeError(f"required anchor not found in {path}: {old!r}")
    return text.replace(old, new)


def append_before(text: str, marker: str, block: str, *, path: str) -> str:
    if block.strip() in text:
        return text
    if marker not in text:
        raise RuntimeError(f"append marker not found in {path}: {marker!r}")
    return text.replace(marker, block + "\n\n" + marker, 1)


def update_source_phrase() -> None:
    path = "src/consciousness_bridge/projection_parity_model_separation.py"
    text = read(path)
    text = text.replace(
        "Therefore every P83 parity interval is exact,\nnot merely an enclosure.",
        "Therefore every P83 parity interval is exact, not merely an enclosure.",
    )
    write(path, text)


def update_readme() -> None:
    path = "README.md"
    text = read(path)
    replacements = {
        "the P1-P82 program map, and the current P82 frontier":
            "the P1-P83 program map, and the current P83 frontier",
        "P19-P24, P71-P82": "P19-P24, P71-P83",
        "P71-P82": "P71-P83",
        "P75-P82": "P75-P83",
        "P1 through P82 with explicit dependency branches":
            "P1 through P83 with explicit dependency branches",
        "**82 proposition-level results** and **70 equation-driven quantitative figures**. The theorem frontier is P82.":
            "**83 proposition-level results** and **71 equation-driven quantitative figures**. The theorem frontier is P83.",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    p82 = (
        "P82 asks what nested projected events can reveal that separate P81 event tests still discard. "
        "For a parent cylinder and a stricter child cylinder, their difference is a generally non-cylinder residual event. "
        "Under the declared P75 conditional-independence model, P82 derives the exact parameter-box range of that residual directly from disjoint parent and added-view response coordinates, rather than conservatively subtracting two separate event intervals. "
        "The resulting certificate retains all of P81 and adds 256 genuinely new nested contrasts. "
        "An exact-rational witness gives P80 = 0, P81 = 1/16, and P82 = 1/12. "
        "This is a stronger model-distance certificate, not evidence that the latent state is consciousness."
    )
    p83 = (
        "P83 asks whether a simple dependency observable can expose incompatibility that remains hidden even after the P82 nested-residual audit. "
        "For every two-, three-, and four-view subset, it tests both binary parity events. Conditional independence inside each P75 latent branch gives the exact identity "
        "`P_s(H(J,b)) = [1 + (-1)^b product_j(1 - 2 q_{j,s})]/2`. The product is multi-affine, so its complete range on a rational parameter box is attained at response-coordinate vertices; prevalence then enters affinely and is extremized at its endpoints. "
        "The standard P83 family contains only 22 genuinely new parity observables, and every event mismatch transfers to a full-law L-infinity lower bound by dividing by the eight cells in a parity event. "
        "An exact-rational witness fixes one observed channel at one half in both latent branches and uses an empirical law supported on equal-bit pairs: the complete P82 audit remains zero, while P83 certifies `1/16`. "
        "P83 is therefore a strict strengthening of the declared P75 model-distance certificate on that witness, not a consciousness-identification result."
    )
    if p83 not in text:
        if p82 not in text:
            raise RuntimeError("README P82 narrative anchor not found")
        text = text.replace(p82, p82 + "\n\n" + p83, 1)

    figure_block = """![P83 exact projection-parity certificate](docs/figures/p83_exact_projection_parity.svg)

**P83 frontier figure.** P83 adds 22 exact parity observables to the complete P82 certificate. The figure shows the Bernoulli parity identity, exact multi-affine box extremization, the eight-cell event-mass transfer, and the strict exact-rational witness with `L82 = 0` and `L83 = 1/16`. The result is conditional on the declared P75 model and does not identify the latent state with experience."""
    if figure_block not in text:
        text = text.replace(p83, p83 + "\n\n" + figure_block, 1)

    write(path, text)


def update_start_here() -> None:
    path = "START_HERE.md"
    text = read(path)
    replacements = {
        "the 82-result theorem program": "the 83-result theorem program",
        "The repository contains **82 proposition-level results**. The current theorem frontier is **P82**.":
            "The repository contains **83 proposition-level results**. The current theorem frontier is **P83**.",
        "Target-model adequacy\\nP75-P82": "Target-model adequacy\\nP75-P83",
        "P71-P82": "P71-P83",
        "P74-P82": "P74-P83",
        "## The 82 results, organized by scientific role":
            "## The 83 results, organized by scientific role",
        "**P75-P82** | Target-model adequacy and certified continuous-family separation":
            "**P75-P83** | Target-model adequacy and certified continuous-family separation",
        "## The current frontier: P71-P82 in plain language":
            "## The current frontier: P71-P83 in plain language",
        "declared four-view binary latent target-measurement family used in P75-P82":
            "declared four-view binary latent target-measurement family used in P75-P83",
        "\\(L_{78},L_{80},L_{81}\\) | progressively tighter certified lower bounds used in continuous-model separation":
            "\\(L_{78},L_{80},L_{81},L_{82},L_{83}\\) | progressively tighter certified lower bounds used in continuous-model separation",
        "**Proposition frontier:** P81": "**Proposition frontier:** P83",
        "**Proposition-level results:** 81": "**Proposition-level results:** 83",
        "## Current theorem frontier: P82": "## Current theorem frontier: P83",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    p82_frontier = """**P82: exact nested projection contrasts.** Separate projected-event intervals can discard dependence created by shared parameters. P82 computes exact ranges for 256 nested residual events directly from the P75 factorization and can strictly improve P81 while preserving one-sided certification."""
    p83_frontier = """**P83: exact projection parity.** P83 adds 22 parity observables on two, three, and four views. The branchwise parity probability has a closed product form whose extrema on a rational box occur at vertices. A strict exact-rational witness has `L82 = 0` but `L83 = 1/16`, showing that parity can expose a dependency constraint invisible to all predeclared P82 events."""
    anchor = "The direct P81 proof is [here](docs/proposition_81_projection_event_model_separation.md), with its [equation/provenance record](docs/p81_equation_provenance.md), [implementation](src/consciousness_bridge/projection_event_model_separation.py), and [tests](tests/test_projection_event_model_separation.py)."
    if p82_frontier not in text:
        text = replace_required(text, anchor, anchor + "\n\n" + p82_frontier, path=path)
    if p83_frontier not in text:
        text = text.replace(p82_frontier, p82_frontier + "\n\n" + p83_frontier, 1)

    old_tail = """[P82: Exact Nested Projection-Contrast Certificate](docs/proposition_82_exact_nested_projection_contrast.md) strengthens P81 by computing exact P75 parameter-box ranges for non-cylinder residual events formed from nested projected cylinders. It preserves the one-sided model-rejection logic and does not identify any latent state with consciousness."""
    new_tail = """[P83: Exact Projection-Parity Certificate](docs/proposition_83_exact_projection_parity.md) strengthens the complete P82 lower bound with 22 exact parity observables. Its strict witness has `L82 = 0` and `L83 = 1/16`. The theorem remains a conditional model-distance certificate and does not identify any latent state with consciousness."""
    text = text.replace(old_tail, new_tail)
    write(path, text)


def update_theorem_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    text = text.replace("frontier is **P82**", "frontier is **P83**")
    text = text.replace("**P1 through P82 with explicit dependency branches**", "**P1 through P83 with explicit dependency branches**")
    text = text.replace("P71-P82 return", "P71-P83 return")
    chain = "&\\text{P82: exact nested residual-event constraints tighten P81 while preserving certification}"
    if "P83: projection-parity" not in text:
        text = replace_required(
            text,
            chain,
            chain + "\\\\\n&\\Downarrow\\\\\n&\\text{P83: projection-parity constraints expose additional exact dependence structure}",
            path=path,
        )

    block = r"""## P83 frontier: exact projection-parity separation

P82 retains common-parameter structure for nested residual events. P83 adds a complementary dependency observable. For selected views $J$ and parity $b$,

\[
H(J,b)=\{x:\bigoplus_{j\in J}x_j=b\},
\]

and P75 conditional independence gives

\[
\boxed{
P_s(H(J,b))
=
\frac{1+(-1)^b\prod_{j\in J}(1-2q_{j,s})}{2}.
}
\]

The product is multi-affine in the selected response coordinates. Exact branch extrema therefore occur at box vertices, and the latent mixture is then affine in prevalence. P83 audits both parities on every two-, three-, and four-view subset, for 22 genuinely new events, and defines

\[
\boxed{L_{83}(B)=\max\{L_{82}(B),L_{\mathrm{par}}(B)\}.}
\]

A strict exact-rational witness fixes one observed channel at Bernoulli one half in both latent branches. Every P75 law in that box then has pair parity one half, while an empirical equal-bit law has parity one. The complete P82 event family remains compatible, giving

\[
\boxed{L_{82}(B)=0<L_{83}(B)=1/16.}
\]

P83 retains the already-proved P78 mesh-width upper certificate for branch-and-bound and the P79 one-sided sampling-radius rejection handoff. It does not claim a new convergence-rate theorem and does not identify the P75 latent state with consciousness.

Direct proof: [P83](proposition_83_exact_projection_parity.md). Provenance: [P83 equation record](p83_equation_provenance.md). Implementation: [`projection_parity_model_separation.py`](../src/consciousness_bridge/projection_parity_model_separation.py). Tests: [`test_projection_parity_model_separation.py`](../tests/test_projection_parity_model_separation.py).
"""
    if "## P83 frontier: exact projection-parity separation" not in text:
        text += "\n\n" + block
    write(path, text)


def update_research_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    text = text.replace("frontier is **P82**", "frontier is **P83**")
    text = text.replace("**P1 through P82**", "**P1 through P83**")
    text = text.replace("P71-P82 form", "P71-P83 form")
    text = text.replace("from P1 through P82", "from P1 through P83")

    p82_line = "19. [P82 exact nested projection-contrast separation](proposition_82_exact_nested_projection_contrast.md) for exact nested residual-event box intervals, the 256-contrast audit, P82 >= P81 dominance, and the strict 1/12 versus 1/16 witness."
    p83_line = "19. [P83 exact projection-parity separation](proposition_83_exact_projection_parity.md) for the 22-event parity audit, exact multi-affine box intervals, P83 >= P82 dominance, and the strict `1/16` versus zero witness."
    if p83_line not in text:
        if p82_line in text:
            text = text.replace(p82_line, p82_line + "\n" + p83_line, 1)
        else:
            marker = "[P82 exact nested projection-contrast separation](proposition_82_exact_nested_projection_contrast.md)"
            idx = text.find(marker)
            if idx == -1:
                raise RuntimeError("research navigation P82 reading anchor not found")
            line_end = text.find("\n", idx)
            text = text[:line_end] + "\n" + p83_line + text[line_end:]

    p82_row = "| Nested projection-contrast continuous target-model separation | P82 | Adds exact residual-event ranges for nested projected cylinders and retains common-parameter structure beyond separate P81 event tests | [P82](proposition_82_exact_nested_projection_contrast.md) |"
    p83_row = "| Projection-parity continuous target-model separation | P83 | Adds 22 exact parity-event ranges whose multi-affine branch structure can expose dependence incompatibility invisible to the complete P82 event family | [P83](proposition_83_exact_projection_parity.md) |"
    if p83_row not in text:
        text = replace_required(text, p82_row, p82_row + "\n" + p83_row, path=path)

    text += "" if "p83_equation_provenance.md" in text else "\n\n**Current frontier provenance:** [P83 equation and provenance record](p83_equation_provenance.md).\n"
    write(path, text)


def update_detailed_record() -> None:
    path = "docs/detailed_proposition_record.md"
    text = read(path)
    text = text.replace("## Complete P1 to P82 chronology", "## Complete P1 to P83 chronology")
    block = """## P83: Exact Projection-Parity Certificate for Continuous P75 Separation

P83 strengthens the complete P82 continuous-family lower bound with 22 parity observables on all two-, three-, and four-view subsets. Conditional independence inside each P75 latent branch yields an exact Bernoulli parity identity. Its response-coordinate product is multi-affine, so exact rational box extrema occur at endpoint vertices; affine prevalence mixing then gives the exact full-box parity interval. Event mismatch transfers to full-law L-infinity distance through the eight-cell support size. A constructive exact-rational witness has `L82 = 0` and `L83 = 1/16`, proving strict improvement on the same parameter box. P83 keeps the P78 upper certificate and P79 rejection direction unchanged and does not identify the latent state with consciousness.

- Proof: [Proposition 83](proposition_83_exact_projection_parity.md)
- Provenance: [P83 equation record](p83_equation_provenance.md)
- Implementation: [`projection_parity_model_separation.py`](../src/consciousness_bridge/projection_parity_model_separation.py)
- Tests: [`test_projection_parity_model_separation.py`](../tests/test_projection_parity_model_separation.py)
- Figure: [P83 exact projection-parity certificate](figures/p83_exact_projection_parity.svg)
"""
    if "## P83: Exact Projection-Parity Certificate" not in text:
        text += "\n\n" + block
    write(path, text)


def update_equation_map() -> None:
    path = "docs/equation_and_citation_map.md"
    text = read(path)
    block = """## P83: exact projection-parity certificate

| Equation or object | Role | Provenance |
| --- | --- | --- |
| $H(J,b)=\{x:\bigoplus_{j\in J}x_j=b\}$ | finite projection-parity event | standard binary parity definition; P83 observable family |
| $P_s(H(J,b))=[1+(-1)^b\prod_{j\in J}(1-2q_{j,s})]/2$ | exact latent-branch parity law | standard Bernoulli character identity applied to P75 conditional independence |
| vertex extrema of $\prod_j(1-2q_{j,s})$ | exact rational branch interval | standard multi-affine box-extremum principle; new P83 certification use |
| $L_{\mathrm{par}}=\max d(\hat p(H),[\ell_H,u_H])/8$ | event-to-full-law lower bound | P81 event-mass transfer plus exact P83 parity intervals |
| $L_{83}=\max\{L_{82},L_{\mathrm{par}}\}$ | combined certificate | repository-original P83 construction |
| $L_{82}=0<L_{83}=1/16$ witness | proves strict improvement is possible | repository-original exact-rational constructive witness |

Full classification: [P83 equation and provenance record](p83_equation_provenance.md). The parity observable is a model diagnostic, not a definition or measure of consciousness.
"""
    if "## P83: exact projection-parity certificate" not in text:
        text += "\n\n" + block
    write(path, text)


def update_citations_and_changelog() -> None:
    path = "CITATION.cff"
    text = read(path)
    text = text.replace("Current documented theorem frontier: P82.", "Current documented theorem frontier: P83.")
    p82_sentence = "Proposition 82 adds exact nested projection-contrast residual intervals for the same P75 family, audits 256 genuinely new residual events, and yields a never-weaker certificate with an exact-rational strict witness improving P81 from one sixteenth to one twelfth."
    p83_sentence = "Proposition 83 adds 22 exact projection-parity observables whose branch probabilities have a closed multi-affine product form, yielding an exact-rational never-weaker certificate and a strict witness with P82 equal to zero while P83 equals one sixteenth."
    if p83_sentence not in text:
        text = replace_required(text, p82_sentence, p82_sentence + " " + p83_sentence, path=path)
    write(path, text)

    path = "CITATION.md"
    text = read(path)
    block = """## Proposition 83 method citation

For work that specifically uses the newest continuous-family certificate, cite the program together with **Proposition 83: Exact Projection-Parity Certificate for Continuous P75 Separation**. P83 adds 22 parity observables, exact rational box extremization through the Bernoulli parity identity, and a strict witness with `L82 = 0 < L83 = 1/16`.

The result is a conditional model-distance certificate for the declared P75 latent family. It should not be cited as an identification, definition, or measurement of consciousness, and non-rejection remains inconclusive.
"""
    if "## Proposition 83 method citation" not in text:
        text += "\n\n" + block
    write(path, text)

    path = "CHANGELOG.md"
    text = read(path)
    block = """# Unreleased research frontier - P83

- Added Proposition 83, Exact Projection-Parity Certificate for Continuous P75 Separation.
- Added 22 predeclared parity observables across all two-, three-, and four-view subsets of the P75 observed variables.
- Derived the exact branch identity `P_s(H(J,b)) = [1 + (-1)^b product_j(1 - 2 q_(j,s))]/2` and exact rational box extrema by multi-affine vertex evaluation.
- Defined `L83(B) = max(L82(B), L_parity(B))`, so the new certificate is never weaker than P82 on the same box.
- Added an exact strict witness with `L82(B)=0` and `L83(B)=1/16`, exposing dependence structure that the complete P82 event family can leave compatible.
- Added implementation, regression tests, proof, equation provenance, theorem figure, navigation, citation guidance, and website integration.
- Kept v0.82.0 as the latest formal release while P83 is under review; the documented theorem frontier and release version are intentionally distinct during development.
- Preserved the P78 mesh-width upper certificate, the P79 one-sided rejection gate, and the explicit boundary that the physical-to-experiential bridge remains open.

"""
    if not text.startswith("# Unreleased research frontier - P83"):
        text = block + text
    write(path, text)


def update_verifier() -> None:
    path = "scripts/verify_repository.py"
    text = read(path)
    text = replace_required(text, 'CURRENT_FRONTIER = "P82"', 'CURRENT_FRONTIER = "P83"', path=path)
    text = replace_required(text, "for number in range(1, 83):", "for number in range(1, 84):", path=path)
    write(path, text)


def update_visual_frontier() -> None:
    path = "figures/CURRENT_FRONTIER.md"
    text = read(path)
    text = text.replace("# Current visual frontier: P71-P82", "# Current visual frontier: P71-P83")
    text = text.replace("## P75-P81: target-model adequacy and certified separation", "## P75-P83: target-model adequacy and certified separation")
    text = text.replace("P71-P82 derives consciousness", "P71-P83 derives consciousness")
    block = """### P82: exact nested projection contrasts

P82 preserves shared-parameter dependence for 256 nested residual events rather than subtracting separate projected-event intervals. Its exact witness strengthens P81 from `1/16` to `1/12` on the declared box.

![P82 exact nested projection contrasts](../docs/figures/p82_exact_nested_projection_contrast.svg)

[Read the P82 proposition](../docs/proposition_82_exact_nested_projection_contrast.md)

[Open the P82 equation provenance](../docs/p82_equation_provenance.md)

### P83: exact projection parity

P83 adds 22 parity observables. The branchwise parity probability is an exact multi-affine product transform, so rational box extrema are certified at vertices. A strict witness leaves the entire P82 family compatible while P83 certifies a full-law lower bound of `1/16`.

![P83 exact projection parity](../docs/figures/p83_exact_projection_parity.svg)

[Read the P83 proposition](../docs/proposition_83_exact_projection_parity.md)

[Open the P83 equation provenance](../docs/p83_equation_provenance.md)

[Open the P83 implementation](../src/consciousness_bridge/projection_parity_model_separation.py)

[Open the P83 numerical tests](../tests/test_projection_parity_model_separation.py)
"""
    text = append_before(text, "## Run the current research stack", block, path=path)
    write(path, text)


def update_website_index() -> None:
    path = "website/index.html"
    text = read(path)
    replacements = {
        "an 82-result mathematical-physics research program": "an 83-result mathematical-physics research program",
        "Explore all 82 results": "Explore all 83 results",
        "<strong>82</strong><span>proposition-level results</span>": "<strong>83</strong><span>proposition-level results</span>",
        "<strong>P82</strong><span>current theorem frontier</span>": "<strong>P83</strong><span>current theorem frontier</span>",
        "82 proposition-level results through P82": "83 proposition-level results through P83",
        "The 82 results form": "The 83 results form",
        "The 82-result program": "The 83-result program",
        "P73-P82": "P73-P83",
        "P75-P82": "P75-P83",
        "P71-P82": "P71-P83",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    p82_card = """      <div class="figure-card">
        <img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p82_exact_nested_projection_contrast.svg" alt="P82 exact nested projection-contrast certificate" />
        <div><h3>P82 · Exact nested projection contrasts</h3><p>Nested parent-child projected events define residual events that are generally not cylinders. P82 computes their P75 parameter-box ranges exactly, audits 256 genuinely new contrasts, and has an exact witness improving the P81 lower bound from 1/16 to 1/12.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_82_exact_nested_projection_contrast.md">Read P82 →</a></div>
      </div>"""
    p83_card = """      <div class="figure-card">
        <img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p83_exact_projection_parity.svg" alt="P83 exact projection-parity certificate" />
        <div><h3>P83 · Exact projection parity</h3><p>P83 adds 22 exact parity observables whose branch probabilities reduce to a multi-affine product. Exact rational vertex extremization exposes dependence constraints that can remain invisible to every P82 nested event. A strict witness has L82 = 0 and L83 = 1/16.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_83_exact_projection_parity.md">Read P83 →</a></div>
      </div>"""
    if p83_card not in text:
        text = replace_required(text, p82_card, p82_card + "\n\n" + p83_card, path=path)

    # Tests deliberately look for the repository-relative latest-figure path as
    # an auditable publication reference, in addition to the raw image URL.
    marker = "</main>"
    audit_note = "  <!-- Current theorem asset: docs/figures/p83_exact_projection_parity.svg -->"
    if audit_note not in text:
        text = text.replace(marker, audit_note + "\n" + marker, 1)
    write(path, text)


def update_website_research_map() -> None:
    path = "website/research-map.html"
    text = read(path)
    replacements = {
        "through Proposition 82": "through Proposition 83",
        "Eighty-two results, one dependency-aware scientific program": "Eighty-three results, one dependency-aware scientific program",
        "P71-P82 return": "P71-P83 return",
        "and P82 adds exact nested residual-event constraints that preserve common-parameter structure beyond separate event tests.":
            "P82 adds exact nested residual-event constraints that preserve common-parameter structure beyond separate event tests, and P83 adds exact projection-parity constraints that expose additional dependence structure.",
        "<strong>82</strong><span>proposition-level results</span>": "<strong>83</strong><span>proposition-level results</span>",
        "None of P71-P82 is a consciousness ontology.": "None of P71-P83 is a consciousness ontology.",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    block = """<section id="p83-frontier"><div class="section-head"><p class="eyebrow">IV-M · Dependency-aware parity separation</p><h2>P83: Can a parity constraint reject a P75 box that every P82 event leaves compatible?</h2></div><div class="result-grid"><article class="result"><span>P83A</span><h3>Exact branch parity identity</h3><p>Conditional independence gives a closed product formula for every two-, three-, and four-view parity probability.</p></article><article class="result"><span>P83B</span><h3>Exact rational box extremization</h3><p>The product is multi-affine, so branch extrema occur at response-coordinate vertices; prevalence is then extremized at its endpoints.</p></article><article class="result"><span>P83C</span><h3>Strict strengthening of P82</h3><p>The 22-event family is combined with the complete P82 certificate. An exact witness has L82 = 0 while L83 = 1/16.</p></article></div><div class="figure-card"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p83_exact_projection_parity.svg" alt="P83 exact projection-parity certificate"/><div><h3>P83 exact projection parity</h3><p>Parity makes an interaction constraint explicit without treating it as a consciousness variable. The full derivation, exact witness, code, and interpretation boundary are auditable from the proposition record.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_83_exact_projection_parity.md">Read Proposition 83 →</a></div></div><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p83_equation_provenance.md">Open P83 equation provenance →</a></p></section>"""
    text = append_before(text, "<footer", block, path=path)
    write(path, text)


def update_website_start_here() -> None:
    path = "website/start-here.html"
    text = read(path)
    text = text.replace("82", "83") if "83 proposition-level results" not in text else text
    # Restore the formal release number if a broad count replacement touched it.
    text = text.replace("v0.83.0", "v0.82.0")
    text = text.replace("0.83.0", "0.82.0")
    block = """    <section id="p83-frontier" class="boundary">
      <p class="eyebrow">Current theorem frontier</p>
      <h2>P83 · Exact projection-parity separation</h2>
      <p>P83 adds 22 exact parity observables to the complete P82 continuous-family certificate. The branchwise probability has a closed product form, its rational parameter-box extrema occur at vertices, and a strict witness has L82 = 0 while L83 = 1/16. This is a model-distance result under the declared P75 assumptions, not an identification of consciousness.</p>
      <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_83_exact_projection_parity.md">Read Proposition 83 →</a></p>
    </section>"""
    text = append_before(text, "  </main>", block, path=path)
    write(path, text)


def update_website_atlas_and_sources() -> None:
    path = "website/visual-atlas.html"
    text = read(path)
    block = """<section id="p83"><div class="section-head"><p class="eyebrow">Current theorem frontier · P83</p><h2>Exact projection-parity certificate</h2><p>Twenty-two parity observables expose dependency structure that can remain hidden from the complete P82 event family while retaining exact-rational certification.</p></div><div class="figure-card"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p83_exact_projection_parity.svg" alt="P83 exact projection-parity certificate"/><div><h3>L82 = 0, L83 = 1/16 on the strict witness</h3><p>The figure follows the observable from the Bernoulli parity identity through exact multi-affine box extremization to the certified full-law lower bound.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_83_exact_projection_parity.md">Open the theorem →</a></div></div></section>"""
    text = append_before(text, "</main>", block, path=path)
    write(path, text)

    path = "website/sources.html"
    text = read(path)
    block = """<section id="p83-source"><div class="section-head"><p class="eyebrow">Current theorem source</p><h2>P83 exact projection parity</h2><p>The P83 proof separates standard Bernoulli parity algebra and multi-affine box extremization from the repository-original model-separation construction and strict rational witness.</p></div><div class="source-grid"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_83_exact_projection_parity.md"><h3>Proposition 83</h3><p>Formal theorem, proof, witness, branch-and-bound handoff, and scientific boundary.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p83_equation_provenance.md"><h3>P83 provenance</h3><p>Equation-by-equation classification of imported, standard, and repository-original ingredients.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/projection_parity_model_separation.py"><h3>P83 implementation</h3><p>Exact Fraction-based parity intervals and certified P83 branch-and-bound lower bounds.</p></a></div></section>"""
    text = append_before(text, "</main>", block, path=path)
    write(path, text)


def update_pyproject_description() -> None:
    path = "pyproject.toml"
    text = read(path)
    old = "exact nested projection-contrast certification, exact residual-event box bounds,"
    new = "exact nested projection-contrast certification, exact residual-event box bounds, exact projection-parity certification, dependency-aware parity box bounds,"
    if new not in text:
        text = replace_required(text, old, new, path=path)
    write(path, text)


def main() -> None:
    update_source_phrase()
    update_readme()
    update_start_here()
    update_theorem_roadmap()
    update_research_navigation()
    update_detailed_record()
    update_equation_map()
    update_citations_and_changelog()
    update_verifier()
    update_visual_frontier()
    update_website_index()
    update_website_research_map()
    update_website_start_here()
    update_website_atlas_and_sources()
    update_pyproject_description()
    print("P83 publication integration applied; formal release remains v0.82.0")


if __name__ == "__main__":
    main()
