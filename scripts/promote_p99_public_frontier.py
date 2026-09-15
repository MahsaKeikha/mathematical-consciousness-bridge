"""One-time publication promotion for Proposition 99.

Advance the public theorem frontier from P98 to P99 while preserving P98 as the
immediate predecessor. This file is temporary migration machinery and should be
removed after the promoted state is committed and fully validated.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text.rstrip() + "\n", encoding="utf-8")


def replace(text: str, old: str, new: str, *, required: bool = False) -> str:
    if old in text:
        return text.replace(old, new)
    if required and new not in text:
        raise RuntimeError(f"required promotion marker not found: {old!r}")
    return text


def insert_before(text: str, marker: str, block: str, *, identity: str) -> str:
    if identity in text:
        return text
    if marker not in text:
        raise RuntimeError(f"insertion marker not found: {marker!r}")
    return text.replace(marker, block + marker, 1)


# Changelog.
path = "CHANGELOG.md"
text = read(path)
if "# Unreleased research frontier - P99" not in text:
    text = """# Unreleased research frontier - P99

## P99 cross-fitted e-value aggregation frontier

- Added Proposition 99 as an exact distributed-evidence extension of the P96-P98 selection-valid cross-fitting chain.
- Converted valid level-tau fold rejection indicators into exact e-values R(tau)/tau.
- Allowed finite exact-rational threshold mixtures fixed before own-fold evaluation.
- Aggregated dependent cross-fitted fold e-values by a fixed convex average, using only expectation linearity and Markov's inequality.
- Certified the balanced K=2, B=2, m=1, 95 percent distributed-evidence crossing at 3774 observations per regime and first denominator-24 replication at 3792.
- Recorded unique two-fold totals 15096 and 15168, compared with P98 totals 16180 and 16224 for the matched equal-split design.
- Proved that the gain is configuration-specific: P99 does not uniformly dominate P98 and P98 does not uniformly dominate P99.
- Preserved the boundary that own-fold leakage, post-hoc calibration search, dependent-stream pseudo-folds, model acceptance, consciousness identification, nonphysicality, and bridge completion remain outside the theorem.
- Kept formal release v0.82.0 separate from the advancing theorem frontier.

""" + text
write(path, text)

# Repository citation metadata.
path = "CITATION.bib"
text = read(path)
text = text.replace("Current documented theorem frontier: P98.", "Current documented theorem frontier: P99.")
write(path, text)

path = "CITATION.cff"
text = read(path)
text = text.replace("Current documented theorem frontier: P98", "Current documented theorem frontier: P99")
if "cross-fitted e-value aggregation" not in text.lower():
    text = text.replace(
        " Current documented theorem frontier: P99.",
        " Proposition 99 adds cross-fitted e-value aggregation for distributed evidence while preserving exact finite-sample and selection-valid guard conditions. Current documented theorem frontier: P99.",
        1,
    )
write(path, text)

path = "CITATION.md"
text = read(path)
text = text.replace("current documented frontier, P98", "current documented frontier, P99")
text = text.replace("Current documented theorem frontier: P98", "Current documented theorem frontier: P99")
text = text.replace("theorem frontier **P98**", "theorem frontier **P99**")
text = text.replace("P1 through P98 chronological theorem record", "P1 through P99 chronological theorem record")
if "## Current theorem frontier: P99" not in text:
    text = text.replace("## Current theorem frontier: P98", "## Immediate predecessor theorem frontier: P98", 1)
    marker = "## Immediate predecessor theorem frontier: P98"
    block = """## Current theorem frontier: P99

The current documented theorem frontier is **P99**. P99 turns selection-valid P96/P98 fold rejection indicators into exact e-values, permits a finite calibration mixture fixed before own-fold evaluation, and combines the resulting cross-fitted fold evidence by a fixed convex average. The aggregate remains a valid e-value without assuming the final fold certificates are independent, and a global level-alpha rejection is obtained at aggregate e-value at least `1/alpha`.

For the declared two-fold, two-regime, one-step-dependent distributed-evidence checkpoint at 95 percent confidence, the per-regime crossing is **3774** and the first denominator-24 exact replication is **3792**, with unique totals **15096 / 15168**. This is a configuration-specific gain over the matched equal-split P98 checkpoint, not a uniform dominance claim.

P99 remains a conditional model-rejection theorem. It does not justify own-fold leakage, post-hoc calibration search, naive dependent-stream splitting, model acceptance after non-rejection, consciousness identification, nonphysicality, or completion of the physical-to-experiential bridge.

"""
    text = text.replace(marker, block + marker, 1)
write(path, text)

# Standard e-value reference.
path = "references.bib"
text = read(path)
if "10.1214/20-AOS2020" not in text:
    text += """

@article{VovkWang2021EValues,
  author  = {Vladimir Vovk and Ruodu Wang},
  title   = {E-values: Calibration, combination, and applications},
  journal = {The Annals of Statistics},
  year    = {2021},
  volume  = {49},
  number  = {3},
  pages   = {1736--1754},
  doi     = {10.1214/20-AOS2020}
}
"""
write(path, text)

# README.
path = "README.md"
text = read(path)
text = text.replace("The current public theorem frontier is **P98**.", "The current public theorem frontier is **P99**.")
text = text.replace("**Public theorem frontier:** P98", "**Public theorem frontier:** P99")
text = text.replace("[Read the current frontier](docs/proposition_98_cross_fitted_selection_valid_certification.md)", "[Read the current frontier](docs/proposition_99_cross_fitted_evalue_aggregation.md)")
pattern = re.compile(r"### Current theorem frontier\n\n!\[P98.*?(?=\n### |\n## )", re.DOTALL)
if pattern.search(text):
    block = """### Current theorem frontier

