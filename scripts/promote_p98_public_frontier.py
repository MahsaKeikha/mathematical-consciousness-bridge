"""One-time publication promotion for Proposition 98.

This migration advances the public theorem frontier from P97 to P98 while
preserving P97 as the immediate predecessor. It is temporary promotion machinery
and should be removed after the promoted state is committed and validated.
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


def prepend_once(text: str, marker: str, block: str, *, identity: str) -> str:
    if identity in text:
        return text
    if marker not in text:
        raise RuntimeError(f"insertion marker not found: {marker!r}")
    return text.replace(marker, block + marker, 1)


# Changelog.
path = "CHANGELOG.md"
text = read(path)
if "# Unreleased research frontier - P98" not in text:
    block = """# Unreleased research frontier - P98

## P98 cross-fitted selection-valid certification frontier

- Added Proposition 98 as the rotated independent-block extension of P96 selection-valid holdout certification.
- Allowed every independent block to serve once as certification information and as selection information for the other folds, while forbidding own-fold leakage.
- Combined fold-level P96 guarantees with exact fold budgets and a union bound; cross-fitted fold certificates need not be independent.
- Certified the balanced K=2, B=2, m=1, 95 percent per-regime crossing at 4045 observations and first exact denominator-24 replication at 4056.
- Recorded unique cross-fitted observation totals 16180 and 16224, with each opposite block reused as selection information rather than counted again.
- Preserved the boundary that dependent-stream splitting, own-fold leakage, unbudgeted repeated cross-fitting, model acceptance, consciousness identification, nonphysicality, and bridge completion remain open.
- Kept formal release v0.82.0 separate from the advancing theorem frontier.

"""
    text = block + text
write(path, text)

# Citation metadata.
path = "CITATION.bib"
text = read(path)
text = replace(text, "Current documented theorem frontier: P97.", "Current documented theorem frontier: P98.")
write(path, text)

path = "CITATION.cff"
text = read(path)
if "Proposition 98 rotates" not in text:
    text = text.replace(
        " Current documented theorem frontier: P97. The physical-to-experiential bridge remains open",
        " Proposition 98 rotates P96-style selection/certification separation across mutually independent blocks: each fold selects its plan using only the other blocks, freezes the plan before evaluating its own certification block, and receives an exact fold-level error budget. A union bound across folds gives one simultaneous cross-fitted guarantee without assuming the fold certificates are independent. Current documented theorem frontier: P98. The physical-to-experiential bridge remains open",
        1,
    )
text = text.replace("Current documented theorem frontier: P97", "Current documented theorem frontier: P98")
if "  - cross-fitted certification\n" not in text:
    text = text.replace("  - simultaneous candidate-family selection\n", "  - simultaneous candidate-family selection\n  - cross-fitted certification\n")
write(path, text)

path = "CITATION.md"
text = read(path)
text = text.replace("current documented frontier, P97", "current documented frontier, P98")
text = text.replace("Current documented theorem frontier: P97", "Current documented theorem frontier: P98")
text = text.replace("theorem frontier **P97**", "theorem frontier **P98**")
text = text.replace("P1 through P97 chronological theorem record", "P1 through P98 chronological theorem record")
if "## Current theorem frontier: P98" not in text:
    marker = "## DOI and archival status"
    block = """## Current theorem frontier: P98

The current documented theorem frontier is **P98**. P98 rotates P96-style selection-valid holdout certification across mutually independent blocks. Each fold may choose an arbitrarily complicated plan from the other blocks, but its own certification block is excluded from that selection information and the plan is frozen before evaluation. Exact fold-level error budgets are combined by a union bound, so the cross-fitted certificates remain simultaneously valid even though their selection information overlaps.

P98 is a conditional model-rejection theorem. It does not justify ordinary dependent-stream splitting, own-fold leakage, repeated unbudgeted cross-fitting, model acceptance after non-rejection, consciousness identification, nonphysicality, or completion of the physical-to-experiential bridge.

