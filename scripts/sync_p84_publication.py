"""One-shot synchronization of P84 reader, citation, website, and audit surfaces."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_if_present(text: str, old: str, new: str) -> str:
    if old in text:
        return text.replace(old, new)
    return text


def insert_before_once(text: str, marker: str, addition: str, *, path: str) -> str:
    if addition.strip() in text:
        return text
    count = text.count(marker)
    if count != 1:
        raise RuntimeError(f"expected one marker in {path}, found {count}: {marker[:100]!r}")
    return text.replace(marker, addition + marker, 1)


def insert_after_line(text: str, prefix: str, addition: str, *, path: str) -> str:
    if addition.strip() in text:
        return text
    lines = text.splitlines()
    indices = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    if not indices:
        raise RuntimeError(f"missing line prefix in {path}: {prefix!r}")
    index = indices[-1]
    lines[index + 1:index + 1] = addition.rstrip("\n").splitlines()
    return "\n".join(lines) + "\n"


def sync_readme() -> None:
    path = "README.md"
    text = read(path)
    replacements = (
        ("P1-P83 program map, and the current P83 frontier", "P1-P84 program map, and the current P84 frontier"),
        ("| Public theorem frontier | **P83** |", "| Public theorem frontier | **P84** |"),
        ("| Proposition-level results | **83** |", "| Proposition-level results | **84** |"),
        ("Read the complete P1 to P83 detailed proposition record", "Read the complete P1 to P84 detailed proposition record"),
        ("83 proposition-level results", "84 proposition-level results"),
        ("The theorem frontier is P83.", "The theorem frontier is P84."),
        ("## Current theorem frontier: P83", "## Current theorem frontier: P84"),
        ("P71-P83", "P71-P84"),
        ("P75-P83", "P75-P84"),
        ("P74-P83", "P74-P84"),
    )
    for old, new in replacements:
        text = replace_if_present(text, old, new)

    p84_block = """
P84 asks whether two parity characters can each remain separately compatible while their shared P75 parameter relation is already impossible. It uses the 15 nonconstant Walsh characters on four binary views and both signs for each unordered pair, giving 210 predeclared signed pairwise contrasts. Each branch expectation is a sum of two Walsh products and is therefore multi-affine in the shared response coordinates; its rational parameter-box range is exact by endpoint evaluation, and prevalence is then extremized exactly at its endpoints. The empirical contrast mismatch transfers to full-law L-infinity distance through the discrete L1 norm. An exact-rational witness keeps the complete P82 and P83 certificates at zero while `chi_{1,2} - chi_{1,3}` is forced to zero by the P75 box and has empirical expectation `3/16`; with contrast L1 norm 16, P84 certifies `3/256`. P84 is a strict dependency-aware model-distance strengthening on that witness, not an identification of consciousness.

![P84 exact pairwise Walsh-contrast certificate](docs/figures/p84_exact_pairwise_walsh_contrast.svg)

**P84 frontier figure.** P84 audits 210 exact signed Walsh contrasts while retaining the complete P83 certificate. The figure shows the branchwise Walsh-product identity, exact shared-parameter box extremization, the observable-to-L-infinity transfer, and the strict exact-rational witness with `L82 = L83 = 0` and `L84 = 3/256`. The physical-to-experiential bridge remains open.

