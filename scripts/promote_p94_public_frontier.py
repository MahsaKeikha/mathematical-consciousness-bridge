"""Promote the validated P94 candidate to the public theorem frontier.

This is a one-run migration helper for PR #156. It fails loudly when expected
P93 publication markers are absent, writes the formal P94 proposition and
source-authored theorem SVG, advances reader/navigation surfaces, and leaves
figure gateway regeneration to ``generate_all_figures.py``.

Delete this helper after the exact promoted head is validated.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CANDIDATE = ROOT / "docs" / "p94_candidate_finite_range_dependent_sign_coherence.md"
FORMAL = ROOT / "docs" / "proposition_94_finite_range_dependent_sign_coherence.md"
FIGURE = ROOT / "docs" / "figures" / "p94_finite_range_dependent_sign_coherence.svg"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(path: str, old: str, new: str) -> None:
    text = read(path)
    if text.count(old) != 1:
        raise RuntimeError(f"{path}: expected one occurrence of {old!r}, found {text.count(old)}")
    write(path, text.replace(old, new, 1))


def require(path: str, token: str) -> None:
    if token not in read(path):
        raise RuntimeError(f"{path}: missing required token {token!r}")


def replace_section(text: str, section_id: str, replacement: str) -> str:
    pattern = re.compile(
        rf'<section(?=[^>]*\bid="{re.escape(section_id)}")[^>]*>.*?</section>',
        flags=re.DOTALL,
    )
    match = pattern.search(text)
    if match is None:
        raise RuntimeError(f"missing section id={section_id!r}")
    return text[: match.start()] + replacement + text[match.end() :]


def promote_proof() -> None:
    if FORMAL.exists():
        raise RuntimeError("formal P94 proposition already exists")
    if not CANDIDATE.is_file():
        raise RuntimeError("P94 candidate proof is missing")
    text = CANDIDATE.read_text(encoding="utf-8")
    text = text.replace(
        "# P94 Candidate: Finite-Range Dependent Sign-Coherence Rejection",
        "# Proposition 94: Finite-Range Dependent Sign-Coherence Rejection",
        1,
    )
    marker = "\n## Scientific boundary\n"
    if marker not in text:
        raise RuntimeError("P94 candidate lacks scientific-boundary marker")
    drift = r'''
## P94G. Exact temporal-drift no-go certificate

The common-marginal assumption is not a cosmetic restriction. The P75 family is
not closed under arbitrary pooling of time-varying parameter regimes.

P94 supplies two explicit parameter vectors, each strictly inside the P75 cube.
Each time-specific P75 law has a strictly positive P92 determinant product. Yet
the equal-weight pooled law has

\[
(D_1,D_2,D_3)
=
\left(
-\frac{65}{65536},
\frac{11}{65536},
\frac{3}{65536}
\right),
\]

so

\[
\boxed{
D_1D_2D_3
=
-\frac{2145}{281474976710656}<0.
}
\]

Thus a pooled sample from drifting but individually valid P75 regimes can
produce exactly the qualitative sign pattern used by the P92 rejection witness.
Finite-range dependence with one common marginal law is therefore a different
problem from temporal drift. A future drift theorem must declare a population
target that remains meaningful under time variation rather than silently
interpreting the pooled law as one stationary P75 distribution.

The exact construction is implemented by
`certify_p94_temporal_pooling_no_go_exact()` and covered by regression tests.
'''
    text = text.replace(marker, "\n" + drift + marker, 1)
    FORMAL.write_text(text, encoding="utf-8")
    CANDIDATE.unlink()


def write_figure() -> None:
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="900" viewBox="0 0 1440 900" role="img" aria-labelledby="title desc">
<title id="title">P94 Finite-Range Dependent Sign-Coherence Rejection</title>
<desc id="desc">What this figure shows: P94 extends the P93 seven-cell finite-sample sign-coherence rejection rule from IID observations to a declared m-dependent sequence with one common marginal law. Residue classes modulo m plus one yield independent groups, Holder and Hoeffding give a squared-radius penalty of m plus one, and exact rational certification gives threshold examples 1623 for m zero, 3246 for m one, and 4869 for m two. A separate exact construction shows why temporal drift is not covered: two individually valid interior P75 regimes can pool to a law with negative three-minor determinant product. Scientific status: conditional model rejection under the declared common-marginal finite-range dependence model; not a drift-robust theorem and not a consciousness ontology claim.</desc>
<rect width="1440" height="900" fill="#ffffff"/>
<text x="72" y="70" font-family="Arial, Helvetica, sans-serif" font-size="35" font-weight="700" fill="#111827">P94 · Finite-range dependent sign-coherence rejection</text>
<text x="72" y="112" font-family="Arial, Helvetica, sans-serif" font-size="19" fill="#374151">P93 supplies the localized nonlinear witness. P94 relaxes temporal independence while keeping one common marginal law.</text>

<rect x="58" y="150" width="310" height="560" rx="22" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
<text x="86" y="194" font-family="Arial, Helvetica, sans-serif" font-size="21" font-weight="700" fill="#111827">1 · Declared dependence</text>
<text x="86" y="234" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#475569">Common marginal law P</text>
<text x="86" y="266" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#475569">m-dependent observations</text>
<rect x="86" y="300" width="252" height="88" rx="15" fill="#ffffff" stroke="#94a3b8"/>
<text x="212" y="333" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#475569">Color time by residue</text>
<text x="212" y="366" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="24" font-weight="700" fill="#111827">q = m + 1</text>
<text x="86" y="430" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#475569">Indices in each residue class</text>
<text x="86" y="458" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#475569">are mutually independent.</text>
<line x1="86" y1="494" x2="338" y2="494" stroke="#cbd5e1"/>
<text x="86" y="536" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#475569">Classes need not be independent.</text>
<text x="86" y="568" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#475569">Generalized Holder combines</text>
<text x="86" y="596" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#475569">their moment bounds safely.</text>

<rect x="388" y="150" width="360" height="560" rx="22" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
<text x="416" y="194" font-family="Arial, Helvetica, sans-serif" font-size="21" font-weight="700" fill="#111827">2 · Dependence-adjusted radius</text>
<text x="416" y="238" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#475569">For one selected cell:</text>
<text x="568" y="282" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="700" fill="#111827">Pr(error &gt; eps) &lt;= 2 exp(-2 n eps^2/q)</text>
<rect x="416" y="318" width="304" height="98" rx="16" fill="#ffffff" stroke="#94a3b8"/>
<text x="568" y="350" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#475569">Seven-cell simultaneous radius</text>
<text x="568" y="384" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="700" fill="#111827">eps^2 = (m+1) log(14/alpha)/(2n)</text>
<text x="416" y="462" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#475569">Exact gate:</text>
<text x="432" y="500" font-family="Arial, Helvetica, sans-serif" font-size="17" font-weight="700" fill="#111827">certified upper eps^2 &lt; r_min^2</text>
<text x="416" y="548" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#475569">P79 supplies the rational</text>
<text x="416" y="576" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#475569">logarithm bracket. No ordinary</text>
<text x="416" y="604" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#475569">floating square root is needed.</text>

<rect x="768" y="150" width="282" height="560" rx="22" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
<text x="796" y="194" font-family="Arial, Helvetica, sans-serif" font-size="21" font-weight="700" fill="#111827">3 · Exact 95% crossings</text>
<text x="796" y="244" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#475569">Established r_min = 1/24</text>
<rect x="796" y="280" width="226" height="74" rx="14" fill="#ffffff" stroke="#94a3b8"/>
<text x="909" y="309" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#475569">m = 0</text>
<text x="909" y="337" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="21" font-weight="700" fill="#111827">1623 / 1632</text>
<rect x="796" y="376" width="226" height="74" rx="14" fill="#ffffff" stroke="#94a3b8"/>
<text x="909" y="405" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#475569">m = 1</text>
<text x="909" y="433" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="21" font-weight="700" fill="#111827">3246 / 3264</text>
<rect x="796" y="472" width="226" height="74" rx="14" fill="#ffffff" stroke="#94a3b8"/>
<text x="909" y="501" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#475569">m = 2</text>
<text x="909" y="529" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="21" font-weight="700" fill="#111827">4869 / 4872</text>
<text x="796" y="590" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#475569">first number = mathematical crossing</text>
<text x="796" y="618" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#475569">second = exact 24-count replication</text>

<rect x="1070" y="150" width="312" height="560" rx="22" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
<text x="1098" y="194" font-family="Arial, Helvetica, sans-serif" font-size="21" font-weight="700" fill="#111827">4 · Drift is different</text>
<text x="1098" y="236" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#475569">Two interior P75 regimes:</text>
<text x="1098" y="270" font-family="Arial, Helvetica, sans-serif" font-size="17" font-weight="700" fill="#111827">product(D) &gt; 0 in each</text>
<line x1="1098" y1="300" x2="1354" y2="300" stroke="#cbd5e1"/>
<text x="1098" y="342" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#475569">50/50 pooled law:</text>
<text x="1098" y="382" font-family="Arial, Helvetica, sans-serif" font-size="16" font-weight="700" fill="#111827">D1 = -65/65536</text>
<text x="1098" y="414" font-family="Arial, Helvetica, sans-serif" font-size="16" font-weight="700" fill="#111827">D2 = 11/65536</text>
<text x="1098" y="446" font-family="Arial, Helvetica, sans-serif" font-size="16" font-weight="700" fill="#111827">D3 = 3/65536</text>
<rect x="1098" y="482" width="256" height="92" rx="15" fill="#ffffff" stroke="#64748b"/>
<text x="1226" y="516" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#475569">pooled determinant product</text>
<text x="1226" y="548" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="19" font-weight="700" fill="#111827">-2145 / 2^48 &lt; 0</text>
<text x="1098" y="618" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#475569">Pooling drift can imitate rejection.</text>
<text x="1098" y="646" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#475569">P94 therefore requires one marginal law.</text>

<rect x="58" y="752" width="1324" height="106" rx="22" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="2"/>
<text x="88" y="794" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#111827">Scientific boundary</text>
<text x="286" y="794" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#111827">Conditional on a declared finite dependence range and one common marginal law.</text>
<text x="88" y="832" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#475569">Non-rejection is inconclusive. P94 does not establish drift robustness, unknown-range robustness, nonphysicality, or a completed physical-to-experiential bridge.</text>
</svg>'''
    FIGURE.write_text(svg, encoding="utf-8")


def promote_verifier() -> None:
    path = "scripts/verify_repository.py"
    text = read(path)
    if 'CURRENT_FRONTIER = "P93"' not in text:
        raise RuntimeError("repository verifier is not on P93")
    text = text.replace('CURRENT_FRONTIER = "P93"', 'CURRENT_FRONTIER = "P94"', 1)
    anchor = '    "tests/test_localized_sign_coherence_rejection.py",\n'
    if anchor not in text:
        raise RuntimeError("verifier P93 core-file anchor missing")
    addition = (
        anchor
        + '    "docs/proposition_94_finite_range_dependent_sign_coherence.md",\n'
        + '    "docs/p94_equation_provenance.md",\n'
        + '    "docs/figures/p94_finite_range_dependent_sign_coherence.svg",\n'
        + '    "src/consciousness_bridge/finite_range_dependent_sign_coherence.py",\n'
        + '    "src/consciousness_bridge/finite_range_dependent_sign_coherence_threshold.py",\n'
        + '    "tests/test_finite_range_dependent_sign_coherence.py",\n'
    )
    text = text.replace(anchor, addition, 1)
    text = text.replace(
        'if "Current documented theorem frontier: P93" not in citation:\n        raise RuntimeError("CITATION.md does not declare P93 as the current theorem frontier")',
        'if f"Current documented theorem frontier: {CURRENT_FRONTIER}" not in citation:\n        raise RuntimeError(f"CITATION.md does not declare {CURRENT_FRONTIER} as the current theorem frontier")',
        1,
    )
    stale_anchor = 'STALE_READER_FRONTIER_MARKERS = (\n'
    if stale_anchor not in text:
        raise RuntimeError("stale-reader marker tuple missing")
    text = text.replace(
        stale_anchor,
        stale_anchor
        + '    "Current theorem frontier · P93",\n'
        + '    "current P93 frontier",\n'
        + '    "<strong>P93</strong><span>current theorem frontier</span>",\n',
        1,
    )
    write(path, text)


def promote_syncer() -> None:
    path = "scripts/sync_figure_publication.py"
    text = read(path)
    text = text.replace(
        '            "empirical determinants = (-1/48, 1/64, 5/192)",\n            "empirical determinants = (-1/48, 1/64, 5/192)",',
        '            "empirical determinants = (-1/48, 1/64, 5/192)",',
        1,
    )
    text = text.replace(
        '            "d_inf(P_emp, M_75) = 1/24",\n            "d_inf(P_emp, M_75) = 1/24",',
        '            "d_inf(P_emp, M_75) = 1/24",',
        1,
    )
    anchor = '    return []\n\n\ndef _frontier_page'
    if anchor not in text:
        raise RuntimeError("syncer frontier-summary return anchor missing")
    p94 = '''    if frontier == 94:
        return [
            "### Exact P94 finite-range dependent sign-coherence rejection",
            "",
            "P94 preserves the P92/P93 nonlinear rejection witness under a declared finite-range dependent stream with one common marginal law.",
            "",
            "```text",
            "eps_m^2 = (m+1) log(14/alpha) / (2n)",
            "m=0: crossing 1623; exact replication 1632",
            "m=1: crossing 3246; exact replication 3264",
            "m=2: crossing 4869; exact replication 4872",
            "pooled-drift no-go determinants = (-65/65536, 11/65536, 3/65536)",
            "pooled determinant product = -2145/281474976710656",
            "```",
            "",
            "P94 is conditional on the declared dependence range and common marginal law. It does not establish arbitrary drift robustness or identify consciousness.",
            "",
        ]
    return []


def _frontier_page'''
    text = text.replace(anchor, p94, 1)
    write(path, text)


def promote_prepare_website() -> None:
    replace_once(
        "scripts/prepare_website.py",
        '    "p93_localized_sign_coherence_rejection.svg"\n',
        '    "p94_finite_range_dependent_sign_coherence.svg"\n',
    )
    replace_once(
        "scripts/prepare_website.py",
        'CURRENT_RECORD_TEXT = "Current record:</strong> 93 proposition-level results through P93"',
        'CURRENT_RECORD_TEXT = "Current record:</strong> 94 proposition-level results through P94"',
    )


def promote_readme() -> None:
    path = "README.md"
    text = read(path)
    required = (
        "The current public theorem frontier is **P93**.",
        "**Public theorem frontier:** P93",
        "[Read the current frontier](docs/proposition_93_localized_sign_coherence_rejection.md)",
    )
    for token in required:
        if token not in text:
            raise RuntimeError(f"README missing {token!r}")
    text = text.replace("The current public theorem frontier is **P93**.", "The current public theorem frontier is **P94**.", 1)
    text = text.replace("**Public theorem frontier:** P93", "**Public theorem frontier:** P94", 1)
    text = text.replace(
        "[Read the current frontier](docs/proposition_93_localized_sign_coherence_rejection.md)",
        "[Read the current frontier](docs/proposition_94_finite_range_dependent_sign_coherence.md)",
        1,
    )
    pattern = re.compile(r"### Current theorem frontier\n.*?(?=\n### |\n## )", re.DOTALL)
    match = pattern.search(text)
    if match is None:
        raise RuntimeError("README current theorem section missing")
    current = '''### Current theorem frontier

![P94 Finite-Range Dependent Sign-Coherence Rejection](docs/figures/p94_finite_range_dependent_sign_coherence.svg)

**Figure 2. P94 finite-range dependent sign-coherence rejection.** P94 keeps the P92/P93 seven-cell nonlinear witness but replaces the IID concentration step with a declared finite-range dependence model. For dependence range `m`, the squared confidence radius is multiplied by `m+1`. At 95 percent confidence, the established witness crosses at 1623 for `m=0`, 3246 for `m=1`, and 4869 for `m=2`. An exact temporal-pooling no-go construction shows why arbitrary drift is outside this theorem: two individually valid interior P75 regimes can pool to a law with negative determinant product.

P94 is conditional on one common marginal four-view law and a declared finite dependence range. Non-rejection remains inconclusive. The result does not identify consciousness, establish nonphysicality, or close the physical-to-experiential bridge.
'''
    text = text[: match.start()] + current + text[match.end() :]
    text = text.replace("### P93 localized finite-sample frontier", "### P93 historical IID finite-sample frontier")
    text = text.replace("The current Research II frontier is [P93]", "The historical IID finite-sample step is [P93]")
    write(path, text)


def promote_citations() -> None:
    path = "CITATION.md"
    text = read(path)
    text = text.replace("## Current theorem frontier: P93", "## Current theorem frontier: P94", 1)
    text = text.replace("The current documented theorem frontier is **P93**.", "The current documented theorem frontier is **P94**.", 1)
    if "P94" not in text:
        raise RuntimeError("CITATION.md P94 promotion failed")
    write(path, text)

    path = "CITATION.cff"
    text = read(path)
    text = text.replace("Current documented theorem frontier: P93.", "Current documented theorem frontier: P94.")
    insertion = (
        " Proposition 94 extends the localized P92/P93 sign-coherence rejection witness to a declared finite-range dependent sequence with one common marginal law, uses exact rational certification of the dependence-adjusted radius, and gives an exact temporal-pooling counterexample showing why arbitrary marginal drift is outside that theorem."
    )
    marker = " Current documented theorem frontier: P94."
    if marker not in text:
        raise RuntimeError("CITATION.cff current frontier marker missing after replacement")
    text = text.replace(marker, insertion + marker, 1)
    write(path, text)


def promote_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    text = text.replace("The current documented theorem frontier is **P93**.", "The current documented theorem frontier is **P94**.", 1)
    text = text.replace("**Results:** P75 through P93", "**Results:** P75 through P94", 1)
    text = text.replace(
        "**Current frontier:** [P93: Localized Finite-Sample Sign-Coherence Rejection](proposition_93_localized_sign_coherence_rejection.md)",
        "**Current frontier:** [P94: Finite-Range Dependent Sign-Coherence Rejection](proposition_94_finite_range_dependent_sign_coherence.md)",
        1,
    )
    text = text.replace("P74 through P93 via", "P74 through P94 via")
    text = text.replace("P71 through P93", "P71 through P94")
    text = text.replace("the full 93 proposition index", "the full 94 proposition index", 1)
    text = text.replace("## P93 current frontier", "## P93 historical IID finite-sample frontier", 1)
    p94 = '''

## P94 current frontier

For P94:

| What you want | Direct link |
| --- | --- |
| The theorem and proof | [P94 proposition](proposition_94_finite_range_dependent_sign_coherence.md) |
| Equation and method provenance | [P94 provenance](p94_equation_provenance.md) |
| Implementation | [`finite_range_dependent_sign_coherence.py`](../src/consciousness_bridge/finite_range_dependent_sign_coherence.py) |
| Exact threshold implementation | [`finite_range_dependent_sign_coherence_threshold.py`](../src/consciousness_bridge/finite_range_dependent_sign_coherence_threshold.py) |
| Exact tests | [`test_finite_range_dependent_sign_coherence.py`](../tests/test_finite_range_dependent_sign_coherence.py) |
| Figure | [P94 finite-range dependence certificate](figures/p94_finite_range_dependent_sign_coherence.svg) |

P94 relaxes temporal independence, not stationarity. Its confidence radius carries an exact `m+1` squared-radius penalty under a declared finite dependence range and one common marginal law. The exact pooling counterexample proves that arbitrary marginal drift can imitate the P92 negative determinant-product pattern, so drift remains outside the theorem.
'''
    if p94.strip() in text:
        raise RuntimeError("P94 navigation block already present")
    text = text.rstrip() + p94 + "\n"
    write(path, text)


def promote_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    text = text.replace(
        "The current documented theorem frontier is **P93**. The proposition record runs from **P1 through P93 with explicit dependency branches**. P71-P93 return",
        "The current documented theorem frontier is **P94**. The proposition record runs from **P1 through P94 with explicit dependency branches**. P71-P94 return",
        1,
    )
    needle = "&\\text{P93: the P92 sign-coherence witness yields a localized seven-cell finite-sample rejection certificate}\\\\\n"
    if needle not in text:
        raise RuntimeError("roadmap P93 dependency node missing")
    text = text.replace(
        needle,
        needle + "&\\Downarrow\\\\\n&\\text{P94: finite-range dependence preserves the localized rejection gate under one common marginal law}\\\\\n",
        1,
    )
    table_anchor = "| [P92](proposition_92_exact_global_mixed_prevalence_distance.md) | three-minor conditional sign coherence | exact full-cube mixed-prevalence P75 distance `d_inf = 1/24` | proved conditional nonlinear theorem |\n"
    if table_anchor not in text:
        raise RuntimeError("roadmap proposition-index anchor missing")
    table_add = table_anchor + "| [P93](proposition_93_localized_sign_coherence_rejection.md) | seven-cell finite-sample sign preservation | localized IID rejection of P75 | proved conditional statistical theorem |\n| [P94](proposition_94_finite_range_dependent_sign_coherence.md) | finite-range coloring, Holder-Hoeffding concentration, exact rational radius certification | localized finite-range dependent rejection plus temporal-pooling no-go | proved conditional statistical theorem |\n"
    text = text.replace(table_anchor, table_add, 1)
    text = text.replace("A substantive continuation beyond P93", "A substantive continuation beyond P94")
    text = text.replace("None of P71-P93 identifies", "None of P71-P94 identifies")
    after_pattern = re.compile(r"## After P93\n\n.*?(?=\n## |\Z)", re.DOTALL)
    after_match = after_pattern.search(text)
    if after_match is None:
        raise RuntimeError("roadmap After P93 block missing")
    after = r'''## P94: finite-range dependent sign-coherence rejection

P94 keeps the P92 population sign-coherence obstruction and P93 seven-cell localization, but replaces IID sampling by a declared finite-range dependent sequence with one common marginal law. With `q=m+1`, residue classes modulo `q` are internally independent and generalized Holder combines their Hoeffding moment bounds without requiring independence between classes. This gives

\[
\varepsilon^{(m)}_{n,7}(\alpha)=\sqrt{\frac{(m+1)\log(14/\alpha)}{2n}}.
\]

The executable certificate compares the squared radius using P79 exact rational logarithm bounds. The exact drift no-go construction separately proves that pooling time-varying but individually valid P75 regimes can create a negative P92 determinant product, so common marginality is scientifically necessary for this theorem.

Direct proof: [P94](proposition_94_finite_range_dependent_sign_coherence.md). Provenance: [P94 equation record](p94_equation_provenance.md). Implementation: [`finite_range_dependent_sign_coherence.py`](../src/consciousness_bridge/finite_range_dependent_sign_coherence.py). Tests: [`test_finite_range_dependent_sign_coherence.py`](../tests/test_finite_range_dependent_sign_coherence.py).

## After P94

P94 closes the first short-range temporal-dependence extension of the localized P92/P93 witness. Any P95 candidate must close a genuinely new mathematical or scientific gap. Natural directions include an explicitly drift-aware target, unknown-range or mixing-process concentration with declared assumptions, or a different observable witness not already implied by P92-P94. The physical-to-experiential bridge remains open.'''
    text = text[: after_match.start()] + after + text[after_match.end() :]
    write(path, text)


def promote_reproducibility() -> None:
    path = "docs/reproducibility.md"
    text = read(path)
    text = text.replace("Run only the current P93 theorem checks | focused P93 commands below", "Run only the current P94 theorem checks | focused P94 commands below", 1)
    text = text.replace("The current public theorem frontier is **P93**.", "The current public theorem frontier is **P94**.", 1)
    pattern = re.compile(r"## 5\. Focused audit of the current P93 frontier\n.*?(?=\n---\n\n## 6\.)", re.DOTALL)
    match = pattern.search(text)
    if match is None:
        raise RuntimeError("reproducibility focused P93 section missing")
    section = r'''## 5. Focused audit of the current P94 frontier

The current theorem frontier is **P94**.

Its direct technical record is:

```text
docs/proposition_94_finite_range_dependent_sign_coherence.md
docs/p94_equation_provenance.md
src/consciousness_bridge/finite_range_dependent_sign_coherence.py
src/consciousness_bridge/finite_range_dependent_sign_coherence_threshold.py
tests/test_finite_range_dependent_sign_coherence.py
docs/figures/p94_finite_range_dependent_sign_coherence.svg
figures/manifest.json
```

Run the focused theorem and publication checks with:

```bash
python -m pytest -q \
  tests/test_finite_range_dependent_sign_coherence.py \
  tests/test_frontier_reader_narrative.py \
  tests/test_figure_publication_sync.py \
  tests/test_frontier_publication_consistency.py
python scripts/sync_figure_publication.py --check
python scripts/verify_repository.py
```

P94 extends P93 from IID observations to a declared `m`-dependent sequence sharing one common marginal four-view law. Its seven-cell radius is

\[
\varepsilon^{(m)}_{n,7}(\alpha)
=
\sqrt{\frac{(m+1)\log(14/\alpha)}{2n}}.
\]

For the established `1/24` limiting sign radius at 95 percent confidence, exact rational certification gives crossings `1623`, `3246`, and `4869` for `m=0,1,2`. The first exact denominator-24 replications are `1632`, `3264`, and `4872`.

The exact temporal-pooling no-go certificate is also part of P94. It shows that two individually valid interior P75 regimes can pool to determinants `(-65/65536, 11/65536, 3/65536)` with negative product. P94 therefore does not treat arbitrary temporal drift as finite-range dependence.

Non-rejection remains inconclusive. P94 does not identify the latent state with consciousness, establish nonphysicality, validate an alternative ontology, or close the physical-to-experiential bridge.
'''
    text = text[: match.start()] + section + text[match.end() :]
    write(path, text)


def promote_reader_html() -> None:
    homepage = read("website/index.html")
    homepage = homepage.replace("Current record:</strong> 93 proposition-level results through P93", "Current record:</strong> 94 proposition-level results through P94")
    homepage = homepage.replace("The 93 results form several dependency branches.", "The 94 results form several dependency branches.")
    homepage = homepage.replace("The 93-result program", "The 94-result program")
    homepage = homepage.replace("all 93 propositions", "all 94 propositions")
    p94_home = '''<!-- current-frontier-home: P94 -->
<section id="p94-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head">
    <p class="eyebrow">Research II · Current theorem frontier · P94</p>
    <h2>Finite-range dependent sign-coherence rejection</h2>
    <p>P94 extends the P93 seven-cell rejection witness from IID observations to a declared <strong>m-dependent</strong> stream with one common marginal four-view law. The squared confidence radius acquires the exact factor <strong>m+1</strong>.</p>
  </div>
  <div class="theorem-figure-shell"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p94_finite_range_dependent_sign_coherence.svg"><img loading="eager" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p94_finite_range_dependent_sign_coherence.svg" alt="P94 finite-range dependent sign-coherence rejection certificate" /></a></div>
  <div class="frontier-summary-grid">
    <article class="frontier-summary-card"><h3>Dependence-adjusted confidence event</h3><p><strong>eps^2 = (m+1) log(14/alpha)/(2n)</strong> for the same seven observable cells used by P92 and P93.</p></article>
    <article class="frontier-summary-card"><h3>Exact 95 percent crossings</h3><p><strong>1623</strong> for m=0, <strong>3246</strong> for m=1, and <strong>4869</strong> for m=2; exact profile replications are 1632, 3264, and 4872.</p></article>
    <article class="frontier-summary-card"><h3>Exact drift no-go</h3><p>Two individually valid interior P75 regimes can pool to determinant signs <strong>(-,+,+)</strong>. Arbitrary temporal drift is therefore outside P94.</p></article>
  </div>
  <div class="boundary"><p><strong>Scientific boundary:</strong> P94 is conditional on a declared finite dependence range and one common marginal law. Non-rejection remains inconclusive. It does not establish drift robustness, identify consciousness, or close the physical-to-experiential bridge.</p></div>
  <p><a href="research-map.html">Research II map</a> · <a href="visual-atlas.html">Theorem figures</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_94_finite_range_dependent_sign_coherence.md">proposition_94_finite_range_dependent_sign_coherence.md</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p94_equation_provenance.md">p94_equation_provenance.md</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/finite_range_dependent_sign_coherence.py">finite_range_dependent_sign_coherence.py</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_finite_range_dependent_sign_coherence.py">test_finite_range_dependent_sign_coherence.py</a></p>
</section>'''
    homepage = replace_section(homepage, "p93-frontier", p94_home)
    write("website/index.html", homepage)

    atlas = read("website/visual-atlas.html")
    match = re.search(r'<!-- current-frontier-visual: P93 -->\s*(<section(?=[^>]*id="p93-frontier")[^>]*>.*?</section>)', atlas, re.DOTALL)
    if match is None:
        raise RuntimeError("Visual Atlas P93 current block missing")
    p93 = match.group(1)
    p93 = p93.replace("current-frontier-visual", "", 1)
    p93 = p93.replace("Current theorem frontier · P93", "Previous theorem frontier · P93", 1)
    p94 = '''<!-- current-frontier-visual: P94 -->
<section id="p94-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head"><p class="eyebrow">Current theorem frontier · P94</p><h2>Finite-range dependent sign-coherence rejection</h2><p>P94 extends P93 to a declared m-dependent stream with one common marginal law. The squared seven-cell radius is multiplied by m+1, while an exact pooling counterexample shows why arbitrary marginal drift remains outside the theorem.</p></div>
  <div class="theorem-figure-shell"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p94_finite_range_dependent_sign_coherence.svg" alt="P94 finite-range dependent sign-coherence rejection certificate" /></div>
  <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_94_finite_range_dependent_sign_coherence.md">proposition_94_finite_range_dependent_sign_coherence.md</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p94_equation_provenance.md">p94_equation_provenance.md</a></p>
</section>'''
    atlas = atlas[: match.start()] + p94 + "\n\n" + p93 + atlas[match.end() :]
    write("website/visual-atlas.html", atlas)

    for path in ("website/plain-language.html", "website/start-here.html"):
        text = read(path)
        text = text.replace("93 results · current frontier P93", "94 results · current frontier P94")
        text = text.replace("Open all 93 Research II results", "Open all 94 Research II results")
        text = text.replace("The 93 Research II propositions by scientific role", "The 94 Research II propositions by scientific role")
        text = text.replace("This is the 93-result Research II theorem program currently reaching P93.", "This is the 94-result Research II theorem program currently reaching P94.")
        text = text.replace("The current theorem frontier is P93.", "The current theorem frontier is P94.")
        old_match = re.search(r'<section class="boundary" id="p93-reader-frontier">.*?</section>', text, re.DOTALL)
        if old_match is None:
            raise RuntimeError(f"{path}: P93 reader block missing")
        p93 = old_match.group(0).replace("Research II · Current frontier · P93", "Research II · Historical IID frontier · P93", 1)
        p94 = '''<section class="boundary" id="p94-reader-frontier"><div class="section-head"><p class="eyebrow">Research II · Current frontier · P94</p><h2>Short-range temporal dependence can be certified without pretending drift is harmless</h2><p>P94 keeps the seven-cell P92/P93 sign witness and replaces IID concentration by a declared m-dependent model with one common marginal law. The squared radius pays an exact factor m+1. A separate exact counterexample shows that pooling drifting P75 regimes can manufacture the negative determinant-product pattern, so temporal drift is not silently absorbed into the theorem.</p><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_94_finite_range_dependent_sign_coherence.md">Read P94 theorem</a></p></div></section>'''
        text = text[: old_match.start()] + p94 + "\n\n" + p93 + text[old_match.end() :]
        write(path, text)

    research = read("website/research-map.html")
    research = research.replace("Ninety-three results, one dependency-aware scientific program", "Ninety-four results, one dependency-aware scientific program")
    research = research.replace("Current Research II model-audit range: P75-P93.", "Current Research II model-audit range: P75-P94.")
    research = research.replace("The current theorem frontier is P93.", "The current theorem frontier is P94.")
    p93_match = re.search(r'<section id="p93-research-map"[^>]*>.*?</section>', research, re.DOTALL)
    if p93_match is None:
        raise RuntimeError("research map P93 block missing")
    p93 = p93_match.group(0).replace("P93 · Localized finite-sample nonlinear rejection", "P93 · Historical IID finite-sample nonlinear rejection", 1)
    p94 = '''<section id="p94-research-map" class="theorem-frontier">
  <div class="section-head"><p class="eyebrow">P94 · Finite-range dependent nonlinear rejection</p><h2>P94: Can the P92/P93 sign obstruction survive short-range temporal dependence?</h2></div>
  <p><strong>Yes, conditionally.</strong> If all observations share one marginal four-view law and dependence vanishes beyond a declared range m, residue classes modulo m+1 yield the concentration bound needed to preserve the seven selected cells.</p>
  <p><strong>Exact radius:</strong> eps^2 = (m+1) log(14/alpha)/(2n). At 95 percent confidence the established 1/24 witness crosses at 1623, 3246, and 4869 for m=0,1,2.</p>
  <p><strong>Drift boundary:</strong> two individually valid interior P75 regimes can pool to determinants (-65/65536, 11/65536, 3/65536), whose product is negative. P94 therefore does not certify arbitrary marginal drift.</p>
  <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_94_finite_range_dependent_sign_coherence.md">Read P94 theorem</a> · <a href="visual-atlas.html">See the P94 figure</a></p>
</section>'''
    research = research[: p93_match.start()] + p94 + "\n\n" + p93 + research[p93_match.end() :]
    write("website/research-map.html", research)

    lineage = read("website/research-lineage.html")
    lineage = lineage.replace('<strong>93</strong><span>proposition-level results</span>', '<strong>94</strong><span>proposition-level results</span>')
    lineage = lineage.replace('<strong>P93</strong><span>current theorem frontier</span>', '<strong>P94</strong><span>current theorem frontier</span>')
    write("website/research-lineage.html", lineage)

    sources = read("website/sources.html")
    if 'id="p94-source"' not in sources:
        block = '''\n<section id="p94-source"><div class="section-head"><p class="eyebrow">Current Research II theorem source · P94</p><h2>Finite-range dependent sign-coherence rejection</h2></div><div class="result-grid"><article class="result"><h3>Formal record</h3><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_94_finite_range_dependent_sign_coherence.md">Proof</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p94_equation_provenance.md">provenance</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/finite_range_dependent_sign_coherence.py">implementation</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_finite_range_dependent_sign_coherence.py">tests</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p94_finite_range_dependent_sign_coherence.svg">figure</a></p></article><article class="result"><h3>Scientific boundary</h3><p>Conditional on a declared finite dependence range and one common marginal law. The exact pooling no-go shows that arbitrary temporal drift is a separate inferential problem. Non-rejection remains inconclusive.</p></article></div></section>\n'''
        sources = sources.replace("</main>", block + "</main>", 1)
    write("website/sources.html", sources)


def promote_records() -> None:
    detailed = read("docs/detailed_proposition_record.md")
    if "## Proposition 94" not in detailed:
        detailed += '''\n\n## Proposition 94: Finite-Range Dependent Sign-Coherence Rejection\n\n- Proof: `docs/proposition_94_finite_range_dependent_sign_coherence.md`\n- Provenance: `docs/p94_equation_provenance.md`\n- Implementation: `src/consciousness_bridge/finite_range_dependent_sign_coherence.py`\n- Exact thresholds: `src/consciousness_bridge/finite_range_dependent_sign_coherence_threshold.py`\n- Tests: `tests/test_finite_range_dependent_sign_coherence.py`\n- Figure: `docs/figures/p94_finite_range_dependent_sign_coherence.svg`\n\nP94 replaces P93's IID sampling assumption by a declared finite-range dependent sequence with one common marginal law. It also contains an exact temporal-pooling no-go showing that arbitrary drift can imitate the P92 sign rejection pattern.\n'''
    write("docs/detailed_proposition_record.md", detailed)

    eq = read("docs/equation_and_citation_map.md")
    if "Proposition 94" not in eq:
        eq += '''\n\n### P94 finite-range dependent sign-coherence rejection\n\n- Theorem: [Proposition 94](proposition_94_finite_range_dependent_sign_coherence.md)\n- Equation provenance: [P94 equation record](p94_equation_provenance.md)\n- Implementation: [`finite_range_dependent_sign_coherence.py`](../src/consciousness_bridge/finite_range_dependent_sign_coherence.py)\n- Exact thresholds: [`finite_range_dependent_sign_coherence_threshold.py`](../src/consciousness_bridge/finite_range_dependent_sign_coherence_threshold.py)\n- Regression tests: [`test_finite_range_dependent_sign_coherence.py`](../tests/test_finite_range_dependent_sign_coherence.py)\n'''
    write("docs/equation_and_citation_map.md", eq)

    matrix = read("docs/claim_source_matrix.md")
    if "P94 finite-range dependent rejection" not in matrix:
        matrix += '''\n| P94 finite-range dependent rejection | Under one common marginal law and declared m-dependence, the P92/P93 seven-cell rejection gate has squared radius `(m+1) log(14/alpha)/(2n)`; arbitrary temporal pooling is not covered | repository theorem with established concentration ingredients | [P94 proof](proposition_94_finite_range_dependent_sign_coherence.md), [P94 provenance](p94_equation_provenance.md), exact tests |\n'''
    write("docs/claim_source_matrix.md", matrix)

    glossary = read("docs/glossary.md")
    if "## Current theorem frontier: P94" not in glossary:
        glossary += '''\n\n## Current theorem frontier: P94\n\n**Finite-range dependence:** observations may depend across nearby time indices but sigma-fields separated by more than a declared range `m` are independent. P94 uses residue classes modulo `m+1` to recover independent groups.\n\n**Common marginal law:** every observation has the same four-view population law. P94 requires this because an exact counterexample shows that pooling different valid P75 regimes can create a negative P92 determinant product.\n'''
    write("docs/glossary.md", glossary)

    changelog = read("CHANGELOG.md")
    if "Unreleased research frontier - P94" not in changelog:
        changelog = '''# Unreleased research frontier - P94\n\n- Added Proposition 94, Finite-Range Dependent Sign-Coherence Rejection.\n- Extended P93 from IID observations to a declared m-dependent sequence with one common marginal four-view law.\n- Derived the seven-cell radius `sqrt((m+1) log(14/alpha)/(2n))` by residue-class coloring, Holder, and Hoeffding concentration.\n- Kept the executable rejection direction exact by comparing squared radii using P79 rational logarithm brackets.\n- Certified 95 percent witness crossings 1623, 3246, and 4869 for dependence ranges 0, 1, and 2, with first exact 24-count replications 1632, 3264, and 4872.\n- Added an exact temporal-pooling no-go certificate: two individually valid interior P75 regimes can pool to a law with negative P92 determinant product.\n- Preserved the scientific boundary that non-rejection is inconclusive and the physical-to-experiential bridge remains open.\n- Kept formal release v0.82.0 separate from the advancing theorem frontier.\n\n''' + changelog
    write("CHANGELOG.md", changelog)


def promote_tests() -> None:
    p93 = '''from pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\n\n\ndef _read(path: str) -> str:\n    return (ROOT / path).read_text(encoding="utf-8")\n\n\ndef test_p93_proof_states_localized_rejection_and_boundary() -> None:\n    text = _read("docs/proposition_93_localized_sign_coherence_rejection.md")\n    lower = text.lower()\n    assert "seven" in lower\n    assert "1623" in text\n    assert "1632" in text\n    assert "non-rejection remains inconclusive" in lower\n    assert "physical-to-experiential bridge remains open" in lower\n\n\ndef test_p93_is_preserved_as_historical_iid_frontier() -> None:\n    atlas = _read("website/visual-atlas.html")\n    assert 'id="p93-frontier"' in atlas\n    assert "Previous theorem frontier · P93" in atlas\n    assert "p93_localized_sign_coherence_rejection.svg" in atlas\n    assert atlas.index('id="p94-frontier"') < atlas.index('id="p93-frontier"')\n\n\ndef test_p93_reader_surfaces_remain_linked_as_history() -> None:\n    plain = _read("website/plain-language.html")\n    start = _read("website/start-here.html")\n    assert 'id="p93-reader-frontier"' in plain\n    assert "P93" in start\n    assert "P93" in plain\n\n\ndef test_permanent_publication_workflows_are_read_only() -> None:\n    for path in (\n        ".github/workflows/figures.yml",\n        ".github/workflows/reproducibility.yml",\n        ".github/workflows/validate-research-three-website.yml",\n    ):\n        text = _read(path)\n        assert "contents: read" in text\n        assert "contents: write" not in text\n        assert "git push" not in text\n'''
    write("tests/test_p93_reader_surface_coherence.py", p93)

    p94 = '''from pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\n\n\ndef _read(path: str) -> str:\n    return (ROOT / path).read_text(encoding="utf-8")\n\n\ndef test_p94_formal_record_is_complete() -> None:\n    proof = _read("docs/proposition_94_finite_range_dependent_sign_coherence.md")\n    assert "common marginal" in proof.lower()\n    assert "3246" in proof and "4869" in proof\n    assert "-\\frac{2145}{281474976710656}" in proof\n    assert "physical-to-experiential bridge" in proof.lower()\n    for path in (\n        "docs/p94_equation_provenance.md",\n        "docs/figures/p94_finite_range_dependent_sign_coherence.svg",\n        "src/consciousness_bridge/finite_range_dependent_sign_coherence.py",\n        "src/consciousness_bridge/finite_range_dependent_sign_coherence_threshold.py",\n        "tests/test_finite_range_dependent_sign_coherence.py",\n    ):\n        assert (ROOT / path).is_file()\n\n\ndef test_p94_is_current_reader_frontier() -> None:\n    home = _read("website/index.html")\n    atlas = _read("website/visual-atlas.html")\n    plain = _read("website/plain-language.html")\n    start = _read("website/start-here.html")\n    research = _read("website/research-map.html")\n    assert 'id="p94-frontier"' in home\n    assert "Current theorem frontier · P94" in home\n    assert atlas.index('id="p94-frontier"') < atlas.index('id="p93-frontier"')\n    assert "Previous theorem frontier · P93" in atlas\n    assert 'id="p94-reader-frontier"' in plain\n    assert 'id="p94-reader-frontier"' in start\n    assert 'id="p94-research-map"' in research\n    assert "94 results · current frontier P94" in plain\n    assert "94 results · current frontier P94" in start\n\n\ndef test_p94_drift_boundary_is_visible_to_readers() -> None:\n    for path in (\n        "README.md",\n        "website/index.html",\n        "website/plain-language.html",\n        "website/start-here.html",\n        "website/research-map.html",\n    ):\n        text = _read(path).lower()\n        assert "p94" in text\n        assert "drift" in text\n        assert "physical-to-experiential bridge" in text\n'''
    write("tests/test_p94_reader_surface_coherence.py", p94)

    orientation = read("tests/test_website_research_orientation.py")
    orientation = orientation.replace("p93 = text.index('id=\"p93-research-map\"')", "p94 = text.index('id=\"p94-research-map\"')\n    p93 = text.index('id=\"p93-research-map\"')")
    orientation = orientation.replace("assert text.count('id=\"p93-research-map\"') == 1", "assert text.count('id=\"p94-research-map\"') == 1\n    assert text.count('id=\"p93-research-map\"') == 1")
    orientation = orientation.replace("assert main_open < p90 < p91 < p93 < p92 < main_close", "assert main_open < p90 < p91 < p94 < p93 < p92 < main_close")
    write("tests/test_website_research_orientation.py", orientation)

    publication = read("tests/test_publication_contract_v2.py")
    publication = publication.replace('assert "P93" in research_map', 'assert "P94" in research_map')
    publication = publication.replace('assert \'id="p93-research-map"\' in research_map', 'assert \'id="p94-research-map"\' in research_map')
    publication = publication.replace('assert "current frontier P93" in plain', 'assert "current frontier P94" in plain')
    write("tests/test_publication_contract_v2.py", publication)


def main() -> None:
    require("scripts/verify_repository.py", 'CURRENT_FRONTIER = "P93"')
    require("website/index.html", '<!-- current-frontier-home: P93 -->')
    require("website/visual-atlas.html", '<!-- current-frontier-visual: P93 -->')
    promote_proof()
    write_figure()
    promote_verifier()
    promote_syncer()
    promote_prepare_website()
    promote_readme()
    promote_citations()
    promote_navigation()
    promote_roadmap()
    promote_reproducibility()
    promote_reader_html()
    promote_records()
    promote_tests()
    print("[P94] source publication migration applied; regenerate figures next")


if __name__ == "__main__":
    main()