"""
    text = text.replace(marker, block + marker, 1)
if "P98 rotates P96" not in text:
    marker = "These remain conditional statistical target-measurement results, not validation of an experiential ontology or a privileged consciousness label."
    paragraph = "P98 rotates P96-style selection-valid holdout certification across mutually independent blocks. Every block serves once as certification information and may serve as selection information for the other folds. Fold certificates are covered simultaneously by exact error-budget accounting and a union bound; they need not be independent. P98 does not validate own-fold leakage, naive splitting of one dependent stream, model acceptance, consciousness identification, nonphysicality, or bridge completion.\n\n"
    text = text.replace(marker, paragraph + marker, 1)
write(path, text)

# README and Start Here.
path = "README.md"
text = read(path)
text = text.replace("The current public theorem frontier is **P97**.", "The current public theorem frontier is **P98**.")
text = text.replace("[Read the current frontier](docs/proposition_97_simultaneous_candidate_family_selection.md)", "[Read the current frontier](docs/proposition_98_cross_fitted_selection_valid_certification.md)")
text = text.replace("**Public theorem frontier:** P97", "**Public theorem frontier:** P98")
if "![P98 Cross-Fitted Selection-Valid Certification]" not in text:
    pattern = re.compile(r"### Current theorem frontier\n\n!\[P97.*?\n\nP97 does not.*?physical-to-experiential bridge\.\n", re.DOTALL)
    block = """### Current theorem frontier

![P98 Cross-Fitted Selection-Valid Certification](docs/figures/p98_cross_fitted_selection_valid_certification.svg)

**Figure 2. P98 cross-fitted selection-valid certification.** P98 rotates the P96 separation between selection and certification across mutually independent data blocks. In fold `k`, the plan may be chosen arbitrarily from all other blocks, but block `k` itself is excluded from the selection information and the plan is frozen before its certification statistics are inspected. P96 supplies fold-level validity, while a second union bound across exact fold budgets gives one simultaneous cross-fitted guarantee without assuming the fold certificates are independent.

For two folds, two regimes per fold, one-step dependence, and a 5 percent global error budget, the local regime budget is **1/80**. The exact mathematical crossing remains **4045 observations per regime**, with first denominator-24 replication at **4056**. Each certification block therefore contains **8090 / 8112** observations, and the unique cross-fitted totals are **16180 / 16224**.

P98 does not justify letting a fold use its own certification statistics to choose its plan, treating adjacent pieces of one dependent stream as independent blocks, repeated unbudgeted cross-fitting followed by selective reporting, model acceptance after non-rejection, identifying consciousness, establishing nonphysicality, or closing the physical-to-experiential bridge.
"""
    text, count = pattern.subn(lambda _: block, text, count=1)
    if count != 1:
        raise RuntimeError("README current frontier block not found")
write(path, text)

path = "START_HERE.md"
text = read(path)
text = text.replace("The public theorem frontier is **P97**.", "The public theorem frontier is **P98**.")
text = text.replace("read 97 propositions", "read 98 propositions")
text = text.replace("**[P97](docs/proposition_97_simultaneous_candidate_family_selection.md)**", "**[P98](docs/proposition_98_cross_fitted_selection_valid_certification.md)**")
if "### P98: cross-fitted selection-valid certification" not in text:
    text += """

### P98: cross-fitted selection-valid certification

P98 rotates P96's selection/holdout separation across mutually independent blocks. For fold `k`, the regime plan may be learned from all other blocks, but block `k` is excluded from its own selection information and the plan is frozen before certification. P96 gives the fold-level guarantee; a union bound across exact fold budgets makes all folds simultaneously valid even though their selection information overlaps. [Read P98](docs/proposition_98_cross_fitted_selection_valid_certification.md).

For two folds with two one-step-dependent regimes each, equal spending of a 5 percent global error budget gives 4045 observations per regime for the mathematical crossing and 4056 for the first exact denominator-24 replication. Unique cross-fitted data totals are 16180 and 16224. P98 does not justify own-fold leakage, naive splitting of one dependent stream, unbudgeted repeated cross-fitting, model acceptance, consciousness identification, nonphysicality, or completion of the physical-to-experiential bridge.
"""
write(path, text)

# Glossary and proposition archive.
path = "docs/glossary.md"
text = read(path)
text = text.replace("The current public frontier is **P97**.", "The current public frontier is **P98**.")
text = text.replace("## Current theorem frontier: P97", "## Immediate predecessor theorem frontier: P97")
if "## Current theorem frontier: P98" not in text:
    text += """

## Current theorem frontier: P98

**Cross-fitted certification block:** one independent data block that is held out from the selection information for its own fold and used once for final certification.

**Own-fold exclusion:** the requirement that fold `k` may not use certification statistics from block `k` to choose the plan later certified on block `k`.