"""
    if "docs/figures/p84_exact_pairwise_walsh_contrast.svg" not in text:
        marker = "Only after the physical description, the target, and the way the target is measured are all scientifically defensible"
        text = insert_before_once(text, marker, p84_block, path=path)
    write(path, text)


def sync_start_here() -> None:
    path = "START_HERE.md"
    text = read(path)
    replacements = (
        ("the 83-result theorem program", "the 84-result theorem program"),
        ("83 proposition-level results", "84 proposition-level results"),
        ("current theorem frontier is **P83**", "current theorem frontier is **P84**"),
        ("P75-P83", "P75-P84"),
        ("P71-P83", "P71-P84"),
        ("P74-P83", "P74-P84"),
        ("## The 83 results", "## The 84 results"),
        ("**P75-P83**", "**P75-P84**"),
        ("## The current frontier: P71-P83", "## The current frontier: P71-P84"),
        ("P75-P83 model", "P75-P84 model"),
        ("\\(L_{78},L_{80},L_{81},L_{82},L_{83}\\)", "\\(L_{78},L_{80},L_{81},L_{82},L_{83},L_{84}\\)"),
        ("**Proposition frontier:** P83", "**Proposition frontier:** P84"),
        ("**Proposition-level results:** 83", "**Proposition-level results:** 84"),
    )
    for old, new in replacements:
        text = replace_if_present(text, old, new)

    p84_plain = """**P84: exact pairwise Walsh contrasts.** P84 keeps shared P75 response-parameter dependence across two Walsh parity characters instead of certifying the characters separately. It audits 210 signed pairwise contrasts with exact rational box ranges. A strict witness has `L82 = L83 = 0` but `L84 = 3/256`, showing that a cross-character relation can expose incompatibility that every predeclared P83 parity test leaves individually compatible.

"""
    marker = "---\n\n## How to read any theorem in this repository"
    if p84_plain.strip() not in text:
        text = insert_before_once(text, marker, p84_plain, path=path)

    final_heading = "## Current theorem frontier: P83"
    if final_heading in text:
        index = text.rfind(final_heading)
        text = text[:index] + """## Current theorem frontier: P84

[P84: Exact Pairwise Walsh-Contrast Certificate](docs/proposition_84_exact_pairwise_walsh_contrast.md) strengthens the complete P83 lower bound with 210 exact signed pairwise Walsh contrasts. Its strict witness has `L82 = L83 = 0` and `L84 = 3/256`. The theorem remains a conditional model-distance certificate and does not identify any latent state with consciousness.
"""
    write(path, text)


def sync_changelog() -> None:
    path = "CHANGELOG.md"
    text = read(path)
    marker = "# Unreleased research frontier - P83\n\n"
    if "# Unreleased research frontier - P84" not in text:
        if marker not in text:
            raise RuntimeError("P83 unreleased changelog heading not found")
        p84 = """# Unreleased research frontier - P84

- Added Proposition 84, Exact Pairwise Walsh-Contrast Certificate for Continuous P75 Separation.
- Added all 15 nonconstant four-bit Walsh characters and 210 predeclared signed pairwise contrasts.
- Derived exact branchwise contrast ranges by multi-affine vertex evaluation over shared P75 response coordinates and exact affine prevalence extremization.
- Defined `L84(B) = max(L83(B), L_Walsh(B))`, so P84 is never weaker than P83 on the same box.
- Added an exact-rational strict witness with `L82(B)=L83(B)=0` and `L84(B)=3/256` from `chi_{1,2} - chi_{1,3}`.
- Added exact implementation, regression tests, proof, equation provenance, theorem figure, visual navigation, citation guidance, and website integration.
- Kept v0.82.0 as the latest formal release while P84 is under review; release version and theorem frontier remain explicitly distinct.
- Preserved the P78 mesh-width upper certificate, P79 one-sided rejection gate, and the boundary that the physical-to-experiential bridge remains open.

## P83 merged theorem frontier

"""
        text = text.replace(marker, p84, 1)
    write(path, text)


def sync_citations() -> None:
    path = "CITATION.cff"
    text = read(path)
    p83_sentence = (
        "Proposition 83 adds 22 exact projection-parity observables whose branch probabilities have a closed multi-affine product form, "
        "yielding an exact-rational never-weaker certificate and a strict witness with P82 equal to zero while P83 equals one sixteenth. "
    )
    p84_sentence = (
        "Proposition 84 adds 210 signed pairwise Walsh contrasts that retain shared response-parameter dependence across two parity characters, "
        "with exact multi-affine rational box ranges and a strict witness for which P82 and P83 are zero while P84 equals three over 256. "
    )
    if p84_sentence not in text:
        if p83_sentence not in text:
            raise RuntimeError("P83 citation abstract anchor not found")
        text = text.replace(p83_sentence, p83_sentence + p84_sentence, 1)
    text = text.replace("Current documented theorem frontier: P83.", "Current documented theorem frontier: P84.")
    text = text.replace("current documented theorem frontier: P83.", "current documented theorem frontier: P84.")
    write(path, text)

    path = "CITATION.md"
    text = read(path)
    if "## Proposition 84 method citation" not in text:
        text += """

