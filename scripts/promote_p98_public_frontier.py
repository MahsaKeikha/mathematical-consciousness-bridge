"""One-time publication promotion for Proposition 98.

Advance the reader-facing and audit-facing repository state from P97 to P98
while preserving P97 as the immediate predecessor. This file is temporary
promotion machinery and should be removed after the promoted state is committed
and validated.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text.rstrip() + "\n", encoding="utf-8")


def replace(text: str, old: str, new: str) -> str:
    return text.replace(old, new) if old in text else text


# Changelog.
path = "CHANGELOG.md"
text = read(path)
if not text.startswith("# Unreleased research frontier - P98"):
    text = """# Unreleased research frontier - P98

## P98 cross-fitted selection-valid certification frontier

- Added Proposition 98 as the rotated independent-block extension of P96 holdout selection validity.
- Allowed every independent block to serve once as certification information and elsewhere as selection information, while forbidding a fold from using its own certification statistics to choose the plan later tested on that fold.
- Combined fold-level P96 guarantees with exact rational fold budgets and one outer union bound; no independence between the final fold certificates is assumed.
- Certified the balanced K=2, B=2, m=1, 95 percent crossing at 4045 observations per regime and first exact denominator-24 replication at 4056.
- Recorded 8090/8112 observations per certification fold and 16180/16224 unique observations across two genuinely distinct folds.
- Preserved the boundary that arbitrary splits of a dependent stream, own-fold leakage, unbudgeted cross-fitting search, model acceptance, consciousness identification, nonphysicality, and bridge completion remain open.
- Kept formal release v0.82.0 separate from the advancing theorem frontier.

""" + text
write(path, text)

# Citation metadata.
path = "CITATION.bib"
text = read(path)
text = text.replace("Current documented theorem frontier: P97.", "Current documented theorem frontier: P98.")
write(path, text)

path = "CITATION.cff"
text = read(path)
if "Proposition 98 rotates independent holdout certification" not in text:
    text = text.replace(
        " Current documented theorem frontier: P97. The physical-to-experiential bridge remains open",
        " Proposition 98 rotates independent holdout certification across mutually independent data blocks: each fold selects its plan using only the other blocks, freezes that plan before its own certification block is inspected, and combines fold-level P96 guarantees with an outer exact error budget and union bound. Current documented theorem frontier: P98. The physical-to-experiential bridge remains open",
        1,
    )
text = text.replace("Current documented theorem frontier: P97", "Current documented theorem frontier: P98")
if "  - cross-fitted selection-valid certification\n" not in text:
    text = text.replace("  - simultaneous candidate-family selection\n", "  - simultaneous candidate-family selection\n  - cross-fitted selection-valid certification\n")
write(path, text)

path = "CITATION.md"
text = read(path)
text = text.replace("current documented frontier, P97", "current documented frontier, P98")
text = text.replace("Current documented theorem frontier: P97", "Current documented theorem frontier: P98")
text = text.replace("theorem frontier **P97**", "theorem frontier **P98**")
text = text.replace("P1 through P97 chronological theorem record", "P1 through P98 chronological theorem record")
text = text.replace("## Current theorem frontier: P97", "## Previous theorem frontier: P97")
if "## Current theorem frontier: P98" not in text:
    marker = "## DOI and archival status"
    block = """## Current theorem frontier: P98

The current documented theorem frontier is **P98**. P98 rotates the P96 independent-holdout construction across mutually independent data blocks. For fold `k`, the selected regime plan may be an arbitrarily complicated function of the other blocks, but block `k` must be excluded from its own selection rule and the plan must be frozen before block `k` is inspected for certification. Exact fold-level error budgets are then combined by a union bound, so the final fold certificates need not be independent.

For two folds with two one-step-dependent regimes each at 95 percent global confidence, the per-regime mathematical crossing is **4045**, the first exact denominator-24 replication is **4056**, and the unique-data totals are **16180 / 16224**.

P98 is a conditional model-rejection theorem. It does not validate arbitrary splits of one dependent stream, leakage of a fold into its own plan selection, unbudgeted exploration of multiple cross-fitting schemes, model acceptance after non-rejection, consciousness identification, nonphysicality, or completion of the physical-to-experiential bridge.

"""
    text = text.replace(marker, block + marker, 1)
if "P98 rotates the P96" not in text:
    marker = "These remain conditional statistical target-measurement results, not validation of an experiential ontology or a privileged consciousness label."
    para = "P98 rotates the P96 holdout principle across mutually independent data blocks. Each block is excluded from its own plan-selection rule, every fold receives an exact failure budget, and an outer union bound makes the rotated certificates simultaneous without assuming they are independent. P98 does not validate arbitrary dependent-stream splitting, own-fold leakage, unbudgeted cross-fitting search, model acceptance, consciousness identification, nonphysicality, or bridge completion.\n\n"
    text = text.replace(marker, para + marker, 1)
write(path, text)

# Glossary and chronological record.
path = "docs/glossary.md"
text = read(path)
text = text.replace("The current public frontier is **P97**.", "The current public frontier is **P98**.")
text = text.replace("## Current theorem frontier: P97", "## Immediate predecessor theorem frontier: P97")
if "## Current theorem frontier: P98" not in text:
    text += """

