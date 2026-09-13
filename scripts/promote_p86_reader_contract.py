"""Promote the public reader contract from P85 to P86 without erasing P85 history."""

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


def replace_many(text: str, replacements: dict[str, str]) -> str:
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def promote_readme() -> None:
    path = "README.md"
    text = read(path)
    text = replace_many(
        text,
        {
            "the P1-P85 program map, and the current P85 frontier": "the P1-P86 program map, and the current P86 frontier",
            "Public theorem frontier | **P85**": "Public theorem frontier | **P86**",
            "Proposition-level results | **85**": "Proposition-level results | **86**",
            "P1 to P85": "P1 to P86",
            "P1 through P85": "P1 through P86",
            "P71-P85": "P71-P86",
            "P73-P85": "P73-P86",
            "P75-P85": "P75-P86",
            "P77-P85": "P77-P86",
            "85 proposition-level results": "86 proposition-level results",
            "P85 frontier figure.": "P85 previous-frontier figure.",
        },
    )
    if "P86 asks whether adding exact four-event" not in text:
        anchor = "**P85 previous-frontier figure.**"
        pos = text.find(anchor)
        if pos < 0:
            raise RuntimeError("README P85 figure caption not found")
        end = text.find("\n\n", pos)
        if end < 0:
            raise RuntimeError("README P85 caption end not found")
        addition = """

P86 asks whether exact four-event shared-parameter parity functionals can sharpen the complete P85 certificate on the same P75 parameter box. The standard P86 audit contains 2640 sign-normalized four-event functionals. Its exact-rational strict witness has the complete `L85 = 5/48` lower bound while `Q = P(H02) - P(H23) + P(H012) - P(H123)` has empirical value `-9/8`, exact P75 interval `[0,0]`, centered coefficient norm `8`, and therefore `L86 = 9/64`. The exact hierarchy gain is `7/192`. This is a stronger conditional model-distance certificate, not an identification of the latent state with consciousness.

![P86 exact four-event projection-parity functional certificate](docs/figures/p86_exact_quadruple_projection_parity_functional.svg)

**P86 frontier figure.** P86 retains the complete P85 hierarchy and adds exact four-event shared-parameter functionals. The strict witness gives `L85 = 5/48 < L86 = 9/64`. Read the [P86 proof](docs/proposition_86_exact_quadruple_projection_parity_functional.md) and [P86 equation provenance](docs/p86_equation_provenance.md) for the exact derivation, deterministic witness search, executable audit, and interpretation boundary.
"""
        text = text[: end + 2] + addition + text[end + 2 :]
    for token in (
        "Public theorem frontier | **P86**",
        "Proposition-level results | **86**",
        "P1 through P86 with explicit dependency branches",
        "P19-P24, P71-P86",
        "proposition_86_exact_quadruple_projection_parity_functional.md",
        "p86_exact_quadruple_projection_parity_functional.svg",
    ):
        if token not in text:
            raise RuntimeError(f"README missing {token!r}")
    write(path, text)


