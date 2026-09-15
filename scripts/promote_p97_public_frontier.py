"""One-time publication promotion for Proposition 97.

This migration advances the reader-facing and audit-facing repository state from
P96 to P97 while preserving P96 as the immediate predecessor. It is temporary
promotion machinery and should be removed after the generated/publication state
is committed and validated.
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


# Citation metadata.
path = "CITATION.bib"
text = read(path)
text = replace(text, "Current documented theorem frontier: P96.", "Current documented theorem frontier: P97.")
write(path, text)

path = "CITATION.cff"
text = read(path)
if "Proposition 97 permits same-data selection" not in text:
    text = text.replace(
        " Current documented theorem frontier: P96. The physical-to-experiential bridge remains open",
        " Proposition 97 permits same-data selection among a finite predeclared family of candidate regime plans by allocating exact candidate-level error budgets, applying P95 within every candidate, and taking a second union bound across candidates so all candidate certificates remain simultaneously valid before post-inspection selection. Current documented theorem frontier: P97. The physical-to-experiential bridge remains open",
        1,
    )
text = text.replace("Current documented theorem frontier: P96", "Current documented theorem frontier: P97")
if "  - simultaneous candidate-family selection\n" not in text:
    text = text.replace("  - experimental design\n", "  - experimental design\n  - simultaneous candidate-family selection\n")
write(path, text)

path = "CITATION.md"
text = read(path)
text = text.replace("current documented frontier, P96", "current documented frontier, P97")
text = text.replace("Current documented theorem frontier: P96", "Current documented theorem frontier: P97")
text = text.replace("theorem frontier **P96**", "theorem frontier **P97**")
text = text.replace("P1 through P96 chronological theorem record", "P1 through P97 chronological theorem record")
if "P97 complements P96" not in text:
    marker = "These remain conditional statistical target-measurement results, not validation of an experiential ontology or a privileged consciousness label."
    paragraph = (
        "P97 complements P96 by covering a finite same-data selection problem. The complete candidate family must be fixed before certification statistics are inspected. Each candidate receives an exact P95 familywise budget, and a second union bound across candidates makes all candidate certificates simultaneous. The final candidate may then be selected after inspection without invalidating the selected certificate. P97 does not cover newly generated post-inspection candidates, unrestricted candidate families, model acceptance, consciousness identification, nonphysicality, or bridge completion.\n\n"
    )
    if marker in text:
        text = text.replace(marker, paragraph + marker, 1)
write(path, text)

# Glossary and chronological archive.
path = "docs/glossary.md"
text = read(path)
text = text.replace("The current public frontier is **P96**.", "The current public frontier is **P97**.")
text = text.replace("## Current theorem frontier: P96", "## Immediate predecessor theorem frontier: P96")
if "## Current theorem frontier: P97" not in text:
    text += """

## Current theorem frontier: P97

**Finite candidate family:** a complete list of candidate regime plans fixed before the certification statistics are inspected. P97 permits post-inspection selection only from this predeclared finite family.

**Candidate-level error budget:** the exact rational failure budget assigned to one candidate plan. Inside that candidate, P95 divides or otherwise allocates the candidate budget across its regimes.

**Simultaneous candidate certificate:** the event on which every candidate-specific P95 certificate is valid at once. P97 obtains it by a union bound across candidates, so the candidate certificates may reuse the same observations and may be statistically dependent.

**Same-data selection cost:** unlike P96, P97 does not require a separate pilot sample. It pays instead through multiplicity: the global error budget is split across the predeclared candidates.

**P97 boundary:** a candidate created after inspecting certification results is outside the theorem. Unbounded post-inspection search, unrestricted within-regime drift, model acceptance under non-rejection, consciousness identification, nonphysicality, and completion of the physical-to-experiential bridge are not established.
"""
write(path, text)

path = "docs/detailed_proposition_record.md"
text = read(path)
text = text.replace("Complete P1 to P96 chronology", "Complete P1 to P97 chronology")
text = text.replace("96 disconnected proposition-level results", "97 disconnected proposition-level results")
if "## P97: Simultaneous Finite Candidate-Family Selection" not in text:
    text += """

## P97: Simultaneous Finite Candidate-Family Selection

