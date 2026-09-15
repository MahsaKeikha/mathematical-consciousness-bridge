"""Repair dependency, navigation, and reproducibility contracts for P95."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROADMAP = ROOT / "docs" / "theorem_roadmap.md"
NAVIGATION = ROOT / "docs" / "research_navigation.md"
REPRODUCIBILITY = ROOT / "docs" / "reproducibility.md"


def repair_roadmap() -> None:
    text = ROADMAP.read_text(encoding="utf-8")

    p94_dependency = (
        r"&\text{P94: finite-range dependence preserves the localized rejection gate "
        r"under one common marginal law}\\"
    )
    p95_dependency = (
        p94_dependency
        + "\n&\\Downarrow\\\\\n"
        + r"&\text{P95: predeclared drift regimes combine local P94 gates with familywise error control}\\"
    )
    if r"\text{P95:" not in text.split("## 2. Target-side bridge lineage", 1)[0]:
        if p94_dependency not in text:
            raise RuntimeError("P94 dependency-map anchor not found")
        text = text.replace(p94_dependency, p95_dependency, 1)

    text = re.sub(
        r"\n### P95: drift-aware stratified continuation\n.*?\Z",
        "\n",
        text,
        flags=re.DOTALL,
    )

    old_after = (
        "## After P94\n\n"
        "P94 closes the first short-range temporal-dependence extension of the localized P92/P93 witness. "
        "Any P95 candidate must close a genuinely new mathematical or scientific gap. Natural directions include "
        "an explicitly drift-aware target, unknown-range or mixing-process concentration with declared assumptions, "
        "or a different observable witness not already implied by P92-P94. The physical-to-experiential bridge remains open."
    )
    new_boundary = """## P95: drift-aware stratified sign-coherence rejection

P94 proves that arbitrary pooling across changing marginals can create the forbidden P92 sign pattern even when the time-specific laws are individually P75-compatible. P95 therefore changes the population target rather than weakening the stationary theorem. It declares temporal regimes before testing, permits a different marginal law and finite dependence range in each regime, applies the P94 sign-stability gate locally, and allocates exact regime-specific error budgets whose sum is bounded by the desired familywise level. If any regime rejects, the joint null that every regime-specific marginal belongs to P75 is rejected. Cross-regime independence is not required.

For the established P92 witness, two equally budgeted regimes with dependence range one cross the strict 95 percent familywise gate at 3645 observations per regime; the first exact denominator-24 replication is 3648.

Direct proof: [P95](proposition_95_drift_aware_stratified_sign_coherence.md). Provenance: [P95 equation record](p95_equation_provenance.md). Implementation: [`drift_aware_stratified_sign_coherence.py`](../src/consciousness_bridge/drift_aware_stratified_sign_coherence.py). Tests: [`test_drift_aware_stratified_sign_coherence.py`](../tests/test_drift_aware_stratified_sign_coherence.py).

## After P95

P95 closes the first predeclared-regime repair of the P94 temporal-pooling no-go. Any P96 candidate must close a genuinely new mathematical or scientific gap. Natural directions include data-dependent segmentation with valid selection accounting, gradual within-regime drift with an explicitly time-varying target, unknown-range or mixing-process concentration under declared assumptions, or a different observable witness not already implied by P92-P95. The physical-to-experiential bridge remains open."""

    if "## P95: drift-aware stratified sign-coherence rejection" not in text:
        if old_after not in text:
            raise RuntimeError("P94 future-work boundary not found")
        text = text.replace(old_after, new_boundary, 1)
    else:
        text = text.replace("## After P94", "## After P95", 1)
        text = text.replace("Any P95 candidate", "Any P96 candidate")

    ROADMAP.write_text(text, encoding="utf-8")


def repair_navigation() -> None:
    text = NAVIGATION.read_text(encoding="utf-8")
    replacements = (
        ("**Results:** P75 through P94", "**Results:** P75 through P95"),
        (
            "**Current frontier:** [P94: Finite-Range Dependent Sign-Coherence Rejection](proposition_94_finite_range_dependent_sign_coherence.md)",
            "**Current frontier:** [P95: Drift-Aware Stratified Sign-Coherence Rejection](proposition_95_drift_aware_stratified_sign_coherence.md)",
        ),
        ("P74 through P94", "P74 through P95"),
        ("P71 through P94", "P71 through P95"),
        ("the full 94 proposition index", "the full 95 proposition index"),
        ("full 94 proposition index", "full 95 proposition index"),
    )
    for old, new in replacements:
        text = text.replace(old, new)

    audit_heading = "## Audit the current frontier without searching folders\n\n"
    p95_audit = """For P95:

