"""Promote reader-facing publication surfaces to the P90 theorem frontier.

P90 is the first theorem after P89 to use a genuinely nonlinear constraint of
the declared P75 image. The strict box fixes prevalence at zero, so the model
reduces to one product Bernoulli component and a canonical 2 by 2 slice must
have determinant zero. Matching exact rational lower and upper certificates
prove full-law L-infinity distance 5/72 for the established witness.

The promoter preserves the Research I, Research II, Research III architecture
and the scientific boundary that model separation is not an identification of
consciousness or a proof of nonphysicality.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURE_NAME = "p90_exact_nonlinear_rank_one_separation.svg"
PROOF_NAME = "proposition_90_exact_nonlinear_rank_one_separation.md"
PROVENANCE_NAME = "p90_equation_provenance.md"
SOURCE_NAME = "exact_nonlinear_rank_one_separation.py"
TEST_NAME = "test_exact_nonlinear_rank_one_separation.py"


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
        text = text.rstrip() + "\n\n" + block.strip() + "\n"
    return text


def write_figure() -> None:
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="900" viewBox="0 0 1440 900" role="img" aria-labelledby="title desc">
<title id="title">P90 Exact Nonlinear Rank-One Slice Separation</title>
<desc id="desc">Three-panel exact certificate. The empirical two by two slice has determinant five over one hundred ninety-two. The rank-one model identity forces an L-infinity radius of at least five over seventy-two. A rational P75 model point attains exactly five over seventy-two, which is seven thirds of the complete P89 linear certificate.</desc>
<rect width="1440" height="900" fill="#ffffff"/>
<text x="72" y="78" font-family="Arial, Helvetica, sans-serif" font-size="38" font-weight="700" fill="#111827">P90 · Exact nonlinear rank-one slice separation</text>
<text x="72" y="122" font-family="Arial, Helvetica, sans-serif" font-size="22" fill="#374151">A nonlinear model-image constraint gives an exact distance beyond the complete P89 linear envelope.</text>
<rect x="60" y="170" width="400" height="500" rx="24" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
<text x="92" y="220" font-family="Arial, Helvetica, sans-serif" font-size="24" font-weight="700" fill="#111827">1 · Empirical slice</text>
<text x="92" y="260" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#475569">Fix (X1, X2) = (1, 0)</text>
<rect x="118" y="305" width="130" height="90" fill="#ffffff" stroke="#64748b"/><rect x="248" y="305" width="130" height="90" fill="#ffffff" stroke="#64748b"/><rect x="118" y="395" width="130" height="90" fill="#ffffff" stroke="#64748b"/><rect x="248" y="395" width="130" height="90" fill="#ffffff" stroke="#64748b"/>
<text x="183" y="360" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="24" fill="#111827">1/8</text><text x="313" y="360" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="24" fill="#111827">1/24</text><text x="183" y="450" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="24" fill="#111827">0</text><text x="313" y="450" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="24" fill="#111827">5/24</text>
<text x="92" y="535" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#111827">det = ad - bc = 5/192</text>
<text x="92" y="578" font-family="Arial, Helvetica, sans-serif" font-size="19" fill="#475569">slice mass = 3/8</text>
<text x="92" y="620" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#475569">The observed table is not rank one.</text>
<rect x="520" y="170" width="400" height="500" rx="24" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
<text x="552" y="220" font-family="Arial, Helvetica, sans-serif" font-size="24" font-weight="700" fill="#111827">2 · Nonlinear lower bound</text>
<text x="552" y="272" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#111827">P75 product slice: ad = bc</text>
<text x="552" y="330" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#475569">Within L-infinity radius e:</text>
<text x="552" y="380" font-family="Arial, Helvetica, sans-serif" font-size="20" fill="#111827">(a-e)(d-e) &lt;= (b+e)(c+e)</text>
<text x="552" y="430" font-family="Arial, Helvetica, sans-serif" font-size="20" fill="#111827">ad - bc &lt;= (a+b+c+d)e</text>
<text x="552" y="500" font-family="Arial, Helvetica, sans-serif" font-size="29" font-weight="700" fill="#111827">e &gt;= 5/72</text>
<text x="552" y="548" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#475569">Exact arithmetic. No floating-point</text>
<text x="552" y="578" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#475569">optimization is needed for the bound.</text>
<rect x="980" y="170" width="400" height="500" rx="24" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
<text x="1012" y="220" font-family="Arial, Helvetica, sans-serif" font-size="24" font-weight="700" fill="#111827">3 · Matching model point</text>
<rect x="1038" y="305" width="130" height="90" fill="#ffffff" stroke="#64748b"/><rect x="1168" y="305" width="130" height="90" fill="#ffffff" stroke="#64748b"/><rect x="1038" y="395" width="130" height="90" fill="#ffffff" stroke="#64748b"/><rect x="1168" y="395" width="130" height="90" fill="#ffffff" stroke="#64748b"/>
<text x="1103" y="360" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="24" fill="#111827">1/18</text><text x="1233" y="360" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="24" fill="#111827">1/9</text><text x="1103" y="450" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="24" fill="#111827">5/72</text><text x="1233" y="450" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="24" fill="#111827">5/36</text>
<text x="1012" y="535" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#111827">det = 0 exactly</text>
<text x="1012" y="578" font-family="Arial, Helvetica, sans-serif" font-size="20" fill="#111827">full-law L-infinity = 5/72</text>
<text x="1012" y="620" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#475569">Lower and upper certificates match.</text>
<rect x="60" y="715" width="1320" height="115" rx="24" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="2"/>
<text x="92" y="760" font-family="Arial, Helvetica, sans-serif" font-size="24" font-weight="700" fill="#111827">Exact comparison</text>
<text x="300" y="760" font-family="Arial, Helvetica, sans-serif" font-size="24" fill="#111827">P89 linear = 5/168</text><text x="620" y="760" font-family="Arial, Helvetica, sans-serif" font-size="24" fill="#111827">P90 nonlinear = 5/72</text><text x="985" y="760" font-family="Arial, Helvetica, sans-serif" font-size="24" font-weight="700" fill="#111827">improvement = 7/3 x</text>
<text x="92" y="804" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#475569">Scientific boundary: exact separation for the declared strict P75 box only. This does not identify consciousness, prove nonphysicality, or close the physical-to-experiential bridge.</text>
</svg>'''
    write(f"docs/figures/{FIGURE_NAME}", svg + "\n")


def promote_readme() -> None:
    path = "README.md"
    text = read(path)
    text = replace_many(text, (
        ("The current public theorem frontier is **P89**.", "The current public theorem frontier is **P90**."),
        ("**Public theorem frontier:** P89", "**Public theorem frontier:** P90"),
        ("docs/proposition_89_complete_linear_parity_duality.md", f"docs/{PROOF_NAME}"),
    ))
    block = f'''### Current theorem frontier

![P90 Exact Nonlinear Rank-One Slice Separation](docs/figures/{FIGURE_NAME})

**Figure 2. P90 exact nonlinear rank-one slice separation.** P90 moves beyond the complete P89 linear parity-functional envelope. On the established strict P75 box, prevalence is fixed at zero, so the observable family is a single product Bernoulli law and the canonical two-by-two slice must satisfy `ad = bc`. The empirical slice has exact determinant residual `5/192`, forcing full-law L-infinity distance at least `5/72`; an explicit rational P75 point attains exactly `5/72`. Thus the exact nonlinear distance is `L90 = 5/72 = (7/3)L89`.

P90 remains a conditional model-separation theorem for the declared strict P75 box. It does not identify consciousness, establish nonphysicality, validate an alternative theory, or close the physical-to-experiential bridge.

'''
    text = re.sub(r"### Current theorem frontier\n.*?(?=## Choose your path)", block, text, flags=re.DOTALL)
    write(path, text)


def promote_citation() -> None:
    for path in ("CITATION.cff", "CITATION.md"):
        text = read(path)
        text = text.replace("Current documented theorem frontier: P89", "Current documented theorem frontier: P90")
        text = text.replace("Current theorem frontier: P89", "Current theorem frontier: P90")
        if path == "CITATION.md":
            text = append_once(text, "proposition_90_exact_nonlinear_rank_one_separation.md", f'''## Current theorem frontier: P90

The current documented theorem frontier is **P90**, an exact nonlinear rank-one slice separation theorem for the declared strict P75 box.

- Proof: [`{PROOF_NAME}`](docs/{PROOF_NAME})
- Equation provenance: [`{PROVENANCE_NAME}`](docs/{PROVENANCE_NAME})
- Implementation: [`{SOURCE_NAME}`](src/consciousness_bridge/{SOURCE_NAME})
- Exact tests: [`{TEST_NAME}`](tests/{TEST_NAME})

P90 is a conditional model-separation result. It does not identify consciousness or establish nonphysicality.''')
        write(path, text)


def promote_docs() -> None:
    path = "docs/detailed_proposition_record.md"
    text = read(path).replace("## Complete P1 to P89 chronology", "## Complete P1 to P90 chronology")
    text = append_once(text, "## Proposition 90: Exact Nonlinear Rank-One Slice Separation", f'''## Proposition 90: Exact Nonlinear Rank-One Slice Separation

P90 moves beyond the complete P89 linear parity-functional envelope by using a nonlinear rank-one identity of the actual strict P75 model image. Because the strict box fixes prevalence at zero, the four-view model is one product Bernoulli law, so every canonical two-by-two slice has determinant zero. The established empirical slice has determinant residual `5/192`, yielding an exact L-infinity lower bound `5/72`; one rational P75 parameter point attains full-law distance exactly `5/72`. Therefore `L90 = 5/72 = (7/3)L89` on the stated witness.

- [Proof]({PROOF_NAME})
- [Equation provenance]({PROVENANCE_NAME})
- Implementation: `src/consciousness_bridge/{SOURCE_NAME}`
- Tests: `tests/{TEST_NAME}`
- Figure: `docs/figures/{FIGURE_NAME}`

This is a conditional exact model-separation theorem for the strict P75 box and does not identify consciousness, establish nonphysicality, or close the physical-to-experiential bridge.''')
    write(path, text)

    path = "docs/research_navigation.md"
    text = read(path)
    text = replace_many(text, (
        ("The current documented theorem frontier is **P89**.", "The current documented theorem frontier is **P90**."),
        ("**Results:** P75 through P89", "**Results:** P75 through P90"),
        ("P74 through P89", "P74 through P90"),
        ("P71 through P89", "P71 through P90"),
        ("the full 89 proposition index", "the full 90 proposition index"),
    ))
    text = append_once(text, "For P90:", f'''## P90 current frontier

For P90:

| What you want | Direct link |
| --- | --- |
| The theorem and proof | [P90 proposition]({PROOF_NAME}) |
| Equation and method provenance | [P90 provenance]({PROVENANCE_NAME}) |
| Implementation | [`{SOURCE_NAME}`](../src/consciousness_bridge/{SOURCE_NAME}) |
| Regression tests | [`{TEST_NAME}`](../tests/{TEST_NAME}) |
| Figure | [P90 nonlinear rank-one certificate](figures/{FIGURE_NAME}) |
| Repository reproduction | [Reproducibility Guide](reproducibility.md) |

P90 is a conditional model-separation result for the declared strict P75 box. It uses nonlinear model-image structure but does not identify the latent state with consciousness, establish nonphysicality, or close the physical-to-experiential bridge.''')
    write(path, text)

    path = "docs/theorem_roadmap.md"
    text = read(path)
    text = replace_many(text, (
        ("The current documented theorem frontier is **P89**.", "The current documented theorem frontier is **P90**."),
        ("P1 through P89 with explicit dependency branches", "P1 through P90 with explicit dependency branches"),
        ("## After P89", "## After P90"),
        ("continuation beyond P89", "continuation beyond P90"),
        ("A future P90 claim", "A future P91 claim"),
    ))
    p89_dependency = "&\\text{P89: complete linear parity-functional duality closes all real linear directions on the eleven canonical parity coordinates}"
    p90_dependency = "&\\text{P90: nonlinear rank-one slice separation gives exact strict-box distance }5/72"
    if p90_dependency not in text:
        if p89_dependency not in text:
            raise RuntimeError("P89 dependency-map anchor missing")
        text = text.replace(p89_dependency, p89_dependency + "\\\\n&\\Downarrow\\\\n" + p90_dependency, 1)

    text = append_once(text, "## P90: exact nonlinear rank-one slice separation", fr'''## P90: exact nonlinear rank-one slice separation

P90 is the first result after the complete P89 linear parity-functional closure to exploit genuinely nonlinear structure of the declared P75 image. On the strict box, prevalence is fixed at zero and the observable law is one product Bernoulli component. A canonical two-by-two slice must therefore satisfy `ad = bc`. The empirical determinant residual `5/192` gives an exact lower radius `5/72`, and a rational P75 point gives a matching full-law upper radius `5/72`.

\[
L_{{90}}=\frac{{5}}{{72}}=\frac{{7}}{{3}}L_{{89}}>\frac{{5}}{{168}}=L_{{89}}.
\]

- Proof: [P90]({PROOF_NAME})
- Provenance: [{PROVENANCE_NAME}]({PROVENANCE_NAME})
- Figure: [P90 nonlinear rank-one certificate](figures/{FIGURE_NAME})
- Source: [`{SOURCE_NAME}`](../src/consciousness_bridge/{SOURCE_NAME})
- Tests: [`{TEST_NAME}`](../tests/{TEST_NAME})

P90 is exact for the stated strict box only. It does not identify consciousness, establish nonphysicality, or solve the physical-to-experiential bridge.

## After P90

A future P91 result should address nonlinear structure beyond the single-component boundary case, for example nonzero latent mixing where rank-one slice identities no longer hold directly.''')
    write(path, text)

    path = "docs/reproducibility.md"
    text = read(path)
    text = text.replace("The current public theorem frontier is **P89**.", "The current public theorem frontier is **P90**.")
    text = append_once(text, "## 5. Focused audit of the current P90 frontier", f'''## 5. Focused audit of the current P90 frontier

The exact P90 technical record is:

```text
docs/{PROOF_NAME}
docs/{PROVENANCE_NAME}
src/consciousness_bridge/{SOURCE_NAME}
tests/{TEST_NAME}
docs/figures/{FIGURE_NAME}
```

Run the focused theorem checks with:

```bash
python -m pytest tests/{TEST_NAME}
```

The exact witness satisfies `L90 = 5/72 = (7/3)L89`. The result is limited to the declared strict single-component P75 box.''')
    write(path, text)


def promote_prepare_website() -> None:
    path = "scripts/prepare_website.py"
    text = read(path)
    text = text.replace('"p89_complete_linear_parity_duality.svg"', f'"{FIGURE_NAME}"')
    text = text.replace('CURRENT_RECORD_TEXT = "Current record:</strong> 89 proposition-level results through P89"', 'CURRENT_RECORD_TEXT = "Current record:</strong> 90 proposition-level results through P90"')
    write(path, text)


def p90_home_section() -> str:
    return f'''<!-- current-frontier-home: P90 -->
<section id="p90-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head">
    <p class="eyebrow">Research II · Current theorem frontier · P90</p>
    <h2>Exact nonlinear rank-one slice separation</h2>
    <p>P90 moves beyond the complete P89 linear envelope. On the strict P75 box, prevalence is fixed at zero, so a canonical two-by-two product-law slice must have determinant zero. The empirical determinant residual gives an exact lower radius of 5/72 and a rational P75 point attains the same full-law radius.</p>
  </div>
  <div class="theorem-figure-shell"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/{FIGURE_NAME}"><img loading="eager" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/{FIGURE_NAME}" alt="P90 exact nonlinear rank-one slice separation certificate" /></a></div>
  <div class="frontier-summary-grid">
    <article class="frontier-summary-card"><h3>Nonlinear model identity</h3><p>The strict P75 box reduces to a product law, forcing the selected slice to satisfy <strong>ad = bc</strong>.</p></article>
    <article class="frontier-summary-card"><h3>Matching exact certificates</h3><p>The determinant residual gives <strong>5/72</strong> as a lower bound and an explicit rational P75 point attains exactly <strong>5/72</strong>.</p></article>
    <article class="frontier-summary-card"><h3>Beyond P89</h3><p><strong>L90 = 5/72 = (7/3)L89</strong>. The gain comes from nonlinear image structure, not a larger linear coefficient search.</p></article>
  </div>
  <div class="boundary"><p><strong>Scientific boundary:</strong> P90 is exact only for the declared strict P75 box. It does not identify consciousness, establish nonphysicality, validate an alternative theory, or close the physical-to-experiential bridge.</p></div>
  <p><a href="research-map.html">Research II map</a> · <a href="visual-atlas.html">Theorem figures</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF_NAME}">{PROOF_NAME}</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROVENANCE_NAME}">{PROVENANCE_NAME}</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/{SOURCE_NAME}">{SOURCE_NAME}</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/{TEST_NAME}">{TEST_NAME}</a></p>
</section>

'''


def promote_website() -> None:
    path = "website/index.html"
    text = read(path)
    text = replace_many(text, (
        ("Explore all 89 results", "Explore all 90 results"),
        ("<strong>89</strong><span>proposition-level results</span>", "<strong>90</strong><span>proposition-level results</span>"),
        ("89 proposition-level results through P89", "90 proposition-level results through P90"),
        ("P89 current theorem frontier", "P90 current theorem frontier"),
        ("Current theorem frontier · P89", "Current theorem frontier · P90"),
        ("The 89 results form several dependency branches.", "The 90 results form several dependency branches."),
        ("all 89 propositions", "all 90 propositions"),
        ("P71-P89", "P71-P90"), ("P73-P89", "P73-P90"), ("P74-P89", "P74-P90"), ("P75-P89", "P75-P90"), ("P1-P89", "P1-P90"),
    ))
    text = re.sub(
        r'<!-- current-frontier-home: P(?:89|90) -->\s*<section id="p(?:89|90)-frontier".*?</section>\s*',
        "",
        text,
        flags=re.DOTALL,
    )
    marker = '<section id="research-iii-overview"'
    if marker not in text:
        raise RuntimeError("website index Research III marker missing")
    text = text.replace(marker, p90_home_section() + marker, 1)
    write(path, text)

    path = "website/visual-atlas.html"
    text = read(path)
    text = re.sub(r'<!-- current-frontier-visual: P89 -->\s*', "", text)
    text = text.replace('<section id="p89-frontier" class="theorem-frontier current-frontier-visual">', '<section id="p89-frontier" class="theorem-frontier">')
    text = text.replace("Current theorem frontier · P89", "Previous theorem frontier · P89")
    text = re.sub(
        r'<!-- current-frontier-visual: P90 -->\s*<section id="p90-frontier".*?</section>\s*',
        "",
        text,
        flags=re.DOTALL,
    )
    atlas = p90_home_section().replace("current-frontier-home", "current-frontier-visual")
    marker = '<section id="p89-frontier"'
    if marker not in text:
        raise RuntimeError("Visual Atlas P89 section missing")
    text = text.replace(marker, atlas + marker, 1)
    text = text.replace("P1-P89", "P1-P90").replace("89 results", "90 results")
    write(path, text)

    for path in ("website/start-here.html", "website/plain-language.html", "website/research-lineage.html"):
        text = read(path)
        text = replace_many(text, (
            ("89 results", "90 results"), ("89-result", "90-result"), ("89 propositions", "90 propositions"),
            ("P1-P89", "P1-P90"), ("P75-P89", "P75-P90"), ("P71-P89", "P71-P90"),
            ("current frontier P89", "current frontier P90"), ("current theorem frontier P89", "current theorem frontier P90"),
            ("<strong>P89</strong><span>current theorem frontier</span>", "<strong>P90</strong><span>current theorem frontier</span>"),
            ("<strong>89</strong><span>proposition-level results</span>", "<strong>90</strong><span>proposition-level results</span>"),
        ))
        write(path, text)

    # P90 reader-surface canonicalization
    path = "website/plain-language.html"
    text = read(path)
    text = text.replace("This is the 90-result Research II theorem program currently reaching P89.", "This is the 90-result Research II theorem program currently reaching P90.")
    text = text.replace("currently through P89.", "currently through P90.")
    text = text.replace("The current theorem frontier is P89.", "The current theorem frontier is P90.")
    text = text.replace("P88 is a checkpoint, not the destination", "P90 is the current checkpoint, not the destination")
    text = text.replace("P88 is one mathematical checkpoint inside a much larger research program.", "P90 is the current mathematical checkpoint inside a much larger research program.")
    text = text.replace("The destination is not Proposition 89, 100, or 200.", "The destination is not Proposition 90, 100, or 200.")
    text = text.replace("shows how all 88 Research II results connect", "shows how all 90 Research II results connect")
    text = re.sub(r'<section class="boundary" id="p(?:89|90)-reader-frontier">.*?</section>', '<section class="boundary" id="p90-reader-frontier"><div class="section-head"><p class="eyebrow">Research II · Current exact frontier · P90</p><h2>Exact nonlinear rank-one slice separation</h2><p>P90 moves beyond the complete P89 linear parity-functional envelope by exploiting a nonlinear identity of the declared strict P75 model image. With prevalence fixed at zero, the active law is one product Bernoulli component, so the canonical two-by-two slice must satisfy <strong>ad = bc</strong>. The empirical determinant residual is <strong>5/192</strong>, giving the exact distance <strong>L90 = 5/72 = (7/3)L89</strong>, while P89 remains the complete-linear subfrontier at <strong>5/168</strong>.</p><p>This is a conditional exact separation result for the stated strict box. It does not identify consciousness, establish nonphysicality, exhaust more general nonlinear mixture regimes, or close the physical-to-experiential bridge.</p></div></section>', text, count=1, flags=re.DOTALL)
    write(path, text)

    path = "website/start-here.html"
    text = read(path)
    text = text.replace("current Research II P89 frontier", "current Research II P90 frontier")
    text = text.replace("Open all 89 Research II results", "Open all 90 Research II results")
    text = text.replace("P78-P89 progressively tighten global separation", "P78-P90 progressively tighten global separation")
    if '      <p><strong>P90 moves beyond that complete linear envelope.</strong> On the strict P75 box, prevalence is fixed at zero, so the active observable law is a single product Bernoulli component and a canonical two-by-two slice must satisfy <strong>ad = bc</strong>. The empirical determinant residual gives a lower radius of <strong>5/72</strong>, and an explicit rational P75 point attains the same full-law distance. Thus <strong>L90 = 5/72 = (7/3)L89</strong>.</p>' not in text:
        text = text.replace('      <p><strong>P89 closes the complete real linear parity-functional class.</strong> <strong>P89 is the current complete-linear frontier.</strong> It removes both the finite coefficient-radius restriction and the exactly-four-observable support restriction. Across every real linear functional of all eleven canonical P83 parity coordinates, matching exact lower and upper certificates prove <strong>L89 = 5/168</strong>, strictly above <strong>L88 = 1/64</strong>.</p>', '      <p><strong>P89 closes the complete real linear parity-functional class.</strong> <strong>P89 is the current complete-linear frontier.</strong> It removes both the finite coefficient-radius restriction and the exactly-four-observable support restriction. Across every real linear functional of all eleven canonical P83 parity coordinates, matching exact lower and upper certificates prove <strong>L89 = 5/168</strong>, strictly above <strong>L88 = 1/64</strong>.</p>' + "\n" + '      <p><strong>P90 moves beyond that complete linear envelope.</strong> On the strict P75 box, prevalence is fixed at zero, so the active observable law is a single product Bernoulli component and a canonical two-by-two slice must satisfy <strong>ad = bc</strong>. The empirical determinant residual gives a lower radius of <strong>5/72</strong>, and an explicit rational P75 point attains the same full-law distance. Thus <strong>L90 = 5/72 = (7/3)L89</strong>.</p>', 1)
    text = text.replace('docs/proposition_89_complete_linear_parity_duality.md">Read P89 theorem', 'docs/proposition_90_exact_nonlinear_rank_one_separation.md">Read P90 theorem')
    write(path, text)

    path = "website/implementation.html"
    text = read(path).replace("Stage 06 · P73-P89", "Stage 06 · P73-P90").replace("P73-P89", "P73-P90")
    write(path, text)

    path = "website/research-map.html"
    text = read(path)
    text = replace_many(text, (("P75-P89", "P75-P90"), ("P71-P89", "P71-P90"), ("P1-P89", "P1-P90")))
    text = append_once(text, "p90-research-map", f'''<section id="p90-research-map" class="theorem-frontier">
  <div class="section-head"><p class="eyebrow">P90 · Nonlinear model-image separation</p><h2>P90: How much stronger is the actual nonlinear P75 image than its complete linear envelope?</h2></div>
  <p>On the strict box, the selected two-by-two slice must satisfy the rank-one identity <code>ad = bc</code>. Matching exact certificates prove full-law L-infinity distance <strong>5/72</strong>, equal to <strong>7/3</strong> times P89's complete linear value.</p>
  <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF_NAME}">{PROOF_NAME}</a> · <a href="index.html#p90-frontier">Current frontier</a></p>
</section>''')
    write(path, text)


def promote_figure_surfaces() -> None:
    path = "docs/figure_catalog.md"
    text = read(path)
    text = append_once(text, FIGURE_NAME, f'''| [P90 Exact Nonlinear Rank-One Slice Separation](figures/{FIGURE_NAME}) | What this figure shows: the empirical canonical two-by-two slice violates the rank-one product-law identity by determinant 5/192; the exact interval argument gives radius 5/72; a rational P75 model point attains the same full-law radius. Main takeaway: nonlinear model-image structure certifies `L90 = 5/72 = (7/3)L89`. | Conditional exact model separation for the declared strict P75 box only. | [Proposition 90]({PROOF_NAME}) |''')
    write(path, text)

    for path in ("docs/figures/README.md", "figures/README.md", "figures/CURRENT_FRONTIER.md"):
        text = read(path)
        text = append_once(text, FIGURE_NAME, f'''## P90 current theorem frontier

![P90 exact nonlinear rank-one slice separation]({"" if path == "docs/figures/README.md" else "../docs/figures/"}{FIGURE_NAME})

Canonical theorem figure: `{FIGURE_NAME}`. P90 proves the exact strict-box nonlinear distance `5/72`, beyond the complete P89 linear value `5/168`.''')
        write(path, text)

    path = "docs/equation_and_citation_map.md"
    text = read(path)
    text = append_once(text, PROVENANCE_NAME, f'''## P90 exact nonlinear rank-one slice separation

- Theorem: [Proposition 90]({PROOF_NAME})
- Equation provenance: [P90 equation record]({PROVENANCE_NAME})
- Implementation: [`{SOURCE_NAME}`](../src/consciousness_bridge/{SOURCE_NAME})
- Tests: [`{TEST_NAME}`](../tests/{TEST_NAME})
- Figure: [P90 nonlinear rank-one certificate](figures/{FIGURE_NAME})''')
    write(path, text)

    path = "docs/claim_source_matrix.md"
    text = read(path)
    text = text.replace("The current repository contains 89 proposition-level results", "The current repository contains 90 proposition-level results")
    text = text.replace("P75-P89", "P75-P90")
    text = append_once(text, "P90 nonlinear rank-one separation", f'''| P90 nonlinear rank-one separation | The strict P75 box has exact full-law L-infinity distance 5/72 from the established empirical witness | repository theorem | [P90 proof]({PROOF_NAME}), [P90 provenance]({PROVENANCE_NAME}), implementation/tests, [P90 figure](figures/{FIGURE_NAME}) | Exact only for the declared strict single-component box; no consciousness identification or nonphysicality claim |''')
    write(path, text)


def main() -> None:
    write_figure()
    promote_readme()
    promote_citation()
    promote_docs()
    promote_prepare_website()
    promote_website()
    promote_figure_surfaces()
    print("P90 public frontier surfaces promoted")


if __name__ == "__main__":
    main()