**Question.** Can the same certification data be used to compare candidate regime plans and then select one after inspection without invalidating the selected rejection certificate?

**Result.** Yes for a finite candidate family fixed before certification statistics are inspected. Candidate `k` receives an exact familywise budget `alpha_k`; P95 controls all regimes inside that candidate, and a second union bound controls all candidates simultaneously when `sum_k alpha_k <= alpha`. On that simultaneous event, any post-inspection selection rule restricted to the predeclared family preserves validity of the selected candidate certificate.

For two equally budgeted candidates, each with two regimes and dependence range one, the 95 percent mathematical threshold is 4045 observations per regime and the first exact denominator-24 replication is 4056. Because the candidates reuse the same underlying observations, the balanced unique-observation totals are 8090 and 8112.

**Boundary.** The candidate family itself must be fixed before inspection. Newly generated post-inspection candidates, unrestricted search, within-regime drift beyond the local assumptions, model acceptance after non-rejection, consciousness identification, nonphysicality, and completion of the physical-to-experiential bridge remain open.

Direct proof: [P97](proposition_97_simultaneous_candidate_family_selection.md). Provenance: [P97 equation record](p97_equation_provenance.md). Implementation: [`simultaneous_candidate_family_selection.py`](../src/consciousness_bridge/simultaneous_candidate_family_selection.py). Tests: [`test_simultaneous_candidate_family_selection.py`](../tests/test_simultaneous_candidate_family_selection.py).
"""
write(path, text)

# Reader maps.
path = "docs/research_map.md"
text = read(path)
text = text.replace("The public theorem frontier is **P95**", "The public theorem frontier is **P97**")
text = text.replace("P94 is the current Research II theorem frontier.", "P94 is a historical finite-range Research II step.")
text = text.replace(
    "If you want the current result itself, open **[P95](proposition_95_drift_aware_stratified_sign_coherence.md)**.",
    "If you want the current result itself, open **[P97](proposition_97_simultaneous_candidate_family_selection.md)**. For the previous independent-holdout frontier, open **[P96](proposition_96_selection_valid_holdout_stratification.md)**."
)
if "## P97: simultaneous finite candidate-family selection" not in text:
    text += """

## P97: simultaneous finite candidate-family selection

P97 addresses a complementary selection problem to P96. Instead of separating pilot and holdout data, it permits the same certification data to be reused across a finite family of candidate regime plans, provided the complete family is fixed before the certification statistics are inspected.

Each candidate receives its own exact P95 familywise error budget. A second union bound across candidates produces one simultaneous event on which every candidate certificate is valid. The final candidate may therefore be selected after inspection without invalidating the selected certificate.

For two equally budgeted candidates with two one-step-dependent regimes each, the 95 percent threshold is 4045 observations per regime, with first exact denominator-24 replication at 4056. The multiplicity cost replaces P96's sample-separation cost.

P97 does not justify creating a new candidate after inspection, unbounded same-data search, unrestricted within-regime drift, model acceptance after non-rejection, consciousness identification, nonphysicality, or completion of the physical-to-experiential bridge.
"""
write(path, text)

path = "docs/research_navigation.md"
text = read(path)
text = text.replace("The current documented theorem frontier is **P96**.", "The current documented theorem frontier is **P97**.")
text = text.replace("**Results:** P75 through P96", "**Results:** P75 through P97")
text = text.replace(
    "**Current frontier:** [P96: Selection-Valid Holdout Stratification](proposition_96_selection_valid_holdout_stratification.md)",
    "**Current frontier:** [P97: Simultaneous Finite Candidate-Family Selection](proposition_97_simultaneous_candidate_family_selection.md)"
)
text = text.replace("P74 through P96", "P74 through P97")
text = text.replace("P71 through P96", "P71 through P97")
text = text.replace("full 96 proposition index", "full 97 proposition index")
if "For P97:" not in text:
    marker = "## Audit the current frontier without searching folders\n\nFor P96:"
    block = """## Audit the current frontier without searching folders

For P97:

