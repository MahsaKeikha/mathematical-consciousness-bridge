"""One-time guarded promotion of the proved P87 theorem to public frontier.

The script is intentionally deterministic.  It promotes reader/publication
surfaces only after the P87 proof, provenance, implementation, exact tests, and
canonical SVG already exist in the repository.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

P87_PROOF = "proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md"
P87_FIGURE = "p87_exact_bounded_primitive_quad_projection_parity.svg"
P87_SOURCE = "bounded_primitive_quad_projection_parity_functional_separation.py"
P87_TEST = "test_bounded_primitive_quad_projection_parity_functional_separation.py"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_required(text: str, old: str, new: str, *, label: str) -> str:
    if old in text:
        return text.replace(old, new)
    if new in text:
        return text
    raise RuntimeError(f"could not resolve {label}: {old!r}")


def promote_readme() -> None:
    path = "README.md"
    text = read(path)
    replacements = (
        ("P1-P86 program map, and the current P86 frontier", "P1-P87 program map, and the current P87 frontier"),
        ("| Public theorem frontier | **P86** |", "| Public theorem frontier | **P87** |"),
        ("| Proposition-level results | **86** |", "| Proposition-level results | **87** |"),
        ("P1 to P86 detailed proposition record", "P1 to P87 detailed proposition record"),
        ("P19-P24, P71-P86", "P19-P24, P71-P87"),
        ("P71-P86", "P71-P87"),
        ("P75-P86", "P75-P87"),
        ("P77-P86", "P77-P87"),
        ("The repository now contains 86 proposition-level results. The theorem frontier is P86.", "The repository now contains 87 proposition-level results. The theorem frontier is P87."),
        ("**86 proposition-level results**", "**87 proposition-level results**"),
        ("Current theorem frontier: **P86**.", "Current theorem frontier: **P87**."),
    )
    for old, new in replacements:
        if old in text:
            text = text.replace(old, new)

    text = re.sub(
        r"The research currently contains \*\*86 proposition-level results\*\*",
        "The research currently contains **87 proposition-level results**",
        text,
    )

    spotlight = f"""

> [!IMPORTANT]
> **Current theorem frontier — P87.** P87 completes the primitive four-event coefficient box at radius two: every nonzero primitive coefficient vector with `0 < |c_i| <= 2`, modulo global sign, is audited across four distinct canonical even-parity observables. This gives **120 coefficient patterns per four-event subset and 39,600 exact functionals**. On the exact rational strict witness, the complete P86 bound is `1/192` while P87 certifies `1/96`, a factor-of-two improvement on the same box and empirical law. [Read P87](docs/{P87_PROOF}) · [equation provenance](docs/p87_equation_provenance.md) · [implementation](src/consciousness_bridge/{P87_SOURCE}) · [exact tests](tests/{P87_TEST}).

![P87 complete bounded-primitive four-event certificate](docs/figures/{P87_FIGURE})

**P87 frontier figure.** The figure shows the complete 39,600-function bounded-primitive family, exact multi-affine parameter-box certification, mass-conservation centering, and the strict hierarchy witness `L86 = 1/192 < L87 = 1/96`. P87 remains a conditional model-separation theorem for the declared P75 family; it does not identify the latent state with consciousness or solve the physical-to-experiential bridge.
"""
    if P87_FIGURE not in text:
        anchor = "for proposition-by-proposition assumptions, statements, proofs, implementations, tests, and scientific boundaries."
        index = text.find(anchor)
        if index < 0:
            raise RuntimeError("could not locate README detailed-record anchor")
        end = index + len(anchor)
        text = text[:end] + spotlight + text[end:]
    write(path, text)


def promote_start_here() -> None:
    path = "START_HERE.md"
    text = read(path)
    replacements = (
        ("86-result theorem program", "87-result theorem program"),
        ("86 proposition-level results", "87 proposition-level results"),
        ("current theorem frontier is **P86**", "current theorem frontier is **P87**"),
        ("P75-P86", "P75-P87"),
        ("P71-P86", "P71-P87"),
        ("P77-P86", "P77-P87"),
        ("The 86 results", "The 87 results"),
        ("**Proposition frontier:** P86", "**Proposition frontier:** P87"),
        ("**Proposition-level results:** 86", "**Proposition-level results:** 87"),
        ("## Current frontier: P86", "## Previous theorem frontier: P86"),
    )
    for old, new in replacements:
        if old in text:
            text = text.replace(old, new)

    if "## Current frontier: P87" not in text:
        text += f"""

