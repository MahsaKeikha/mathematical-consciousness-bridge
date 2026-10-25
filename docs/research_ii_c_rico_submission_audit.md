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
## Reviewer revision v2: proposed control-system design (24 October 2026)

The working manuscript now includes an explicitly **proposed**, not executed, application to finite-alphabet sensor-model monitoring after adaptive feedback-controller selection. It separates pilot selection of the controller and measurement regime from independent confirmation, requires a declared filtration and fresh certification unit, and identifies false-alarm frequency, abstention rate, crossing rate, and sample use as outcomes for any future simulation. Rejection is evidence against the declared sensor-response model, **not** a proof of controller unsafety. Serially dependent closed-loop trajectories cannot be relabeled independent folds; valid application requires independent reset episodes or a separately justified dependence-aware certificate. These requirements should be validated prior to any empirical or simulation-performance claim.

The manuscript's AI-assistance disclosure was also changed to avoid claiming completed independent verification of every proof and computation. Author disclosures remain subject to author confirmation. No new control experiment has been reported.

## Reviewer revision v3: explicit claim-to-assumption mapping

The proposed sensor-model example now specifies independent reset episodes as its certification unit. Pilot controller choice and regime choice may be arbitrary functions of pilot data only when the subsequent null test has its declared error guarantee conditional on the pilot selection. Adjacent time points from a single closed-loop trajectory are not automatically independent. The manuscript also distinguishes the required assumptions across holdout testing, finite-family same-data search, cross-fitting, fold e-value aggregation, and the sequential conditional e-process. Finally, the exact rational witness checkpoints are described as algebraic calculations, not Monte Carlo type-I error, empirical power, control cost, or achieved safety performance. The proposed control simulation remains unrun. These are reviewer-oriented clarification changes, not new experimental evidence.

## Reviewer revision v4: exact two-round arithmetic and journal decision boundary

The worked checkpoint has one rejecting fold from two at declared fold level 0.04. Its round e-value is `(1/2)*(1/0.04)=25/2`; with a predictable half-stake the factor equals `1/2+(1/2)*(25/2)=27/4`. Two conditionally valid fresh rounds yield `(27/4)^2=729/16=45.5625`, crossing the 95% anytime boundary `20`, whereas one factor does not. This checks exact rational arithmetic **conditional on** valid fold certificates and fresh-round conditional null calibration. It is not a simulation of operating characteristics or independent validation of the witness generator.

The example supports sensor-model incompatibility under specified assumptions, **not** a guarantee about stability, closed-loop regret, tracking error, controller safety, or constraint satisfaction. A plant, objective, and controller benchmark are necessary to evaluate those outcomes. The Word manuscript also fixes a duplicate subsection number by labeling the proposed application 8.3.

## Reviewer revision v5: independent e-process simulation (24 October 2026)

A **new, deliberately simplified** unit simulation checked the e-process aggregation rule, not the latent-witness generator. At each of 100 fresh rounds in 20,000 independent Monte Carlo replications (NumPy seed `20261023`), two independent Bernoulli(0.04) fold-rejection indicators were generated. Fold e-values were `I(reject)/0.04`, the round e-value their equally weighted average, and wealth was updated by the predictable half-stake factor `0.5 + 0.5*E_t`. A crossing was counted if wealth reached 20 at any of the 100 inspected rounds. There were **545 crossings / 20,000 replications = 0.02725** (Monte Carlo standard error about 0.00115). This observed rate is below 0.05 and consistent with the anytime-valid bound, but does not prove validity or exercise the P94-P99 latent measurement rejection code, controlled-system dynamics, or an adaptive controller. The local executable audit script is `independent_eprocess_null_stress.py`, supplied with the manuscript review files; promote it to maintained repository tests only after review. Do not mislabel this as controller safety or sensitivity analysis.

## Reviewer revision v6: code-backed null experiment and Monte Carlo precision

The independent simulation script is now versioned at `scripts/research_ii_c_eprocess_null_stress.py`. It uses seed 20261023, 20,000 independent sequences, 100 rounds per sequence, two Bernoulli(0.04) fold-rejection indicators per round, equal fold averaging and fixed half-stakes. A direct local rerun printed `count_cross=545 fraction=0.027250 threshold=20`. The Wilson 95% binomial confidence interval for the Monte Carlo crossing proportion is approximately [0.02508, 0.02960]. This interval concerns the probability induced by the deliberately simplified null simulator, not the theoretical anytime-valid level or the complete measurement-model witness.

In the reader-facing manuscript the exact arithmetic threshold typo `above 1/0.` was corrected to `above the 95% crossing boundary of 20.` The linked website page `website/research-ii-c-paper.html` now exposes this distinction between reproducible toy simulation, exact arithmetic and the still-proposed control application. This is not evidence of actual closed-loop performance.

## Reviewer revision v7: distinguish simulation uncertainty from error guarantees

The manuscript now explicitly separates the Wilson 95% interval for the **simulated crossing proportion** from the theorem's **anytime-valid type-I error bound**. The simulated Bernoulli fold indicators are independent and freshly sampled with known null probability, fixed fold weights and fixed half-stakes. The general theorem needs conditional e-value validity and predictable stakes, and cannot inherit calibration from this simplified generator. Dependence in real controller trajectories, shared selection information, or a misspecified latent-model witness must be tested separately. The local standalone simulation reproduces 545 crossings from 20,000 null sequences, but this is not a full end-to-end P94-P100 code validation.
