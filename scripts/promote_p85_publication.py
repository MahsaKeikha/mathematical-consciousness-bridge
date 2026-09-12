"""Synchronize the verified P85 theorem across public research surfaces.

This is an idempotent release-maintenance script used once to promote the
already-proved P85 result through reader documentation and the website. It does
not modify theorem code, theorem tests, or the formal package version.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PROOF = "proposition_85_exact_triple_projection_parity_functional.md"
PROVENANCE = "p85_equation_provenance.md"
FIGURE = "p85_exact_triple_projection_parity_functional.svg"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    if "\u2013" in text or "\u2014" in text:
        raise RuntimeError(f"forbidden dash character introduced in {path}")
    target = ROOT / path
    old = target.read_text(encoding="utf-8")
    if old != text:
        target.write_text(text, encoding="utf-8")
        print(f"updated {path}")


def replace(text: str, old: str, new: str) -> str:
    return text.replace(old, new)


def insert_after(text: str, marker: str, addition: str) -> str:
    if addition.strip() in text:
        return text
    if marker not in text:
        raise RuntimeError(f"promotion marker not found: {marker[:100]!r}")
    return text.replace(marker, marker + addition, 1)


def promote_readme() -> None:
    text = read("README.md")
    substitutions = {
        "the P1-P84 program map, and the current P84 frontier": "the P1-P85 program map, and the current P85 frontier",
        "| Public theorem frontier | **P84** |": "| Public theorem frontier | **P85** |",
        "| Proposition-level results | **84** |": "| Proposition-level results | **85** |",
        "Read the complete P1 to P84 detailed proposition record": "Read the complete P1 to P85 detailed proposition record",
        "P1 through P84 with explicit dependency branches": "P1 through P85 with explicit dependency branches",
        "P19-P24, P71-P84": "P19-P24, P71-P85",
        "P71-P84": "P71-P85",
        "P75-P84": "P75-P85",
        "84 proposition-level results": "85 proposition-level results",
        "The theorem frontier is P84.": "The theorem frontier is P85.",
        "Later P61-P70 and P71-P84": "Later P61-P70 and P71-P85",
    }
    for old, new in substitutions.items():
        text = replace(text, old, new)

    p84_caption = (
        "**P84 frontier figure.** P84 preserves the common parameter geometry of pairs of P83 parity events. "
        "The strict witness `L83 = 0 < L84 = 1/32` demonstrates a genuine strengthening while retaining the P78 mesh upper certificate and P79 one-sided finite-data rejection gate.\n"
    )
    p85_block = """

P85 asks whether pairwise silence can still hide a higher-order shared-parameter incompatibility. It keeps three distinct canonical even-parity observables tied to one P75 parameter assignment and audits 660 sign-normalized three-event functionals. Because each branch functional is multi-affine, its exact rational box range is obtained at common response-coordinate endpoints. A centered coefficient transfer then converts a functional interval gap into a full-law L-infinity lower bound. The exact regression witness has the complete `L84 = 0` certificate, empirical functional value `5/8`, exact P75 interval `[1,2]`, gap `3/8`, centered coefficient norm `12`, and therefore `L85 = 1/32`. This is a strict certificate improvement on that box, not a claim that the latent state is consciousness or that the physical-to-experiential bridge has been solved.

![P85 exact three-event projection-parity functional certificate](docs/figures/p85_exact_triple_projection_parity_functional.svg)

**P85 frontier figure.** P85 tests exact three-event shared-parameter compatibility beyond the complete P84 certificate. The displayed exact-rational witness gives `L84 = 0 < L85 = 1/32`. Read the [P85 proof](docs/proposition_85_exact_triple_projection_parity_functional.md) and [P85 equation provenance](docs/p85_equation_provenance.md) for the assumptions, derivation, executable audit, and interpretation boundary.
"""
    text = insert_after(text, p84_caption, p85_block)

    required = (
        "Public theorem frontier | **P85**",
        "Proposition-level results | **85**",
        "P1 through P85 with explicit dependency branches",
        "P19-P24, P71-P85",
        "85 proposition-level results",
        "The theorem frontier is P85.",
        FIGURE,
        PROOF,
        PROVENANCE,
    )
    for token in required:
        if token not in text:
            raise RuntimeError(f"README promotion missing {token!r}")
    write("README.md", text)


def promote_start_here() -> None:
    text = read("START_HERE.md")
    substitutions = {
        "84-result theorem": "85-result theorem",
        "84 proposition-level results": "85 proposition-level results",
        "P1-P84": "P1-P85",
        "P71-P84": "P71-P85",
        "current P84 frontier": "current P85 frontier",
        "current theorem frontier is P84": "current theorem frontier is P85",
        "through P84": "through P85",
    }
    for old, new in substitutions.items():
        text = replace(text, old, new)
    if "## Current frontier: P85" not in text:
        text += f"""