| Audit surface | Canonical route |
| --- | --- |
| Direct theorem | [P97 proposition](proposition_97_simultaneous_candidate_family_selection.md) |
| Equation and method provenance | [P97 provenance](p97_equation_provenance.md) |
| Implementation | [`simultaneous_candidate_family_selection.py`](../src/consciousness_bridge/simultaneous_candidate_family_selection.py) |
| Regression tests | [`test_simultaneous_candidate_family_selection.py`](../tests/test_simultaneous_candidate_family_selection.py) |
| Theorem figure | [P97 simultaneous candidate-family certificate](figures/p97_simultaneous_candidate_family_selection.svg) |
| Repository reproduction | [Reproducibility Guide](reproducibility.md) |

P97 is a conditional same-data selection-valid model-audit result for a finite candidate family fixed before certification statistics are inspected. It pays for candidate search through explicit multiplicity rather than P96 sample separation. New post-inspection candidates, unrestricted within-regime drift, model acceptance, consciousness identification, nonphysicality, and bridge completion remain outside the theorem.

---

For P96 (previous frontier):"""
    if marker in text:
        text = text.replace(marker, block, 1)
text = text.replace("## P94 immediate predecessor", "## P94 historical finite-range frontier")
text = text.replace("## P95 immediate predecessor", "## P95 historical drift-aware frontier")
text = text.replace("## P96 current frontier", "## P96 previous frontier")
text = text.replace(
    "**Current frontier:** [P96: Selection-Valid Holdout Stratification](proposition_96_selection_valid_holdout_stratification.md)",
    "**Previous frontier:** [P96: Selection-Valid Holdout Stratification](proposition_96_selection_valid_holdout_stratification.md)"
)
if "## P97 current frontier" not in text:
    text += """

## P97 current frontier

**Current frontier:** [P97: Simultaneous Finite Candidate-Family Selection](proposition_97_simultaneous_candidate_family_selection.md)

| What you want | Direct link |
| --- | --- |
| The theorem and proof | [P97 proposition](proposition_97_simultaneous_candidate_family_selection.md) |
| Equation and method provenance | [P97 provenance](p97_equation_provenance.md) |
| Implementation | [`simultaneous_candidate_family_selection.py`](../src/consciousness_bridge/simultaneous_candidate_family_selection.py) |
| Regression tests | [`test_simultaneous_candidate_family_selection.py`](../tests/test_simultaneous_candidate_family_selection.py) |
| Figure | [P97 simultaneous candidate-family certificate](figures/p97_simultaneous_candidate_family_selection.svg) |

P97 permits same-data comparison and post-inspection selection only within a finite candidate family fixed before certification statistics are inspected. It assigns exact candidate-level budgets, nests P95 within each candidate, and uses a second union bound across candidates to preserve simultaneous validity.
"""
write(path, text)

path = "docs/theorem_roadmap.md"
text = read(path)
text = text.replace("The current documented theorem frontier is **P96**.", "The current documented theorem frontier is **P97**.")
text = text.replace("P1 through P96 with explicit dependency branches", "P1 through P97 with explicit dependency branches")
text = text.replace("P71-P96 return to the core P19 bridge-sufficiency lineage", "P71-P97 return to the core P19 bridge-sufficiency lineage")
if "P97: finite predeclared candidate families" not in text:
    text = text.replace(
        "&\\text{P96: pilot-selected regime plans are frozen and certified on independent holdout information}\\\\\n",
        "&\\text{P96: pilot-selected regime plans are frozen and certified on independent holdout information}\\\\\n&\\Downarrow\\\\\n&\\text{P97: finite predeclared candidate families support same-data selection by simultaneous error accounting}\\\\\n",
        1,
    )
if "## P97: simultaneous finite candidate-family selection" not in text:
    marker = "## After P96"
    section = """## P97: simultaneous finite candidate-family selection

P96 obtains selection validity by separating pilot selection from independent holdout certification. P97 proves a complementary theorem for finite same-data search. Before inspecting certification statistics, fix a finite family of candidate regime plans indexed by `k=1,...,K`. Candidate `k` receives a familywise budget `alpha_k`, and the budgets obey

\\[
\\sum_{k=1}^{K}\\alpha_k \\le \\alpha.
\\]

Inside each candidate, P95 controls all declared regimes. Therefore candidate `k` fails with probability at most `alpha_k`. A union bound across candidates gives

