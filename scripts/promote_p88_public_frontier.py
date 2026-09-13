"""Guarded one-time promotion of the held-out P88 theorem frontier.

Run only after the candidate P88 implementation/tests are green.  The script
promotes the formal proof/provenance/figure and synchronizes reader-facing
frontier surfaces.  CI must validate the transformed tree before it is merged.
"""

from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = "proposition_88_heldout_selected_parity_functional_certification.md"
FIGURE = "p88_heldout_selected_parity_functional_certification.svg"
SOURCE = "heldout_selected_parity_functional_certification.py"
TEST = "test_heldout_selected_parity_functional_certification.py"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_all(path: str, pairs: tuple[tuple[str, str], ...]) -> None:
    text = read(path)
    for old, new in pairs:
        text = text.replace(old, new)
    write(path, text)


def replace_function(text: str, name: str, next_name: str, replacement: str) -> str:
    pattern = re.compile(
        rf"def {re.escape(name)}\(.*?(?=\ndef {re.escape(next_name)}\()",
        re.DOTALL,
    )
    text, count = pattern.subn(replacement.rstrip() + "\n\n", text, count=1)
    if count != 1:
        raise RuntimeError(f"could not replace function {name}")
    return text


def formalize_docs() -> None:
    candidate = ROOT / "docs" / "p88_candidate_heldout_selected_parity_functional_certification.md"
    provenance = ROOT / "docs" / "p88_candidate_equation_provenance.md"
    if not candidate.is_file() or not provenance.is_file():
        raise RuntimeError("candidate P88 proof/provenance are missing")

    proof_text = candidate.read_text(encoding="utf-8")
    proof_text = proof_text.replace(
        "# Candidate P88: Held-Out Certification for a Discovery-Selected P87 Box/Functional Test",
        "# Proposition 88: Held-Out Certification for a Discovery-Frozen P75 Box/P87 Functional Test",
    )
    proof_text = proof_text.replace(
        "**Candidate theorem under exact regression audit.** This document does not promote the public theorem frontier beyond P87 yet.",
        "**Proved conditional finite-sample theorem with exact computational certificate.**",
    )
    proof_text = proof_text.replace("Candidate P88", "P88")
    proof_text = proof_text.replace("candidate P88", "P88")
    proof_text += r'''

---

## 7. Exact held-out sample-size design threshold

For a discovery-frozen functional with exact score width $R$ and a specified
functional interval gap $\Delta>0$, the ideal Hoeffding rejection inequality is

\[
R\sqrt{\frac{\log(2/\alpha)}{2n}}<\Delta.
\]

Equivalently,

\[
\boxed{
n>\frac{R^2\log(2/\alpha)}{2\Delta^2}.
}
\]

P88 does not use a floating-point approximation to decide the implemented
threshold.  The function `p88_minimum_validation_sample_size_for_gap_exact`
searches for the smallest integer $n$ for which the P79-certified rational
upper radius satisfies the strict inequality.

For the stored witness, $R=5$, $\Delta=5/24$, and $\alpha=1/20$, so the ideal
expression is $n>288\log 40$.  With the declared P79 settings (12 logarithm
series terms and a 24-bit dyadic square-root ceiling), the exact certified
threshold is

\[
\boxed{n_{\min}=1063.}
\]

At $n=1062$ the certified unit-range radius is $349591/8388608$ and the strict
rejection inequality still fails.  At $n=1063$ the unit-range radius is
$698853/16777216$ and the strict inequality holds.  This is a deterministic
design threshold for a *specified* gap; it is not a prospective guarantee that
a random validation sample will realize that gap.

---

## 8. Proposition 88

Let discovery data $D$ determine a P75 parameter box $B_D$ and one P87
functional $Q_D$.  Let an IID validation sample of size $n$ from population law
$p$ be independent of $D$.  Conditional on $D$, define the exact P75 interval
$I_{B_D}(Q_D)$, exact score width $R_D$, empirical validation value
$\widehat Q_D$, exact centered transfer norm $D(Q_D)$, and a P79-certified
rational upper bound $\bar r_{n,\alpha}$ on
$\sqrt{\log(2/\alpha)/(2n)}$.  Then with probability at least $1-\alpha$,

\[
\boxed{
\inf_{q\in\mathcal M_{B_D}}\|p-q\|_\infty
\ge
\frac{
[\operatorname{dist}(\widehat Q_D,I_{B_D}(Q_D))
-R_D\bar r_{n,\alpha}]_+
}{D(Q_D)}.
}
\]

Consequently, under the null $p\in\mathcal M_{B_D}$, the rejection rule

\[
\operatorname{dist}(\widehat Q_D,I_{B_D}(Q_D))
>R_D\bar r_{n,\alpha}
\]

has conditional type-I error at most $\alpha$, and the same coverage holds
unconditionally after averaging over discovery data.  No union bound over the
39,600-function discovery family is required because exactly one box/functional
pair is frozen before validation.

The theorem is box-specific.  It becomes a statement about the full admissible
P75 family only when the frozen box covers that family or a separately certified
covering argument extends the result to every required box.

---

## 9. Scientific interpretation boundary

P88 is a finite-sample validation theorem for a declared statistical model set.
It does not establish that the P75 latent variable is consciousness; it does not
prove consciousness is nonphysical; it does not validate an alternative model
after rejection; and it does not close the physical-to-experiential bridge.
The software also cannot establish experimental independence or prove that the
tested box/function was genuinely frozen before validation was inspected.
'''
    write(f"docs/{PROOF}", proof_text)
    candidate.unlink()

    provenance_text = provenance.read_text(encoding="utf-8")
    provenance_text = provenance_text.replace(
        "# Candidate P88 Equation Provenance", "# P88 Equation Provenance"
    )
    provenance_text = provenance_text.replace(
        "Candidate P88 remains unpromoted until its implementation and full repository regression gates are green.",
        "P88 is the proved conditional finite-sample frontier theorem after full repository regression audit.",
    )
    provenance_text = provenance_text.replace("Candidate P88", "P88")
    provenance_text = provenance_text.replace("candidate P88", "P88")
    provenance_text += r'''

## 10. Exact design-threshold provenance

The ideal scalar Hoeffding inequality $R\sqrt{\log(2/\alpha)/(2n)}<\Delta$
rearranges to

\[
n>\frac{R^2\log(2/\alpha)}{2\Delta^2}.
\]

The repository implementation does not round this expression to decide the
certificate.  It searches integer $n$ and evaluates the P79 rational upper
envelope at each candidate.  For $R=5$, $\Delta=5/24$, $\alpha=1/20$, 12
series terms, and 24 square-root bits, exact regression checks prove $n=1062$
is insufficient and $n=1063$ is sufficient.
'''
    write("docs/p88_equation_provenance.md", provenance_text)
    provenance.unlink()


