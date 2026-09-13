"""One-time guarded promotion of the proved P88 theorem to the public frontier.

The script updates reader, theorem-map, figure-publication, website, and CI
surfaces only after the P88 proof, provenance, exact implementation, tests, and
canonical SVG exist.  The formal release stays at v0.82.0; only the public
proposition frontier advances from 87/P87 to 88/P88.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

P88_PROOF = "proposition_88_exact_expanded_bounded_primitive_quad_projection_parity_functional.md"
P88_FIGURE = "p88_exact_expanded_bounded_primitive_quad_projection_parity.svg"
P88_SOURCE = "expanded_bounded_primitive_quad_projection_parity_functional_separation.py"
P88_TEST = "test_expanded_bounded_primitive_quad_projection_parity_functional_separation.py"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_if_present(text: str, old: str, new: str) -> str:
    return text.replace(old, new) if old in text else text


def promote_primary_reader_surfaces() -> None:
    # README is intentionally concise in the current reader design.
    path = "README.md"
    text = read(path)
    replacements = (
        ("The current public theorem frontier is **P87**.", "The current public theorem frontier is **P88**."),
        ("docs/proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md", f"docs/{P88_PROOF}"),
        ("**Public theorem frontier:** P87", "**Public theorem frontier:** P88"),
    )
    for old, new in replacements:
        text = replace_if_present(text, old, new)
    write(path, text)

    path = "START_HERE.md"
    text = read(path)
    replacements = (
        ("The public theorem frontier is **P87**.", "The public theorem frontier is **P88**."),
        ("You do not need to read 87 propositions", "You do not need to read 88 propositions"),
        ("**[P87](docs/proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md)**", f"**[P88](docs/{P88_PROOF})**"),
    )
    for old, new in replacements:
        text = replace_if_present(text, old, new)
    write(path, text)


def append_p88_records() -> None:
    path = "docs/detailed_proposition_record.md"
    text = read(path)
    text = text.replace("Complete P1 to P87 chronology", "Complete P1 to P88 chronology")
    if "## Proposition 88:" not in text:
        text += f"""

## Proposition 88: Exact expanded bounded primitive four-event projection-parity functional certificate

**P88** enlarges the complete primitive nonzero four-coefficient box from `0 < |c_i| <= 2` to `0 < |c_i| <= 3` while holding fixed the four-event order, the eleven canonical P83 parity coordinates, the P75 latent measurement family, and the full-law L-infinity target metric. The expanded box has **632 sign-normalized primitive coefficient patterns per four-event subset** and therefore **208,560 exact functionals** across `C(11,4)=330` subsets.

The exact interval calculation remains multi-affine in the P75 response coordinates, so parameter-box extrema occur at endpoints. Mass-conservation centering supplies the exact full-law transfer norm. On the same rational hierarchy witness used by P86 and P87, the P88 functional `P(H02) - P(H13) - 3P(H123) + 2P(H0123)` has empirical value `-11/8`, exact P75 interval `[-1,2]`, gap `3/8`, centered coefficient norm `24`, and therefore lower bound `1/64`.

Exhausting all 208,560 P88 functionals attains that value, giving the strict hierarchy

`L85 = 0 < L86 = 1/192 < L87 = 1/96 < L88 = 1/64`.

**Boundary.** P88 is a conditional rejection certificate for the declared P75 family. It does not identify a latent state with consciousness, validate an alternative ontology, or close the physical-to-experiential bridge.

- Proof: [{P88_PROOF}]({P88_PROOF})
- Provenance: [p88_equation_provenance.md](p88_equation_provenance.md)
- Implementation: [`{P88_SOURCE}`](../src/consciousness_bridge/{P88_SOURCE})
- Tests: [`{P88_TEST}`](../tests/{P88_TEST})
- Figure: [`{P88_FIGURE}`](figures/{P88_FIGURE})
"""
    write(path, text)

    path = "docs/equation_and_citation_map.md"
    text = read(path)
    text = text.replace("Current theorem frontier: **P87**", "Current theorem frontier: **P88**")
    text = text.replace("current theorem frontier is **P87**", "current theorem frontier is **P88**")
    text = text.replace("P1-P87", "P1-P88")
    if "## P88: expanded bounded primitive four-event" not in text:
        text += f"""

