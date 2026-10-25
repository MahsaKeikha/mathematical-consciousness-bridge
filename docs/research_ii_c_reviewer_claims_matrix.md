# Research II-C: reviewer-facing claims and required evidence

**Working manuscript:** reviewer-defensible v20. This matrix tracks assertions, assumptions, limitations and the next falsifiable test; it does not certify proofs or acceptance.

| Claim | Required assumption | Current evidence | Remaining gate |
|---|---|---|---|
| Pilot-selection-valid holdout rejection | Conditional size on fresh data given pilot-selected plan | Stated in manuscript/theorem record | Check selection sigma-field and null conditioning against implementation |
| Same-data finite-family protection | Candidate family fixed before certification and simultaneous multiplicity budget | Mathematical argument; repository checkpoints | Audit level allocations for every selected family |
| Cross-fitted fold rejection | Own-fold exclusion and valid fold-specific null | Symbolic derivation | Audit all reused data and fold null intersection |
| Fold e-value aggregation | Each e-value nonnegative with expectation ≤1, weights admissible independently of evaluated outcomes | Exact two-fold Bernoulli check; algebra | Verify certificate calibration for actual latent-model simulator |
| Anytime-valid e-process | Conditional round e-value expectation ≤1 given full past; predictable stake | Standard supermartingale argument plus synthetic checks | End-to-end conditional calibration with fresh model-specific episodes |
| Model-monitoring application | Specified plant, controller, episode/reset model and sensor null | Proposed study design only | Run independent closed-loop simulation with controls |
| Control performance or safety | Separate stability, tracking, constraint and safety metrics | No such results claimed | Prespecified empirical/control benchmarks |

The manuscript's novelty is the **specific, assumption-preserving composition** of existing selection, cross-fitting, e-value and sequential techniques around a finite-alphabet rejection certificate; it is **not** the invention of any of those general devices.

## Reviewer decision checkpoints

1. Verify the finite-cell base certificate and its exact-rational witness from a second implementation.
2. Validate all null hypotheses, conditioning information and multiplicity budgets.
3. Rerun the model-specific simulator under a proven null and alternatives proved outside the null.
4. Confirm results are not described as control-system performance without an actual plant/policy study.
5. Independently verify every bibliographic entry, including statements relying on the cited paper.
6. Pin a specific Git commit for the final manuscript's numerical results and archive a reproducible release.

**Status:** the exact Bernoulli stress tests check aggregation behavior under toy laws; they do not complete items 1-4 for the P94-P99 latent-model certificate. A clean visual presentation does not substitute for scientific verification.

## Manuscript v21: explicit conditional-validity proof obligations

Working manuscript v21 adds Section 10.3 spelling out the implementation-level proof requirements for (i) pilot/holdout conditioning, (ii) fold-by-fold exclusion, (iii) fixed finite-family multiplicity correction, and (iv) fresh-round filtration and predictable staking. The critical distinction is conditional validity after selection versus mere unconditional validity for an unselected plan. It also explicitly notes that fixed-weight e-value averaging needs no cross-fold independence while raw adjacent time-series segments are not automatically independent evaluation units. This section adds **no new theorem or experimental evidence**; it makes proof obligations auditable. Seven figures and the 33-item reference list are preserved.
