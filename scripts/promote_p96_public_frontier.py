"""Promote the canonical public research frontier from P95 to P96.

This migration is intentionally deterministic and idempotent. It updates the
hand-maintained reader, citation, verification, and website sources. Generated
figure gateway files are rebuilt afterwards by ``generate_all_figures.py`` and
``sync_figure_publication.py``.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def _write(path: str, text: str) -> None:
    (ROOT / path).write_text(text.rstrip() + "\n", encoding="utf-8")


def _replace(path: str, old: str, new: str, *, required: bool = True) -> None:
    text = _read(path)
    if old not in text:
        if required and new not in text:
            raise RuntimeError(f"{path}: expected source text not found: {old!r}")
        return
    _write(path, text.replace(old, new))


def _regex(path: str, pattern: str, replacement: str, *, flags: int = 0) -> None:
    text = _read(path)
    updated, count = re.subn(pattern, replacement, text, flags=flags)
    if count == 0:
        if replacement.strip() not in text:
            raise RuntimeError(f"{path}: regex did not match: {pattern!r}")
        return
    _write(path, updated)


P96_TITLE = "Selection-Valid Holdout Stratification"
P96_PROOF = "proposition_96_selection_valid_holdout_stratification.md"
P96_PROVENANCE = "p96_equation_provenance.md"
P96_FIGURE = "p96_selection_valid_holdout_stratification.svg"
P96_SOURCE = "selection_valid_holdout_stratification.py"
P96_TEST = "test_selection_valid_holdout_stratification.py"


# ---------------------------------------------------------------------------
# Verifier and generated-publication machinery
# ---------------------------------------------------------------------------
_replace(
    "scripts/verify_repository.py",
    'CURRENT_FRONTIER = "P95"',
    'CURRENT_FRONTIER = "P96"',
)
_replace(
    "scripts/verify_repository.py",
    '    "tests/test_drift_aware_stratified_sign_coherence.py",\n',
    '    "tests/test_drift_aware_stratified_sign_coherence.py",\n'
    '    "docs/proposition_96_selection_valid_holdout_stratification.md",\n'
    '    "docs/p96_equation_provenance.md",\n'
    '    "docs/figures/p96_selection_valid_holdout_stratification.svg",\n'
    '    "src/consciousness_bridge/selection_valid_holdout_stratification.py",\n'
    '    "tests/test_selection_valid_holdout_stratification.py",\n',
)
_replace(
    "scripts/verify_repository.py",
    'STALE_READER_FRONTIER_MARKERS = (\n',
    'STALE_READER_FRONTIER_MARKERS = (\n'
    '    "Current theorem frontier · P95",\n'
    '    "current P95 frontier",\n'
    '    "<strong>P95</strong><span>current theorem frontier</span>",\n',
)

sync = _read("scripts/sync_figure_publication.py")
if "if frontier == 96:" not in sync:
    needle = "    return []\n\n\ndef _frontier_page"
    block = '''    if frontier == 96:
        return [
            "### Exact P96 selection-valid holdout stratification",
            "",
            "P96 closes one precise adaptive-regime gap left open by P95: pilot information may choose the regime plan, but the plan is frozen before an independent certification sample is inspected.",
            "",
            "```text",
            "pilot selects: B, regime definitions, m_b, alpha_b",
            "holdout requirement: C independent of S",
            "familywise condition: sum_b alpha_b <= alpha",
            "extra alpha penalty for pilot-selection complexity = 0",
            "B=2, m=1, 95% holdout crossing = 3645 per regime",
            "first exact denominator-24 holdout replication = 3648 per regime",
            "```",
            "",
            "The zero extra selection penalty is conditional on a genuinely independent holdout design and a plan frozen before holdout evaluation. Same-data redesign, naive splitting of a dependent stream, within-regime drift, model acceptance, consciousness identification, and bridge completion are not established.",
            "",
        ]
    return []


def _frontier_page'''
    if needle not in sync:
        raise RuntimeError("sync_figure_publication.py: P96 insertion point missing")
    sync = sync.replace(needle, block)
    _write("scripts/sync_figure_publication.py", sync)


# ---------------------------------------------------------------------------
# README, Start Here, changelog, citations
# ---------------------------------------------------------------------------
readme = _read("README.md")
readme = readme.replace(
    "The current public theorem frontier is **P95**.",
    "The current public theorem frontier is **P96**.",
)
readme = readme.replace(
    "**[Read the current frontier](docs/proposition_95_drift_aware_stratified_sign_coherence.md)**",
    "**[Read the current frontier](docs/proposition_96_selection_valid_holdout_stratification.md)**",
)
readme = re.sub(
    r"### Current theorem frontier\n\n.*?\n\n## Choose your path",
    '''### Current theorem frontier

![P96 Selection-Valid Holdout Stratification](docs/figures/p96_selection_valid_holdout_stratification.svg)

**Figure 2. P96 selection-valid holdout stratification.** P95 permits changing marginal laws across predeclared regimes, but it deliberately leaves data-dependent regime selection outside its guarantee. P96 closes one precise version of that gap by separating selection from certification. Pilot information may choose the number of regimes, regime definitions, declared dependence ranges, rational error budgets, and certification allocation. The selected plan is frozen before an independent holdout sample is inspected. Conditional on the pilot information, P95 applies to the fixed plan; the tower property then preserves the same unconditional familywise error bound.

For two selected regimes with one-step dependence and equal division of a 5 percent familywise budget, the holdout threshold remains **3645 observations per regime**, with the first exact denominator-24 replication at **3648 per regime**. The complexity of the pilot search itself adds no further alpha penalty under the declared independence and frozen-plan assumptions.

P96 does not justify reusing certification observations to redesign the segmentation, treating an ordinary random split of one dependent time series as automatically independent, allowing unrestricted drift inside a selected certification regime, accepting P75 after non-rejection, identifying consciousness, establishing nonphysicality, or closing the physical-to-experiential bridge.

## Choose your path''',
    readme,
    flags=re.S,
)
readme = readme.replace("**Public theorem frontier:** P95", "**Public theorem frontier:** P96")
_write("README.md", readme)

start = _read("START_HERE.md")
start = start.replace("The public theorem frontier is **P95**.", "The public theorem frontier is **P96**.")
start = start.replace("You do not need to read 94 propositions", "You do not need to read 96 propositions")
start = start.replace(
    "| Read the current frontier result | **[P95](docs/proposition_95_drift_aware_stratified_sign_coherence.md)** |",
    "| Read the current frontier result | **[P96](docs/proposition_96_selection_valid_holdout_stratification.md)** |",
)
start = start.replace("### P95: drift-aware stratified rejection", "### P95 historical drift-aware stratified rejection")
if "### P96: selection-valid holdout stratification" not in start:
    start += '''

### P96: selection-valid holdout stratification

P95 requires the regime plan to be fixed independently of the certification witness. P96 closes one precise post-selection gap by allowing arbitrary pilot-data selection of the regime plan, freezing that plan, and then applying P95 to genuinely independent holdout information. Conditional P95 validity integrates to the same unconditional familywise guarantee, so pilot-search complexity itself requires no additional alpha spending under the declared independence assumptions. The pilot data are not reused for certification. [Read P96](docs/proposition_96_selection_valid_holdout_stratification.md).

An ordinary random split of a temporally dependent stream is not automatically an independent holdout design. Same-data redesign, within-regime drift, model acceptance after non-rejection, consciousness identification, and the physical-to-experiential bridge remain outside the theorem.
'''
_write("START_HERE.md", start)

changelog = _read("CHANGELOG.md")
if not changelog.startswith("# Unreleased research frontier - P96"):
    prefix = '''# Unreleased research frontier - P96

## P96 selection-valid holdout stratification frontier

- Added Proposition 96 as the independent-holdout selection-valid continuation of P95.
- Allowed arbitrary pilot-data selection of regime count, regime definitions, declared finite dependence ranges, rational error budgets, and certification resource allocation.
- Required the selected plan to be frozen before certification and the certification information to be independent of the pilot-selection information.
- Proved conditional P95 familywise validity and integrated it with the tower property to preserve the same unconditional error bound without an extra pilot-selection-complexity alpha penalty.
- Preserved the P95 balanced holdout threshold: 3645 observations per regime for B=2 and m=1 at 95 percent familywise confidence, with first exact denominator-24 replication at 3648 per regime.
- Made the sample-separation cost explicit: pilot observations do not count as certification observations.
- Preserved the boundary that a naive split of one dependent time series is not automatically independent; same-data redesign, within-regime drift, non-rejection as acceptance, consciousness identification, and bridge completion remain open.
- Kept formal release v0.82.0 separate from the advancing theorem frontier.

'''
    changelog = prefix + changelog
_write("CHANGELOG.md", changelog)

_replace(
    "CITATION.bib",
    "Current documented theorem frontier: P95.",
    "Current documented theorem frontier: P96.",
)

cff = _read("CITATION.cff")
cff = cff.replace("Current documented theorem frontier: P95.", "Current documented theorem frontier: P96.")
if "Proposition 96" not in cff:
    cff = cff.replace(
        "Proposition 95 repairs the P94 temporal-pooling failure for predeclared regimes: regime-specific finite-range P94 certificates receive exact error budgets, and a familywise union bound rejects the joint null that every regime-specific marginal belongs to P75 without requiring independence between regimes. Current documented theorem frontier: P96.",
        "Proposition 95 repairs the P94 temporal-pooling failure for predeclared regimes: regime-specific finite-range P94 certificates receive exact error budgets, and a familywise union bound rejects the joint null that every regime-specific marginal belongs to P75 without requiring independence between regimes. Proposition 96 permits arbitrary pilot-data selection of that regime plan when the plan is frozen before evaluation on genuinely independent holdout information; conditional P95 validity and the tower property preserve the same unconditional familywise bound without an extra selection-complexity alpha penalty. Current documented theorem frontier: P96.",
    )
_write("CITATION.cff", cff)

citation = _read("CITATION.md")
citation = citation.replace(
    "This is the preferred citation for the research program at the current documented frontier, P94.",
    "This is the preferred citation for the research program at the current documented frontier, P96.",
)
citation = citation.replace(
    "note         = {Ongoing research program. Current documented theorem frontier: P94.}",
    "note         = {Ongoing research program. Current documented theorem frontier: P96.}",
)
citation = citation.replace(
    "The current citation metadata identify Version **0.82.0** and theorem frontier **P94**.",
    "The current citation metadata identify Version **0.82.0** and theorem frontier **P96**.",
)
citation = citation.replace(
    "The current documented theorem frontier is **P95**.",
    "The current documented theorem frontier is **P96**.",
)
citation = citation.replace(
    "[Detailed proposition record](docs/detailed_proposition_record.md): P1 through P94 chronological theorem record.",
    "[Detailed proposition record](docs/detailed_proposition_record.md): P1 through P96 chronological theorem record.",
)
if "## Current theorem frontier: P96" not in citation:
    citation += '''

## Current theorem frontier: P96

P96 is the selection-valid independent-holdout continuation of P95. Pilot information may choose the regime count, regime definitions, declared finite dependence ranges, and rational error budgets. The complete plan must be frozen before an independent certification sample is evaluated. Conditional on the pilot information, the selected plan is fixed and the P95 familywise guarantee applies; averaging the conditional failure probability preserves the same unconditional error bound.

- Proof: [`proposition_96_selection_valid_holdout_stratification.md`](docs/proposition_96_selection_valid_holdout_stratification.md)
- Equation provenance: [`p96_equation_provenance.md`](docs/p96_equation_provenance.md)
- Implementation: [`selection_valid_holdout_stratification.py`](src/consciousness_bridge/selection_valid_holdout_stratification.py)
- Tests: [`test_selection_valid_holdout_stratification.py`](tests/test_selection_valid_holdout_stratification.py)
- Figure: [`p96_selection_valid_holdout_stratification.svg`](docs/figures/p96_selection_valid_holdout_stratification.svg)

The sample-splitting, conditioning, union-bound, and tower-property ingredients are standard. The repository-original contribution is their explicit integration with the P92-P95 sign-coherence chain and executable guards for this model-audit problem. P96 does not license same-data redesign, assume that a naive split of a dependent time series is independent, establish model acceptance after non-rejection, identify consciousness, or close the physical-to-experiential bridge.
'''
_write("CITATION.md", citation)


# ---------------------------------------------------------------------------
# Theorem roadmap and audit/navigation documents
# ---------------------------------------------------------------------------
roadmap = _read("docs/theorem_roadmap.md")
roadmap = roadmap.replace("current documented theorem frontier is **P95**", "current documented theorem frontier is **P96**")
roadmap = roadmap.replace("**P1 through P95 with explicit dependency branches**", "**P1 through P96 with explicit dependency branches**")
roadmap = roadmap.replace("P71-P95 return to", "P71-P96 return to")
if "P96: pilot-selected regime plans" not in roadmap:
    roadmap = roadmap.replace(
        "&\\text{P95: predeclared drift regimes combine local P94 gates with familywise error control}\\\\\n",
        "&\\text{P95: predeclared drift regimes combine local P94 gates with familywise error control}\\\\\n"
        "&\\Downarrow\\\\\n"
        "&\\text{P96: pilot-selected regime plans are frozen and certified on independent holdout information}\\\\\n",
    )
roadmap = re.sub(
    r"## After P95\n.*\Z",
    '''## P96: selection-valid holdout stratification

P95 requires regime boundaries and error budgets to be fixed independently of the certification witness. P96 closes one precise post-selection gap by introducing a pilot-selection sigma-field and a separate certification sample. The pilot may choose the number of regimes, their definitions, declared finite dependence ranges, rational error budgets, and certification allocation. The complete plan is frozen before holdout evaluation.

With pilot information \(\mathcal S\) and certification information \(\mathcal C\), P96 assumes the holdout design justifies

\[
\mathcal C\perp\!\!\!\perp\mathcal S.
\]

Conditional on \(\mathcal S\), the selected plan is fixed and P95 gives

\[
\Pr\left(\bigcap_b \mathcal A_b\mid\mathcal S\right)
\ge 1-\sum_b\alpha_b\ge 1-\alpha.
\]

The tower property therefore preserves the same unconditional familywise bound. No additional alpha penalty depending on pilot-search complexity is required under these assumptions. The cost is data separation: pilot observations are not certification observations.

For two selected regimes with dependence range one and equal allocation of a 5 percent familywise budget, the holdout threshold remains 3645 observations per regime, with first exact denominator-24 replication at 3648.

Direct proof: [P96](proposition_96_selection_valid_holdout_stratification.md). Provenance: [P96 equation record](p96_equation_provenance.md). Implementation: [`selection_valid_holdout_stratification.py`](../src/consciousness_bridge/selection_valid_holdout_stratification.py). Tests: [`test_selection_valid_holdout_stratification.py`](../tests/test_selection_valid_holdout_stratification.py).

P96 is sufficient under a genuinely independent holdout design. A naive random split of one temporally dependent stream is not automatically covered. Same-data redesign, gradual within-regime drift, unknown dependence structure, model acceptance, consciousness identification, nonphysicality, and bridge completion remain open.

## After P96

P96 closes the independent-holdout version of adaptive regime selection. Any P97 candidate must close a genuinely new mathematical or scientific gap. Natural directions include guarded cross-fitting or multiple independent splits that recover pilot efficiency without invalidating selection, simultaneous candidate-family accounting without sample splitting, gradual within-regime drift with an explicitly time-varying target, or concentration under broader declared dependence classes. The physical-to-experiential bridge remains open.
''',
    roadmap,
    flags=re.S,
)
_write("docs/theorem_roadmap.md", roadmap)

nav = _read("docs/research_navigation.md")
nav = nav.replace("current documented theorem frontier is **P95**", "current documented theorem frontier is **P96**")
nav = nav.replace("**Results:** P75 through P95", "**Results:** P75 through P96")
nav = nav.replace(
    "**Current frontier:** [P95: Drift-Aware Stratified Sign-Coherence Rejection](proposition_95_drift_aware_stratified_sign_coherence.md)",
    "**Current frontier:** [P96: Selection-Valid Holdout Stratification](proposition_96_selection_valid_holdout_stratification.md)",
    1,
)
nav = nav.replace("P74 through P95", "P74 through P96")
nav = nav.replace("P71 through P95", "P71 through P96")
nav = nav.replace("full 95 proposition index", "full 96 proposition index")
nav = nav.replace("## P95 current frontier", "## P95 immediate predecessor")
nav = nav.replace(
    "P95 permits marginal drift across predeclared regimes while keeping a common marginal law only within each regime. It replaces invalid pooling with a familywise statement about the regime-specific P75 laws.",
    "P95 permits marginal drift across predeclared regimes while keeping a common marginal law only within each regime. P96 keeps that local P95 logic but allows the regime plan itself to be chosen from separate pilot information.",
)
# Replace the first current-frontier audit block, from 'For P95:' through its boundary paragraph.
nav = re.sub(
    r"For P95:\n\n\| Audit surface.*?P95 is a conditional drift-aware model-audit result.*?physical-to-experiential bridge\.\n",
    '''For P96:

| Audit surface | Canonical route |
| --- | --- |
| Direct theorem | [P96 proposition](proposition_96_selection_valid_holdout_stratification.md) |
| Equation and method provenance | [P96 provenance](p96_equation_provenance.md) |
| Implementation | [`selection_valid_holdout_stratification.py`](../src/consciousness_bridge/selection_valid_holdout_stratification.py) |
| Regression tests | [`test_selection_valid_holdout_stratification.py`](../tests/test_selection_valid_holdout_stratification.py) |
| Theorem figure | [P96 selection-valid holdout certificate](figures/p96_selection_valid_holdout_stratification.svg) |
| Repository reproduction | [Reproducibility Guide](reproducibility.md) |

P96 is a conditional selection-valid model-audit result. Pilot selection may be arbitrarily complicated, but the selected plan must be frozen before evaluation on genuinely independent holdout information that satisfies the selected local P94 assumptions. A naive split of one dependent stream is not automatically independent. The theorem does not establish model acceptance after non-rejection, identify consciousness, establish nonphysicality, or close the physical-to-experiential bridge.
''',
    nav,
    count=1,
    flags=re.S,
)
if "## P96 current frontier" not in nav:
    nav += '''

## P96 current frontier

**Current frontier:** [P96: Selection-Valid Holdout Stratification](proposition_96_selection_valid_holdout_stratification.md)

| What you want | Direct link |
| --- | --- |
| The theorem and proof | [P96 proposition](proposition_96_selection_valid_holdout_stratification.md) |
| Equation and method provenance | [P96 provenance](p96_equation_provenance.md) |
| Implementation | [`selection_valid_holdout_stratification.py`](../src/consciousness_bridge/selection_valid_holdout_stratification.py) |
| Regression tests | [`test_selection_valid_holdout_stratification.py`](../tests/test_selection_valid_holdout_stratification.py) |
| Figure | [P96 selection-valid holdout certificate](figures/p96_selection_valid_holdout_stratification.svg) |

P96 permits pilot-selected regime plans only when selection and certification are separated by a justified independent holdout design and the selected plan is frozen before holdout evaluation. It inherits the P95 local rejection logic and preserves the same familywise error budget by conditioning on the pilot information.
'''
_write("docs/research_navigation.md", nav)

repro = _read("docs/reproducibility.md")
repro = repro.replace("current P95 theorem checks", "current P96 theorem checks")
repro = repro.replace("current public theorem frontier is **P95**", "current public theorem frontier is **P96**")
repro = repro.replace("## 5. Focused audit of the current P95 frontier", "## 5. Focused audit of the current P96 frontier")
repro = repro.replace("The current theorem frontier is **P95**.", "The current theorem frontier is **P96**.")
repro = re.sub(
    r"Its direct technical record is:\n\n```text\n.*?```\n\nRun the focused theorem and publication checks with:\n\n```bash\n.*?```\n\nP95 responds.*?physical-to-experiential bridge\.\n",
    '''Its direct technical record is:

```text
docs/proposition_96_selection_valid_holdout_stratification.md
docs/p96_equation_provenance.md
src/consciousness_bridge/selection_valid_holdout_stratification.py
tests/test_selection_valid_holdout_stratification.py
docs/figures/p96_selection_valid_holdout_stratification.svg
figures/manifest.json
```

Run the focused theorem and publication checks with:

```bash
python -m pytest -q \\
  tests/test_selection_valid_holdout_stratification.py \\
  tests/test_p96_reader_surface_coherence.py \\
  tests/test_p95_reader_surface_coherence.py \\
  tests/test_frontier_reader_narrative.py \\
  tests/test_figure_publication_sync.py \\
  tests/test_frontier_publication_consistency.py
python scripts/sync_figure_publication.py --check
python scripts/verify_repository.py
```

P96 permits arbitrary pilot selection of the regime plan, freezes the plan before holdout evaluation, and applies P95 to independent certification information. Conditional P95 validity and the tower property preserve the same unconditional familywise error bound, so no additional alpha penalty is charged for pilot-selection complexity under the declared independence assumptions.

For two equally budgeted selected regimes with dependence range one at 95 percent familywise confidence, the holdout threshold remains `3645` observations per regime, with first exact denominator-24 replication at `3648` per regime. Pilot observations are additional and do not count toward certification.

A naive random split of one dependent time series is not automatically independent. Non-rejection remains inconclusive. P96 does not license same-data redesign, identify a latent state with consciousness, establish nonphysicality, validate an alternative ontology, or close the physical-to-experiential bridge.
''',
    repro,
    count=1,
    flags=re.S,
)
repro = repro.replace(
    "docs/figures/p92_exact_global_mixed_prevalence_distance.svg",
    "docs/figures/p96_selection_valid_holdout_stratification.svg",
)
_write("docs/reproducibility.md", repro)

# Complete proposition record: append an explicit P96 entry if absent.
record = _read("docs/detailed_proposition_record.md")
if "## P96" not in record and "### P96" not in record:
    record += '''

## P96: Selection-Valid Holdout Stratification

**Question.** Can P95 remain selection-valid when the regime plan is chosen adaptively from data?

**Result.** Yes for one precise design: use pilot information to choose the complete finite regime plan, freeze that plan, and certify it on independent holdout information. Conditional on the pilot sigma-field, P95 applies to the fixed plan; the tower property preserves the same unconditional familywise error bound. No extra alpha penalty is required for the complexity of the pilot search under the stated independence assumptions.

**Exact checkpoint.** For two selected regimes, one-step dependence, and a 5 percent familywise budget split equally, the holdout threshold remains 3645 per regime and the first exact denominator-24 replication remains 3648 per regime.

**Boundary.** Pilot observations are not certification observations. A naive split of a dependent time series is not automatically independent. Same-data redesign, within-regime drift, model acceptance, consciousness identification, nonphysicality, and bridge completion are not established.

- [Proof](proposition_96_selection_valid_holdout_stratification.md)
- [Equation provenance](p96_equation_provenance.md)
- [Figure](figures/p96_selection_valid_holdout_stratification.svg)
- [Implementation](../src/consciousness_bridge/selection_valid_holdout_stratification.py)
- [Tests](../tests/test_selection_valid_holdout_stratification.py)
'''
_write("docs/detailed_proposition_record.md", record)

# Compact additions to source/equation/figure audit maps.
claim_matrix = _read("docs/claim_source_matrix.md")
claim_matrix = claim_matrix.replace(
    "current repository contains 95 proposition-level results",
    "current repository contains 96 proposition-level results",
)
if "| P96 selection-valid holdout stratification |" not in claim_matrix:
    claim_matrix += '''
| P96 selection-valid holdout stratification | A pilot-selected regime plan may be certified with the P95 familywise guarantee without an extra pilot-search alpha penalty when the plan is frozen before evaluation on genuinely independent holdout information satisfying the selected local assumptions. | Repository-original synthesis of standard conditional/sample-splitting logic with the P92-P95 chain | `docs/proposition_96_selection_valid_holdout_stratification.md`, `docs/p96_equation_provenance.md`, exact implementation and tests | Independence and frozen-plan assumptions are essential; naive splitting of a dependent stream and same-data redesign are not covered; non-rejection is not acceptance and no consciousness ontology follows. |
'''
_write("docs/claim_source_matrix.md", claim_matrix)

eqmap = _read("docs/equation_and_citation_map.md")
if "P96 selection-valid holdout" not in eqmap.lower():
    eqmap += '''

## P96 selection-valid holdout stratification

P96 conditions on pilot-selection information, applies the fixed-plan P95 guarantee to independent certification data, and uses the tower property to recover the same unconditional familywise error bound. The sample-splitting, conditioning, union-bound, and tower-property ingredients are standard. The project-specific synthesis and executable guard conditions are documented in [p96_equation_provenance.md](p96_equation_provenance.md) and [Proposition 96](proposition_96_selection_valid_holdout_stratification.md).
'''
_write("docs/equation_and_citation_map.md", eqmap)

figcat = _read("docs/figure_catalog.md")
if P96_FIGURE not in figcat:
    figcat += '''

### P96 selection-valid holdout stratification

![P96 selection-valid holdout stratification](figures/p96_selection_valid_holdout_stratification.svg)

**What it shows.** Pilot information selects and freezes a regime plan, an independence gate separates pilot selection from certification, and independent holdout data are tested with the P94/P95 machinery. Conditional familywise validity integrates to the same unconditional guarantee.

**Scientific boundary.** This is a theorem diagram for an independent-holdout design. It does not establish that an arbitrary split of a dependent stream is independent, permit same-data redesign, validate a non-rejected model, identify consciousness, or close the physical-to-experiential bridge.
'''
_write("docs/figure_catalog.md", figcat)

research_map = _read("docs/research_map.md")
research_map = research_map.replace("P75-P95", "P75-P96")
research_map = research_map.replace("through P95", "through P96")
if "P96 selection-valid holdout" not in research_map.lower():
    research_map += '''

## P96: selection-valid holdout stratification

P96 closes one explicit adaptive-selection gap left by P95. Pilot information may select the finite regime plan, dependence ranges, and rational error allocation. The plan is frozen before a genuinely independent certification sample is evaluated. Conditioning on the pilot information makes the selected P95 plan fixed, and the tower property preserves the same unconditional familywise bound.

This is a sample-separation theorem, not a general same-data post-selection result. Pilot observations do not count as certification observations, and a naive split of one temporally dependent stream is not automatically independent.
'''
_write("docs/research_map.md", research_map)

glossary = _read("docs/glossary.md")
glossary = glossary.replace("current theorem frontier is P95", "current theorem frontier is P96")
glossary = glossary.replace("current documented theorem frontier is P95", "current documented theorem frontier is P96")
_write("docs/glossary.md", glossary)


# ---------------------------------------------------------------------------
# Website reader surfaces
# ---------------------------------------------------------------------------
home = _read("website/index.html")
home = home.replace("<strong>95</strong><span>proposition-level results</span>", "<strong>96</strong><span>proposition-level results</span>")
home = home.replace("P95 current theorem frontier · v0.82.0", "P96 current theorem frontier · v0.82.0")
home = home.replace("Explore all 95 results", "Explore all 96 results")
home = home.replace("95 proposition-level results through P95", "96 proposition-level results through P96")
home = home.replace("The 95 results form", "The 96 results form")
home = home.replace("The 95-result program", "The 96-result program")
home = home.replace("all 95 propositions", "all 96 propositions")
home = re.sub(
    r"<!-- current-frontier-home: P95 -->\n<section id=\"p95-frontier\".*?</section>",
    '''<!-- current-frontier-home: P96 -->
<section id="p96-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head">
    <p class="eyebrow">Research II · Current theorem frontier · P96</p>
    <h2>Selection-valid holdout stratification</h2>
    <p>P96 closes one precise adaptive-regime gap left by P95. Pilot information may choose the regime plan, but the complete plan is frozen before a genuinely independent holdout sample is evaluated with the P95 familywise certificate.</p>
  </div>
  <div class="theorem-figure-shell"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p96_selection_valid_holdout_stratification.svg"><img loading="eager" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p96_selection_valid_holdout_stratification.svg" alt="P96 selection-valid holdout stratification certificate" /></a></div>
  <div class="frontier-summary-grid">
    <article class="frontier-summary-card"><h3>Pilot selection may be complex</h3><p>Pilot information may choose the number and definition of regimes, declared dependence ranges, rational error budgets, and certification allocation.</p></article>
    <article class="frontier-summary-card"><h3>Selection and certification are separated</h3><p>The selected plan is frozen before holdout evaluation. Conditional P95 validity and the tower property preserve the same unconditional familywise error bound.</p></article>
    <article class="frontier-summary-card"><h3>Exact balanced checkpoint</h3><p>For B=2 and m=1 at 95 percent familywise confidence, the holdout crossing remains <strong>3645 per regime</strong>; the first exact denominator-24 replication is <strong>3648</strong>.</p></article>
  </div>
  <div class="boundary"><p><strong>Scientific boundary:</strong> a naive random split of one dependent time series is not automatically an independent holdout design. Same-data redesign, gradual within-regime drift, model acceptance after non-rejection, consciousness identification, nonphysicality, and bridge completion are not established.</p></div>
  <p><a href="research-map.html">Research II map</a> · <a href="visual-atlas.html">Theorem figures</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_96_selection_valid_holdout_stratification.md">proposition_96_selection_valid_holdout_stratification.md</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p96_equation_provenance.md">p96_equation_provenance.md</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/selection_valid_holdout_stratification.py">selection_valid_holdout_stratification.py</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_selection_valid_holdout_stratification.py">test_selection_valid_holdout_stratification.py</a></p>
</section>''',
    home,
    count=1,
    flags=re.S,
)
_write("website/index.html", home)

p96_reader = '''<section class="boundary" id="p96-reader-frontier"><div class="section-head"><p class="eyebrow">Research II · Current frontier · P96</p><h2>Adaptive pilot selection is separated from final certification</h2><p>P95 requires the regime plan to be fixed independently of the certification witness. P96 permits pilot information to choose that plan, freezes it before holdout evaluation, and then applies P95 to genuinely independent certification information. Conditional validity integrates to the same unconditional familywise bound, so pilot-search complexity itself adds no alpha penalty under the declared independence assumptions.</p><p><strong>Balanced holdout checkpoint:</strong> B=2, m=1 gives 3645 observations per regime for the 95 percent mathematical crossing and 3648 for the first exact denominator-24 replication.</p><p><strong>Boundary:</strong> a naive split of one dependent stream is not automatically independent. Same-data redesign, within-regime drift, model acceptance after non-rejection, consciousness identification, and bridge completion remain outside the theorem.</p><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_96_selection_valid_holdout_stratification.md">Read P96 theorem</a></p></div></section>'''

for path in ("website/plain-language.html", "website/start-here.html"):
    text = _read(path)
    text = text.replace("95 results · current frontier P95", "96 results · current frontier P96")
    text = text.replace("95-result Research II theorem program currently reaching P95", "96-result Research II theorem program currently reaching P96")
    text = text.replace("Open all 95 Research II results", "Open all 96 Research II results")
    text = text.replace("The 95 propositions", "The 96 propositions")
    text = text.replace("P1-P95", "P1-P96")
    text = text.replace("P75-P95", "P75-P96")
    text = text.replace("The 95 Research II propositions by scientific role", "The 96 Research II propositions by scientific role")
    text = text.replace("P78-P95 develop", "P78-P96 develop")
    text = text.replace("current Research II P95 frontier", "current Research II P96 frontier")
    text = text.replace("The current theorem frontier is P95.", "The current theorem frontier is P96.")
    if 'id="p96-reader-frontier"' not in text:
        marker = '<section class="boundary" id="p95-reader-frontier">'
        position = text.find(marker)
        if position < 0:
            raise RuntimeError(f"{path}: P95 reader-frontier insertion point missing")
        text = text[:position] + p96_reader + "\n\n" + text[position:]
        text = text.replace(
            '<section class="boundary" id="p95-reader-frontier"><div class="section-head"><p class="eyebrow">Research II · Current frontier · P95</p>',
            '<section class="boundary" id="p95-reader-frontier"><div class="section-head"><p class="eyebrow">Research II · Immediate predecessor · P95</p>',
            1,
        )
    _write(path, text)

research = _read("website/research-map.html")
research = research.replace("through Proposition 94", "through Proposition 96")
research = research.replace("Ninety-four results", "Ninety-six results")
research = research.replace("P71-P94 return", "P71-P96 return")
research = research.replace("Current Research II model-audit range: P75-P94.", "Current Research II model-audit range: P75-P96.")
research = research.replace("Current Research II model-audit range: P75-P95.", "Current Research II model-audit range: P75-P96.")
research = research.replace("The current theorem frontier is P95.", "The current theorem frontier is P96.")
research = research.replace("<strong>95</strong><span>proposition-level results</span>", "<strong>96</strong><span>proposition-level results</span>")
research = research.replace("<strong>P95</strong><span>current theorem frontier</span>", "<strong>P96</strong><span>current theorem frontier</span>")
research = research.replace("P73-P94", "P73-P96")
research = research.replace("P74-P94", "P74-P96")
research = research.replace("P77-P94", "P77-P96")
research = research.replace("P77-P94 move", "P77-P96 move")
research = research.replace("P77-P94:", "P77-P96:")
research = research.replace("P94 remains a conditional model-rejection theorem", "P96 remains a conditional model-rejection theorem")
research = research.replace("Current theorem frontier P94", "Current theorem frontier P96")
research = research.replace("index.html#p94-frontier", "index.html#p96-frontier")
if 'id="p96-research-map"' not in research:
    marker = '<section class="result" id="p95-research-map">'
    position = research.find(marker)
    if position < 0:
        raise RuntimeError("website/research-map.html: P95 insertion point missing")
    p96_map = '''<section class="result" id="p96-research-map"><span>P96</span><h3>P96: Can a pilot-selected regime plan be certified without paying for the complexity of the pilot search?</h3><p>Yes under one precise sample-separation design. Pilot information may choose the finite regime plan, dependence ranges, rational error budgets, and certification allocation. The plan is frozen before a genuinely independent holdout sample is evaluated with P95. Conditional P95 validity and the tower property preserve the same unconditional familywise error bound.</p><p><strong>Exact balanced checkpoint:</strong> B=2, m=1 gives the same 95 percent holdout crossing of 3645 observations per regime and first exact denominator-24 replication at 3648. Pilot observations are additional sample cost.</p><p><strong>Boundary:</strong> an ordinary random split of one dependent time series is not automatically independent. Same-data redesign, within-regime drift, model acceptance, consciousness identification, nonphysicality, and bridge completion remain open.</p><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_96_selection_valid_holdout_stratification.md">Read P96 theorem</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p96_equation_provenance.md">P96 equation provenance</a></p></section>\n\n'''
    research = research[:position] + p96_map + research[position:]
_write("website/research-map.html", research)

atlas = _read("website/visual-atlas.html")
atlas = atlas.replace("<!-- current-frontier-visual: P95 -->", "<!-- current-frontier-visual: P96 -->")
if 'id="p96-frontier"' not in atlas:
    marker = '<section id="p95-frontier"'
    position = atlas.find(marker)
    if position < 0:
        raise RuntimeError("website/visual-atlas.html: P95 insertion point missing")
    p96_atlas = '''<section id="p96-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head"><p class="eyebrow">Current theorem frontier · P96</p><h2>Selection-valid holdout stratification</h2><p>P96 permits arbitrary pilot selection of a finite regime plan when the plan is frozen before evaluation on genuinely independent holdout information. Conditional P95 validity then integrates to the same unconditional familywise guarantee.</p></div>
  <div class="theorem-figure-shell"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p96_selection_valid_holdout_stratification.svg"><img loading="eager" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p96_selection_valid_holdout_stratification.svg" alt="P96 selection-valid holdout stratification" /></a></div>
  <p><strong>Exact checkpoint:</strong> B=2, m=1, 95 percent familywise confidence keeps the P95 holdout crossing at 3645 per regime and first exact replication at 3648.</p>
  <p><strong>Scientific boundary:</strong> the independent-holdout and frozen-plan assumptions are essential. Same-data redesign, naive dependent-stream splitting, within-regime drift, model acceptance, and consciousness ontology are outside the theorem.</p>
  <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_96_selection_valid_holdout_stratification.md">Proof</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p96_equation_provenance.md">Equation provenance</a></p>
</section>\n\n'''
    atlas = atlas[:position] + p96_atlas + atlas[position:]
atlas = atlas.replace("<p class=\"eyebrow\">Current theorem frontier · P95</p>", "<p class=\"eyebrow\">Previous theorem frontier · P95</p>", 1)
_write("website/visual-atlas.html", atlas)

lineage = _read("website/research-lineage.html")
lineage = lineage.replace("<strong>95</strong><span>proposition-level results</span>", "<strong>96</strong><span>proposition-level results</span>")
lineage = lineage.replace("<strong>P95</strong><span>current theorem frontier</span>", "<strong>P96</strong><span>current theorem frontier</span>")
_write("website/research-lineage.html", lineage)

sources = _read("website/sources.html")
sources = sources.replace("P95 current theorem frontier", "P96 current theorem frontier")
sources = sources.replace("p95_drift_aware_stratified_sign_coherence.svg", "p96_selection_valid_holdout_stratification.svg")
_write("website/sources.html", sources)

# Turn the P95 reader test into a predecessor-coherence test now that P96 is current.
p95_test = '''from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p95_formal_record_is_preserved() -> None:
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


def test_p95_is_immediate_reader_predecessor_of_p96() -> None:
    atlas = _read("website/visual-atlas.html")
    research = _read("website/research-map.html")
    assert atlas.index('id="p96-frontier"') < atlas.index('id="p95-frontier"')
    assert "Previous theorem frontier · P95" in atlas
    assert research.index('id="p96-research-map"') < research.index('id="p95-research-map"')


def test_p95_scientific_boundary_remains_visible() -> None:
    proof = _read("docs/proposition_95_drift_aware_stratified_sign_coherence.md").lower()
    assert "predeclared" in proof
    assert "physical-to-experiential bridge" in proof
'''
_write("tests/test_p95_reader_surface_coherence.py", p95_test)

print("[p96] promoted canonical reader, citation, verification, and website sources to P96")