**Fold-level error budget:** the exact rational failure budget assigned to one cross-fitted certification statement. The fold budgets must sum to at most the global error budget.

**Cross-fold dependence:** P98 does not assume the final fold certificates are independent. Their selection information overlaps by construction; simultaneous validity is obtained by a union bound.

**P98 boundary:** adjacent pieces of a dependent stream are not automatically independent blocks. Own-fold leakage, misspecified dependence, repeated unbudgeted cross-fitting, model acceptance under non-rejection, consciousness identification, nonphysicality, and bridge completion remain outside the theorem.
"""
write(path, text)

path = "docs/detailed_proposition_record.md"
text = read(path)
text = text.replace("Complete P1 to P97 chronology", "Complete P1 to P98 chronology")
text = text.replace("97 disconnected proposition-level results", "98 disconnected proposition-level results")
if "## P98: Cross-Fitted Selection-Valid Certification" not in text:
    text += """

## P98: Cross-Fitted Selection-Valid Certification

**Question.** Can P96's selection/certification separation be rotated across independent blocks so every block contributes to certification somewhere without sacrificing post-selection validity?

**Result.** Yes. For fold `k`, the selected regime plan may be any function of the other mutually independent blocks, but its own certification block is excluded from the selection information and the plan is frozen before evaluation. P96 supplies the fold-level conditional guarantee. Exact fold budgets `beta_k` satisfying `sum_k beta_k <= alpha` are then combined by a union bound, so all fold certificates are simultaneously valid even though their selection information overlaps. Post-inspection fold selection is therefore valid on the simultaneous event.

For `K=2`, two regimes per fold, dependence range one, and equal division of a 5 percent global budget, the per-regime mathematical threshold is 4045 and the first exact denominator-24 replication is 4056. Each fold contains 8090 / 8112 certification observations, giving unique cross-fitted totals 16180 / 16224.

**Boundary.** P98 requires genuinely independent certification blocks and forbids own-fold leakage. It does not validate naive splitting of one dependent stream, unbudgeted repeated cross-fitting, model acceptance, consciousness identification, nonphysicality, or completion of the physical-to-experiential bridge.

Direct proof: [P98](proposition_98_cross_fitted_selection_valid_certification.md). Provenance: [P98 equation record](p98_equation_provenance.md). Implementation: [`cross_fitted_selection_valid_certification.py`](../src/consciousness_bridge/cross_fitted_selection_valid_certification.py). Tests: [`test_cross_fitted_selection_valid_certification.py`](../tests/test_cross_fitted_selection_valid_certification.py).
"""
write(path, text)

# Research maps and navigation.
path = "docs/research_map.md"
text = read(path)
text = text.replace("The public theorem frontier is **P97**", "The public theorem frontier is **P98**")
text = text.replace("If you want the current result itself, open **[P97](proposition_97_simultaneous_candidate_family_selection.md)**.", "If you want the current result itself, open **[P98](proposition_98_cross_fitted_selection_valid_certification.md)**. For the previous finite-candidate same-data frontier, open **[P97](proposition_97_simultaneous_candidate_family_selection.md)**.")
if "## P98: cross-fitted selection-valid certification" not in text:
    text += """

## P98: cross-fitted selection-valid certification

P98 returns to the P96 sample-separation idea, but rotates it across mutually independent data blocks so every block contributes to certification once. Fold `k` may select an arbitrarily complicated regime plan from the other blocks. Its own block is excluded from that selection information, the plan is frozen, and P96 then certifies the fold on its own block.

The fold certificates are generally dependent because their selection information overlaps. P98 therefore does not multiply fold probabilities. It allocates exact fold-level error budgets and applies a union bound, producing one simultaneous event on which every cross-fitted certificate is valid.

For two folds with two one-step-dependent regimes each, the 95 percent per-regime threshold is 4045 and the first exact denominator-24 replication is 4056. Unique cross-fitted data totals are 16180 and 16224.

