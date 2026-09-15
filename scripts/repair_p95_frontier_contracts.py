"""Repair the dependency and future-work contracts required by P95 promotion."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROADMAP = ROOT / "docs" / "theorem_roadmap.md"


def main() -> None:
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

    # The initial promoter appends a compact P95 note. The canonical roadmap
    # needs a level-two frontier section before the future-work boundary.
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
    print("[p95] repaired theorem-roadmap dependency and future-work contracts")


if __name__ == "__main__":
    main()