## P88: expanded bounded primitive four-event parity-functional separation

P88 exhausts the sign-normalized primitive nonzero coefficient box `0 < |c_i| <= 3` over four distinct canonical even-parity observables. The 632 coefficient patterns across 330 four-event subsets give **208,560 exact functionals**. Exact multi-affine endpoint evaluation and mass-conservation centering produce the strict exact-rational hierarchy `L87 = 1/96 < L88 = 1/64` on the stored witness.

- Proof: [{P88_PROOF}]({P88_PROOF})
- Provenance: [p88_equation_provenance.md](p88_equation_provenance.md)
- Implementation: [`{P88_SOURCE}`](../src/consciousness_bridge/{P88_SOURCE})
- Tests: [`{P88_TEST}`](../tests/{P88_TEST})

Scientific boundary: this is a conditional model-separation theorem for the declared P75 family, not an identification of a latent variable with consciousness.
"""
    write(path, text)

    path = "docs/claim_source_matrix.md"
    text = read(path)
    if "P88" not in text:
        text += f"""

| P88 expanded bounded primitive four-event certificate | repository-original exact finite construction | [P88 proof]({P88_PROOF}), [equation provenance](p88_equation_provenance.md), [implementation](../src/consciousness_bridge/{P88_SOURCE}), [tests](../tests/{P88_TEST}) | `632` primitive sign-normalized patterns per four-event subset, `208,560` exact functionals, and strict exact witness `L87=1/96 < L88=1/64` | conditional separation from the declared P75 family only; does not identify consciousness or solve the physical-to-experiential bridge |
"""
    write(path, text)


def promote_roadmap_and_navigation() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    text = text.replace(
        "The current documented theorem frontier is **P87**. The proposition record runs from **P1 through P87 with explicit dependency branches**. P71-P87",
        "The current documented theorem frontier is **P88**. The proposition record runs from **P1 through P88 with explicit dependency branches**. P71-P88",
    )
    text = text.replace("None of P71-P87", "None of P71-P88")
    text = text.replace("## After P87", "## P87 predecessor boundary")
    p88_row = f"| [P88]({P88_PROOF}) | complete primitive four-event coefficient box with `0 < |c_i| <= 3` | expanded bounded-primitive parity separation strictly strengthening P87 | proved conditional computational theorem |"
    if p88_row not in text:
        matches = list(re.finditer(r"^\| \[P87\].*$", text, re.MULTILINE))
        if matches:
            match = matches[-1]
            text = text[: match.end()] + "\n" + p88_row + text[match.end() :]
    if "## P88: expanded bounded-primitive four-event parity-functional separation" not in text:
        text += f"""

## P88: expanded bounded-primitive four-event parity-functional separation

P88 closes the first larger complete primitive coefficient box after P87 while keeping the functional order fixed. It expands `0 < |c_i| <= 2` to `0 < |c_i| <= 3`, giving **632 sign-normalized primitive coefficient patterns per four-event subset** and **208,560 exact functionals** in total.

On the same exact rational witness,

\[
\\boxed{{L_{{87}}=1/96<L_{{88}}=1/64}}.
\]

The strict witness uses coefficient pattern `(1,-1,-3,2)`, so it is genuinely outside the complete P87 coefficient box.

Direct proof: [P88]({P88_PROOF}). Provenance: [P88 equation record](p88_equation_provenance.md). Implementation: [`{P88_SOURCE}`](../src/consciousness_bridge/{P88_SOURCE}). Tests: [`{P88_TEST}`](../tests/{P88_TEST}). Figure: [P88 expanded bounded-primitive certificate](figures/{P88_FIGURE}).

P88 remains a conditional model-separation theorem for the declared P75 family. It does not identify the latent state with consciousness and does not close the physical-to-experiential bridge.