## Current theorem frontier: P98

**Cross-fitted certification block:** one of several mutually independent data blocks used as certification information in exactly one fold while the complementary blocks may be used for that fold's plan selection.

**Own-fold exclusion:** the requirement that fold `k` cannot use certification statistics from block `k` to choose the plan later certified on block `k`.

**Rotated holdout:** the P98 design in which each independent block takes a turn as the held-out certification block and may serve as selection information for other folds.

**Fold-level error budget:** the exact rational failure budget `beta_k` assigned to fold `k`. The P98 simultaneous guarantee requires the fold budgets to sum to no more than the global error budget.

**P98 boundary:** ordinary splitting of one dependent stream does not create independent certification blocks. Own-fold leakage, misspecified dependence, unrestricted within-regime drift, unbudgeted exploration of cross-fitting schemes, model acceptance, consciousness identification, nonphysicality, and completion of the physical-to-experiential bridge are not established.
"""
write(path, text)

path = "docs/detailed_proposition_record.md"
text = read(path)
text = text.replace("Complete P1 to P97 chronology", "Complete P1 to P98 chronology")
text = text.replace("97 disconnected proposition-level results", "98 disconnected proposition-level results")
if "## P98: Cross-Fitted Selection-Valid Certification" not in text:
    text += """

## P98: Cross-Fitted Selection-Valid Certification

**Question.** Can the P96 independent-holdout principle be rotated so every genuinely independent data block contributes to final certification somewhere, without allowing a fold to select and certify its own plan on the same information?

**Result.** Yes. Let mutually independent blocks `D_1,...,D_K` be given. For fold `k`, the selected P95/P96 regime plan may be an arbitrary function of the other blocks but must exclude `D_k` from its own selection information and be frozen before `D_k` is evaluated. P96 then gives a fold-level failure probability bounded by `beta_k`. When `sum_k beta_k <= alpha`, a union bound yields one simultaneous event of confidence at least `1-alpha` for all rotated fold certificates. The fold certificates themselves need not be independent.

For two folds, two regimes per fold, dependence range one, and equal 5 percent global spending, the local budget is `1/80`, the first mathematical crossing is 4045 observations per regime, and the first exact denominator-24 replication is 4056. Each certification fold therefore uses 8090 or 8112 observations, and the two-fold unique-data totals are 16180 or 16224.

**Boundary.** P98 requires genuinely independent certification blocks and own-fold exclusion. A random partition of one dependent time series is not automatically valid. Misspecified dependence ranges, unrestricted within-regime drift, unbudgeted exploration of multiple cross-fitting schemes, model acceptance, consciousness identification, nonphysicality, and completion of the physical-to-experiential bridge remain open.

Direct proof: [P98](proposition_98_cross_fitted_selection_valid_certification.md). Provenance: [P98 equation record](p98_equation_provenance.md). Implementation: [`cross_fitted_selection_valid_certification.py`](../src/consciousness_bridge/cross_fitted_selection_valid_certification.py). Tests: [`test_cross_fitted_selection_valid_certification.py`](../tests/test_cross_fitted_selection_valid_certification.py).
"""
write(path, text)

# Research map and navigation.
path = "docs/research_map.md"
text = read(path)
text = text.replace("The public theorem frontier is **P97**", "The public theorem frontier is **P98**")
text = text.replace(
    "If you want the current result itself, open **[P97](proposition_97_simultaneous_candidate_family_selection.md)**.",
    "If you want the current result itself, open **[P98](proposition_98_cross_fitted_selection_valid_certification.md)**. For the previous finite same-data family frontier, open **[P97](proposition_97_simultaneous_candidate_family_selection.md)**."
)
if "## P98: cross-fitted selection-valid certification" not in text:
    text += """

## P98: cross-fitted selection-valid certification

P98 returns to the P96 independent-holdout principle and rotates it across several mutually independent blocks. In fold `k`, the plan may be learned by any procedure using the other blocks, but block `k` is excluded from its own selection information and is used only after the plan is frozen.

Each fold therefore receives a valid P96 certificate with failure budget `beta_k`. The fold certificates may be dependent because their selection information overlaps. P98 does not multiply their probabilities; it combines their unconditional failure bounds with one union bound. Any post-inspection selected fold remains valid on the simultaneous event.

For two folds, two regimes per fold, and one-step dependence, the 95 percent per-regime crossing remains 4045 and the first exact replication remains 4056. Unlike P97, the folds are genuinely different certification blocks, so the unique-data totals are 16180 and 16224.

P98 does not justify splitting one dependent stream and calling the pieces independent, using a fold's own certification statistics to choose its plan, unbudgeted exploration of many cross-fitting schemes, model acceptance after non-rejection, consciousness identification, nonphysicality, or completion of the physical-to-experiential bridge.
"""
write(path, text)

path = "docs/research_navigation.md"
text = read(path)
text = text.replace("The current documented theorem frontier is **P97**.", "The current documented theorem frontier is **P98**.")
text = text.replace("**Results:** P75 through P97", "**Results:** P75 through P98")
text = text.replace("P74 through P97", "P74 through P98")
text = text.replace("P71 through P97", "P71 through P98")
text = text.replace("full 97 proposition index", "full 98 proposition index")
text = text.replace("## P97 current frontier", "## P97 previous frontier")
if "For P98:" not in text:
    marker = "## Audit the current frontier without searching folders\n\nFor P97:"
    block = """## Audit the current frontier without searching folders