P98 does not justify own-fold leakage, treating adjacent pieces of one dependent stream as independent blocks, repeated unbudgeted cross-fitting, model acceptance under non-rejection, consciousness identification, nonphysicality, or completion of the physical-to-experiential bridge.
"""
write(path, text)

path = "docs/research_navigation.md"
text = read(path)
text = text.replace("The current documented theorem frontier is **P97**.", "The current documented theorem frontier is **P98**.")
text = text.replace("**Results:** P75 through P97", "**Results:** P75 through P98")
text = text.replace("**Current frontier:** [P97: Simultaneous Finite Candidate-Family Selection](proposition_97_simultaneous_candidate_family_selection.md)", "**Current frontier:** [P98: Cross-Fitted Selection-Valid Certification](proposition_98_cross_fitted_selection_valid_certification.md)")
text = text.replace("P74 through P97", "P74 through P98")
text = text.replace("P71 through P97", "P71 through P98")
text = text.replace("full 97 proposition index", "full 98 proposition index")
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

P98 is a conditional cross-fitted model-audit result. Every fold's certification block must be genuinely independent of the information used to select that fold's plan. Fold certificates may still be mutually dependent; the simultaneous guarantee uses exact error budgets and a union bound.

---

For P97 (previous frontier):"""
    text = text.replace(marker, block, 1)
text = text.replace("## P97 current frontier", "## P97 previous frontier")
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

P98 rotates P96's independent-holdout logic across mutually independent blocks. Every block is used once for certification and may be reused as selection information in other folds, while exact fold budgets and a union bound preserve simultaneous validity.
"""
write(path, text)

path = "docs/theorem_roadmap.md"
text = read(path)
text = text.replace("The current documented theorem frontier is **P97**.", "The current documented theorem frontier is **P98**.")
text = text.replace("P1 through P97 with explicit dependency branches", "P1 through P98 with explicit dependency branches")
text = text.replace("P71-P97 return to the core P19 bridge-sufficiency lineage", "P71-P98 return to the core P19 bridge-sufficiency lineage")
if "P98: rotated independent blocks" not in text:
    text = text.replace(
        "&\\text{P97: finite predeclared candidate families support same-data selection by simultaneous error accounting}\\\\\n",
        "&\\text{P97: finite predeclared candidate families support same-data selection by simultaneous error accounting}\\\\\n&\\Downarrow\\\\\n&\\text{P98: rotated independent blocks support cross-fitted selection-valid certification}\\\\\n",
        1,
    )
if "## P98: cross-fitted selection-valid certification" not in text:
    marker = "## After P97"
    section = """## P98: cross-fitted selection-valid certification

P98 rotates the P96 selection/certification separation across mutually independent blocks. For fold `k`, the plan is selected from information contained only in the other blocks and frozen before block `k` is evaluated. P96 therefore gives a fold-level failure probability at most `beta_k`.

With exact budgets satisfying

\\[
\\sum_{k=1}^{K}\\beta_k \\le \\alpha,
\\]

no independence among the final fold certificates is required. A union bound gives

\\[
\\Pr\\left(\\bigcap_{k=1}^{K}\\mathcal A_k\\right) \\ge 1-\\alpha.
\\]

Any fold may then be selected after inspection because every fold certificate is already covered on the simultaneous event.

For `K=2`, two regimes per fold, dependence range one, and equal spending of a 5 percent global budget, the local error budget is `1/80`. The per-regime crossing is 4045, the first exact denominator-24 replication is 4056, the per-fold totals are 8090 / 8112, and the unique cross-fitted totals are 16180 / 16224.

Direct proof: [P98](proposition_98_cross_fitted_selection_valid_certification.md). Provenance: [P98 equation record](p98_equation_provenance.md). Implementation: [`cross_fitted_selection_valid_certification.py`](../src/consciousness_bridge/cross_fitted_selection_valid_certification.py). Tests: [`test_cross_fitted_selection_valid_certification.py`](../tests/test_cross_fitted_selection_valid_certification.py).

P98 does not validate own-fold leakage, naive splitting of a dependent stream, repeated unbudgeted cross-fitting, model acceptance, consciousness identification, nonphysicality, or bridge completion.

## After P98"""
    text = text.replace(marker, section, 1)
text = text.replace("Any P98 candidate must close", "Any P99 candidate must close")
write(path, text)

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

P98 rotates P96-style independent holdout certification across mutually independent blocks. Each fold excludes its own certification block from plan selection, freezes the selected plan, and is covered by an exact fold-level budget. A union bound across folds makes all cross-fitted certificates simultaneous without requiring fold independence.

For two folds with two one-step-dependent regimes each, the 95 percent threshold is `4045` per regime, the first exact denominator-24 replication is `4056`, and the unique cross-fitted totals are `16180 / 16224`.