## Current frontier: P87

P87 completes the bounded primitive four-event parity-functional family with nonzero integer coefficients satisfying `|c_i| <= 2`. After removing nonprimitive all-even vectors and one global-sign redundancy, the family contains **120 coefficient patterns for each of 330 four-event subsets, or 39,600 exact functionals**.

The exact rational strict witness strengthens the same-box certificate from `L86 = 1/192` to `L87 = 1/96`. The interval calculation is exact by multi-affine endpoint enumeration, and the full-law transfer uses the exact centered coefficient norm.

This is a conditional rejection result for the declared P75 latent measurement family. It does not identify that latent state with consciousness and does not close the physical-to-experiential bridge.

- [P87 proof](docs/{P87_PROOF})
- [P87 equation provenance](docs/p87_equation_provenance.md)
- [P87 implementation](src/consciousness_bridge/{P87_SOURCE})
- [P87 exact tests](tests/{P87_TEST})
- [P87 figure](docs/figures/{P87_FIGURE})
"""
    write(path, text)


def promote_detailed_record() -> None:
    path = "docs/detailed_proposition_record.md"
    text = read(path)
    text = text.replace("Complete P1 to P86 chronology", "Complete P1 to P87 chronology")
    if "## Proposition 87:" not in text:
        text += f"""

## Proposition 87: Exact bounded-primitive four-event projection-parity functional certificate

**P87** completes the primitive nonzero four-coefficient box `0 < |c_i| <= 2` for four distinct canonical even-parity observables, modulo one global sign. The coefficient count is exact: `(4^4 - 2^4)/2 = 120` sign-normalized primitive patterns per four-event subset. Across `C(11,4) = 330` subsets, the complete family contains **39,600 exact functionals**.

Each latent-branch functional is multi-affine in the P75 response coordinates, so exact rational box extrema occur at endpoint vertices; prevalence is affine and is likewise extremized at endpoints. Mass-conservation centering gives an exact transfer denominator for converting any functional interval mismatch into a full-law L-infinity lower bound.

On the stored exact rational witness, the complete P86 bound is `1/192`. The P87 functional `P(H02) - P(H13) - 2P(H123) + 2P(H0123)` has empirical value `-17/24`, exact P75 interval `[-1/2, 2]`, gap `5/24`, centered coefficient norm `20`, and therefore lower bound `1/96`. Exhausting the full family attains that value, proving the strict hierarchy step `L86 = 1/192 < L87 = 1/96`.

**Boundary.** P87 rejects only the declared P75 family under its assumptions. It does not identify a latent state with consciousness, validate an alternative ontology, or close the physical-to-experiential bridge.

- Proof: [{P87_PROOF}]({P87_PROOF})
- Provenance: [p87_equation_provenance.md](p87_equation_provenance.md)
- Implementation: [`{P87_SOURCE}`](../src/consciousness_bridge/{P87_SOURCE})
- Tests: [`{P87_TEST}`](../tests/{P87_TEST})
- Figure: [`{P87_FIGURE}`](figures/{P87_FIGURE})
"""
    write(path, text)


def promote_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    text = text.replace(
        "The current documented theorem frontier is **P86**. The proposition record runs from **P1 through P86 with explicit dependency branches**. P71-P86",
        "The current documented theorem frontier is **P87**. The proposition record runs from **P1 through P87 with explicit dependency branches**. P71-P87",
    )
    p86_dep = "&\\text{P86: minimally weighted four-event parity functionals test compatibility beyond the complete P85 triple certificate}"
    p87_dep = "&\\text{P87: the complete primitive coefficient box at radius two strengthens the P86 four-event certificate}"
    if p87_dep not in text:
        text = text.replace(p86_dep + "\n\\end{aligned}", p86_dep + "\\\\\n&\\Downarrow\\\\\n" + p87_dep + "\n\\end{aligned}", 1)

    p87_row = f"| [P87]({P87_PROOF}) | complete primitive four-event coefficient box with `0 < |c_i| <= 2` | bounded-primitive shared-parameter parity separation strictly strengthening P86 | proved conditional computational theorem |"
    if p87_row not in text:
        match = re.search(r"^\| \[P86\].*$", text, re.MULTILINE)
        if match is None:
            raise RuntimeError("could not locate P86 theorem-roadmap table row")
        text = text[: match.end()] + "\n" + p87_row + text[match.end() :]

    text = text.replace("After P86, the target-side chain", "After P87, the target-side chain")
    text = text.replace(
        "A substantive continuation beyond P86 must close a separately stated mathematical or statistical gap",
        "P87 closes the complete primitive coefficient box at radius two and strictly improves the P86 witness. A substantive continuation beyond P87 must close a separately stated mathematical or statistical gap",
    )
    text = text.replace("None of P71-P86", "None of P71-P87")
    text = text.replace("## After P86", "## P86 predecessor boundary")

    if "## P87: complete bounded-primitive four-event parity-functional separation" not in text:
        text += f"""