## Current frontier: P85

P85 is the current documented theorem frontier. It strengthens P84 by testing exact signed functionals of three distinct canonical even-parity observables under one shared P75 parameter assignment. The exact regression witness has the complete P84 lower bound equal to zero while P85 certifies a full-law L-infinity lower bound of `1/32`.

This remains a conditional model-separation result. The physical-to-experiential bridge itself remains open.

- [P85 proof](docs/{PROOF})
- [P85 equation provenance](docs/{PROVENANCE})
- [P85 source](src/consciousness_bridge/triple_projection_parity_functional_separation.py)
- [P85 tests](tests/test_triple_projection_parity_functional_separation.py)
- [P85 figure](docs/figures/{FIGURE})
"""
    required = ("85 proposition-level results", "P85", f"docs/{PROOF}", "physical-to-experiential bridge itself remains open")
    for token in required:
        if token not in text:
            raise RuntimeError(f"START_HERE promotion missing {token!r}")
    write("START_HERE.md", text)


def promote_navigation() -> None:
    text = read("docs/research_navigation.md")
    substitutions = {
        "The current documented theorem frontier is **P84**.": "The current documented theorem frontier is **P85**.",
        "The complete proposition record runs from **P1 through P84**.": "The complete proposition record runs from **P1 through P85**.",
        "P71-P84 form a target-side methodology branch": "P71-P85 form a target-side methodology branch",
        "dependency structure from P1 through P84": "dependency structure from P1 through P85",
        "The current theorem frontier is P84, but": "The current theorem frontier is P85, but",
        "**Current frontier provenance:** [P84 equation and provenance record](p84_equation_provenance.md).": "**Current frontier provenance:** [P85 equation and provenance record](p85_equation_provenance.md).",
    }
    for old, new in substitutions.items():
        text = replace(text, old, new)

    reading_marker = "35. [P84 equation and provenance record](p84_equation_provenance.md) for common-vertex joint parity contrasts, the 220-contrast family, the strict P84 > P83 witness, and the scientific interpretation boundary.\n"
    text = insert_after(
        text,
        reading_marker,
        "36. [P85 equation and provenance record](p85_equation_provenance.md) for exact three-event shared-parameter parity functionals, the 660-functional family, the strict P85 > P84 witness, and the scientific interpretation boundary.\n",
    )

    branch_marker = "| Joint projection-parity continuous target-model separation | P84 | Adds 220 exact coupled parity-event contrasts that preserve shared-parameter compatibility beyond separate P83 ranges | [P84](proposition_84_exact_projection_parity_contrast.md) |\n"
    text = insert_after(
        text,
        branch_marker,
        "| Three-event projection-parity functional separation | P85 | Adds 660 exact signed three-event parity functionals that test shared-parameter compatibility beyond the complete P84 pairwise certificate | [P85](proposition_85_exact_triple_projection_parity_functional.md) |\n",
    )

    index_marker = "| P84 | [Exact joint projection-parity contrast](proposition_84_exact_projection_parity_contrast.md) | exact shared-parameter parity-event contrast separation beyond the complete P83 scalar audit |\n"
    text = insert_after(
        text,
        index_marker,
        "| P85 | [Exact three-event projection-parity functional](proposition_85_exact_triple_projection_parity_functional.md) | exact three-event shared-parameter parity-functional separation beyond the complete P84 pairwise certificate |\n",
    )

    figure_marker = "| [P84 figure](figures/p84_exact_joint_projection_parity_contrast.svg) | current frontier: exact shared-parameter parity-event contrast certification with the strict L83 = 0, L84 = 1/32 witness |\n"
    if figure_marker in text:
        text = text.replace(
            figure_marker,
            "| [P84 figure](figures/p84_exact_joint_projection_parity_contrast.svg) | previous frontier: exact shared-parameter pairwise parity-event contrast certification |\n"
            "| [P85 figure](figures/p85_exact_triple_projection_parity_functional.svg) | current frontier: exact three-event shared-parameter parity-functional certification with the strict L84 = 0, L85 = 1/32 witness |\n",
            1,
        )

    frontier_marker = "| P84 | exact joint parity-event shared-parameter constraints | [P84](proposition_84_exact_projection_parity_contrast.md) |\n"
    text = insert_after(
        text,
        frontier_marker,
        "| P85 | exact three-event parity-functional shared-parameter constraints | [P85](proposition_85_exact_triple_projection_parity_functional.md) |\n",
    )

    if "20. [P84 exact joint projection-parity separation]" in text and "[P85 exact three-event projection-parity functional]" not in text:
        marker = "20. [P84 exact joint projection-parity separation](proposition_84_exact_projection_parity_contrast.md) for the stronger shared-parameter question: whether two individually compatible P83 parity observations can be realized simultaneously. It covers 220 exact coupled contrasts, P84 >= P83 dominance, and the strict `L83 = 0 < L84 = 1/32` witness.\n"
        text = insert_after(
            text,
            marker,
            "21. [P85 exact three-event projection-parity functional](proposition_85_exact_triple_projection_parity_functional.md) for the next shared-parameter question: whether the complete P84 pairwise certificate can remain silent while a three-event relation is incompatible. It covers 660 exact sign-normalized functionals, P85 >= P84 dominance, and the strict `L84 = 0 < L85 = 1/32` witness.\n",
        )

    required = (
        "current documented theorem frontier is **P85**",
        "P71-P85",
        "| P85 |",
        PROOF,
        PROVENANCE,
    )
    for token in required:
        if token not in text:
            raise RuntimeError(f"navigation promotion missing {token!r}")
    write("docs/research_navigation.md", text)


def promote_roadmap() -> None:
    text = read("docs/theorem_roadmap.md")
    substitutions = {
        "The current documented theorem frontier is **P84**.": "The current documented theorem frontier is **P85**.",
        "P1 through P84 with explicit dependency branches": "P1 through P85 with explicit dependency branches",
        "P71-P84 return": "P71-P85 return",
        "P71-P84": "P71-P85",
        "## After P84": "## After P85",
        "After P84": "After P85",
    }
    for old, new in substitutions.items():
        text = replace(text, old, new)

    dep_marker = "&\\text{P84: joint parity contrasts test shared-parameter compatibility across P83 observables}\n"
    if dep_marker in text and "P85: three-event parity functionals" not in text:
        text = text.replace(
            dep_marker,
            dep_marker + "&\\Downarrow\\\\\n&\\text{P85: three-event parity functionals test compatibility beyond the complete P84 pairwise certificate}\n",
            1,
        )

    if "### P85: exact three-event projection-parity functional" not in text:
        before = "## After P85"
        section = f"""