![P99 Cross-Fitted E-Value Aggregation](docs/figures/p99_cross_fitted_evalue_aggregation.svg)

**Figure 2. P99 cross-fitted e-value aggregation.** P99 converts a selection-valid level-`tau` fold rejection into the exact e-value `R(tau)/tau`. Finite threshold mixtures remain valid when their calibration is frozen before own-fold evaluation. Fixed convex averaging across folds remains valid even when the cross-fitted fold certificates are dependent, because the proof uses expectation linearity rather than independence.

For two equally weighted folds, two regimes per fold, one-step dependence, and 5 percent global error, the declared distributed-evidence design uses fold test level **1/25** and local regime level **1/50**. The exact mathematical crossing is **3774 observations per regime**, with first denominator-24 replication at **3792**. The unique two-fold totals are **15096 / 15168**. The matched equal-split P98 checkpoint is **4045 / 4056** per regime and **16180 / 16224** unique observations.

P99 does not uniformly dominate P98. It is designed to accumulate distributed evidence across several valid folds, while P98 can be better when one fold is individually decisive. P99 does not justify post-hoc calibration search, own-fold leakage, dependent-stream pseudo-folds, model acceptance, consciousness identification, nonphysicality, or completion of the physical-to-experiential bridge.
"""
    text = pattern.sub(lambda _: block, text, count=1)
text = text.replace("P1 through P98", "P1 through P99")
text = text.replace("98 proposition-level results", "99 proposition-level results")
write(path, text)

# Top-level Start Here.
path = "START_HERE.md"
text = read(path)
text = text.replace("The public theorem frontier is **P98**.", "The public theorem frontier is **P99**.")
text = text.replace("read 98 propositions", "read 99 propositions")
text = text.replace("**[P98](docs/proposition_98_cross_fitted_selection_valid_certification.md)**", "**[P99](docs/proposition_99_cross_fitted_evalue_aggregation.md)**")
if "### P99: cross-fitted e-value aggregation" not in text:
    text += """

### P99: cross-fitted e-value aggregation

P99 extends the P98 cross-fitted design from simultaneous foldwise error spending to exact evidence aggregation. A valid level-`tau` fold rejection becomes the e-value `R(tau)/tau`. Finite calibration mixtures fixed before own-fold evaluation remain e-values, and a fixed convex average across folds remains valid without assuming the fold certificates are independent.

For two folds with two one-step-dependent regimes each, the declared 95 percent distributed-evidence checkpoint crosses at 3774 observations per regime and first reaches an exact denominator-24 replication at 3792. Unique two-fold totals are 15096 and 15168. The gain over P98 is configuration-specific, and neither procedure uniformly dominates the other.

P99 does not justify own-fold leakage, post-hoc calibration search, naive dependent-stream splitting, model acceptance, consciousness identification, nonphysicality, or completion of the physical-to-experiential bridge. [Read P99](docs/proposition_99_cross_fitted_evalue_aggregation.md).
"""
write(path, text)

# Glossary.
path = "docs/glossary.md"
text = read(path)
text = text.replace("The current public frontier is **P98**.", "The current public frontier is **P99**.")
text = text.replace("## Current theorem frontier: P98", "## Immediate predecessor theorem frontier: P98")
if "## Current theorem frontier: P99" not in text:
    text += """

## Current theorem frontier: P99

**E-value:** a realized value of a nonnegative random variable whose expectation under the null is at most one.

**Fold test level:** a threshold `tau` at which a selection-valid P96 fold certificate is evaluated before conversion to the e-value `R(tau)/tau`.

**Threshold mixture:** a finite convex combination of fold e-values at predeclared test levels. The grid and weights must be frozen before the fold's own certification statistics are inspected.

**Cross-fitted e-value aggregate:** a fixed convex average of valid fold e-values. P99 does not require the final fold e-values to be independent.

**Distributed evidence:** an evidence geometry in which several folds contribute moderately to the global rejection rather than one fold being individually decisive.

**P99 boundary:** the theorem does not permit own-fold leakage, post-hoc calibration search, arbitrary dependent-stream splitting, model acceptance, consciousness identification, nonphysicality, or bridge completion. P99 does not uniformly dominate P98.
"""
write(path, text)

# Detailed proposition record.
path = "docs/detailed_proposition_record.md"
text = read(path)
text = text.replace("Complete P1 to P98 chronology", "Complete P1 to P99 chronology")
text = text.replace("98 disconnected proposition-level results", "99 disconnected proposition-level results")
if "## P99: Cross-Fitted E-Value Aggregation" not in text:
    text += """

## P99: Cross-Fitted E-Value Aggregation

**Question.** Can several selection-valid cross-fitted folds contribute moderate evidence toward one global rejection without assuming fold independence and without splitting the global alpha across folds in advance?

**Result.** Yes, for a declared finite e-value calibration. A valid P96 fold rejection at level `tau` gives the exact e-value `R(tau)/tau`. Finite exact-rational mixtures across thresholds remain fold e-values when calibration is frozen before own-fold evaluation. Fixed convex averaging across folds preserves null expectation at most one even when the fold certificates are dependent. Markov's inequality then gives a global level-alpha rejection at aggregate e-value at least `1/alpha`.

For `K=2`, two regimes per fold, dependence range one, equal fold weights, global alpha `1/20`, and fold test level `1/25`, the local regime level is `1/50`. The per-regime crossing is 3774 and the first exact denominator-24 replication is 3792, giving unique totals 15096 / 15168. The matched equal-split P98 crossing is 4045 / 4056 per regime. The P99 gain is configuration-specific and is not a uniform dominance theorem.

**Boundary.** P99 requires genuine own-fold exclusion, frozen calibration, independent certification blocks in the P98 sense, and the declared local dependence assumptions. It does not establish model acceptance, consciousness identification, nonphysicality, or completion of the physical-to-experiential bridge.