## P87: complete bounded-primitive four-event parity-functional separation

P87 replaces P86's single primitive magnitude multiset `{{1,1,1,2}}` with the complete primitive nonzero integer coefficient box `0 < |c_i| <= 2` over four distinct canonical even-parity observables. Removing the 16 all-even nonprimitive vectors and one global-sign redundancy leaves 120 coefficient patterns per four-event subset and **39,600 exact functionals** in total.

The same exact multi-affine endpoint argument gives every P75 parameter-box interval. Mass-conservation centering gives the exact full-law L-infinity transfer denominator. On the exact rational strict witness,

\[
\\boxed{{L_{{86}}=1/192<L_{{87}}=1/96}}.
\]

Direct proof: [P87]({P87_PROOF}). Provenance: [P87 equation record](p87_equation_provenance.md). Implementation: [`{P87_SOURCE}`](../src/consciousness_bridge/{P87_SOURCE}). Tests: [`{P87_TEST}`](../tests/{P87_TEST}). Figure: [P87 bounded-primitive four-event certificate](figures/{P87_FIGURE}).

P87 remains a conditional model-separation theorem for the declared P75 family. It does not identify the latent state with consciousness and does not close the physical-to-experiential bridge.

## After P87

The bounded radius-two primitive four-event family is now complete. A substantive P88 should therefore close a new gap rather than merely rename the same search. Natural directions include a rigorously bounded larger coefficient family with a new strict witness, an exact support-function or convex relaxation of the parity-coordinate image, or an observable-specific finite-sample theorem that carries sampling uncertainty through a selected functional while preserving one-sided rejection validity.
"""
    write(path, text)


def promote_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    text = text.replace(
        "The current documented theorem frontier is **P86**. The complete proposition record runs from **P1 through P86**. P71-P86",
        "The current documented theorem frontier is **P87**. The complete proposition record runs from **P1 through P87**. P71-P87",
    )
    text = text.replace("from P1 through P86", "from P1 through P87")

    start = text.index("## Recommended reading order")
    end = text.index("## Scientific branch map", start)
    section = text[start:end]
    if f"[P87 exact bounded-primitive four-event projection-parity functional]({P87_PROOF})" not in section:
        lines = section.splitlines()
        p86_index = next(i for i, line in enumerate(lines) if "[P86 exact minimally weighted" in line)
        lines.insert(
            p86_index + 1,
            f"0. [P87 exact bounded-primitive four-event projection-parity functional]({P87_PROOF}) for the complete radius-two primitive coefficient audit, 39,600 exact functionals, P87 >= P86 dominance, and the strict `L86 = 1/192 < L87 = 1/96` witness.",
        )
        counter = 0
        for i, line in enumerate(lines):
            if re.match(r"^\d+\. ", line):
                counter += 1
                lines[i] = re.sub(r"^\d+\. ", f"{counter}. ", line, count=1)
        new_section = "\n".join(lines) + ("\n" if section.endswith("\n") else "")
        text = text[:start] + new_section + text[end:]

    p87_branch = f"| Complete bounded-primitive four-event projection-parity functional separation | P87 | Exhausts all 39,600 primitive nonzero four-event integer functionals with `|c_i| <= 2` and strictly strengthens P86 on the exact witness | [P87]({P87_PROOF}) |"
    if p87_branch not in text:
        match = re.search(r"^\| Minimally weighted four-event projection-parity functional separation \| P86 \|.*$", text, re.MULTILINE)
        if match is None:
            raise RuntimeError("could not locate P86 branch-map row")
        text = text[: match.end()] + "\n" + p87_branch + text[match.end() :]

    p87_index = f"| P87 | [Bounded-primitive four-event projection-parity functional]({P87_PROOF}) | complete radius-two primitive coefficient audit and strict P87 > P86 exact separation |"
    if p87_index not in text:
        matches = list(re.finditer(r"^\| P86 \|.*$", text, re.MULTILINE))
        if not matches:
            raise RuntimeError("could not locate P86 proposition-index row")
        match = matches[-1]
        text = text[: match.end()] + "\n" + p87_index + text[match.end() :]

    if "P87 equation and provenance record" not in text:
        anchor = "[P85 equation and provenance record](p85_equation_provenance.md)"
        if anchor in text:
            text = text.replace(
                anchor,
                anchor + " for the P85 triple-functional step.\n39. [P87 equation and provenance record](p87_equation_provenance.md)",
                1,
            )
    write(path, text)


def promote_reproducibility() -> None:
    path = "docs/reproducibility.md"
    text = read(path)
    replacements = (
        ("the top-level GitHub figure gateway advertises P86", "the top-level GitHub figure gateway advertises P87"),
        ("the Visual Atlas presents P86 before historical P84/P85 frontiers", "the Visual Atlas presents P87 before historical P86/P85 frontiers"),
        ("For P86 the deployed artifact must contain:", "For P87 the deployed artifact must contain:"),
        ("_site/figures/p86_exact_minimally_weighted_quad_projection_parity.svg", f"_site/figures/{P87_FIGURE}"),
        ('src="figures/p86_exact_minimally_weighted_quad_projection_parity.svg"', f'src="figures/{P87_FIGURE}"'),
        ("The current repository frontier is **P86**, and the proof sequence is expected through Proposition 86.", "The current repository frontier is **P87**, and the proof sequence is expected through Proposition 87."),
        ("the current P86 theorem figure", "the current P87 theorem figure"),
        ("the P86 SVG as bundled", "the P87 SVG as bundled"),
        ("verifies that the Visual Atlas loads P86", "verifies that the Visual Atlas loads P87"),
        ("## 12. Reproduce the current P86 implementation checks directly", "## 12. Reproduce the current P87 implementation checks directly"),
        ("The current theorem frontier is **P86**.", "The current theorem frontier is **P87**."),
        ("docs/proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md", f"docs/{P87_PROOF}"),
        ("docs/p86_equation_provenance.md", "docs/p87_equation_provenance.md"),
        ("src/consciousness_bridge/weighted_quad_projection_parity_functional_separation.py", f"src/consciousness_bridge/{P87_SOURCE}"),
        ("tests/test_weighted_quad_projection_parity_functional_separation.py", f"tests/{P87_TEST}"),
        ("docs/figures/p86_exact_minimally_weighted_quad_projection_parity.svg", f"docs/figures/{P87_FIGURE}"),
        ("tests/test_weighted_quad_projection_parity_functional_separation.py \\", f"tests/{P87_TEST} \\\"),
        ("The P86 exact hierarchy witness is:", "The P87 exact hierarchy witness is:"),
        ("L85 = 0 < L86 = 1/192", "L86 = 1/192 < L87 = 1/96"),
        ("useful for auditing P86", "useful for auditing P87"),
    )
    for old, new in replacements:
        if old in text:
            text = text.replace(old, new)
    write(path, text)


def promote_citation_surfaces() -> None:
    path = "CITATION.cff"
    text = read(path)
    text = text.replace("Current documented theorem frontier: P86.", "Current documented theorem frontier: P87.")
    text = text.replace("Current documented theorem frontier: P86.\"", "Current documented theorem frontier: P87.\"")
    p87_sentence = (
        " Proposition 87 completes the primitive nonzero four-event integer coefficient box with absolute coefficient at most two, auditing 39,600 exact functionals and giving an exact strict witness with P86 equal to one one-hundred-ninety-second while P87 equals one ninety-sixth."
    )
    if "Proposition 87 completes the primitive nonzero" not in text:
        needle = "Proposition 86 adds 10,560 exact minimally weighted four-event parity functionals with primitive coefficient magnitudes {1,1,1,2}; its strict exact-rational witness has the complete P85 certificate equal to zero while P86 equals one one-hundred-ninety-second."
        if needle in text:
            text = text.replace(needle, needle + p87_sentence, 1)
    text = text.replace("Current documented theorem frontier: P86.", "Current documented theorem frontier: P87.")
    write(path, text)

    for relative in ("CITATION.md", "docs/equation_and_citation_map.md"):
        text = read(relative)
        text = text.replace("Current theorem frontier: **P86**", "Current theorem frontier: **P87**")
        text = text.replace("current theorem frontier is **P86**", "current theorem frontier is **P87**")
        text = text.replace("P1-P86", "P1-P87")
        if relative.endswith("equation_and_citation_map.md") and "## P87: bounded-primitive four-event" not in text:
            text += f"""