def promote_start_here() -> None:
    path = "START_HERE.md"
    text = read(path)
    text = replace_many(
        text,
        {
            "the 85-result theorem program": "the 86-result theorem program",
            "**85 proposition-level results**": "**86 proposition-level results**",
            "The current theorem frontier is **P84**": "The current theorem frontier is **P86**",
            "P75-P84": "P75-P86",
            "P77-P84": "P77-P86",
            "P74-P84": "P74-P86",
            "## The 84 results, organized by scientific role": "## The 86 results, organized by scientific role",
            "## The current frontier: P71-P85 in plain language": "## The current frontier: P71-P86 in plain language",
            "P71-P85": "P71-P86",
            "**Proposition frontier:** P84": "**Proposition frontier:** P86",
            "**Proposition-level results:** 84": "**Proposition-level results:** 86",
            "## Current theorem frontier: P84": "## Historical frontier: P84",
            "## Current frontier: P85": "## Previous frontier: P85",
            "P85 is the current documented theorem frontier.": "P85 is the previous documented theorem frontier immediately preceding P86.",
            "P78},L_{80},L_{81},L_{82},L_{83},L_{84}": "P78},L_{80},L_{81},L_{82},L_{83},L_{84},L_{85},L_{86}",
        },
    )
    if "**P85: exact three-event parity functionals.**" not in text:
        marker = "**P84: exact joint projection parity.**"
        pos = text.find(marker)
        if pos >= 0:
            end = text.find("\n", pos)
            p85_line = "\n\n**P85: exact three-event parity functionals.** P85 adds 660 sign-normalized three-event shared-parameter functionals and can strictly improve the complete P84 certificate while remaining conditional on the declared P75 family."
            p86_line = "\n\n**P86: exact four-event parity functionals.** P86 retains the complete P85 hierarchy and adds 2640 four-event shared-parameter functionals. Its strict rational witness gives `L85 = 5/48 < L86 = 9/64`, an exact gain of `7/192`."
            text = text[:end] + p85_line + p86_line + text[end:]
    if "## Current frontier: P86" not in text:
        text += """

## Current frontier: P86

P86 is the current documented theorem frontier. It strengthens the complete P85 box certificate by adding 2640 exact sign-normalized four-event parity functionals under one shared P75 parameter assignment. The strict exact-rational witness gives `L85 = 5/48 < L86 = 9/64`, with exact improvement `7/192`.

This remains a conditional model-separation result. The physical-to-experiential bridge itself remains open.

- [P86 proof](docs/proposition_86_exact_quadruple_projection_parity_functional.md)
- [P86 equation provenance](docs/p86_equation_provenance.md)
- [P86 source](src/consciousness_bridge/quadruple_projection_parity_functional_separation.py)
- [P86 tests](tests/test_quadruple_projection_parity_functional_separation.py)
- [P86 deterministic witness search](scripts/search_p86_strict_witness.py)
- [P86 figure](docs/figures/p86_exact_quadruple_projection_parity_functional.svg)
"""
    for token in (
        "86 proposition-level results",
        "current theorem frontier is **P86**",
        "docs/proposition_86_exact_quadruple_projection_parity_functional.md",
        "## Current frontier: P86",
    ):
        if token not in text:
            raise RuntimeError(f"START_HERE missing {token!r}")
    write(path, text)


def promote_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    text = replace_many(
        text,
        {
            "current documented theorem frontier is **P85**": "current documented theorem frontier is **P86**",
            "P1 through P85": "P1 through P86",
            "P71-P85": "P71-P86",
            "After P85": "After P86",
        },
    )
    dep = "&\\text{P85: three-event parity functionals test compatibility beyond the complete P84 pairwise certificate}"
    if dep in text and "P86: four-event parity functionals" not in text:
        text = text.replace(
            dep,
            dep + "\\\\\n&\\Downarrow\\\\\n&\\text{P86: four-event parity functionals sharpen the complete P85 certificate under one shared P75 box}",
            1,
        )
    if "### P86: exact four-event projection-parity functional certificate" not in text:
        marker = "## 5. Current open frontier"
        section = """
### P86: exact four-event projection-parity functional certificate

P86 retains the complete P85 lower-bound hierarchy and adds all 2640 standard sign-normalized four-event functionals built from the eleven canonical even-parity observables. Each branch functional is multi-affine, so its exact rational box range is attained at common response-coordinate endpoints; prevalence is then extremized at its endpoints. The centered coefficient norm transfers any exact functional mismatch to a certified full-law L-infinity lower bound.

The strict rational witness has complete `L85 = 5/48`, while the four-event functional `P(H02) - P(H23) + P(H012) - P(H123)` has empirical value `-9/8`, exact P75 interval `[0,0]`, centered coefficient norm `8`, and `L86 = 9/64`. Thus `L86 - L85 = 7/192` on the same box.

Direct proof: [P86](proposition_86_exact_quadruple_projection_parity_functional.md). Provenance: [P86 equation record](p86_equation_provenance.md). Implementation: [`quadruple_projection_parity_functional_separation.py`](../src/consciousness_bridge/quadruple_projection_parity_functional_separation.py). Tests: [`test_quadruple_projection_parity_functional_separation.py`](../tests/test_quadruple_projection_parity_functional_separation.py).

P86 remains a conditional model-separation theorem for the declared P75 family. It does not identify a latent state with consciousness or close the physical-to-experiential bridge.

"""
        if marker not in text:
            raise RuntimeError("roadmap open-frontier marker missing")
        text = text.replace(marker, section + marker, 1)
    for token in (
        "current documented theorem frontier is **P86**",
        "After P86",
        "proposition_86_exact_quadruple_projection_parity_functional.md",
        "p86_equation_provenance.md",
    ):
        if token not in text:
            raise RuntimeError(f"roadmap missing {token!r}")
    write(path, text)


