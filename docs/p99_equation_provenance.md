# P99 Equation and Novelty Provenance

## Scope

P99 combines standard e-value theory with the repository's exact P92-P98 certification chain. The novelty claim is deliberately narrow. P99 does not claim to invent e-values, convex e-value averaging, Markov rejection, cross-fitting, sample splitting, or exact rational arithmetic. Its repository-specific contribution is the construction that turns selection-valid P96/P98 fold rejection indicators into exact rational e-values, permits a finite calibration mixture fixed without own-fold leakage, aggregates the resulting fold evidence without assuming fold independence, and connects that evidence calculus to the established sign-coherence witness and exact finite-sample threshold machinery.

## Standard ingredients

The following ingredients are standard probability and statistics facts and are not claimed as repository-original:

1. **E-values.** A nonnegative random variable `E` satisfying
   \[
   \mathbb E_0[E]\le 1
   \]
   under the null is an e-variable, and an observed realization is an e-value.
2. **Level-test to e-value conversion.** If `R(tau)` is a binary rejection indicator with
   \[
   \Pr_0(R(\tau)=1)\le \tau,
   \]
   then
   \[
   E(\tau)=R(\tau)/\tau
   \]
   has null expectation at most one.
3. **Convex e-value averaging.** Fixed nonnegative weights summing to one preserve the e-value property under arbitrary dependence.
4. **Markov's inequality.** If `E` is nonnegative and `E_0[E] <= 1`, then
   \[
   \Pr_0(E\ge 1/\alpha)\le \alpha.
   \]
5. **Conditional validity and the tower property.** A fold test whose plan and calibration are fixed using information independent of its own certification block remains valid after averaging over that selection information.

A modern e-value reference is:

Vovk, V. and Wang, R. (2021). *E-values: Calibration, combination, and applications*. The Annals of Statistics 49(3), 1736-1754. DOI: 10.1214/20-AOS2020.

## Repository-specific dependency chain

P99 depends on the following established repository results:

- **P92:** the three-minor sign-coherence obstruction excludes the declared mixed-prevalence P75 family at exact global witness radius `1/24`.
- **P94:** finite-range dependent observations with one common marginal admit an exact-rational localized rejection radius.
- **P95:** predeclared drift regimes combine local P94 certificates with familywise error control.
- **P96:** an arbitrarily complicated pilot-selected regime plan may be certified on genuinely independent holdout information without an extra penalty for selection complexity.
- **P97:** same-data selection from a finite predeclared candidate family is protected by explicit multiplicity accounting.
- **P98:** the P96 selection and certification separation can be rotated across mutually independent blocks, producing valid cross-fitted fold certificates without requiring the final fold certificates to be independent.

## P99 conditional fold e-value

For fold `k`, let `S_k` contain the information used to choose the regime plan and the finite e-value calibration. The fold's own certification block `D_k` is excluded from `S_k`, so

\[
\mathcal D_k\perp \mathcal S_k.
\]

At a threshold `tau` fixed given `S_k`, P96 supplies a binary fold rejection indicator `R_k(tau)` satisfying

\[
\Pr\bigl(R_k(\tau)=1\mid\mathcal S_k\bigr)\le\tau
\]

under the selected fold null. Therefore

\[
\boxed{
E_k(\tau)=\frac{R_k(\tau)}{\tau}
}
\]

obeys

\[
\mathbb E\bigl[E_k(\tau)\mid\mathcal S_k\bigr]\le 1.
\]

The tower property gives

\[
\boxed{\mathbb E[E_k(\tau)]\le 1.}
\]

## Finite threshold mixture

For a finite threshold grid `tau_kj` and exact rational mixture weights `lambda_kj` fixed before own-fold evaluation, define

\[
\boxed{
E_k=\sum_j\lambda_{kj}\frac{R_k(\tau_{kj})}{\tau_{kj}},
\qquad
\sum_j\lambda_{kj}=1.
}
\]

Linearity of conditional expectation gives

\[
\mathbb E[E_k\mid\mathcal S_k]\le 1
\]

without requiring the threshold tests to be independent.

## Cross-fold aggregation

Let exact fold weights satisfy

\[
w_k>0,
\qquad
\sum_k w_k=1.
\]

Define

\[
\boxed{
E_{\mathrm{CF}}=\sum_k w_kE_k.
}
\]

Under the cross-fitted global null in which every selected fold null is true,

\[
\mathbb E[E_{\mathrm{CF}}]
=\sum_k w_k\mathbb E[E_k]
\le 1.
\]

No independence among the final fold e-values is needed for this averaging step. Markov's inequality therefore gives

\[
\boxed{
\Pr\left(E_{\mathrm{CF}}\ge\frac1\alpha\right)\le\alpha.
}
\]

## Exact balanced distributed-evidence checkpoint

At global 95 percent confidence with two folds, two regimes per fold, dependence range one, equal fold weights, and fold test level

\[
\tau=\frac1{25},
\]

equal regime spending inside each fold gives

\[
\alpha_{kb}=\frac1{50}.
\]

The inherited P94 exact-rational radius calculation against witness radius `1/24` gives the first certifying per-regime integer

\[
\boxed{3774},
\]

and the first denominator-24 witness replication at or above that threshold

\[
\boxed{3792}.
\]

Thus each fold uses

\[
\boxed{7548}\quad\text{or}\quad\boxed{7584}
\]

certification observations, and the unique two-fold totals are

\[
\boxed{15096}\quad\text{or}\quad\boxed{15168}.
\]

If both folds reject at level `1/25`, each fold e-value is `25`. With weights `1/2,1/2`,

\[
E_{\mathrm{CF}}=25\ge20=1/(1/20),
\]

so the 5 percent global null is rejected.

For the matched P98 equal-split design, the local regime level is `1/80` and the per-regime crossing is `4045`, with exact replication `4056`. The P99 distributed-evidence checkpoint therefore lowers the crossing by

\[
\boxed{271}
\]

observations per regime in this declared configuration.

## No uniform dominance

P99 does not uniformly dominate P98. If only one of two equally weighted folds rejects at level `1/25`, then

\[
E_{\mathrm{CF}}=\frac12\cdot25=\frac{25}{2}<20,
\]

so P99 does not reject. A sufficiently strong single fold may still cross its stricter P98 fold-specific threshold and make P98 reject. The procedures therefore protect different evidence geometries: P98 is naturally sparse, while P99 can accumulate distributed evidence.

## Scientific boundary

P99 requires the plan, threshold grid, threshold mixture weights, and fold weights to be fixed independently of each fold's own certification statistics. It still requires the P98 independent-block structure and the declared P94/P95 within-regime assumptions. It does not validate post-hoc calibration search, own-fold leakage, arbitrary dependent-stream splitting, misspecified dependence ranges, unrestricted drift, model acceptance after non-rejection, identification of a latent state with consciousness, nonphysicality of consciousness, or completion of the physical-to-experiential bridge.