Direct proof: [P99](proposition_99_cross_fitted_evalue_aggregation.md). Provenance: [P99 equation record](p99_equation_provenance.md). Implementation: [`cross_fitted_evalue_aggregation.py`](../src/consciousness_bridge/cross_fitted_evalue_aggregation.py). Tests: [`test_cross_fitted_evalue_aggregation.py`](../tests/test_cross_fitted_evalue_aggregation.py).
"""
write(path, text)

# Research map documentation.
path = "docs/research_map.md"
text = read(path)
text = text.replace("The public theorem frontier is **P98**", "The public theorem frontier is **P99**")
text = text.replace("If you want the current result itself, open **[P98](proposition_98_cross_fitted_selection_valid_certification.md)**.", "If you want the current result itself, open **[P99](proposition_99_cross_fitted_evalue_aggregation.md)**. For the previous cross-fitted simultaneous-error frontier, open **[P98](proposition_98_cross_fitted_selection_valid_certification.md)**.")
if "## P99: cross-fitted e-value aggregation" not in text:
    text += """

## P99: cross-fitted e-value aggregation

P99 asks whether moderate evidence from several selection-valid cross-fitted folds can be accumulated without assuming the final fold certificates are independent. At a test level `tau` fixed before own-fold evaluation, a valid P96 fold rejection indicator becomes the e-value `R(tau)/tau`. Finite threshold mixtures and a fixed convex average across folds preserve null expectation at most one. Markov's inequality converts the final aggregate into a global level-alpha rejection rule.

For two folds with two one-step-dependent regimes each, fold test level `1/25`, and global alpha `1/20`, the local regime level is `1/50`. The mathematical threshold is 3774 observations per regime and the first exact denominator-24 replication is 3792, with unique totals 15096 / 15168.

P99 is complementary to P98. It can gain in distributed-evidence configurations but does not uniformly dominate P98. Own-fold leakage, post-hoc calibration search, dependent-stream pseudo-folds, model acceptance, consciousness identification, nonphysicality, and completion of the physical-to-experiential bridge remain outside the theorem.
"""
write(path, text)

# Research navigation.
path = "docs/research_navigation.md"
text = read(path)
text = text.replace("The current documented theorem frontier is **P98**.", "The current documented theorem frontier is **P99**.")
text = text.replace("**Results:** P75 through P98", "**Results:** P75 through P99")
text = text.replace("**Current frontier:** [P98: Cross-Fitted Selection-Valid Certification](proposition_98_cross_fitted_selection_valid_certification.md)", "**Current frontier:** [P99: Cross-Fitted E-Value Aggregation](proposition_99_cross_fitted_evalue_aggregation.md)")
text = text.replace("P74 through P98", "P74 through P99")
text = text.replace("P71 through P98", "P71 through P99")
text = text.replace("full 98 proposition index", "full 99 proposition index")
text = text.replace("## P98 current frontier", "## P98 immediate predecessor frontier")
if "For P99:" not in text:
    marker = "For P98:"
    block = """For P99:

| Audit surface | Canonical route |
| --- | --- |
| Direct theorem | [P99 proposition](proposition_99_cross_fitted_evalue_aggregation.md) |
| Equation and method provenance | [P99 provenance](p99_equation_provenance.md) |
| Implementation | [`cross_fitted_evalue_aggregation.py`](../src/consciousness_bridge/cross_fitted_evalue_aggregation.py) |
| Regression tests | [`test_cross_fitted_evalue_aggregation.py`](../tests/test_cross_fitted_evalue_aggregation.py) |
| Theorem figure | [P99 cross-fitted e-value aggregation](figures/p99_cross_fitted_evalue_aggregation.svg) |
| Repository reproduction | [Reproducibility Guide](reproducibility.md) |

P99 is a conditional distributed-evidence model-audit result. The fold plan and finite e-value calibration must be fixed without using the fold's own certification statistics. P99 does not require final fold e-values to be independent, but it still requires the P98 independent-block structure for selection-valid certification.

"""
    text = text.replace(marker, block + marker, 1)
write(path, text)

# Theorem roadmap.
path = "docs/theorem_roadmap.md"
text = read(path)
text = text.replace("The current documented theorem frontier is **P98**.", "The current documented theorem frontier is **P99**.")
text = text.replace("P1 through P98 with explicit dependency branches", "P1 through P99 with explicit dependency branches")
text = text.replace("P71-P98 return", "P71-P99 return")
text = text.replace("P98: rotated independent-block holdouts support cross-fitted selection-valid certification}\\\\", "P98: rotated independent-block holdouts support cross-fitted selection-valid certification}\\\\\n&\\Downarrow\\\\\n&\\text{P99: exact e-value aggregation accumulates distributed cross-fitted evidence without fold independence}\\\\")
# Repair a historical escaped-equation corruption left by an earlier migration.
text = re.sub(
    r"Conditional on \\\(\\mathcal S\\\\\\\), the selected plan is fixed and P95 gives.*?The tower property therefore preserves",
    lambda _: "Conditional on \\(\\mathcal S\\), the selected plan is fixed and P95 gives\n\n\\[\n\\Pr\\left(\\bigcap_b \\mathcal A_b\\mid\\mathcal S\\right)\n\\ge 1-\\sum_b\\alpha_b\\ge 1-\\alpha.\n\\]\n\nThe tower property therefore preserves",
    text,
    count=1,
    flags=re.DOTALL,
)
if "## P99: cross-fitted e-value aggregation" not in text:
    marker = "## After P98"
    block = """## P99: cross-fitted e-value aggregation

P98 controls the collection of cross-fitted fold statements by allocating a global error budget across folds. P99 provides a complementary distributed-evidence construction. Conditional on the selection information for fold `k`, a valid level-`tau` P96 rejection indicator satisfies