def promote_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    text = replace_many(
        text,
        {
            "current documented theorem frontier is **P85**": "current documented theorem frontier is **P86**",
            "P1 through P85": "P1 through P86",
            "P71-P85": "P71-P86",
            "Current frontier provenance:** [P85 equation and provenance record](p85_equation_provenance.md)": "Current frontier provenance:** [P86 equation and provenance record](p86_equation_provenance.md)",
        },
    )
    p85_read = "[P85 exact three-event projection-parity functional](proposition_85_exact_triple_projection_parity_functional.md)"
    if p85_read in text and "[P86 exact four-event projection-parity functional]" not in text:
        idx = text.find(p85_read)
        line_end = text.find("\n", idx)
        addition = "\n22. [P86 exact four-event projection-parity functional](proposition_86_exact_quadruple_projection_parity_functional.md) for the next hierarchy step: 2640 exact four-event functionals, P86 >= P85 pointwise, and the strict `5/48 < 9/64` complete-certificate witness."
        text = text[:line_end] + addition + text[line_end:]
    p85_prov = "[P85 equation and provenance record](p85_equation_provenance.md)"
    if p85_prov in text and "[P86 equation and provenance record](p86_equation_provenance.md) for exact four-event" not in text:
        idx = text.find(p85_prov)
        line_end = text.find("\n", idx)
        addition = "\n37. [P86 equation and provenance record](p86_equation_provenance.md) for exact four-event common-parameter extrema, centered coefficient transfer, strict P86 > P85 provenance, and the interpretation boundary."
        text = text[:line_end] + addition + text[line_end:]
    p85_branch = "| Three-event projection-parity functional separation | P85 | Adds 660 exact signed three-event parity functionals that test shared-parameter compatibility beyond the complete P84 pairwise certificate | [P85](proposition_85_exact_triple_projection_parity_functional.md) |"
    if p85_branch in text and "| Four-event projection-parity functional separation | P86 |" not in text:
        text = text.replace(
            p85_branch,
            p85_branch + "\n| Four-event projection-parity functional separation | P86 | Adds 2640 exact signed four-event parity functionals and can strictly sharpen the complete P85 certificate on the same rational P75 box | [P86](proposition_86_exact_quadruple_projection_parity_functional.md) |",
            1,
        )
    p85_index = re.search(r"^\| P85 \|.*$", text, flags=re.MULTILINE)
    if p85_index and not re.search(r"^\| P86 \|", text, flags=re.MULTILINE):
        row = "| P86 | [Exact four-event projection-parity functional certificate](proposition_86_exact_quadruple_projection_parity_functional.md) | 2640 exact four-event shared-parameter functionals and strict complete-P85 hierarchy improvement |"
        text = text[: p85_index.end()] + "\n" + row + text[p85_index.end() :]
    for token in (
        "current documented theorem frontier is **P86**",
        "P71-P86",
        "| P86 |",
        "proposition_86_exact_quadruple_projection_parity_functional.md",
        "p86_equation_provenance.md",
    ):
        if token not in text:
            raise RuntimeError(f"navigation missing {token!r}")
    write(path, text)


def promote_detail() -> None:
    path = "docs/detailed_proposition_record.md"
    text = read(path).replace("Complete P1 to P85 chronology", "Complete P1 to P86 chronology")
    if "## P86: exact four-event projection-parity functional certificate" not in text:
        text += """

## P86: exact four-event projection-parity functional certificate

**Question.** Can exact four-event shared-parameter parity relations sharpen the complete P85 certificate on the same rational P75 parameter box?

**Result.** Yes. P86 audits 2640 sign-normalized four-event functionals and defines `L86` as the maximum of the complete P85 lower bound and the strongest new four-event transfer. The construction is pointwise never weaker than P85. An exact-rational witness has `L85 = 5/48`, while one four-event functional has empirical value `-9/8`, exact P75 interval `[0,0]`, centered coefficient norm `8`, and therefore `L86 = 9/64`, with exact gain `7/192`.

**Scientific boundary.** This is a conditional model-separation theorem for the declared P75 family. It does not identify a latent state with consciousness, validate an alternative model, or close the physical-to-experiential bridge.

- Proof: [`proposition_86_exact_quadruple_projection_parity_functional.md`](proposition_86_exact_quadruple_projection_parity_functional.md)
- Provenance: [`p86_equation_provenance.md`](p86_equation_provenance.md)
- Source: [`quadruple_projection_parity_functional_separation.py`](../src/consciousness_bridge/quadruple_projection_parity_functional_separation.py)
- Tests: [`test_quadruple_projection_parity_functional_separation.py`](../tests/test_quadruple_projection_parity_functional_separation.py)
- Search: [`search_p86_strict_witness.py`](../scripts/search_p86_strict_witness.py)
"""
    if "Complete P1 to P86 chronology" not in text:
        raise RuntimeError("detailed chronology was not promoted")
    write(path, text)


