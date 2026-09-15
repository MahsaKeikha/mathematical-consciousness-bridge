# Proposition 99: Cross-Fitted E-Value Aggregation

## Purpose

P98 gives a rigorous cross-fitted familywise certificate by assigning each fold an error budget and applying a union bound across folds. That construction is exact, dependence-robust, and naturally effective when one fold becomes individually decisive.

P99 asks a different question:

> Can several selection-valid cross-fitted folds contribute moderate evidence toward one global rejection without assuming the fold certificates are independent and without dividing the global alpha across folds in advance?

The answer is yes for a declared finite e-value calibration.

For each fold and each level `tau`, P99 converts the valid P96 fold rejection indicator into the e-value

\[
E_k(\tau)=\frac{\mathbf 1\{R_k(\tau)=1\}}{\tau}.
\]

Finite exact-rational mixtures across thresholds remain fold e-values. A fixed convex average across folds remains an e-value even when the cross-fitted fold certificates are dependent. Markov's inequality then gives a global level-alpha rejection rule.

The result is complementary to P98, not a replacement for it. P99 can be strictly better when evidence is distributed across folds. P98 can be better when one fold contains very strong sparse evidence.

---

## P99A. Cross-fitted fold design

Let

\[
\mathcal D_1,\ldots,\mathcal D_K,
\qquad K\ge 2,
\]

be mutually independent certification blocks.

For fold `k`, let

\[
\mathcal S_k
\subseteq
\sigma(\mathcal D_1,\ldots,\mathcal D_{k-1},\mathcal D_{k+1},\ldots,\mathcal D_K)
\]

contain the information used to select the fold-specific regime plan.

The plan may be an arbitrarily complicated `S_k`-measurable construction, but it must be frozen before any certification statistic from `D_k` is inspected.

P99 also permits the finite e-value calibration for fold `k` to be chosen using `S_k`. Its threshold grid and mixture weights must likewise be frozen before `D_k` is evaluated.

Therefore

\[
\boxed{\mathcal D_k\perp\mathcal S_k.}
\]

This is the same own-fold exclusion that makes P96 and P98 selection-valid.

---

## P99B. A level-tau fold rejection becomes an e-value

Fix fold `k` and condition on `S_k`. The selected plan and its calibration are now fixed.

For one declared threshold

\[
0<\tau<1,
\]

allocate exact regime-level error weights inside the selected fold plan so that the total P95/P96 familywise budget is at most `tau`.

Let

\[
R_k(\tau)\in\{0,1\}
\]

be the resulting P96 rejection indicator for the selected joint P75 null in fold `k`.

Under that fold null, P96 gives

\[
\Pr\bigl(R_k(\tau)=1\mid\mathcal S_k\bigr)\le\tau.
\]

Define

\[
\boxed{
E_k(\tau)
=
\frac{R_k(\tau)}{\tau}.
}
\]

Then

\[
\mathbb E\bigl[E_k(\tau)\mid\mathcal S_k\bigr]
=
\frac{\Pr(R_k(\tau)=1\mid\mathcal S_k)}{\tau}
\le1.
\]

Thus `E_k(tau)` is a conditional e-value for the selected fold null.

Taking expectations again gives

\[
\boxed{
\mathbb E[E_k(\tau)]\le1.
}
\]

---

## P99C. Finite threshold mixtures

A single threshold favors one evidence-strength regime. To avoid pretending that one threshold is universally optimal, choose a finite grid

\[
\tau_{k1},\ldots,\tau_{kJ_k}
\]

and exact nonnegative mixture weights

\[
\lambda_{k1},\ldots,\lambda_{kJ_k},
\qquad
\sum_{j=1}^{J_k}\lambda_{kj}=1.
\]

All thresholds and weights must be frozen before the fold's own certification block is evaluated.

Define

\[
\boxed{
E_k
=
\sum_{j=1}^{J_k}
\lambda_{kj}
\frac{R_k(\tau_{kj})}{\tau_{kj}}.
}
\]

Linearity of conditional expectation gives

\[
\mathbb E[E_k\mid\mathcal S_k]
\le
\sum_j\lambda_{kj}
=1.
\]

Therefore

\[
\boxed{\mathbb E[E_k]\le1.}
\]

No independence among the threshold tests is required.

---

## P99D. Aggregation across cross-fitted folds

Choose exact fold weights

\[
w_1,\ldots,w_K>0,
\qquad
\sum_{k=1}^{K}w_k=1,
\]