\\[
\\Pr(R_k(\tau)=1\\mid\\mathcal S_k)\\le\tau.
\\]

Therefore

\\[
E_k(\tau)=R_k(\tau)/\tau
\\]

has conditional and unconditional null expectation at most one. Finite threshold mixtures remain fold e-values, and a fixed convex average

\\[
E_{\\mathrm{CF}}=\\sum_k w_kE_k
\\]

remains an e-value even when the final cross-fitted fold certificates are dependent. Markov's inequality yields a global level-alpha rejection rule at `E_CF >= 1/alpha`.

For two equally weighted folds with two one-step-dependent regimes each, global alpha `1/20`, and fold test level `1/25`, the local regime budget is `1/50`. The exact mathematical crossing is 3774 observations per regime and the first denominator-24 replication is 3792, giving unique totals 15096 / 15168. The matched P98 equal-split design crosses at 4045 / 4056 per regime. P99 does not uniformly dominate P98; its advantage is specific to distributed-evidence configurations.

Direct proof: [P99](proposition_99_cross_fitted_evalue_aggregation.md). Provenance: [P99 equation record](p99_equation_provenance.md). Implementation: [`cross_fitted_evalue_aggregation.py`](../src/consciousness_bridge/cross_fitted_evalue_aggregation.py). Tests: [`test_cross_fitted_evalue_aggregation.py`](../tests/test_cross_fitted_evalue_aggregation.py).

P99 does not validate own-fold leakage, post-hoc calibration search, dependent-stream pseudo-folds, misspecified local dependence, model acceptance, consciousness identification, nonphysicality, or bridge completion.

## After P99

P99 closes the finite fixed-round distributed-evidence aggregation gap left open by P98. A natural P100 direction is an anytime-valid sequential extension in which fresh independent certification rounds contribute e-values over time and optional stopping is controlled by an explicit test-martingale or e-process argument. The physical-to-experiential bridge remains open.

"""
    text = text.replace(marker, block, 1)
text = re.sub(
    r"\nP96 closes the independent-holdout version of adaptive regime selection\. "
    r"Any P99 candidate must close a genuinely new mathematical or scientific gap\. "
    r"Natural directions include .*?The physical-to-experiential bridge remains open\.\n",
    "\n",
    text,
    count=1,
    flags=re.DOTALL,
)
write(path, text.rstrip() + "\n")

# Reproducibility guide.
path = "docs/reproducibility.md"
text = read(path)
text = text.replace("The current public theorem frontier is **P98**.", "The current public theorem frontier is **P99**.")
text = text.replace("current P98 theorem checks", "current P99 theorem checks")
text = text.replace("## 5. Focused audit of the current P98 frontier", "## 5. Focused audit of the current P99 frontier")
if "tests/test_cross_fitted_evalue_aggregation.py" not in text:
    marker = "tests/test_cross_fitted_selection_valid_certification.py"
    text = text.replace(marker, marker + "\ntests/test_cross_fitted_evalue_aggregation.py", 1)
if "docs/figures/p99_cross_fitted_evalue_aggregation.svg" not in text:
    marker = "docs/figures/p98_cross_fitted_selection_valid_certification.svg"
    text = text.replace(marker, marker + "\ndocs/figures/p99_cross_fitted_evalue_aggregation.svg", 1)
write(path, text)

# Equation and citation map.
path = "docs/equation_and_citation_map.md"
text = read(path)
if "## P99 cross-fitted e-value aggregation" not in text:
    text += """

## P99 cross-fitted e-value aggregation

- Theorem: [`proposition_99_cross_fitted_evalue_aggregation.md`](proposition_99_cross_fitted_evalue_aggregation.md)
- Equation and novelty provenance: [`p99_equation_provenance.md`](p99_equation_provenance.md)
- Implementation: [`cross_fitted_evalue_aggregation.py`](../src/consciousness_bridge/cross_fitted_evalue_aggregation.py)
- Tests: [`test_cross_fitted_evalue_aggregation.py`](../tests/test_cross_fitted_evalue_aggregation.py)
- Figure: [`p99_cross_fitted_evalue_aggregation.svg`](figures/p99_cross_fitted_evalue_aggregation.svg)
- Standard method source: Vovk and Wang (2021), *The Annals of Statistics* 49(3), 1736-1754, DOI `10.1214/20-AOS2020`.

P99 uses standard e-value expectation control, convex averaging, and Markov rejection. Repository-specific content is the integration with the exact P92-P98 certification chain, the frozen finite threshold calibration, exact-rational executable certificate, and the 3774/3792 distributed-evidence checkpoint. It does not claim a new e-value calculus.
"""
write(path, text)

# Claim/source matrix.
path = "docs/claim_source_matrix.md"
text = read(path)
if "P99 cross-fitted e-value aggregation" not in text:
    text += """

## P99 cross-fitted e-value aggregation

| Claim | Evidence role | Support | Boundary |
| --- | --- | --- | --- |
| A valid level-`tau` fold rejection gives `R(tau)/tau` with null expectation at most one | Standard probability / e-value construction | Vovk and Wang (2021); P96 fold validity | Requires fold test validity at the declared level |
| Fixed convex averages of fold e-values remain e-values without fold independence | Standard e-value merging by averaging | Vovk and Wang (2021); linearity of expectation | Weights must be fixed independently of certification outcomes |
| P99 integrates this construction with cross-fitted P96/P98 certification and exact rational thresholds | Repository-original integration | P99 proof, implementation, tests, provenance | Does not claim invention of e-values or averaging |
| Balanced distributed-evidence crossing is 3774 per regime with exact replication 3792 | Repository-original exact computation | P99 implementation and regression tests | Configuration-specific, not a universal sample-complexity theorem |
| P99 does not uniformly dominate P98 | Repository-original comparison statement | P99 exact examples | Sparse and distributed evidence can favor different procedures |
"""
write(path, text)

# Literature map and reference audit.
path = "docs/literature_map.md"
text = read(path)
if "10.1214/20-AOS2020" not in text:
    text += """