def promote_citations() -> None:
    for path in ("CITATION.cff", "CITATION.md", "CITATION.bib"):
        text = read(path)
        text = replace_many(
            text,
            {
                "Current documented theorem frontier: P85": "Current documented theorem frontier: P86",
                "current documented theorem frontier: P85": "current documented theorem frontier: P86",
                "current theorem frontier P85": "current theorem frontier P86",
                "frontier P85": "frontier P86",
            },
        )
        if path == "CITATION.md" and "P86" not in text:
            text += "\n\nCurrent documented theorem frontier: **P86**, with the exact four-event projection-parity functional certificate recorded in `docs/proposition_86_exact_quadruple_projection_parity_functional.md`.\n"
        write(path, text)


def p86_home_section() -> str:
    return '''<section id="p86-frontier" class="theorem-frontier">
  <div class="section-head">
    <p class="eyebrow">Current theorem frontier · P86</p>
    <h2>P86 in plain language: four linked parity relations can sharpen the complete P85 certificate</h2>
    <p>P86 retains every lower bound already available through P85, then audits 2640 exact four-event shared-parameter parity functionals. Its strict rational witness raises the complete certificate from 5/48 to 9/64 on the same P75 parameter box.</p>
  </div>
  <div class="theorem-figure-shell">
    <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p86_exact_quadruple_projection_parity_functional.svg" aria-label="Open the full P86 theorem figure"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p86_exact_quadruple_projection_parity_functional.svg?v=1" alt="P86 exact four-event shared-parameter parity certificate" /></a>
  </div>
  <div class="frontier-summary-grid">
    <article class="result"><span>2640</span><h3>Exact four-event functionals</h3><p>P86 audits every sign-normalized four-event choice from the eleven canonical even-parity observables.</p></article>
    <article class="result"><span>Exact</span><h3>Shared-parameter ranges</h3><p>Multi-affine branch extrema occur at common response-coordinate endpoints, followed by exact prevalence-endpoint extremization.</p></article>
    <article class="result"><span>9/64</span><h3>Strict certified separation</h3><p>The witness has complete P85 = 5/48, empirical functional -9/8, P75 interval [0,0], centered coefficient norm 8, and exact gain 7/192.</p></article>
  </div>
  <div class="two-col">
    <div><h3>What it adds</h3><p>P86 preserves the complete P85 hierarchy and adds a higher-order exact lower-bound family. On the strict witness, the new four-event certificate is strictly sharper than every inherited P85 certificate combined.</p></div>
    <aside class="card"><h3>What it does not establish</h3><p>The result is conditional on the declared P75 latent model. It does not identify the latent state with consciousness, validate an alternative model, or close the physical-to-experiential bridge.</p></aside>
  </div>
  <div class="frontier-actions"><a class="button primary" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_86_exact_quadruple_projection_parity_functional.md">Read the P86 proof</a><a class="button" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p86_equation_provenance.md">Audit equation provenance</a></div>
</section>'''


def promote_homepage() -> None:
    path = "website/index.html"
    text = read(path)
    text = replace_many(
        text,
        {
            "Explore all 85 results": "Explore all 86 results",
            "<strong>85</strong><span>proposition-level results</span>": "<strong>86</strong><span>proposition-level results</span>",
            "<strong>P85</strong><span>current theorem frontier</span>": "<strong>P86</strong><span>current theorem frontier</span>",
            "The 85-result program": "The 86-result program",
            "85 proposition-level results through P85": "86 proposition-level results through P86",
            "P73-P85": "P73-P86",
            "P75-P85": "P75-P86",
            "P71-P85:": "P71-P86:",
            "Current theorem frontier · P85": "Previous theorem frontier · P85",
        },
    )
    if 'id="p86-frontier"' not in text:
        pattern = re.compile(r'<section id="p85-frontier" class="theorem-frontier">.*?</section>', re.DOTALL)
        match = pattern.search(text)
        if not match:
            raise RuntimeError("homepage P85 section not found")
        text = text[: match.end()] + "\n\n" + p86_home_section() + text[match.end() :]
    for token in (
        "Explore all 86 results",
        "<strong>86</strong><span>proposition-level results</span>",
        "<strong>P86</strong><span>current theorem frontier</span>",
        "The 86-result program",
        "P75-P86",
        "P71-P86:",
        "p86_exact_quadruple_projection_parity_functional.svg",
        "proposition_86_exact_quadruple_projection_parity_functional.md",
    ):
        if token not in text:
            raise RuntimeError(f"homepage missing {token!r}")
    write(path, text)