### P85: exact three-event projection-parity functional

P85 keeps three distinct canonical even-parity observables tied to one shared P75 parameter assignment. Across the eleven canonical even-parity events it audits 660 sign-normalized three-event functionals. Multi-affinity makes every branch box range exact at common endpoint vertices, and the final prevalence mixture is affine.

For coefficient function `g(x)`, subtracting a constant does not change the functional difference between probability laws. P85 therefore uses the exact centered norm

\\[
D(T)=\\min_c\\sum_x |g(x)-c|
\\]

to transfer an empirical functional gap into a full-law L-infinity lower bound. The exact strict witness has `L84 = 0`, empirical functional `5/8`, exact P75 range `[1,2]`, gap `3/8`, centered norm `12`, and therefore `L85 = 1/32`.

![P85 exact three-event projection-parity functional](figures/{FIGURE})

Direct proof: [P85]({PROOF}). Provenance: [P85 equation record]({PROVENANCE}). Implementation: [`triple_projection_parity_functional_separation.py`](../src/consciousness_bridge/triple_projection_parity_functional_separation.py). Tests: [`test_triple_projection_parity_functional_separation.py`](../tests/test_triple_projection_parity_functional_separation.py).

P85 is a conditional model-separation theorem for the declared P75 family. It does not identify the latent state with consciousness, validate an alternative model, establish nonphysicality, or close the physical-to-experiential bridge.