### Vovk and Wang 2021: e-values

**Reference:** Vladimir Vovk and Ruodu Wang, *E-values: Calibration, combination, and applications*, The Annals of Statistics 49(3), 1736-1754, DOI 10.1214/20-AOS2020.

**Role here:** standard source for e-values, expectation-based evidence, and valid e-value averaging. P99 cites this work for the general evidence calculus and does not present those standard ingredients as repository-original.
"""
write(path, text)

path = "docs/reference_audit.md"
text = read(path)
if "10.1214/20-AOS2020" not in text:
    text += """

### Vovk and Wang 2021

- **Title:** E-values: Calibration, combination, and applications
- **Journal:** The Annals of Statistics 49(3), 1736-1754
- **DOI:** 10.1214/20-AOS2020
- **Evidence role:** standard statistical method source for the e-value definition and averaging construction used by P99
- **Not claimed:** P99 does not claim authorship of e-values, e-value averaging, or Markov-based rejection
"""
write(path, text)

# Verifier current frontier and required files.
path = "scripts/verify_repository.py"
text = read(path)
text = text.replace('CURRENT_FRONTIER = "P98"', 'CURRENT_FRONTIER = "P99"')
if '"docs/proposition_99_cross_fitted_evalue_aggregation.md"' not in text:
    marker = '    "tests/test_p98_reader_surface_coherence.py",\n'
    addition = marker + '    "docs/proposition_99_cross_fitted_evalue_aggregation.md",\n    "docs/p99_equation_provenance.md",\n    "docs/figures/p99_cross_fitted_evalue_aggregation.svg",\n    "src/consciousness_bridge/cross_fitted_evalue_aggregation.py",\n    "tests/test_cross_fitted_evalue_aggregation.py",\n    "tests/test_p99_reader_surface_coherence.py",\n'
    text = text.replace(marker, addition, 1)
if '"Current theorem frontier · P98",' not in text:
    marker = 'STALE_READER_FRONTIER_MARKERS = (\n'
    text = text.replace(marker, marker + '    "Current theorem frontier · P98",\n    "current P98 frontier",\n    "<strong>P98</strong><span>current theorem frontier</span>",\n    "98 results · current frontier P98",\n    "Explore all 98 results",\n', 1)
write(path, text)

# Figure synchronizer: add P99 summary before the generic return.
path = "scripts/sync_figure_publication.py"
text = read(path)
if "if frontier == 99:" not in text:
    marker = "    return []\n\n\ndef _frontier_page"
    block = """    if frontier == 99:
        return [
            "### Exact P99 cross-fitted e-value aggregation",
            "",
            "P99 converts selection-valid P96/P98 fold rejection indicators into exact e-values and accumulates distributed evidence without assuming the final fold certificates are independent.",
            "",
            "```text",
            "fold test level tau = 1/25",
            "local regime alpha = 1/50",
            "K=2 folds, B=2 regimes, m=1",
            "95% mathematical crossing = 3774 per regime",
            "first exact denominator-24 replication = 3792 per regime",
            "cross-fitted unique totals = 15096 / 15168",
            "matched P98 crossing = 4045 / 4056 per regime",
            "```",
            "",
            "P99 uses fixed finite calibration and exact convex e-value averaging. It does not uniformly dominate P98 and does not validate own-fold leakage, post-hoc calibration search, dependent-stream pseudo-folds, model acceptance, consciousness identification, nonphysicality, or bridge completion.",
            "",
        ]
    return []


def _frontier_page"""
    text = text.replace(marker, block, 1)
write(path, text)

# Website homepage counts and current frontier.
path = "website/index.html"
text = read(path)
text = text.replace('<strong>98</strong><span>proposition-level results</span>', '<strong>99</strong><span>proposition-level results</span>', 1)
text = text.replace('P98 current theorem frontier · v0.82.0', 'P99 current theorem frontier · v0.82.0', 1)
text = text.replace('Explore all 98 results', 'Explore all 99 results', 1)
text = text.replace('98 proposition-level results through P98. The 98 results', '99 proposition-level results through P99. The 99 results', 1)
text = text.replace('The 98-result program', 'The 99-result program', 1)
text = text.replace('all 98 propositions', 'all 99 propositions', 1)
pattern = re.compile(r'<!-- current-frontier-home: P98 -->.*?(?=<section id="research-iii-overview">)', re.DOTALL)
block = """<!-- current-frontier-home: P99 -->
<section id="p99-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head">
    <p class="eyebrow">Research II · Current theorem frontier · P99</p>
    <h2>Cross-fitted e-value aggregation</h2>
    <p>P99 turns selection-valid fold rejections into exact e-values and combines distributed evidence across cross-fitted folds without assuming that the final fold certificates are independent.</p>
  </div>
  <div class="theorem-figure-shell"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p99_cross_fitted_evalue_aggregation.svg"><img loading="eager" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p99_cross_fitted_evalue_aggregation.svg" alt="P99 cross-fitted e-value aggregation" /></a></div>
  <div class="frontier-summary-grid">
    <article class="frontier-summary-card"><h3>Evidence, not only alpha spending</h3><p>A valid level-tau fold rejection contributes the exact e-value R(tau)/tau. Finite threshold mixtures are allowed when calibration is frozen before own-fold evaluation.</p></article>
    <article class="frontier-summary-card"><h3>Fold independence is not required for averaging</h3><p>Fixed convex averaging uses only expectation linearity. The P98 independent-block structure is still required to make each fold selection-valid.</p></article>
    <article class="frontier-summary-card"><h3>Exact distributed-evidence checkpoint</h3><p>For K=2, B=2, m=1, and tau=1/25, the crossing is <strong>3774 per regime</strong>; exact replication is <strong>3792</strong>; unique totals are <strong>15096 / 15168</strong>.</p></article>
  </div>
  <div class="boundary"><p><strong>Scientific boundary:</strong> P99 does not uniformly dominate P98. Calibration and fold weights must be fixed without own-fold evidence. Dependent-stream pseudo-folds, model acceptance, consciousness identification, nonphysicality, and bridge completion are not established.</p></div>
  <p><a href="research-map.html">Research II map</a> · <a href="visual-atlas.html">Theorem figures</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_99_cross_fitted_evalue_aggregation.md">P99 theorem</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p99_equation_provenance.md">P99 provenance</a></p>