## After P88

The radius-three primitive four-event box is now complete. A P89 claim should close a separately stated mathematical or scientific gap rather than continue coefficient inflation without a new structural question. Candidate directions include exact support-function geometry of the parity-coordinate image, a principled stopping criterion for coefficient-box expansion, or a finite-sample theorem that propagates sampling uncertainty through data-dependent functional selection while preserving one-sided validity.
"""
    write(path, text)

    path = "docs/research_navigation.md"
    text = read(path)
    text = text.replace(
        "The current documented theorem frontier is **P87**. The complete proposition record runs from **P1 through P87**. P71-P87",
        "The current documented theorem frontier is **P88**. The complete proposition record runs from **P1 through P88**. P71-P88",
    )
    text = text.replace("from P1 through P87", "from P1 through P88")
    if "P88 exact expanded bounded-primitive" not in text:
        anchor = re.search(r"^\d+\. \[P87 exact bounded-primitive.*$", text, re.MULTILINE)
        if anchor:
            insertion = f"\n0. [P88 exact expanded bounded-primitive four-event projection-parity functional]({P88_PROOF}) for the complete radius-three primitive coefficient audit, 208,560 exact functionals, P88 >= P87 dominance, and the strict `L87 = 1/96 < L88 = 1/64` witness."
            text = text[: anchor.end()] + insertion + text[anchor.end() :]
            # Renumber only the recommended-reading section.
            start = text.find("## Recommended reading order")
            end = text.find("## Scientific branch map", start)
            if start >= 0 and end > start:
                section = text[start:end]
                counter = 0
                lines = section.splitlines()
                for i, line in enumerate(lines):
                    if re.match(r"^\d+\. ", line):
                        counter += 1
                        lines[i] = re.sub(r"^\d+\. ", f"{counter}. ", line, count=1)
                text = text[:start] + "\n".join(lines) + "\n" + text[end:]
    p88_branch = f"| Expanded bounded-primitive four-event projection-parity functional separation | P88 | Exhausts 208,560 primitive nonzero four-event integer functionals with `|c_i| <= 3` and strictly strengthens P87 on the exact witness | [P88]({P88_PROOF}) |"
    if p88_branch not in text:
        match = re.search(r"^\| Complete bounded-primitive four-event projection-parity functional separation \| P87 \|.*$", text, re.MULTILINE)
        if match:
            text = text[: match.end()] + "\n" + p88_branch + text[match.end() :]
    p88_index = f"| P88 | [Expanded bounded-primitive four-event projection-parity functional]({P88_PROOF}) | complete radius-three primitive coefficient audit and strict P88 > P87 exact separation |"
    if p88_index not in text:
        matches = list(re.finditer(r"^\| P87 \|.*$", text, re.MULTILINE))
        if matches:
            match = matches[-1]
            text = text[: match.end()] + "\n" + p88_index + text[match.end() :]
    write(path, text)


def promote_figure_catalog_and_reproducibility() -> None:
    path = "docs/figure_catalog.md"
    text = read(path)
    text = text.replace(
        "**Current catalog:** 145 SVG figures: 17 architecture/conceptual visuals, 18 foundational quantum-physics visuals, 70 proposition/theorem visuals, and 40 quantitative figures.",
        "**Current catalog:** 146 SVG figures: 17 architecture/conceptual visuals, 18 foundational quantum-physics visuals, 71 proposition/theorem visuals, and 40 quantitative figures.",
    )
    if P88_FIGURE not in text:
        text += f"""

## P88 expanded bounded primitive four-event projection-parity certificate

![P88 expanded bounded primitive four-event projection-parity certificate](figures/{P88_FIGURE})

**What it shows.** P88 closes the complete primitive coefficient box `0 < |c_i| <= 3`: 632 sign-normalized coefficient patterns per four-event subset and 208,560 exact functionals. The exact strict witness gives `L87 = 1/96 < L88 = 1/64`.