For P98:

| Audit surface | Canonical route |
| --- | --- |
| Direct theorem | [P98 proposition](proposition_98_cross_fitted_selection_valid_certification.md) |
| Equation and method provenance | [P98 provenance](p98_equation_provenance.md) |
| Implementation | [`cross_fitted_selection_valid_certification.py`](../src/consciousness_bridge/cross_fitted_selection_valid_certification.py) |
| Regression tests | [`test_cross_fitted_selection_valid_certification.py`](../tests/test_cross_fitted_selection_valid_certification.py) |
| Theorem figure | [P98 cross-fitted certificate](figures/p98_cross_fitted_selection_valid_certification.svg) |
| Repository reproduction | [Reproducibility Guide](reproducibility.md) |

P98 is a conditional rotated-holdout theorem. It requires mutually independent certification blocks, own-fold exclusion from selection, frozen fold plans, and exact fold-level error accounting. The final fold certificates may be dependent.

---

For P97 (previous frontier):"""
    text = text.replace(marker, block, 1)
if "## P98 current frontier" not in text:
    text += """

## P98 current frontier

**Current frontier:** [P98: Cross-Fitted Selection-Valid Certification](proposition_98_cross_fitted_selection_valid_certification.md)

| What you want | Direct link |
| --- | --- |
| The theorem and proof | [P98 proposition](proposition_98_cross_fitted_selection_valid_certification.md) |
| Equation and method provenance | [P98 provenance](p98_equation_provenance.md) |
| Implementation | [`cross_fitted_selection_valid_certification.py`](../src/consciousness_bridge/cross_fitted_selection_valid_certification.py) |
| Regression tests | [`test_cross_fitted_selection_valid_certification.py`](../tests/test_cross_fitted_selection_valid_certification.py) |
| Figure | [P98 cross-fitted certificate](figures/p98_cross_fitted_selection_valid_certification.svg) |

P98 rotates independent holdout certification across mutually independent blocks. Every block may contribute to selection for other folds and to certification in its own fold, but no fold may use its own certification statistics to choose the plan later tested on that fold.
"""
write(path, text)

# Theorem roadmap.
path = "docs/theorem_roadmap.md"
text = read(path)
text = text.replace("The current documented theorem frontier is **P97**.", "The current documented theorem frontier is **P98**.")
text = text.replace("P1 through P97 with explicit dependency branches", "P1 through P98 with explicit dependency branches")
text = text.replace("P71-P97 return to the core P19 bridge-sufficiency lineage", "P71-P98 return to the core P19 bridge-sufficiency lineage")
if "P98: rotated independent-block holdouts" not in text:
    text = text.replace(
        "&\\text{P97: finite predeclared candidate families support same-data selection by simultaneous error accounting}\\\\\n",
        "&\\text{P97: finite predeclared candidate families support same-data selection by simultaneous error accounting}\\\\\n&\\Downarrow\\\\\n&\\text{P98: rotated independent-block holdouts support cross-fitted selection-valid certification}\\\\\n",
        1,
    )
if "## P98: cross-fitted selection-valid certification" not in text:
    marker = "## After P97"
    section = """## P98: cross-fitted selection-valid certification

P98 rotates the P96 selection-certification separation across `K` mutually independent data blocks. For fold `k`, the selected plan `Pi_k` may depend arbitrarily on the other blocks but not on the certification block `D_k` itself. Thus

\\[
D_k \\perp S_k,
\\]

and P96 gives a fold-level event `A_k` with

\\[
\\Pr(A_k^c) \\le \\beta_k.
\\]

The final fold certificates need not be independent because their selection information overlaps. If

\\[
\\sum_{k=1}^{K} \\beta_k \\le \\alpha,
\\]

then the union bound gives

\\[
\\Pr\\left(\\bigcap_{k=1}^{K} A_k\\right) \\ge 1-\\alpha.
\\]

For two folds, two regimes per fold, dependence range one, and equal 5 percent spending, the per-regime threshold is 4045 and the first exact denominator-24 replication is 4056. Each certification fold uses 8090 or 8112 observations, while the two-fold unique totals are 16180 or 16224.

Direct proof: [P98](proposition_98_cross_fitted_selection_valid_certification.md). Provenance: [P98 equation record](p98_equation_provenance.md). Implementation: [`cross_fitted_selection_valid_certification.py`](../src/consciousness_bridge/cross_fitted_selection_valid_certification.py). Tests: [`test_cross_fitted_selection_valid_certification.py`](../tests/test_cross_fitted_selection_valid_certification.py).

P98 does not validate dependent-stream pseudo-folds, own-fold leakage, misspecified dependence, unrestricted within-regime drift, unbudgeted cross-fitting search, model acceptance, consciousness identification, nonphysicality, or bridge completion.

## After P98"""
    text = text.replace(marker, section, 1)