</section>

"""
if pattern.search(text):
    text = pattern.sub(lambda _: block, text, count=1)
else:
    raise RuntimeError("homepage P98 frontier block not found")
write(path, text)

# Plain Language and website Start Here.
reader_block = """<section class="boundary" id="p99-reader-frontier"><div class="section-head"><p class="eyebrow">Research II · Current frontier · P99</p><h2>Several valid folds can now contribute evidence to one exact global test</h2><p>P99 converts a valid level-tau cross-fitted fold rejection into the exact e-value R(tau)/tau. A finite calibration mixture remains valid when it is frozen before the fold sees its own certification evidence, and fixed convex averaging across folds remains valid without assuming the final fold certificates are independent.</p></div><p>In the balanced two-fold, two-regime, one-step-dependent example, fold test level 1/25 gives local regime level 1/50. The mathematical crossing is <strong>3774 observations per regime</strong>, the first exact denominator-24 replication is <strong>3792</strong>, and the unique two-fold totals are <strong>15096 / 15168</strong>.</p><p>P99 does not uniformly dominate P98. Its advantage is distributed evidence. P98 can remain better when one fold is individually decisive. Own-fold leakage, post-hoc calibration search, dependent-stream pseudo-folds, model acceptance, consciousness identification, nonphysicality, and the physical-to-experiential bridge remain open.</p><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_99_cross_fitted_evalue_aggregation.md">Read P99 theorem</a></p></section>

"""
for path in ("website/plain-language.html", "website/start-here.html"):
    text = read(path)
    text = text.replace("98 results · current frontier P98", "99 results · current frontier P99")
    text = text.replace("The 98 Research II propositions by scientific role", "The 99 Research II propositions by scientific role")
    text = text.replace("Research II · Current frontier · P98", "Research II · Previous frontier · P98", 1)
    text = text.replace("Research II · Previous frontier · P97", "Research II · Historical frontier · P97", 1)
    if 'id="p99-reader-frontier"' not in text:
        marker = '<section class="boundary" id="p98-reader-frontier">'
        text = text.replace(marker, reader_block + marker, 1)
    write(path, text)

# Website Research Map.
path = "website/research-map.html"
text = read(path)
text = text.replace("Current Research II model-audit range: P75-P98.", "Current Research II model-audit range: P75-P99.")
text = text.replace("The current theorem frontier is P98.", "The current theorem frontier is P99.")
if 'id="p99-research-map"' not in text:
    marker = '<section class="result" id="p98-research-map">'
    block = """<section class="result" id="p99-research-map"><span>P99</span><h3>P99: Can distributed cross-fitted evidence be combined without fold independence?</h3><p>Yes, for a declared finite e-value calibration. A valid level-tau fold rejection becomes R(tau)/tau, finite threshold mixtures remain e-values when frozen before own-fold evaluation, and a fixed convex average remains valid without assuming the final fold certificates are independent.</p><p>The balanced K=2, B=2, m=1, 95 percent distributed-evidence checkpoint crosses at 3774 per regime, with exact replication at 3792 and unique totals 15096 / 15168. P99 does not uniformly dominate P98.</p><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_99_cross_fitted_evalue_aggregation.md">Read P99 theorem</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p99_equation_provenance.md">P99 equation provenance</a> · <a href="index.html#p99-frontier">Overview P99 frontier</a></p></section>

"""
    text = text.replace(marker, block + marker, 1)
text = text.replace('href="index.html#p98-frontier">Overview P97 frontier', 'href="visual-atlas.html#p97-frontier">Visual Atlas P97 frontier')
write(path, text)

# Visual Atlas.
path = "website/visual-atlas.html"
text = read(path)
text = text.replace('<!-- current-frontier-visual: P98 -->', '<!-- current-frontier-visual: P99 -->', 1)
text = text.replace("Current theorem frontier · P98", "Previous theorem frontier · P98", 1)
text = text.replace("Previous theorem frontier · P97", "Historical theorem frontier · P97", 1)
if 'id="p99-frontier"' not in text:
    marker = '<section id="p98-frontier"'
    block = """<section id="p99-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head"><p class="eyebrow">Current theorem frontier · P99</p><h2>Cross-fitted e-value aggregation</h2><p>P99 turns selection-valid cross-fitted fold rejections into exact e-values and combines distributed evidence by fixed convex averaging without assuming the final fold certificates are independent.</p></div>
  <div class="theorem-figure-shell"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p99_cross_fitted_evalue_aggregation.svg"><img loading="eager" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p99_cross_fitted_evalue_aggregation.svg" alt="P99 cross-fitted e-value aggregation" /></a></div>
  <div class="frontier-summary-grid"><article class="frontier-summary-card"><h3>Exact e-values</h3><p>At a frozen fold test level tau, rejection contributes R(tau)/tau.</p></article><article class="frontier-summary-card"><h3>Dependent folds can be averaged</h3><p>Fixed convex averaging requires no fold-independence assumption beyond the P98 structure used for each fold's own validity.</p></article><article class="frontier-summary-card"><h3>3774 / 3792</h3><p>The balanced distributed-evidence checkpoint reaches the global 95 percent threshold earlier than the matched equal-split P98 example.</p></article></div>
  <div class="boundary"><p><strong>Boundary:</strong> the gain is configuration-specific. P99 does not uniformly dominate P98 and does not relax own-fold exclusion, calibration, dependence, or bridge-interpretation guards.</p></div>
