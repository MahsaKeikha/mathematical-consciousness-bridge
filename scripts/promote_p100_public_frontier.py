"""Promote P100 across the public theorem-frontier publication contract.

This is an idempotent repository migration helper. It keeps the formal package
release at v0.82.0 while advancing the documented theorem frontier from P99 to
P100, preserves P99 as the immediate historical predecessor, synchronizes the
figure gateway, and installs reader-surface regression guards for P100.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def write(relative: str, text: str) -> None:
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def replace_required(text: str, old: str, new: str, *, label: str) -> str:
    if old in text:
        return text.replace(old, new)
    if new in text:
        return text
    raise RuntimeError(f"{label}: expected text not found: {old!r}")


def replace_once_required(text: str, old: str, new: str, *, label: str) -> str:
    if old in text:
        return text.replace(old, new, 1)
    if new in text:
        return text
    raise RuntimeError(f"{label}: expected text not found: {old!r}")


def regex_replace_once(text: str, pattern: str, replacement: str, *, label: str) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
    if count == 1:
        return updated
    if replacement in text:
        return text
    raise RuntimeError(f"{label}: regex did not match")


def insert_before_once(text: str, marker: str, addition: str, *, label: str) -> str:
    if addition.strip() in text:
        return text
    if marker not in text:
        raise RuntimeError(f"{label}: insertion marker not found")
    return text.replace(marker, addition + marker, 1)


def append_once(text: str, marker: str, addition: str) -> str:
    if marker in text:
        return text
    return text.rstrip() + "\n\n" + addition.strip() + "\n"


P100_HOME = '''<!-- current-frontier-home: P100 -->
<section id="p100-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head">
    <p class="eyebrow">Research II · Current theorem frontier · P100</p>
    <h2>Anytime-valid sequential e-process</h2>
    <p>P100 composes fresh, conditionally valid P99 certification rounds with predictable reserve stakes into one nonnegative supermartingale, so evidence can be inspected after every round and stopped at the first valid threshold crossing.</p>
  </div>
  <div class="theorem-figure-shell"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p100_anytime_sequential_eprocess.svg"><img loading="eager" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p100_anytime_sequential_eprocess.svg" alt="P100 anytime-valid sequential e-process" /></a></div>
  <div class="frontier-summary-grid">
    <article class="frontier-summary-card"><h3>Predictable reserve stake</h3><p>Before current certification data are inspected, choose eta_t from past information only and set F_t = (1 - eta_t) + eta_t E_t.</p></article>
    <article class="frontier-summary-card"><h3>Anytime-valid crossing</h3><p>The product M_t is a nonnegative supermartingale. Ville's inequality controls the probability of ever crossing 1 / alpha.</p></article>
    <article class="frontier-summary-card"><h3>Exact two-round checkpoint</h3><p>With E_t = <strong>25 / 2</strong> and eta_t = <strong>1 / 2</strong>, each factor is <strong>27 / 4</strong> and M_2 = <strong>729 / 16 = 45.5625</strong> &gt; 20. The declared unique-data totals are <strong>30192 / 30336</strong>.</p></article>
  </div>
  <div class="boundary"><p><strong>Scientific boundary:</strong> current-round planning, calibration, and stake selection must be frozen from past information, and current certification data must remain conditionally valid given that past. P100 does not validate reused-data relabeling, current-round leakage, model acceptance, consciousness identification, nonphysicality, or completion of the physical-to-experiential bridge.</p></div>
  <p><a href="research-map.html">Research II map</a> · <a href="visual-atlas.html">Theorem figures</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_100_anytime_sequential_eprocess.md">P100 theorem</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p100_equation_provenance.md">P100 provenance</a></p>
</section>'''

P100_ATLAS = '''<!-- current-frontier-visual: P100 -->
<section id="p100-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head"><p class="eyebrow">Current theorem frontier · P100</p><h2>Anytime-valid sequential e-process</h2><p>P100 carries P99 evidence across fresh certification rounds. Predictable reserve stakes form factors F_t = (1 - eta_t) + eta_t E_t, and their product is monitored with an anytime-valid threshold.</p></div>
  <div class="theorem-figure-shell"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p100_anytime_sequential_eprocess.svg"><img loading="eager" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p100_anytime_sequential_eprocess.svg" alt="P100 anytime-valid sequential e-process" /></a></div>
  <div class="frontier-summary-grid"><article class="frontier-summary-card"><h3>Fresh conditional validity</h3><p>Each current P99 round must retain null expectation at most one after conditioning on the accumulated past.</p></article><article class="frontier-summary-card"><h3>Repeated inspection is protected</h3><p>Ville's inequality controls the event that the nonnegative supermartingale ever reaches 1 / alpha.</p></article><article class="frontier-summary-card"><h3>729 / 16</h3><p>Two moderate half-staked rounds cross the 95 percent threshold even though each P99 round e-value is only 25 / 2.</p></article></div>
  <div class="boundary"><p><strong>Boundary:</strong> the current plan, calibration, and stake must be predictable from past information, and current certification data must remain conditionally fresh. Reusing certification observations or leaking current outcomes into current choices invalidates this contract.</p></div>
  <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_100_anytime_sequential_eprocess.md">Read Proposition 100</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p100_equation_provenance.md">P100 equation provenance</a></p>
</section>

'''

P100_READER = '''<section class="boundary" id="p100-reader-frontier"><div class="section-head"><p class="eyebrow">Research II · Current frontier · P100</p><h2>Fresh certification rounds can now accumulate evidence under repeated inspection</h2><p>P100 takes each fresh P99 round e-value E_t and combines it with a predictable reserve stake eta_t through F_t = (1 - eta_t) + eta_t E_t. The product M_t is a nonnegative supermartingale, so Ville's inequality protects the first crossing of 1 / alpha even when the stopping time depends on the observed history.</p><p><strong>Exact P100 checkpoint:</strong> a moderate P99 round has E_t = <strong>25 / 2</strong>, below the 95 percent threshold 20. With eta_t = <strong>1 / 2</strong>, the factor is <strong>27 / 4</strong>. Two fresh rounds give M_2 = <strong>729 / 16 = 45.5625</strong>, so the first crossing occurs at round two. The declared two-round unique-data totals are <strong>30192 / 30336</strong>.</p><p>The reserve matters: if E_t = 0 at eta_t = 1 / 2, the process is multiplied by 1 / 2 rather than destroyed. The current plan, calibration, and stake must be frozen from past information, and current certification data must remain conditionally valid given that past.</p><p>P100 does not make reused data fresh, does not permit current-round leakage, and does not establish model acceptance, consciousness identification, nonphysicality, or completion of the physical-to-experiential bridge.</p><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_100_anytime_sequential_eprocess.md">Read P100</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p100_equation_provenance.md">Audit P100 provenance</a></p></div></section>

'''

P100_RESEARCH_RESULT = '''<section class="result" id="p100-research-map"><span>P100</span><h3>P100: Can fresh P99 rounds accumulate evidence with anytime-valid stopping?</h3><p>Yes, under a sequential conditional-validity contract. If E_t is the current fresh P99 e-value and eta_t is chosen from past information only, then F_t = (1 - eta_t) + eta_t E_t has conditional expectation at most one. The product M_t is therefore a nonnegative supermartingale, and Ville's inequality controls the probability of ever crossing 1 / alpha.</p><p>The exact 95 percent checkpoint uses E_t = 25 / 2 and eta_t = 1 / 2, so F_t = 27 / 4. One round remains below 20, while two fresh rounds give M_2 = 729 / 16 = 45.5625 &gt; 20. The declared two-round unique-data totals are 30192 / 30336.</p><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_100_anytime_sequential_eprocess.md">Open P100</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p100_equation_provenance.md">P100 provenance</a></p></section>

'''


def patch_theorem_notation() -> None:
    path = "docs/proposition_100_anytime_sequential_eprocess.md"
    text = read(path)
    text = text.replace(
        "At the end of round `t-1`, the analyst may use `F_{t-1}` to choose the next round's:",
        "At the end of round `t-1`, the analyst may use the information in `mathcal F_{t-1}` to choose the next round's:",
    )
    text = text.replace(
        "Since `M_{t-1}` is nonnegative and `F_{t-1}`-measurable,",
        "Since `M_{t-1}` is nonnegative and `mathcal F_{t-1}`-measurable,",
    )
    write(path, text)


def patch_verifier() -> None:
    path = "scripts/verify_repository.py"
    text = read(path)
    text = replace_required(text, 'CURRENT_FRONTIER = "P99"', 'CURRENT_FRONTIER = "P100"', label=path)
    core_anchor = '    "tests/test_p99_reader_surface_coherence.py",\n'
    core_add = (
        core_anchor
        + '    "docs/proposition_100_anytime_sequential_eprocess.md",\n'
        + '    "docs/p100_equation_provenance.md",\n'
        + '    "docs/figures/p100_anytime_sequential_eprocess.svg",\n'
        + '    "src/consciousness_bridge/anytime_sequential_eprocess.py",\n'
        + '    "tests/test_anytime_sequential_eprocess.py",\n'
        + '    "tests/test_p100_reader_surface_coherence.py",\n'
    )
    if '"docs/proposition_100_anytime_sequential_eprocess.md"' not in text:
        text = replace_once_required(text, core_anchor, core_add, label=path)
    stale_add = (
        '    "Current theorem frontier · P99",\n'
        '    "current P99 frontier",\n'
        '    "<strong>P99</strong><span>current theorem frontier</span>",\n'
        '    "99 results · current frontier P99",\n'
        '    "Explore all 99 results",\n'
    )
    if '"99 results · current frontier P99"' not in text.split("STALE_READER_FRONTIER_MARKERS = (", 1)[1].split(")", 1)[0]:
        text = text.replace("STALE_READER_FRONTIER_MARKERS = (\n", "STALE_READER_FRONTIER_MARKERS = (\n" + stale_add, 1)
    write(path, text)


def patch_figure_sync() -> None:
    path = "scripts/sync_figure_publication.py"
    text = read(path)
    if "if frontier == 100:" not in text:
        summary = '''    if frontier == 100:\n        return [\n            "",\n            "P100 composes fresh, conditionally valid P99 certification rounds into an anytime-valid sequential e-process with predictable reserve stakes.",\n            "",\n            "At the exact 95 percent checkpoint, one moderate round has E_t = 25/2 and half stake gives F_t = 27/4. Two fresh rounds give M_2 = 729/16 = 45.5625 > 20, with declared unique-data totals 30192 / 30336.",\n            "",\n            "P100 uses standard supermartingale and Ville inequality machinery. Its repository-specific contribution is the exact integration with the P92-P99 certification chain and explicit guards against current-round leakage and non-fresh certification data.",\n        ]\n'''
        text = text.replace("    if frontier == 99:\n", summary + "    if frontier == 99:\n", 1)
    write(path, text)


def patch_readme() -> None:
    path = "README.md"
    text = read(path)
    text = text.replace(
        "Historical selection-valid lineage: P96 introduced independent holdout certification after data-dependent plan selection; P97, P98, and P99 extend that line through finite candidate families, cross-fitting, and e-value aggregation.",
        "Historical selection-valid lineage: P96 introduced independent holdout certification after data-dependent plan selection; P97, P98, and P99 extend that line through finite candidate families, cross-fitting, and e-value aggregation. P100 adds the outer anytime-valid sequential layer across fresh certification rounds.",
    )
    text = text.replace("The current public theorem frontier is **P99**.", "The current public theorem frontier is **P100**.")
    text = text.replace("[Read the current frontier](docs/proposition_99_cross_fitted_evalue_aggregation.md)", "[Read the current frontier](docs/proposition_100_anytime_sequential_eprocess.md)")
    pattern = r"### Current theorem frontier\n\n.*?(?=### Immediate predecessor:)"
    current = '''### Current theorem frontier

![P100 Anytime-Valid Sequential E-Process](docs/figures/p100_anytime_sequential_eprocess.svg)

**Figure 2. P100 anytime-valid sequential e-process.** P100 takes the selection-valid P99 e-value from each fresh certification round and forms the predictable reserve factor `F_t = (1 - eta_t) + eta_t E_t`. Under the sequential null, the conditional expectation of each factor is at most one, so the product `M_t` is a nonnegative supermartingale and Ville's inequality makes the first crossing of `1 / alpha` anytime-valid.

At the exact 95 percent checkpoint, a moderate P99 round has `E_t = 25/2 = 12.5`, below the single-round threshold 20. With `eta_t = 1/2`, the factor is `27/4 = 6.75`. Two fresh rounds produce `M_2 = 729/16 = 45.5625 > 20`. The inherited mathematical crossing is 3774 observations per regime, exact denominator-24 replication is 3792, one round uses 15096 / 15168 unique observations, and the two-round crossing uses **30192 / 30336**.

P100 uses standard e-process, supermartingale, predictable-stake, and Ville-inequality machinery. The repository-specific result is the exact integration with P92-P99, explicit current-round predictability and freshness guards, exact-rational bookkeeping, and the reproducible two-round crossing. It does not validate reused-data relabeling, current-round leakage, model acceptance, consciousness identification, nonphysicality, or completion of the physical-to-experiential bridge.

'''
    text = regex_replace_once(text, pattern, current, label=path)
    text = text.replace("### Immediate predecessor: P97", "### Immediate predecessor: P99")
    text = text.replace("[P97: Simultaneous Finite Candidate-Family Selection](docs/proposition_97_simultaneous_candidate_family_selection.md) remains the immediate same-data selection predecessor to P98. P97 permits post-inspection choice only within a finite candidate family fixed before certification statistics are inspected and pays for that search through explicit multiplicity. P98 takes a different route by rotating genuinely independent certification blocks while enforcing own-fold exclusion.", "[P99: Cross-Fitted E-Value Aggregation](docs/proposition_99_cross_fitted_evalue_aggregation.md) is the immediate fixed-round evidence predecessor to P100. P99 aggregates valid cross-fitted evidence within one certification round; P100 adds the outer sequential layer across fresh rounds.")
    text = text.replace("**Public theorem frontier:** P99", "**Public theorem frontier:** P100")
    write(path, text)


def patch_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    text = text.replace("The current documented theorem frontier is **P99**.", "The current documented theorem frontier is **P100**.")
    text = text.replace("P1 through P99 with explicit dependency branches", "P1 through P100 with explicit dependency branches")
    text = text.replace("P71-P99 return to the core P19", "P71-P100 return to the core P19")
    dep = "&\\text{P99: exact e-value aggregation accumulates distributed cross-fitted evidence without fold independence}\\\\\n"
    if "P100: predictable reserve stakes" not in text:
        text = text.replace(dep, dep + "&\\Downarrow\\\\\n&\\text{P100: predictable reserve stakes turn fresh P99 rounds into an anytime-valid sequential e-process}\\\\\n", 1)
    old_after = r"## After P99\n.*\Z"
    p100_tail = '''## P100: anytime-valid sequential e-process

P100 closes the fixed-round boundary left open by P99. Let `E_t` be the P99 e-value from the current certification round, and require conditional validity given the accumulated past:

\\[
\\mathbb E[E_t\\mid\\mathcal F_{t-1}]\\le1.
\\]

Choose an exact-rational stake `eta_t` from past information only and define

\\[
F_t=(1-\\eta_t)+\\eta_tE_t,
\\qquad
M_t=\\prod_{s=1}^{t}F_s.
\\]

Then `M_t` is a nonnegative supermartingale. Ville's inequality yields

\\[
\\Pr\\left(\\sup_t M_t\\ge1/\\alpha\\right)\\le\\alpha,
\\]

so the process may be inspected after every round and stopped at the first threshold crossing. Cross-round mutual independence is not the theorem's requirement; the essential requirement is current-round conditional e-value validity given the past, together with the inherited P99 within-round certification contract.

At the exact 95 percent checkpoint, one moderate P99 round has `E_t = 25/2`. With half stake, `F_t = 27/4`; two fresh rounds give `M_2 = 729/16 = 45.5625 > 20`. The two-round unique-data accounting is 30192 at the mathematical crossing and 30336 at the first exact denominator-24 replication.

- Proof: [P100](proposition_100_anytime_sequential_eprocess.md)
- Provenance: [p100_equation_provenance.md](p100_equation_provenance.md)
- Figure: [P100 anytime-valid sequential e-process](figures/p100_anytime_sequential_eprocess.svg)
- Source: [`anytime_sequential_eprocess.py`](../src/consciousness_bridge/anytime_sequential_eprocess.py)
- Tests: [`test_anytime_sequential_eprocess.py`](../tests/test_anytime_sequential_eprocess.py)

P100 does not make reused observations fresh, permit current-round leakage, validate misspecified conditional null laws, establish model acceptance after non-rejection, identify a latent state with consciousness, establish nonphysicality, or close the physical-to-experiential bridge.

## After P100

P100 completes the planned P1-P100 theorem sequence for this publication cycle. The next priority is consolidation rather than proposition-number expansion: integrate the dependency chain, exact finite-data checkpoints, selection-validity hierarchy, and anytime-valid P100 capstone into the publication manuscript and preprint. Any later theorem extension should close a newly identified scientific or inferential gap rather than continue numbering for its own sake. The physical-to-experiential bridge remains open.
'''
    if "## P100: anytime-valid sequential e-process" not in text:
        text, count = re.subn(old_after, p100_tail, text, count=1, flags=re.S)
        if count != 1:
            raise RuntimeError(f"{path}: failed to replace After P99 tail")
    write(path, text)


def patch_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    text = text.replace("The current documented theorem frontier is **P99**.", "The current documented theorem frontier is **P100**.")
    text = text.replace("**Results:** P75 through P99", "**Results:** P75 through P100")
    if "**Current frontier:** [P100:" not in text:
        marker = "**Start with:** [P75: Target Model Adequacy](proposition_75_target_model_adequacy_overidentification.md)\n"
        addition = "\n**Current frontier:** [P100: Anytime-Valid Sequential E-Process](proposition_100_anytime_sequential_eprocess.md)\n\n**Immediate predecessor:** [P99: Cross-Fitted E-Value Aggregation](proposition_99_cross_fitted_evalue_aggregation.md)\n"
        text = text.replace(marker, marker + addition, 1)
    audit = '''For P100:

| Audit surface | Canonical route |
| --- | --- |
| Direct theorem | [P100 proposition](proposition_100_anytime_sequential_eprocess.md) |
| Equation and method provenance | [P100 provenance](p100_equation_provenance.md) |
| Implementation | [`anytime_sequential_eprocess.py`](../src/consciousness_bridge/anytime_sequential_eprocess.py) |
| Regression tests | [`test_anytime_sequential_eprocess.py`](../tests/test_anytime_sequential_eprocess.py) |
| Theorem figure | [P100 anytime-valid sequential e-process](figures/p100_anytime_sequential_eprocess.svg) |
| Repository reproduction | [Reproducibility Guide](reproducibility.md) |

P100 is a conditional anytime-valid sequential model-audit result. Current-round plan, calibration, and stake choices must be predictable from past information only, and current certification data must preserve conditional P99 validity given that past. Reused-data relabeling and current-round leakage are not covered.

'''
    text = insert_before_once(text, "For P99:\n", audit, label=path)
    text = text.replace("the full 99 proposition index", "the full 100 proposition index")
    write(path, text)


def patch_reproducibility() -> None:
    path = "docs/reproducibility.md"
    text = read(path)
    text = text.replace("The current public theorem frontier is **P99**.", "The current public theorem frontier is **P100**.")
    pattern = r"## 5\. Focused audit of the current P99 frontier\n.*?(?=\n---\n\n## 6\.)"
    section = '''## 5. Focused audit of the current P100 frontier

The current theorem frontier is **P100**.

Its direct technical record is:

```text
docs/proposition_100_anytime_sequential_eprocess.md
docs/p100_equation_provenance.md
src/consciousness_bridge/anytime_sequential_eprocess.py
tests/test_anytime_sequential_eprocess.py
docs/figures/p100_anytime_sequential_eprocess.svg
figures/manifest.json
```

Run the focused theorem and publication checks with:

```bash
python -m pytest -q \\
  tests/test_anytime_sequential_eprocess.py \\
  tests/test_p100_reader_surface_coherence.py \\
  tests/test_p99_reader_surface_coherence.py \\
  tests/test_figure_publication_sync.py \\
  tests/test_frontier_publication_consistency.py
python scripts/sync_figure_publication.py --check
python scripts/verify_repository.py
```

P100 composes fresh P99 round e-values with predictable reserve stakes. Under the declared sequential null, each current round remains conditionally valid given the past, the cumulative product is a nonnegative supermartingale, and Ville's inequality protects repeated inspection and adaptive stopping.

For the exact 95 percent checkpoint, a moderate round has `E_t = 25/2`, half stake gives `F_t = 27/4`, and two fresh rounds give `M_2 = 729/16 = 45.5625 > 20`. The inherited per-regime crossings are `3774 / 3792`; the two-round unique-data totals are `30192 / 30336`.

P100 does not make reused certification data fresh, permit current-round leakage, establish model acceptance, identify consciousness, establish nonphysicality, or complete the physical-to-experiential bridge.
'''
    text = regex_replace_once(text, pattern, section, label=path)
    write(path, text)


def patch_citations() -> None:
    path = "CITATION.md"
    text = read(path)
    text = text.replace("## Current theorem frontier: P99", "## Current theorem frontier: P100")
    text = text.replace("The current documented theorem frontier is **P99**.", "The current documented theorem frontier is **P100**.")
    text = append_once(text, "P100 anytime-valid sequential e-process", '''### P100 anytime-valid sequential e-process

The P100 capstone composes fresh selection-valid P99 e-values with predictable reserve stakes into a nonnegative supermartingale. Its standard sequential ingredients are sourced to Ville and modern e-process/time-uniform inference literature; the repository-specific contribution is the exact integration with the P92-P99 certification chain, explicit current-round predictability/freshness guards, and the exact `729/16` two-round crossing.
''')
    write(path, text)

    path = "CITATION.cff"
    text = read(path)
    text = text.replace("  - cross-fitted selection-valid certification\n", "  - cross-fitted selection-valid certification\n  - e-value aggregation\n  - anytime-valid sequential inference\n  - e-processes\n")
    text = text.replace("Proposition 99 adds cross-fitted e-value aggregation for distributed evidence while preserving exact finite-sample and selection-valid guard conditions. Current documented theorem frontier: P99.", "Proposition 99 adds cross-fitted e-value aggregation for distributed evidence while preserving exact finite-sample and selection-valid guard conditions. Proposition 100 composes fresh, conditionally valid P99 certification rounds with predictable reserve stakes into a nonnegative supermartingale and uses Ville's inequality for anytime-valid repeated inspection and adaptive stopping; its exact checkpoint has two half-staked moderate rounds crossing at 729/16 with declared two-round unique-data totals 30192 / 30336. Current documented theorem frontier: P100.")
    text = text.replace("Current documented theorem frontier: P99.", "Current documented theorem frontier: P100.")
    write(path, text)

    for path in ("CITATION.bib", "references.bib"):
        text = read(path)
        additions = '''@article{howard2021timeuniform,
  author = {Howard, Steven R. and Ramdas, Aaditya and McAuliffe, Jon and Sekhon, Jasjeet},
  title = {Time-uniform, nonparametric, nonasymptotic confidence sequences},
  journal = {The Annals of Statistics},
  year = {2021},
  volume = {49},
  number = {2},
  pages = {1055--1080},
  doi = {10.1214/20-AOS1991}
}

@book{ville1939etude,
  author = {Ville, Jean},
  title = {Etude critique de la notion de collectif},
  year = {1939},
  publisher = {Gauthier-Villars},
  address = {Paris}
}
'''
        if "howard2021timeuniform" not in text:
            text = text.rstrip() + "\n\n" + additions
        write(path, text)


def patch_documentation_records() -> None:
    entries = {
        "docs/detailed_proposition_record.md": '''## P100: Anytime-Valid Sequential E-Process

**Question.** Can several fresh P99 certification rounds accumulate evidence over time while preserving type-I control under repeated inspection and a data-dependent stopping time?

**Result.** Yes, when the current P99 e-value remains conditionally valid given the past and the current stake is predictable. With `F_t = (1 - eta_t) + eta_t E_t` and `M_t = product_{s <= t} F_s`, the process is a nonnegative supermartingale. Ville's inequality gives `P(sup_t M_t >= 1/alpha) <= alpha`. At the exact 95 percent checkpoint, `E_t = 25/2`, `eta_t = 1/2`, `F_t = 27/4`, and two fresh rounds give `M_2 = 729/16 > 20`, with declared unique-data totals `30192 / 30336`.

Direct proof: [P100](proposition_100_anytime_sequential_eprocess.md). Provenance: [P100 equation record](p100_equation_provenance.md). Implementation: [`anytime_sequential_eprocess.py`](../src/consciousness_bridge/anytime_sequential_eprocess.py). Tests: [`test_anytime_sequential_eprocess.py`](../tests/test_anytime_sequential_eprocess.py).
''',
        "docs/equation_and_citation_map.md": '''## P100: anytime-valid sequential e-process

| Equation or method | Scientific role | Provenance |
| --- | --- | --- |
| `E[E_t | F_(t-1)] <= 1` | Conditional round e-value validity | Inherited from P99 under the declared fresh-round conditional contract |
| `F_t = (1 - eta_t) + eta_t E_t` | Predictable reserve-stake factor | Standard betting/e-process construction; P100 exact-rational implementation |
| `M_t = product_{s <= t} F_s` | Nonnegative supermartingale evidence process | Standard sequential evidence machinery |
| `P(sup_t M_t >= 1/alpha) <= alpha` | Anytime-valid crossing control | Ville (1939); modern time-uniform inference context in Howard et al. (2021) |
| `25/2 -> 27/4 -> 729/16` | Exact two-round repository checkpoint | Repository-original integration and exact arithmetic |

Full boundary and source record: [P100 equation provenance](p100_equation_provenance.md).
''',
        "docs/claim_source_matrix.md": '''## P100 source boundary

| Claim | Class | Source / audit route |
| --- | --- | --- |
| Nonnegative supermartingale + Ville crossing control | Standard sequential probability | Ville (1939); Howard et al. (2021) |
| E-value calibration/composition context | Standard e-value theory | Vovk and Wang (2021) |
| P99-to-P100 exact conditional integration and `729/16` checkpoint | Repository-original theorem/computation | [P100 theorem](proposition_100_anytime_sequential_eprocess.md), [provenance](p100_equation_provenance.md), implementation and tests |
''',
        "docs/literature_map.md": '''## Sequential evidence and anytime-valid inference used by P100

P100 uses standard nonnegative-supermartingale and time-uniform inference machinery rather than claiming that machinery as new. Ville (1939) supplies the classical maximal inequality. Howard, Ramdas, McAuliffe, and Sekhon (2021) provide modern time-uniform inference context, and Vovk and Wang (2021) provide the e-value calibration and combination context already used by P99. P100's novel scope is the repository-specific exact integration with the P92-P99 certification chain.
''',
        "docs/reference_audit.md": '''## P100 sequential-inference references

- Ville (1939): classical nonnegative-supermartingale maximal inequality used for the anytime-valid crossing rule.
- Howard, Ramdas, McAuliffe, and Sekhon (2021), DOI `10.1214/20-AOS1991`: modern time-uniform inference context.
- Vovk and Wang (2021), DOI `10.1214/20-AOS2020`: e-value calibration and combination context inherited from P99.

These references support standard method ingredients only. The exact P92-P100 composition, conditional freshness guards, and rational checkpoint are repository-specific results.
''',
    }
    for path, addition in entries.items():
        text = read(path)
        text = append_once(text, "## P100", addition)
        write(path, text)

    path = "docs/glossary.md"
    text = read(path)
    text = text.replace("The current documented theorem frontier is **P99**.", "The current documented theorem frontier is **P100**.")
    text = append_once(text, "### E-process", '''### E-process

A nonnegative evidence process whose sequential validity is preserved under the declared null. In P100, `M_t = product_{s <= t} ((1 - eta_s) + eta_s E_s)` is a nonnegative supermartingale when each current P99 e-value is conditionally valid given the past and each stake is predictable.

### Predictable stake

A stake chosen from information available before the current certification data are inspected. P100 permits adaptation to completed rounds but rejects current-round leakage.
''')
    write(path, text)

    path = "docs/research_map.md"
    text = read(path)
    text = text.replace("The current documented theorem frontier is **P99**.", "The current documented theorem frontier is **P100**.")
    text = text.replace("current theorem frontier is **P99**", "current theorem frontier is **P100**")
    text = append_once(text, "## P100: anytime-valid sequential e-process", '''## P100: anytime-valid sequential e-process

P100 adds the outer sequential layer to P99. Each current fresh P99 e-value must remain conditionally valid given the accumulated past; the current exact-rational stake must be chosen before current certification data are inspected. The product of reserve-stake factors is a nonnegative supermartingale, and Ville's inequality controls the probability of ever crossing `1/alpha`.

At the exact 95 percent checkpoint, `E_t = 25/2`, `eta_t = 1/2`, and `F_t = 27/4`; two fresh rounds give `M_2 = 729/16 = 45.5625 > 20`. The declared two-round unique-data totals are `30192 / 30336`.

Direct theorem: [P100](proposition_100_anytime_sequential_eprocess.md). Provenance: [P100 equation record](p100_equation_provenance.md).
''')
    write(path, text)


def patch_websites() -> None:
    path = "website/index.html"
    text = read(path)
    replacements = {
        '<strong>99</strong><span>proposition-level results</span>': '<strong>100</strong><span>proposition-level results</span>',
        'P99 current theorem frontier · v0.82.0': 'P100 current theorem frontier · v0.82.0',
        'Explore all 99 results →': 'Explore all 100 results →',
        '99 proposition-level results through P99': '100 proposition-level results through P100',
        'The 99-result program is summarized here; <a href="research-map.html">all 99 propositions</a>': 'The 100-result program is summarized here; <a href="research-map.html">all 100 propositions</a>',
        'current P94 frontier': 'current P100 frontier',
        'sources.html#p94-source': 'sources.html#p100-source',
        '93 proposition-level results through P93': '100 proposition-level results through P100',
        '<!-- Current theorem asset: docs/figures/p92_exact_global_mixed_prevalence_distance.svg -->': '<!-- Current theorem asset: docs/figures/p100_anytime_sequential_eprocess.svg -->',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = regex_replace_once(text, r'<!-- current-frontier-home: P99 -->\n<section id="p99-frontier".*?</section>', P100_HOME, label=path)
    write(path, text)

    path = "website/visual-atlas.html"
    text = read(path)
    match = re.search(r'<!-- current-frontier-visual: P99 -->\n(<section id="p99-frontier".*?</section>\n)', text, flags=re.S)
    if match:
        p99 = match.group(1).replace("Current theorem frontier · P99", "Previous theorem frontier · P99", 1)
        p99 = p99.replace('class="theorem-frontier current-frontier-visual"', 'class="theorem-frontier"', 1)
        text = text[:match.start()] + P100_ATLAS + p99 + text[match.end():]
    elif '<!-- current-frontier-visual: P100 -->' not in text:
        raise RuntimeError(f"{path}: P99 current section not found")
    write(path, text)

    for path in ("website/plain-language.html", "website/start-here.html"):
        text = read(path)
        text = text.replace("99 results · current frontier P99", "100 results · current frontier P100")
        text = text.replace("99-result Research II theorem program currently reaching P99", "100-result Research II theorem program currently reaching P100")
        text = text.replace("Open all 99 Research II results", "Open all 100 Research II results")
        text = text.replace("The 99 propositions", "The 100 propositions")
        text = text.replace("P1-P99", "P1-P100")
        text = text.replace("P75-P99", "P75-P100")
        text = text.replace("The 99 Research II propositions by scientific role", "The 100 Research II propositions by scientific role")
        if 'id="p100-reader-frontier"' not in text:
            match = re.search(r'(<section class="boundary" id="p99-reader-frontier">.*?</section>\n)', text, flags=re.S)
            if not match:
                raise RuntimeError(f"{path}: P99 reader frontier not found")
            p99 = match.group(1).replace("Research II · Current frontier · P99", "Research II · Previous frontier · P99", 1)
            text = text[:match.start()] + P100_READER + p99 + text[match.end():]
        write(path, text)

    path = "website/research-map.html"
    text = read(path)
    text = text.replace("Ninety-eight results, one dependency-aware scientific program", "One hundred results, one dependency-aware scientific program")
    text = text.replace("Current Research II model-audit range: P75-P99.", "Current Research II model-audit range: P75-P100.")
    text = text.replace("The current theorem frontier is P99.", "The current theorem frontier is P100.")
    text = text.replace('<div><strong>99</strong><span>proposition-level results</span></div>', '<div><strong>100</strong><span>proposition-level results</span></div>')
    text = text.replace('<div><strong>P99</strong><span>current theorem frontier</span></div>', '<div><strong>P100</strong><span>current theorem frontier</span></div>')
    text = text.replace("P74-P98 continue", "P74-P100 continue")
    text = text.replace("P73-P98", "P73-P100")
    text = text.replace("P77-P99", "P77-P100")
    text = text.replace("P19 and P71-P98", "P19 and P71-P100")
    text = text.replace("index.html#p99-frontier", "index.html#p100-frontier")
    text = text.replace("Continue to the current P99 frontier", "Continue to the current P100 frontier")
    text = text.replace("visual-atlas.html#p99-frontier", "visual-atlas.html#p100-frontier")
    text = text.replace("See the P99 figure", "See the P100 figure")
    text = text.replace("docs/p99_equation_provenance.md", "docs/p100_equation_provenance.md", 1)
    text = text.replace("Audit P99 provenance", "Audit P100 provenance")
    if 'id="p100-research-map"' not in text:
        text = text.replace('<section class="result" id="p99-research-map">', P100_RESEARCH_RESULT + '<section class="result" id="p99-research-map">', 1)
    write(path, text)

    path = "website/implementation.html"
    text = read(path)
    text = text.replace("Stage 06 · P73-P99", "Stage 06 · P73-P100")
    text = text.replace("P73-P99 build a continuous chain", "P73-P100 build a continuous chain")
    text = text.replace("current P99 frontier", "current P100 frontier")
    phrase = "P99 aggregates selection-valid fold evidence with exact e-values"
    if "P100 compounds fresh P99 round evidence" not in text and phrase in text:
        text = text.replace(phrase, phrase + "; P100 compounds fresh P99 round evidence through predictable reserve stakes into an anytime-valid sequential e-process", 1)
    write(path, text)


def patch_start_here_markdown() -> None:
    path = "START_HERE.md"
    text = read(path)
    text = text.replace("The current public theorem frontier is **P99**.", "The current public theorem frontier is **P100**.")
    text = text.replace("current theorem frontier is **P99**", "current theorem frontier is **P100**")
    text = text.replace("P1-P99", "P1-P100")
    text = append_once(text, "### P100: anytime-valid sequential e-process", '''### P100: anytime-valid sequential e-process

P100 adds a sequential outer layer to P99. Each new certification round produces a P99 e-value `E_t` that must remain conditionally valid given the completed history. A stake `eta_t` is chosen from past information only, and the factor `F_t = (1 - eta_t) + eta_t E_t` updates the cumulative process `M_t`.

The exact 95 percent checkpoint is intentionally easy to audit: `E_t = 25/2` is not individually decisive; half stake gives `F_t = 27/4`; two fresh rounds give `M_2 = 729/16 = 45.5625 > 20`. The declared two-round unique-data totals are `30192 / 30336`.

The protection is anytime-valid because `M_t` is a nonnegative supermartingale under the declared sequential null and Ville's inequality controls the probability of ever crossing `1 / alpha`. P100 does not permit current-round leakage or reused-data relabeling.

Direct proof: [P100](docs/proposition_100_anytime_sequential_eprocess.md).
''')
    write(path, text)


def patch_change_log() -> None:
    path = "CHANGELOG.md"
    text = read(path)
    if "Unreleased research frontier - P100" not in text:
        marker = text.find("## ")
        block = '''## Unreleased research frontier - P100

- Added Proposition 100, an exact anytime-valid sequential e-process over fresh P99 certification rounds.
- Added predictable exact-rational reserve stakes, conditional-freshness guards, and Ville-threshold monitoring.
- Added the exact `25/2 -> 27/4 -> 729/16` two-round checkpoint and `30192 / 30336` unique-data accounting.
- Added the canonical P100 figure, equation/novelty provenance, reader-surface contracts, and publication synchronization while keeping the formal release at v0.82.0.

'''
        if marker >= 0:
            text = text[:marker] + block + text[marker:]
        else:
            text = block + text
    write(path, text)


def patch_reader_tests() -> None:
    # Historical reader tests should track the current public frontier without
    # losing their own proposition-specific checks.
    for path_obj in sorted((ROOT / "tests").glob("test_p*_reader_surface_coherence.py")):
        if path_obj.name in {"test_p99_reader_surface_coherence.py", "test_p100_reader_surface_coherence.py"}:
            continue
        text = path_obj.read_text(encoding="utf-8")
        text = text.replace('CURRENT_FRONTIER = "P99"', 'CURRENT_FRONTIER = "P100"')
        text = text.replace("The current public theorem frontier is **P99**.", "The current public theorem frontier is **P100**.")
        text = text.replace("The current documented theorem frontier is **P99**.", "The current documented theorem frontier is **P100**.")
        text = text.replace("99 results · current frontier P99", "100 results · current frontier P100")
        text = text.replace("## 5. Focused audit of the current P99 frontier", "## 5. Focused audit of the current P100 frontier")
        path_obj.write_text(text, encoding="utf-8")

    p99 = '''from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def test_p99_is_preserved_as_the_immediate_historical_predecessor() -> None:
    home = _read("website/index.html")
    atlas = _read("website/visual-atlas.html")
    plain = _read("website/plain-language.html")
    start = _read("website/start-here.html")
    research = _read("website/research-map.html")
    roadmap = _read("docs/theorem_roadmap.md")
    navigation = _read("docs/research_navigation.md")

    assert '<!-- current-frontier-home: P100 -->' in home
    assert 'id="p100-frontier"' in atlas
    assert 'id="p99-frontier"' in atlas
    assert atlas.index('id="p100-frontier"') < atlas.index('id="p99-frontier"')
    assert "Previous theorem frontier · P99" in atlas
    assert 'id="p99-reader-frontier"' in plain
    assert 'id="p99-reader-frontier"' in start
    assert 'id="p99-research-map"' in research
    assert research.index('id="p100-research-map"') < research.index('id="p99-research-map"')
    assert "## P99: cross-fitted e-value aggregation" in roadmap
    assert "For P99:" in navigation
    assert "p99_cross_fitted_evalue_aggregation.svg" in navigation


def test_p99_exact_checkpoint_and_boundary_remain_auditable() -> None:
    theorem = _read("docs/proposition_99_cross_fitted_evalue_aggregation.md")
    source = _read("src/consciousness_bridge/cross_fitted_evalue_aggregation.py")
    tests = _read("tests/test_cross_fitted_evalue_aggregation.py")

    assert "3774" in theorem and "3792" in theorem
    assert "15096" in theorem and "15168" in theorem
    assert "physical-to-experiential bridge" in theorem
    assert "aggregate_e_value" in source
    assert "3774" in tests and "3792" in tests
'''
    write("tests/test_p99_reader_surface_coherence.py", p99)

    p100 = '''from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def test_p100_is_current_across_reader_and_publication_surfaces() -> None:
    verifier = _read("scripts/verify_repository.py")
    home = _read("website/index.html")
    atlas = _read("website/visual-atlas.html")
    plain = _read("website/plain-language.html")
    start = _read("website/start-here.html")
    research = _read("website/research-map.html")
    implementation = _read("website/implementation.html")
    readme = _read("README.md")
    roadmap = _read("docs/theorem_roadmap.md")
    navigation = _read("docs/research_navigation.md")
    reproducibility = _read("docs/reproducibility.md")
    citation = _read("CITATION.md")

    assert 'CURRENT_FRONTIER = "P100"' in verifier
    assert '<!-- current-frontier-home: P100 -->' in home
    assert 'id="p100-frontier"' in home
    assert "Current theorem frontier · P100" in home
    assert "Explore all 100 results" in home
    assert '<!-- current-frontier-visual: P100 -->' in atlas
    assert atlas.index('id="p100-frontier"') < atlas.index('id="p99-frontier"')
    assert "Previous theorem frontier · P99" in atlas
    assert 'id="p100-reader-frontier"' in plain
    assert 'id="p100-reader-frontier"' in start
    assert "100 results · current frontier P100" in plain
    assert "100 results · current frontier P100" in start
    assert 'id="p100-research-map"' in research
    assert "Current Research II model-audit range: P75-P100." in research
    assert "The current theorem frontier is P100." in research
    assert "Stage 06 · P73-P100" in implementation
    assert "P73-P100 build a continuous chain" in implementation
    assert "current P100 frontier" in implementation
    assert "P100 compounds fresh P99 round evidence" in implementation
    assert "The current public theorem frontier is **P100**." in readme
    assert "docs/proposition_100_anytime_sequential_eprocess.md" in readme
    assert "The current documented theorem frontier is **P100**." in roadmap
    assert "P1 through P100 with explicit dependency branches" in roadmap
    assert "## P100: anytime-valid sequential e-process" in roadmap
    assert "## After P100" in roadmap
    assert "The current documented theorem frontier is **P100**." in navigation
    assert "**Results:** P75 through P100" in navigation
    assert "For P100:" in navigation
    assert "p100_anytime_sequential_eprocess.svg" in navigation
    assert "The current public theorem frontier is **P100**." in reproducibility
    assert "## 5. Focused audit of the current P100 frontier" in reproducibility
    assert "docs/figures/p100_anytime_sequential_eprocess.svg" in reproducibility
    assert "## Current theorem frontier: P100" in citation


def test_p100_exact_checkpoint_and_scientific_boundary_are_visible() -> None:
    theorem = _read("docs/proposition_100_anytime_sequential_eprocess.md")
    provenance = _read("docs/p100_equation_provenance.md")
    source = _read("src/consciousness_bridge/anytime_sequential_eprocess.py")
    home = _read("website/index.html")
    start = _read("website/start-here.html")

    for token in ("25}{2", "27}{4", "729}{16", "30192", "30336"):
        assert token in theorem
    assert "Ville" in theorem
    assert "nonnegative supermartingale" in theorem
    assert "physical-to-experiential bridge" in theorem
    assert "standard" in provenance.lower()
    assert "repository-specific" in provenance.lower()
    assert "physical-to-experiential bridge" in source
    assert "729 / 16" in home
    assert "Exact P100 checkpoint:" in start
'''
    write("tests/test_p100_reader_surface_coherence.py", p100)

    # Generic narrative tests sometimes pin the current count/frontier. Update
    # only those explicit current-state phrases, not historical P99 content.
    for path_obj in sorted((ROOT / "tests").glob("test_*.py")):
        if path_obj.name in {"test_p99_reader_surface_coherence.py", "test_p100_reader_surface_coherence.py"}:
            continue
        text = path_obj.read_text(encoding="utf-8")
        text = text.replace('CURRENT_FRONTIER = "P99"', 'CURRENT_FRONTIER = "P100"')
        text = text.replace("Current theorem frontier · P99", "Current theorem frontier · P100")
        text = text.replace("current P99 frontier", "current P100 frontier")
        text = text.replace("99 results · current frontier P99", "100 results · current frontier P100")
        text = text.replace("Explore all 99 results", "Explore all 100 results")
        text = text.replace("The current public theorem frontier is **P99**.", "The current public theorem frontier is **P100**.")
        text = text.replace("The current documented theorem frontier is **P99**.", "The current documented theorem frontier is **P100**.")
        text = text.replace("## 5. Focused audit of the current P99 frontier", "## 5. Focused audit of the current P100 frontier")
        path_obj.write_text(text, encoding="utf-8")


def main() -> None:
    patch_theorem_notation()
    patch_verifier()
    patch_figure_sync()
    patch_readme()
    patch_roadmap()
    patch_navigation()
    patch_reproducibility()
    patch_citations()
    patch_documentation_records()
    patch_websites()
    patch_start_here_markdown()
    patch_change_log()
    patch_reader_tests()

    subprocess.run(
        [sys.executable, "scripts/sync_figure_publication.py"],
        cwd=ROOT,
        check=True,
    )
    print("[p100] public theorem frontier promoted to P100; formal release remains v0.82.0")


if __name__ == "__main__":
    main()