**How to read it.** Move from finite primitive-family counting, through exact multi-affine P75 box certification and mass-conservation centering, to the strict rational hierarchy improvement.

**Scientific status.** Source-controlled theorem diagram for [Proposition 88]({P88_PROOF}); it illustrates a proved conditional computational theorem. It is not empirical evidence that the latent P75 state is consciousness.
"""
    write(path, text)

    path = "docs/reproducibility.md"
    text = read(path)
    replacements = (
        ("The current repository frontier is **P87**, and the proof sequence is expected through Proposition 87.", "The current repository frontier is **P88**, and the proof sequence is expected through Proposition 88."),
        ("## 12. Reproduce the current P87 implementation checks directly", "## 12. Reproduce the current P88 implementation checks directly"),
        ("The current theorem frontier is **P87**.", "The current theorem frontier is **P88**."),
        ("docs/proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md", f"docs/{P88_PROOF}"),
        ("docs/p87_equation_provenance.md", "docs/p88_equation_provenance.md"),
        ("src/consciousness_bridge/bounded_primitive_quad_projection_parity_functional_separation.py", f"src/consciousness_bridge/{P88_SOURCE}"),
        ("tests/test_bounded_primitive_quad_projection_parity_functional_separation.py", f"tests/{P88_TEST}"),
        ("docs/figures/p87_exact_bounded_primitive_quad_projection_parity.svg", f"docs/figures/{P88_FIGURE}"),
        ("The P87 exact hierarchy witness is:", "The P88 exact hierarchy witness is:"),
        ("L86 = 1/192 < L87 = 1/96", "L87 = 1/96 < L88 = 1/64"),
    )
    for old, new in replacements:
        text = replace_if_present(text, old, new)
    write(path, text)


def promote_citation_and_changelog() -> None:
    for path in ("CITATION.cff", "CITATION.md"):
        text = read(path)
        text = text.replace("Current documented theorem frontier: P87", "Current documented theorem frontier: P88")
        text = text.replace("Current theorem frontier: **P87**", "Current theorem frontier: **P88**")
        text = text.replace("P1-P87", "P1-P88")
        write(path, text)

    path = "CHANGELOG.md"
    text = read(path)
    if "Promote P88 expanded bounded-primitive" not in text[:3500]:
        marker = "# Changelog\n"
        entry = """

## Unreleased

### Promote P88 expanded bounded-primitive four-event certificate