</section>

"""
    text = text.replace(marker, block + marker, 1)
write(path, text)

# Website Sources.
path = "website/sources.html"
text = read(path)
if 'id="p99-source"' not in text:
    marker = '<section id="p98-source">'
    block = """<section id="p99-source"><div class="section-head"><p class="eyebrow">Current theorem source · P99</p><h2>Cross-fitted e-value aggregation</h2><p>P99 uses standard e-value calculus to aggregate selection-valid cross-fitted fold evidence while preserving the repository's exact finite-sample guards.</p></div><div class="source-grid"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_99_cross_fitted_evalue_aggregation.md"><h3>Proposition 99</h3><p>Formal e-value aggregation theorem, exact checkpoint, non-dominance comparison, and scientific boundary.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p99_equation_provenance.md"><h3>P99 provenance</h3><p>Separates standard e-value, averaging, and Markov ingredients from repository-specific integration.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/cross_fitted_evalue_aggregation.py"><h3>P99 implementation</h3><p>Exact-rational threshold mixtures, fold weighting, nested P96 certification, and balanced thresholds.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_cross_fitted_evalue_aggregation.py"><h3>P99 exact tests</h3><p>Distributed evidence, calibration guards, dependence robustness, non-dominance examples, and 3774/3792 checkpoints.</p></a><a href="https://doi.org/10.1214/20-AOS2020"><h3>Standard e-value reference</h3><p>Vovk and Wang (2021), The Annals of Statistics.</p></a></div><div class="boundary"><p><strong>Scientific boundary:</strong> e-value aggregation is evidence calculus, not a consciousness ontology. P99 does not establish model acceptance, consciousness identification, nonphysicality, or bridge completion.</p></div></section>