\\[
\\Pr(\\text{any candidate certificate fails})
\\le
\\sum_{k=1}^{K}\\alpha_k
\\le
\\alpha.
\\]

On the simultaneous event, every candidate certificate is valid at once, so the final candidate can be selected after inspection by any rule restricted to the predeclared family.

For `K=2`, two regimes per candidate, dependence range one, and equal spending of a 5 percent global budget, the local error budget is `1/80`. The mathematical threshold is 4045 observations per regime and the first exact denominator-24 replication is 4056. Because the candidates reuse the same dataset, the balanced unique-observation totals are 8090 and 8112.

Direct proof: [P97](proposition_97_simultaneous_candidate_family_selection.md). Provenance: [P97 equation record](p97_equation_provenance.md). Implementation: [`simultaneous_candidate_family_selection.py`](../src/consciousness_bridge/simultaneous_candidate_family_selection.py). Tests: [`test_simultaneous_candidate_family_selection.py`](../tests/test_simultaneous_candidate_family_selection.py).

P97 does not validate a candidate generated after inspecting certification results, an unrestricted or infinite search without additional control, within-regime drift beyond the local assumptions, model acceptance under non-rejection, consciousness identification, nonphysicality, or bridge completion.

## After P97"""
    if marker in text:
        text = text.replace(marker, section, 1)
write(path, text)

path = "docs/reproducibility.md"
text = read(path)
text = text.replace("Run only the current P96 theorem checks | focused P95 commands below", "Run only the current P97 theorem checks | focused P97 commands below")
text = text.replace("The current public theorem frontier is **P96**.", "The current public theorem frontier is **P97**.")
pattern = re.compile(r"## 5\. Focused audit of the current P96 frontier.*?\n---\n\n## 6\.", re.DOTALL)
replacement = """## 5. Focused audit of the current P97 frontier

The current theorem frontier is **P97**.

Its direct technical record is:

```text
docs/proposition_97_simultaneous_candidate_family_selection.md
docs/p97_equation_provenance.md
src/consciousness_bridge/simultaneous_candidate_family_selection.py
tests/test_simultaneous_candidate_family_selection.py
docs/figures/p97_simultaneous_candidate_family_selection.svg
figures/manifest.json
```

Run the focused theorem and publication checks with:

```bash
python -m pytest -q \\
  tests/test_simultaneous_candidate_family_selection.py \\
  tests/test_p97_reader_surface_coherence.py \\
  tests/test_p96_reader_surface_coherence.py \\
  tests/test_frontier_reader_narrative.py \\
  tests/test_figure_publication_sync.py \\
  tests/test_frontier_publication_consistency.py
python scripts/sync_figure_publication.py --check
python scripts/verify_repository.py
```

P97 permits the same certification data to be used across a finite predeclared candidate family. Candidate-level P95 certificates are made simultaneous by a second union bound, so a final post-inspection choice within that fixed family preserves validity.

For two equally budgeted candidates with two one-step-dependent regimes each, the 95 percent threshold is `4045` observations per regime and the first exact denominator-24 replication is `4056`. The balanced unique-observation totals are `8090` and `8112` because candidate plans reuse the same data.

A new candidate generated after inspection is outside the theorem. Non-rejection remains inconclusive. P97 does not license unrestricted same-data search, identify a latent state with consciousness, establish nonphysicality, validate an alternative ontology, or close the physical-to-experiential bridge.

---

## 6."""
text = pattern.sub(replacement, text, count=1)
text = text.replace("docs/figures/p96_selection_valid_holdout_stratification.svg", "docs/figures/p97_simultaneous_candidate_family_selection.svg", 1)
write(path, text)

