# P80 Equation and Provenance Record

## Purpose

This record documents the mathematical lineage of [Proposition 80](proposition_80_simplex_coupled_model_separation.md) and separates three categories that should not be conflated:

1. structure inherited from earlier propositions in this repository;
2. standard mathematical facts used as ingredients;
3. the repository-specific synthesis that produces the P80 certificate.

P80 tightens the [P78](proposition_78_certified_continuous_model_separation.md) boxwise lower bound for the continuous [P75](proposition_75_target_model_adequacy_overidentification.md) four-view binary latent family by enforcing probability normalization inside each exact interval relaxation.

---

## 1. Equation map

| Object | Formula or statement | Classification | Direct supporting route |
| --- | --- | --- | --- |
| P78 exact cell enclosure | $\ell_i(B)\le q_i(\theta)\le u_i(B)$ | Inherited exact multi-affine parameter-box enclosure | [P78 proof](proposition_78_certified_continuous_model_separation.md) |
| Probability normalization | $\sum_i q_i=1$ | Standard defining property of a finite probability law | [P80 definitions](proposition_80_simplex_coupled_model_separation.md#2-definitions) |
| P80 interval-simplex relaxation | $\mathcal R_\Delta(B)=\{q:\ell_i\le q_i\le u_i,\ \sum_iq_i=1\}$ | Repository synthesis of the P78 interval enclosure with normalization | [P80 definitions](proposition_80_simplex_coupled_model_separation.md#2-definitions) |
| Inclusion chain | $\mathcal M(B)\subseteq\mathcal R_\Delta(B)\subseteq\mathcal R_\square(B)$ | Exact set-theoretic consequence of P78 enclosure plus normalization | [P80 proof, Sections 4.1-4.2](proposition_80_simplex_coupled_model_separation.md#4-proof) |
| P78 coordinate threshold | $r_\square=\max_i d(\widehat p_i,[\ell_i,u_i])$ | Inherited product-box $L_\infty$ distance | [P78 proof](proposition_78_certified_continuous_model_separation.md) and [P80 Section 4.3](proposition_80_simplex_coupled_model_separation.md#43-exact-l_infty-feasibility-characterization) |
| Radius feasibility | $r\ge r_\square$ and $\sum_i\max(\ell_i,\widehat p_i-r)\le1\le\sum_i\min(u_i,\widehat p_i+r)$ | Coordinatewise overlap plus exact interval-sum feasibility | [P80 Section 4.3](proposition_80_simplex_coupled_model_separation.md#43-exact-l_infty-feasibility-characterization) |
| Exact P80 radius | $L_{80}(B)=\max(r_\square,r_A,r_C)$ | Repository exact-rational reduction to three one-dimensional thresholds | [P80 theorem and proof](proposition_80_simplex_coupled_model_separation.md#3-theorem) |
| P80 dominance | $L_{80}(B)\ge L_{78}(B)$ | Distance monotonicity under nested feasible sets | [P80 Section 4.2](proposition_80_simplex_coupled_model_separation.md#42-p80-dominates-the-p78-product-interval-relaxation) |
| Strict-improvement witness | $L_\Delta=1/15>1/30=L_\square$ | Constructive algebraic example showing normalization can strengthen the relaxation | [P80 Section 5](proposition_80_simplex_coupled_model_separation.md#5-strict-improvement-witness) |
| Global certificate | $\min_{B\in\mathcal B}L_{80}(B)\le d_\infty(\widehat p,\mathcal M_{4,2})$ | Branch-and-bound lower-bound assembly inherited from P78 with a tighter local relaxation | [P80 Section 4.4](proposition_80_simplex_coupled_model_separation.md#44-global-branch-and-bound-certificate) |
| Statistical handoff | $L_{80}>\overline\varepsilon_{79}$ | P80 model-distance lower bound compared with P79 sampling-radius upper certificate | [P80 Section 6](proposition_80_simplex_coupled_model_separation.md#6-p77p79-rejection-handoff) and [P79](proposition_79_certified_sampling_radius.md) |
| Exact arithmetic | `fractions.Fraction` throughout the certificate path | Implementation choice preventing floating-point direction ambiguity in certified quantities | [`simplex_coupled_model_separation.py`](../src/consciousness_bridge/simplex_coupled_model_separation.py) and [Python `fractions` documentation](https://docs.python.org/3/library/fractions.html) |

Every row provides a direct route to the theorem, proof, implementation, or source used to justify the statement. No table entry is intended to stand as an unsupported assertion.

---

## 2. Exact feasibility identity

For

\[
\mathcal R_\Delta
=
\{q:\ell_i\le q_i\le u_i,\ \sum_iq_i=1\},
\]

define the coordinatewise product-box threshold

\[
\boxed{
r_\square
=
\max_i d\!\left(\widehat p_i,[\ell_i,u_i]\right).
}
\]

For radius $r\ge r_\square$, every clipped interval

\[
[\max(\ell_i,\widehat p_i-r),\ \min(u_i,\widehat p_i+r)]
\]

is nonempty. A normalized vector exists inside those clipped intervals exactly when

\[
\sum_i\max(\ell_i,\widehat p_i-r)
\le1
\le
\sum_i\min(u_i,\widehat p_i+r).
\]

Therefore

\[
\boxed{
 d_\infty(\widehat p,\mathcal R_\Delta)
=
\inf\left\{
r\ge r_\square:
\sum_i\max(\ell_i,\widehat p_i-r)
\le1
\le
\sum_i\min(u_i,\widehat p_i+r)
\right\}.
}
\]

The two endpoint-sum functions are monotone piecewise-linear functions of $r$. With rational empirical probabilities and rational interval endpoints, their breakpoints and interpolation crossings are rational. This yields

\[
\boxed{
 d_\infty(\widehat p,\mathcal R_\Delta)
=
\max(r_\square,r_A,r_C),
}
\]

with exact rational arithmetic.

---

## 3. Why the dominance direction is rigorous

The true P75 box image, the P80 interval-simplex relaxation, and the P78 product relaxation satisfy

\[
\mathcal M(B)
\subseteq
\mathcal R_\Delta(B)
\subseteq
\mathcal R_\square(B).
\]

For any point $x$ and nested sets $A\subseteq B$,

\[
d(x,A)\ge d(x,B).
\]

Applying this twice gives

\[
L_{78}(B)
\le
L_{80}(B)
\le
 d_\infty(\widehat p,\mathcal M(B)).
\]

This chain is the central certification statement: P80 is **tighter than P78 but still conservative relative to the true model image**. The improvement comes from removing points that violate normalization, not from making a stronger assumption about the latent model.

---

## 4. What is repository-specific

The underlying ingredients are elementary: finite probability vectors are normalized, interval constraints define a box, and distance to a smaller nested feasible set cannot decrease. The repository-specific contribution of P80 is the complete exact-rational certification pipeline that:

- imports the exact P78 multi-affine cell intervals;
- restores normalization through $\mathcal R_\Delta(B)$;
- reduces the $L_\infty$ distance to the three thresholds $r_\square$, $r_A$, and $r_C$;
- inserts the stronger local bound into the established P78 branch-and-bound architecture;
- preserves the directionally safe P79 statistical handoff;
- exposes proof, code, tests, and figure geometry as directly inspectable artifacts.

This record does not claim that the normalization fact itself is novel.

---

## 5. Reproducibility routes

| Artifact | Purpose | Direct link |
| --- | --- | --- |
| Proposition 80 | Formal theorem, assumptions, proof, witness, and scope | [Open theorem](proposition_80_simplex_coupled_model_separation.md) |
| P80 implementation | Exact-rational interval-simplex distance and branch-and-bound certificate | [Open source](../src/consciousness_bridge/simplex_coupled_model_separation.py) |
| P80 unit tests | Feasibility, strict improvement, P80 $\ge$ P78, refinement, and scope guards | [Open tests](../tests/test_simplex_coupled_model_separation.py) |
| P80 figure test | Geometry and publication-layout guard | [Open geometry test](../tests/test_p80_figure_geometry.py) |
| P80 theorem figure | Visual explanation of the nested-set certificate | [Open SVG](figures/p80_simplex_coupled_model_separation.svg) |
| P78 predecessor | Exact cell intervals and continuous-family lower-bound architecture | [Open P78](proposition_78_certified_continuous_model_separation.md) |
| P79 numerical handoff | One-sided exact-rational sampling-radius certificate | [Open P79](proposition_79_certified_sampling_radius.md) |
| P77 statistical criterion | Full-law confidence-region separation requirement | [Open P77](proposition_77_full_law_model_set_separation.md) |

---

## 6. Scientific scope

P80 is not a theory of consciousness. It is a stronger numerical lower-bound certificate for the same declared P75 observed-law model family used in P78. It does not validate the P75 latent model, does not establish that the latent variable is experiential, does not make non-rejection equivalent to model acceptance, and does not close the physical-to-experiential bridge.

That boundary is part of the theorem record, not a disclaimer added after the mathematics.