Own-fold leakage and naive splitting of one dependent stream remain outside the theorem. Non-rejection is not model acceptance, and P98 does not identify consciousness, establish nonphysicality, or close the physical-to-experiential bridge.

---

## 6."""
text, count = pattern.subn(lambda _: replacement, text, count=1)
if count != 1 and "## 5. Focused audit of the current P98 frontier" not in text:
    raise RuntimeError("P97 reproducibility frontier section not found")
text = text.replace("docs/figures/p97_simultaneous_candidate_family_selection.svg", "docs/figures/p98_cross_fitted_selection_valid_certification.svg")
write(path, text)

# Claim and equation maps.
path = "docs/claim_source_matrix.md"
text = read(path)
if "### P98 current frontier" not in text:
    text += """

### P98 current frontier

| Claim | Evidence class | Canonical source |
| --- | --- | --- |
| Mutually independent blocks support rotated leave-one-block-out selection-valid certification when every fold excludes its own block from plan selection | Theorem under declared assumptions | [P98 proof](proposition_98_cross_fitted_selection_valid_certification.md) |
| Fold certificates need not be independent; exact fold budgets plus a union bound provide simultaneous coverage | Theorem under declared assumptions | [P98 provenance](p98_equation_provenance.md) |
| `K=2`, `B=2`, `m=1` crosses at 4045 per regime, first exact replicate 4056, with unique totals 16180 / 16224 | Exact rational computation | [`test_cross_fitted_selection_valid_certification.py`](../tests/test_cross_fitted_selection_valid_certification.py) |
| P98 does not validate own-fold leakage, dependent-stream splitting, or consciousness ontology | Scientific boundary | [P98 proof](proposition_98_cross_fitted_selection_valid_certification.md) |
"""
write(path, text)

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

P98 combines standard conditional/sample-splitting logic, P96 fold-level certification, and a standard union bound across exact fold budgets. The project-specific contribution is the explicit rotated-block theorem, exact certificate object, scientific guard conditions, and 4045/4056 with 16180/16224 reproducible checkpoints.
"""
write(path, text)

# Repository verifier.
path = "scripts/verify_repository.py"
text = read(path)
text = text.replace('CURRENT_FRONTIER = "P97"', 'CURRENT_FRONTIER = "P98"')
if '"docs/proposition_98_cross_fitted_selection_valid_certification.md"' not in text:
    marker = '    "tests/test_p97_reader_surface_coherence.py",\n'
    addition = marker + '    "docs/proposition_98_cross_fitted_selection_valid_certification.md",\n    "docs/p98_equation_provenance.md",\n    "docs/figures/p98_cross_fitted_selection_valid_certification.svg",\n    "src/consciousness_bridge/cross_fitted_selection_valid_certification.py",\n    "tests/test_cross_fitted_selection_valid_certification.py",\n    "tests/test_p98_reader_surface_coherence.py",\n'
    text = text.replace(marker, addition, 1)
if '"Current theorem frontier · P97",' not in text:
    marker = "STALE_READER_FRONTIER_MARKERS = (\n"
    addition = marker + '    "Current theorem frontier · P97",\n    "current P97 frontier",\n    "<strong>P97</strong><span>current theorem frontier</span>",\n    "97 results · current frontier P97",\n    "Explore all 97 results",\n'
    text = text.replace(marker, addition, 1)
write(path, text)

# Figure publication summary.
path = "scripts/sync_figure_publication.py"
text = read(path)
if "if frontier == 98:" not in text:
    marker = "    return []\n"
    block = """    if frontier == 98:
        return [
            "### Exact P98 cross-fitted selection-valid certification",
            "",
            "P98 rotates P96-style selection/holdout separation across mutually independent data blocks. Every block serves once as certification information and may serve as selection information for the other folds.",
            "",
            "```text",
            "fold budgets: sum_k beta_k <= alpha",
            "inside fold k: sum_b alpha_kb <= beta_k",
            "K=2, B=2, m=1: local alpha = 1/80",
            "95% mathematical crossing = 4045 per regime",
            "first exact denominator-24 replication = 4056 per regime",
            "per-fold totals = 8090 / 8112",
            "unique cross-fitted totals = 16180 / 16224",
            "```",
            "",
            "P98 requires genuinely independent certification blocks and own-fold exclusion from plan selection. Naive dependent-stream splitting, own-fold leakage, unbudgeted repeated cross-fitting, model acceptance, consciousness identification, nonphysicality, and bridge completion are not established.",
            "",
        ]