# Lightweight provenance indexes.
path = "docs/equation_and_citation_map.md"
text = read(path)
if "## P97 same-data finite candidate-family selection" not in text:
    text += """

## P97 same-data finite candidate-family selection

- Theorem: [`proposition_97_simultaneous_candidate_family_selection.md`](proposition_97_simultaneous_candidate_family_selection.md)
- Equation and novelty provenance: [`p97_equation_provenance.md`](p97_equation_provenance.md)
- Implementation: [`simultaneous_candidate_family_selection.py`](../src/consciousness_bridge/simultaneous_candidate_family_selection.py)
- Exact tests: [`test_simultaneous_candidate_family_selection.py`](../tests/test_simultaneous_candidate_family_selection.py)
- Figure: [`p97_simultaneous_candidate_family_selection.svg`](figures/p97_simultaneous_candidate_family_selection.svg)

P97 uses standard union-bound logic at two nested levels, but the exact integration with the P92-P95 sign-coherence chain, the candidate-family certificate object, and the 4045/4056 exact checkpoint are repository-specific constructions documented in the P97 provenance record.
"""
write(path, text)

path = "docs/claim_source_matrix.md"
text = read(path)
if "P97" not in text:
    text += """

### P97 current frontier

| Claim | Evidence class | Canonical source |
| --- | --- | --- |
| A finite candidate family fixed before inspection can support same-data post-inspection selection when all candidate P95 certificates are made simultaneous | Theorem under declared assumptions | [`proposition_97_simultaneous_candidate_family_selection.md`](proposition_97_simultaneous_candidate_family_selection.md) |
| Two candidates, two regimes, `m=1`, equal 5 percent global spending cross at 4045 per regime and first exact replicate at 4056 | Exact rational computation | [`test_simultaneous_candidate_family_selection.py`](../tests/test_simultaneous_candidate_family_selection.py) |
| P97 does not validate newly generated post-inspection candidates or establish consciousness ontology | Scientific boundary | [`p97_equation_provenance.md`](p97_equation_provenance.md) |
"""
write(path, text)

# Verifier and deterministic figure synchronization.
path = "scripts/verify_repository.py"
text = read(path)
text = text.replace('CURRENT_FRONTIER = "P96"', 'CURRENT_FRONTIER = "P97"')
if '"docs/proposition_97_simultaneous_candidate_family_selection.md"' not in text:
    marker = '    "tests/test_selection_valid_holdout_stratification.py",\n'
    addition = (
        marker
        + '    "docs/proposition_97_simultaneous_candidate_family_selection.md",\n'
        + '    "docs/p97_equation_provenance.md",\n'
        + '    "docs/figures/p97_simultaneous_candidate_family_selection.svg",\n'
        + '    "src/consciousness_bridge/simultaneous_candidate_family_selection.py",\n'
        + '    "tests/test_simultaneous_candidate_family_selection.py",\n'
        + '    "tests/test_p97_reader_surface_coherence.py",\n'
    )
    text = text.replace(marker, addition, 1)
if '"Current theorem frontier · P96"' not in text:
    text = text.replace(
        "STALE_READER_FRONTIER_MARKERS = (\n",
        "STALE_READER_FRONTIER_MARKERS = (\n    \"Current theorem frontier · P96\",\n    \"current P96 frontier\",\n    \"<strong>P96</strong><span>current theorem frontier</span>\",\n    \"96 results · current frontier P96\",\n    \"Explore all 96 results\",\n",
        1,
    )
write(path, text)

path = "scripts/sync_figure_publication.py"
text = read(path)
if "if frontier == 97:" not in text:
    marker = "    return []\n\n\ndef _frontier_page"
    block = '''    if frontier == 97:
        return [
            "### Exact P97 simultaneous finite candidate-family selection",
            "",
            "P97 complements P96 by permitting same-data post-inspection selection within a finite candidate family fixed before certification statistics are inspected.",
            "",
            "```text",
            "candidate budgets: sum_k alpha_k <= alpha",
            "inside candidate k: sum_b alpha_kb <= alpha_k",
            "K=2, B=2, m=1: local alpha = 1/80",
            "95% mathematical crossing = 4045 per regime",
            "first exact denominator-24 replication = 4056 per regime",
            "balanced unique-observation totals = 8090 / 8112",
            "```",
            "",
            "P97 pays for same-data search through multiplicity. The candidate family must be fixed before inspection. New post-inspection candidates, unrestricted within-regime drift, model acceptance, consciousness identification, nonphysicality, and bridge completion are not established.",
            "",
        ]
    return []


def _frontier_page'''
    text = text.replace(marker, block, 1)
write(path, text)

