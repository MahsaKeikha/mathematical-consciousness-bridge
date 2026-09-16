# P1-P100 Publication Package

This directory converts the frozen P1-P100 theorem frontier into a journal-facing manuscript without changing the mathematical record on `main`.

## Frozen scientific source

The publication branch was created from the verified P100 merge commit:

```text
d7e7b159588586ff3325bd9c77b611df4bc22fa9
```

The formal package release remains `v0.82.0`. The documented theorem frontier is `P100`.

The manuscript must not silently strengthen a theorem, convert a modeling assumption into an empirical fact, or convert a model-family rejection into an ontological conclusion.

## Target submission

Primary target: *Neuroscience of Consciousness*, Research Article.

Special issue target: **Is There More to Consciousness Than Computation?**

Working title:

> **Testing physical and computational sufficiency in consciousness science: exact model separation and anytime-valid falsification**

The article is framed as a theoretical and methodological contribution. It asks how claims of computational, functional, physical, quantum-operational, or implementation-dependent sufficiency can be turned into falsifiable mathematical statements with finite-data and sequential validity.

## Central claim

For an independently specified target `E` and a declared physical or computational descriptor `T`, sufficiency is a factorization claim. Deterministically,

\[
E=B\circ T.
\]

Stochastically, under the finite formulation used in the repository,

\[
E\perp\!\!\!\perp\Omega\mid T,
\qquad
I(E;\Omega\mid T)=0.
\]

The paper develops an auditable route from this criterion to exact model-family separation, finite-sample rejection, selection-valid certification, e-value aggregation, and anytime-valid sequential evidence.

## Nonclaims that must remain visible

The manuscript does not claim that:

- consciousness is nonphysical;
- consciousness is an additional spacetime dimension;
- consciousness is a quantum variable or a state of matter;
- a latent target state is identical to phenomenal consciousness;
- rejecting one physical or computational descriptor rejects all possible physical descriptions;
- failure to reject a model validates that model;
- the exact synthetic P92-P100 witnesses are biological observations.

A rejection is always relative to the declared descriptor, target construction, measurement model, and statistical assumptions.

## Main manuscript theorem spine

| Manuscript role | Repository source | Scientific function |
| --- | --- | --- |
| Foundations | P1-P18 | invariance, identifiability, recovery, temporal and scale-aware representation |
| Sufficiency criterion | P19-P24 | deterministic/stochastic physical sufficiency and finite-data residual certification |
| Operational physics | P25-P44 | scale compatibility and quantum-operational specialization |
| Target provenance | P71-P76 | non-circular target construction, target-channel robustness, identifiability, adequacy |
| Exact model separation | P77-P92 | complete declared model-family distance and nonlinear exact separation |
| Dependence and drift | P93-P95 | localized finite-sample rejection, finite-range dependence, predeclared drift regimes |
| Selection validity | P96-P98 | independent holdout, simultaneous candidate-family control, cross-fitting |
| Evidence accumulation | P99 | exact e-value aggregation |
| Sequential validity | P100 | predictable reserve stakes and anytime-valid e-process |

The P45-P70 optimization and calibration branch remains part of the supplement and implementation record rather than the central narrative.

## Main figures

The initial main-text figure set is deliberately small and theorem-centered:

1. `../docs/figures/theorem_roadmap.svg`
2. `../docs/figures/p19_fundamental_physical_sufficiency.svg`
3. `../docs/figures/p71_target_provenance_noncircularity.svg`
4. `../docs/figures/p92_exact_global_mixed_prevalence_distance.svg`
5. `../docs/figures/p100_anytime_sequential_eprocess.svg`

Candidate supplementary figures include the P38 quantum-operational, P75 adequacy, P89 complete linear-parity, P94 dependence, P98 cross-fitting, and P99 e-value aggregation figures.

## Files

- `manuscript.md`: journal-facing main manuscript.
- `supplementary_methods.md`: proposition lineage, exact derivations, audit and reproducibility record.
- `cover_letter.md`: special-issue cover letter draft.
- `figure_plan.md`: figure selection and caption contract.
- `submission_checklist.md`: journal and scientific-boundary checks before export.

## Publication rule

Every consequential statement in the manuscript must be classifiable as one of:

1. externally established mathematics or science;
2. repository-original theorem or computation;
3. modeling assumption or definition;
4. generated or synthetic result;
5. open scientific question.

If a sentence cannot be classified cleanly, it should be revised before submission.