"""
    text = text.replace(marker, block + marker, 1)
write(path, text)

# Update P97 reader test so it remains a predecessor contract under P98.
path = "tests/test_p97_reader_surface_coherence.py"
text = read(path)
text = text.replace("def test_p97_is_current_reader_frontier() -> None:", "def test_p97_is_previous_reader_frontier() -> None:")
text = text.replace("assert 'CURRENT_FRONTIER = \"P97\"' in verifier", "assert 'CURRENT_FRONTIER = \"P98\"' in verifier")
text = text.replace("assert '<!-- current-frontier-home: P97 -->' in home", "assert 'id=\"p97-frontier\"' in home")
text = text.replace("assert \"Current theorem frontier · P97\" in home", "assert \"P97\" in home")
text = text.replace("assert \"Explore all 97 results\" in home", "assert \"Explore all 98 results\" in home")
text = text.replace("assert '<!-- current-frontier-visual: P97 -->' in atlas", "assert '<!-- current-frontier-visual: P98 -->' in atlas")
text = text.replace("assert atlas.index('id=\"p97-frontier\"') < atlas.index('id=\"p96-frontier\"')", "assert atlas.index('id=\"p98-frontier\"') < atlas.index('id=\"p97-frontier\"')")
text = text.replace("assert \"Previous theorem frontier · P96\" in atlas", "assert \"Previous theorem frontier · P97\" in atlas")
text = text.replace("assert \"97 results · current frontier P97\" in plain", "assert \"98 results · current frontier P98\" in plain")
text = text.replace("assert \"97 results · current frontier P97\" in start", "assert \"98 results · current frontier P98\" in start")
text = text.replace("assert research.index('id=\"p97-research-map\"') < research.index('id=\"p96-research-map\"')", "assert research.index('id=\"p98-research-map\"') < research.index('id=\"p97-research-map\"')")
text = text.replace("assert \"Current Research II model-audit range: P75-P97.\" in research", "assert \"Current Research II model-audit range: P75-P98.\" in research")
text = text.replace("assert \"The current theorem frontier is P97.\" in research", "assert \"The current theorem frontier is P98.\" in research")
text = text.replace("assert \"The current public theorem frontier is **P97**.\" in readme", "assert \"The current public theorem frontier is **P98**.\" in readme")
text = text.replace("assert \"The current documented theorem frontier is **P97**.\" in roadmap", "assert \"The current documented theorem frontier is **P98**.\" in roadmap")
text = text.replace("assert \"P1 through P97 with explicit dependency branches\" in roadmap", "assert \"P1 through P98 with explicit dependency branches\" in roadmap")
text = text.replace("assert \"## After P97\" in roadmap", "assert \"## P98: cross-fitted selection-valid certification\" in roadmap")
text = text.replace("assert \"The current documented theorem frontier is **P97**.\" in navigation", "assert \"The current documented theorem frontier is **P98**.\" in navigation")
text = text.replace("assert \"**Results:** P75 through P97\" in navigation", "assert \"**Results:** P75 through P98\" in navigation")
text = text.replace("assert \"For P97:\" in navigation", "assert \"For P98:\" in navigation")
text = text.replace("assert \"The current public theorem frontier is **P97**.\" in reproducibility", "assert \"The current public theorem frontier is **P98**.\" in reproducibility")
text = text.replace("assert \"## 5. Focused audit of the current P97 frontier\" in reproducibility", "assert \"## 5. Focused audit of the current P98 frontier\" in reproducibility")
text = text.replace("assert \"## Current theorem frontier: P97\" in citation", "assert \"## Current theorem frontier: P98\" in citation")
write(path, text)

# Website overview.
path = "website/index.html"
text = read(path)
text = text.replace("<strong>97</strong><span>proposition-level results</span>", "<strong>98</strong><span>proposition-level results</span>")
text = text.replace("P97 current theorem frontier · v0.82.0", "P98 current theorem frontier · v0.82.0")
text = text.replace("Explore all 97 results →", "Explore all 98 results →")
text = text.replace("97 proposition-level results through P97", "98 proposition-level results through P98")
text = text.replace("The 97-result program", "The 98-result program")
text = text.replace("all 97 propositions", "all 98 propositions")
if '<!-- current-frontier-home: P98 -->' not in text:
    marker = '<!-- current-frontier-home: P97 -->\n'
    block = """<!-- current-frontier-home: P98 -->