# Website overview.
path = "website/index.html"
text = read(path)
text = text.replace('<strong>96</strong><span>proposition-level results</span>', '<strong>97</strong><span>proposition-level results</span>')
text = text.replace('P96 current theorem frontier · v0.82.0', 'P97 current theorem frontier · v0.82.0')
text = text.replace('Explore all 96 results', 'Explore all 97 results')
text = text.replace('96 proposition-level results through P96', '97 proposition-level results through P97')
text = text.replace('The 96 results form several dependency branches.', 'The 97 results form several dependency branches.')
text = text.replace('The 96-result program is summarized here; <a href="research-map.html">all 96 propositions</a>', 'The 97-result program is summarized here; <a href="research-map.html">all 97 propositions</a>')
p97_home = '''<!-- current-frontier-home: P97 -->
<section id="p97-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head">
    <p class="eyebrow">Research II · Current theorem frontier · P97</p>
    <h2>Simultaneous finite candidate-family selection</h2>
    <p>P97 complements P96. The same certification data may be used to compare and select among a finite family of candidate regime plans when the complete family is fixed before the certification statistics are inspected and all candidate certificates are covered simultaneously.</p>
  </div>
  <div class="theorem-figure-shell"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p97_simultaneous_candidate_family_selection.svg"><img loading="eager" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p97_simultaneous_candidate_family_selection.svg" alt="P97 simultaneous finite candidate-family selection certificate" /></a></div>
  <div class="frontier-summary-grid">
    <article class="frontier-summary-card"><h3>Same data can compare candidates</h3><p>The candidate plans may reuse the same observations and may be statistically dependent. The family itself must be fixed before inspection.</p></article>
    <article class="frontier-summary-card"><h3>Two-level error accounting</h3><p>P95 controls regimes inside each candidate. A second union bound across candidate budgets makes every candidate certificate valid simultaneously.</p></article>
    <article class="frontier-summary-card"><h3>Exact balanced checkpoint</h3><p>For K=2, B=2, and m=1 at 95 percent global confidence, the crossing is <strong>4045 per regime</strong>; the first exact denominator-24 replication is <strong>4056</strong>.</p></article>
  </div>
  <div class="boundary"><p><strong>Scientific boundary:</strong> the candidate family must be predeclared. Newly generated post-inspection candidates, unrestricted same-data search, gradual within-regime drift, model acceptance after non-rejection, consciousness identification, nonphysicality, and bridge completion are not established.</p></div>
  <p><a href="research-map.html">Research II map</a> · <a href="visual-atlas.html">Theorem figures</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_97_simultaneous_candidate_family_selection.md">proposition_97_simultaneous_candidate_family_selection.md</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p97_equation_provenance.md">p97_equation_provenance.md</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/simultaneous_candidate_family_selection.py">simultaneous_candidate_family_selection.py</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_simultaneous_candidate_family_selection.py">test_simultaneous_candidate_family_selection.py</a></p>
</section>

'''
text = re.sub(
    r'<!-- current-frontier-home: P96 -->.*?(?=<section id="research-iii-overview">)',
    p97_home,
    text,
    count=1,
    flags=re.DOTALL,
)
write(path, text)

# Plain language and Start Here website surfaces.
p97_reader = '''<section class="boundary" id="p97-reader-frontier"><div class="section-head"><p class="eyebrow">Research II · Current frontier · P97</p><h2>Same-data candidate selection can be valid when the entire finite search family is covered at once</h2><p>P97 complements the P96 independent-holdout strategy. Before looking at certification statistics, declare a finite family of candidate regime plans. Each candidate receives its own P95 familywise error budget, and a second union bound covers all candidates simultaneously. After that simultaneous certificate is established, the final candidate can be chosen from the predeclared family using the same data without invalidating its certificate.</p></div><p><strong>Exact balanced checkpoint:</strong> two candidates, two regimes per candidate, and one-step dependence give 4045 observations per regime at 95 percent global confidence; the first exact denominator-24 replication is 4056.</p><p><strong>Boundary:</strong> a newly invented candidate after inspection is not covered. Unrestricted search, within-regime drift, model acceptance after non-rejection, consciousness identification, nonphysicality, and the physical-to-experiential bridge remain open.</p></section>

'''
for path in ("website/plain-language.html", "website/start-here.html"):
    text = read(path)
    text = text.replace("96 results · current frontier P96", "97 results · current frontier P97")
    text = text.replace("current Research II frontier P96", "current Research II frontier P97")
    text = text.replace("The 96 Research II propositions by scientific role", "The 97 Research II propositions by scientific role")
    if 'id="p97-reader-frontier"' not in text:
        marker = '<section class="boundary" id="p96-reader-frontier">'
        if marker not in text:
            raise RuntimeError(f"P96 reader insertion point not found in {path}")
        text = text.replace(marker, p97_reader + marker, 1)
    text = text.replace("Research II · Current frontier · P96", "Research II · Previous frontier · P96")
    write(path, text)