fixed independently of the certification outcomes.

Define the aggregate

\[
\boxed{
E_{\mathrm{CF}}
=
\sum_{k=1}^{K}w_kE_k.
}
\]

The fold e-values need not be independent. Their selection information generally overlaps under cross-fitting.

Nevertheless, under the cross-fitted global null that every selected fold null is true,

\[
\mathbb E[E_{\mathrm{CF}}]
=
\sum_{k=1}^{K}w_k\mathbb E[E_k]
\le
\sum_{k=1}^{K}w_k
=1.
\]

Hence

\[
\boxed{
\mathbb E[E_{\mathrm{CF}}]\le1.
}
\]

This step uses only linearity of expectation. It does not multiply fold probabilities and does not assume independent fold certificates.

---

## P99E. Global level-alpha rejection

For a declared global level

\[
0<\alpha<1,
\]

Markov's inequality gives

\[
\Pr\left(E_{\mathrm{CF}}\ge\frac1\alpha\right)
\le
\alpha.
\]

Therefore the rule

\[
\boxed{
\text{reject }H_0^{\mathrm{CF}}
\quad\text{if}\quad
E_{\mathrm{CF}}\ge\frac1\alpha
}
\]

has type-I error at most `alpha` under the declared P99 assumptions.

The final comparison is an exact rational comparison whenever the thresholds and mixture weights are rational and the nested P96 gates use the established exact certification machinery.

---

## P99F. Why P99 differs from the P98 union bound

P98 makes all fold confidence statements simultaneously correct by requiring

\[
\sum_k\beta_k\le\alpha.
\]

With equal spending, each fold receives `alpha/K`.

P99 does not make that same simultaneous-confidence claim. Instead it constructs one nonnegative global evidence variable with expectation at most one under the global null.

That distinction matters.

P98 asks whether at least one fold can cross a stricter fold-specific familywise gate.

P99 asks whether the weighted evidence contributed by several valid fold tests is large enough in aggregate.

The two procedures therefore answer the same global-null testing problem through different valid error-control constructions.

---

## P99G. Exact distributed-evidence checkpoint

Take

\[
K=2,
\qquad
B=2,
\qquad
m=1,
\qquad
\alpha=\frac1{20}.
\]

Give both folds equal weight

\[
w_1=w_2=\frac12.
\]

Use the single fold test level

\[
\boxed{\tau=\frac1{25}}.
\]

Inside each fold, divide that fold test level equally across the two regimes:

\[
\boxed{
\alpha_{kb}
=
\frac{1/25}{2}
=
\frac1{50}.
}
\]

For the established denominator-24 P92 witness and dependence range one, the exact P94/P95 gate crosses at

\[
\boxed{n=3774}
\]

observations per regime.

The first exact denominator-24 replication at or above that threshold is

\[
\boxed{n_{\mathrm{exact}}=3792}.
\]

Each fold therefore uses

\[
\boxed{7548}
\]

observations at the mathematical crossing and

\[
\boxed{7584}
\]

at the first exact replication.

Across the two genuinely different certification blocks, the unique totals are

\[
\boxed{15096}
\]

and

\[
\boxed{15168}.
\]

If both folds reject at level `1/25`, each contributes

\[
E_k=25.
\]

Thus

\[
E_{\mathrm{CF}}
=
\frac12(25)+\frac12(25)
=25.
\]

The 95 percent global threshold is

\[
\frac1\alpha=20,
\]

so

\[
\boxed{25\ge20}
\]

and the cross-fitted global null is rejected.

---

## P99H. Strict comparison with the balanced P98 checkpoint

For the same

\[
K=2,\quad B=2,\quad m=1,\quad \alpha=1/20,
\]

P98 equal fold spending gives fold alpha `1/40`, local regime alpha `1/80`, and the established crossing

\[
4045
\]

per regime, with first exact replication at

\[
4056.
\]

P99's declared distributed-evidence checkpoint instead uses local alpha `1/50` and crosses at

\[
3774,
\]

with first exact replication at

\[
3792.
\]

Thus, in the specific configuration where both folds carry moderate evidence sufficient for level `1/25` rejection, P99 reaches a valid global rejection strictly earlier than the equal-split P98 design.

The mathematical crossing improves by

\[
\boxed{4045-3774=271}
\]

observations per regime.

The unique two-fold mathematical total decreases from

\[
16180
\]

to

\[
15096.
\]