text = text.replace("Any P98 candidate must close", "Any P99 candidate must close")
write(path, text)

# Reproducibility guide.
path = "docs/reproducibility.md"
text = read(path)
text = text.replace("Run only the current P97 theorem checks | focused P97 commands below", "Run only the current P98 theorem checks | focused P98 commands below")
text = text.replace("The current public theorem frontier is **P97**.", "The current public theorem frontier is **P98**.")
pattern = re.compile(r"## 5\. Focused audit of the current P97 frontier.*?\n---\n\n## 6\.", re.DOTALL)
replacement = """## 5. Focused audit of the current P98 frontier

The current theorem frontier is **P98**.

Its direct technical record is:

```text
docs/proposition_98_cross_fitted_selection_valid_certification.md
docs/p98_equation_provenance.md
src/consciousness_bridge/cross_fitted_selection_valid_certification.py
tests/test_cross_fitted_selection_valid_certification.py
docs/figures/p98_cross_fitted_selection_valid_certification.svg
figures/manifest.json
```

Run the focused theorem and publication checks with:

```bash
python -m pytest -q \\
  tests/test_cross_fitted_selection_valid_certification.py \\
  tests/test_p98_reader_surface_coherence.py \\
  tests/test_p97_reader_surface_coherence.py \\
  tests/test_frontier_reader_narrative.py \\
  tests/test_figure_publication_sync.py \\
  tests/test_frontier_publication_consistency.py
python scripts/sync_figure_publication.py --check
python scripts/verify_repository.py
```

P98 rotates P96 holdout validity across genuinely independent blocks. Each fold excludes its own certification block from plan selection, and an outer exact fold budget plus union bound makes all rotated certificates simultaneous.

For two folds with two one-step-dependent regimes each, the 95 percent per-regime threshold is `4045`, first exact replication is `4056`, and the unique-data totals are `16180` and `16224`.

A random partition of one dependent stream is not automatically a valid cross-fitted design. Own-fold leakage, unbudgeted scheme search, model acceptance, consciousness identification, nonphysicality, and bridge completion remain outside P98.

---

## 6."""
text = pattern.sub(replacement, text, count=1)
text = text.replace("docs/figures/p97_simultaneous_candidate_family_selection.svg", "docs/figures/p98_cross_fitted_selection_valid_certification.svg", 1)
write(path, text)

# Provenance indexes.
path = "docs/equation_and_citation_map.md"
text = read(path)
if "## P98 cross-fitted selection-valid certification" not in text:
    text += """

## P98 cross-fitted selection-valid certification

- Theorem: [`proposition_98_cross_fitted_selection_valid_certification.md`](proposition_98_cross_fitted_selection_valid_certification.md)
- Equation and novelty provenance: [`p98_equation_provenance.md`](p98_equation_provenance.md)
- Implementation: [`cross_fitted_selection_valid_certification.py`](../src/consciousness_bridge/cross_fitted_selection_valid_certification.py)
- Exact tests: [`test_cross_fitted_selection_valid_certification.py`](../tests/test_cross_fitted_selection_valid_certification.py)
- Figure: [`p98_cross_fitted_selection_valid_certification.svg`](figures/p98_cross_fitted_selection_valid_certification.svg)

P98 uses standard conditional holdout validity, the tower property, sample rotation, and a union bound. The repository-specific contribution is the exact integration of those ingredients with the P92-P96 sign-coherence chain, explicit own-fold exclusion, exact rational fold and regime budgets, and the executable 4045/4056 and 16180/16224 checkpoints.
"""
write(path, text)

path = "docs/claim_source_matrix.md"
text = read(path)
if "### P98 current frontier" not in text:
    text += """

### P98 current frontier

| Claim | Evidence class | Canonical source |
| --- | --- | --- |
| Mutually independent blocks can rotate between selection and certification when each fold excludes its own certification block from its own plan selection | Theorem under declared assumptions | [`proposition_98_cross_fitted_selection_valid_certification.md`](proposition_98_cross_fitted_selection_valid_certification.md) |
| Two folds, two regimes, `m=1`, equal 5 percent global spending give 4045/4056 per regime and 16180/16224 unique observations | Exact rational computation | [`test_cross_fitted_selection_valid_certification.py`](../tests/test_cross_fitted_selection_valid_certification.py) |
| P98 does not validate dependent-stream pseudo-folds, own-fold leakage, or a consciousness ontology | Scientific boundary | [`p98_equation_provenance.md`](p98_equation_provenance.md) |
"""
write(path, text)

# Verifier.
path = "scripts/verify_repository.py"
text = read(path)
text = text.replace('CURRENT_FRONTIER = "P97"', 'CURRENT_FRONTIER = "P98"')
if '"docs/proposition_98_cross_fitted_selection_valid_certification.md"' not in text:
    marker = '    "tests/test_p97_reader_surface_coherence.py",\n'
    addition = marker + '    "docs/proposition_98_cross_fitted_selection_valid_certification.md",\n    "docs/p98_equation_provenance.md",\n    "docs/figures/p98_cross_fitted_selection_valid_certification.svg",\n    "src/consciousness_bridge/cross_fitted_selection_valid_certification.py",\n    "tests/test_cross_fitted_selection_valid_certification.py",\n    "tests/test_p98_reader_surface_coherence.py",\n'
    text = text.replace(marker, addition, 1)
