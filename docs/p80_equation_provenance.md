# P80 Equation and Provenance Record

## Purpose

Proposition 80 tightens the P78 boxwise lower bound used in the continuous P75 full-law separation problem by enforcing probability normalization inside each interval relaxation. This page classifies which ingredients are inherited, which are standard convex/probability facts, and which combination is specific to this repository.

## Equation map

| Object | Formula | Classification | Direct source |
| --- | --- | --- | --- |
| P78 cell enclosure | $\ell_i(B)\le q_i(\theta)\le u_i(B)$ | Inherited from P78 exact multi-affine box enclosure | [P78 proof](proposition_78_certified_continuous_model_separation.md) |
| Probability normalization | $\sum_i q_i=1$ | Standard probability-simplex constraint | Any finite discrete probability law |
| P80 interval-simplex relaxation | $\mathcal R_\Delta(B)=\{q:\ell_i\le q_i\le u_i,\sum_i q_i=1\}$ | Repository synthesis of P78 intervals with the simplex constraint | [P80 proof](proposition_80_simplex_coupled_model_separation.md) |
| Inclusion chain | $\mathcal M(B)\subseteq\mathcal R_\Delta(B)\subseteq\mathcal R_\square(B)$ | Immediate set-theoretic consequence of the P78 enclosures and normalization | [P80 proof](proposition_80_simplex_coupled_model_separation.md) |
| P80 dominance | $L_{80}(B)\ge L_{78}(B)$ | Distance-to-nested-sets monotonicity | [P80 proof](proposition_80_simplex_coupled_model_separation.md) |
| Radius feasibility | $\sum_i\max(\ell_i,\widehat p_i-r)\le1\le\sum_i\min(u_i,\widehat p_i+r)$ | Standard interval-sum feasibility specialized to an $L_\infty$ ball | [P80 proof](proposition_80_simplex_coupled_model_separation.md) |
| Exact rational crossing | first crossing of monotone piecewise-linear endpoint sums | Elementary exact piecewise-linear algebra; repository implementation uses `Fraction` | [`simplex_coupled_model_separation.py`](../src/consciousness_bridge/simplex_coupled_model_separation.py) |
| Global certificate | $\min_{B\in\mathcal B}L_{80}(B)\le d_\infty(\widehat p,\mathcal M_{4,2})$ | Branch-and-bound lower-bound assembly inherited from P78, with a tighter box relaxation | [P80 proof](proposition_80_simplex_coupled_model_separation.md) |
| Statistical handoff | $L_{80}>\overline\varepsilon_{79}$ | Combination of P80 model-distance lower bound and P79 sampling-radius upper bound | [P79](proposition_79_certified_sampling_radius.md), [P80](proposition_80_simplex_coupled_model_separation.md) |

## What is new here

The individual ingredients are elementary: probability vectors lie on a simplex, interval constraints define a box, and distance to a nested smaller feasible set cannot be smaller. The repository contribution in P80 is the exact certification pipeline that combines these facts with the P78 multi-affine cell intervals, derives the one-dimensional rational feasibility test for the interval-simplex $L_\infty$ distance, and inserts the stronger bound into the existing P77/P78/P79 branch-and-bound rejection chain without changing its inequality direction.

The core computational identity is

\[
\boxed{
 d_\infty(\widehat p,\mathcal R_\Delta)
=
\inf\left\{r\ge0:
\sum_i\max(\ell_i,\widehat p_i-r)\le1\le
\sum_i\min(u_i,\widehat p_i+r)
\right\}.
}
\]

Because the endpoint sums are monotone piecewise-linear functions with rational breakpoints whenever the inputs are rational, the implementation can compute the crossing radius exactly using rational arithmetic rather than a floating-point optimizer.

## Scientific scope

P80 is not a new theory of consciousness. It is a stronger numerical lower-bound certificate for the same P75 observed-law model family used in P78. It does not provide new evidence that the P75 latent variable is experiential and does not close the physical-to-experiential bridge.

## Reproducibility

- [P80 theorem and proof](proposition_80_simplex_coupled_model_separation.md)
- [P80 implementation](../src/consciousness_bridge/simplex_coupled_model_separation.py)
- [P80 tests](../tests/test_simplex_coupled_model_separation.py)
- [P80 figure](figures/p80_simplex_coupled_model_separation.svg)