"""
        if before not in text:
            raise RuntimeError("roadmap After P85 marker missing")
        text = text.replace(before, section + before, 1)

    required = (
        "current documented theorem frontier is **P85**",
        "P71-P85",
        f"[P85]({PROOF})",
        PROVENANCE,
        "After P85",
    )
    for token in required:
        if token not in text:
            raise RuntimeError(f"roadmap promotion missing {token!r}")
    write("docs/theorem_roadmap.md", text)


def promote_detailed_record() -> None:
    text = read("docs/detailed_proposition_record.md")
    text = replace(text, "## Complete P1 to P84 chronology", "## Complete P1 to P85 chronology")
    if "## Proposition P85" not in text:
        text += f"""

## Proposition P85 - Exact three-event projection-parity functional certificate

**P85** strengthens P84 for the same declared P75 four-view binary latent family. It asks whether three canonical even-parity observables can be compatible with one shared parameter assignment even when the complete P84 pairwise certificate is silent. The standard family contains 660 sign-normalized three-event functionals. Exact multi-affine endpoint evaluation gives each functional's P75 box interval, and an exact centered coefficient norm transfers interval mismatch to a full-law L-infinity lower bound.

The exact regression witness has `L84 = 0`, empirical functional value `5/8`, exact P75 interval `[1,2]`, gap `3/8`, centered coefficient norm `12`, and `L85 = 1/32`. Thus P85 is strictly stronger than P84 on that box. This remains a conditional model-separation certificate; it does not identify a latent state with consciousness or close the physical-to-experiential bridge.

- Proof: [Proposition 85]({PROOF})
- Provenance: [P85 equation and provenance record]({PROVENANCE})
- Figure: [P85 exact three-event projection-parity functional](figures/{FIGURE})
- Implementation: [`triple_projection_parity_functional_separation.py`](../src/consciousness_bridge/triple_projection_parity_functional_separation.py)
- Tests: [`test_triple_projection_parity_functional_separation.py`](../tests/test_triple_projection_parity_functional_separation.py)
"""
    if "Complete P1 to P85 chronology" not in text:
        raise RuntimeError("detailed chronology was not promoted")
    write("docs/detailed_proposition_record.md", text)


def promote_figure_catalog() -> None:
    text = read("docs/figure_catalog.md")
    link = f"(figures/{FIGURE})"
    if link not in text:
        text += f"""

## P85 exact three-event projection-parity functional certificate

[Open the full SVG](figures/{FIGURE})

**What it shows and how to interpret it.** The figure shows why compatibility checks on one parity observable and on all P84 pairs can still be silent while a signed relation among three observables is incompatible with every shared P75 parameter assignment in the declared box. Read left to right from the lower-order limitation, through the exact three-event functional and common-vertex interval, to the exact-rational strict witness. The witness has `L84 = 0`, functional gap `3/8`, centered coefficient norm `12`, and `L85 = 1/32`.

**Scientific status.** This is the visual companion to Proposition 85. It is a conditional exact model-separation result for the declared P75 family, not empirical consciousness evidence, not a proof of nonphysicality, and not a solution of the physical-to-experiential bridge.
"""
    if link not in text:
        raise RuntimeError("P85 figure catalog link missing")
    write("docs/figure_catalog.md", text)


def promote_citations() -> None:
    cff = read("CITATION.cff")
    cff = replace(cff, "Current documented theorem frontier: P84", "Current documented theorem frontier: P85")
    write("CITATION.cff", cff)

    guide = read("CITATION.md")
    if "P85" not in guide:
        guide += f"""

## Current theorem frontier: P85

The current documented theorem frontier is **P85**, the exact three-event projection-parity functional certificate. When citing this frontier result specifically, cite [Proposition 85](docs/{PROOF}) together with its [equation and provenance record](docs/{PROVENANCE}), implementation, tests, and exact theorem figure. P85 is conditional on the declared P75 model and does not claim that the physical-to-experiential bridge has been solved.
"""
    else:
        guide = replace(guide, "current documented theorem frontier is P84", "current documented theorem frontier is P85")
    if "P85" not in guide:
        raise RuntimeError("citation guide was not promoted")
    write("CITATION.md", guide)


def promote_equation_map() -> None:
    path = "docs/equation_and_citation_map.md"
    text = read(path)
    if "## P85" not in text and PROOF not in text:
        text += f"""

