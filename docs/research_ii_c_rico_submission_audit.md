# Research II-C: RICO submission audit (October 2026)

**Status:** working manuscript and reviewer audit, not an independently verified proof or an accepted publication.

**Title:** Selection-Valid and Anytime-Valid Evidence after Adaptive Model Search: Holdout Stratification, Cross-Fitting, E-Value Aggregation, and Sequential E-Processes.

**Manuscript provenance:** Compared the September 19 *Journal of Statistical Planning and Inference* submission draft against the September 17 Research II-C draft. Both contain eleven main sections and seven cited references. The earlier research document has seven embedded figures; the September 19 submission document has no embedded figures. Figure omission needs an editorial decision before resubmission, not an assumption that the graphics are validated for RICO.

## What the current paper actually claims

The paper's claimed novelty is an explicitly guarded composition of predeclared regime-specific error control, independent pilot/holdout selection, finite prespecified same-data search, cross-fitting with own-fold exclusion, fold e-value aggregation, and fresh-round anytime-valid accumulation around a concrete model-rejection witness. These component statistical devices are established; no general novel e-value theorem is asserted solely from their juxtaposition.

## Inference checks that must survive peer review

1. **Pilot/holdout:** selection can depend arbitrarily on the pilot only when the holdout remains valid conditional on the selection information.
2. **Same-data search:** the candidate family and its error allocation must be fixed independently of the inspected candidate outcomes.
3. **Cross-fitting:** independent certification blocks must exclude their own outcomes from the corresponding selection plans. Overlapping selection data may make fold evidence dependent; use valid simultaneous error budgeting, not an independence shortcut.
4. **E-values:** if P(reject_j | selection information) <= a_j, then E_j = 1{reject_j}/a_j has conditional expectation <=1. Fixed nonnegative convex mixtures preserve the null bound without requiring cross-fold independence; ex post outcome-based weighting generally does not.
5. **Sequential evidence:** each new round must satisfy E[E_t | F_(t-1)] <=1 under the sequential global null. For a predictable eta_t in [0,1], the factor 1-eta_t+eta_t E_t has conditional null expectation <=1; the product is a nonnegative supermartingale and Ville's inequality protects repeated threshold checks. Fixed-round marginal validity alone is not enough.
6. **Scope of scientific claims:** model rejection is relative to the declared statistical family and assumptions. Failure to reject does not validate the family or any semantic interpretation of its latent classes.

The sequential assumptions can be checked against [P100](proposition_100_anytime_sequential_eprocess.md) and its upstream P95-P99 records. Review [reproducibility guidance](reproducibility.md) before claiming that every exact numerical checkpoint is reproduced by the submitted manuscript.

## RICO-specific presentation gaps

- Present a specific controlled-system, adaptive policy evaluation, or optimization example with a clearly declared filtration and independent certification unit, or explicitly explain that this paper is purely statistical methodology rather than an empirical control-system demonstration.
- Clarify the exact mathematical advance and show the significance for control and optimization readers, not only the latent measurement example.
- Audit all displayed equations and exact-rational checkpoints against the original code and theorem records before preparing a final submission.
- Determine whether the seven figures from the earlier draft belong in the revised paper, are merely supplemental, or were intentionally excluded.
- Prepare a new RICO cover letter. The September 19 one addresses a different journal.
- Ensure submission identity, competing interests, and AI assistance disclosures comply with the receiving journal's current instructions.

This document records a review workflow and known boundaries; it is not an independent guarantee of mathematical correctness.