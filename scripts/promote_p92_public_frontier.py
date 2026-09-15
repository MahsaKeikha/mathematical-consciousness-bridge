"""Promote canonical publication surfaces from P91 to P92.

P92 closes the P91 full-cube mixed-prevalence distance bracket exactly:

    d_inf(P_emp, M_75) = 1/24.

The lower certificate uses a nonlinear three-minor sign-coherence invariant on
the X1=1 observable subtensor. The matching upper point is the genuinely mixed
rational P75 point established in P91. This promoter preserves P91 as the
historical bracket theorem and makes P92 the reader-facing current frontier.

The script is intentionally idempotent. It is a migration helper, not a
permanent self-writing workflow.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = "proposition_92_exact_global_mixed_prevalence_distance.md"
PROVENANCE = "p92_equation_provenance.md"
FIGURE = "p92_exact_global_mixed_prevalence_distance.svg"
SOURCE = "exact_global_mixed_prevalence_distance.py"
TEST = "test_exact_global_mixed_prevalence_distance.py"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def replace_many(text: str, replacements: tuple[tuple[str, str], ...]) -> str:
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def append_once(text: str, marker: str, block: str) -> str:
    if marker not in text:
        rendered = block.strip()
        if rendered.startswith("<section") and "</main>" in text:
            text = text.replace("</main>", rendered + "\n\n</main>", 1)
        else:
            text = text.rstrip() + "\n\n" + rendered + "\n"
    return text


def promote_readme() -> None:
    path = "README.md"
    text = read(path)
    text = replace_many(
        text,
        (
            ("The current public theorem frontier is **P91**.", "The current public theorem frontier is **P92**."),
            ("**[Read the current frontier](docs/proposition_91_mixed_prevalence_rank_two_flattening_separation.md)**", f"**[Read the current frontier](docs/{PROOF})**"),
            ("**Public theorem frontier:** P91", "**Public theorem frontier:** P92"),
        ),
    )
    block = f'''### Current theorem frontier

![P92 Exact Global Mixed-Prevalence Distance](docs/figures/{FIGURE})

**Figure 2. P92 exact global mixed-prevalence distance.** P92 closes the full-cube P75 distance problem left open by P91. On the observable `X1 = 1` subtensor, three conditional two-by-two determinants of every two-component P75 mixture have a nonnegative sign product. The empirical determinants are exactly `-1/48`, `1/64`, and `5/192`, with exact sign-stability radii `1/24`, `3/56`, and `5/72`. Therefore no P75 law can lie strictly closer than `1/24`. The explicit genuinely mixed rational P75 point from P91 lies exactly at `1/24`, so `d_inf(P_emp, M75) = 1/24` over the complete P75 cube.

P92 is a conditional model-separation theorem. It does not identify consciousness, establish nonphysicality, validate an alternative theory, or close the physical-to-experiential bridge.
'''
    text = re.sub(
        r"### Current theorem frontier\n.*?(?=\n## Choose your path)",
        block.rstrip(),
        text,
        count=1,
        flags=re.DOTALL,
    )
    write(path, text)


def promote_citations() -> None:
    path = "CITATION.md"
    text = replace_many(
        read(path),
        (
            ("current documented frontier, P91", "current documented frontier, P92"),
            ("Current documented theorem frontier: P91", "Current documented theorem frontier: P92"),
            ("theorem frontier **P91**", "theorem frontier **P92**"),
            ("theorem frontier **P91**", "theorem frontier **P92**"),
            ("P1 through P91 chronological theorem record", "P1 through P92 chronological theorem record"),
        ),
    )
    current_block = f'''## Current theorem frontier: P92

The current documented theorem frontier is **P92**. The formal package release remains **Version 0.82.0**. P92 closes the global mixed-prevalence P75 distance bracket left open by P91. A nonlinear three-minor sign-coherence invariant on the `X1 = 1` observable subtensor gives the exact lower bound `d_inf >= 1/24`, and the explicit genuinely mixed rational P75 point from P91 attains `1/24`. Therefore P92 proves `d_inf(P_emp, M75) = 1/24` over the complete P75 parameter cube.

- Proof: [`{PROOF}`](docs/{PROOF})
- Equation provenance: [`{PROVENANCE}`](docs/{PROVENANCE})
- Implementation: [`{SOURCE}`](src/consciousness_bridge/{SOURCE})
- Exact tests: [`{TEST}`](tests/{TEST})

P92 remains a conditional model-separation theorem. It does not identify consciousness, establish nonphysicality, validate an alternative theory, or close the physical-to-experiential bridge.

## Historical mixed-prevalence frontier: P91

P91 remains the preceding full-cube nonlinear theorem. It proves `1/42 < d_inf(P_emp, M75) <= 1/24` by a rank-two flattening certificate plus the mixed upper point. P92 closes that bracket exactly and does not erase the P91 structural result.
'''
    text = re.sub(
        r"## Current theorem frontier: P91\n.*?(?=\n## Historical nonlinear frontier: P90)",
        current_block.rstrip(),
        text,
        flags=re.DOTALL,
    )
    text = append_once(
        text,
        f"[{PROVENANCE}](docs/{PROVENANCE})",
        f'''## Proposition 92 method citation

For work that uses the exact full-cube mixed-prevalence distance theorem, cite the program together with **Proposition 92: Exact Global Mixed-Prevalence Distance** and its [equation provenance record](docs/{PROVENANCE}). P92 proves `d_inf(P_emp, M75) = 1/24` for the established witness and complete P75 parameter cube.''',
    )
    write(path, text)

    for path in ("CITATION.bib", "CITATION.cff"):
        text = replace_many(
            read(path),
            (
                ("Current documented theorem frontier: P91", "Current documented theorem frontier: P92"),
                ("current documented theorem frontier P91", "current documented theorem frontier P92"),
                ("theorem frontier P91", "theorem frontier P92"),
            ),
        )
        write(path, text)


def promote_navigation() -> None:
    path = "docs/research_navigation.md"
    text = replace_many(
        read(path),
        (
            ("The current documented theorem frontier is **P91**.", "The current documented theorem frontier is **P92**."),
            ("**Results:** P75 through P91", "**Results:** P75 through P92"),
            ("P74 through P91", "P74 through P92"),
            ("P71 through P91", "P71 through P92"),
            ("P71-P91", "P71-P92"),
            ("the full 91 proposition index", "the full 92 proposition index"),
            (
                "**Current frontier:** [P91: Mixed-Prevalence Rank-Two Flattening Separation](proposition_91_mixed_prevalence_rank_two_flattening_separation.md)",
                f"**Current frontier:** [P92: Exact Global Mixed-Prevalence Distance]({PROOF})",
            ),
            ("## P91 current frontier", "## P91 historical mixed-prevalence frontier"),
        ),
    )
    text = append_once(
        text,
        "## P92 current frontier",
        f'''## P92 current frontier

For P92:

| What you want | Direct link |
| --- | --- |
| The theorem and proof | [P92 proposition]({PROOF}) |
| Equation and method provenance | [P92 provenance]({PROVENANCE}) |
| Implementation | [`{SOURCE}`](../src/consciousness_bridge/{SOURCE}) |
| Regression tests | [`{TEST}`](../tests/{TEST}) |
| Figure | [P92 exact global distance](figures/{FIGURE}) |
| Repository reproduction | [Reproducibility Guide](reproducibility.md) |

P92 proves the exact full-cube result `d_inf(P_emp, M75) = 1/24`. Its lower certificate is a nonlinear three-minor sign-coherence invariant. The result does not identify the latent state with consciousness, establish nonphysicality, or close the physical-to-experiential bridge.''',
    )
    write(path, text)


def promote_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = replace_many(
        read(path),
        (
            ("The current documented theorem frontier is **P91**.", "The current documented theorem frontier is **P92**."),
            ("P1 through P91 with explicit dependency branches", "P1 through P92 with explicit dependency branches"),
            ("## After P91", "## After P92"),
            ("continuation beyond P91", "continuation beyond P92"),
            ("A future P92 claim", "A future P93 claim"),
            ("Any P92 candidate", "Any P93 candidate"),
            ("Any P92 claim", "Any P93 claim"),
        ),
    )
    dependency_marker = r"\text{P92: three-minor sign coherence closes the full mixed-prevalence P75 distance at 1/24}"
    if dependency_marker not in text:
        text = text.replace(
            "\\end{aligned}",
            "&\\Downarrow\\\\\n&" + dependency_marker + "\\\\\n\\end{aligned}",
            1,
        )
    p91_row = "| [P91](proposition_91_mixed_prevalence_rank_two_flattening_separation.md) | rank-two bipartite flattening and exact 3 by 3 minor interval exclusion | full mixed-prevalence P75 separation bracket `1/42 < d_inf <= 1/24` | proved conditional nonlinear theorem |"
    p92_row = f"| [P92]({PROOF}) | three-minor conditional sign coherence | exact full-cube mixed-prevalence P75 distance `d_inf = 1/24` | proved conditional nonlinear theorem |"
    if p92_row not in text:
        if p91_row in text:
            text = text.replace(p91_row, p91_row + "\n" + p92_row, 1)
        else:
            text = text.replace("\n## 4. Calibration branch remains separate", "\n" + p92_row + "\n\n## 4. Calibration branch remains separate", 1)
    p92_block = f'''## P92: exact global mixed-prevalence distance

P92 closes the P91 bracket exactly. On the `X1 = 1` observable subtensor, every two-component P75 mixture has three conditional two-by-two determinants whose product is nonnegative. For the established empirical witness those determinants are `-1/48`, `1/64`, and `5/192`, with exact sign-stability radii `1/24`, `3/56`, and `5/72`.

Any law closer than `1/24` therefore keeps sign pattern `(-,+,+)` and has negative determinant product, which is impossible for P75. The P91 mixed rational point attains distance exactly `1/24`, so

\[
\\boxed{{d_\\infty(P_{{\\mathrm{{emp}}}},\\mathcal M_{{75}})=\\frac{{1}}{{24}}.}}
\]

- [P92]({PROOF})
- Provenance: [{PROVENANCE}]({PROVENANCE})
- Figure: [P92 exact global distance](figures/{FIGURE})
- Source: [`{SOURCE}`](../src/consciousness_bridge/{SOURCE})
- Tests: [`{TEST}`](../tests/{TEST})

P92 is a conditional model-separation theorem and does not identify consciousness or close the physical-to-experiential bridge.'''
    if "## P92: exact global mixed-prevalence distance" not in text:
        text = text.replace("\n## After P92", "\n" + p92_block + "\n\n## After P92", 1)
    text = text.replace(
        "Natural P92 directions include tightening the mixed-prevalence global distance bracket, combining several rank-two minors into a stronger exact certificate, or deriving a finite-sample rejection theorem specialized to the P91 algebraic witness.",
        "Natural P93 directions include finite-sample calibration of the P92 nonlinear sign certificate, stability under alternative observable slicings, or exact comparison with broader latent-class families.",
    )
    write(path, text)


def promote_records() -> None:
    path = "docs/detailed_proposition_record.md"
    text = replace_many(
        read(path),
        (
            ("## Complete P1 to P91 chronology", "## Complete P1 to P92 chronology"),
            ("P1 through P91", "P1 through P92"),
        ),
    )
    text = append_once(
        text,
        "## Proposition 92: Exact Global Mixed-Prevalence Distance",
        f'''## Proposition 92: Exact Global Mixed-Prevalence Distance

P92 closes the P91 full-cube bracket. Three conditional two-by-two determinants on the `X1 = 1` subtensor have nonnegative product for every P75 law. The empirical determinant values are `-1/48`, `1/64`, and `5/192`; their exact sign-stability radii are `1/24`, `3/56`, and `5/72`. Hence every P75 law is at least `1/24` away, and the explicit mixed P91 point attains exactly `1/24`.

- [Proof]({PROOF})
- [Equation provenance]({PROVENANCE})
- Implementation: `src/consciousness_bridge/{SOURCE}`
- Tests: `tests/{TEST}`
- Figure: `docs/figures/{FIGURE}`

This is a conditional model-separation theorem. It does not identify consciousness, establish nonphysicality, or close the physical-to-experiential bridge.''',
    )
    write(path, text)

    path = "docs/equation_and_citation_map.md"
    text = append_once(
        read(path),
        "## P92 exact global mixed-prevalence distance",
        f'''## P92 exact global mixed-prevalence distance

- Theorem: [Proposition 92]({PROOF})
- Equation provenance: [P92 equation record]({PROVENANCE})
- Implementation: [`{SOURCE}`](../src/consciousness_bridge/{SOURCE})
- Exact tests: [`{TEST}`](../tests/{TEST})
- Figure: [`{FIGURE}`](figures/{FIGURE})

The two-rank-one determinant identity is elementary linear algebra. The repository-original content is the selected three-minor sign-coherence certificate, exact empirical radii, and matching full-cube distance theorem.''',
    )
    write(path, text)

    path = "docs/claim_source_matrix.md"
    text = append_once(
        read(path),
        "| P92 exact global mixed-prevalence distance |",
        f'''| P92 exact global mixed-prevalence distance | The established empirical witness has exact full-cube P75 L-infinity distance `1/24`. | Repository-original conditional theorem using an elementary two-rank-one determinant identity plus exact rational sign-stability certification. | [{PROOF}]({PROOF}); [{PROVENANCE}]({PROVENANCE}); `../src/consciousness_bridge/{SOURCE}`; `../tests/{TEST}` | Do not identify the latent state with consciousness or infer nonphysicality from model separation. |''',
    )
    write(path, text)

    path = "docs/figure_catalog.md"
    text = append_once(
        read(path),
        f"| [P92 Exact Global Mixed-Prevalence Distance](figures/{FIGURE}) |",
        f'''| [P92 Exact Global Mixed-Prevalence Distance](figures/{FIGURE}) | What this figure shows: three exact conditional determinant signs, their sign-stability radii, the universal P75 nonnegative sign-product invariant, and the matching exact distance `1/24`. | Conditional theorem figure, not empirical consciousness evidence. | [P92 proof]({PROOF}); [equation provenance]({PROVENANCE}) |''',
    )
    write(path, text)


def promote_reproducibility() -> None:
    path = "docs/reproducibility.md"
    text = replace_many(
        read(path),
        (
            ("The current public theorem frontier is **P91**.", "The current public theorem frontier is **P92**."),
            ("## 5. Focused audit of the current P91 frontier", "## 5. Focused audit of the current P92 frontier"),
            ("The current theorem frontier is **P91**.", "The current theorem frontier is **P92**."),
            ("docs/proposition_91_mixed_prevalence_rank_two_flattening_separation.md", f"docs/{PROOF}"),
            ("docs/p91_equation_provenance.md", f"docs/{PROVENANCE}"),
            ("src/consciousness_bridge/mixed_prevalence_rank_two_flattening_separation.py", f"src/consciousness_bridge/{SOURCE}"),
            ("tests/test_mixed_prevalence_rank_two_flattening_separation.py", f"tests/{TEST}"),
            ("docs/figures/p91_mixed_prevalence_rank_two_flattening_separation.svg", f"docs/figures/{FIGURE}"),
        ),
    )
    text = append_once(
        text,
        "P92 exact audit command",
        f'''### P92 exact audit command

```bash
python -m pytest -q tests/{TEST}
python scripts/sync_figure_publication.py --check
python scripts/verify_repository.py
```

The P92 theorem uses exact `Fraction` arithmetic for all published determinant values, sign radii, factorization checks, and the matching `1/24` upper certificate.''',
    )
    write(path, text)


def promote_start_and_glossary() -> None:
    for path in ("START_HERE.md", "docs/glossary.md", "docs/research_map.md"):
        text = replace_many(
            read(path),
            (
                ("91 results", "92 results"),
                ("91 proposition-level results", "92 proposition-level results"),
                ("current frontier P91", "current frontier P92"),
                ("Current frontier P91", "Current frontier P92"),
                ("through P91", "through P92"),
                ("P1-P91", "P1-P92"),
                ("P71-P91", "P71-P92"),
                ("P75-P91", "P75-P92"),
            ),
        )
        if path == "START_HERE.md":
            text = append_once(
                text,
                "P92 exact full-cube frontier",
                f'''### P92 exact full-cube frontier

The current Research II frontier is [P92](docs/{PROOF}). P92 closes the P91 mixed-prevalence bracket and proves the exact full-cube result `d_inf(P_emp, M75) = 1/24` through a nonlinear three-minor sign-coherence invariant.''',
            )
        write(path, text)


def _p92_home_section() -> str:
    return f'''<!-- current-frontier-home: P92 -->
<section id="p92-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head">
    <p class="eyebrow">Research II · Current theorem frontier · P92</p>
    <h2>Exact global mixed-prevalence distance</h2>
    <p>P92 closes the P91 full-cube bracket. Three conditional two-by-two determinants on the `X1 = 1` subtensor have a nonnegative product for every two-component P75 mixture.</p>
  </div>
  <div class="theorem-figure-shell"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/{FIGURE}"><img loading="eager" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/{FIGURE}" alt="P92 exact global mixed-prevalence distance certificate" /></a></div>
  <div class="frontier-summary-grid">
    <article class="frontier-summary-card"><h3>Universal nonlinear invariant</h3><p>For every P75 law, the selected determinant product is <strong>nonnegative</strong>.</p></article>
    <article class="frontier-summary-card"><h3>Exact empirical obstruction</h3><p>The empirical determinant signs are <strong>(-, +, +)</strong>. Their exact stability radii are <strong>1/24, 3/56, 5/72</strong>.</p></article>
    <article class="frontier-summary-card"><h3>Exact global closure</h3><p>No P75 law lies closer than <strong>1/24</strong>, and the mixed P91 point attains it. Therefore <strong>d_inf = 1/24</strong>.</p></article>
  </div>
  <div class="boundary"><p><strong>Scientific boundary:</strong> P92 is an exact conditional model-separation theorem. It does not identify consciousness, establish nonphysicality, validate an alternative theory, or close the physical-to-experiential bridge.</p></div>
  <p><a href="research-map.html">Research II map</a> · <a href="visual-atlas.html">Theorem figures</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF}">{PROOF}</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROVENANCE}">{PROVENANCE}</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/{SOURCE}">{SOURCE}</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/{TEST}">{TEST}</a></p>
</section>'''


def promote_website() -> None:
    path = "website/index.html"
    text = replace_many(
        read(path),
        (
            ("91 proposition-level results through P91", "92 proposition-level results through P92"),
            ("The 91 results", "The 92 results"),
            ("91-result program", "92-result program"),
            ("all 91 propositions", "all 92 propositions"),
            ("current P91 frontier", "current P92 frontier"),
            ("Current P91 frontier", "Current P92 frontier"),
            ("sources.html#p91-source", "sources.html#p92-source"),
            ("P91 sources", "P92 sources"),
            ("<!-- Current theorem asset: docs/figures/p91_mixed_prevalence_rank_two_flattening_separation.svg -->", f"<!-- Current theorem asset: docs/figures/{FIGURE} -->"),
        ),
    )
    text = re.sub(
        r"<!-- current-frontier-home: P91 -->\s*<section id=\"p91-frontier\".*?</section>",
        _p92_home_section(),
        text,
        count=1,
        flags=re.DOTALL,
    )
    write(path, text)

    path = "website/visual-atlas.html"
    text = read(path)
    if 'id="p92-frontier"' not in text:
        p92 = f'''<section id="p92-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head"><p class="eyebrow">Current theorem frontier · P92</p><h2>Exact global mixed-prevalence distance</h2><p>The three-minor sign-coherence invariant gives the exact full-cube theorem <strong>d_inf(P_emp, M75) = 1/24</strong>.</p></div>
  <div class="theorem-figure-shell"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/{FIGURE}" alt="P92 exact global mixed-prevalence distance certificate" /></div>
  <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF}">{PROOF}</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROVENANCE}">{PROVENANCE}</a></p>
</section>

'''
        anchor = text.find('<section id="p91-frontier"')
        if anchor < 0:
            raise RuntimeError("visual atlas has no P91 frontier anchor")
        text = text[:anchor] + p92 + text[anchor:]
    text = text.replace("Current theorem frontier · P91", "Historical mixed-prevalence frontier · P91")
    write(path, text)

    path = "website/start-here.html"
    text = replace_many(
        read(path),
        (
            ("91 results · current frontier P91", "92 results · current frontier P92"),
            ("91 proposition-level results", "92 proposition-level results"),
            ("through P91", "through P92"),
            ("Open all 91 Research II results", "Open all 92 Research II results"),
            ("The 91 propositions are the formal theorem record of Research II", "The 92 propositions are the formal theorem record of Research II"),
            ("P1-P91 build the mathematical conditions", "P1-P92 build the mathematical conditions"),
            ("P75-P91 test the declared target-measurement model", "P75-P92 test the declared target-measurement model"),
            ("<span>P75-P91</span>", "<span>P75-P92</span>"),
            ("You do not need to read 91 Research II proofs in order", "You do not need to read 92 Research II proofs in order"),
        ),
    )
    text = append_once(
        text,
        'id="p92-start-frontier"',
        f'''<section class="boundary" id="p92-start-frontier"><div class="section-head"><p class="eyebrow">Research II · Current frontier · P92</p><h2>The full mixed-prevalence distance is now exact</h2><p>P92 closes the P91 bracket by combining three conditional determinant signs. The exact result is <strong>d_inf(P_emp, M75) = 1/24</strong>.</p><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF}">Read P92 theorem</a></p></div></section>''',
    )
    write(path, text)

    path = "website/plain-language.html"
    text = replace_many(
        read(path),
        (
            ("This is the 91-result Research II theorem program currently reaching P91.", "This is the 92-result Research II theorem program currently reaching P92."),
            ("A 91-result sufficiency and falsification architecture", "A 92-result sufficiency and falsification architecture"),
            ("The 91-result proposition program", "The 92-result proposition program"),
            ("The current theorem frontier is P91.", "The current theorem frontier is P92."),
            ("P91 is the current checkpoint, not the destination", "P92 is the current checkpoint, not the destination"),
            ("P91 is the current mathematical checkpoint", "P92 is the current mathematical checkpoint"),
            ("shows how all 91 Research II results connect", "shows how all 92 Research II results connect"),
        ),
    )
    text = text.replace("Research II · Current frontier · P91", "Research II · Historical mixed-prevalence frontier · P91")
    if 'id="p92-reader-frontier"' not in text:
        block = f'''<section class="boundary" id="p92-reader-frontier"><div class="section-head"><p class="eyebrow">Research II · Current frontier · P92</p><h2>The mixed-prevalence gap closes exactly at 1/24</h2><p>P92 uses a nonlinear three-minor sign-coherence rule that every P75 mixture must obey. The empirical witness violates that sign rule robustly up to radius 1/24, and the mixed P91 model point reaches the boundary exactly.</p><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF}">Read P92</a></p></div></section>\n\n'''
        marker = '<section class="boundary" id="p91-reader-frontier">'
        text = text.replace(marker, block + marker, 1)
    write(path, text)

    path = "website/research-map.html"
    text = replace_many(
        read(path),
        (
            ("Ninety-one results, one dependency-aware scientific program", "Ninety-two results, one dependency-aware scientific program"),
            ("through Proposition 91", "through Proposition 92"),
            ("P71-P91", "P71-P92"),
            ("P73-P91", "P73-P92"),
            ("P74-P91", "P74-P92"),
            ("P75-P91", "P75-P92"),
            ("P77-P91", "P77-P92"),
            ("P78-P91", "P78-P92"),
            ("91 proposition-level", "92 proposition-level"),
            ("Current Research II model-audit range: P75-P91.", "Current Research II model-audit range: P75-P92."),
            ("Continue to the current P91 frontier", "Continue to the current P92 frontier"),
            ("culminating in P91 mixed-prevalence rank-two flattening separation", "culminating in P92 exact global mixed-prevalence distance"),
        ),
    )
    text = text.replace("Current Research II theorem frontier · P91", "Historical mixed-prevalence frontier · P91")
    if 'id="p92-research-map"' not in text:
        block = f'''<section id="p92-research-map" class="theorem-frontier">
  <div class="section-head"><p class="eyebrow">Current Research II theorem frontier · P92</p><h2>P92: What is the exact distance to the complete mixed-prevalence P75 family?</h2></div>
  <p>P92 closes the P91 bracket. Every P75 law has a nonnegative product of three selected conditional two-by-two determinants on the X1 = 1 subtensor. The empirical signs are (-,+,+), and the smallest exact sign-stability radius is 1/24.</p>
  <p><strong>Exact result:</strong> <code>d_inf(P_emp, M75) = 1/24</code>.</p>
  <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF}">{PROOF}</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROVENANCE}">{PROVENANCE}</a> · <a href="index.html#p92-frontier">Current frontier</a></p>
</section>'''
        text = text.replace("</main>", block + "\n\n</main>", 1)
    write(path, text)

    path = "website/research-lineage.html"
    text = replace_many(
        read(path),
        (
            ("<strong>91</strong><span>proposition-level results</span>", "<strong>92</strong><span>proposition-level results</span>"),
            ("<strong>P91</strong><span>current theorem frontier</span>", "<strong>P92</strong><span>current theorem frontier</span>"),
            ("through P91", "through P92"),
        ),
    )
    write(path, text)

    path = "website/sources.html"
    text = append_once(
        read(path),
        'id="p92-source"',
        f'''<section id="p92-source" class="boundary"><div class="section-head"><p class="eyebrow">Current theorem source record · P92</p><h2>Exact global mixed-prevalence distance</h2></div><p>Proof: <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF}">{PROOF}</a> · provenance: <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROVENANCE}">{PROVENANCE}</a> · implementation: <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/{SOURCE}">{SOURCE}</a> · tests: <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/{TEST}">{TEST}</a>.</p><p>The determinant identity is elementary linear algebra. The selected exact sign-coherence obstruction and matching full-cube distance certificate are repository-original. The result does not identify consciousness or prove nonphysicality.</p></section>''',
    )
    write(path, text)

    path = "website/implementation.html"
    text = replace_many(
        read(path),
        (
            ("P91", "P92"),
            ("91 proposition", "92 proposition"),
        ),
    )
    write(path, text)


def promote_prepare_website() -> None:
    path = "scripts/prepare_website.py"
    text = replace_many(
        read(path),
        (
            ("p91_mixed_prevalence_rank_two_flattening_separation.svg", FIGURE),
            ("Current record:</strong> 91 proposition-level results through P91", "Current record:</strong> 92 proposition-level results through P92"),
            ("with Research II P90", "with Research II P92"),
            ("with P91", "with P92"),
            ("current P91", "current P92"),
            ("bundled P91", "bundled P92"),
            ("to 91/P91", "to 92/P92"),
            ('id="p91-frontier"', 'id="p92-frontier"'),
            ("pre-P91", "pre-P92"),
            ("<strong>91</strong><span>proposition-level results</span>", "<strong>92</strong><span>proposition-level results</span>"),
            ("<strong>P91</strong><span>current theorem frontier</span>", "<strong>P92</strong><span>current theorem frontier</span>"),
        ),
    )
    write(path, text)


def promote_sync_summary() -> None:
    path = "scripts/sync_figure_publication.py"
    text = read(path)
    marker = "    return []\n\n\ndef _frontier_page"
    if "if frontier == 92:" not in text:
        block = '''    if frontier == 92:\n        return [\n            "### Exact P92 full-cube mixed-prevalence distance",\n            "",\n            "P92 closes the P91 bracket through a nonlinear three-minor sign-coherence invariant on the X1=1 subtensor.",\n            "",\n            "```text",\n            "empirical determinants = (-1/48, 1/64, 5/192)",\n            "sign-stability radii = (1/24, 3/56, 5/72)",\n            "universal P75 determinant product >= 0",\n            "d_inf(P_emp, M_75) = 1/24",\n            "```",\n            "",\n            "P92 is a conditional model-separation theorem and does not identify consciousness or close the physical-to-experiential bridge.",\n            "",\n        ]\n'''
        text = text.replace(marker, block + marker, 1)
    write(path, text)


def promote_verifier() -> None:
    path = "scripts/verify_repository.py"
    text = replace_many(
        read(path),
        (
            ('CURRENT_FRONTIER = "P91"', 'CURRENT_FRONTIER = "P92"'),
            ('"docs/figures/p91_mixed_prevalence_rank_two_flattening_separation.svg",', '"docs/figures/p91_mixed_prevalence_rank_two_flattening_separation.svg",\n    "docs/figures/p92_exact_global_mixed_prevalence_distance.svg",'),
            ('"docs/p91_equation_provenance.md",', '"docs/p91_equation_provenance.md",\n    "docs/proposition_92_exact_global_mixed_prevalence_distance.md",\n    "docs/p92_equation_provenance.md",'),
            ('"src/consciousness_bridge/mixed_prevalence_rank_two_flattening_separation.py",', '"src/consciousness_bridge/mixed_prevalence_rank_two_flattening_separation.py",\n    "src/consciousness_bridge/exact_global_mixed_prevalence_distance.py",'),
            ('"tests/test_mixed_prevalence_rank_two_flattening_separation.py",', '"tests/test_mixed_prevalence_rank_two_flattening_separation.py",\n    "tests/test_exact_global_mixed_prevalence_distance.py",'),
            ('range(1, 92)', 'range(1, 93)'),
            ('p91_mixed_prevalence_rank_two_flattening_separation.svg")', 'p92_exact_global_mixed_prevalence_distance.svg")'),
            ('len(figures) != 149', 'len(figures) != 150'),
            ('canonical 149 figures', 'canonical 150 figures'),
            ('p91 = visual_atlas.index(\'id="p91-frontier"\')\n    p90 = visual_atlas.index(\'id="p90-frontier"\')\n    p89 = visual_atlas.index(\'id="p89-frontier"\')\n    if not (p91 < p90 < p89):\n        raise RuntimeError("Visual Atlas does not lead with the current P91 figure")', 'p92 = visual_atlas.index(\'id="p92-frontier"\')\n    p91 = visual_atlas.index(\'id="p91-frontier"\')\n    p90 = visual_atlas.index(\'id="p90-frontier"\')\n    if not (p92 < p91 < p90):\n        raise RuntimeError("Visual Atlas does not lead with the current P92 figure")'),
            ('if "Current documented theorem frontier: P91" not in citation:', 'if "Current documented theorem frontier: P92" not in citation:'),
            ('raise RuntimeError("CITATION.md does not declare P91 as the current theorem frontier")', 'raise RuntimeError("CITATION.md does not declare P92 as the current theorem frontier")'),
            ('if "P91" not in (ROOT / "CITATION.cff").read_text(encoding="utf-8"):', 'if "P92" not in (ROOT / "CITATION.cff").read_text(encoding="utf-8"):'),
            ('raise RuntimeError("CITATION.cff does not mention P91")', 'raise RuntimeError("CITATION.cff does not mention P92")'),
        ),
    )
    stale_anchor = 'STALE_READER_FRONTIER_MARKERS = (\n'
    if '"Current theorem frontier · P91",' not in text:
        text = text.replace(
            stale_anchor,
            stale_anchor
            + '    "Current theorem frontier · P91",\n'
            + '    "current P91 frontier",\n'
            + '    "<strong>P91</strong><span>current theorem frontier</span>",\n',
            1,
        )
    write(path, text)


def promote_workflows() -> None:
    paths = (
        ".github/workflows/figures.yml",
        ".github/workflows/reproducibility.yml",
        ".github/workflows/validate-research-three-website.yml",
    )
    for path in paths:
        text = replace_many(
            read(path),
            (
                ("Certified P91 visual publication gate", "Certified P92 visual publication gate"),
                ("Exact-reference P91 release audit", "Exact-reference P92 release audit"),
                ("promote_p91_public_frontier.py", "promote_p92_public_frontier.py"),
                ("test_p91_reader_surface_coherence.py", "test_p92_reader_surface_coherence.py"),
                ("p91_mixed_prevalence_rank_two_flattening_separation.svg", FIGURE),
                ("Validate committed P91 publication state", "Validate committed P92 publication state"),
                ("Upload reproduced P91 visual record", "Upload reproduced P92 visual record"),
                ("reproduced-visual-record-v0.82.0-p91", "reproduced-visual-record-v0.82.0-p92"),
                ("current-frontier-home: P91", "current-frontier-home: P92"),
                ('id=\\"p91-frontier\\"', 'id=\\"p92-frontier\\"'),
                ("91 proposition-level results through P91", "92 proposition-level results through P92"),
                ("all 91 propositions", "all 92 propositions"),
                ("<strong>91</strong><span>proposition-level results</span>", "<strong>92</strong><span>proposition-level results</span>"),
                ("<strong>P91</strong><span>current theorem frontier</span>", "<strong>P92</strong><span>current theorem frontier</span>"),
                ("p91=t.index", "p92=t.index"),
                ("assert p91 < p90 < p89", "assert p92 < p91 < p90"),
                ("P91 reader coherence", "P92 reader coherence"),
                ("P91" , "P92") if path == ".github/workflows/validate-research-three-website.yml" else ("__NOOP__", "__NOOP__"),
            ),
        )
        write(path, text)


def write_reader_tests() -> None:
    path = "tests/test_p92_reader_surface_coherence.py"
    content = f'''from pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\n\n\ndef _read(path: str) -> str:\n    return (ROOT / path).read_text(encoding="utf-8")\n\n\ndef test_p92_proof_states_exact_global_distance_and_boundary() -> None:\n    text = _read("docs/{PROOF}")\n    lower = text.lower()\n    assert "1/24" in text\n    assert "sign-coherence" in lower\n    assert "exact global" in lower\n    assert "physical-to-experiential bridge remains open" in lower\n\n\ndef test_p92_homepage_is_current_and_links_complete_record() -> None:\n    text = _read("website/index.html")\n    assert 'id="p92-frontier"' in text\n    assert "Current theorem frontier · P92" in text\n    assert "{FIGURE}" in text\n    assert "{PROOF}" in text\n    assert "{PROVENANCE}" in text\n    assert "{SOURCE}" in text\n    assert "{TEST}" in text\n    assert "d_inf = 1/24" in text\n\n\ndef test_visual_atlas_orders_p92_before_p91_and_p90() -> None:\n    text = _read("website/visual-atlas.html")\n    p92 = text.index('id="p92-frontier"')\n    p91 = text.index('id="p91-frontier"')\n    p90 = text.index('id="p90-frontier"')\n    assert p92 < p91 < p90\n    assert "{FIGURE}" in text[p92:p91]\n\n\ndef test_p92_reader_surfaces_preserve_scientific_boundary() -> None:\n    for path in ("README.md", "website/index.html", "website/plain-language.html", "website/start-here.html", "website/research-map.html"):\n        text = _read(path).lower()\n        assert "p92" in text\n        assert "physical-to-experiential bridge" in text\n\n\ndef test_p92_start_here_and_plain_language_are_current() -> None:\n    start = _read("website/start-here.html")\n    plain = _read("website/plain-language.html")\n    assert "P92" in start and "92" in start\n    assert "P92" in plain and "92" in plain\n    assert 'id="p92-reader-frontier"' in plain\n\n\ndef test_p92_workflows_are_read_only_publication_gates() -> None:\n    for path in (".github/workflows/figures.yml", ".github/workflows/reproducibility.yml", ".github/workflows/validate-research-three-website.yml"):\n        text = _read(path)\n        assert "contents: read" in text\n        assert "contents: write" not in text\n        assert "git push" not in text\n'''
    write(path, content)

    path = "tests/test_p91_reader_surface_coherence.py"
    content = '''from pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\n\n\ndef _read(path: str) -> str:\n    return (ROOT / path).read_text(encoding="utf-8")\n\n\ndef test_p91_proof_remains_historically_auditable() -> None:\n    text = _read("docs/proposition_91_mixed_prevalence_rank_two_flattening_separation.md")\n    assert "1/42" in text\n    assert "1/24" in text\n    assert "rank at most two" in text.lower()\n    assert "physical-to-experiential bridge remains open" in text.lower()\n\n\ndef test_p91_visual_record_is_preserved_below_p92() -> None:\n    text = _read("website/visual-atlas.html")\n    p92 = text.index('id="p92-frontier"')\n    p91 = text.index('id="p91-frontier"')\n    p90 = text.index('id="p90-frontier"')\n    assert p92 < p91 < p90\n    assert "p91_mixed_prevalence_rank_two_flattening_separation.svg" in text[p91:p90]\n\n\ndef test_p91_is_not_still_declared_current() -> None:\n    for path in ("README.md", "docs/research_navigation.md", "docs/theorem_roadmap.md", "website/index.html"):\n        text = _read(path)\n        assert "current public theorem frontier is **P91**" not in text\n        assert "Current theorem frontier · P91" not in text\n\n\ndef test_p91_scientific_boundary_is_preserved() -> None:\n    for path in ("docs/proposition_91_mixed_prevalence_rank_two_flattening_separation.md", "website/research-map.html", "website/visual-atlas.html"):\n        text = _read(path).lower()\n        assert "p91" in text\n        assert "physical-to-experiential bridge" in text or "model" in text\n'''
    write(path, content)


def promote_orientation_test() -> None:
    path = "tests/test_website_research_orientation.py"
    text = read(path)
    text = replace_many(
        text,
        (
            ('"proposition_91_mixed_prevalence_rank_two_flattening_separation.md",\n        "p91_equation_provenance.md",\n        "test_mixed_prevalence_rank_two_flattening_separation.py",\n        \'index.html#p91-frontier\',', '"proposition_91_mixed_prevalence_rank_two_flattening_separation.md",\n        "proposition_92_exact_global_mixed_prevalence_distance.md",\n        "p92_equation_provenance.md",\n        "test_exact_global_mixed_prevalence_distance.py",\n        \'index.html#p92-frontier\','),
            ('assert \'index.html#p89-frontier\' not in text', 'assert \'index.html#p91-frontier\' not in text'),
            ('p90 = text.index(\'id="p90-research-map"\')\n    p91 = text.index(\'id="p91-research-map"\')\n    p90_text = text[p90:p91]\n    p91_text = text[p91:main_close]', 'p90 = text.index(\'id="p90-research-map"\')\n    p91 = text.index(\'id="p91-research-map"\')\n    p92 = text.index(\'id="p92-research-map"\')\n    p90_text = text[p90:p91]\n    p91_text = text[p91:p92]\n    p92_text = text[p92:main_close]'),
            ('assert text.count(\'id="p91-research-map"\') == 1\n    assert main_open < p90 < p91 < main_close', 'assert text.count(\'id="p91-research-map"\') == 1\n    assert text.count(\'id="p92-research-map"\') == 1\n    assert main_open < p90 < p91 < p92 < main_close'),
            ('assert "Current Research II theorem frontier" not in p90_text\n    assert "Current Research II theorem frontier · P91" in p91_text', 'assert "Current Research II theorem frontier" not in p90_text\n    assert "Current Research II theorem frontier" not in p91_text\n    assert "Current Research II theorem frontier · P92" in p92_text'),
            ('assert "p91_equation_provenance.md" in frontier_text', 'assert "p91_equation_provenance.md" in frontier_text or "p92_equation_provenance.md" in text\n    assert "proposition_92_exact_global_mixed_prevalence_distance.md" in text\n    assert "p92_equation_provenance.md" in text'),
        ),
    )
    write(path, text)


def main() -> None:
    promote_readme()
    promote_citations()
    promote_navigation()
    promote_roadmap()
    promote_records()
    promote_reproducibility()
    promote_start_and_glossary()
    promote_website()
    promote_prepare_website()
    promote_sync_summary()
    promote_verifier()
    promote_workflows()
    write_reader_tests()
    promote_orientation_test()
    print("[P92] reader-facing publication surfaces promoted")


if __name__ == "__main__":
    main()