<section id="p98-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head">
    <p class="eyebrow">Research II · Current theorem frontier · P98</p>
    <h2>Cross-fitted selection-valid certification</h2>
    <p>P98 rotates P96's independent selection/certification separation across mutually independent data blocks. Every fold selects its plan from the other blocks, freezes that plan, and certifies only on its own excluded block.</p>
  </div>
  <div class="theorem-figure-shell"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p98_cross_fitted_selection_valid_certification.svg"><img loading="eager" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p98_cross_fitted_selection_valid_certification.svg" alt="P98 cross-fitted selection-valid certification" /></a></div>
  <div class="frontier-summary-grid">
    <article class="frontier-summary-card"><h3>Every block contributes</h3><p>Each independent block is used once for certification and may be reused as selection information for the other folds.</p></article>
    <article class="frontier-summary-card"><h3>No fold-independence fiction</h3><p>Cross-fitted certificates may be dependent because selection information overlaps. Exact fold budgets plus a union bound provide simultaneous validity.</p></article>
    <article class="frontier-summary-card"><h3>Exact balanced checkpoint</h3><p>K=2, B=2, m=1 gives <strong>4045 per regime</strong>, first exact replication <strong>4056</strong>, and unique totals <strong>16180 / 16224</strong>.</p></article>
  </div>
  <div class="boundary"><p><strong>Scientific boundary:</strong> certification blocks must be genuinely independent of their own fold's selection information. Own-fold leakage, naive dependent-stream splitting, unbudgeted repeated cross-fitting, model acceptance, consciousness identification, nonphysicality, and bridge completion are not established.</p></div>
  <p><a href="research-map.html">Research II map</a> · <a href="visual-atlas.html">Theorem figures</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_98_cross_fitted_selection_valid_certification.md">P98 theorem</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p98_equation_provenance.md">P98 provenance</a></p>
</section>

"""
    text = text.replace(marker, block + '<!-- previous-frontier-home: P97 -->\n', 1)
text = text.replace("Research II · Current theorem frontier · P97", "Research II · Previous theorem frontier · P97")
write(path, text)

# Plain-language and Start Here website pages.
for path in ("website/plain-language.html", "website/start-here.html"):
    text = read(path)
    text = text.replace("97 results · current frontier P97", "98 results · current frontier P98")
    text = text.replace("97-result", "98-result")
    text = text.replace("97 propositions", "98 propositions")
    text = text.replace("97 Research II", "98 Research II")
    text = text.replace("P1-P97", "P1-P98")
    text = text.replace("P75-P97", "P75-P98")
    text = text.replace("Open all 97 Research II results", "Open all 98 Research II results")
    if 'id="p98-reader-frontier"' not in text:
        marker = '<section class="boundary" id="p97-reader-frontier">'
        block = """<section class="boundary" id="p98-reader-frontier"><div class="section-head"><p class="eyebrow">Research II · Current frontier · P98</p><h2>Every independent block can contribute to certification without leaking into its own plan selection</h2><p>P98 rotates P96's sample-separation idea across mutually independent blocks. Fold k chooses its plan from the other blocks, freezes the plan, and is certified only on block k. Exact fold budgets are combined by a union bound, so all cross-fitted certificates remain valid simultaneously even though their selection information overlaps.</p></div><p><strong>Exact balanced checkpoint:</strong> K=2 folds, B=2 regimes per fold, m=1 gives 4045 observations per regime, first exact replication 4056, and unique totals 16180 / 16224.</p><p><strong>Boundary:</strong> own-fold leakage, naive splitting of a dependent stream, unbudgeted repeated cross-fitting, model acceptance, consciousness identification, nonphysicality, and the physical-to-experiential bridge remain open.</p><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_98_cross_fitted_selection_valid_certification.md">Read P98 theorem</a></p></section>