## P87: bounded-primitive four-event parity-functional separation

P87 exhausts the sign-normalized primitive nonzero integer coefficient box `0 < |c_i| <= 2` over four distinct canonical even-parity observables. The 120 coefficient patterns across 330 four-event subsets give 39,600 exact functionals. Exact multi-affine endpoint evaluation and mass-conservation centering yield the strict exact-rational certificate `L86 = 1/192 < L87 = 1/96` on the stored witness.

- Proof: [{P87_PROOF}]({P87_PROOF})
- Provenance: [p87_equation_provenance.md](p87_equation_provenance.md)
- Implementation: [`{P87_SOURCE}`](../src/consciousness_bridge/{P87_SOURCE})
- Tests: [`{P87_TEST}`](../tests/{P87_TEST})

Scientific boundary: this is a conditional model-separation theorem for the declared P75 family, not an identification of a latent variable with consciousness.
"""
        write(relative, text)


def promote_figure_catalog() -> None:
    path = "docs/figure_catalog.md"
    text = read(path)
    if P87_FIGURE not in text:
        text += f"""

## P87 complete bounded-primitive four-event projection-parity certificate

![P87 complete bounded-primitive four-event projection-parity certificate](figures/{P87_FIGURE})

**What it shows.** The complete primitive nonzero coefficient box `0 < |c_i| <= 2` contains 120 sign-normalized coefficient patterns per four-event subset and 39,600 exact functionals across the eleven canonical even-parity coordinates. The displayed strict witness has `L86 = 1/192 < L87 = 1/96`.

