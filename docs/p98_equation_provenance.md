# P98 Equation and Novelty Provenance

## Scope

P98 combines standard cross-fitting/sample-splitting logic with the repository's exact P92-P96 rejection chain. The novelty claim is deliberately narrow: P98 does not claim a new union bound, a new concentration inequality, or a general theorem that arbitrary cross-validation is inferentially valid. It proves the specific rotated holdout construction required after P96 and P97, integrates it with exact-rational P95/P94 certification, and makes the simultaneous fold accounting executable.

## Standard ingredients

The following ingredients are standard probability/statistics facts and are not claimed as repository-original:

1. **Conditional validity under independent holdout information.** If a model or testing plan is measurable with respect to information independent of a holdout block, a valid holdout theorem may be conditioned on the selection information and then averaged over it.
2. **Tower property.** If \(\Pr(A^c\mid\mathcal S)\le \beta\) almost surely, then \(\Pr(A^c)\le\beta\).
3. **Union bound.** For events \(E_1,\ldots,E_K\),
   \[
   \Pr\left(\bigcup_k E_k\right)\le\sum_k\Pr(E_k).
   \]
4. **Cross-fitting/sample rotation.** Independent data blocks may take turns serving as holdout information while the complementary blocks are used for selection, provided the held-out block is excluded from its own selection rule.

## Repository-specific dependency chain

P98 depends on the following established repository results:

- **P92:** the declared negative three-minor sign pattern excludes the full mixed-prevalence P75 family, with exact global \(L_\infty\) witness radius \(1/24\).
- **P94:** finite-range dependent observations with one common marginal admit an exact-rational localized rejection radius.
- **P95:** predeclared drift regimes combine local P94 certificates with familywise error control.
- **P96:** an arbitrarily complex pilot-selected regime plan can be certified without an additional selection-complexity alpha penalty when the certification information is genuinely independent of the selection information.
- **P97:** same-data selection among a finite predeclared candidate family is valid only after paying an explicit simultaneous candidate-family multiplicity budget.

P98 keeps the P96 independence requirement for each fold but rotates which block is held out, then adds a fold-level simultaneous guarantee.

## P98 derivation

Let independent blocks be

\[
\mathcal D_1,\ldots,\mathcal D_K.
\]

For fold \(k\), the selected plan \(\widehat\Pi_k\) is measurable with respect to selection information

\[
\mathcal S_k\subseteq \sigma(\mathcal D_1,\ldots,\mathcal D_{k-1},\mathcal D_{k+1},\ldots,\mathcal D_K),
\]

and block \(\mathcal D_k\) is excluded from its own plan-selection rule. Mutual block independence gives

\[
\mathcal D_k\perp\mathcal S_k.
\]

If fold \(k\) receives exact failure budget \(\beta_k\), P96 gives conditionally

\[
\Pr(\mathcal A_k^c\mid\mathcal S_k)\le\beta_k.
\]

Taking expectations yields

\[
\Pr(\mathcal A_k^c)\le\beta_k.
\]

The fold events need not be independent because their selection information overlaps. If

\[
\sum_{k=1}^{K}\beta_k\le\alpha,
\]

then the union bound gives

\[
\Pr\left(\bigcap_{k=1}^{K}\mathcal A_k\right)
\ge 1-\sum_{k=1}^{K}\beta_k
\ge 1-\alpha.
\]

On this simultaneous event, any post-inspection selected fold remains valid, and rejection by any certified fold rejects the cross-fitted joint null that all selected fold-specific regime plans are P75-compatible under their declared assumptions.

## Exact balanced checkpoint

At global 95 percent confidence with two folds, two regimes per fold, and dependence range one,

\[
\alpha=\frac1{20},\qquad
\beta_k=\frac1{40},\qquad
\alpha_{kb}=\frac1{80}.
\]

The inherited P94 radius condition against the established witness radius \(1/24\) is therefore identical to the local P97 checkpoint:

\[
\frac{2\log(14/(1/80))}{2n}<\frac1{24^2},
\]

or equivalently

\[
n>576\log(1120).
\]

The exact-rational logarithm bracket machinery gives the first certifying integer

\[
\boxed{4045},
\]

and the first multiple of the 24-observation witness profile

\[
\boxed{4056}.
\]

With two regimes in each certification block, this gives

\[
\boxed{8090}\quad\text{and}\quad\boxed{8112}
\]

observations per fold. Because the two folds are genuinely distinct certification blocks, the total unique-data requirements are

\[
\boxed{16180}\quad\text{and}\quad\boxed{16224}.
\]

The complementary block is reused as selection information for the opposite fold and is not counted again.

## Scientific boundary

P98 requires genuine independence of the certification blocks and forbids leakage of a fold's own certification statistics into the plan later tested on that fold. It does not validate arbitrary splits of one dependent stream, misspecified dependence ranges, unrestricted within-regime drift, unbudgeted exploration of many cross-fitting schemes, model acceptance after non-rejection, consciousness identification, nonphysicality, or completion of the physical-to-experiential bridge.
