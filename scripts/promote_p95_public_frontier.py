"""Promote canonical reader and publication surfaces from P94 to P95.

P95 is the drift-aware stratified continuation of P94. The promoter keeps P94
as the historical pooling no-go and finite-range predecessor while making P95
the current theorem frontier. It is deliberately deterministic and idempotent
so generated figure/publication surfaces can be rebuilt from one canonical
promotion step.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURE = "p95_drift_aware_stratified_sign_coherence.svg"
PROOF = "proposition_95_drift_aware_stratified_sign_coherence.md"
PROVENANCE = "p95_equation_provenance.md"
SOURCE = "drift_aware_stratified_sign_coherence.py"
TEST = "test_drift_aware_stratified_sign_coherence.py"


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


def insert_before_once(text: str, marker: str, block: str, *, guard: str) -> str:
    if guard in text:
        return text
    if marker not in text:
        raise RuntimeError(f"promotion marker not found: {marker}")
    return text.replace(marker, block.rstrip() + "\n\n" + marker, 1)


def write_figure() -> None:
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="900" viewBox="0 0 1440 900" role="img" aria-labelledby="title desc">
<title id="title">P95 Drift-Aware Stratified Sign-Coherence Rejection</title>
<desc id="desc">What this figure shows: P95 responds to the P94 temporal-pooling no-go by replacing one pooled stationary target with a family of predeclared regime-specific P75 tests. Each regime may have its own marginal law, sample size, dependence range, and exact error budget. A union bound controls all local P94 confidence events without requiring independence between regimes. How to read it: move from the P94 pooling warning on the left, through predeclared regime-specific laws in the center, to the familywise rejection rule on the right. The lower strip gives the balanced two-regime one-dependent 95 percent checkpoint. Main takeaway: drift across regimes is allowed, but stationarity is still required locally inside each declared regime. Scientific status: conditional statistical model-audit theorem. It does not validate data-dependent segmentation, prove model acceptance after non-rejection, identify consciousness, establish nonphysicality, or close the physical-to-experiential bridge.</desc>
<rect width="1440" height="900" fill="#ffffff"/>
<text x="70" y="65" font-family="Arial, Helvetica, sans-serif" font-size="36" font-weight="700" fill="#111827">P95 - Drift-Aware Stratified Sign-Coherence Rejection</text>
<text x="70" y="105" font-family="Arial, Helvetica, sans-serif" font-size="20" fill="#475569">Do not pool drifting P75 regimes. Test predeclared regimes locally and control the familywise error exactly.</text>

<rect x="60" y="155" width="400" height="515" rx="22" fill="#fff7ed" stroke="#f97316" stroke-width="2"/>
<text x="92" y="205" font-family="Arial, Helvetica, sans-serif" font-size="24" font-weight="700" fill="#111827">1. P94 pooling no-go</text>
<text x="92" y="250" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#475569">Two valid time-specific P75 laws can have</text>
<text x="92" y="282" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#475569">a pooled law with the forbidden sign pattern.</text>
<rect x="95" y="325" width="330" height="95" rx="15" fill="#ffffff" stroke="#fb923c"/>
<text x="260" y="362" text-anchor="middle" font-family="Georgia, serif" font-size="20" fill="#111827">Regime 1: D1 D2 D3 &gt; 0</text>
<text x="260" y="397" text-anchor="middle" font-family="Georgia, serif" font-size="20" fill="#111827">Regime 2: D1 D2 D3 &gt; 0</text>
<text x="92" y="470" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#c2410c">Pooled signs: (-,+,+)</text>
<text x="92" y="510" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#475569">Conclusion: the pooled marginal is not a valid</text>
<text x="92" y="540" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#475569">stationary target when the process drifts.</text>
<text x="92" y="610" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#9a3412">DO NOT POOL</text>

<rect x="520" y="155" width="400" height="515" rx="22" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
<text x="552" y="205" font-family="Arial, Helvetica, sans-serif" font-size="24" font-weight="700" fill="#111827">2. Predeclared regimes</text>
<text x="552" y="250" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#475569">For b = 1,...,B declare before testing:</text>
<text x="552" y="300" font-family="Georgia, serif" font-size="21" fill="#111827">P_b, n_b, m_b, alpha_b</text>
<text x="552" y="350" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#475569">Local assumption: one common marginal P_b</text>
<text x="552" y="380" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#475569">inside regime b and m_b-dependent sampling.</text>
<text x="552" y="435" font-family="Georgia, serif" font-size="20" fill="#111827">sum_b alpha_b &lt;= alpha</text>
<text x="552" y="490" font-family="Georgia, serif" font-size="19" fill="#111827">eps_b^2 = (m_b+1) log(14/alpha_b)/(2 n_b)</text>
<text x="552" y="545" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#475569">Different regimes may have different marginals.</text>
<text x="552" y="575" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#475569">No cross-regime independence is required.</text>
<text x="552" y="625" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#1d4ed8">Boundaries and error budgets must be predeclared.</text>

<rect x="980" y="155" width="400" height="515" rx="22" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
<text x="1012" y="205" font-family="Arial, Helvetica, sans-serif" font-size="24" font-weight="700" fill="#111827">3. Familywise rejection</text>
<text x="1012" y="250" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#475569">Joint null:</text>
<text x="1012" y="292" font-family="Georgia, serif" font-size="20" fill="#111827">H0: P_b in M75 for every b</text>
<text x="1012" y="348" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#475569">If one regime has</text>
<text x="1012" y="390" font-family="Georgia, serif" font-size="19" fill="#111827">D1 D2 D3 &lt; 0</text>
<text x="1012" y="425" font-family="Georgia, serif" font-size="19" fill="#111827">and eps_b &lt; min_i r_bi</text>
<text x="1012" y="480" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#475569">then that regime is outside P75 and</text>
<text x="1012" y="510" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#475569">the all-regimes joint null is rejected.</text>
<text x="1012" y="565" font-family="Georgia, serif" font-size="20" fill="#166534">confidence &gt;= 1 - sum_b alpha_b</text>
<text x="1012" y="615" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#166534">Union bound only: regime events may be dependent.</text>

<rect x="60" y="715" width="1320" height="120" rx="22" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
<text x="90" y="755" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#111827">Balanced 95 percent checkpoint</text>
<text x="90" y="795" font-family="Georgia, serif" font-size="21" fill="#111827">B = 2, m = 1, alpha_b = 0.025: mathematical crossing n = 3645 per regime; first exact 24-count replication n = 3648.</text>
<text x="90" y="824" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#64748b">Boundary: P95 handles predeclared regime drift, not data-selected change points or unrestricted gradual drift. The physical-to-experiential bridge remains open.</text>
</svg>'''
    write(f"docs/figures/{FIGURE}", svg + "\n")


def promote_verifier() -> None:
    path = "scripts/verify_repository.py"
    text = read(path).replace('CURRENT_FRONTIER = "P94"', 'CURRENT_FRONTIER = "P95"')
    marker = '    "tests/test_finite_range_dependent_sign_coherence.py",\n'
    addition = (
        marker
        + f'    "docs/{PROOF}",\n'
        + f'    "docs/{PROVENANCE}",\n'
        + f'    "docs/figures/{FIGURE}",\n'
        + f'    "src/consciousness_bridge/{SOURCE}",\n'
        + f'    "tests/{TEST}",\n'
    )
    if f'    "docs/{PROOF}",' not in text:
        if marker not in text:
            raise RuntimeError("P94 verifier marker missing")
        text = text.replace(marker, addition, 1)
    write(path, text)


def promote_figure_sync() -> None:
    path = "scripts/sync_figure_publication.py"
    text = read(path)
    if "if frontier == 95:" not in text:
        marker = "    return []\n\n\ndef _frontier_page"
        block = '''    if frontier == 95:
        return [
            "### Exact P95 drift-aware stratified sign-coherence rejection",
            "",
            "P95 responds to the P94 temporal-pooling no-go by testing predeclared regimes separately and controlling the complete family with one explicit error budget.",
            "",
            "```text",
            "local radius: eps_b^2 = (m_b+1) log(14/alpha_b) / (2 n_b)",
            "familywise condition: sum_b alpha_b <= alpha",
            "joint null: P_b belongs to M_75 for every declared regime b",
            "B=2, m=1, 95% familywise crossing = 3645 per regime",
            "first exact denominator-24 replication = 3648 per regime",
            "```",
            "",
            "P95 permits arbitrary marginal changes between predeclared regimes and requires only local common-marginal finite-range assumptions. It does not validate data-dependent segmentation, unrestricted gradual drift, model acceptance, or any consciousness ontology.",
            "",
        ]
    return []


def _frontier_page'''
        if marker not in text:
            raise RuntimeError("frontier summary insertion marker missing")
        text = text.replace(marker, block, 1)
    write(path, text)


def promote_readme() -> None:
    path = "README.md"
    text = read(path)
    text = replace_many(text, (
        ("The current public theorem frontier is **P94**.", "The current public theorem frontier is **P95**."),
        ("docs/proposition_94_finite_range_dependent_sign_coherence.md", f"docs/{PROOF}"),
        ("**Public theorem frontier:** P94", "**Public theorem frontier:** P95"),
    ))
    block = f'''### Current theorem frontier

![P95 Drift-Aware Stratified Sign-Coherence Rejection](docs/figures/{FIGURE})

**Figure 2. P95 drift-aware stratified sign-coherence rejection.** P94 proved that pooling time-varying P75 marginals can manufacture the same negative three-minor sign pattern used for rejection. P95 therefore changes the target instead of pretending the pooled stream is stationary. The stream is split into predeclared regimes; each regime receives its own P94 finite-range certificate and exact error budget. A union bound then controls the complete family without requiring independence between regimes. At 95 percent familywise confidence, two equally budgeted one-dependent regimes cross the established P92 witness threshold at 3645 observations per regime, with the first exact denominator-24 replication at 3648.

P95 permits arbitrary marginal changes between predeclared regimes, but it still requires one common marginal law inside each regime and predeclared boundaries. It does not validate data-dependent segmentation, prove P75 after non-rejection, identify consciousness, establish nonphysicality, or close the physical-to-experiential bridge.

'''
    text = re.sub(r"### Current theorem frontier\n.*?(?=## Choose your path)", block, text, flags=re.DOTALL)
    write(path, text)


def promote_citations() -> None:
    path = "CITATION.cff"
    text = read(path)
    sentence = (
        " Proposition 95 repairs the P94 temporal-pooling failure for predeclared regimes: "
        "regime-specific finite-range P94 certificates receive exact error budgets, and a familywise union bound rejects the joint null that every regime-specific marginal belongs to P75 without requiring independence between regimes."
    )
    if "Proposition 95 repairs" not in text:
        text = text.replace(" Current documented theorem frontier: P94.", sentence + " Current documented theorem frontier: P95.", 1)
    text = text.replace("Current documented theorem frontier: P94.", "Current documented theorem frontier: P95.")
    write(path, text)

    path = "CITATION.bib"
    write(path, read(path).replace("Current documented theorem frontier: P94.", "Current documented theorem frontier: P95."))

    path = "CITATION.md"
    text = read(path)
    text = text.replace("## Current theorem frontier: P94", "## Previous theorem frontier: P94", 1)
    text = text.replace("The current documented theorem frontier is **P94**.", "P94 is the immediate finite-range predecessor to the current frontier.", 1)
    text = append_once(text, "## Current theorem frontier: P95", f'''## Current theorem frontier: P95

The current documented theorem frontier is **P95**. The formal package release remains **Version 0.82.0**.

P95 is the drift-aware stratified continuation of P94. It permits different marginal four-view laws across predeclared regimes, applies the P94 finite-range certificate inside each regime, and controls the complete family by exact error-budget allocation and a union bound. No independence between regime confidence events is required.

For the established P92 witness, two equally budgeted one-dependent regimes at 95 percent familywise confidence have a first mathematical crossing at `3645` observations per regime and a first exact denominator-24 replication at `3648`.

- Proof: [`{PROOF}`](docs/{PROOF})
- Equation provenance: [`{PROVENANCE}`](docs/{PROVENANCE})
- Implementation: [`{SOURCE}`](src/consciousness_bridge/{SOURCE})
- Tests: [`{TEST}`](tests/{TEST})
- Figure: [`{FIGURE}`](docs/figures/{FIGURE})

P95 is a conditional model-audit theorem. It does not validate data-dependent segmentation, establish P75 under non-rejection, identify consciousness, establish nonphysicality, or close the physical-to-experiential bridge.''')
    write(path, text)


def promote_start_here_markdown() -> None:
    path = "START_HERE.md"
    text = read(path)
    text = replace_many(text, (
        ("The public theorem frontier is **P94**.", "The public theorem frontier is **P95**."),
        ("[P94](docs/proposition_94_finite_range_dependent_sign_coherence.md)", f"[P95](docs/{PROOF})"),
        ("through P94", "through P95"),
    ))
    text = append_once(text, "### P95: drift-aware stratified rejection", f'''### P95: drift-aware stratified rejection

P94 showed why drifting marginals cannot be pooled safely. P95 makes the next valid move: declare regimes before testing, permit a different marginal law in every regime, certify each regime with its own P94 radius and error budget, and reject the all-regimes P75 null if any regime is locally incompatible. [Read P95](docs/{PROOF}).''')
    write(path, text)


def promote_docs() -> None:
    path = "docs/detailed_proposition_record.md"
    text = read(path)
    text = replace_many(text, (("P1-P94", "P1-P95"), ("P1 through P94", "P1 through P95")))
    text = append_once(text, "## Proposition 95: Drift-Aware Stratified Sign-Coherence Rejection", f'''## Proposition 95: Drift-Aware Stratified Sign-Coherence Rejection

P95 responds directly to the P94 temporal-pooling no-go. The observation stream is partitioned into predeclared regimes, and each regime may have its own marginal four-view law, sample size, finite dependence range, and exact error budget. P94 is applied locally. A union bound then gives simultaneous familywise validity without requiring independence between regimes. If any regime has a certified negative P92 determinant product, the joint null that every regime-specific marginal belongs to P75 is rejected. For two equally budgeted one-dependent regimes at 95 percent familywise confidence, the established witness crosses at 3645 observations per regime and first clears on an exact 24-count replication at 3648.

- [Proof]({PROOF})
- [Equation provenance]({PROVENANCE})
- Implementation: `../src/consciousness_bridge/{SOURCE}`
- Tests: `../tests/{TEST}`
- Figure: `figures/{FIGURE}`

P95 requires predeclared regimes and local common-marginal assumptions. Data-dependent segmentation and unrestricted gradual drift remain open.''')
    write(path, text)

    path = "docs/research_navigation.md"
    text = read(path)
    text = text.replace("The current documented theorem frontier is **P94**.", "The current documented theorem frontier is **P95**.", 1)
    text = text.replace("## P94 current frontier", "## P94 immediate predecessor", 1)
    text = append_once(text, "## P95 current frontier", f'''## P95 current frontier

**Current frontier:** [P95: Drift-Aware Stratified Sign-Coherence Rejection]({PROOF})

| What you want | Direct link |
| --- | --- |
| The theorem and proof | [P95 proposition]({PROOF}) |
| Equation and method provenance | [P95 provenance]({PROVENANCE}) |
| Implementation | [`{SOURCE}`](../src/consciousness_bridge/{SOURCE}) |
| Regression tests | [`{TEST}`](../tests/{TEST}) |
| Figure | [P95 drift-aware stratified certificate](figures/{FIGURE}) |

P95 permits marginal drift across predeclared regimes while keeping a common marginal law only within each regime. It replaces invalid pooling with a familywise statement about the regime-specific P75 laws.''')
    write(path, text)

    path = "docs/theorem_roadmap.md"
    text = read(path)
    text = replace_many(text, (
        ("The current documented theorem frontier is **P94**.", "The current documented theorem frontier is **P95**."),
        ("P1 through P94 with explicit dependency branches", "P1 through P95 with explicit dependency branches"),
        ("P71-P94 return", "P71-P95 return"),
    ))
    row94 = "| [P94](proposition_94_finite_range_dependent_sign_coherence.md)"
    if "| [P95](proposition_95_drift_aware_stratified_sign_coherence.md)" not in text and row94 in text:
        lines = text.splitlines()
        for index, line in enumerate(lines):
            if line.startswith(row94):
                lines.insert(index + 1, "| [P95](proposition_95_drift_aware_stratified_sign_coherence.md) | predeclared drift regimes, local P94 gates, familywise error allocation | drift-aware rejection of the all-regimes P75 null | proved conditional statistical theorem |")
                break
        text = "\n".join(lines) + ("\n" if read(path).endswith("\n") else "")
    text = append_once(text, "### P95: drift-aware stratified continuation", '''### P95: drift-aware stratified continuation

P94 proves both a finite-range dependent rejection theorem under one common marginal law and an exact counterexample to arbitrary temporal pooling. P95 takes the non-pooling route. It declares regimes before testing, permits a different marginal P75 candidate in every regime, and uses local P94 certificates plus a familywise union bound. This preserves falsifiability under regime-level drift without pretending the pooled law is stationary.

The next open directions are data-dependent segmentation with valid selection accounting, gradual drift inside a regime, and broader dependence classes.''')
    write(path, text)

    path = "docs/reproducibility.md"
    text = read(path)
    text = text.replace("## 5. Focused audit of the current P94 frontier", "## 5. Focused audit of the current P95 frontier")
    text = text.replace("The current theorem frontier is **P94**.", "The current theorem frontier is **P95**.", 1)
    text = append_once(text, f"docs/{PROOF}", f'''P95 direct technical record:

```text
docs/{PROOF}
docs/{PROVENANCE}
docs/figures/{FIGURE}
src/consciousness_bridge/{SOURCE}
tests/{TEST}
```

Focused check:

```bash
python -m pytest -q tests/{TEST}
```''')
    write(path, text)

    path = "docs/research_map.md"
    text = read(path)
    text = text.replace("The public theorem frontier is **P94**", "The public theorem frontier is **P95**", 1)
    text = text.replace("If you want the current result itself, open **[P94](proposition_94_finite_range_dependent_sign_coherence.md)**.", f"If you want the current result itself, open **[P95]({PROOF})**. For the finite-range single-marginal predecessor, open **[P94](proposition_94_finite_range_dependent_sign_coherence.md)**.", 1)
    text = append_once(text, "### P95: What if the marginal law drifts across predeclared regimes?", f'''### P95: What if the marginal law drifts across predeclared regimes?

P95 does not pool those regimes. It gives each predeclared regime its own marginal law, finite-range dependence assumption, sample size, and error budget. Local P94 certificates are then combined by a familywise union bound. If any regime is certified outside P75, the all-regimes P75 null is rejected at the declared familywise confidence. [Read P95]({PROOF}).''')
    write(path, text)

    path = "docs/glossary.md"
    text = read(path).replace("P94 is the current documented theorem frontier", "P95 is the current documented theorem frontier")
    write(path, text)

    for path in ("docs/claim_source_matrix.md", "docs/equation_and_citation_map.md"):
        text = read(path)
        text = append_once(text, "P95 drift-aware stratified", f'''\nP95 drift-aware stratified sign-coherence rejection: predeclared regime-specific P94 confidence events with exact error allocation are combined by a familywise union bound. The theorem permits marginal drift across regimes but not data-dependent segmentation without additional selection accounting. Formal record: [{PROOF}]({PROOF}) and [{PROVENANCE}]({PROVENANCE}).''')
        write(path, text)


def p95_home_section() -> str:
    return f'''<!-- current-frontier-home: P95 -->
<section id="p95-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head">
    <p class="eyebrow">Research II · Current theorem frontier · P95</p>
    <h2>Drift-aware stratified sign-coherence rejection</h2>
    <p>P95 responds to the P94 pooling no-go by testing <strong>predeclared regimes separately</strong>. Marginal laws may change between regimes; each regime receives its own finite-range P94 certificate and exact error budget.</p>
  </div>
  <div class="theorem-figure-shell"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/{FIGURE}"><img loading="eager" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/{FIGURE}" alt="P95 drift-aware stratified sign-coherence rejection certificate" /></a></div>
  <div class="frontier-summary-grid">
    <article class="frontier-summary-card"><h3>Drift is allowed across regimes</h3><p>Each predeclared regime may have its own marginal four-view law, sample size, dependence range, and error budget.</p></article>
    <article class="frontier-summary-card"><h3>Familywise confidence</h3><p>If <strong>sum alpha_b &lt;= alpha</strong>, all local P94 confidence events hold simultaneously with probability at least <strong>1-alpha</strong>, with no cross-regime independence assumption.</p></article>
    <article class="frontier-summary-card"><h3>Exact balanced checkpoint</h3><p>At 95 percent familywise confidence with two regimes and m=1, the mathematical crossing is <strong>3645 per regime</strong>; the first exact 24-count replication is <strong>3648</strong>.</p></article>
  </div>
  <div class="boundary"><p><strong>Scientific boundary:</strong> regime boundaries and error budgets must be predeclared. P95 does not validate data-selected change points, unrestricted gradual drift, model acceptance, consciousness identification, or a completed physical-to-experiential bridge.</p></div>
  <p><a href="research-map.html">Research II map</a> · <a href="visual-atlas.html">Theorem figures</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF}">{PROOF}</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROVENANCE}">{PROVENANCE}</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/{SOURCE}">{SOURCE}</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/{TEST}">{TEST}</a></p>
</section>'''


def promote_homepage() -> None:
    path = "website/index.html"
    text = read(path)
    text = replace_many(text, (
        ("<strong>94</strong><span>proposition-level results</span>", "<strong>95</strong><span>proposition-level results</span>"),
        ("P94 current theorem frontier · v0.82.0", "P95 current theorem frontier · v0.82.0"),
        ("Explore all 94 results", "Explore all 95 results"),
        ("94 proposition-level results through P94", "95 proposition-level results through P95"),
        ("The 94 results form", "The 95 results form"),
        ("The 94-result program", "The 95-result program"),
        ("all 94 propositions", "all 95 propositions"),
    ))
    pattern = re.compile(r"<!-- current-frontier-home: P93 -->.*?<section id=\"research-iii-overview\">", re.DOTALL)
    replacement = p95_home_section() + "\n\n<section id=\"research-iii-overview\">"
    if 'id="p95-frontier"' not in text:
        text, count = pattern.subn(replacement, text, count=1)
        if count != 1:
            raise RuntimeError("homepage P94 frontier block not found")
    write(path, text)


def reader_block() -> str:
    return f'''<section class="boundary" id="p95-reader-frontier"><div class="section-head"><p class="eyebrow">Research II · Current frontier · P95</p><h2>Drift is handled by testing predeclared regimes instead of pooling them</h2><p>P94 showed that pooling changing marginal laws can create a false qualitative sign-coherence rejection. P95 keeps the P94 finite-range certificate inside each predeclared regime, permits different marginals across regimes, and controls the full set of regime tests with one explicit familywise error budget. With two equally budgeted one-dependent regimes at 95 percent familywise confidence, the established witness crosses at 3645 observations per regime and first clears on an exact replication at 3648.</p><p><strong>Boundary:</strong> data-dependent segmentation and unrestricted gradual drift require additional theory. Non-rejection does not establish P75, and the physical-to-experiential bridge remains open.</p><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF}">Read P95 theorem</a></p></div></section>'''


def promote_plain_and_start() -> None:
    for path in ("website/plain-language.html", "website/start-here.html"):
        text = read(path)
        text = replace_many(text, (
            ("94 results · current frontier P94", "95 results · current frontier P95"),
            ("94-result Research II theorem program currently reaching P94", "95-result Research II theorem program currently reaching P95"),
            ("A 93-result sufficiency and falsification architecture", "A 95-result sufficiency and falsification architecture"),
            ("currently through P93", "currently through P95"),
            ("The 94 Research II propositions by scientific role", "The 95 Research II propositions by scientific role"),
        ))
        marker = '<section class="boundary" id="p94-reader-frontier">'
        text = insert_before_once(text, marker, reader_block(), guard='id="p95-reader-frontier"')
        text = text.replace("Research II · Current frontier · P94", "Research II · Immediate predecessor · P94", 1)
        write(path, text)


def promote_research_map_html() -> None:
    path = "website/research-map.html"
    text = read(path)
    text = replace_many(text, (
        ("<strong>94</strong><span>proposition-level results</span>", "<strong>95</strong><span>proposition-level results</span>"),
        ("<strong>P94</strong><span>current theorem frontier</span>", "<strong>P95</strong><span>current theorem frontier</span>"),
        ("The current theorem frontier is P94.", "The current theorem frontier is P95."),
    ))
    block = f'''<section class="result" id="p95-research-map"><span>P95</span><h3>P95: How can the sign-coherence test remain valid when the marginal law changes across known regimes?</h3><p>P95 tests predeclared regimes separately instead of pooling them. Each regime gets its own P94 finite-range certificate and exact error budget. A union bound controls the complete family without assuming regime independence. Any locally certified P92 sign violation rejects the joint null that every regime-specific marginal belongs to P75.</p><p><strong>Exact balanced checkpoint:</strong> B=2, m=1 gives a 95 percent familywise crossing at 3645 observations per regime and first exact denominator-24 replication at 3648.</p><p><strong>Boundary:</strong> regime boundaries must be predeclared; data-selected segmentation and gradual within-regime drift remain open.</p><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF}">Read P95 theorem</a></p></section>'''
    text = insert_before_once(text, "</main>", block, guard='id="p95-research-map"')
    write(path, text)


def promote_research_lineage() -> None:
    path = "website/research-lineage.html"
    text = read(path)
    text = replace_many(text, (
        ("<strong>94</strong><span>proposition-level results</span>", "<strong>95</strong><span>proposition-level results</span>"),
        ("<strong>P94</strong><span>current theorem frontier</span>", "<strong>P95</strong><span>current theorem frontier</span>"),
        ("through P94", "through P95"),
    ))
    write(path, text)


def p95_atlas_section() -> str:
    return f'''<section id="p95-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head"><p class="eyebrow">Current theorem frontier · P95</p><h2>Drift-aware stratified sign-coherence rejection</h2><p>P95 repairs the P94 pooling failure by treating predeclared temporal regimes as separate population targets. Each regime gets a local finite-range confidence gate and exact error budget, while a union bound provides familywise validity without assuming the regime events are independent.</p></div>
  <div class="theorem-figure-shell"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/{FIGURE}"><img loading="eager" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/{FIGURE}" alt="P95 drift-aware stratified sign-coherence rejection" /></a></div>
  <p><strong>Exact checkpoint:</strong> B=2, m=1, 95 percent familywise confidence gives crossing 3645 and first exact replication 3648 per regime.</p>
  <p><strong>Scientific boundary:</strong> predeclared regimes only. Data-dependent segmentation, unrestricted gradual drift, model acceptance, and consciousness ontology are outside the theorem.</p>
  <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF}">Proof</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROVENANCE}">Equation provenance</a></p>
</section>'''


def promote_visual_atlas() -> None:
    path = "website/visual-atlas.html"
    text = read(path)
    marker = '<section id="p94-frontier"'
    text = insert_before_once(text, marker, p95_atlas_section(), guard='id="p95-frontier"')
    text = text.replace("Current theorem frontier · P94", "Previous theorem frontier · P94", 1)
    write(path, text)


def promote_p94_reader_test() -> None:
    path = "tests/test_p94_reader_surface_coherence.py"
    text = read(path)
    text = text.replace("def test_p94_is_current_reader_frontier() -> None:", "def test_p94_remains_visible_as_immediate_predecessor() -> None:")
    old = '''    assert 'id="p94-frontier"' in home
    assert "Current theorem frontier · P94" in home
    assert atlas.index('id="p94-frontier"') < atlas.index('id="p93-frontier"')
    assert "Previous theorem frontier · P93" in atlas
    assert 'id="p94-reader-frontier"' in plain
    assert 'id="p94-reader-frontier"' in start
    assert 'id="p94-research-map"' in research
    assert "94 results · current frontier P94" in plain
    assert "94 results · current frontier P94" in start
'''
    new = '''    assert 'id="p94-frontier"' not in home
    assert atlas.index('id="p95-frontier"') < atlas.index('id="p94-frontier"')
    assert "Previous theorem frontier · P94" in atlas
    assert 'id="p94-reader-frontier"' in plain
    assert 'id="p94-reader-frontier"' in start
    assert 'id="p94-research-map"' in research
    assert "95 results · current frontier P95" in plain
    assert "95 results · current frontier P95" in start
'''
    if old in text:
        text = text.replace(old, new)
    write(path, text)


def write_p95_reader_test() -> None:
    path = "tests/test_p95_reader_surface_coherence.py"
    if (ROOT / path).is_file():
        return
    write(path, '''from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p95_formal_record_is_complete() -> None:
    proof = _read("docs/proposition_95_drift_aware_stratified_sign_coherence.md")
    assert "predeclared" in proof.lower()
    assert "3645" in proof and "3648" in proof
    assert "familywise" in proof.lower()
    for path in (
        "docs/p95_equation_provenance.md",
        "docs/figures/p95_drift_aware_stratified_sign_coherence.svg",
        "src/consciousness_bridge/drift_aware_stratified_sign_coherence.py",
        "tests/test_drift_aware_stratified_sign_coherence.py",
    ):
        assert (ROOT / path).is_file()


def test_p95_is_current_reader_frontier() -> None:
    home = _read("website/index.html")
    atlas = _read("website/visual-atlas.html")
    plain = _read("website/plain-language.html")
    start = _read("website/start-here.html")
    research = _read("website/research-map.html")
    assert 'id="p95-frontier"' in home
    assert "Current theorem frontier · P95" in home
    assert atlas.index('id="p95-frontier"') < atlas.index('id="p94-frontier"')
    assert "Previous theorem frontier · P94" in atlas
    assert 'id="p95-reader-frontier"' in plain
    assert 'id="p95-reader-frontier"' in start
    assert 'id="p95-research-map"' in research
    assert "95 results · current frontier P95" in plain
    assert "95 results · current frontier P95" in start


def test_p95_scientific_boundary_is_visible() -> None:
    for path in (
        "README.md",
        "website/index.html",
        "website/plain-language.html",
        "website/start-here.html",
        "website/research-map.html",
    ):
        text = _read(path).lower()
        assert "p95" in text
        assert "predeclared" in text
        assert "physical-to-experiential bridge" in text
''')


def promote_changelog() -> None:
    path = "CHANGELOG.md"
    text = read(path)
    block = '''## P95 drift-aware stratified sign-coherence frontier

- Added Proposition 95 as the drift-aware continuation of the P94 temporal-pooling no-go.
- Replaced invalid pooled-stationary inference with predeclared regime-specific P94 gates and exact familywise error allocation.
- Permitted arbitrary marginal changes between regimes, different within-regime dependence ranges, and dependent regime confidence events.
- Certified the balanced B=2, m=1 95 percent crossing at 3645 observations per regime and first exact denominator-24 replication at 3648.
- Preserved the scientific boundary: data-dependent segmentation and unrestricted gradual drift remain open, non-rejection is inconclusive, and the physical-to-experiential bridge remains open.
- Kept formal release v0.82.0 separate from the advancing theorem frontier.
'''
    if "## P95 drift-aware stratified sign-coherence frontier" not in text:
        text = block + "\n" + text
    write(path, text)


def main() -> None:
    write_figure()
    promote_verifier()
    promote_figure_sync()
    promote_readme()
    promote_citations()
    promote_start_here_markdown()
    promote_docs()
    promote_homepage()
    promote_plain_and_start()
    promote_research_map_html()
    promote_research_lineage()
    promote_visual_atlas()
    promote_p94_reader_test()
    write_p95_reader_test()
    promote_changelog()
    print("[p95] promoted canonical reader and publication sources to P95")


if __name__ == "__main__":
    main()