if '"Current theorem frontier · P97"' not in text:
    text = text.replace(
        "STALE_READER_FRONTIER_MARKERS = (\n",
        "STALE_READER_FRONTIER_MARKERS = (\n    \"Current theorem frontier · P97\",\n    \"current P97 frontier\",\n    \"<strong>P97</strong><span>current theorem frontier</span>\",\n    \"97 results · current frontier P97\",\n    \"Explore all 97 results\",\n",
        1,
    )
write(path, text)

# Figure publication summary.
path = "scripts/sync_figure_publication.py"
text = read(path)
if "if frontier == 98:" not in text:
    marker = "    return []\n\n\ndef _frontier_page"
    block = '''    if frontier == 98:
        return [
            "### Exact P98 cross-fitted selection-valid certification",
            "",
            "P98 rotates the P96 independent-holdout principle across mutually independent certification blocks while preserving own-fold exclusion from plan selection.",
            "",
            "```text",
            "fold budgets: sum_k beta_k <= alpha",
            "inside fold k: sum_b alpha_kb <= beta_k",
            "K=2 folds, B=2 regimes, m=1: local alpha = 1/80",
            "95% mathematical crossing = 4045 per regime",
            "first exact denominator-24 replication = 4056 per regime",
            "per-fold totals = 8090 / 8112",
            "cross-fitted unique totals = 16180 / 16224",
            "```",
            "",
            "P98 requires genuinely independent certification blocks and no own-fold leakage. The final fold certificates may be dependent; validity is combined by an outer union bound. Dependent-stream pseudo-folds, unbudgeted scheme search, model acceptance, consciousness identification, nonphysicality, and bridge completion are not established.",
            "",
        ]
    return []


def _frontier_page'''
    text = text.replace(marker, block, 1)
write(path, text)

# README.
path = "README.md"
text = read(path)
text = text.replace("The current public theorem frontier is **P97**.", "The current public theorem frontier is **P98**.")
text = text.replace("docs/proposition_97_simultaneous_candidate_family_selection.md", "docs/proposition_98_cross_fitted_selection_valid_certification.md", 1)
text = re.sub(
    r"### Current theorem frontier\n\n.*?\n## Choose your path",
    """### Current theorem frontier

![P98 Cross-Fitted Selection-Valid Certification](docs/figures/p98_cross_fitted_selection_valid_certification.svg)

**Figure 2. P98 cross-fitted selection-valid certification.** P98 rotates the P96 holdout principle across mutually independent data blocks. In fold `k`, an arbitrary plan may be learned from the other blocks, but block `k` is excluded from its own selection rule and is inspected only after the fold plan is frozen. P96 then supplies a fold-level guarantee, and one outer union bound controls the complete set of rotated certificates without assuming that the final fold certificates are independent.

For two folds with two one-step-dependent regimes each at 95 percent global confidence, the per-regime crossing is **4045**, the first exact denominator-24 replication is **4056**, each certification fold contains **8090 / 8112** observations, and the two-fold unique-data totals are **16180 / 16224**.

P98 does not justify treating arbitrary pieces of one dependent stream as independent folds, using a fold's own certification statistics to choose the plan later tested on that fold, unbudgeted exploration of many cross-fitting schemes, accepting P75 after non-rejection, identifying consciousness, establishing nonphysicality, or closing the physical-to-experiential bridge.

## Choose your path""",
    text,
    count=1,
    flags=re.DOTALL,
)
text = text.replace("**Public theorem frontier:** P97", "**Public theorem frontier:** P98")
write(path, text)

# START_HERE markdown.
path = "START_HERE.md"
text = read(path)
text = text.replace("The public theorem frontier is **P97**.", "The public theorem frontier is **P98**.")
text = text.replace("read 97 propositions", "read 98 propositions")
text = text.replace("**[P97](docs/proposition_97_simultaneous_candidate_family_selection.md)**", "**[P98](docs/proposition_98_cross_fitted_selection_valid_certification.md)**")
if "### P98: cross-fitted selection-valid certification" not in text:
    text += """

### P98: cross-fitted selection-valid certification

P98 rotates the P96 independent-holdout idea across mutually independent blocks. Each fold may choose its regime plan using the other blocks, but its own certification block is excluded from that selection and is evaluated only after the plan is frozen. The fold certificates are allowed to be dependent; an outer union bound controls their total error budget.

For two folds with two one-step-dependent regimes each, the 95 percent per-regime threshold is 4045 and the first exact denominator-24 replication is 4056. Because the folds are genuinely different certification blocks, the unique totals are 16180 and 16224.

P98 does not make an ordinary split of a dependent time series independent. It does not permit own-fold leakage, unbudgeted cross-fitting search, model acceptance after non-rejection, consciousness identification, nonphysicality, or completion of the physical-to-experiential bridge. [Read P98](docs/proposition_98_cross_fitted_selection_valid_certification.md).
"""
write(path, text)

