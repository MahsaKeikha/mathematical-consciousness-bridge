# P96 Equation Provenance and Novelty Record

## Scope

Proposition 96 is a selection-valid extension of the P95 drift-aware stratified rejection certificate. It does not claim that sample splitting, conditional inference, the union bound, or the tower property are new statistical ideas. The repository-original contribution is the explicit integration of those standard ideas with the P92-P95 sign-coherence chain, including executable guards that prevent pilot data reuse from being silently treated as an independent holdout certificate.

## Equation provenance

| P96 object or equation | Provenance | Role in P96 |
| --- | --- | --- |
| Pilot sigma-field `S` and conditioning on selection information | standard probability and post-selection sample-splitting logic | makes the selected segmentation and budgets fixed when the holdout certificate is analyzed |
| `C independent of S` | declared design assumption | prevents the pilot search from selecting an extreme value in the certification sample |
| `sum_b alpha_b <= alpha` | inherited from P95 familywise budgeting | allows the number of selected regimes and their unequal budgets to be pilot dependent while retaining one global failure budget |
| `Pr(intersection A_b | S) >= 1 - sum_b alpha_b` | P95 union-bound structure applied conditionally | gives simultaneous holdout coverage for the pilot-selected plan without requiring independence between selected regimes |
| `Pr(union A_b^c) = E[Pr(union A_b^c | S)]` | standard law of total probability / tower property | converts the conditional P95 guarantee into an unconditional P96 guarantee |
| `alpha_extra,selection = 0` | consequence of the declared independent-holdout design, not a universal property of adaptive selection | records that pilot algorithm complexity causes no additional alpha spending once the plan is frozen before independent holdout evaluation |
| `((m_b+1) Lbar_b)/(2 n_b) < (min_i rhat_bi)^2` | inherited exact-rational P79/P94/P95 gate | preserves the safe direction of the executable holdout rejection comparison |
| `n_holdout = 3645` per regime for `B=2, m=1` at 95 percent familywise confidence | inherited exactly from P95 | shows that pilot selection complexity does not change the holdout threshold under the P96 independence assumptions |
| `n_total = n_pilot + sum_b n_b` | elementary bookkeeping | makes the data-separation cost explicit rather than describing independent selection as free information |

## Repository-original synthesis

P96 adds the following project-specific result to the established theorem chain:

1. P94 supplies a local finite-range sign-coherence rejection gate.
2. P95 permits different predeclared marginal laws across regimes and combines their local gates familywise.
3. P96 allows the regime plan itself to be chosen adaptively from pilot information, provided the plan is frozen and certification uses independent holdout information satisfying the selected local assumptions.
4. Conditional P95 validity plus the tower property preserves the same unconditional familywise error bound.
5. The executable interface refuses to issue a P96 certificate unless pilot-holdout independence and frozen-plan status are explicitly declared.

The novelty claim is therefore **not** a new theorem about sample splitting in general. It is a theorem and implementation about how independent holdout selection closes the specific adaptive-regime gap left open by P95 in this model-audit program.

## Exact checkpoint

For the established P92 witness, two pilot-selected regimes, one-step dependence, equal error budgets, and 95 percent familywise confidence:

```text
local alpha budget = 1/40
first certifying holdout n per regime = 3645
first exact denominator-24 replication per regime = 3648
certifying holdout observations across two regimes = 7290
exact-replication holdout observations across two regimes = 7296
```

With a 500-observation pilot, total bookkeeping becomes 7790 and 7796 respectively. The pilot size is illustrative and is not itself a theorem threshold.

## Assumptions that carry scientific weight

P96 requires more than a software flag. The study design must justify that the certification information is independent of the pilot-selection information in the sense needed by the conditional argument. In particular, a naive random split of one short-range dependent time series can retain dependence between pilot and holdout observations and is not automatically covered.

The selected certification regimes must also satisfy the P94 common-marginal and declared finite-range dependence assumptions. Pilot selection does not make a nonstationary certification block stationary.

## Interpretation boundary

P96 is a conditional statistical model-audit theorem. It does not establish that a selected regime is conscious, validate P75 after non-rejection, prove nonphysicality, or close the physical-to-experiential bridge. It also does not license repeated redesign after holdout inspection. Any reuse of certification data for selection requires a different validity argument.
