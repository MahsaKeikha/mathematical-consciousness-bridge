"""Synchronize all public research surfaces with the P86 theorem frontier.

This maintenance script is intentionally idempotent. It promotes only current
frontier/count language, preserves P85 as a historical theorem frontier, adds
P86 proof/provenance/figure links, and hardens the repository verifier against
future P85-current publication regressions.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

P86_PROOF = "proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md"
P86_PROVENANCE = "p86_equation_provenance.md"
P86_FIGURE = "p86_exact_minimally_weighted_quad_projection_parity.svg"
P86_SOURCE = "weighted_quad_projection_parity_functional_separation.py"
P86_TEST = "test_weighted_quad_projection_parity_functional_separation.py"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    if "\u2013" in text or "\u2014" in text:
        raise RuntimeError(f"forbidden en/em dash introduced in {path}")
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
            "complete P1 to P85 detailed proposition record": "complete P1 to P86 detailed proposition record",
            "contains **85 proposition-level results**": "contains **86 proposition-level results**",
            "The theorem frontier is P85.": "The theorem frontier is P86.",
            "P71-P85 formalize": "P71-P86 formalize",
            "**P19-P24, P71-P85**": "**P19-P24, P71-P86**",
            "spans P1 through P85 with explicit dependency branches": "spans P1 through P86 with explicit dependency branches",
            "Later P61-P70 and P71-P85 are": "Later P61-P70 and P71-P86 are",
        },
    )
    if "## Current theorem frontier: P86" not in text:
        text += f'''\n\n---\n\n## Current theorem frontier: P86\n\nP86 strengthens the complete P85 certificate with the smallest non-uniform primitive weighted four-event parity family. It exhausts 10,560 exact functionals with coefficient magnitudes `{{1,1,1,2}}`. On the exact rational hierarchy witness, the complete P85 certificate is silent while P86 certifies `L85 = 0 < L86 = 1/192`. This remains a conditional rejection certificate for the declared P75 latent measurement family and does not identify any latent state with consciousness or close the physical-to-experiential bridge.\n\n![P86 exact minimally weighted four-event projection-parity certificate](docs/figures/{P86_FIGURE})\n\n**P86 frontier figure.** The figure shows why lower-order unit-weight compatibility need not exhaust shared-parameter linear structure, the exact multi-affine box interval, centered full-law transfer, and the strict rational witness.\n\n- [P86 proof](docs/{P86_PROOF})\n- [P86 equation provenance](docs/{P86_PROVENANCE})\n- [P86 implementation](src/consciousness_bridge/{P86_SOURCE})\n- [P86 tests](tests/{P86_TEST})\n'''
    for token in (
        "Public theorem frontier | **P86**",
        "Proposition-level results | **86**",
        "P1 through P86 with explicit dependency branches",
        P86_PROOF,
        P86_FIGURE,
    ):
        if token not in text:
            raise RuntimeError(f"README missing P86 token {token!r}")
    write(path, text)


def promote_start_here() -> None:
    path = "START_HERE.md"
    text = read(path)
    text = replace_many(
        text,
        {
            "the 85-result theorem program": "the 86-result theorem program",
            "contains **85 proposition-level results**": "contains **86 proposition-level results**",
            "current theorem frontier is **P84**": "current theorem frontier is **P86**",
            "current theorem frontier is **P85**": "current theorem frontier is **P86**",
            "P77-P84": "P77-P86",
            "P77-P85": "P77-P86",
            "P75-P84": "P75-P86",
            "P75-P85": "P75-P86",
            "P71-P85": "P71-P86",
            "## The 84 results, organized by scientific role": "## The 86 results, organized by scientific role",
            "**Proposition frontier:** P84": "**Proposition frontier:** P86",
            "**Proposition frontier:** P85": "**Proposition frontier:** P86",
            "**Proposition-level results:** 84": "**Proposition-level results:** 86",
            "**Proposition-level results:** 85": "**Proposition-level results:** 86",
            "## Current theorem frontier: P84": "## Previous theorem frontier: P84",
            "## Current frontier: P85": "## Previous theorem frontier: P85",
            "current documented theorem frontier. It strengthens P84": "previous documented theorem frontier. It strengthens P84",
        },
    )
    if "## Current frontier: P86" not in text:
        text += f'''\n\n## Current frontier: P86\n\nP86 is the current documented theorem frontier. It tests 10,560 exact minimally weighted four-event parity functionals with primitive coefficient magnitudes `{{1,1,1,2}}` under one shared P75 parameter assignment. The strict exact-rational witness has the complete `L85 = 0` certificate while P86 gives `L86 = 1/192`.\n\nThis is a stronger conditional model-separation certificate, not an identification of consciousness. The physical-to-experiential bridge remains open.\n\n- [P86 proof](docs/{P86_PROOF})\n- [P86 equation provenance](docs/{P86_PROVENANCE})\n- [P86 source](src/consciousness_bridge/{P86_SOURCE})\n- [P86 tests](tests/{P86_TEST})\n- [P86 figure](docs/figures/{P86_FIGURE})\n'''
    if "86 proposition-level results" not in text or "P86" not in text:
        raise RuntimeError("START_HERE.md did not promote to P86")
    write(path, text)


def promote_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    text = replace_many(
        text,
        {
            "current documented theorem frontier is **P85**": "current documented theorem frontier is **P86**",
            "record runs from **P1 through P85**": "record runs from **P1 through P86**",
            "P71-P85 form": "P71-P86 form",
            "dependency structure from P1 through P85": "dependency structure from P1 through P86",
            "**Current frontier provenance:** [P85 equation and provenance record](p85_equation_provenance.md).": "**Previous frontier provenance:** [P85 equation and provenance record](p85_equation_provenance.md).\n\n**Current frontier provenance:** [P86 equation and provenance record](p86_equation_provenance.md).",
        },
    )
    if "| P86 |" not in text:
        text += f'''\n\n## P86 current frontier record\n\n| Proposition | Direct proof | Main role |\n| --- | --- | --- |\n| P86 | [Exact minimally weighted four-event projection-parity functional]({P86_PROOF}) | 10,560 exact `{{1,1,1,2}}` weighted four-event shared-parameter functionals; strict `L85 = 0 < L86 = 1/192` hierarchy witness |\n\n- [P86 equation and provenance record]({P86_PROVENANCE})\n- [P86 implementation](../src/consciousness_bridge/{P86_SOURCE})\n- [P86 regression tests](../tests/{P86_TEST})\n- [P86 theorem figure](figures/{P86_FIGURE})\n\nP85 remains the previous theorem frontier and its proof, figure, implementation, and exact witness remain part of the permanent scientific record.\n'''
    for token in ("current documented theorem frontier is **P86**", "| P86 |", P86_PROOF, P86_PROVENANCE):
        if token not in text:
            raise RuntimeError(f"research navigation missing {token!r}")
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
    if P86_PROOF not in text:
        text += f'''\n\n## P86: minimally weighted four-event parity-functional separation\n\nP86 extends the shared-parameter parity hierarchy beyond the complete P85 triple-functional certificate. For four distinct canonical even-parity observables it uses the smallest non-uniform primitive coefficient magnitude multiset `{{1,1,1,2}}`, yielding 10,560 sign-normalized functionals. Every functional remains multi-affine in the P75 branch response coordinates, so its rational parameter-box interval is exact at common endpoint vertices; mass-conservation centering transfers any interval mismatch to a sound full-law L-infinity lower bound.\n\nThe exact strict witness has `L85 = 0 < L86 = 1/192`. P86 is a conditional model-separation theorem and does not identify the latent variable with consciousness.\n\n- Proof: [{P86_PROOF}]({P86_PROOF})\n- Provenance: [{P86_PROVENANCE}]({P86_PROVENANCE})\n- Figure: [P86 weighted four-event certificate](figures/{P86_FIGURE})\n- Source: [`{P86_SOURCE}`](../src/consciousness_bridge/{P86_SOURCE})\n- Tests: [`{P86_TEST}`](../tests/{P86_TEST})\n\n## After P86\n\nThe next frontier should not be inferred merely by increasing functional order. Any P87 claim must close a separately stated mathematical or scientific gap and must include a strict or otherwise informative certificate that is not already implied by P86.\n'''
    for token in ("current documented theorem frontier is **P86**", "After P86", P86_PROOF, P86_PROVENANCE):
        if token not in text:
            raise RuntimeError(f"theorem roadmap missing {token!r}")
    write(path, text)


def promote_detailed_record() -> None:
    path = "docs/detailed_proposition_record.md"
    text = read(path)
    text = text.replace("## Complete P1 to P85 chronology", "## Complete P1 to P86 chronology")
    if "## Proposition 86" not in text:
        text += f'''\n\n## Proposition 86: Exact minimally weighted four-event projection-parity functional certificate\n\n**Scientific question.** Can the complete P85 unit-weight one-, pair-, and triple-parity certificate remain silent while a minimally non-uniform weighted relation among four parity observables is incompatible with one shared P75 parameter assignment?\n\n**Result.** Yes. P86 exhausts 10,560 exact four-event functionals with primitive coefficient magnitudes `{{1,1,1,2}}`. Multi-affinity gives exact rational P75 box intervals at endpoint vertices, and exact mass-conservation centering transfers functional mismatch to full-law L-infinity distance. The strict rational witness satisfies `L85 = 0 < L86 = 1/192`.\n\n**Boundary.** This rejects only the declared P75 family under its assumptions. It does not identify a latent state with consciousness or close the physical-to-experiential bridge.\n\n- Proof: [`{P86_PROOF}`]({P86_PROOF})\n- Provenance: [`{P86_PROVENANCE}`]({P86_PROVENANCE})\n- Implementation: [`{P86_SOURCE}`](../src/consciousness_bridge/{P86_SOURCE})\n- Tests: [`{P86_TEST}`](../tests/{P86_TEST})\n- Figure: [`{P86_FIGURE}`](figures/{P86_FIGURE})\n'''
    if "Complete P1 to P86 chronology" not in text:
        raise RuntimeError("detailed proposition record still lacks P86 chronology")
    write(path, text)


def promote_citations() -> None:
    path = "CITATION.cff"
    text = read(path)
    text = text.replace("Current documented theorem frontier: P85", "Current documented theorem frontier: P86")
    if "Proposition 86 adds" not in text:
        text = text.replace(
            "The downstream calibration branch includes lower-bounded heterogeneous calibration and exact primal-dual gap decomposition through P70.",
            "Proposition 86 adds 10,560 exact minimally weighted four-event parity functionals with primitive coefficient magnitudes {1,1,1,2}; its strict exact-rational witness has the complete P85 certificate equal to zero while P86 equals one one-hundred-ninety-second. The downstream calibration branch includes lower-bounded heterogeneous calibration and exact primal-dual gap decomposition through P70.",
        )
    write(path, text)

    path = "CITATION.md"
    text = read(path)
    text = replace_many(
        text,
        {
            "current documented frontier, P84": "current documented frontier, P86",
            "Current documented theorem frontier: P84": "Current documented theorem frontier: P86",
            "theorem frontier **P84**": "theorem frontier **P86**",
            "P1 through P84 chronological theorem record": "P1 through P86 chronological theorem record",
        },
    )
    if "## Proposition 86 method citation" not in text:
        text += f'''\n\n## Proposition 86 method citation\n\nFor work using the minimally weighted four-event shared-parameter parity certificate, cite the program together with **Proposition 86: Exact Minimally Weighted Four-Event Projection-Parity Functional Certificate**. P86 exhausts 10,560 exact functionals with primitive coefficient magnitudes `{{1,1,1,2}}` and includes the strict exact-rational hierarchy witness `L85 = 0 < L86 = 1/192`.\n\n- [P86 proof](docs/{P86_PROOF})\n- [P86 equation provenance](docs/{P86_PROVENANCE})\n\nP86 is conditional on the declared P75 model and should not be cited as an identification or definition of consciousness.\n'''
    write(path, text)

    path = "CITATION.bib"
    text = read(path)
    text = text.replace("Current documented theorem frontier: P85", "Current documented theorem frontier: P86")
    text = text.replace("Current documented theorem frontier: P84", "Current documented theorem frontier: P86")
    write(path, text)


def p86_home_section() -> str:
    return f'''\n    <section id="p86-frontier" class="theorem-frontier">\n      <div class="section-head">\n        <p class="eyebrow">Current theorem frontier · P86</p>\n        <h2>P86: minimally weighted four-event shared-parameter parity separation</h2>\n        <p>P86 goes beyond the complete P85 triple-functional certificate by testing the smallest non-uniform primitive four-event coefficient family, with magnitudes {{1,1,1,2}}. The standard audit contains 10,560 exact functionals.</p>\n      </div>\n      <div class="theorem-figure-shell">\n        <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/{P86_FIGURE}" aria-label="Open the full P86 theorem figure">\n          <img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/{P86_FIGURE}" alt="P86 exact minimally weighted four-event parity certificate with L85 zero and L86 one over 192" />\n        </a>\n      </div>\n      <div class="frontier-summary-grid">\n        <article class="frontier-summary-card"><h3>What changes at P86</h3><p>P85 uses unit-magnitude signed triples. P86 permits the first non-uniform primitive weighting across four distinct canonical parity observables while preserving one shared P75 parameter assignment.</p></article>\n        <article class="frontier-summary-card"><h3>Exact strict witness</h3><p>The complete P85 certificate is zero. One P86 functional has empirical value -13/12, exact P75 box interval [-1,1], gap 1/12, centered norm 16, and therefore L86 = 1/192.</p></article>\n        <article class="frontier-summary-card"><h3>Scientific boundary</h3><p>This is a stronger rejection certificate for the declared P75 family. It does not identify its latent state with consciousness and does not solve the physical-to-experiential bridge.</p></article>\n      </div>\n      <div class="frontier-actions"><a class="button" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P86_PROOF}">Open the P86 theorem</a></div>\n    </section>\n'''


def promote_website_index() -> None:
    path = "website/index.html"
    text = read(path)
    text = replace_many(
        text,
        {
            "Explore all 85 results": "Explore all 86 results",
            "<strong>85</strong><span>proposition-level results</span>": "<strong>86</strong><span>proposition-level results</span>",
            "<strong>P85</strong><span>current theorem frontier</span>": "<strong>P86</strong><span>current theorem frontier</span>",
            "85 proposition-level results through P85": "86 proposition-level results through P86",
            "P73-P85 progressively": "P73-P86 progressively",
            "The 85-result program": "The 86-result program",
            "P75-P85": "P75-P86",
            "P71-P85:": "P71-P86:",
            "P75 → P84 certification ladder": "P75 → P86 certification ladder",
            "P74-P84": "P74-P86",
            "<!-- Current theorem asset: docs/figures/p84_exact_joint_projection_parity_contrast.svg -->": f"<!-- Current theorem asset: docs/figures/{P86_FIGURE} -->",
        },
    )
    if 'id="p86-frontier"' not in text:
        marker = '    <section id="provenance">'
        if marker not in text:
            raise RuntimeError("homepage provenance marker missing")
        text = text.replace(marker, p86_home_section() + "\n" + marker, 1)
    for token in ("Explore all 86 results", "<strong>P86</strong><span>current theorem frontier</span>", "The 86-result program", "P75-P86", "P71-P86:", P86_PROOF, P86_FIGURE):
        if token not in text:
            raise RuntimeError(f"website/index.html missing {token!r}")
    write(path, text)


def promote_simple_website_pages() -> None:
    replacements = {
        "<strong>85</strong><span>proposition-level results</span>": "<strong>86</strong><span>proposition-level results</span>",
        "<strong>P85</strong><span>current theorem frontier</span>": "<strong>P86</strong><span>current theorem frontier</span>",
        "What the 85 results are doing": "What the 86 results are doing",
        "all 85 results": "all 86 results",
        "P75-P85": "P75-P86",
        "P73-P85": "P73-P86",
        "P77-P85": "P77-P86",
        "P71-P85": "P71-P86",
        "through Proposition 85": "through Proposition 86",
        "Eighty-five results": "Eighty-six results",
        "Current theorem frontier · P85": "Previous theorem frontier · P85",
    }
    for path in (
        "website/plain-language.html",
        "website/start-here.html",
        "website/research-map.html",
        "website/implementation.html",
    ):
        text = replace_many(read(path), replacements)
        if path == "website/research-map.html" and "P86" not in text:
            text = text.replace(
                "</main>",
                f'''  <section id="p86"><p class="eyebrow">Current certified frontier · P86</p><h2>P86: minimally weighted four-event parity separation</h2><p>10,560 exact {{1,1,1,2}} weighted functionals; strict hierarchy witness L85 = 0 &lt; L86 = 1/192.</p><a class="button primary" href="index.html#p86-frontier">Continue to the current P86 frontier</a></section>\n</main>''',
                1,
            )
        if path == "website/implementation.html" and P86_SOURCE not in text:
            text = text.replace(
                "</main>",
                f'''  <section><p class="eyebrow">Current theorem implementation · P86</p><h2>Exact minimally weighted four-event parity separation</h2><p><code>src/consciousness_bridge/{P86_SOURCE}</code> implements the 10,560-function exact P86 family and the P86 branch-and-bound lower bound.</p></section>\n</main>''',
                1,
            )
        write(path, text)


def promote_visual_atlas() -> None:
    path = "website/visual-atlas.html"
    text = read(path)
    text = text.replace("Current theorem frontier · P85", "Previous theorem frontier · P85")
    if 'id="p86-frontier"' not in text:
        section = f'''\n    <section id="p86-frontier" class="theorem-frontier">\n      <div class="section-head"><p class="eyebrow">Current theorem frontier · P86</p><h2>Minimally weighted four-event shared-parameter parity certificate</h2><p>The 10,560-function P86 audit is the current exact continuous-model frontier.</p></div>\n      <div class="theorem-figure-shell"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/{P86_FIGURE}"><img loading="lazy" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/{P86_FIGURE}" alt="P86 minimally weighted four-event parity certificate" /></a></div>\n      <div class="frontier-summary-grid"><article class="frontier-summary-card"><h3>Exact family</h3><p>Four distinct canonical parity events with primitive coefficient magnitudes {{1,1,1,2}} yield 10,560 sign-normalized functionals.</p></article><article class="frontier-summary-card"><h3>Strict hierarchy</h3><p>The exact witness has L85 = 0 and L86 = 1/192.</p></article><article class="frontier-summary-card"><h3>Boundary</h3><p>This remains conditional on P75 and is not an experiential identification theorem.</p></article></div>\n    </section>\n'''
        text = text.replace("</main>", section + "\n</main>", 1)
    if text.count("Current theorem frontier") != 1:
        raise RuntimeError("visual atlas must contain exactly one current theorem frontier label")
    if "Current theorem frontier · P86" not in text or P86_FIGURE not in text:
        raise RuntimeError("visual atlas did not promote P86")
    write(path, text)


def promote_auxiliary_docs() -> None:
    for path in ("docs/equation_and_citation_map.md", "docs/figure_catalog.md"):
        text = read(path)
        if "P86" not in text:
            if path.endswith("equation_and_citation_map.md"):
                text += f'''\n\n## P86 minimally weighted four-event parity certificate\n\n- Proof: [{P86_PROOF}]({P86_PROOF})\n- Provenance: [{P86_PROVENANCE}]({P86_PROVENANCE})\n- Exact family: 10,560 primitive `{{1,1,1,2}}` weighted four-event parity functionals.\n- Strict hierarchy witness: `L85 = 0 < L86 = 1/192`.\n- Interpretation: conditional P75 model separation only; physical-to-experiential bridge remains open.\n'''
            else:
                text += f'''\n\n## P86 exact minimally weighted four-event projection-parity certificate\n\n![P86 exact minimally weighted four-event projection-parity certificate](figures/{P86_FIGURE})\n\n**What it shows.** The P86 figure displays the transition from complete P85 silence to a four-event `{{1,1,1,2}}` shared-parameter functional with exact empirical value -13/12 outside the P75 box interval [-1,1]. The gap 1/12 divided by centered coefficient norm 16 gives `L86 = 1/192`.\n\n**Scientific status.** Conditional exact model-separation theorem for P75; not an identification of consciousness.\n'''
        write(path, text)


def promote_verifier() -> None:
    path = "scripts/verify_repository.py"
    text = read(path)
    text = text.replace('CURRENT_FRONTIER = "P85"', 'CURRENT_FRONTIER = "P86"')
    if f'    "docs/{P86_PROOF}",' not in text:
        text = text.replace(
            '    "docs/p85_equation_provenance.md",\n',
            '    "docs/p85_equation_provenance.md",\n'
            f'    "docs/{P86_PROOF}",\n'
            f'    "docs/{P86_PROVENANCE}",\n',
            1,
        )
    text = text.replace("for number in range(1, 86):", "for number in range(1, 87):")
    stale_marker = '    "<strong>84</strong><span>proposition-level results</span>",\n'
    p85_stale = (
        '    "<strong>85</strong><span>proposition-level results</span>",\n'
        '    "<strong>P85</strong><span>current theorem frontier</span>",\n'
        '    "current P85 frontier",\n'
        '    "actual P85 research frontier",\n'
        '    "What the 85 results are doing",\n'
        '    "shows how all 85 results connect",\n'
        '    "through Proposition 85",\n'
        '    "Eighty-five results",\n'
        '    "Open all 85 results",\n'
        '    "The 85 propositions by scientific role",\n'
        '    "complete 85-result dependency structure",\n'
        '    "You do not need to read 85 proofs in order",\n'
    )
    if p85_stale.splitlines()[0].strip() not in text:
        if stale_marker not in text:
            raise RuntimeError("could not find stale reader marker tuple")
        text = text.replace(stale_marker, p85_stale + stale_marker, 1)
    if 'CURRENT_FRONTIER = "P86"' not in text or "range(1, 87)" not in text:
        raise RuntimeError("repository verifier did not promote to P86")
    write(path, text)


def main() -> None:
    promote_readme()
    promote_start_here()
    promote_navigation()
    promote_roadmap()
    promote_detailed_record()
    promote_citations()
    promote_website_index()
    promote_simple_website_pages()
    promote_visual_atlas()
    promote_auxiliary_docs()
    promote_verifier()
    print("P86 publication surfaces synchronized")


if __name__ == "__main__":
    main()
