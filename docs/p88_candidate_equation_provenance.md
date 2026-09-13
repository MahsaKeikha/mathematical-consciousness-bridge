# Candidate P88 Equation Provenance

This record separates inherited concentration machinery, inherited P87 algebra, and the new sample-splitting argument. Candidate P88 remains unpromoted until its implementation and full repository regression gates are green.

## 1. Inherited P87 functional algebra

For a fixed four-event primitive parity functional

\[
Q(p)=\sum_i c_iP_p(H_{J_i}),
\]

P87 supplies:

- the exact empirical value;
- an exact P75 parameter-box interval `I_B(Q)` by multi-affine endpoint enumeration;
- the exact sixteen-cell score `g_Q(x)` induced by the parity indicators; and
- the centered transfer norm `D(Q)=min_a sum_x |g_Q(x)-a|` used to convert functional mismatch to a full-law L-infinity distance lower bound.

Direct dependency: `proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md`.

## 2. Inherited P77 Hoeffding concentration

P77 uses the standard two-sided Hoeffding inequality. For IID variables `Y_k` in `[0,1]`,

\[
\Pr\left(
\left|\frac1n\sum_kY_k-EY_k\right|>t
\right)
\le2e^{-2nt^2}.
\]

Candidate P88 does not strengthen or alter Hoeffding. It rescales one selected P87 score to `[0,1]` after that score has been fixed independently of the validation data.

## 3. New conditional-on-discovery selection argument

Let `D` denote discovery data and let `Q_D` be any P87 functional measurable with respect to `D`. Let the validation observations be IID from population law `p` and independent of `D`.

Conditional on `D`, `Q_D` is fixed. If its exact cell-score width is

\[
R_D=g_{\max,D}-g_{\min,D},
\]

then Hoeffding gives

\[
\Pr\left(
|\widehat Q_V-Q_D(p)|
>
R_D\sqrt{\frac{\log(2/\alpha)}{2n}}
\;\middle|\;D
\right)
\le\alpha.
\]

The conditional upper bound is the same `alpha` for every discovery realization. The tower property therefore gives the unconditional statement

\[
\Pr\left(
|\widehat Q_V-Q_D(p)|
\le
R_D\sqrt{\frac{\log(2/\alpha)}{2n}}
\right)
\ge1-\alpha.
\]

This is the key new theorem step. Because only the frozen `Q_D` is tested on validation data, no union bound over the discovery search family appears.

## 4. Inherited P79 one-sided numerical certification

P79 constructs an exact rational upper envelope for

\[
\sqrt{\frac{\log(2K/\alpha)}{2n}}.
\]

Candidate P88 invokes the same implementation with `K=1`, giving a certified rational upper bound on

\[
\sqrt{\frac{\log(2/\alpha)}{2n}}.
\]

Multiplication by the exact integer/rational score width `R_D` preserves the upper direction.

## 5. Distance-to-interval contraction

For any closed interval `I` and scalars `u,v`,

\[
\operatorname{dist}(u,I)
\ge
\operatorname{dist}(v,I)-|u-v|.
\]

This follows from the fact that distance to a nonempty closed set is 1-Lipschitz. Applying it with `u=Q_D(p)` and `v=hat Q_V` yields

\[
\operatorname{dist}(Q_D(p),I_B(Q_D))
\ge
[\widehat\Delta_D-\overline\varepsilon_D]_+.
\]

## 6. Full-law transfer

For every P75 law `q` generated in the parameter box, `Q_D(q)` lies inside `I_B(Q_D)`. P87's centered coefficient inequality gives

\[
|Q_D(p)-Q_D(q)|\le D(Q_D)\|p-q\|_\infty.
\]

Therefore, on the validation confidence event,

\[
\inf_{q\in\mathcal M_B}\|p-q\|_\infty
\ge
\frac{[\widehat\Delta_D-\overline\varepsilon_D]_+}{D(Q_D)}.
\]

## 7. Exact regression witness

For the stored P87 functional with coefficients `(1,-1,-2,2)`, the exact score values over the sixteen cells have minimum `-3`, maximum `2`, and width `5`. With `n=2400`, `alpha=1/20`, 12 P79 series terms, and 24 dyadic square-root bits:

\[
\overline r=465101/16777216,
\]

\[
\overline\varepsilon_Q=2325505/16777216,
\]

\[
\widehat\Delta_Q=5/24,
\]

\[
[\widehat\Delta_Q-\overline\varepsilon_Q]_+
=3509245/50331648,
\]

and with `D(Q)=20`,

\[
\boxed{L_{88,\mathrm{heldout}}=701849/201326592>0.}
\]

The exact sixteen-cell P79 radius on the same sample is `615553/16777216`, while the available P87 empirical distance lower bound is `1/96`; this specific global-radius handoff is therefore inconclusive even though the held-out functional route rejects.

## 8. Evidence classification

| Ingredient | Role | Support |
| --- | --- | --- |
| P87 exact functional interval | inherited deterministic model algebra | P87 proof and implementation |
| P87 centered transfer norm | inherited deterministic distance transfer | P87 proof and implementation |
| scalar Hoeffding inequality | inherited finite-sample concentration | P77 concentration layer |
| rational upper radius | inherited one-sided numerical certification | P79 implementation |
| conditioning on independent discovery selection | new statistical argument | conditional Hoeffding plus tower property |
| held-out population gap lower bound | new theorem consequence | interval-distance Lipschitz inequality |
| `701849/201326592` strict witness | repository-original exact regression result | candidate P88 tests |

## 9. Scientific boundary

The implementation cannot establish that two datasets were truly independent; that must come from experimental provenance. The result does not define consciousness, does not identify the P75 latent variable with experience, does not establish nonphysicality, and does not solve the physical-to-experiential bridge.