def promote_atlas() -> None:
    path = "website/visual-atlas.html"
    text = read(path).replace("Current theorem frontier · P85", "Previous theorem frontier · P85")
    if 'id="p86-frontier"' not in text:
        p85 = re.search(r'<section id="p85-frontier".*?</section>', text, flags=re.DOTALL)
        if not p85:
            raise RuntimeError("atlas P85 section not found")
        section = '''<section id="p86-frontier" class="theorem-frontier">
  <div class="section-head"><p class="eyebrow">Current theorem frontier · P86</p><h2>Exact four-event shared-parameter parity functionals</h2><p>The figure records the 2640-function audit and the exact strict hierarchy witness `L85 = 5/48 < L86 = 9/64`.</p></div>
  <div class="theorem-figure-shell"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p86_exact_quadruple_projection_parity_functional.svg" aria-label="Open the full P86 theorem figure"><img loading="lazy" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p86_exact_quadruple_projection_parity_functional.svg?v=1" alt="P86 exact four-event shared-parameter parity certificate" /></a></div>
  <div class="frontier-summary-grid"><article class="frontier-summary-card"><h3>Family</h3><p>2640 sign-normalized four-event functionals preserve one shared P75 parameter assignment.</p></article><article class="frontier-summary-card"><h3>Exact witness</h3><p>Q(empirical) = -9/8, Q(P75 box) = 0, D(Q) = 8, hence the new bound is 9/64.</p></article><article class="frontier-summary-card"><h3>Hierarchy</h3><p>Complete P85 is 5/48 on the same box, so P86 improves the certificate by 7/192.</p></article></div>
  <div class="frontier-actions"><a class="button" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_86_exact_quadruple_projection_parity_functional.md">Open the P86 theorem</a></div>
</section>'''
        text = text[: p85.end()] + "\n\n" + section + text[p85.end() :]
    if text.count("Current theorem frontier") != 1:
        raise RuntimeError("atlas must expose exactly one current theorem frontier")
    write(path, text)


def promote_secondary_website() -> None:
    replacements = {
        "<strong>85</strong><span>proposition-level results</span>": "<strong>86</strong><span>proposition-level results</span>",
        "<strong>P85</strong><span>current theorem frontier</span>": "<strong>P86</strong><span>current theorem frontier</span>",
        "What the 85 results are doing": "What the 86 results are doing",
        "Eighty-five results": "Eighty-six results",
        "through Proposition 85": "through Proposition 86",
        "P73-P85": "P73-P86",
        "P75-P85": "P75-P86",
        "P77-P85": "P77-P86",
        "P78-P85": "P78-P86",
        "actual P85 research frontier": "actual P86 research frontier",
        "shows how all 85 results connect": "shows how all 86 results connect",
        "Continue to the current P85 frontier": "Continue to the current P86 frontier",
        'href="index.html#p85-frontier">Continue to the current P86 frontier': 'href="index.html#p86-frontier">Continue to the current P86 frontier',
    }
    for path in (
        "website/plain-language.html",
        "website/start-here.html",
        "website/research-map.html",
        "website/implementation.html",
    ):
        text = replace_many(read(path), replacements)
        if path == "website/start-here.html" and "P86 strengthens the complete P85 certificate" not in text:
            marker = "</main>"
            addition = '<section class="boundary"><h2>Current P86 frontier</h2><p><strong>P86 strengthens the complete P85 certificate</strong> with 2640 exact four-event shared-parameter parity functionals. The strict rational witness gives L85 = 5/48 &lt; L86 = 9/64, while the physical-to-experiential bridge remains open.</p></section>\n'
            text = text.replace(marker, addition + marker, 1)
        if path == "website/plain-language.html" and "four-event" not in text:
            text = text.replace("</main>", '<section class="boundary"><h2>P86 in one sentence</h2><p>P86 adds exact four-event shared-parameter parity relations and can certify a strictly sharper P75 model-distance lower bound than the complete P85 hierarchy, without making an ontological claim about consciousness.</p></section>\n</main>', 1)
        if path == "website/research-map.html" and "9/64" not in text:
            text = text.replace("</main>", '<section id="p86"><p class="eyebrow">Current certified frontier · P86</p><h2>P86: exact four-event shared-parameter parity functionals</h2><p>The 2640-function exact audit preserves the complete P85 hierarchy and has a strict rational witness with L85 = 5/48 &lt; L86 = 9/64, an exact gain of 7/192.</p><p><a class="button primary" href="index.html#p86-frontier">Open the P86 frontier figure</a></p></section>\n</main>', 1)
        if path == "website/implementation.html" and "quadruple_projection_parity_functional_separation.py" not in text:
            text = text.replace("</main>", '<section><div class="section-head"><p class="eyebrow">P86 executable frontier</p><h2>Exact four-event parity functionals</h2></div><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/quadruple_projection_parity_functional_separation.py">quadruple_projection_parity_functional_separation.py</a> implements the 2640-function exact P86 box certificate and its branch-and-bound wrapper.</p></section>\n</main>', 1)
        write(path, text)