"""
    text = text.replace(marker, block + marker, 1)
text = text.replace("Immediate predecessor theorem source · P97", "Historical theorem source · P97", 1)
text = text.replace("Current theorem source · P98", "Immediate predecessor theorem source · P98", 1)
write(path, text)

# Website implementation and lineage receive concise P99 entries.
path = "website/implementation.html"
text = read(path)
if "P99 cross-fitted e-value aggregation" not in text:
    marker = "</main>"
    block = """<section><div class="section-head"><p class="eyebrow">Current Research II implementation · P99</p><h2>P99 cross-fitted e-value aggregation</h2></div><p>The executable P99 layer uses exact rational fold levels, threshold-mixture weights, regime alpha weights, and fold weights. It delegates each threshold test to the selection-valid P96/P95/P94 chain and compares the final aggregate e-value with `1/alpha` exactly.</p><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/cross_fitted_evalue_aggregation.py">Open P99 implementation</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_cross_fitted_evalue_aggregation.py">Open P99 tests</a></p></section>\n"""
    text = text.replace(marker, block + marker, 1)
write(path, text)

path = "website/research-lineage.html"
text = read(path)
text = text.replace("P71-P98", "P71-P99")
if "P99" not in text or "e-value aggregation" not in text.lower():
    marker = "</main>"
    block = """<section class="boundary"><div class="section-head"><p class="eyebrow">Current Research II frontier · P99</p><h2>From selection-valid cross-fitting to distributed evidence</h2></div><p>P98 made rotated independent-block certification simultaneous. P99 adds an evidence layer: valid fold rejections become e-values, finite frozen calibrations are mixed exactly, and dependent cross-fitted fold evidence is averaged without assuming fold independence. The physical-to-experiential bridge remains open.</p></section>\n"""
    text = text.replace(marker, block + marker, 1)
write(path, text)

# Update historical reader-contract tests to recognize P99 as current while preserving older results.
path = "tests/test_p98_reader_surface_coherence.py"
text = read(path)
start = text.index("def test_p98_is_current_reader_frontier()")
end = text.index("\ndef test_p98_repository_audit_surfaces_are_synchronized()", start)
replacement = '''def test_p98_is_preserved_below_p99() -> None:
    verifier = _read("scripts/verify_repository.py")
    atlas = _read("website/visual-atlas.html")
    plain = _read("website/plain-language.html")
    start = _read("website/start-here.html")
    research = _read("website/research-map.html")

    assert 'CURRENT_FRONTIER = "P99"' in verifier
    assert atlas.index('id="p99-frontier"') < atlas.index('id="p98-frontier"')
    assert "Previous theorem frontier · P98" in atlas
    assert 'id="p98-reader-frontier"' in plain
    assert 'id="p98-reader-frontier"' in start
    assert 'id="p98-research-map"' in research
    assert research.index('id="p99-research-map"') < research.index('id="p98-research-map"')
    assert "99 results · current frontier P99" in plain
    assert "99 results · current frontier P99" in start

'''
text = text[:start] + replacement + text[end+1:]
start = text.index("def test_p98_repository_audit_surfaces_are_synchronized()")
end = text.index("\ndef test_p98_scientific_boundary_is_visible()", start)
replacement = '''def test_p98_repository_audit_surfaces_preserve_history() -> None:
    readme = _read("README.md")
    roadmap = _read("docs/theorem_roadmap.md")
    navigation = _read("docs/research_navigation.md")
    reproducibility = _read("docs/reproducibility.md")
    citation = _read("CITATION.md")

    assert "The current public theorem frontier is **P99**." in readme
    assert "P98" in readme
    assert "## P98: cross-fitted selection-valid certification" in roadmap
    assert "## P99: cross-fitted e-value aggregation" in roadmap
    assert "The current documented theorem frontier is **P99**." in navigation
    assert "For P98" in navigation
    assert "p98_cross_fitted_selection_valid_certification.svg" in navigation
    assert "The current public theorem frontier is **P99**." in reproducibility
    assert "## 5. Focused audit of the current P99 frontier" in reproducibility
    assert "P98" in citation and "P99" in citation

'''
text = text[:start] + replacement + text[end+1:]
write(path, text)

for path in ("tests/test_p97_reader_surface_coherence.py", "tests/test_p96_reader_surface_coherence.py", "tests/test_p94_reader_surface_coherence.py"):
    text = read(path)
    text = text.replace('CURRENT_FRONTIER = "P98"', 'CURRENT_FRONTIER = "P99"')
    text = text.replace("98 results · current frontier P98", "99 results · current frontier P99")
    text = text.replace("The current public theorem frontier is **P98**.", "The current public theorem frontier is **P99**.")
    text = text.replace("The current documented theorem frontier is **P98**.", "The current documented theorem frontier is **P99**.")
    text = text.replace("## 5. Focused audit of the current P98 frontier", "## 5. Focused audit of the current P99 frontier")
    if "atlas.index('id=\"p99-frontier\"')" not in text and "atlas = _read" in text:
        text = text.replace(
            "assert atlas.index('id=\"p98-frontier\"') < atlas.index('id=\"p97-frontier\"')",
            "assert atlas.index('id=\"p99-frontier\"') < atlas.index('id=\"p98-frontier\"')\n    assert atlas.index('id=\"p98-frontier\"') < atlas.index('id=\"p97-frontier\"')",
            1,
        )
    if "research.index('id=\"p99-research-map\"')" not in text and "research = _read" in text:
        text = text.replace(
            "assert research.index('id=\"p98-research-map\"') < research.index('id=\"p97-research-map\"')",
            "assert research.index('id=\"p99-research-map\"') < research.index('id=\"p98-research-map\"')\n    assert research.index('id=\"p98-research-map\"') < research.index('id=\"p97-research-map\"')",
            1,
        )
    text = text.replace('assert "Previous theorem frontier · P97" in atlas', 'assert "Previous theorem frontier · P98" in atlas')
    write(path, text)

print("[P99] public frontier promotion complete")


# P99 final publication contract pass
_P99_ROOT = Path(__file__).resolve().parents[1]

def _p99_read(relative: str) -> str:
    return (_P99_ROOT / relative).read_text(encoding="utf-8")

def _p99_write(relative: str, value: str) -> None:
    (_P99_ROOT / relative).write_text(value, encoding="utf-8")

# Preserve the P96 historical selection-valid milestone in the README.
_p99_text = _p99_read("README.md")
if "P96" not in _p99_text:
    _p99_status = "**Current theorem frontier:** P99"
    _p99_history = (
        "Historical selection-valid lineage: P96 introduced independent holdout "
        "certification after data-dependent plan selection; P97, P98, and P99 extend "
        "that line through finite candidate families, cross-fitting, and e-value aggregation.\n\n"
    )
    _p99_text = _p99_text.replace(_p99_status, _p99_history + _p99_status, 1)
    _p99_write("README.md", _p99_text)

# The current Visual Atlas block must link its theorem record as well as its figure.
_p99_text = _p99_read("website/visual-atlas.html")
_p99_start = _p99_text.index('id="p99-frontier"')
_p99_end = _p99_text.index('id="p98-frontier"', _p99_start)
_p99_segment = _p99_text[_p99_start:_p99_end]
if "proposition_99_" not in _p99_segment:
    _p99_close = _p99_segment.rfind("</section>")
    _p99_links = (
        '<p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/'
        'docs/proposition_99_cross_fitted_evalue_aggregation.md">Read Proposition 99</a> · '
        '<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/'
        'docs/p99_equation_provenance.md">P99 equation provenance</a></p>\n'
    )
    _p99_segment = _p99_segment[:_p99_close] + _p99_links + _p99_segment[_p99_close:]
    _p99_text = _p99_text[:_p99_start] + _p99_segment + _p99_text[_p99_end:]
    _p99_write("website/visual-atlas.html", _p99_text)

# Research lineage must expose the same 99-result current-stage count as the homepage.
_p99_text = _p99_read("website/research-lineage.html")
_p99_text = _p99_text.replace(
    '<strong>98</strong><span>proposition-level results</span>',
    '<strong>99</strong><span>proposition-level results</span>',
)
_p99_text = _p99_text.replace("P98 current theorem frontier", "P99 current theorem frontier")
_p99_text = _p99_text.replace("98 proposition-level results through P98", "99 proposition-level results through P99")
_p99_text = _p99_text.replace("all 98 propositions", "all 99 propositions")
_p99_write("website/research-lineage.html", _p99_text)

# Reader links that mean current frontier must follow the P99 homepage anchor.
for _p99_file in ("website/implementation.html", "website/research-map.html"):
    _p99_text = _p99_read(_p99_file)
    _p99_text = _p99_text.replace("index.html#p98-frontier", "index.html#p99-frontier")
    _p99_write(_p99_file, _p99_text)

# Keep the Research Map orientation sentence synchronized with the theorem frontier.
_p99_text = _p99_read("website/research-map.html")
_p99_text = _p99_text.replace("through Proposition 98.", "through Proposition 99.")
_p99_write("website/research-map.html", _p99_text)

print("[P99] final publication contract pass complete")
