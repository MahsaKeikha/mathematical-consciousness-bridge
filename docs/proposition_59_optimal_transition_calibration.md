# Proposition 59: optimal transition-calibration allocation

## Purpose

P58 gives simultaneous confidence intervals for unknown pairwise switching costs and propagates those intervals into a certified lower and upper route cost. P59 asks the next experimental-design question:

> If transition measurements themselves are costly, how should a fixed calibration budget be distributed across pairwise transitions to reduce a declared route-uncertainty surrogate as efficiently as possible?

P59 solves one explicit convex design problem exactly. It does **not** claim to solve the full combinatorial robust-routing experiment-design problem.

## Setup

For each calibrated pairwise transition edge \(e\), suppose the P58 confidence radius has the inverse-square-root form

\[
\rho_e(n_e)=\frac{a_e}{\sqrt{n_e}},
\]

where \(n_e>0\) is the continuous calibration effort assigned to that edge and \(a_e>0\) is a known coefficient. Under the bounded-observation Hoeffding model used by P58,

\[
\boxed{
a_e
=
B_e\sqrt{\frac12\log\frac{2}{\alpha_e}}.
}
\]

Let \(w_e>0\) be a declared sensitivity weight describing how strongly uncertainty on edge \(e\) contributes to the chosen route-uncertainty surrogate. The design objective is

\[
\boxed{
U(n)
=
\sum_{e\in E}\frac{w_ea_e}{\sqrt{n_e}}
}
\]

subject to

\[
\boxed{
\sum_{e\in E}n_e=N,
\qquad n_e>0.
}
\]

The weights may encode a fixed route, a route family relaxation, an empirical edge-importance score, or another predeclared surrogate. Their scientific meaning must be stated before the optimization result is interpreted.

## Proposition

Define

\[
b_e=w_ea_e,
\qquad
S=\sum_{j\in E}b_j^{2/3}.
\]

Then the optimization problem above is strictly convex and has the unique solution

\[
\boxed{
n_e^*
=
N\frac{b_e^{2/3}}{S}.
}
\]

The minimum achievable surrogate uncertainty is

\[
\boxed{
U^*(N)
=
\frac{S^{3/2}}{\sqrt{N}}.
}
\]

Equivalently, for any target uncertainty \(\varepsilon>0\), the continuous budget condition

\[
\boxed{
N
\ge
\frac{S^3}{\varepsilon^2}
}
\]

is sufficient and necessary for the optimum of this declared surrogate problem to satisfy \(U^*(N)\le\varepsilon\).

## Proof

Each term \(b_en_e^{-1/2}\) has second derivative

\[
\frac{3b_e}{4}n_e^{-5/2}>0,
\]

so the objective is strictly convex on the positive orthant. The affine budget constraint therefore admits at most one optimum.

Form the Lagrangian

\[
\mathcal L(n,\lambda)
=
\sum_e b_en_e^{-1/2}
+
\lambda\left(\sum_en_e-N\right).
\]

The first-order condition for every edge is

\[
-\frac12b_en_e^{-3/2}+\lambda=0.
\]

Hence

\[
n_e
=
\left(\frac{b_e}{2\lambda}\right)^{2/3}.
\]

Normalizing by \(\sum_en_e=N\) gives

\[
\boxed{
n_e^*=N\frac{b_e^{2/3}}{\sum_jb_j^{2/3}}.}
\]

Substitution yields

\[
U^*(N)
=
\sum_e\frac{b_e}{\sqrt{N b_e^{2/3}/S}}
=
\frac{\sqrt S}{\sqrt N}\sum_eb_e^{2/3}
=
\boxed{\frac{S^{3/2}}{\sqrt N}}.
\]

The target-budget formula follows by solving \(S^{3/2}/\sqrt N\le\varepsilon\).

## Interpretation

The allocation obeys a two-thirds-power law:

\[
\boxed{
n_e^*\propto(w_ea_e)^{2/3}.}
\]

An edge receives more calibration effort when it is both more uncertain per observation and more important to the declared routing surrogate. But the growth is sublinear: an edge whose effective coefficient is eight times larger receives four times, not eight times, as much continuous budget.

This creates a direct bridge from P58 uncertainty quantification to experiment planning. P58 says how noisy pairwise measurements affect robust route certification. P59 says how to spend a limited calibration budget optimally for one transparent surrogate objective.

## Scientific boundary

P59 is a resource-allocation theorem, not a consciousness theorem. It does not identify a physical quantity with experience, does not prove that the sensitivity weights are uniquely correct, does not solve adaptive edge discovery, and does not solve the full minimax combinatorial robust-route design problem. Those require additional assumptions and separate theorems.

## Implementation

- [`optimal_transition_calibration.py`](../src/consciousness_bridge/optimal_transition_calibration.py)
- [`test_optimal_transition_calibration.py`](../tests/test_optimal_transition_calibration.py)
