# P97 Equation and Novelty Provenance

## Scope

P97 combines standard finite-family simultaneous inference with the repository's exact P92-P95 rejection chain. The novelty claim is deliberately narrow: the proposition does not claim a new union bound. It identifies and proves the exact same-data selection-valid extension needed after P96, integrates it with the P95 regime certificate, and gives an executable exact-rational candidate-family accounting rule and checkpoint.

## Standard ingredients

The following ingredients are standard probability/statistics facts and are not claimed as repository-original:

1. **Union bound.** For events \(E_1,\ldots,E_J\),
   \[
   \Pr\left(\bigcup_j E_j\right)\le\sum_j\Pr(E_j).
   \]
2. **Simultaneous-to-selected implication.** If every member of a finite family of statements is correct on one event, then any data-dependent selection of one member is also correct on that event.
3. **Bonferroni-style equal spending.** A global budget \(\alpha\) may be split as \(\alpha/J\) over \(J\) candidate families and then further over their local tests.

## Repository-specific dependency chain

P97 depends on the following established repository results:

- **P92:** a negative product of the three declared minors excludes the full mixed-prevalence P75 family and the exact witness has global \(L_\infty\) distance \(1/24\).
- **P94:** declared finite-range dependence yields a local seven-cell confidence radius with exact-rational certification.
- **P95:** predeclared drift regimes combine local P94 gates with a regime-level union bound.
- **P96:** arbitrary pilot selection incurs no extra alpha penalty when the plan is frozen and certified on independent holdout information; P96 explicitly leaves same-data selection open.

P97 changes the selection design rather than the P92 witness. It fixes a finite candidate family before inspection, applies P95 to every member, and adds a second union bound across candidates.

## P97 derivation

For candidate \(j\), P95 gives a simultaneous event \(\mathcal A_j\) with

\[
\Pr(\mathcal A_j^c)\le\beta_j.
\]

If

\[
\sum_{j=1}^J\beta_j\le\alpha,
\]

then

\[
\Pr\left(\bigcap_{j=1}^J\mathcal A_j\right)
\ge
1-\sum_{j=1}^J\beta_j
\ge1-\alpha.
\]

For any data-dependent selected index \(\widehat J\in\{1,\ldots,J\}\),

\[
\bigcap_{j=1}^J\mathcal A_j\subseteq\mathcal A_{\widehat J},
\]

so

\[
\Pr(\mathcal A_{\widehat J})\ge1-\alpha.
\]

No independence between candidate certificates is used.

## Exact balanced checkpoint

At global 95 percent confidence with two candidate plans, two regimes per plan, and dependence range one,

\[
\alpha=\frac1{20},\qquad
\beta_j=\frac1{40},\qquad
\alpha_{jb}=\frac1{80}.
\]

The inherited P94 radius condition against the established witness radius \(1/24\) is

\[
\frac{2\log(14/(1/80))}{2n}<\frac1{24^2},
\]

or equivalently

\[
n>576\log(1120).
\]

The exact-rational logarithm bracket machinery identifies the first certifying integer as

\[
\boxed{4045},
\]

and the first multiple of the 24-observation witness profile as

\[
\boxed{4056}.
\]

For two balanced regimes on one reused dataset this gives 8090 and 8112 unique observations respectively. Candidate count is paid through the error budget, not by duplicating the dataset.

## Scientific boundary

P97 certifies selection only from the finite family fixed before inspection. It does not validate candidates generated after observing certification statistics, unbudgeted infinite search, misspecified dependence, unrestricted within-regime drift, model acceptance after non-rejection, consciousness identification, nonphysicality, or completion of the physical-to-experiential bridge.