## P85 - Exact three-event projection-parity functional certificate

**New repository result.** P85 strengthens the P84 pairwise parity audit by retaining one shared P75 parameter assignment across three canonical even-parity observables. The exact branch range follows from multi-affinity and common endpoint evaluation. The full-law transfer uses the standard centered finite-dimensional norm inequality, with the exact coefficient center chosen by median absolute-deviation minimization.

The standard audit contains 660 sign-normalized functionals. The exact strict witness has `L84 = 0 < L85 = 1/32`. See [Proposition 85]({PROOF}), [P85 equation provenance]({PROVENANCE}), and the [P85 theorem figure](figures/{FIGURE}).

**Boundary:** this is a conditional adequacy/model-separation result for the declared P75 family. It neither identifies the latent state with consciousness nor closes the physical-to-experiential bridge.
"""
    write(path, text)


def p85_homepage_section() -> str:
    return f"""<section id=\"p84\" class=\"theorem-frontier\">
  <div class=\"section-head\">
    <p class=\"eyebrow\">Previous theorem frontier · P84</p>
    <h2>P84: pairwise shared-parameter parity compatibility</h2>
    <p>P84 keeps two P83 parity observables tied to one shared P75 parameter assignment. Its strict witness established that separate scalar compatibility does not imply pairwise shared-parameter compatibility.</p>
  </div>
  <div class=\"theorem-figure-shell\">
    <a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p84_exact_joint_projection_parity_contrast.svg\"><img src=\"https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p84_exact_joint_projection_parity_contrast.svg\" alt=\"P84 exact joint projection-parity contrast certificate\" /></a>
  </div>
</section>

<section id=\"p85-frontier\" class=\"theorem-frontier\">
  <div class=\"section-head\">
    <p class=\"eyebrow\">Current theorem frontier · P85</p>
    <h2>P85 in plain language: three measurements can reveal a conflict that every pairwise certificate misses</h2>
    <p>P85 asks whether three parity-based observations can all come from one shared setting of the declared P75 model. Even when the complete P84 pairwise certificate is silent, the three observations can still impose a relation that no allowed shared parameter choice can satisfy.</p>
  </div>
  <div class=\"theorem-figure-shell\">
    <a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/{FIGURE}\" aria-label=\"Open the full P85 theorem figure\"><img src=\"https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/{FIGURE}?v=1\" alt=\"P85 exact three-event shared-parameter parity certificate\" /></a>
  </div>
  <div class=\"frontier-summary-grid\">
    <article class=\"result\"><span>660</span><h3>Exact three-event functionals</h3><p>P85 audits all sign-normalized triples from the eleven canonical even-parity events.</p></article>
    <article class=\"result\"><span>Exact</span><h3>Common-parameter box ranges</h3><p>Multi-affinity means branch extrema occur at shared response-coordinate endpoints; prevalence is then extremized at its endpoints.</p></article>
    <article class=\"result\"><span>1/32</span><h3>Strict certified separation</h3><p>The exact witness has P84 lower bound 0, empirical functional 5/8, P75 interval [1,2], gap 3/8, and centered coefficient norm 12.</p></article>
  </div>
  <div class=\"two-col\">
    <div><h3>What it adds</h3><p>P85 retains everything in P84 and adds exact three-event shared-parameter constraints. On the repository witness, this raises the certified lower bound from zero to 1/32.</p></div>
    <aside class=\"card\"><h3>What it does not claim</h3><p>P85 tests one declared latent measurement family. It does not identify the latent state with consciousness, prove consciousness is nonphysical, validate an alternative model, or solve the physical-to-experiential bridge.</p></aside>
  </div>
  <p><a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF}\">Read Proposition 85</a> · <a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROVENANCE}\">Equation provenance</a> · <a href=\"implementation.html\">Implementation path</a></p>