## Proposition 84 method citation

For work that specifically uses the newest dependency-aware continuous-family certificate, cite the program together with **Proposition 84: Exact Pairwise Walsh-Contrast Certificate for Continuous P75 Separation**. P84 adds 210 signed pairwise Walsh contrasts, exact rational box extremization over shared response coordinates, and a strict witness with `L82 = L83 = 0 < L84 = 3/256`.

The result is a conditional model-distance certificate for the declared P75 latent family. It should not be cited as an identification, definition, or measurement of consciousness, and non-rejection remains inconclusive.
"""
    write(path, text)


def sync_verifier() -> None:
    path = "scripts/verify_repository.py"
    text = read(path)
    text = text.replace('CURRENT_FRONTIER = "P83"', 'CURRENT_FRONTIER = "P84"')
    text = text.replace("for number in range(1, 84):", "for number in range(1, 85):")
    write(path, text)


def sync_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    replacements = (
        ("current documented theorem frontier is **P83**", "current documented theorem frontier is **P84**"),
        ("complete proposition record runs from **P1 through P83**", "complete proposition record runs from **P1 through P84**"),
        ("P71-P83 form", "P71-P84 form"),
        ("from P1 through P83.", "from P1 through P84."),
    )
    for old, new in replacements:
        text = replace_if_present(text, old, new)

    if "[P84 exact pairwise Walsh-contrast separation]" not in text:
        lines = text.splitlines()
        target = next(i for i, line in enumerate(lines) if "[P83 exact projection-parity separation]" in line)
        lines.insert(
            target + 1,
            "20. [P84 exact pairwise Walsh-contrast separation](proposition_84_exact_pairwise_walsh_contrast.md) for the 210-contrast audit, exact shared-parameter multi-affine box intervals, P84 >= P83 dominance, and the strict `3/256` versus zero witness.",
        )
        start = lines.index("## Recommended reading order") + 1
        end = lines.index("## Scientific branch map")
        counter = 1
        for i in range(start, end):
            if re.match(r"^\d+\. ", lines[i]):
                lines[i] = re.sub(r"^\d+\. ", f"{counter}. ", lines[i])
                counter += 1
        text = "\n".join(lines) + "\n"

    p84_branch = "| Pairwise Walsh-contrast continuous target-model separation | P84 | Adds 210 exact signed two-character contrasts that preserve shared P75 response-parameter dependence beyond separate P83 parity intervals | [P84](proposition_84_exact_pairwise_walsh_contrast.md) |"
    text = insert_after_line(
        text,
        "| Projection-parity continuous target-model separation | P83 |",
        p84_branch,
        path=path,
    )

    p84_index = "| P84 | [Exact pairwise Walsh-contrast model separation](proposition_84_exact_pairwise_walsh_contrast.md) | exact dependency-aware signed-Walsh lower certificate with strict P84 > P83 witness |"
    text = insert_after_line(text, "| P83 |", p84_index, path=path)

    if "[P84 equation and provenance record]" not in text:
        marker = "## Scientific branch map"
        addition = "34. [P84 equation and provenance record](p84_equation_provenance.md) for Walsh identities, multi-affine exactness, the `3/256` strict witness, and the scientific interpretation boundary.\n\n"
        text = insert_before_once(text, marker, addition, path=path)
        # Renumber the recommended list again after the provenance insertion.
        lines = text.splitlines()
        start = lines.index("## Recommended reading order") + 1
        end = lines.index("## Scientific branch map")
        counter = 1
        for i in range(start, end):
            if re.match(r"^\d+\. ", lines[i]):
                lines[i] = re.sub(r"^\d+\. ", f"{counter}. ", lines[i])
                counter += 1
        text = "\n".join(lines) + "\n"
    write(path, text)


def sync_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    for old, new in (
        ("P1-P83", "P1-P84"),
        ("P1 through P83", "P1 through P84"),
        ("P71-P83", "P71-P84"),
        ("P75-P83", "P75-P84"),
        ("current theorem frontier is P83", "current theorem frontier is P84"),
        ("current theorem frontier is **P83**", "current theorem frontier is **P84**"),
    ):
        text = replace_if_present(text, old, new)
    p84_row = "| P84 | Exact pairwise Walsh-contrast model separation | P75, P78-P83 | exact 210-member signed-Walsh box certificate, P84 >= P83, strict `3/256` versus zero witness | [proof](proposition_84_exact_pairwise_walsh_contrast.md) |"
    if p84_row not in text:
        lines = text.splitlines()
        candidates = [i for i, line in enumerate(lines) if line.startswith("| P83 |")]
        if candidates:
            lines.insert(candidates[-1] + 1, p84_row)
            text = "\n".join(lines) + "\n"
    if "## P84 current frontier" not in text:
        text += """