# Website overview.
path = "website/index.html"
text = read(path)
text = text.replace('<strong>97</strong><span>proposition-level results</span>', '<strong>98</strong><span>proposition-level results</span>')
text = text.replace('P97 current theorem frontier · v0.82.0', 'P98 current theorem frontier · v0.82.0')
text = text.replace('Explore all 97 results', 'Explore all 98 results')
text = text.replace('97 proposition-level results through P97', '98 proposition-level results through P98')
text = text.replace('The 97 results form several dependency branches.', 'The 98 results form several dependency branches.')
text = text.replace('The 97-result program is summarized here; <a href="research-map.html">all 97 propositions</a>', 'The 98-result program is summarized here; <a href="research-map.html">all 98 propositions</a>')
p98_home = '''<!-- current-frontier-home: P98 -->
<section id="p98-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head">
    <p class="eyebrow">Research II · Current theorem frontier · P98</p>
    <h2>Cross-fitted selection-valid certification</h2>
    <p>P98 rotates independent holdout certification across mutually independent data blocks. Each fold may learn an arbitrarily complicated regime plan from the other blocks, but its own certification block is excluded from that selection and is evaluated only after the plan is frozen.</p>
  </div>
  <div class="theorem-figure-shell"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p98_cross_fitted_selection_valid_certification.svg"><img loading="eager" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p98_cross_fitted_selection_valid_certification.svg" alt="P98 cross-fitted selection-valid certification" /></a></div>
  <div class="frontier-summary-grid">
    <article class="frontier-summary-card"><h3>Every independent block certifies once</h3><p>Block k can help select plans for other folds, but it is held out from its own fold's selection rule.</p></article>
    <article class="frontier-summary-card"><h3>Fold certificates may be dependent</h3><p>Overlapping selection information is allowed. P98 combines unconditional fold error bounds with one outer union bound instead of assuming independence.</p></article>
    <article class="frontier-summary-card"><h3>Exact balanced checkpoint</h3><p>For K=2, B=2, and m=1, the crossing is <strong>4045 per regime</strong>; exact replication is <strong>4056</strong>; unique totals are <strong>16180 / 16224</strong>.</p></article>
  </div>
  <div class="boundary"><p><strong>Scientific boundary:</strong> independent certification blocks and own-fold exclusion are essential. A random split of one dependent stream is not automatically valid. Own-fold leakage, unbudgeted cross-fitting search, model acceptance, consciousness identification, nonphysicality, and bridge completion are not established.</p></div>
  <p><a href="research-map.html">Research II map</a> · <a href="visual-atlas.html">Theorem figures</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_98_cross_fitted_selection_valid_certification.md">P98 theorem</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p98_equation_provenance.md">P98 provenance</a></p>
</section>

'''
text = re.sub(r'<!-- current-frontier-home: P97 -->.*?(?=<section id="research-iii-overview">)', p98_home, text, count=1, flags=re.DOTALL)
write(path, text)

# Plain-language and Start Here website surfaces.
p98_reader = '''<section class="boundary" id="p98-reader-frontier"><div class="section-head"><p class="eyebrow">Research II · Current frontier · P98</p><h2>Cross-fitting can reuse every independent block without letting a fold select on its own certification evidence</h2><p>P98 rotates the P96 holdout principle. For each fold, the plan may be learned from the other independent blocks, but the fold's own certification block is excluded from its plan-selection rule and is inspected only after the plan is frozen. The fold certificates may be dependent because their selection information overlaps; one outer union bound keeps them simultaneous.</p></div><p><strong>Exact balanced checkpoint:</strong> two folds, two regimes per fold, and one-step dependence give 4045 observations per regime at 95 percent global confidence, first exact replication at 4056, and unique-data totals 16180 / 16224.</p><p><strong>Boundary:</strong> a random split of one dependent stream is not automatically an independent cross-fitted design. Own-fold leakage, unbudgeted scheme search, model acceptance, consciousness identification, nonphysicality, and the physical-to-experiential bridge remain open.</p></section>

'''
for path in ("website/plain-language.html", "website/start-here.html"):
    text = read(path)
    text = text.replace("97 results · current frontier P97", "98 results · current frontier P98")
    text = text.replace("current Research II P97 frontier", "current Research II P98 frontier")
    text = text.replace("The 97 Research II propositions by scientific role", "The 98 Research II propositions by scientific role")
    text = text.replace("97-result proposition program", "98-result proposition program")
    text = text.replace("complete 97-result Research II dependency structure", "complete 98-result Research II dependency structure")
    text = text.replace("Open all 97 Research II results", "Open all 98 Research II results")
    if 'id="p98-reader-frontier"' not in text:
        marker = '<section class="boundary" id="p97-reader-frontier">'
        text = text.replace(marker, p98_reader + marker, 1)
    text = text.replace("Research II · Current frontier · P97", "Research II · Previous frontier · P97")
    write(path, text)

# Research Map website.
path = "website/research-map.html"
text = read(path)
text = text.replace("through Proposition 97.", "through Proposition 98.")
text = text.replace("Ninety-seven results", "Ninety-eight results")
for old, new in (("P71-P97", "P71-P98"), ("P74-P97", "P74-P98"), ("P73-P97", "P73-P98"), ("P77-P97", "P77-P98"), ("P75-P97", "P75-P98")):
    text = text.replace(old, new)
