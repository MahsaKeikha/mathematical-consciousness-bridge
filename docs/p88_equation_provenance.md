# P88 Equation Provenance

This record separates inherited concentration machinery, inherited P87 algebra, and the new sample-splitting argument. P88 is the proved conditional finite-sample frontier theorem after full repository regression audit.

## 1. Inherited P87 functional algebra

For a fixed four-event primitive parity functional

\[
Q(p)=\sum_i c_iP_p(H_{J_i}),
\]

P87 supplies the exact empirical value, the exact P75 parameter-box interval `I_B(Q)`, the exact sixteen-cell score `g_Q(x)`, and the centered transfer norm

\[
D(Q)=\min_a\sum_x|g_Q(x)-a|.
\]

Direct dependency: `proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md`.

## 2. Inherited P77 Hoeffding concentration

For IID variables `Y_k` in `[0,1]`, the standard two-sided Hoeffding inequality gives

\[
\Pr\left(\left|\frac1n\sum_kY_k-EY_k\right|>t\right)\le2e^{-2nt^2}.
\]

P88 does not alter Hoeffding. It applies the bound to one held-out score after the entire tested box/functional pair has been frozen independently of the validation data.

## 3. Conditional-on-discovery frozen-pair argument

Let `D` denote discovery data and let

\[
(B_D,Q_D)
\]

be any P75-box/P87-functional pair measurable with respect to `D`. Let validation observations be IID from population law `p` and independent of `D`.

Conditional on `D`, both the model interval `I_{B_D}(Q_D)` and score `g_D` are fixed. If

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

The conditional upper bound is `alpha` for every discovery realization. The tower property therefore yields the same unconditional statement. Because only one frozen functional is tested on validation data, no union bound over the 39,600-function discovery family is required. Allowing the box itself to depend on validation data would break this conditional-fixed-object argument unless a separate correction were proved.

## 4. Inherited P79 one-sided numerical certification

P79 constructs an exact rational upper envelope for

\[
\sqrt{\frac{\log(2K/\alpha)}{2n}}.
\]

P88 invokes the same implementation with `K=1`, producing a certified rational upper bound on

\[
\sqrt{\frac{\log(2/\alpha)}{2n}}.
\]

Multiplication by exact score width `R_D` preserves the upper direction.

## 5. Distance-to-interval contraction

For any closed interval `I`, distance is 1-Lipschitz:

\[
\operatorname{dist}(u,I)\ge\operatorname{dist}(v,I)-|u-v|.
\]

Hence

\[
\operatorname{dist}(Q_D(p),I_{B_D}(Q_D))
\ge
[\widehat\Delta_D-\overline\varepsilon_D]_+.
\]

## 6. Full-law transfer and exact scope

For every P75 law `q` generated inside `B_D`,

\[
Q_D(q)\in I_{B_D}(Q_D)
\]

and P87 gives

\[
|Q_D(p)-Q_D(q)|\le D(Q_D)\|p-q\|_\infty.
\]

Therefore, on the validation confidence event,

\[
\boxed{
\inf_{q\in\mathcal M_{B_D}}\|p-q\|_\infty
\ge
\frac{[\widehat\Delta_D-\overline\varepsilon_D]_+}{D(Q_D)}.
}
\]

This bound concerns `M_{B_D}`. It becomes a global P75-family statement only if `B_D` itself contains the full admissible parameter region or a separately certified covering argument extends the result across all required boxes.

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
[\widehat\Delta_Q-\overline\varepsilon_Q]_+=3509245/50331648,
\]

and with `D(Q)=20`,

\[
\boxed{L_{88,\mathrm{heldout}}=701849/201326592>0.}
\]

The exact sixteen-cell P79 radius on the same sample is `615553/16777216`, while the available P87 empirical distance lower bound for this box is `1/96`; this specific lower-bound-to-global-radius handoff is therefore inconclusive even though the held-out functional route rejects the frozen box.

## 8. Evidence classification

| Ingredient | Role | Support |
| --- | --- | --- |
| P87 exact functional interval | inherited deterministic model algebra | P87 proof and implementation |
| P87 centered transfer norm | inherited deterministic distance transfer | P87 proof and implementation |
| scalar Hoeffding inequality | inherited finite-sample concentration | P77 concentration layer |
| rational upper radius | inherited one-sided numerical certification | P79 implementation |
| conditioning on an independent discovery-frozen box/functional pair | new statistical argument | conditional Hoeffding plus tower property |
| held-out population gap lower bound | new theorem consequence | interval-distance 1-Lipschitz property |
| `701849/201326592` strict witness | repository-original exact regression result | P88 tests |

## 9. Scientific boundary

The implementation cannot establish that discovery and validation datasets were truly independent, nor can it prove that the tested box and functional were frozen before validation was inspected; those are experimental-provenance obligations. The result is box-specific unless a valid global covering argument is supplied. It does not define consciousness, identify the P75 latent variable with experience, establish nonphysicality, or solve the physical-to-experiential bridge.


## 10. Exact design-threshold provenance

The ideal scalar Hoeffding inequality $R\sqrt{\log(2/\alpha)/(2n)}<\Delta$
rearranges to

\[
n>\frac{R^2\log(2/\alpha)}{2\Delta^2}.
\]

The repository implementation does not round this expression to decide the
certificate.  It searches integer $n$ and evaluates the P79 rational upper
envelope at each candidate.  For $R=5$, $\Delta=5/24$, $\alpha=1/20$, 12
series terms, and 24 square-root bits, exact regression checks prove $n=1062$
is insufficient and $n=1063$ is sufficient.