**How to read it.** Move left to right from finite family enumeration, through exact multi-affine P75 box certification and centered full-law transfer, to the exact rational hierarchy improvement.

**Scientific status.** Source-controlled theorem diagram for [Proposition 87]({P87_PROOF}); it illustrates a proved conditional computational theorem. It is not empirical evidence that the latent P75 state is consciousness.
"""
    write(path, text)


def promote_verifiers_and_builders() -> None:
    path = "scripts/verify_repository.py"
    text = read(path)
    text = text.replace('CURRENT_FRONTIER = "P86"', 'CURRENT_FRONTIER = "P87"')
    text = text.replace(
        '    "docs/figures/p86_exact_minimally_weighted_quad_projection_parity.svg",',
        '    "docs/figures/p86_exact_minimally_weighted_quad_projection_parity.svg",\n    "docs/figures/p87_exact_bounded_primitive_quad_projection_parity.svg",',
    )
    text = text.replace(
        '    "docs/p86_equation_provenance.md",',
        '    "docs/p86_equation_provenance.md",\n    "docs/proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md",\n    "docs/p87_equation_provenance.md",',
    )
    text = text.replace("for number in range(1, 87):", "for number in range(1, int(CURRENT_FRONTIER[1:]) + 1):")
    stale_anchor = 'STALE_READER_FRONTIER_MARKERS = (\n'
    if '"current P86 frontier"' not in text:
        text = text.replace(
            stale_anchor,
            stale_anchor
            + '    "86-result theorem program and current P86 frontier",\n'
            + '    "Current frontier · P86",\n'
            + '    "<strong>P86</strong><span>current theorem frontier</span>",\n'
            + '    "current P86 frontier",\n'
            + '    "actual P86 research frontier",\n',
            1,
        )
    write(path, text)

    path = "scripts/prepare_website.py"
    text = read(path)
    text = text.replace('CURRENT_FRONTIER_FIGURE = "p86_exact_minimally_weighted_quad_projection_parity.svg"', f'CURRENT_FRONTIER_FIGURE = "{P87_FIGURE}"')
    text = re.sub(r'ASSET_VERSION = "[^"]+"', 'ASSET_VERSION = "20260913-mobile17-p87"', text, count=1)
    text = text.replace("Require P86 to be the primary visual frontier", "Require P87 to be the primary visual frontier")
    text = text.replace("current P86 theorem figure", "current P87 theorem figure")
    text = text.replace("bundled P86 theorem figure", "bundled P87 theorem figure")
    text = text.replace("P86 frontier", "P87 frontier")
    text = text.replace("p86 = homepage.index('id=\"p86-frontier\"')", "p87 = homepage.index('id=\"p87-frontier\"')")
    text = text.replace("if p86 >= homepage.index(marker):", "if p87 >= homepage.index(marker):")
    text = text.replace("Homepage P86 frontier appears too late", "Homepage P87 frontier appears too late")
    text = text.replace("for marker in ('id=\"plain-language\"', 'id=\"p84-frontier\"', 'id=\"p85-frontier\"'):", "for marker in ('id=\"plain-language\"', 'id=\"p84-frontier\"', 'id=\"p85-frontier\"', 'id=\"p86-frontier\"'):")
    text = text.replace('"Current theorem frontier · P85",', '"Current theorem frontier · P86",\n        "Current theorem frontier · P85",')
    write(path, text)


def promote_figure_sync() -> None:
    path = "scripts/sync_figure_publication.py"
    text = read(path)

    old_function_start = text.index("def _p86_visual_section() -> str:")
    old_function_end = text.index("\n\ndef _normalize_visual_atlas", old_function_start)
    new_function = f'''def _p87_visual_section() -> str:\n    return f\'\'\'<section id="p87-frontier" class="theorem-frontier current-frontier-visual">\n  <div class="section-head">\n    <p class="eyebrow">Current theorem frontier · P87</p>\n    <h2>Complete bounded-primitive four-event parity certificate</h2>\n    <p>P87 exhausts every primitive nonzero four-coefficient pattern with absolute coefficient at most two: 120 patterns per four-event subset and 39,600 exact functionals in total.</p>\n  </div>\n  <div class="theorem-figure-shell">\n    <a href="{{BLOB_PREFIX}}docs/figures/{P87_FIGURE}" aria-label="Open the full P87 theorem figure">\n      <img loading="eager" decoding="async" src="{{RAW_FIGURE_PREFIX}}{P87_FIGURE}" alt="P87 bounded-primitive four-event parity certificate showing L86 one over 192 and L87 one over 96" />\n    </a>\n  </div>\n  <div class="frontier-summary-grid">\n    <article class="frontier-summary-card"><h3>Complete bounded family</h3><p>120 sign-normalized primitive coefficient patterns across 330 four-event subsets produce 39,600 exact functionals.</p></article>\n    <article class="frontier-summary-card"><h3>Strict hierarchy</h3><p>The same exact rational witness has <strong>L86 = 1/192 &lt; L87 = 1/96</strong>.</p></article>\n    <article class="frontier-summary-card"><h3>Exact certification</h3><p>Multi-affine endpoint ranges and mass-conservation centering keep the complete calculation rational and one-sided.</p></article>\n  </div>\n  <div class="boundary"><p><strong>Scientific boundary:</strong> P87 is a conditional exact model-separation theorem for the declared P75 family. It does not identify consciousness, establish nonphysicality, or close the physical-to-experiential bridge.</p></div>\n  <p><a href="{{BLOB_PREFIX}}docs/{P87_PROOF}">Open the P87 theorem</a> · <a href="{{BLOB_PREFIX}}docs/p87_equation_provenance.md">Equation provenance</a> · <a href="{{BLOB_PREFIX}}src/consciousness_bridge/{P87_SOURCE}">Implementation</a> · <a href="{{BLOB_PREFIX}}tests/{P87_TEST}">Exact tests</a></p>\n</section>\'\'\'\n'''
    text = text[:old_function_start] + new_function + text[old_function_end:]

    normal_start = text.index("def _normalize_visual_atlas(text: str) -> str:")
    normal_end = text.index("\n\ndef _normalize_homepage", normal_start)
    new_atlas = '''def _normalize_visual_atlas(text: str) -> str:\n    pattern = re.compile(r'<section id="p87-frontier".*?</section>', re.DOTALL)\n    text, count = pattern.subn("", text, count=1)\n    if count not in (0, 1):\n        raise RuntimeError(f"expected at most one P87 Visual Atlas section, found {count}")\n    text = text.replace("Current theorem frontier · P86", "Previous theorem frontier · P86")\n    marker = "<!-- current-frontier-visual: P87 -->"\n    text = re.sub(r"\\s*<!-- current-frontier-visual: P(?:86|87) -->\\s*", "", text)\n    boundary = re.search(r'<section class="boundary">.*?</section>', text, re.DOTALL)\n    if boundary is None:\n        raise RuntimeError("could not locate Visual Atlas reading-boundary section")\n    prefix = text[: boundary.end()].rstrip()\n    suffix = text[boundary.end() :].lstrip()\n    insertion = "\\n\\n" + marker + "\\n" + _p87_visual_section() + "\\n\\n"\n    result = prefix + insertion + suffix\n    had_final_newline = result.endswith("\\n")\n    result = "\\n".join(line.rstrip() for line in result.splitlines())\n    return result + ("\\n" if had_final_newline else "")\n'''
    text = text[:normal_start] + new_atlas + text[normal_end:]

    home_start = text.index("def _normalize_homepage(text: str) -> str:")
    home_end = text.index("\n\ndef _expected_outputs", home_start)
    new_home = '''def _normalize_homepage(text: str) -> str:\n    """Make P87 the first theorem visual and demote older homepage frontiers."""\n    pattern = re.compile(r'\\s*<section id="p87-frontier".*?</section>\\s*', re.DOTALL)\n    text, count = pattern.subn("\\n", text, count=1)\n    if count not in (0, 1):\n        raise RuntimeError(f"expected at most one P87 homepage section, found {count}")\n    text = text.replace("Current theorem frontier · P86", "Previous theorem frontier · P86")\n    replacements = (\n        ("Explore all 86 results", "Explore all 87 results"),\n        ("<strong>86</strong><span>proposition-level results</span>", "<strong>87</strong><span>proposition-level results</span>"),\n        ("<strong>P86</strong><span>current theorem frontier</span>", "<strong>P87</strong><span>current theorem frontier</span>"),\n        ("The 86-result program", "The 87-result program"),\n        ("The 86 results form several dependency branches.", "The 87 results form several dependency branches."),\n        ("You do not need to read all 86 propositions in numerical order", "You do not need to read all 87 propositions in numerical order"),\n        ("Focus on P19 and P71-P86, then read the falsification program.", "Focus on P19 and P71-P87, then read the falsification program."),\n        ("P75-P86", "P75-P87"),\n        ("P71-P86:", "P71-P87:"),\n    )\n    for old, new in replacements:\n        if old in text:\n            text = text.replace(old, new)\n    marker = "<!-- current-frontier-home: P87 -->"\n    text = re.sub(r"\\s*<!-- current-frontier-home: P(?:86|87) -->\\s*", "\\n", text)\n    hero = re.search(r'<section class="hero">.*?</section>', text, re.DOTALL)\n    if hero is None:\n        raise RuntimeError("could not locate homepage hero section")\n    prefix = text[: hero.end()].rstrip()\n    suffix = text[hero.end() :].lstrip()\n    insertion = "\\n\\n" + marker + "\\n" + _p87_visual_section() + "\\n\\n"\n    result = prefix + insertion + suffix\n    had_final_newline = result.endswith("\\n")\n    result = "\\n".join(line.rstrip() for line in result.splitlines())\n    return result + ("\\n" if had_final_newline else "")\n'''
    text = text[:home_start] + new_home + text[home_end:]

    old86 = '''    if frontier == 86:\n        lines.extend(\n            [\n                "### Exact P86 hierarchy witness",\n                "",\n                "The current exact rational witness preserves the complete P85 certificate at zero while the minimally weighted four-event family is strictly positive:",\n                "",\n                "```text",\n                "L85 = 0 < L86 = 1/192",\n                "10,560 standard P86 functionals",\n                "primitive coefficient magnitudes {1,1,1,2}",\n                "```",\n                "",\n                "This is a conditional model-separation result inside the declared P75 family. It is not an identification of a latent state with conscious experience.",\n                "",\n            ]\n        )\n'''
    new87 = '''    if frontier == 87:\n        lines.extend(\n            [\n                "### Exact P87 hierarchy witness",\n                "",\n                "The complete bounded-primitive four-event family strictly strengthens P86 on the same exact rational witness:",\n                "",\n                "```text",\n                "L86 = 1/192 < L87 = 1/96",\n                "120 primitive coefficient patterns per four-event subset",\n                "39,600 standard P87 functionals",\n                "```",\n                "",\n                "This is a conditional model-separation result inside the declared P75 family. It is not an identification of a latent state with conscious experience.",\n                "",\n            ]\n        )\n'''
    if old86 not in text:
        raise RuntimeError("could not locate P86 frontier-page special block")
    text = text.replace(old86, new87, 1)
    write(path, text)


def promote_website_text() -> None:
    for path in sorted((ROOT / "website").glob("*.html")):
        text = path.read_text(encoding="utf-8")
        replacements = (
            ("Explore all 86 results", "Explore all 87 results"),
            ("<strong>86</strong><span>proposition-level results</span>", "<strong>87</strong><span>proposition-level results</span>"),
            ("<strong>P86</strong><span>current theorem frontier</span>", "<strong>P87</strong><span>current theorem frontier</span>"),
            ("The 86-result program", "The 87-result program"),
            ("P75-P86", "P75-P87"),
            ("P71-P86:", "P71-P87:"),
            ("P77-P86", "P77-P87"),
            ("through Proposition 86", "through Proposition 87"),
            ("current theorem frontier is P86", "current theorem frontier is P87"),
            ("Current theorem frontier is P86", "Current theorem frontier is P87"),
        )
        for old, new in replacements:
            if old in text:
                text = text.replace(old, new)
        path.write_text(text, encoding="utf-8")


def promote_workflows() -> None:
    path = ".github/workflows/reproducibility.yml"
    text = read(path)
    text = text.replace("Exact-reference P86 release audit", "Exact-reference P87 frontier audit")
    text = text.replace("Upload reproduced P86 visual record", "Upload reproduced P87 visual record")
    text = text.replace("reproduced-visual-record-v0.82.0-p86", "reproduced-visual-record-main-p87")
    text = text.replace("docs/figures/p86_exact_minimally_weighted_quad_projection_parity.svg", f"docs/figures/{P87_FIGURE}")
    write(path, text)


def promote_changelog() -> None:
    path = "CHANGELOG.md"
    text = read(path)
    if "Promote P87" not in text[:2000]:
        marker = "# Changelog\n"
        entry = f"""