# Research Map website.
path = "website/research-map.html"
text = read(path)
text = text.replace("through Proposition 96.", "through Proposition 97.")
text = text.replace("Ninety-six results", "Ninety-seven results")
for old, new in (("P71-P96", "P71-P97"), ("P74-P96", "P74-P97"), ("P73-P96", "P73-P97"), ("P77-P96", "P77-P97"), ("P75-P96", "P75-P97")):
    text = text.replace(old, new)
text = text.replace("The current theorem frontier is P96.", "The current theorem frontier is P97.")
text = text.replace("Research Map · Current theorem frontier P96", "Research Map · Current theorem frontier P97")
text = text.replace("P96 remains a conditional model-rejection theorem", "P97 remains a conditional model-rejection theorem")
p97_map = '''<section class="result" id="p97-research-map"><span>P97</span><h3>P97: Can the same data select among candidate regime plans without invalidating the selected certificate?</h3><p>Yes for a finite family fixed before certification statistics are inspected. Candidate k receives a P95 familywise budget alpha_k. A second union bound across candidates makes all candidate certificates valid simultaneously, so the final candidate may be selected after inspection from that predeclared family.</p><p><strong>Exact balanced checkpoint:</strong> K=2 candidates, B=2 regimes, and m=1 give a 95 percent crossing at 4045 observations per regime and first exact denominator-24 replication at 4056. The balanced unique-observation totals are 8090 and 8112 because candidate plans reuse the same data.</p><p><strong>Boundary:</strong> new post-inspection candidates, unrestricted search, within-regime drift, model acceptance, consciousness identification, nonphysicality, and bridge completion remain open.</p><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_97_simultaneous_candidate_family_selection.md">Read P97 theorem</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p97_equation_provenance.md">P97 equation provenance</a> · <a href="index.html#p97-frontier">Overview P97 frontier</a></p></section>

'''
if 'id="p97-research-map"' not in text:
    marker = '<section class="result" id="p96-research-map">'
    if marker not in text:
        raise RuntimeError("P96 Research Map block not found")
    text = text.replace(marker, p97_map + marker, 1)
text = text.replace("Continue to the current P96 frontier", "Continue to the current P97 frontier")
text = text.replace("index.html#p96-frontier", "index.html#p97-frontier", 1)
text = text.replace("visual-atlas.html#p96-frontier", "visual-atlas.html#p97-frontier", 1)
text = text.replace("See the P96 figure", "See the P97 figure", 1)
text = text.replace("docs/p96_equation_provenance.md", "docs/p97_equation_provenance.md", 1)
text = text.replace("Audit P96 provenance", "Audit P97 provenance", 1)
write(path, text)