- Prove P88 by completing the primitive coefficient box `0 < |c_i| <= 3` at the same four-event order: 632 sign-normalized patterns per subset and 208,560 exact functionals.
- Add the exact strict witness `L87 = 1/96 < L88 = 1/64`, with proof, provenance, exact implementation, exhaustive tests, and canonical SVG theorem figure.
- Promote reader, navigation, reproducibility, figure-publication, and website surfaces to the P88 / 88-result frontier while retaining v0.82.0 as the formal release and the physical-to-experiential bridge as open.
"""
        text = text.replace(marker, marker + entry, 1)
    write(path, text)


def promote_verifier_and_website_builder() -> None:
    path = "scripts/verify_repository.py"
    text = read(path)
    text = text.replace('CURRENT_FRONTIER = "P87"', 'CURRENT_FRONTIER = "P88"')
    text = text.replace(
        '    "docs/figures/p87_exact_bounded_primitive_quad_projection_parity.svg",',
        '    "docs/figures/p87_exact_bounded_primitive_quad_projection_parity.svg",\n    "docs/figures/p88_exact_expanded_bounded_primitive_quad_projection_parity.svg",',
    )
    text = text.replace(
        '    "docs/p87_equation_provenance.md",',
        '    "docs/p87_equation_provenance.md",\n    "docs/proposition_88_exact_expanded_bounded_primitive_quad_projection_parity_functional.md",\n    "docs/p88_equation_provenance.md",',
    )
    text = text.replace("for number in range(1, 88):", "for number in range(1, 89):")
    text = text.replace(
        '"p87_exact_bounded_primitive_quad_projection_parity.svg"',
        '"p88_exact_expanded_bounded_primitive_quad_projection_parity.svg"',
    )
    text = text.replace('p87 = visual_atlas.index(\'id="p87-frontier"\')', 'p88 = visual_atlas.index(\'id="p88-frontier"\')\n    p87 = visual_atlas.index(\'id="p87-frontier"\')')
    text = text.replace("if not (p87 < p86 and p87 < p84 and p87 < p85):", "if not (p88 < p87 and p88 < p86 and p88 < p84 and p88 < p85):")
    text = text.replace("Visual Atlas does not lead with the current P87 figure", "Visual Atlas does not lead with the current P88 figure")
    write(path, text)

    path = "scripts/prepare_website.py"
    text = read(path)
    text = text.replace('CURRENT_FRONTIER_FIGURE = "p87_exact_bounded_primitive_quad_projection_parity.svg"', f'CURRENT_FRONTIER_FIGURE = "{P88_FIGURE}"')
    text = text.replace('CURRENT_RECORD_TEXT = "Current record:</strong> 87 proposition-level results through P87"', 'CURRENT_RECORD_TEXT = "Current record:</strong> 88 proposition-level results through P88"')
    text = re.sub(r'ASSET_VERSION = "[^"]+"', 'ASSET_VERSION = "20260913-mobile18-p88"', text, count=1)
    text = text.replace("internally consistent with P87", "internally consistent with P88")
    text = text.replace("current P87 theorem figure", "current P88 theorem figure")
    text = text.replace("bundled P87 theorem figure", "bundled P88 theorem figure")
    text = text.replace("P87 theorem figure", "P88 theorem figure")
    text = text.replace("p87_atlas = visual_atlas.index('id=\"p87-frontier\"')", "p88_atlas = visual_atlas.index('id=\"p88-frontier\"')")
    text = text.replace("if p87_atlas >= visual_atlas.index(marker):", "if p88_atlas >= visual_atlas.index(marker):")
    text = text.replace("Visual Atlas does not present P87 before", "Visual Atlas does not present P88 before")
    text = text.replace("('id=\"p86-frontier\"', 'id=\"p85-frontier\"')", "('id=\"p87-frontier\"', 'id=\"p86-frontier\"', 'id=\"p85-frontier\"')")
    text = text.replace("p87 = homepage.index('id=\"p87-frontier\"')", "p88 = homepage.index('id=\"p88-frontier\"')")
    text = text.replace("if p87 >= homepage.index(marker):", "if p88 >= homepage.index(marker):")
    text = text.replace("Homepage P87 frontier appears too late", "Homepage P88 frontier appears too late")
    text = text.replace("'id=\"p86-frontier\"',", "'id=\"p87-frontier\"',\n        'id=\"p86-frontier\"',")
    text = text.replace("87/P87", "88/P88")
    write(path, text)


def promote_figure_synchronizer() -> None:
    path = "scripts/sync_figure_publication.py"
    text = read(path)
    text = text.replace("if frontier == 87:", "if frontier == 88:")
    text = text.replace('"### Exact P87 hierarchy witness"', '"### Exact P88 hierarchy witness"')
    text = text.replace(
        '"P87 completes the primitive four-event coefficient box with nonzero integer coefficients satisfying `|c_i| <= 2` and strictly strengthens the complete P86 certificate on the exact rational witness:"',
        '"P88 completes the first larger primitive four-event coefficient box with nonzero integer coefficients satisfying `|c_i| <= 3` and strictly strengthens the complete P87 certificate on the exact rational witness:"',
    )
    text = text.replace('"L85 = 0 < L86 = 1/192 < L87 = 1/96"', '"L85 = 0 < L86 = 1/192 < L87 = 1/96 < L88 = 1/64"')
    text = text.replace('"120 primitive sign-normalized coefficient patterns per four-event subset"', '"632 primitive sign-normalized coefficient patterns per four-event subset"')
    text = text.replace('"39,600 standard P87 functionals"', '"208,560 standard P88 functionals"')

    start = text.index("def _p87_visual_section() -> str:")
    end = text.index("\n\ndef _remove_section", start)
    new_visual = f'''def _p88_visual_section() -> str:\n    return f\'\'\'<section id="p88-frontier" class="theorem-frontier current-frontier-visual">\n  <div class="section-head">\n    <p class="eyebrow">Current theorem frontier · P88</p>\n    <h2>Expanded bounded primitive four-event parity certificate</h2>\n    <p>P88 completes the primitive coefficient box with |c_i| at most 3 at the same four-event order. Its 208,560-function exact audit strictly strengthens the complete P87 certificate on the same rational witness.</p>\n  </div>\n  <div class="theorem-figure-shell">\n    <a href="{{BLOB_PREFIX}}docs/figures/{P88_FIGURE}" aria-label="Open the full P88 theorem figure">\n      <img loading="eager" decoding="async" src="{{RAW_FIGURE_PREFIX}}{P88_FIGURE}" alt="P88 expanded bounded primitive four-event parity certificate showing L87 equals one over 96 and L88 equals one over 64" />\n    </a>\n  </div>\n  <div class="frontier-summary-grid">\n    <article class="frontier-summary-card"><h3>Complete expanded family</h3><p>632 primitive sign-normalized coefficient patterns per four-event subset yield 208,560 exact P88 functionals.</p></article>\n    <article class="frontier-summary-card"><h3>Strict hierarchy</h3><p>The exact witness has <strong>L85 = 0 &lt; L86 = 1/192 &lt; L87 = 1/96 &lt; L88 = 1/64</strong>.</p></article>\n    <article class="frontier-summary-card"><h3>Reproducible record</h3><p>The proof, provenance, exact implementation, exhaustive tests, theorem SVG, and figure manifest are source controlled.</p></article>\n  </div>\n  <div class="boundary"><p><strong>Scientific boundary:</strong> P88 is a conditional exact model-separation theorem for the declared P75 family. It does not identify consciousness, establish nonphysicality, or close the physical-to-experiential bridge.</p></div>\n  <p><a href="{{BLOB_PREFIX}}docs/{P88_PROOF}">Open the P88 theorem</a> · <a href="{{BLOB_PREFIX}}docs/p88_equation_provenance.md">Equation provenance</a> · <a href="{{BLOB_PREFIX}}src/consciousness_bridge/{P88_SOURCE}">Implementation</a> · <a href="{{BLOB_PREFIX}}tests/{P88_TEST}">Exact tests</a></p>\n</section>\'\'\'\n'''
    text = text[:start] + new_visual + text[end:]
    text = text.replace("def _demote_p86(text: str) -> str:", "def _demote_p87(text: str) -> str:")
    text = text.replace('"Current theorem frontier · P86",\n        "Previous theorem frontier · P86",', '"Current theorem frontier · P87",\n        "Previous theorem frontier · P87",')

    start = text.index("def _normalize_visual_atlas(text: str) -> str:")
    end = text.index("\n\ndef _normalize_homepage", start)
    new_atlas = '''def _normalize_visual_atlas(text: str) -> str:\n    text = _remove_section(text, "p88-frontier")\n    text = _demote_p87(text)\n    text = re.sub(r"\\s*<!-- current-frontier-visual: P\\d+ -->\\s*", "\\n", text)\n    boundary = re.search(r'<section class="boundary">.*?</section>', text, re.DOTALL)\n    if boundary is None:\n        raise RuntimeError("could not locate Visual Atlas reading-boundary section")\n    prefix = text[: boundary.end()].rstrip()\n    suffix = text[boundary.end() :].lstrip()\n    insertion = "\\n\\n<!-- current-frontier-visual: P88 -->\\n" + _p88_visual_section() + "\\n\\n"\n    result = prefix + insertion + suffix\n    return "\\n".join(line.rstrip() for line in result.splitlines()) + "\\n"\n'''
    text = text[:start] + new_atlas + text[end:]

    start = text.index("def _normalize_homepage(text: str) -> str:")
    end = text.index("\n\ndef _expected_outputs", start)
    new_home = '''def _normalize_homepage(text: str) -> str:\n    text = _remove_section(text, "p88-frontier")\n    text = _demote_p87(text)\n    replacements = (\n        ("The 87 results form several dependency branches.", "The 88 results form several dependency branches."),\n        ("all 87 propositions", "all 88 propositions"),\n        ("P71-P87, then read the falsification program", "P71-P88, then read the falsification program"),\n        ("Explore all 87 results", "Explore all 88 results"),\n        ("<strong>87</strong><span>proposition-level results</span>", "<strong>88</strong><span>proposition-level results</span>"),\n        ("<strong>P87</strong><span>current theorem frontier</span>", "<strong>P88</strong><span>current theorem frontier</span>"),\n        ("The 87-result program", "The 88-result program"),\n        ("P75-P87", "P75-P88"),\n        ("P71-P87:", "P71-P88:"),\n    )\n    for old, new in replacements:\n        text = text.replace(old, new)\n    text = re.sub(r"\\s*<!-- current-frontier-home: P\\d+ -->\\s*", "\\n", text)\n    hero = re.search(r'<section class="hero">.*?</section>', text, re.DOTALL)\n    if hero is None:\n        raise RuntimeError("could not locate homepage hero section")\n    prefix = text[: hero.end()].rstrip()\n    suffix = text[hero.end() :].lstrip()\n    insertion = "\\n\\n<!-- current-frontier-home: P88 -->\\n" + _p88_visual_section() + "\\n\\n"\n    result = prefix + insertion + suffix\n    return "\\n".join(line.rstrip() for line in result.splitlines()) + "\\n"\n'''
    text = text[:start] + new_home + text[end:]
    text = text.replace("if frontier != 87:", "if frontier != 88:")
    text = text.replace('raise RuntimeError(f"P87 synchronizer expected frontier 87, found {frontier}")', 'raise RuntimeError(f"P88 synchronizer expected frontier 88, found {frontier}")')
    write(path, text)


def promote_website_text() -> None:
    for path in sorted((ROOT / "website").glob("*.html")):
        text = path.read_text(encoding="utf-8")
        replacements = (
            ("87-result theorem program", "88-result theorem program"),
            ("Open all 87 results", "Open all 88 results"),
            ("Explore all 87 results", "Explore all 88 results"),
            ("<strong>87</strong><span>proposition-level results</span>", "<strong>88</strong><span>proposition-level results</span>"),
            ("<strong>P87</strong><span>current theorem frontier</span>", "<strong>P88</strong><span>current theorem frontier</span>"),
            ("The 87-result program", "The 88-result program"),
            ("The 87 propositions by scientific role", "The 88 propositions by scientific role"),
            ("P75-P87", "P75-P88"),
            ("P71-P87:", "P71-P88:"),
            ("P77-P87", "P77-P88"),
            ("P78-P87 progressively", "P78-P88 progressively"),
            ("through Proposition 87", "through Proposition 88"),
            ("current theorem frontier is P87", "current theorem frontier is P88"),
            ("Current theorem frontier is P87", "Current theorem frontier is P88"),
        )
        for old, new in replacements:
            text = replace_if_present(text, old, new)
        path.write_text(text, encoding="utf-8")

    # Start Here gets a specific current-frontier paragraph and theorem link.
    path = ROOT / "website" / "start-here.html"
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        '<p><strong>P87 is the current exact frontier.</strong> It exhausts every nonzero primitive integer four-event coefficient vector with |c_i| at most 2, modulo one global sign. The family contains 39,600 exact functionals, and on the same rational witness it gives <strong>L86 = 1/192 &lt; L87 = 1/96</strong>.</p>',
        '<p><strong>P87 is the previous exact frontier.</strong> It exhausts every nonzero primitive integer four-event coefficient vector with |c_i| at most 2, modulo one global sign. The family contains 39,600 exact functionals, and on the same rational witness it gives <strong>L86 = 1/192 &lt; L87 = 1/96</strong>.</p>\n      <p><strong>P88 is the current exact frontier.</strong> It expands the complete primitive coefficient box to |c_i| at most 3 without increasing functional order. The family contains 208,560 exact functionals, and the same rational witness gives <strong>L87 = 1/96 &lt; L88 = 1/64</strong>.</p>',
    )
    text = text.replace(
        'href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md">Read P87</a>',
        f'href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P88_PROOF}">Read P88</a>',
    )
    path.write_text(text, encoding="utf-8")

    # Sources page: demote P87 and insert a complete P88 audit card immediately before it.
    path = ROOT / "website" / "sources.html"
    text = path.read_text(encoding="utf-8")
    text = text.replace("Current theorem source · P87", "Previous theorem source · P87")
    if 'id="p88-source"' not in text:
        p87_marker = '<section id="p87-source">'
        p88 = f'''<section id="p88-source"><div class="section-head"><p class="eyebrow">Current theorem source · P88</p><h2>Exact expanded bounded primitive four-event projection-parity certificate</h2><p>P88 completes every nonzero primitive four-event coefficient vector with magnitude at most three, yielding 208,560 exact functionals and the strict hierarchy <strong>L87 = 1/96 &lt; L88 = 1/64</strong>.</p></div><div class="source-grid"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P88_PROOF}"><h3>Proposition 88</h3><p>Formal statement, exact family count, interval proof, transfer bound, strict witness, and scientific boundary.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p88_equation_provenance.md"><h3>P88 provenance</h3><p>Separates inherited parity algebra and endpoint arguments from the repository-original radius-three complete-family construction.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/{P88_SOURCE}"><h3>P88 implementation</h3><p>Exact rational exhaustive enumeration of the complete 208,560-function family.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/{P88_TEST}"><h3>P88 exact tests</h3><p>Family count, exact interval, centered norm, strict witness, dominance, and interpretation-boundary regression tests.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/{P88_FIGURE}"><h3>P88 theorem figure</h3><p>Source-controlled visual summary synchronized with the exact theorem and figure publication manifest.</p></a></div></section>\n\n'''
        text = text.replace(p87_marker, p88 + p87_marker, 1)
    path.write_text(text, encoding="utf-8")


def promote_workflows() -> None:
    for relative in (
        ".github/workflows/figures.yml",
        ".github/workflows/pages.yml",
        ".github/workflows/reproducibility.yml",
    ):
        text = read(relative)
        text = text.replace("P87", "P88")
        text = text.replace("p87_exact_bounded_primitive_quad_projection_parity.svg", P88_FIGURE)
        text = text.replace("87 proposition-level results through P88", "88 proposition-level results through P88")
        text = text.replace("87 proposition-level results", "88 proposition-level results")
        text = text.replace("39,600", "208,560")
        text = text.replace("1/96", "1/64")
        write(relative, text)


def main() -> None:
    required = (
        ROOT / "docs" / P88_PROOF,
        ROOT / "docs" / "p88_equation_provenance.md",
        ROOT / "docs" / "figures" / P88_FIGURE,
        ROOT / "src" / "consciousness_bridge" / P88_SOURCE,
        ROOT / "tests" / P88_TEST,
    )
    missing = [path.relative_to(ROOT).as_posix() for path in required if not path.is_file()]
    if missing:
        raise RuntimeError(f"cannot promote P88; missing canonical records: {missing}")

    promote_primary_reader_surfaces()
    append_p88_records()
    promote_roadmap_and_navigation()
    promote_figure_catalog_and_reproducibility()
    promote_citation_and_changelog()
    promote_verifier_and_website_builder()
    promote_figure_synchronizer()
    promote_website_text()
    promote_workflows()

    subprocess.run(["python", "scripts/sync_figure_publication.py"], cwd=ROOT, check=True)
    print("[p88-promotion] synchronized public theorem frontier to P88 / 88 results")


if __name__ == "__main__":
    main()