</section>"""


def promote_homepage() -> None:
    path = "website/index.html"
    text = read(path)
    substitutions = {
        "Explore all 84 results": "Explore all 85 results",
        "<strong>84</strong><span>proposition-level results</span>": "<strong>85</strong><span>proposition-level results</span>",
        "<strong>P84</strong><span>current theorem frontier</span>": "<strong>P85</strong><span>current theorem frontier</span>",
        "Current record:</strong> 84 proposition-level results through P84": "Current record:</strong> 85 proposition-level results through P85",
        "P73-P84 progressively": "P73-P85 progressively",
        "The 84-result program": "The 85-result program",
        "P75-P84": "P75-P85",
        "P71-P84:": "P71-P85:",
    }
    for old, new in substitutions.items():
        text = replace(text, old, new)

    pattern = re.compile(r'<section id="p84-frontier" class="theorem-frontier">.*?</section>', re.DOTALL)
    if pattern.search(text):
        text = pattern.sub(p85_homepage_section(), text, count=1)
    elif "id=\"p85-frontier\"" not in text:
        raise RuntimeError("homepage P84 frontier section not found")

    required = (
        "Explore all 85 results",
        "<strong>85</strong><span>proposition-level results</span>",
        "<strong>P85</strong><span>current theorem frontier</span>",
        "The 85-result program",
        "P75-P85",
        "P71-P85:",
        FIGURE,
        PROOF,
    )
    for token in required:
        if token not in text:
            raise RuntimeError(f"homepage promotion missing {token!r}")
    if "The 84-result program" in text:
        raise RuntimeError("stale homepage program count remains")
    write(path, text)


def promote_visual_atlas() -> None:
    path = "website/visual-atlas.html"
    text = read(path)
    pattern = re.compile(r'<section id="p84-frontier" class="theorem-frontier">.*?</section>', re.DOTALL)
    if pattern.search(text):
        replacement = f"""<section id=\"p84\"><div class=\"section-head\"><p class=\"eyebrow\">Previous theorem frontier · P84</p><h2>Exact pairwise shared-parameter parity certificate</h2></div><div class=\"figure-card\"><img loading=\"lazy\" decoding=\"async\" src=\"https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p84_exact_joint_projection_parity_contrast.svg\" alt=\"P84 exact joint projection-parity contrast certificate\"/><div><h3>P84: pairwise coupling</h3><p>P84 tests two parity observables under one shared P75 parameter assignment and remains part of the certificate hierarchy.</p></div></div></section>
<section id=\"p85-frontier\" class=\"theorem-frontier\"><div class=\"section-head\"><p class=\"eyebrow\">Current theorem frontier · P85</p><h2>Exact three-event shared-parameter parity certificate</h2><p>P85 adds 660 exact sign-normalized three-event functionals. The strict exact-rational witness has the complete P84 lower bound zero while P85 certifies 1/32.</p></div><div class=\"theorem-figure-shell\"><a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/{FIGURE}\"><img loading=\"lazy\" decoding=\"async\" src=\"https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/{FIGURE}\" alt=\"P85 exact three-event projection-parity functional certificate\"/></a></div><div class=\"boundary\"><p><strong>Scientific boundary:</strong> P85 is a conditional exact model-separation result for the declared P75 family. It does not identify consciousness or close the physical-to-experiential bridge.</p></div><p><a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF}\">Open the theorem</a> · <a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROVENANCE}\">Equation provenance</a></p></section>"""
        text = pattern.sub(replacement, text, count=1)
    elif "Current theorem frontier · P85" not in text:
        raise RuntimeError("visual atlas P84 frontier section not found")

    if text.count("Current theorem frontier") != 1:
        raise RuntimeError("visual atlas must have exactly one current frontier label")
    if "Current theorem frontier · P84" in text:
        raise RuntimeError("stale P84 current frontier remains in atlas")
    for token in ("Current theorem frontier · P85", FIGURE):
        if token not in text:
            raise RuntimeError(f"visual atlas promotion missing {token!r}")
    write(path, text)


def promote_website_start() -> None:
    path = "website/start-here.html"
    text = read(path)
    substitutions = {
        "84-result": "85-result",
        "84 proposition-level": "85 proposition-level",
        "P1-P84": "P1-P85",
        "P71-P84": "P71-P85",
        "P77-P84": "P77-P85",
        "current P84 frontier": "current P85 frontier",
    }
    for old, new in substitutions.items():
        text = replace(text, old, new)
    if "P85 exact three-event" not in text:
        marker = "</main>"
        addition = f"""<section class=\"theorem-frontier\"><div class=\"section-head\"><p class=\"eyebrow\">Current frontier · P85</p><h2>P85 exact three-event shared-parameter certificate</h2><p>P85 asks whether three canonical parity observations can share one P75 parameter assignment when lower-order certificates remain silent. The exact witness gives P84 = 0 and P85 = 1/32.</p></div><p>This is a conditional model-separation theorem and does not claim that consciousness has been derived from physics. The physical-to-experiential bridge remains open.</p><p><a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF}\">Read P85</a> · <a href=\"visual-atlas.html\">Visual Atlas</a> · <a href=\"research-map.html\">Research Map</a></p></section>\n"""
        if marker not in text:
            raise RuntimeError("website start page main close not found")
        text = text.replace(marker, addition + marker, 1)
    for token in ("85", "P85", "v0.82.0", "physical-to-experiential bridge", "does not claim that consciousness has been derived from physics", "research-map.html", "visual-atlas.html"):
        if token not in text:
            raise RuntimeError(f"website start page promotion missing {token!r}")
    write(path, text)


