"""Promote canonical publication surfaces from P90 to P91.

P91 removes the extreme-prevalence restriction used by P90. For arbitrary
latent prevalence, the declared two-component P75 law has a 4 by 4 bipartite
flattening of rank at most two. A selected empirical 3 by 3 minor remains
strictly nonzero throughout the closed full-law L-infinity ball of radius
1/42, while an explicit genuinely mixed rational P75 point lies at distance
1/24. The result is therefore the certified global bracket

    1/42 < d_inf(P_emp, M_75) <= 1/24.

The upper endpoint is not claimed to be the exact global optimum. This promoter
keeps P90 as a historical exact single-component theorem while making P91 the
reader-facing current frontier. It is intentionally idempotent.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = "proposition_91_mixed_prevalence_rank_two_flattening_separation.md"
PROVENANCE = "p91_equation_provenance.md"
FIGURE = "p91_mixed_prevalence_rank_two_flattening_separation.svg"
SOURCE = "mixed_prevalence_rank_two_flattening_separation.py"
TEST = "test_mixed_prevalence_rank_two_flattening_separation.py"


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


def promote_citations() -> None:
    path = "CITATION.md"
    text = read(path)
    text = replace_many(
        text,
        (
            ("current documented frontier, P90", "current documented frontier, P91"),
            ("Current documented theorem frontier: P90", "Current documented theorem frontier: P91"),
            ("theorem frontier **P90**", "theorem frontier **P91**"),
            ("## Current theorem frontier: P90", "## Current theorem frontier: P91"),
            ("P1 through P90 chronological theorem record", "P1 through P91 chronological theorem record"),
        ),
    )
    current_block = f'''## Current theorem frontier: P91

The current documented theorem frontier is **P91**. The formal package release remains **Version 0.82.0**. P91 removes P90's extreme-prevalence restriction. Every two-component P75 law has rank at most two under the declared `(X1,X4)|(X2,X3)` flattening. For the established witness, an exact 512-vertex nonnegative interval calculation excludes the entire closed full-law L-infinity ball of radius `1/42`, while an explicit rational P75 point with prevalence `4/5` lies at distance exactly `1/24`. Therefore P91 certifies `1/42 < d_inf(P_emp, M75) <= 1/24` over the full P75 parameter cube. The upper endpoint is not claimed to be the exact global optimum.

- Proof: [`{PROOF}`](docs/{PROOF})
- Equation provenance: [`{PROVENANCE}`](docs/{PROVENANCE})
- Implementation: [`{SOURCE}`](src/consciousness_bridge/{SOURCE})
- Exact tests: [`{TEST}`](tests/{TEST})

P91 remains a conditional model-separation theorem. It does not identify consciousness, establish nonphysicality, validate an alternative theory, or close the physical-to-experiential bridge.

## Historical nonlinear frontier: P90

P90 remains the exact single-component nonlinear subfrontier at `L90 = 5/72 = (7/3)L89` on the declared strict prevalence-zero P75 face. P91 enlarges the model family to arbitrary prevalence and therefore answers a different question; its bracket must not be compared to `L90` as though both optimized over the same model set.
'''
    text = re.sub(
        r"## Current theorem frontier: P91\n.*?(?=\n## Historical theorem frontier: P89)",
        current_block.rstrip(),
        text,
        flags=re.DOTALL,
    )
    text = append_once(
        text,
        f"[{PROVENANCE}](docs/{PROVENANCE})",
        f'''## Proposition 91 method citation

For work that uses the full mixed-prevalence rank-two flattening certificate, cite the program together with **Proposition 91: Mixed-Prevalence Rank-Two Flattening Separation** and its [equation provenance record](docs/{PROVENANCE}). The theorem gives the certified global bracket `1/42 < d_inf(P_emp, M75) <= 1/24` for the established witness and full P75 parameter cube. The constructive upper endpoint is not claimed to be the exact global optimum.''',
    )
    write(path, text)

    path = "CITATION.bib"
    text = read(path).replace(
        "Current documented theorem frontier: P90",
        "Current documented theorem frontier: P91",
    )
    write(path, text)


def promote_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    text = replace_many(
        text,
        (
            ("The current documented theorem frontier is **P90**.", "The current documented theorem frontier is **P91**."),
            ("**Results:** P75 through P90", "**Results:** P75 through P91"),
            ("P74 through P90", "P74 through P91"),
            ("P71 through P90", "P71 through P91"),
            ("P71-P90", "P71-P91"),
            ("the full 90 proposition index", "the full 91 proposition index"),
            (
                "**Current frontier:** [P90: Exact Nonlinear Rank-One Slice Separation](proposition_90_exact_nonlinear_rank_one_separation.md)",
                f"**Current frontier:** [P91: Mixed-Prevalence Rank-Two Flattening Separation]({PROOF})",
            ),
        ),
    )
    text = append_once(
        text,
        "## P91 current frontier",
        f'''## P91 current frontier

For P91:

| What you want | Direct link |
| --- | --- |
| The theorem and proof | [P91 proposition]({PROOF}) |
| Equation and method provenance | [P91 provenance]({PROVENANCE}) |
| Implementation | [`{SOURCE}`](../src/consciousness_bridge/{SOURCE}) |
| Regression tests | [`{TEST}`](../tests/{TEST}) |
| Figure | [P91 mixed-prevalence rank-two certificate](figures/{FIGURE}) |
| Repository reproduction | [Reproducibility Guide](reproducibility.md) |

P91 certifies `1/42 < d_inf(P_emp, M75) <= 1/24` over the full P75 parameter cube. It does not claim that `1/24` is the exact global optimum and does not identify the latent state with consciousness, establish nonphysicality, or close the physical-to-experiential bridge.''',
    )
    write(path, text)


def promote_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    text = replace_many(
        text,
        (
            (
                "The current documented theorem frontier is **P90**. The proposition record runs from **P1 through P90 with explicit dependency branches**. P71-P88 return",
                "The current documented theorem frontier is **P91**. The proposition record runs from **P1 through P91 with explicit dependency branches**. P71-P91 return",
            ),
            ("## After P90", "## After P91"),
            ("continuation beyond P90", "continuation beyond P91"),
            ("A future P91 claim", "A future P92 claim"),
            ("Any P91 candidate", "Any P92 candidate"),
            ("Any P91 claim", "Any P92 claim"),
        ),
    )
    dependency_marker = r"\text{P91: arbitrary-prevalence P75 mixtures obey rank at most two under the declared bipartite flattening}"
    if dependency_marker not in text:
        text = text.replace(
            "\\end{aligned}",
            "&\\Downarrow\\\\\n&" + dependency_marker + "\\\\\n\\end{aligned}",
            1,
        )
    p90_row = "| [P90](proposition_90_exact_nonlinear_rank_one_separation.md) | nonlinear rank-one slice identity | exact single-component strict-box model separation at 5/72 | proved conditional nonlinear theorem |"
    p91_row = f"| [P91]({PROOF}) | rank-two bipartite flattening and exact 3 by 3 minor interval exclusion | full mixed-prevalence P75 separation bracket `1/42 < d_inf <= 1/24` | proved conditional nonlinear theorem |"
    if p90_row not in text:
        text = text.replace("\n## 4. Calibration branch remains separate", "\n" + p90_row + "\n" + p91_row + "\n\n## 4. Calibration branch remains separate", 1)
    elif p91_row not in text:
        text = text.replace(p90_row, p90_row + "\n" + p91_row, 1)
    text = append_once(
        text,
        "## P91: mixed-prevalence rank-two flattening separation",
        fr'''## P91: mixed-prevalence rank-two flattening separation

P91 removes the extreme-prevalence restriction used by P90. For any P75 parameter vector, grouping `(X1,X4)` against `(X2,X3)` expresses the 4 by 4 observable probability flattening as the sum of two rank-one matrices, hence its rank is at most two and every 3 by 3 minor vanishes.

For the established exact empirical witness, the selected 3 by 3 minor has determinant `1/512`. At full-law L-infinity radius `1/42`, exact enumeration of all 512 vertices of the nonnegative entrywise uncertainty box gives minimum determinant `23/677376 > 0`. Therefore no P75 law lies in that closed ball. A separate rational P75 point with prevalence `4/5` lies at distance exactly `1/24`.

\[
\\boxed{{\\frac{{1}}{{42}}<d_\\infty(P_{{\\mathrm{{emp}}}},\\mathcal M_{{75}})\\le\\frac{{1}}{{24}}.}}
\]

- [P91]({PROOF})
- Provenance: [{PROVENANCE}]({PROVENANCE})
- Figure: [P91 mixed-prevalence rank-two certificate](figures/{FIGURE})
- Source: [`{SOURCE}`](../src/consciousness_bridge/{SOURCE})
- Tests: [`{TEST}`](../tests/{TEST})

The upper endpoint `1/24` is a constructive upper bound, not a claimed exact global optimum. P91 is a conditional model-separation result and does not identify consciousness or close the physical-to-experiential bridge.

## After P91

The next theorem should close a new gap rather than merely increase proposition number. Natural P92 directions include tightening the mixed-prevalence global distance bracket, combining several rank-two minors into a stronger exact certificate, or deriving a finite-sample rejection theorem specialized to the P91 algebraic witness. Any P92 claim must preserve one-sided certification and the repository's scientific boundary.''',
    )
    write(path, text)


def promote_records() -> None:
    path = "docs/detailed_proposition_record.md"
    text = read(path).replace("## Complete P1 to P90 chronology", "## Complete P1 to P91 chronology")
    text = append_once(
        text,
        "## Proposition 91: Mixed-Prevalence Rank-Two Flattening Separation",
        f'''## Proposition 91: Mixed-Prevalence Rank-Two Flattening Separation

P91 removes P90's extreme-prevalence restriction. Every two-component P75 law has rank at most two after the declared `(X1,X4)|(X2,X3)` flattening. The selected empirical 3 by 3 minor has determinant `1/512`; exhaustive exact rational evaluation of all 512 nonnegative interval-box vertices at radius `1/42` keeps that determinant strictly positive, excluding the full P75 family from the closed ball. An explicit rational P75 point with prevalence `4/5` lies at distance `1/24`, yielding `1/42 < d_inf(P_emp, M75) <= 1/24`.

- [Proof]({PROOF})
- [Equation provenance]({PROVENANCE})
- Implementation: `src/consciousness_bridge/{SOURCE}`
- Tests: `tests/{TEST}`
- Figure: `docs/figures/{FIGURE}`

The upper endpoint is not claimed to be the exact global optimum. This is a conditional model-separation theorem and does not identify consciousness, establish nonphysicality, or close the physical-to-experiential bridge.''',
    )
    write(path, text)

    path = "docs/equation_and_citation_map.md"
    text = read(path)
    text = append_once(
        text,
        "## P91 mixed-prevalence rank-two flattening separation",
        f'''## P91 mixed-prevalence rank-two flattening separation

- Theorem: [Proposition 91]({PROOF})
- Equation provenance: [P91 equation record]({PROVENANCE})
- Implementation: [`{SOURCE}`](../src/consciousness_bridge/{SOURCE})
- Exact tests: [`{TEST}`](../tests/{TEST})
- Figure: [`{FIGURE}`](figures/{FIGURE})

The rank-at-most-two implication is standard linear algebra applied to a two-component product mixture. The repository-original content is the selected exact witness, nonnegative 512-vertex interval certificate, and resulting global P75 distance bracket.''',
    )
    write(path, text)

    path = "docs/claim_source_matrix.md"
    text = read(path)
    text = append_once(
        text,
        "| P91 mixed-prevalence rank-two flattening separation |",
        f'''| P91 mixed-prevalence rank-two flattening separation | Every P75 law has rank at most two under the declared bipartite flattening; the established empirical witness is farther than `1/42` from the full family and one mixed rational P75 point lies at `1/24`. | Repository-original conditional theorem built from standard rank algebra plus exact rational certification. | [{PROOF}]({PROOF}); [{PROVENANCE}]({PROVENANCE}); `../src/consciousness_bridge/{SOURCE}`; `../tests/{TEST}` | Do not report `1/24` as the exact global optimum. Do not identify the latent state with consciousness or infer nonphysicality. |''',
    )
    write(path, text)

    path = "docs/figure_catalog.md"
    text = read(path)
    text = append_once(
        text,
        f"| [P91 Mixed-Prevalence Rank-Two Flattening Separation](figures/{FIGURE}) |",
        f'''| [P91 Mixed-Prevalence Rank-Two Flattening Separation](figures/{FIGURE}) | What this figure shows: arbitrary-prevalence two-component P75 laws have rank at most two under the declared 4 by 4 flattening; the selected empirical 3 by 3 minor remains positive throughout the closed radius-`1/42` box, while a genuinely mixed rational P75 point lies at distance `1/24`. | Conditional theorem figure, not empirical consciousness evidence. The upper endpoint is not claimed globally exact. | [P91 proof]({PROOF}); [equation provenance]({PROVENANCE}) |''',
    )
    write(path, text)


def promote_reproducibility() -> None:
    path = "docs/reproducibility.md"
    text = read(path)
    text = replace_many(
        text,
        (
            ("The current public theorem frontier is **P90**.", "The current public theorem frontier is **P91**."),
            ("## 5. Focused audit of the current P90 frontier", "## 5. Focused audit of the current P91 frontier"),
            ("The current theorem frontier is **P90**.", "The current theorem frontier is **P91**."),
            ("docs/proposition_90_exact_nonlinear_rank_one_separation.md", f"docs/{PROOF}"),
            ("docs/p90_equation_provenance.md", f"docs/{PROVENANCE}"),
            ("src/consciousness_bridge/exact_nonlinear_rank_one_separation.py", f"src/consciousness_bridge/{SOURCE}"),
            ("tests/test_exact_nonlinear_rank_one_separation.py", f"tests/{TEST}"),
            ("docs/figures/p90_exact_nonlinear_rank_one_separation.svg", f"docs/figures/{FIGURE}"),
        ),
    )
    text = append_once(
        text,
        "P91 exact audit command",
        f'''### P91 exact audit command

```bash
python -m pytest -q tests/{TEST}
python scripts/sync_figure_publication.py --check
python scripts/verify_repository.py
```

The P91 lower certificate uses only exact `Fraction` arithmetic and checks all 512 vertices of the selected nonnegative determinant box.''',
    )
    write(path, text)


def promote_start_and_glossary() -> None:
    replacements = (
        ("90 results", "91 results"),
        ("90 proposition-level results", "91 proposition-level results"),
        ("current frontier P90", "current frontier P91"),
        ("Current frontier P90", "Current frontier P91"),
        ("through P90", "through P91"),
        ("P1-P90", "P1-P91"),
    )
    for path in ("START_HERE.md", "docs/glossary.md", "docs/research_map.md"):
        text = replace_many(read(path), replacements)
        if path == "START_HERE.md":
            text = append_once(
                text,
                "P91 mixed-prevalence frontier",
                f'''### P91 mixed-prevalence frontier

The current Research II frontier is [P91]({"docs/" if path == "START_HERE.md" else ""}{PROOF}). P91 shows that the nonlinear P75 separation is not confined to P90's prevalence-zero face: over the full two-component mixture cube, the established witness obeys the certified bracket `1/42 < d_inf <= 1/24`. The upper endpoint remains a constructive bound rather than a claimed exact optimum.''',
            )
        write(path, text)


def _p91_home_section() -> str:
    return f'''<!-- current-frontier-home: P91 -->
<section id="p91-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head">
    <p class="eyebrow">Research II · Current theorem frontier · P91</p>
    <h2>Mixed-prevalence rank-two flattening separation</h2>
    <p>P91 removes P90's extreme-prevalence restriction. Every two-component P75 law has rank at most two under the declared `(X1,X4)|(X2,X3)` probability flattening, so every 3 by 3 minor must vanish.</p>
  </div>
  <div class="theorem-figure-shell"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/{FIGURE}"><img loading="eager" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/{FIGURE}" alt="P91 mixed-prevalence rank-two flattening separation certificate" /></a></div>
  <div class="frontier-summary-grid">
    <article class="frontier-summary-card"><h3>Global mixture constraint</h3><p>The 4 by 4 flattening is a sum of two rank-one matrices, hence has rank at most two for every prevalence in <strong>[0,1]</strong>.</p></article>
    <article class="frontier-summary-card"><h3>Exact lower exclusion</h3><p>The empirical selected minor has determinant <strong>1/512</strong>. At radius <strong>1/42</strong>, all 512 nonnegative interval-box vertices retain positive determinant.</p></article>
    <article class="frontier-summary-card"><h3>Constructive upper bound</h3><p>A rational P75 point with prevalence <strong>4/5</strong> lies at distance <strong>1/24</strong>, so <strong>1/42 &lt; d_inf &lt;= 1/24</strong>.</p></article>
  </div>
  <div class="boundary"><p><strong>Scientific boundary:</strong> the upper endpoint 1/24 is not claimed to be the exact global optimum. P91 does not identify consciousness, establish nonphysicality, validate an alternative theory, or close the physical-to-experiential bridge.</p></div>
  <p><a href="research-map.html">Research II map</a> · <a href="visual-atlas.html">Theorem figures</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF}">{PROOF}</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROVENANCE}">{PROVENANCE}</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/{SOURCE}">{SOURCE}</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/{TEST}">{TEST}</a></p>
</section>'''


def promote_website() -> None:
    path = "website/index.html"
    text = read(path)
    text = replace_many(
        text,
        (
            ("90 proposition-level results through P90", "91 proposition-level results through P91"),
            ("The 90 results", "The 91 results"),
            ("90-result program", "91-result program"),
            ("all 90 propositions", "all 91 propositions"),
            ("current P90 frontier", "current P91 frontier"),
            ("Current P90 frontier", "Current P91 frontier"),
            ("sources.html#p90-source", "sources.html#p91-source"),
            ("P90 sources", "P91 sources"),
            ("<!-- Current theorem asset: docs/figures/p90_exact_nonlinear_rank_one_separation.svg -->", f"<!-- Current theorem asset: docs/figures/{FIGURE} -->"),
        ),
    )
    text = re.sub(
        r"<!-- current-frontier-home: P90 -->\s*<section id=\"p90-frontier\".*?</section>",
        _p91_home_section(),
        text,
        count=1,
        flags=re.DOTALL,
    )
    write(path, text)

    path = "website/visual-atlas.html"
    text = read(path)
    if 'id="p91-frontier"' not in text:
        p91 = f'''<section id="p91-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head"><p class="eyebrow">Current theorem frontier · P91</p><h2>Mixed-prevalence rank-two flattening separation</h2><p>The full two-component P75 family has rank at most two under the declared bipartite flattening. The exact empirical minor and nonnegative interval certificate give `1/42 &lt; d_inf`, while a genuinely mixed rational model point gives `d_inf &lt;= 1/24`.</p></div>
  <div class="theorem-figure-shell"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/{FIGURE}" alt="P91 mixed-prevalence rank-two flattening certificate" /></div>
  <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF}">{PROOF}</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROVENANCE}">{PROVENANCE}</a></p>
</section>

'''
        anchor = text.find('<section id="p90-frontier"')
        if anchor < 0:
            raise RuntimeError("visual atlas has no P90 frontier anchor")
        text = text[:anchor] + p91 + text[anchor:]
    write(path, text)

    path = "website/start-here.html"
    text = replace_many(
        read(path),
        (
            ("90 results · current frontier P90", "91 results · current frontier P91"),
            ("90 proposition-level results", "91 proposition-level results"),
            ("through P90", "through P91"),
        ),
    )
    write(path, text)

    path = "website/plain-language.html"
    text = replace_many(
        read(path),
        (
            ("Current exact frontier · P90", "Historical exact single-component frontier · P90"),
            ("current P90 frontier", "current P91 frontier"),
            ("90 proposition-level results", "91 proposition-level results"),
            ("through P90", "through P91"),
        ),
    )
    if 'id="p91-reader-frontier"' not in text:
        block = f'''<section class="boundary" id="p91-reader-frontier"><div class="section-head"><p class="eyebrow">Research II · Current frontier · P91</p><h2>The nonlinear separation survives arbitrary latent mixing</h2><p>P90 used one extreme prevalence face. P91 allows both latent components. A rank-two flattening constraint gives a global lower exclusion greater than 1/42, while an explicit mixed model point gives an upper bound of 1/24. The exact global optimum inside that bracket remains open.</p><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF}">Read P91</a></p></div></section>\n\n'''
        marker = '<section class="boundary" id="p90-reader-frontier">'
        text = text.replace(marker, block + marker, 1)
    write(path, text)

    path = "website/research-map.html"
    text = replace_many(
        read(path),
        (
            ("P71-P90", "P71-P91"),
            ("through P90", "through P91"),
            ("90 proposition-level", "91 proposition-level"),
        ),
    )
    if 'id="p91-research-map"' not in text:
        text = text.rstrip() + f'''\n\n<section id="p91-research-map" class="theorem-frontier">
  <div class="section-head"><p class="eyebrow">P91 · Full mixed-prevalence nonlinear separation</p><h2>P91: Does the P90 separation survive when both latent components are active?</h2></div>
  <p>Yes, in certified bracket form. Every P75 mixture has rank at most two under the declared bipartite flattening. The empirical selected minor remains nonzero throughout the closed radius-1/42 box, while a rational P75 point with prevalence 4/5 lies at distance 1/24.</p>
  <p><strong>Certified result:</strong> <code>1/42 &lt; d_inf(P_emp, M75) &lt;= 1/24</code>. The upper endpoint is not claimed globally exact.</p>
  <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF}">{PROOF}</a> · <a href="index.html#p91-frontier">Current frontier</a></p>
</section>\n'''
    write(path, text)

    path = "website/research-lineage.html"
    text = replace_many(
        read(path),
        (
            ("<strong>90</strong><span>proposition-level results</span>", "<strong>91</strong><span>proposition-level results</span>"),
            ("<strong>P90</strong><span>current theorem frontier</span>", "<strong>P91</strong><span>current theorem frontier</span>"),
            ("through P90", "through P91"),
        ),
    )
    write(path, text)

    path = "website/sources.html"
    text = read(path)
    text = append_once(
        text,
        'id="p91-source"',
        f'''<section id="p91-source" class="boundary"><div class="section-head"><p class="eyebrow">Current theorem source record · P91</p><h2>Mixed-prevalence rank-two flattening separation</h2></div><p>Proof: <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF}">{PROOF}</a> · provenance: <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROVENANCE}">{PROVENANCE}</a> · implementation: <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/{SOURCE}">{SOURCE}</a> · tests: <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/{TEST}">{TEST}</a>.</p><p>The rank-two identity is standard linear algebra for a two-component product mixture. The selected exact witness and interval certificate are repository-original. The result does not identify consciousness or prove nonphysicality.</p></section>''',
    )
    write(path, text)


def promote_prepare_website() -> None:
    path = "scripts/prepare_website.py"
    text = read(path)
    text = replace_many(
        text,
        (
            ("p90_exact_nonlinear_rank_one_separation.svg", FIGURE),
            ("Current record:</strong> 90 proposition-level results through P90", "Current record:</strong> 91 proposition-level results through P91"),
            ("with P90", "with P91"),
            ("current P90", "current P91"),
            ("bundled P90", "bundled P91"),
            ("to 90/P90", "to 91/P91"),
            ('id="p90-frontier"', 'id="p91-frontier"'),
            ("pre-P90", "pre-P91"),
            ("<strong>90</strong><span>proposition-level results</span>", "<strong>91</strong><span>proposition-level results</span>"),
            ("<strong>P90</strong><span>current theorem frontier</span>", "<strong>P91</strong><span>current theorem frontier</span>"),
        ),
    )
    write(path, text)


def promote_workflows() -> None:
    replacements = (
        ("Certified P90 visual publication gate", "Certified P91 visual publication gate"),
        ("promote_p90_public_frontier.py", "promote_p91_public_frontier.py"),
        ("test_p90_reader_surface_coherence.py", "test_p91_reader_surface_coherence.py"),
        ("p90_exact_nonlinear_rank_one_separation.svg", FIGURE),
        ('id=\\"p90-frontier\\"', 'id=\\"p91-frontier\\"'),
        ("p90=t.index", "p91=t.index"),
        ("assert p90 < p89 < p88", "assert p91 < p90 < p89"),
        ("Validate committed P90 publication state", "Validate committed P91 publication state"),
        ("Upload reproduced P90 visual record", "Upload reproduced P91 visual record"),
    )
    for path in (".github/workflows/figures.yml", ".github/workflows/reproducibility.yml"):
        text = replace_many(read(path), replacements)
        write(path, text)


def promote_sync_summary() -> None:
    path = "scripts/sync_figure_publication.py"
    text = read(path)
    marker = "    return []\n\n\ndef _frontier_page"
    if "if frontier == 91:" not in text:
        block = '''    if frontier == 91:\n        return [\n            "### Exact P91 mixed-prevalence rank-two witness",\n            "",\n            "P91 removes the extreme-prevalence restriction. The full two-component P75 family obeys a rank-at-most-two bipartite flattening constraint.",\n            "",\n            "```text",\n            "empirical selected determinant = 1/512",\n            "closed radius 1/42: minimum determinant = 23/677376 > 0",\n            "explicit mixed P75 point: distance = 1/24",\n            "1/42 < d_inf(P_emp, M_75) <= 1/24",\n            "```",\n            "",\n            "The upper endpoint is not claimed to be the exact global optimum. P91 does not identify consciousness or close the physical-to-experiential bridge.",\n            "",\n        ]\n'''
        text = text.replace(marker, block + marker, 1)
    write(path, text)


def write_p91_reader_test() -> None:
    path = "tests/test_p91_reader_surface_coherence.py"
    content = f'''from pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\n\n\ndef _read(path: str) -> str:\n    return (ROOT / path).read_text(encoding="utf-8")\n\n\ndef test_p91_proof_states_exact_global_bracket_and_boundary() -> None:\n    text = _read("docs/{PROOF}")\n    assert "1/42" in text\n    assert "1/24" in text\n    assert "rank at most two" in text.lower()\n    assert "does **not** prove that `1/24` is the exact distance" in text\n    assert "physical-to-experiential bridge remains open" in text\n\n\ndef test_p91_homepage_is_current_and_links_complete_record() -> None:\n    text = _read("website/index.html")\n    assert 'id="p91-frontier"' in text\n    assert "Current theorem frontier · P91" in text\n    assert "{FIGURE}" in text\n    assert "{PROOF}" in text\n    assert "{PROVENANCE}" in text\n    assert "{SOURCE}" in text\n    assert "{TEST}" in text\n    assert "1/42" in text and "1/24" in text\n\n\ndef test_visual_atlas_orders_p91_before_historical_p90_and_p89() -> None:\n    text = _read("website/visual-atlas.html")\n    p91 = text.index('id="p91-frontier"')\n    p90 = text.index('id="p90-frontier"')\n    p89 = text.index('id="p89-frontier"')\n    assert p91 < p90 < p89\n    assert "{FIGURE}" in text[p91:p90]\n\n\ndef test_p91_reader_surfaces_preserve_scientific_boundary() -> None:\n    for path in ("README.md", "website/index.html", "website/plain-language.html"):\n        text = _read(path).lower()\n        assert "p91" in text\n        assert "physical-to-experiential bridge" in text\n'''
    write(path, content)


def main() -> None:
    promote_citations()
    promote_navigation()
    promote_roadmap()
    promote_records()
    promote_reproducibility()
    promote_start_and_glossary()
    promote_website()
    promote_prepare_website()
    promote_workflows()
    promote_sync_summary()
    print("[P91] reader-facing publication surfaces promoted")


if __name__ == "__main__":
    main()