| Audit surface | Canonical route |
| --- | --- |
| Direct theorem | [P95 proposition](proposition_95_drift_aware_stratified_sign_coherence.md) |
| Equation and method provenance | [P95 provenance](p95_equation_provenance.md) |
| Implementation | [`drift_aware_stratified_sign_coherence.py`](../src/consciousness_bridge/drift_aware_stratified_sign_coherence.py) |
| Regression tests | [`test_drift_aware_stratified_sign_coherence.py`](../tests/test_drift_aware_stratified_sign_coherence.py) |
| Theorem figure | [P95 drift-aware stratified certificate](figures/p95_drift_aware_stratified_sign_coherence.svg) |
| Repository reproduction | [Reproducibility Guide](reproducibility.md) |

P95 is a conditional drift-aware model-audit result for the declared P75 family. Regime boundaries and error budgets must be predeclared. The theorem does not validate data-dependent segmentation, establish model acceptance after non-rejection, identify a latent state with consciousness, establish nonphysicality, or close the physical-to-experiential bridge.

---

"""
    if "For P95:" not in text:
        if audit_heading not in text:
            raise RuntimeError("research-navigation audit heading missing")
        text = text.replace(audit_heading, audit_heading + p95_audit, 1)

    NAVIGATION.write_text(text, encoding="utf-8")


def repair_reproducibility() -> None:
    text = REPRODUCIBILITY.read_text(encoding="utf-8")
    text = text.replace(
        "The current public theorem frontier is **P94**.",
        "The current public theorem frontier is **P95**.",
        1,
    )
    text = text.replace(
        "Run only the current P94 theorem checks | focused P94 commands below",
        "Run only the current P95 theorem checks | focused P95 commands below",
        1,
    )

    heading = "## 5. Focused audit of the current P95 frontier"
    if heading in text:
        start = text.index(heading)
        end_marker = "\n---\n\n## 6. Run the full tests"
        end = text.find(end_marker, start)
        if end == -1:
            raise RuntimeError("reproducibility P95 audit end marker missing")
        p95_section = """## 5. Focused audit of the current P95 frontier

The current theorem frontier is **P95**.

Its direct technical record is:

```text
docs/proposition_95_drift_aware_stratified_sign_coherence.md
docs/p95_equation_provenance.md
src/consciousness_bridge/drift_aware_stratified_sign_coherence.py
tests/test_drift_aware_stratified_sign_coherence.py
docs/figures/p95_drift_aware_stratified_sign_coherence.svg
figures/manifest.json
```

Run the focused theorem and publication checks with:

```bash
python -m pytest -q \\
  tests/test_drift_aware_stratified_sign_coherence.py \\
  tests/test_p95_reader_surface_coherence.py \\
  tests/test_frontier_reader_narrative.py \\
  tests/test_figure_publication_sync.py \\
  tests/test_frontier_publication_consistency.py
python scripts/sync_figure_publication.py --check
python scripts/verify_repository.py
```

P95 responds to the P94 temporal-pooling no-go by replacing one pooled marginal target with a family of predeclared regime-specific targets. Each regime has its own local P94 finite-range radius and exact error budget, and the union bound controls the complete family without requiring independence between regimes.

For two equally budgeted regimes with dependence range one at 95 percent familywise confidence, the established P92 witness crosses at `3645` observations per regime. The first exact denominator-24 replication that clears the gate is `3648` per regime.

Non-rejection remains inconclusive. P95 does not validate data-dependent change-point selection, identify the latent state with consciousness, establish nonphysicality, validate an alternative ontology, or close the physical-to-experiential bridge.
"""
        text = text[:start] + p95_section + text[end:]

    REPRODUCIBILITY.write_text(text, encoding="utf-8")


def main() -> None:
    repair_roadmap()
    repair_navigation()
    repair_reproducibility()
    print("[p95] repaired roadmap, navigation, and reproducibility contracts")


if __name__ == "__main__":
    main()