## P84 current frontier

**Exact Pairwise Walsh-Contrast Certificate for Continuous P75 Separation.** P84 retains the complete P83 lower certificate and adds 210 signed pairwise Walsh contrasts. Their branch expectations are multi-affine in shared P75 response coordinates, so rational parameter-box ranges are exact by vertex evaluation. A strict exact-rational witness has `L82 = L83 = 0` and `L84 = 3/256`.

Audit paths: [proof](proposition_84_exact_pairwise_walsh_contrast.md), [equation provenance](p84_equation_provenance.md), [implementation](../src/consciousness_bridge/walsh_contrast_model_separation.py), [tests](../tests/test_walsh_contrast_model_separation.py), and [theorem figure](figures/p84_exact_pairwise_walsh_contrast.svg).

P84 is a conditional model-distance theorem. It does not identify a latent state with consciousness, and the physical-to-experiential bridge remains open.
"""
    write(path, text)


def sync_detailed_record() -> None:
    path = "docs/detailed_proposition_record.md"
    text = read(path)
    for old, new in (
        ("P1-P83", "P1-P84"),
        ("P1 through P83", "P1 through P84"),
        ("83 proposition-level results", "84 proposition-level results"),
        ("current theorem frontier is P83", "current theorem frontier is P84"),
        ("current theorem frontier is **P83**", "current theorem frontier is **P84**"),
    ):
        text = replace_if_present(text, old, new)
    if "## Proposition 84" not in text:
        text += """

## Proposition 84: Exact Pairwise Walsh-Contrast Certificate for Continuous P75 Separation

**Question.** Can shared P75 parameter dependence across two parity characters certify model separation when every predeclared P83 parity observable remains individually compatible?

**Result.** Define the 15 nonconstant Walsh characters `chi_J(x)=(-1)^{sum_{j in J} x_j}` and all 210 signed pairwise contrasts `phi=chi_A+s chi_B`, with `A != B` and `s in {-1,+1}`. Conditional independence gives a branch expectation equal to a signed sum of two products of `(1-2q)`. This expression is multi-affine in the shared response coordinates, so its box extrema are exact at rational endpoint vertices. Dividing empirical expectation mismatch from the exact box interval by `sum_x |phi(x)|` gives a sound full-law L-infinity lower bound. P84 takes the maximum of that finite contrast family and the complete P83 certificate.

**Dominance.** `L84(B) >= L83(B) >= L82(B) >= L81(B) >= L80(B) >= L78(B)` on every parameter box.

**Strict witness.** An exact sixteen-cell empirical law with minimum cell mass `1/64` and maximum `9/64` satisfies the complete P82 and P83 finite families on the declared box. The P75 box nevertheless forces `E[chi_{1,2}-chi_{1,3}]=0`, while the empirical expectation is `3/16`. The contrast L1 norm is 16, giving `L84=3/256>0=L83`.