## Unreleased

### Promote P87 complete bounded-primitive four-event certificate

- Prove and publish P87, exhausting 120 sign-normalized primitive coefficient patterns per four-event subset and 39,600 exact four-event parity functionals with `0 < |c_i| <= 2`.
- Add the exact strict witness `L86 = 1/192 < L87 = 1/96`, with proof, provenance, implementation, exhaustive regression tests, and a canonical SVG frontier figure.
- Promote all reader, navigation, reproducibility, figure-publication, and website surfaces to the P87 frontier while preserving the physical-to-experiential bridge as open.
"""
        if marker not in text:
            raise RuntimeError("CHANGELOG heading not found")
        text = text.replace(marker, marker + entry, 1)
    write(path, text)


def main() -> None:
    required = (
        ROOT / "docs" / P87_PROOF,
        ROOT / "docs" / "p87_equation_provenance.md",
        ROOT / "docs" / "figures" / P87_FIGURE,
        ROOT / "src" / "consciousness_bridge" / P87_SOURCE,
        ROOT / "tests" / P87_TEST,
    )
    missing = [path.relative_to(ROOT).as_posix() for path in required if not path.is_file()]
    if missing:
        raise RuntimeError(f"cannot promote P87; missing canonical records: {missing}")

    promote_readme()
    promote_start_here()
    promote_detailed_record()
    promote_roadmap()
    promote_navigation()
    promote_reproducibility()
    promote_citation_surfaces()
    promote_figure_catalog()
    promote_verifiers_and_builders()
    promote_figure_sync()
    promote_website_text()
    promote_workflows()
    promote_changelog()

    subprocess.run(
        ["python", "scripts/sync_figure_publication.py"],
        cwd=ROOT,
        check=True,
    )
    print("[p87-promotion] synchronized public theorem frontier to P87")


if __name__ == "__main__":
    main()