def promote_reference_maps() -> None:
    additions = {
        "docs/equation_and_citation_map.md": """

## P86 exact four-event projection-parity functional certificate

- Proof: [P86](proposition_86_exact_quadruple_projection_parity_functional.md)
- Provenance: [P86 equation record](p86_equation_provenance.md)
- Implementation: [`quadruple_projection_parity_functional_separation.py`](../src/consciousness_bridge/quadruple_projection_parity_functional_separation.py)
- Exact audit: 2640 sign-normalized four-event functionals, with strict complete-certificate witness `L85 = 5/48 < L86 = 9/64`.
""",
        "docs/figure_catalog.md": """

## P86 exact four-event projection-parity functional certificate

![P86 exact four-event projection-parity functional certificate](figures/p86_exact_quadruple_projection_parity_functional.svg)

**What it shows.** The 2640-function P86 audit, exact witness functional, P75 interval `[0,0]`, centered coefficient norm `8`, complete `L85 = 5/48`, `L86 = 9/64`, and strict gain `7/192`.

**Scientific status.** Conditional exact P75 model-separation theorem; no latent-state identification with consciousness is asserted.
""",
        "docs/figures/README.md": """

### P86 exact four-event projection-parity functional certificate

`p86_exact_quadruple_projection_parity_functional.svg` visualizes the current P86 theorem frontier: 2640 exact four-event shared-parameter functionals and the strict complete-certificate hierarchy witness `L85 = 5/48 < L86 = 9/64`.
""",
    }
    for path, addition in additions.items():
        text = read(path)
        if "p86_exact_quadruple_projection_parity_functional.svg" not in text:
            text += addition
        write(path, text)


def promote_verifier() -> None:
    path = "scripts/verify_repository.py"
    text = read(path)
    text = text.replace('CURRENT_FRONTIER = "P85"', 'CURRENT_FRONTIER = "P86"')
    text = text.replace("for number in range(1, 86):", "for number in range(1, 87):")
    p85_core = '    "docs/p85_equation_provenance.md",\n'
    p86_core = (
        p85_core
        + '    "docs/proposition_86_exact_quadruple_projection_parity_functional.md",\n'
        + '    "docs/p86_equation_provenance.md",\n'
        + '    "docs/figures/p86_exact_quadruple_projection_parity_functional.svg",\n'
        + '    "scripts/search_p86_strict_witness.py",\n'
    )
    if "proposition_86_exact_quadruple_projection_parity_functional.md" not in text:
        if p85_core not in text:
            raise RuntimeError("verifier P85 core marker missing")
        text = text.replace(p85_core, p86_core, 1)
    text = replace_many(
        text,
        {
            '"<strong>85</strong><span>proposition-level results</span>"': '"<strong>85</strong><span>proposition-level results</span>",\n        "<strong>P85</strong><span>current theorem frontier</span>",\n        "current P85 frontier",\n        "through Proposition 85",\n        "Eighty-five results"',
        },
    )
    if 'CURRENT_FRONTIER = "P86"' not in text or "range(1, 87)" not in text:
        raise RuntimeError("verifier P86 promotion failed")
    write(path, text)


def main() -> None:
    promote_readme()
    promote_start_here()
    promote_roadmap()
    promote_navigation()
    promote_detail()
    promote_citations()
    promote_homepage()
    promote_atlas()
    promote_secondary_website()
    promote_reference_maps()
    promote_verifier()
    print("P86 publication contract promoted")


if __name__ == "__main__":
    main()