**Executable record.** [Proof](proposition_84_exact_pairwise_walsh_contrast.md), [provenance](p84_equation_provenance.md), [implementation](../src/consciousness_bridge/walsh_contrast_model_separation.py), [tests](../tests/test_walsh_contrast_model_separation.py), [figure](figures/p84_exact_pairwise_walsh_contrast.svg).

**Boundary.** P84 certifies incompatibility with a declared latent-variable model under stated assumptions. It does not assign experiential meaning to the latent state, and the physical-to-experiential bridge remains open.
"""
    write(path, text)


def sync_equation_map() -> None:
    path = "docs/equation_and_citation_map.md"
    text = read(path)
    for old, new in (
        ("P1-P83", "P1-P84"),
        ("P1 through P83", "P1 through P84"),
        ("current theorem frontier is P83", "current theorem frontier is P84"),
        ("current theorem frontier is **P83**", "current theorem frontier is **P84**"),
    ):
        text = replace_if_present(text, old, new)
    if "## P84 equation and provenance record" not in text:
        text += """

## P84 equation and provenance record

P84 adds signed pairwise Walsh observables

\[
\phi_{A,B,s}(x)=\chi_A(x)+s\chi_B(x),
\qquad
\chi_J(x)=(-1)^{\sum_{j\in J}x_j},
\]

with exact P75 branch expectation

\[
\mathbb E_t[\phi]
=\prod_{j\in A}(1-2q_{j,t})
+s\prod_{j\in B}(1-2q_{j,t}).
\]

The multi-affine box range is exact at vertices. The observable transfer

\[
|\mathbb E_p\phi-\mathbb E_q\phi|
\le \|p-q\|_\infty\sum_x|\phi(x)|
\]

yields the single-contrast lower certificate, and

\[
L_{84}(B)=\max\{L_{83}(B),L_{\mathrm{Walsh}}(B)\}.
\]

The standard P84 family has `2*C(15,2)=210` contrasts. The strict exact-rational witness gives `L82=L83=0` and `L84=3/256`.

**Classification:** repository-original exact-rational computational certificate built from standard Walsh character identities, the P75 conditional-independence factorization, the multi-affine box-extremum principle, and a finite-dimensional norm inequality.

Full record: [P84 provenance](p84_equation_provenance.md), [proof](proposition_84_exact_pairwise_walsh_contrast.md), [implementation](../src/consciousness_bridge/walsh_contrast_model_separation.py), [tests](../tests/test_walsh_contrast_model_separation.py).
"""
    write(path, text)


def sync_figure_catalog() -> None:
    path = "docs/figure_catalog.md"
    text = read(path)
    text = text.replace(
        "**Current catalog:** 141 SVG figures: 17 architecture/conceptual visuals, 18 foundational quantum-physics visuals, 66 proposition/theorem visuals, and 40 quantitative figures.",
        "**Current catalog:** 142 SVG figures: 17 architecture/conceptual visuals, 18 foundational quantum-physics visuals, 67 proposition/theorem visuals, and 40 quantitative figures.",
    )
    if "p84_exact_pairwise_walsh_contrast.svg" not in text:
        text += """

## P84 current frontier figure