text = text.replace("The current theorem frontier is P97.", "The current theorem frontier is P98.")
text = text.replace("Research Map · Current theorem frontier P97", "Research Map · Current theorem frontier P98")
p98_map = '''<section class="result" id="p98-research-map"><span>P98</span><h3>P98: Can every independent block contribute to certification without leaking into its own plan selection?</h3><p>Yes. In fold k, the plan may be learned from the other mutually independent blocks, but block k is excluded from its own plan-selection rule and is certified only after the plan is frozen. Fold-level P96 guarantees receive exact budgets beta_k, and one outer union bound makes all rotated fold certificates simultaneous without assuming those certificates are independent.</p><p><strong>Exact balanced checkpoint:</strong> K=2 folds, B=2 regimes, and m=1 give 4045 observations per regime, first exact replication at 4056, 8090 / 8112 observations per certification fold, and 16180 / 16224 unique observations overall.</p><p><strong>Boundary:</strong> dependent-stream pseudo-folds, own-fold leakage, unbudgeted cross-fitting search, model acceptance, consciousness identification, nonphysicality, and bridge completion remain open.</p><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_98_cross_fitted_selection_valid_certification.md">Read P98 theorem</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p98_equation_provenance.md">P98 equation provenance</a> · <a href="index.html#p98-frontier">Overview P98 frontier</a></p></section>

'''
if 'id="p98-research-map"' not in text:
    marker = '<section class="result" id="p97-research-map">'
    text = text.replace(marker, p98_map + marker, 1)
text = text.replace("Continue to the current P97 frontier", "Continue to the current P98 frontier")
text = text.replace("index.html#p97-frontier", "index.html#p98-frontier", 1)
text = text.replace("visual-atlas.html#p97-frontier", "visual-atlas.html#p98-frontier", 1)
text = text.replace("See the P97 figure", "See the P98 figure", 1)
text = text.replace("docs/p97_equation_provenance.md", "docs/p98_equation_provenance.md", 1)
text = text.replace("Audit P97 provenance", "Audit P98 provenance", 1)
write(path, text)

# Visual Atlas.
path = "website/visual-atlas.html"
text = read(path)
p98_atlas = '''<!-- current-frontier-visual: P98 -->
<section id="p98-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head"><p class="eyebrow">Current theorem frontier · P98</p><h2>Cross-fitted selection-valid certification</h2><p>P98 rotates P96 independent holdout validity across mutually independent blocks. Each fold excludes its own certification block from plan selection, while the final fold certificates are combined by exact error budgets and one union bound.</p></div>
  <div class="theorem-figure-shell"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p98_cross_fitted_selection_valid_certification.svg"><img loading="eager" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p98_cross_fitted_selection_valid_certification.svg" alt="P98 cross-fitted selection-valid certification" /></a></div>
  <p><strong>Exact checkpoint:</strong> K=2, B=2, m=1 gives 4045 per regime, exact replication at 4056, and unique-data totals 16180 / 16224.</p>
  <p><strong>Boundary:</strong> genuinely independent blocks and own-fold exclusion are essential. Dependent-stream pseudo-folds, own-fold leakage, unbudgeted scheme search, model acceptance, consciousness identification, nonphysicality, and bridge completion remain open.</p>
  <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_98_cross_fitted_selection_valid_certification.md">Proof</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p98_equation_provenance.md">Equation provenance</a></p>
</section>

'''
if '<!-- current-frontier-visual: P98 -->' not in text:
    marker = '<!-- current-frontier-visual: P97 -->'
    text = text.replace(marker, p98_atlas, 1)
text = text.replace('<!-- current-frontier-visual: P97 -->\n', '')
text = text.replace("Current theorem frontier · P97", "Previous theorem frontier · P97")
text = text.replace("Previous theorem frontier · P96", "Historical theorem frontier · P96")
write(path, text)

# Source and implementation pages.
path = "website/sources.html"
text = read(path)
if 'id="p98-source"' not in text:
    marker = '<section id="p97-source">'
    source = '''<section id="p98-source"><div class="section-head"><p class="eyebrow">Current theorem source · P98</p><h2>Cross-fitted selection-valid certification</h2><p>P98 rotates independent holdout certification across mutually independent blocks. Each fold excludes its own block from plan selection and is covered by an exact fold-level error budget.</p></div><div class="source-grid"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_98_cross_fitted_selection_valid_certification.md"><h3>Proposition 98</h3><p>Formal rotated-holdout theorem, exact checkpoint, and scientific boundary.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p98_equation_provenance.md"><h3>P98 provenance</h3><p>Separates standard cross-fitting, tower-property, and union-bound ingredients from repository-specific integration.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/cross_fitted_selection_valid_certification.py"><h3>P98 implementation</h3><p>Executable own-fold exclusion, exact fold budgets, nested P96 certificates, and balanced thresholds.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_cross_fitted_selection_valid_certification.py"><h3>P98 exact tests</h3><p>Independent-block guards, leakage rejection, post-inspection fold selection, and exact checkpoints.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p98_cross_fitted_selection_valid_certification.svg"><h3>P98 theorem figure</h3><p>Canonical rotated independent-block certification diagram.</p></a></div><div class="boundary"><p><strong>Scientific boundary:</strong> arbitrary dependent-stream partitions and own-fold leakage are outside P98. Non-rejection remains inconclusive, and consciousness identification, nonphysicality, and bridge completion are not established.</p></div></section>

'''
    text = text.replace(marker, source + marker, 1)