"""
        text = text.replace(marker, block + marker, 1)
    text = text.replace("Research II · Current frontier · P97", "Research II · Previous frontier · P97")
    write(path, text)

# Research Map website.
path = "website/research-map.html"
text = read(path)
text = text.replace("through Proposition 97", "through Proposition 98")
text = text.replace("Ninety-seven results", "Ninety-eight results")
text = text.replace("P71-P97", "P71-P98")
text = text.replace("Current Research II model-audit range: P75-P97.", "Current Research II model-audit range: P75-P98.")
text = text.replace("The current theorem frontier is P97.", "The current theorem frontier is P98.")
text = text.replace("<strong>97</strong><span>proposition-level results</span>", "<strong>98</strong><span>proposition-level results</span>")
text = text.replace("<strong>P97</strong><span>current theorem frontier</span>", "<strong>P98</strong><span>current theorem frontier</span>")
text = text.replace("P74-P97", "P74-P98")
text = text.replace("P73-P97", "P73-P98")
text = text.replace("P77-P97", "P77-P98")
text = text.replace("index.html#p97-frontier", "index.html#p98-frontier")
text = text.replace("visual-atlas.html#p97-frontier", "visual-atlas.html#p98-frontier")
if 'id="p98-research-map"' not in text:
    marker = '<section class="result" id="p97-research-map">'
    block = """<section class="result" id="p98-research-map"><span>P98</span><h3>P98: Can selection-valid certification be cross-fitted so every independent block contributes?</h3><p>Yes under a strict leave-one-block-out design. Fold k selects its regime plan only from the other mutually independent blocks, freezes the plan, and certifies on block k. Exact fold budgets are combined by a union bound, so all fold certificates remain simultaneous even though their selection information overlaps.</p><p><strong>Exact balanced checkpoint:</strong> K=2 folds, B=2 regimes, and m=1 give 4045 observations per regime, first exact denominator-24 replication at 4056, per-fold totals 8090 / 8112, and unique cross-fitted totals 16180 / 16224.</p><p><strong>Boundary:</strong> own-fold leakage, naive dependent-stream splitting, repeated unbudgeted cross-fitting, model acceptance, consciousness identification, nonphysicality, and bridge completion remain open.</p><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_98_cross_fitted_selection_valid_certification.md">Read P98 theorem</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p98_equation_provenance.md">P98 equation provenance</a> · <a href="index.html#p98-frontier">Overview P98 frontier</a></p></section>

"""
    text = text.replace(marker, block + marker, 1)
text = text.replace("Current theorem frontier P97", "Current theorem frontier P98")
write(path, text)

# Visual Atlas.
path = "website/visual-atlas.html"
text = read(path)
if '<!-- current-frontier-visual: P98 -->' not in text:
    marker = '<!-- current-frontier-visual: P97 -->\n'
    block = """<!-- current-frontier-visual: P98 -->
<section id="p98-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head"><p class="eyebrow">Current theorem frontier · P98</p><h2>Cross-fitted selection-valid certification</h2><p>P98 rotates independent selection/certification separation across mutually independent blocks. Each fold is selected without its own certification block, then exact fold budgets are combined by a union bound.</p></div>
  <div class="theorem-figure-shell"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p98_cross_fitted_selection_valid_certification.svg"><img loading="eager" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p98_cross_fitted_selection_valid_certification.svg" alt="P98 cross-fitted selection-valid certification" /></a></div>
  <p><strong>Exact checkpoint:</strong> K=2, B=2, m=1 gives 4045 per regime, exact replication 4056, and unique totals 16180 / 16224.</p>
  <p><strong>Boundary:</strong> mutually independent certification blocks and own-fold exclusion are essential. Naive dependent-stream splitting, own-fold leakage, model acceptance, consciousness identification, nonphysicality, and bridge completion remain open.</p>
  <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_98_cross_fitted_selection_valid_certification.md">Proof</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p98_equation_provenance.md">Equation provenance</a></p>
</section>

"""
    text = text.replace(marker, block + '<!-- previous-frontier-visual: P97 -->\n', 1)
text = text.replace("Current theorem frontier · P97", "Previous theorem frontier · P97")
write(path, text)

# Lightweight updates to supporting website pages.
for path in ("website/implementation.html", "website/sources.html", "website/research-lineage.html"):
    text = read(path)
    text = text.replace("P75-P97", "P75-P98")
    text = text.replace("P71-P97", "P71-P98")
    text = text.replace("current theorem frontier P97", "current theorem frontier P98")
    text = text.replace("Current theorem frontier P97", "Current theorem frontier P98")
    if "P98" not in text:
        text += "\n<!-- P98 cross-fitted selection-valid certification is the current Research II theorem frontier. -->\n"
    write(path, text)