| Figure | What it shows and how to interpret it | Scientific status | Formal context |
| --- | --- | --- | --- |
| [P84 exact pairwise Walsh-contrast certificate](figures/p84_exact_pairwise_walsh_contrast.svg) | What this figure shows: P84 keeps shared P75 response-parameter dependence across two Walsh parity characters, audits 210 signed pairwise contrasts, and transfers exact expectation mismatch to full-law L-infinity distance. How to read it: move from the finite Walsh family, through exact joint multi-affine extremization, to the strict witness. The witness has `L82=L83=0` while `chi12-chi13` yields `L84=3/256`. | Conditional exact-rational computational-certification theorem. It is a model-distance result, not an identification of consciousness; the physical-to-experiential bridge remains open. | [P84 proof](proposition_84_exact_pairwise_walsh_contrast.md), [provenance](p84_equation_provenance.md), [implementation](../src/consciousness_bridge/walsh_contrast_model_separation.py), [tests](../tests/test_walsh_contrast_model_separation.py) |
"""
    write(path, text)


def sync_website_index() -> None:
    path = "website/index.html"
    text = read(path)
    replacements = (
        ("an 83-result mathematical-physics research program", "an 84-result mathematical-physics research program"),
        (">Explore all 83 results<", ">Explore all 84 results<"),
        ("<strong>83</strong><span>proposition-level results</span>", "<strong>84</strong><span>proposition-level results</span>"),
        ("<strong>P83</strong><span>current theorem frontier</span>", "<strong>P84</strong><span>current theorem frontier</span>"),
        ("<strong>Current record:</strong> 83 proposition-level results through P83", "<strong>Current record:</strong> 84 proposition-level results through P84"),
        ("P73-P83 progressively", "P73-P84 progressively"),
        ("The 83 results form", "The 84 results form"),
        ("P75-P83 test", "P75-P84 test"),
        ("read 82 proofs", "read 84 proofs"),
        ("P71-P83", "P71-P84"),
        ("P74-P82", "P74-P84"),
        ("The 83-result program", "The 84-result program"),
        ("<span>P75-P83</span>", "<span>P75-P84</span>"),
    )
    for old, new in replacements:
        text = replace_if_present(text, old, new)
    if "p84_exact_pairwise_walsh_contrast.svg" not in text:
        p83_card = """      <div class="figure-card">
        <img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p83_exact_projection_parity.svg" alt="P83 exact projection-parity certificate" />
        <div><h3>P83 · Exact projection parity</h3><p>P83 adds 22 exact parity observables whose branch probabilities reduce to a multi-affine product. Exact rational vertex extremization exposes dependence constraints that can remain invisible to every P82 nested event. A strict witness has L82 = 0 and L83 = 1/16.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_83_exact_projection_parity.md">Read P83 →</a></div>
      </div>
"""
        p84_card = """
      <div class="figure-card">
        <img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p84_exact_pairwise_walsh_contrast.svg" alt="P84 exact pairwise Walsh-contrast certificate" />
        <div><h3>P84 · Exact pairwise Walsh contrasts</h3><p>P84 audits 210 signed pairwise Walsh contrasts and retains shared P75 response-parameter dependence across two parity characters. A strict exact-rational witness has L82 = L83 = 0 while chi12 - chi13 yields L84 = 3/256.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_84_exact_pairwise_walsh_contrast.md">Read P84 →</a></div>
      </div>
"""
        if p83_card not in text:
            raise RuntimeError("website index P83 figure-card anchor not found")
        text = text.replace(p83_card, p83_card + p84_card, 1)
    write(path, text)


def sync_website_research_map() -> None:
    path = "website/research-map.html"
    text = read(path)
    for old, new in (
        ("Eighty-three results, one dependency-aware scientific program", "Eighty-four results, one dependency-aware scientific program"),
        ("through Proposition 83", "through Proposition 84"),
        ("P77-P83: from full-law rejection to exact dependency-aware certification", "P77-P84: from full-law rejection to exact dependency-aware certification"),
    ):
        text = replace_if_present(text, old, new)
    if 'id="p84-frontier"' not in text:
        p83 = """    <article class="result" id="p83-frontier"><span>P83</span><h3>Exact projection-parity constraints</h3><p>Use 22 exact two-, three-, and four-view parity events to expose dependence incompatibility that the complete P82 event family can leave compatible. The exact witness has L82 = 0 and L83 = 1/16.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_83_exact_projection_parity.md">Open P83 →</a></article>
"""
        p84 = """    <article class="result" id="p84-frontier"><span>P84</span><h3>Exact pairwise Walsh contrasts</h3><p>Use 210 signed two-character Walsh observables to retain shared response-parameter dependence that separate P83 parity intervals can discard. The exact witness has L82 = L83 = 0 and L84 = 3/256.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_84_exact_pairwise_walsh_contrast.md">Open P84 →</a></article>
