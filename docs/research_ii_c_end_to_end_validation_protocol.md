# Research II-C: end-to-end model-specific validation protocol

**Status: preregistered study design, not executed experimental evidence.** This protocol separates mathematical certification from the illustrative Bernoulli exercises in the working manuscript.

## Objective and study unit

The target is type-I error calibration and detection under a **specified latent measurement null and specified alternatives**, not merely under user-selected Bernoulli rejection indicators. The unit is an independently initialized episode/replicate at a frozen controller, measurement regime and sample size. Within-episode temporal samples can be dependent; they are not independent folds. A controller application additionally requires explicit plant dynamics, feedback policy, noise law and reset procedure.

## Required inputs before sampling certification observations

1. A mathematically explicit null distribution from the P75/P94-P99 latent binary-view family, with an executable simulator and a separately validated membership check.
2. A predeclared alternative family parameterized by effect size with known separation from the null family. Do not treat an arbitrary perturbed parameter as outside the null without proof.
3. The implemented P94-P99 certificate, including exact thresholds, sample accounting, fold construction, and witness computation. Identify all uses of pilot information and ensure own-fold exclusion.
4. A fresh-round filtration, initial wealth, alpha boundary, predictable weights, stake schedule, sequential horizon and stopping rule; freeze these before the null and alternative replications.
5. Random seeds, software versions, number of independent replications, test levels, and failure-handling policy.

## Validation gates

**Gate A: arithmetic.** Compare every exact-rational example against a separate reference implementation. Verify values and sample counts, not only the final threshold comparison.

**Gate B: one-round calibration.** For each null parameter setting, estimate unconditional rejection and inspect conditional calibration across *predeclared* pilot-selected strata. Confidence intervals describe Monte Carlo precision, not a theorem. A failing condition cannot be dismissed by pooling over strata.

**Gate C: sequential calibration.** Generate new certification data conditional on each past filtration; inspect threshold crossings after every round, including stopped trajectories. Compare empirical crossing frequencies with alpha and report uncertainty across replications.

**Gate D: model-specific alternatives.** Simulate distributions proven outside the declared latent null. Report detection probability, first-crossing round distribution, abstention, certification sample consumption and effect-size dependence.

**Gate E: controlled-system study.** Specify state equations, sensor channels, control objective, policy candidates and reset protocol. Use pilot episodes for adaptive choice and fresh certification episodes for monitoring. Independently report tracking cost, safety violations, and model-rejection alerts; never equate model rejection with unsafe control.

**Gate F: falsification checks.** Repeat with intentionally reused folds and temporally split non-independent episodes **as counterexamples only**, and show they are excluded from validity claims. Include nonrejecting outcomes, degeneracies and code failure modes.

## Minimum reporting table

| Scenario | Generating law | Eligible independence unit | Replications | Empirical false alarm / detection | Interval | First-crossing time | Sample count | Interpretation |
|---|---|---|---:|---:|---|---|---:|---|
| Valid null A | To be implemented | Independent reset episode | Not run | Not run | Not run | Not run | Not run | Gate B/C |
| Valid null B | To be implemented | Independent reset episode | Not run | Not run | Not run | Not run | Not run | Gate B/C |
| Alternative A | To be implemented and proven outside null | Independent reset episode | Not run | Not run | Not run | Not run | Not run | Gate D |
| Closed-loop plant | To be specified | Independent reset episode | Not run | Not run | Not run | Not run | Not run | Gate E |

The two existing Bernoulli scripts are **unit experiments for e-process aggregation** and do not satisfy Gates B through E.

## Release criteria

Before promoting manuscript claims to empirical validation, archive exact source and commit, complete the above table from executable generated data, independently check null/alternative membership, and rerun under pinned dependencies. Preserve failures and unreported scenarios rather than selecting only favorable outcomes.