def promote_research_map() -> None:
    path = "website/research-map.html"
    text = read(path)
    text = replace(text, "P71-P84", "P71-P85")
    text = replace(text, "P77-P84", "P77-P85")
    if "P85" not in text:
        marker = "</main>"
        addition = f"""<section><div class=\"section-head\"><p class=\"eyebrow\">Current frontier · P85</p><h2>Three-event shared-parameter parity functionals</h2><p>P85 strengthens the P84 pairwise certificate by testing 660 exact signed three-event functionals under one shared P75 parameter assignment. Its exact witness has L84 = 0 and L85 = 1/32.</p></div><div class=\"figure-card\"><img src=\"https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/{FIGURE}\" alt=\"P85 exact three-event projection-parity functional certificate\"/><div><p><a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF}\">P85 proof</a></p></div></div></section>\n"""
        if marker not in text:
            raise RuntimeError("research map main close not found")
        text = text.replace(marker, addition + marker, 1)
    if "P85" not in text:
        raise RuntimeError("research map does not contain P85")
    write(path, text)


def promote_implementation() -> None:
    path = "website/implementation.html"
    text = read(path)
    text = replace(text, "P77-P84", "P77-P85")
    if "triple_projection_parity_functional_separation.py" not in text:
        marker = "</main>"
        addition = f"""<section><div class=\"section-head\"><p class=\"eyebrow\">P85 executable frontier</p><h2>Exact three-event parity-functional separation</h2><p>The authoritative implementation enumerates the 660 standard sign-normalized triple functionals, computes exact rational P75 box intervals by shared endpoint evaluation, uses the exact centered coefficient norm for L-infinity transfer, and combines the result with P84.</p></div><p><a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/triple_projection_parity_functional_separation.py\">Source</a> · <a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_triple_projection_parity_functional_separation.py\">Tests</a> · <a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF}\">Proof</a></p></section>\n"""
        if marker not in text:
            raise RuntimeError("implementation main close not found")
        text = text.replace(marker, addition + marker, 1)
    if "P77-P85" not in text:
        raise RuntimeError("implementation frontier range missing")
    write(path, text)


def promote_misc() -> None:
    figures_readme = read("docs/figures/README.md")
    if FIGURE not in figures_readme:
        figures_readme += f"\n- `{FIGURE}` - P85 exact three-event shared-parameter parity-functional certificate; conditional on the declared P75 family.\n"
    write("docs/figures/README.md", figures_readme)

    changelog = read("CHANGELOG.md")
    if "P85 exact three-event projection-parity functional certificate" not in changelog:
        marker = "# Changelog\n"
        addition = "\n## Unreleased - P85 frontier synchronization\n\n- Promoted the verified P85 exact three-event projection-parity functional certificate across proof provenance, reader navigation, figures, citation metadata, and the public website.\n- Recorded the exact strict witness `L84 = 0 < L85 = 1/32` while preserving the explicit boundary that the physical-to-experiential bridge remains open.\n"
        if marker in changelog:
            changelog = changelog.replace(marker, marker + addition, 1)
        else:
            changelog = addition + changelog
    write("CHANGELOG.md", changelog)


def main() -> None:
    promote_readme()
    promote_start_here()
    promote_navigation()
    promote_roadmap()
    promote_detailed_record()
    promote_figure_catalog()
    promote_citations()
    promote_equation_map()
    promote_homepage()
    promote_visual_atlas()
    promote_website_start()
    promote_research_map()
    promote_implementation()
    promote_misc()
    print("P85 publication surfaces synchronized")


if __name__ == "__main__":
    main()