"""
        if p83 not in text:
            raise RuntimeError("research-map P83 card anchor not found")
        text = text.replace(p83, p83 + p84, 1)
        actions_marker = "    <a class=\"button primary\" href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p83_equation_provenance.md\">Audit P83 equation provenance</a>"
        text = text.replace(
            actions_marker,
            "    <a class=\"button primary\" href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p84_equation_provenance.md\">Audit P84 equation provenance</a>\n"
            "    <a class=\"button\" href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p83_equation_provenance.md\">Audit P83 equation provenance</a>",
            1,
        )
    write(path, text)


def append_website_panel(path: str, panel: str, token: str) -> None:
    text = read(path)
    if token not in text:
        text = insert_before_once(text, "</main>", panel, path=path)
    write(path, text)


def sync_other_website_pages() -> None:
    path = "website/start-here.html"
    text = read(path)
    for old, new in (
        ("83 proposition-level results", "84 proposition-level results"),
        ("P83", "P84") if False else ("__never__", "__never__"),
        ("P71-P83", "P71-P84"),
        ("P75-P83", "P75-P84"),
        ("83-result", "84-result"),
    ):
        text = replace_if_present(text, old, new)
    if "p84-start-here" not in text:
        panel = """
<section class="panel" id="p84-start-here"><h2>Current theorem frontier: P84</h2><p>P84 adds 210 exact signed pairwise Walsh contrasts to the complete P83 certificate. The strict exact-rational witness has L82 = L83 = 0 and L84 = 3/256. This remains a conditional model-distance theorem; the physical-to-experiential bridge is open.</p><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_84_exact_pairwise_walsh_contrast.md">Read P84</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p84_equation_provenance.md">Audit equations</a></p></section>
"""
        text = insert_before_once(text, "</main>", panel, path=path)
    write(path, text)

    append_website_panel(
        "website/visual-atlas.html",
        """
<section class="panel" id="p84-visual"><h2>P84: Exact Pairwise Walsh-Contrast Certificate</h2><div class="figure-card"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p84_exact_pairwise_walsh_contrast.svg" alt="P84 exact pairwise Walsh-contrast certificate" /><div><p>210 signed pairwise Walsh contrasts preserve shared P75 response-parameter dependence across parity characters. The exact witness has L82 = L83 = 0 and L84 = 3/256.</p><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_84_exact_pairwise_walsh_contrast.md">Proof</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p84_equation_provenance.md">Provenance</a></p></div></div></section>
""",
        "p84-visual",
    )
    append_website_panel(
        "website/sources.html",
        """
<section class="panel" id="p84-sources"><h2>P84 equation and provenance audit</h2><p>P84 combines standard Walsh-character algebra, the P75 conditional-independence factorization, exact multi-affine box extremization, and a finite-dimensional observable norm bound. Repository-original claims and imported ingredients are classified explicitly.</p><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p84_equation_provenance.md">Open the P84 provenance record</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_84_exact_pairwise_walsh_contrast.md">Read the theorem</a></p></section>
""",
        "p84-sources",
    )


def sync_orientation_test() -> None:
    path = "tests/test_website_research_orientation.py"
    text = read(path)
    text = text.replace(
        "test_research_map_presents_p77_through_p83_in_dependency_order",
        "test_research_map_presents_p77_through_p84_in_dependency_order",
    )
    text = text.replace('assert "through Proposition 83" in text', 'assert "through Proposition 84" in text')
    if 'p84 = text.index("Open P84 →", frontier)' not in text:
        text = text.replace(
            '    p83 = text.index("Open P83 →", frontier)\n    assert p77 < p78 < p79 < p80 < p81 < p82 < p83',
            '    p83 = text.index("Open P83 →", frontier)\n    p84 = text.index("Open P84 →", frontier)\n    assert p77 < p78 < p79 < p80 < p81 < p82 < p83 < p84',
            1,
        )
    if '"p84_equation_provenance.md"' not in text:
        text = text.replace(
            '        "proposition_83_exact_projection_parity.md",',
            '        "proposition_83_exact_projection_parity.md",\n        "p84_equation_provenance.md",\n        "proposition_84_exact_pairwise_walsh_contrast.md",',
            1,
        )
    if "test_p84_frontier_is_unique_and_structurally_inside_main" not in text:
        text += """