This is a configuration-specific gain, not a uniform power theorem.

---

## P99I. No uniform dominance

Suppose only one of the two equally weighted folds rejects at level `1/25`.

Then

\[
E_{\mathrm{CF}}
=
\frac12(25)
=
\frac{25}{2}
=12.5
<20.
\]

P99 does not reject.

A sufficiently strong single fold may nevertheless cross its P98 fold-specific level and cause P98 to reject.

Therefore

\[
\boxed{
\text{P99 does not uniformly dominate P98, and P98 does not uniformly dominate P99.}
}
\]

P98 is naturally suited to sparse decisive evidence. P99 adds an exact route for distributed evidence.

---

## P99J. Exact multi-threshold example

Take the two thresholds

\[
\tau_1=\frac1{40},
\qquad
\tau_2=\frac1{25},
\]

with mixture weights

\[
\lambda_1=\frac15,
\qquad
\lambda_2=\frac45.
\]

At the exact replication size `3792`, the published witness clears the `1/25` fold gate but not the stricter `1/40` fold gate. Therefore each fold contributes

\[
E_k
=
\frac15\cdot0
+
\frac45\cdot25
=20.
\]

With two equally weighted rejecting folds,

\[
E_{\mathrm{CF}}=20,
\]

which exactly reaches the 95 percent global rejection threshold.

This example shows that a finite threshold mixture can preserve the distributed-evidence certificate while reserving some weight for a stricter evidence level.

---

## P99K. What P99 solves

P99 permits:

- arbitrary leave-one-block-out fold-plan selection under the P98 independence structure;
- a finite exact-rational grid of fold test levels;
- exact rational mixture weights across those levels;
- reuse of the same fold data across the finite threshold tests;
- dependent threshold tests within a fold;
- dependent e-values across cross-fitted folds;
- exact weighted averaging across folds;
- global level-alpha rejection through one e-value threshold;
- accumulation of moderate evidence across several folds;
- an exact finite-sample checkpoint that is strictly earlier than equal-split P98 for the declared distributed-evidence configuration.

---

## P99L. What P99 does not solve

P99 does not justify:

1. choosing threshold grids or mixture weights after inspecting the fold's own certification statistics;
2. using a fold's own certification block to select the plan later tested on that fold;
3. treating adjacent segments of one dependent stream as mutually independent blocks without a valid argument;
4. unbounded or post-hoc calibration search without additional error control;
5. misspecified within-regime dependence ranges;
6. unrestricted drift inside a selected regime;
7. interpreting non-rejection as model acceptance;
8. identifying the latent state with consciousness;
9. concluding that consciousness is nonphysical;
10. completing the physical-to-experiential bridge.

A natural next question is whether the P99 evidence construction can be made sequential and anytime-valid so that additional independent certification rounds may be accumulated under optional stopping without invalidating the global guarantee. That is a separate theorem problem.

---

## Relation to standard e-value theory

The use of nonnegative variables with null expectation at most one, their convex averaging, and rejection through Markov's inequality are standard e-value ideas. A modern reference is:

Vovk, V. and Wang, R. (2021). *E-values: Calibration, combination, and applications*. The Annals of Statistics 49(3), 1736-1754. DOI: 10.1214/20-AOS2020.

P99's repository-specific contribution is the integration of that standard evidence calculus with the P92-P98 exact sign-coherence, drift, selection-valid, and cross-fitted certification chain; the exact binary-certificate construction; the scientific guard conditions; and the reproducible 3774/3792 distributed-evidence checkpoint.

---

## Reproducibility

Implementation:

[`src/consciousness_bridge/cross_fitted_evalue_aggregation.py`](../src/consciousness_bridge/cross_fitted_evalue_aggregation.py)

Regression tests:

[`tests/test_cross_fitted_evalue_aggregation.py`](../tests/test_cross_fitted_evalue_aggregation.py)

Direct predecessors:

- [P95 drift-aware stratified sign-coherence rejection](proposition_95_drift_aware_stratified_sign_coherence.md)
- [P96 selection-valid holdout stratification](proposition_96_selection_valid_holdout_stratification.md)
- [P97 simultaneous finite candidate-family selection](proposition_97_simultaneous_candidate_family_selection.md)
- [P98 cross-fitted selection-valid certification](proposition_98_cross_fitted_selection_valid_certification.md)

Equation and novelty record:

[`p99_equation_provenance.md`](p99_equation_provenance.md)