def write_figure() -> None:
    svg = r'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="760" viewBox="0 0 1280 760" role="img" aria-labelledby="p88-title p88-desc">
<title id="p88-title">P88 held-out certification for a discovery-frozen P75 box and P87 functional</title>
<desc id="p88-desc">Proposition 88 separates discovery from validation. Discovery may select a P75 parameter box and one of the P87 parity functionals, but both are frozen before an independent validation sample is examined. Conditional Hoeffding concentration then needs no 39,600-way multiplicity penalty. The exact witness has score width 5, interval gap 5 over 24, a 95 percent certified minimum validation size of 1063, and at n equals 2400 a positive full-law L-infinity lower confidence bound 701849 over 201326592. The theorem is box-specific unless a separate global covering argument is supplied and does not identify the latent state with consciousness.</desc>
<defs><style>
.bg{fill:#f7f9fc}.panel{fill:#fff;stroke:#cfd8e6;stroke-width:1.5}.soft{fill:#eef4fb;stroke:#9bb4cf;stroke-width:1.2}.ok{fill:#eef8f1;stroke:#8eb89a;stroke-width:1.2}.warn{fill:#fff7e8;stroke:#d6b267;stroke-width:1.2}.head{fill:#173b65}.ink{fill:#172235;font-family:Arial,Helvetica,sans-serif}.muted{fill:#5d6a7c;font-family:Arial,Helvetica,sans-serif}.white{fill:#fff;font-family:Arial,Helvetica,sans-serif}.title{font-size:30px;font-weight:700}.section{font-size:20px;font-weight:700}.body{font-size:14px}.formula{font-size:17px;font-weight:700}.metric{font-size:24px;font-weight:700}.arrow{stroke:#6c87a7;stroke-width:2;fill:none;marker-end:url(#a)}</style><marker id="a" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 Z" fill="#6c87a7"/></marker></defs>
<rect class="bg" width="1280" height="760"/><rect class="head" width="1280" height="112"/><text class="white title" x="52" y="49">P88 Held-Out Selection-Valid Certificate</text><text class="white body" x="52" y="78">Freeze the P75 box and P87 functional on discovery data; test exactly once on independent validation data.</text>
<rect class="panel" x="48" y="145" rx="16" width="270" height="430"/><text class="ink section" x="70" y="182">1. Discovery</text><text class="muted body" x="70" y="212">Use discovery-only information to choose:</text><rect class="soft" x="70" y="240" rx="12" width="226" height="90"/><text class="ink formula" x="90" y="270">P75 box B_D</text><text class="ink formula" x="90" y="301">P87 score Q_D</text><text class="muted body" x="70" y="366">The pair may come from a 39,600-</text><text class="muted body" x="70" y="388">functional search, then it is frozen.</text><rect class="warn" x="70" y="426" rx="12" width="226" height="105"/><text class="ink formula" x="90" y="456">No validation reuse</text><text class="muted body" x="90" y="482">Changing B or Q after looking</text><text class="muted body" x="90" y="503">at validation breaks this proof.</text>
<path class="arrow" d="M325 360 L385 360"/>
<rect class="panel" x="392" y="145" rx="16" width="270" height="430"/><text class="ink section" x="414" y="182">2. Held-out validation</text><text class="muted body" x="414" y="212">Independent IID sample V, size n.</text><rect class="soft" x="414" y="240" rx="12" width="226" height="105"/><text class="ink formula" x="434" y="270">R = g_max - g_min</text><text class="ink formula" x="434" y="300">ε̄ = R r̄(n, α)</text><text class="muted body" x="434" y="326">P79 gives exact rational r̄.</text><rect class="ok" x="414" y="378" rx="12" width="226" height="116"/><text class="ink formula" x="434" y="408">No 39,600-way penalty</text><text class="muted body" x="434" y="434">Conditional on discovery, exactly</text><text class="muted body" x="434" y="455">one fixed scalar score is tested.</text>
<path class="arrow" d="M669 360 L729 360"/>
<rect class="panel" x="736" y="145" rx="16" width="496" height="430"/><text class="ink section" x="760" y="182">3. Exact rejection and confidence bound</text><rect class="soft" x="762" y="220" rx="12" width="444" height="98"/><text class="ink formula" x="782" y="251">Δ̂ = dist(Q̂_V, I_B(Q))</text><text class="ink formula" x="782" y="282">distance ≥ [Δ̂ - ε̄]₊ / D(Q)</text><rect class="ok" x="762" y="342" rx="12" width="212" height="174"/><text class="ink formula" x="782" y="372">Exact witness</text><text class="muted body" x="782" y="399">R = 5, Δ̂ = 5/24</text><text class="ink metric" x="782" y="438">n_min = 1063</text><text class="muted body" x="782" y="467">95% certified threshold</text><rect class="ok" x="994" y="342" rx="12" width="212" height="174"/><text class="ink formula" x="1014" y="372">At n = 2400</text><text class="muted body" x="1014" y="399">population distance LCB</text><text class="ink formula" x="1014" y="432">701849 /</text><text class="ink formula" x="1014" y="456">201326592 &gt; 0</text><text class="muted body" x="1014" y="486">confidence ≥ 95%</text>
<rect class="head" x="48" y="611" rx="14" width="1184" height="101"/><text class="white formula" x="72" y="643">Scientific boundary</text><text class="white body" x="72" y="670">The certificate is for the P75 laws inside the discovery-frozen box. It becomes global only with a separately valid covering argument.</text><text class="white body" x="72" y="693">It does not identify a latent state with consciousness, prove nonphysicality, or solve the physical-to-experiential bridge.</text>
</svg>'''
    write(f"docs/figures/{FIGURE}", svg + "\n")


def update_reader_docs() -> None:
    readme = read("README.md")
    replacements = (
        ("P1-P87 program map, and the current P87 frontier", "P1-P88 program map, and the current P88 frontier"),
        ("| Public theorem frontier | **P87** |", "| Public theorem frontier | **P88** |"),
        ("| Proposition-level results | **87** |", "| Proposition-level results | **88** |"),
        ("P1 to P87 detailed proposition record", "P1 to P88 detailed proposition record"),
        ("**87 proposition-level results** and **71 equation-driven quantitative figures**. The theorem frontier is P86.", "**88 proposition-level results** and **72 equation-driven quantitative figures**. The theorem frontier is P88."),
        ("**87 proposition-level results** and **71 equation-driven quantitative figures**. The theorem frontier is P87.", "**88 proposition-level results** and **72 equation-driven quantitative figures**. The theorem frontier is P88."),
        ("The repository now contains 87 proposition-level results. The theorem frontier is P87.", "The repository now contains 88 proposition-level results. The theorem frontier is P88."),
        ("P71-P87", "P71-P88"),
        ("P75-P87", "P75-P88"),
        ("P77-P87", "P77-P88"),
        ("Current theorem frontier: **P87**", "Current theorem frontier: **P88**"),
        ("**P87 current-frontier figure.**", "**P87 previous-frontier figure.**"),
    )
    for old, new in replacements:
        readme = readme.replace(old, new)
    p88 = r'''

P88 closes the post-selection finite-sample gap created by the much larger P87 search family. A discovery sample may choose a P75 parameter box and one P87 functional, but the pair must then be frozen before an independent validation sample is examined. Conditional on discovery, scalar Hoeffding concentration applies to the single fixed score, so no 39,600-way multiplicity penalty is required. P79 supplies an exact rational one-sided radius, and the P87 centered coefficient norm transfers the held-out functional mismatch to a full-law $L_\infty$ lower confidence bound. For the exact stored witness, the score width is 5 and the interval gap is $5/24$; the certified 95% validation-size threshold is **1063**, and at $n=2400$ the exact lower confidence bound is $701849/201326592>0$.

![P88 held-out selected parity-functional certificate](docs/figures/p88_heldout_selected_parity_functional_certification.svg)

**P88 current-frontier figure.** P88 is a selection-valid finite-sample theorem for a discovery-frozen P75 box/P87 functional pair. The result is box-specific unless a separate certified covering argument extends it to the complete P75 family, and it does not identify a latent state with consciousness.
'''
    anchor = "**P87 previous-frontier figure.**"
    pos = readme.find(anchor)
    if pos < 0:
        raise RuntimeError("README P87 caption anchor missing")
    paragraph_end = readme.find("\n\n", pos)
    if "P88 closes the post-selection" not in readme:
        readme = readme[:paragraph_end] + p88 + readme[paragraph_end:]
    write("README.md", readme)

    start = read("START_HERE.md")
    for old, new in (
        ("87-result theorem program", "88-result theorem program"),
        ("87 proposition-level results", "88 proposition-level results"),
        ("current theorem frontier is **P87**", "current theorem frontier is **P88**"),
        ("**Proposition frontier:** P87", "**Proposition frontier:** P88"),
        ("**Proposition-level results:** 87", "**Proposition-level results:** 88"),
        ("P71-P87", "P71-P88"),
        ("P75-P87", "P75-P88"),
        ("P77-P87", "P77-P88"),
    ):
        start = start.replace(old, new)
    if "## Current frontier: P88" not in start:
        start += f'''\n\n## Current frontier: P88\n\nP88 gives selection-valid finite-sample certification for a discovery-frozen P75 box/P87 functional pair evaluated once on independent validation data. The exact witness has a 95% certified validation threshold of **1063** observations for the specified gap and a positive exact lower confidence bound at `n=2400`. The result applies to the frozen box unless a separate global covering argument is supplied.\n\n- [P88 proof](docs/{PROOF})\n- [P88 equation provenance](docs/p88_equation_provenance.md)\n- [P88 implementation](src/consciousness_bridge/{SOURCE})\n- [P88 exact tests](tests/{TEST})\n- [P88 figure](docs/figures/{FIGURE})\n'''
    write("START_HERE.md", start)

    detailed = read("docs/detailed_proposition_record.md")
    detailed = detailed.replace("Complete P1 to P87 chronology", "Complete P1 to P88 chronology")
    if "## Proposition 88:" not in detailed:
        detailed += f'''\n\n## Proposition 88: Held-out certification for a discovery-frozen P75 box/P87 functional test\n\nP88 freezes a P75 parameter box and one P87 functional using information independent of a subsequent validation sample. Conditional on discovery, one scalar score is fixed, so P79-certified Hoeffding concentration gives a selection-valid held-out radius without a 39,600-function union bound. The exact P87 centered norm transfers the resulting population functional gap into a full-law L-infinity lower confidence bound against the law set generated inside the frozen box.\n\nFor the stored exact witness, score width `R=5`, observed gap `5/24`, and `alpha=1/20`. The exact certified design threshold is `n=1063`; at `n=2400`, the full-law lower confidence bound is `701849/201326592 > 0`. The box and functional must be frozen before validation is inspected, and box-specific rejection is not automatically global P75 rejection.\n\n- Proof: [{PROOF}]({PROOF})\n- Provenance: [p88_equation_provenance.md](p88_equation_provenance.md)\n- Implementation: [`{SOURCE}`](../src/consciousness_bridge/{SOURCE})\n- Tests: [`{TEST}`](../tests/{TEST})\n- Figure: [`{FIGURE}`](figures/{FIGURE})\n'''
    write("docs/detailed_proposition_record.md", detailed)


def update_roadmap_navigation_repro() -> None:
    road = read("docs/theorem_roadmap.md")
    road = road.replace("The current documented theorem frontier is **P87**.", "The current documented theorem frontier is **P88**.")
    road = road.replace("P1 through P87", "P1 through P88")
    road = road.replace("P71-P87", "P71-P88")
    road = road.replace("## After P87", "## Previous frontier boundary: P87")
    dep_end = "\\text{P87: the complete primitive coefficient box at radius two strengthens the P86 four-event certificate}"
    if "\\text{P88:" not in road:
        road = road.replace(dep_end, dep_end + "\\\\\n&\\Downarrow\\\\\n&\\text{P88: held-out validation gives selection-valid finite-sample certification for a discovery-frozen P75 box/P87 score}")
    if "## P88: held-out selection-valid finite-sample certification" not in road:
        road += f'''\n\n## P88: held-out selection-valid finite-sample certification\n\nP88 closes a statistical gap left by the deterministic P87 search. A discovery-only rule may choose a P75 parameter box and one of the 39,600 P87 functionals, after which the pair is frozen and evaluated on independent validation data. Conditional Hoeffding concentration, certified through P79 with `K=1`, gives a box-specific full-law lower confidence bound without a functional-family union bound. The exact witness has `n_min=1063` for its specified 95% gap and a positive exact lower confidence bound at `n=2400`.\n\nDirect proof: [P88]({PROOF}). Provenance: [P88 equation record](p88_equation_provenance.md). Implementation: [`{SOURCE}`](../src/consciousness_bridge/{SOURCE}). Tests: [`{TEST}`](../tests/{TEST}).\n\n## After P88\n\nThe next statistical gap is global held-out coverage over a certified family of parameter boxes or a selection-valid procedure that controls adaptive reuse of validation information without requiring a single pre-frozen box. Any continuation must preserve the distinction between box-specific model rejection and rejection of the complete admissible P75 family.\n'''
    write("docs/theorem_roadmap.md", road)

    nav = read("docs/research_navigation.md")
    nav = nav.replace("The current documented theorem frontier is **P87**.", "The current documented theorem frontier is **P88**.")
    nav = nav.replace("P1 through P87", "P1 through P88")
    nav = nav.replace("P71-P87", "P71-P88")
    recommended_marker = "## Recommended reading order"
    scientific_marker = "## Scientific branch map"
    a = nav.index(recommended_marker)
    b = nav.index(scientific_marker, a)
    rec = nav[a:b]
    if "[P88 " not in rec:
        rec += f"\n1. [P88 held-out selection-valid certification]({PROOF}) for independent discovery/validation, the exact 1063-observation threshold, and the box-specific lower confidence bound.\n"
        nav = nav[:a] + rec + nav[b:]
    branch_start = nav.index(scientific_marker)
    index_marker = "## Complete proposition index"
    branch_end = nav.index(index_marker, branch_start)
    branch = nav[branch_start:branch_end]
    if "| P88 |" not in branch:
        branch += f"\n| Held-out selected-functional finite-sample certification | P88 | Freezes a discovery-selected P75 box/P87 score and validates it on independent data without a 39,600-way functional penalty | [P88]({PROOF}) |\n"
        nav = nav[:branch_start] + branch + nav[branch_end:]
    if f"| P88 | [Held-out selection-valid certification]({PROOF})" not in nav:
        nav += f"\n| P88 | [Held-out selection-valid certification]({PROOF}) | independent held-out validation for a discovery-frozen P75 box/P87 functional |\n"
    write("docs/research_navigation.md", nav)

    repro = read("docs/reproducibility.md")
    repro = repro.replace("The current theorem frontier is **P87**.", "The current theorem frontier is **P88**.")
    repro = repro.replace("## 12. Reproduce the current P87 implementation checks directly", "## 12. Reproduce the current P88 implementation checks directly")
    repro = repro.replace("docs/proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md", f"docs/{PROOF}")
    repro = repro.replace("docs/p87_equation_provenance.md", "docs/p88_equation_provenance.md")
    repro = repro.replace("tests/test_bounded_primitive_quad_projection_parity_functional_separation.py", f"tests/{TEST}")
    write("docs/reproducibility.md", repro)


def update_scholarly_and_catalog() -> None:
    for path in ("CITATION.cff", "CITATION.md", "docs/equation_and_citation_map.md"):
        text = read(path)
        text = text.replace("Current documented theorem frontier: P87.", "Current documented theorem frontier: P88.")
        text = text.replace("Current theorem frontier: **P87**", "Current theorem frontier: **P88**")
        text = text.replace("current theorem frontier is **P87**", "current theorem frontier is **P88**")
        if "P88 held-out" not in text:
            text += "\nP88 held-out validation freezes a discovery-selected P75 box/P87 functional pair before independent validation and provides a selection-valid exact-rational finite-sample certificate.\n"
        write(path, text)
    catalog = read("docs/figure_catalog.md")
    if FIGURE not in catalog:
        catalog += f'''\n\n## P88 held-out selection-valid certificate\n\n![P88 held-out selection-valid certificate](figures/{FIGURE})\n\n**What it shows.** Discovery chooses and freezes a P75 box/P87 functional pair; independent validation applies a scalar P79-certified Hoeffding radius; the exact witness has a 1063-observation certified threshold and a positive lower confidence bound at `n=2400`.\n\n**Scientific status.** Source-controlled theorem diagram for [Proposition 88]({PROOF}). The result is box-specific without an additional covering theorem and is not evidence that the P75 latent state is consciousness.\n'''
    write("docs/figure_catalog.md", catalog)


def update_verifier() -> None:
    text = read("scripts/verify_repository.py")
    text = text.replace('CURRENT_FRONTIER = "P87"', 'CURRENT_FRONTIER = "P88"')
    text = text.replace('    "docs/figures/p87_exact_bounded_primitive_quad_projection_parity.svg",', '    "docs/figures/p87_exact_bounded_primitive_quad_projection_parity.svg",\n    "docs/figures/p88_heldout_selected_parity_functional_certification.svg",')
    text = text.replace('    "docs/p87_equation_provenance.md",', '    "docs/p87_equation_provenance.md",\n    "docs/proposition_88_heldout_selected_parity_functional_certification.md",\n    "docs/p88_equation_provenance.md",')
    text = text.replace("for number in range(1, 88):", "for number in range(1, int(CURRENT_FRONTIER[1:]) + 1):")
    text = re.sub(
        r'if not current_figure\.endswith\(\s*"p87_exact_bounded_primitive_quad_projection_parity\.svg"\s*\):\s*raise RuntimeError\([^\n]+\)',
        'if not current_figure.endswith("p88_heldout_selected_parity_functional_certification.svg"):\n        raise RuntimeError("figure manifest does not point to the canonical P88 SVG")',
        text,
    )
    old = '''    p87 = visual_atlas.index('id="p87-frontier"')\n    p86 = visual_atlas.index('id="p86-frontier"')\n    p84 = visual_atlas.index('id="p84-frontier"')\n    p85 = visual_atlas.index('id="p85-frontier"')\n    if not (p87 < p86 and p87 < p84 and p87 < p85):\n        raise RuntimeError("Visual Atlas does not lead with the current P87 figure")'''
    new = '''    p88 = visual_atlas.index('id="p88-frontier"')\n    p87 = visual_atlas.index('id="p87-frontier"')\n    p86 = visual_atlas.index('id="p86-frontier"')\n    p84 = visual_atlas.index('id="p84-frontier"')\n    p85 = visual_atlas.index('id="p85-frontier"')\n    if not (p88 < p87 and p88 < p86 and p88 < p84 and p88 < p85):\n        raise RuntimeError("Visual Atlas does not lead with the current P88 figure")'''
    if old not in text:
        raise RuntimeError("P87 visual-atlas verifier block not found")
    text = text.replace(old, new)
    stale_anchor = "STALE_READER_FRONTIER_MARKERS = (\n"
    if '"Current theorem frontier · P87"' not in text.split("STALE_READER_FRONTIER_MARKERS",1)[1].split(")",1)[0]:
        text = text.replace(stale_anchor, stale_anchor + '    "Current theorem frontier · P87",\n    "<strong>P87</strong><span>current theorem frontier</span>",\n    "current P87 frontier",\n    "actual P87 research frontier",\n', 1)
    write("scripts/verify_repository.py", text)


def update_figure_sync() -> None:
    path = "scripts/sync_figure_publication.py"
    text = read(path)
    p88_func = f'''def _p88_visual_section() -> str:\n    return f\'\'\'<section id="p88-frontier" class="theorem-frontier current-frontier-visual">\n  <div class="section-head">\n    <p class="eyebrow">Current theorem frontier · P88</p>\n    <h2>Held-out selection-valid finite-sample certificate</h2>\n    <p>P88 freezes a discovery-selected P75 box/P87 functional pair before independent validation, avoiding a 39,600-way functional multiplicity penalty.</p>\n  </div>\n  <div class="theorem-figure-shell"><a href="{{BLOB_PREFIX}}docs/figures/{FIGURE}"><img loading="eager" decoding="async" src="{{RAW_FIGURE_PREFIX}}{FIGURE}" alt="P88 held-out certification with a 1063-observation exact threshold and positive 95 percent lower confidence bound" /></a></div>\n  <div class="frontier-summary-grid">\n    <article class="frontier-summary-card"><h3>Selection-valid split</h3><p>The P75 box and P87 functional are frozen using information independent of validation.</p></article>\n    <article class="frontier-summary-card"><h3>Exact design threshold</h3><p>For the stored gap, the P79-certified 95% minimum validation size is <strong>1063</strong>.</p></article>\n    <article class="frontier-summary-card"><h3>Positive held-out bound</h3><p>At n=2400 the exact full-law lower confidence bound is <strong>701849/201326592 &gt; 0</strong>.</p></article>\n  </div>\n  <div class="boundary"><p><strong>Scientific boundary:</strong> The result is for laws inside the frozen P75 box unless a separate global covering argument is supplied. It does not identify consciousness.</p></div>\n  <p><a href="{{BLOB_PREFIX}}docs/{PROOF}">Open P88</a> · <a href="{{BLOB_PREFIX}}docs/p88_equation_provenance.md">Equation provenance</a> · <a href="{{BLOB_PREFIX}}src/consciousness_bridge/{SOURCE}">Implementation</a> · <a href="{{BLOB_PREFIX}}tests/{TEST}">Exact tests</a></p>\n</section>\'\'\'\n'''
    text = replace_function(text, "_p87_visual_section", "_remove_section", p88_func)
    text = text.replace("def _demote_p86(text: str) -> str:", "def _demote_p87(text: str) -> str:")
    text = text.replace('"Current theorem frontier · P86",\n        "Previous theorem frontier · P86",', '"Current theorem frontier · P87",\n        "Previous theorem frontier · P87",')

    visual = '''def _normalize_visual_atlas(text: str) -> str:\n    text = _remove_section(text, "p88-frontier")\n    text = _demote_p87(text)\n    text = re.sub(r"\\s*<!-- current-frontier-visual: P\\d+ -->\\s*", "\\n", text)\n    boundary = re.search(r'<section class="boundary">.*?</section>', text, re.DOTALL)\n    if boundary is None:\n        raise RuntimeError("could not locate Visual Atlas reading-boundary section")\n    prefix = text[: boundary.end()].rstrip()\n    suffix = text[boundary.end() :].lstrip()\n    insertion = "\\n\\n<!-- current-frontier-visual: P88 -->\\n" + _p88_visual_section() + "\\n\\n"\n    result = prefix + insertion + suffix\n    return "\\n".join(line.rstrip() for line in result.splitlines()) + "\\n"\n'''
    text = replace_function(text, "_normalize_visual_atlas", "_normalize_homepage", visual)

    home = '''def _normalize_homepage(text: str) -> str:\n    text = _remove_section(text, "p88-frontier")\n    text = _demote_p87(text)\n    replacements = (\n        ("The 87 results form several dependency branches.", "The 88 results form several dependency branches."),\n        ("all 87 propositions", "all 88 propositions"),\n        ("P71-P87", "P71-P88"),\n        ("P75-P87", "P75-P88"),\n        ("<strong>87</strong><span>proposition-level results</span>", "<strong>88</strong><span>proposition-level results</span>"),\n        ("<strong>P87</strong><span>current theorem frontier</span>", "<strong>P88</strong><span>current theorem frontier</span>"),\n        ("Explore all 87 results", "Explore all 88 results"),\n        ("The 87-result program", "The 88-result program"),\n    )\n    for old, new in replacements:\n        text = text.replace(old, new)\n    text = re.sub(r"\\s*<!-- current-frontier-home: P\\d+ -->\\s*", "\\n", text)\n    hero = re.search(r'<section class="hero">.*?</section>', text, re.DOTALL)\n    if hero is None:\n        raise RuntimeError("could not locate homepage hero section")\n    prefix = text[: hero.end()].rstrip()\n    suffix = text[hero.end() :].lstrip()\n    insertion = "\\n\\n<!-- current-frontier-home: P88 -->\\n" + _p88_visual_section() + "\\n\\n"\n    result = prefix + insertion + suffix\n    return "\\n".join(line.rstrip() for line in result.splitlines()) + "\\n"\n'''
    text = replace_function(text, "_normalize_homepage", "_expected_outputs", home)
    text = text.replace("if frontier == 87:", "if frontier == 88:")
    text = text.replace("### Exact P87 hierarchy witness", "### Exact P88 held-out witness")
    text = text.replace("P87 completes the primitive four-event coefficient box with nonzero integer coefficients satisfying `|c_i| <= 2` and strictly strengthens the complete P86 certificate on the exact rational witness:", "P88 adds selection-valid finite-sample certification for a discovery-frozen P75 box/P87 functional pair:")
    text = text.replace('"L85 = 0 < L86 = 1/192 < L87 = 1/96",\n                "120 primitive sign-normalized coefficient patterns per four-event subset",\n                "39,600 standard P87 functionals",', '"n_min = 1063 for the stored 95% target gap",\n                "n = 2400 gives 701849/201326592 > 0",\n                "box/function frozen before independent validation",')
    text = text.replace("if frontier != 87:\n        raise RuntimeError(f\"P87 synchronizer expected frontier 87, found {frontier}\")", "if frontier != 88:\n        raise RuntimeError(f\"P88 synchronizer expected frontier 88, found {frontier}\")")
    write(path, text)


def update_website_builder_and_pages() -> None:
    path = "scripts/prepare_website.py"
    text = read(path)
    text = text.replace('CURRENT_FRONTIER_FIGURE = "p87_exact_bounded_primitive_quad_projection_parity.svg"', f'CURRENT_FRONTIER_FIGURE = "{FIGURE}"')
    text = re.sub(r'ASSET_VERSION = "[^"]+"', 'ASSET_VERSION = "20260913-mobile18-p88"', text, count=1)
    validation = '''def _validate_current_frontier_pages(output: Path) -> None:\n    """Require P88 to be the primary visual frontier in the canonical website."""\n    frontier_figure = output / "figures" / CURRENT_FRONTIER_FIGURE\n    if not frontier_figure.is_file():\n        raise RuntimeError(f"website build is missing the current P88 theorem figure: {frontier_figure}")\n    local_frontier_src = f'src="figures/{CURRENT_FRONTIER_FIGURE}"'\n    visual_atlas_path = output / "visual-atlas.html"\n    if not visual_atlas_path.is_file():\n        raise RuntimeError("website build is missing visual-atlas.html")\n    visual_atlas = visual_atlas_path.read_text(encoding="utf-8")\n    if local_frontier_src not in visual_atlas:\n        raise RuntimeError("Visual Atlas does not use the bundled P88 theorem figure")\n    p88_atlas = visual_atlas.index('id="p88-frontier"')\n    for marker in ('id="p87-frontier"', 'id="p86-frontier"', 'id="p85-frontier"'):\n        if p88_atlas >= visual_atlas.index(marker):\n            raise RuntimeError(f"Visual Atlas does not present P88 before {marker}")\n    homepage_path = output / "index.html"\n    if not homepage_path.is_file():\n        raise RuntimeError("website build is missing index.html")\n    homepage = homepage_path.read_text(encoding="utf-8")\n    if local_frontier_src not in homepage:\n        raise RuntimeError("Homepage does not use the bundled P88 theorem figure")\n    p88 = homepage.index('id="p88-frontier"')\n    for marker in ('id="plain-language"', 'id="p87-frontier"', 'id="p86-frontier"', 'id="p85-frontier"'):\n        if p88 >= homepage.index(marker):\n            raise RuntimeError(f"Homepage P88 frontier appears too late, after {marker}")\n    stale_tokens = ("Current theorem frontier · P87", "The 87 results form several dependency branches.", "all 87 propositions")\n    stale = [token for token in stale_tokens if token in homepage]\n    if stale:\n        raise RuntimeError(f"Homepage contains stale pre-P88 reader text: {stale}")\n'''
    text = replace_function(text, "_validate_current_frontier_pages", "prepare_website", validation)
    write(path, text)

    note = '<section class="frontier-note"><p><strong>Current theorem frontier: P88.</strong> Held-out validation freezes a discovery-selected P75 box/P87 functional pair before independent validation; the physical-to-experiential bridge remains open.</p></section>'
    for relative in ("website/plain-language.html", "website/start-here.html", "website/research-map.html", "website/sources.html"):
        page = read(relative)
        for old, new in (("87 results", "88 results"), ("P71-P87", "P71-P88"), ("P75-P87", "P75-P88")):
            page = page.replace(old, new)
        if "Current theorem frontier: P88" not in page:
            page = page.replace("</main>", note + "\n</main>", 1) if "</main>" in page else page.replace("</body>", note + "\n</body>", 1)
        write(relative, page)


def update_changelog() -> None:
    text = read("CHANGELOG.md")
    if "Promote P88 held-out" not in text[:2500]:
        text = text.replace("# Changelog\n", "# Changelog\n\n## Unreleased\n\n### Promote P88 held-out selection-valid certification\n\n- Freeze discovery-selected P75 box/P87 functional pairs before independent validation and certify scalar Hoeffding error without a 39,600-way functional penalty.\n- Add exact sample-size design threshold `n=1063` for the stored 95% gap and a positive full-law lower confidence bound at `n=2400`.\n- Keep rejection explicitly box-specific unless a separate global covering argument is supplied.\n", 1)
    write("CHANGELOG.md", text)


def main() -> None:
    if (ROOT / "docs" / PROOF).exists():
        raise RuntimeError("P88 is already formalized; refusing duplicate promotion")
    formalize_docs()
    write_figure()
    update_reader_docs()
    update_roadmap_navigation_repro()
    update_scholarly_and_catalog()
    update_verifier()
    update_figure_sync()
    update_website_builder_and_pages()
    update_changelog()
    subprocess.run(["python", "scripts/sync_figure_publication.py"], cwd=ROOT, check=True)
    print("[p88-promotion] transformed repository publication frontier to P88")


if __name__ == "__main__":
    main()