def test_p84_frontier_is_unique_and_structurally_inside_main():
    text = MAP.read_text(encoding="utf-8")
    main_open = text.index("<main>")
    main_close = text.index("</main>")
    p84 = text.index('id="p84-frontier"')
    assert text.count('id="p84-frontier"') == 1
    assert main_open < p84 < main_close
    assert "Open P84 →" not in text[main_close:]
    assert "L82 = L83 = 0 and L84 = 3/256" in text
"""
    write(path, text)


def create_integration_test() -> None:
    path = ROOT / "tests/test_p84_research_integration.py"
    if path.exists():
        return
    path.write_text(
        '''from pathlib import Path\n\n\nROOT = Path(__file__).resolve().parents[1]\n\n\ndef _read(path: str) -> str:\n    return (ROOT / path).read_text(encoding="utf-8")\n\n\ndef test_p84_publication_surfaces_are_synchronized() -> None:\n    required = {\n        "README.md": ("P84", "3/256", "p84_exact_pairwise_walsh_contrast.svg"),\n        "START_HERE.md": ("84 proposition-level results", "P84", "3/256"),\n        "docs/research_navigation.md": ("P84", "proposition_84_exact_pairwise_walsh_contrast.md", "p84_equation_provenance.md"),\n        "docs/theorem_roadmap.md": ("P84", "3/256", "walsh_contrast_model_separation.py"),\n        "docs/detailed_proposition_record.md": ("Proposition 84", "210", "3/256"),\n        "docs/equation_and_citation_map.md": ("P84 equation and provenance record", "L_{84}", "210"),\n        "docs/figure_catalog.md": ("142 SVG figures", "p84_exact_pairwise_walsh_contrast.svg", "3/256"),\n        "figures/CURRENT_FRONTIER.md": ("P71-P84", "P84", "3/256"),\n        "CITATION.cff": ("Current documented theorem frontier: P84", "Proposition 84", "three over 256"),\n        "CITATION.bib": ("version      = {0.82.0}", "frontier: P84"),\n        "CITATION.md": ("Proposition 84 method citation", "L84 = 3/256"),\n        "website/index.html": ("84 proposition-level results", "P84", "p84_exact_pairwise_walsh_contrast.svg"),\n        "website/research-map.html": ('id="p84-frontier"', "Open P84", "L84 = 3/256"),\n        "website/visual-atlas.html": ("p84-visual", "p84_exact_pairwise_walsh_contrast.svg", "L84 = 3/256"),\n    }\n    for path, tokens in required.items():\n        text = _read(path)\n        for token in tokens:\n            assert token in text, (path, token)\n\n\ndef test_p84_release_version_remains_formally_v082_during_frontier_development() -> None:\n    pyproject = _read("pyproject.toml")\n    cff = _read("CITATION.cff")\n    readme = _read("README.md")\n    assert 'version = "0.82.0"' in pyproject\n    assert "version: 0.82.0" in cff\n    assert "Formal release | **v0.82.0**" in readme\n    assert "Public theorem frontier | **P84**" in readme\n\n\ndef test_p84_scientific_boundary_is_explicit() -> None:\n    proof = _read("docs/proposition_84_exact_pairwise_walsh_contrast.md")\n    provenance = _read("docs/p84_equation_provenance.md")\n    source = _read("src/consciousness_bridge/walsh_contrast_model_separation.py")\n    for text in (proof, provenance, source):\n        assert "physical-to-experiential bridge" in text\n        assert "consciousness" in text\n    assert "does not identify a latent state" in source\n''',
        encoding="utf-8",
    )


def main() -> None:
    sync_readme()
    sync_start_here()
    sync_changelog()
    sync_citations()
    sync_verifier()
    sync_navigation()
    sync_roadmap()
    sync_detailed_record()
    sync_equation_map()
    sync_figure_catalog()
    sync_website_index()
    sync_website_research_map()
    sync_other_website_pages()
    sync_orientation_test()
    create_integration_test()
    print("P84 publication surfaces synchronized.")


if __name__ == "__main__":
    main()