# Visual Atlas.
path = "website/visual-atlas.html"
text = read(path)
p97_atlas = '''<!-- current-frontier-visual: P97 -->
<section id="p97-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head"><p class="eyebrow">Current theorem frontier · P97</p><h2>Simultaneous finite candidate-family selection</h2><p>P97 permits same-data post-inspection selection from a finite family of candidate regime plans fixed before certification statistics are inspected. P95 controls each candidate internally, and a second union bound makes all candidate certificates simultaneous.</p></div>
  <div class="theorem-figure-shell"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p97_simultaneous_candidate_family_selection.svg"><img loading="eager" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p97_simultaneous_candidate_family_selection.svg" alt="P97 simultaneous finite candidate-family selection certificate" /></a></div>
  <p><strong>Exact checkpoint:</strong> K=2, B=2, m=1 gives 4045 observations per regime and first exact denominator-24 replication at 4056.</p>
  <p><strong>Boundary:</strong> the candidate family must be fixed before inspection. New post-inspection candidates, unrestricted search, within-regime drift, model acceptance, consciousness identification, nonphysicality, and bridge completion remain open.</p>
  <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_97_simultaneous_candidate_family_selection.md">Proof</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p97_equation_provenance.md">Equation provenance</a></p>
</section>

'''
if '<!-- current-frontier-visual: P97 -->' not in text:
    marker = '<!-- current-frontier-visual: P96 -->'
    if marker not in text:
        raise RuntimeError("P96 Visual Atlas marker not found")
    text = text.replace(marker, p97_atlas, 1)
text = text.replace('<!-- current-frontier-visual: P96 -->\n', '')
text = text.replace("Current theorem frontier · P96", "Previous theorem frontier · P96")
text = text.replace("Previous theorem frontier · P95", "Historical theorem frontier · P95")
text = text.replace("Previous theorem frontier · P94", "Historical theorem frontier · P94")
write(path, text)

# Source and implementation pages.
path = "website/sources.html"
text = read(path)
if 'id="p97-source"' not in text:
    marker = '<section id="p96-source">'
    source = '''<section id="p97-source"><div class="section-head"><p class="eyebrow">Current theorem source · P97</p><h2>Simultaneous finite candidate-family selection</h2><p>P97 permits same-data selection among a finite candidate family fixed before certification statistics are inspected. Candidate-specific P95 certificates are made simultaneous with a second union bound, after which the final candidate may be chosen from the covered family.</p></div><div class="source-grid"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_97_simultaneous_candidate_family_selection.md"><h3>Proposition 97</h3><p>Formal same-data finite-family selection theorem, exact checkpoint, and scientific boundary.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p97_equation_provenance.md"><h3>P97 provenance</h3><p>Separates standard nested union-bound logic from repository-specific integration with P92-P95.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/simultaneous_candidate_family_selection.py"><h3>P97 implementation</h3><p>Executable candidate-family guards, exact budget accounting, nested P95 certificates, and balanced thresholds.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_simultaneous_candidate_family_selection.py"><h3>P97 exact tests</h3><p>Same-data selection, multiplicity guards, selected-candidate validity, and 4045/4056 checkpoints.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p97_simultaneous_candidate_family_selection.svg"><h3>P97 theorem figure</h3><p>Canonical simultaneous candidate-family selection diagram in the synchronized publication record.</p></a></div><div class="boundary"><p><strong>Scientific boundary:</strong> newly generated post-inspection candidates and unrestricted search are outside P97. Non-rejection remains inconclusive, and consciousness identification, nonphysicality, and bridge completion are not established.</p></div></section>

'''
    if marker not in text:
        raise RuntimeError("P96 source insertion point not found")
    text = text.replace(marker, source + marker, 1)
text = text.replace("Current theorem source · P96", "Immediate predecessor theorem source · P96")
write(path, text)

path = "website/implementation.html"
text = read(path)
text = text.replace("Stage 06 · P73-P96", "Stage 06 · P73-P97")
text = text.replace("P73-P96 build a continuous chain", "P73-P97 build a continuous chain")
text = text.replace("index.html#p96-frontier", "index.html#p97-frontier")
text = text.replace("current P96 frontier", "current P97 frontier")
if "P97" not in text[text.find("Stage 06 · P73-P97"):]:
    text = text.replace(
        "P96 permits pilot-selected regime plans under a frozen-plan independent-holdout design.",
        "P96 permits pilot-selected regime plans under a frozen-plan independent-holdout design. P97 then permits same-data post-inspection selection within a finite candidate family fixed before certification statistics are inspected, paying an explicit candidate-level multiplicity cost."
    )
write(path, text)

path = "website/research-lineage.html"
text = read(path)
text = text.replace("P96", "P97") if "current theorem frontier" in text.lower() and "P97" not in text else text
write(path, text)

print("[p97-promotion] reader, audit, citation, and website surfaces advanced")