text = text.replace("Current theorem source · P97", "Immediate predecessor theorem source · P97")
write(path, text)

path = "website/implementation.html"
text = read(path)
text = text.replace("Stage 06 · P73-P97", "Stage 06 · P73-P98")
text = text.replace("P73-P97 build a continuous chain", "P73-P98 build a continuous chain")
text = text.replace("index.html#p97-frontier", "index.html#p98-frontier")
text = text.replace("current P97 frontier", "current P98 frontier")
if "P98 rotates" not in text:
    text = text.replace(
        "P97 then permits same-data post-inspection selection within a finite candidate family fixed before certification statistics are inspected, paying an explicit candidate-level multiplicity cost.",
        "P97 then permits same-data post-inspection selection within a finite candidate family fixed before certification statistics are inspected, paying an explicit candidate-level multiplicity cost. P98 rotates P96 independent holdout certification across mutually independent blocks so every block can serve once as certification information while remaining excluded from its own fold's selection rule."
    )
write(path, text)

# Update P97 coherence test so it remains a historical-predecessor contract.
path = "tests/test_p97_reader_surface_coherence.py"
text = read(path)
text = text.replace("def test_p97_is_current_reader_frontier()", "def test_p97_is_preserved_as_previous_reader_frontier()")
text = text.replace("assert 'CURRENT_FRONTIER = \"P97\"' in verifier", "assert 'CURRENT_FRONTIER = \"P98\"' in verifier")
text = text.replace("assert '<!-- current-frontier-home: P97 -->' in home", "assert 'id=\"p98-frontier\"' in home")
text = text.replace("assert \"Current theorem frontier · P97\" in home", "assert \"Current theorem frontier · P98\" in home")
text = text.replace("assert \"Explore all 97 results\" in home", "assert \"Explore all 98 results\" in home")
text = text.replace("assert '<!-- current-frontier-visual: P97 -->' in atlas", "assert '<!-- current-frontier-visual: P98 -->' in atlas")
text = text.replace("assert atlas.index('id=\"p97-frontier\"') < atlas.index('id=\"p96-frontier\"')", "assert atlas.index('id=\"p98-frontier\"') < atlas.index('id=\"p97-frontier\"')")
text = text.replace("assert \"Previous theorem frontier · P96\" in atlas", "assert \"Previous theorem frontier · P97\" in atlas")
text = text.replace("assert \"97 results · current frontier P97\" in plain", "assert \"98 results · current frontier P98\" in plain")
text = text.replace("assert \"97 results · current frontier P97\" in start", "assert \"98 results · current frontier P98\" in start")
text = text.replace("assert research.index('id=\"p97-research-map\"') < research.index('id=\"p96-research-map\"')", "assert research.index('id=\"p98-research-map\"') < research.index('id=\"p97-research-map\"')")
text = text.replace("assert \"Current Research II model-audit range: P75-P97.\" in research", "assert \"Current Research II model-audit range: P75-P98.\" in research")
text = text.replace("assert \"The current theorem frontier is P97.\" in research", "assert \"The current theorem frontier is P98.\" in research")
text = text.replace("def test_p97_repository_audit_surfaces_are_synchronized()", "def test_p97_repository_audit_surfaces_preserve_predecessor()")
text = text.replace("assert \"The current public theorem frontier is **P97**.\" in readme", "assert \"The current public theorem frontier is **P98**.\" in readme")
text = text.replace("assert \"The current documented theorem frontier is **P97**.\" in roadmap", "assert \"The current documented theorem frontier is **P98**.\" in roadmap")
text = text.replace("assert \"P1 through P97 with explicit dependency branches\" in roadmap", "assert \"P1 through P98 with explicit dependency branches\" in roadmap")
text = text.replace("assert \"## After P97\" in roadmap", "assert \"## P98: cross-fitted selection-valid certification\" in roadmap")
text = text.replace("assert \"The current documented theorem frontier is **P97**.\" in navigation", "assert \"The current documented theorem frontier is **P98**.\" in navigation")
text = text.replace("assert \"**Results:** P75 through P97\" in navigation", "assert \"**Results:** P75 through P98\" in navigation")
text = text.replace("assert \"The current public theorem frontier is **P97**.\" in reproducibility", "assert \"The current public theorem frontier is **P98**.\" in reproducibility")
text = text.replace("assert \"## 5. Focused audit of the current P97 frontier\" in reproducibility", "assert \"## 5. Focused audit of the current P98 frontier\" in reproducibility")
text = text.replace("assert \"## Current theorem frontier: P97\" in citation", "assert \"## Current theorem frontier: P98\" in citation")
write(path, text)

print("[p98-promotion] reader, audit, citation, and website surfaces advanced")
