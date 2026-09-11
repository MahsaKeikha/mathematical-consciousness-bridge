# Proposition 80: Simplex-Coupled Box Certificate for Continuous P75 Separation

## Status

**Proved conditional computational theorem.** P80 strengthens the boxwise lower-bound relaxation used by P78 for the same declared P75 four-view binary latent family and the same $L_\infty$ observed-law distance. It changes neither the latent model nor the statistical assumptions of P77/P79.

## Motivation

P78 encloses each of the sixteen observed-cell probabilities over a parameter box $B\subset[0,1]^9$ by exact rational intervals

\[
\ell_i(B)\le q_i(\theta)\le u_i(B),\qquad i=1,\ldots,16.
\]

Its original boxwise lower bound treats those intervals as an uncoupled Cartesian product. Every P75 law, however, is a probability vector and therefore satisfies

\[
\sum_{i=1}^{16}q_i=1.
\]

P80 retains this normalization constraint inside the box relaxation. The resulting feasible set is smaller, so its distance from the empirical law can only increase while remaining a valid lower bound on distance to the true nonlinear model image.

---

## Definitions

Let $\widehat p\in\Delta_{15}$ be the empirical sixteen-cell law. For a P78 parameter box $B$, define the true box image

\[
\mathcal M(B)
=
\{q(\theta):\theta\in B\},
\]

and let $[\ell_i(B),u_i(B)]$ be the exact P78 coordinate ranges.

The original uncoupled P78 relaxation is

\[
\mathcal R_{\square}(B)
=
\prod_{i=1}^{16}[\ell_i(B),u_i(B)].
\]

P80 defines the **simplex-coupled relaxation**

\[
\boxed{
\mathcal R_{\Delta}(B)
=
\left\{
q\in\mathbb R^{16}:
\ell_i(B)\le q_i\le u_i(B),\ 
\sum_{i=1}^{16}q_i=1
\right\}.
}
\]

Because every P75 observed law is normalized,

\[
\boxed{
\mathcal M(B)\subseteq\mathcal R_{\Delta}(B)
\subseteq\mathcal R_{\square}(B).
}
\]

Define the P80 box lower bound

\[
L_{80}(B)
=
d_\infty\!\left(\widehat p,\mathcal R_{\Delta}(B)\right).
\]

---

## Theorem

For every admissible P78 parameter box $B$:

1. $L_{80}(B)$ is a rigorous lower bound on the distance from $\widehat p$ to the true P75 model image over $B$;
2. $L_{80}(B)$ dominates the P78 coordinatewise box lower bound $L_{78}(B)$;
3. $L_{80}(B)$ can be computed exactly in rational arithmetic from the P78 interval endpoints and $\widehat p$;
4. for any finite partition $\mathcal B$ of $[0,1]^9$,

\[
\boxed{
L_{80}(\mathcal B)
:=
\min_{B\in\mathcal B}L_{80}(B)
\le
d_\infty(\widehat p,\mathcal M_{4,2}),
}
\]

where $\mathcal M_{4,2}$ is the complete continuous P75 four-view binary latent family.

Moreover,

\[
\boxed{
L_{80}(\mathcal B)\ge L_{78}(\mathcal B)
}
\]

for the same active partition.

---

## Proof

### 1. Set inclusion gives the certification direction

For every $\theta\in B$, P78's exact cell-range construction gives

\[
\ell_i(B)\le q_i(\theta)\le u_i(B)
\]

for every observed cell. Because $q(\theta)$ is a probability law,

\[
\sum_i q_i(\theta)=1.
\]

Therefore

\[
q(\theta)\in\mathcal R_{\Delta}(B),
\]

and hence

\[
\mathcal M(B)\subseteq\mathcal R_{\Delta}(B).
\]

Distance to a superset cannot exceed distance to the contained set, so

\[
\boxed{
L_{80}(B)
=
d_\infty(\widehat p,\mathcal R_{\Delta}(B))
\le
d_\infty(\widehat p,\mathcal M(B)).
}
\]

Thus P80 preserves the lower-bound direction required by P77.

### 2. P80 dominates the P78 product-interval relaxation

By construction,

\[
\mathcal R_{\Delta}(B)
\subseteq
\mathcal R_{\square}(B).
\]

Therefore

\[
d_\infty(\widehat p,\mathcal R_{\Delta}(B))
\ge
d_\infty(\widehat p,\mathcal R_{\square}(B)).
\]

The right-hand side is exactly the P78 coordinatewise interval lower bound,

\[
L_{78}(B)
=
\max_i d\!\left(\widehat p_i,[\ell_i(B),u_i(B)]\right).
\]

Hence

\[
\boxed{L_{80}(B)\ge L_{78}(B).}
\]

The inequality can be strict because the nearest point in the Cartesian product may fail the normalization constraint.

### 3. Exact $L_\infty$ feasibility characterization

Fix $r\ge0$. There exists a vector $q\in\mathcal R_{\Delta}(B)$ satisfying

\[
\|q-\widehat p\|_\infty\le r
\]

if and only if each coordinate can be chosen from

\[
I_i(r)
=
[\max(\ell_i,\widehat p_i-r),\ 
\min(u_i,\widehat p_i+r)]
\]

and the selected coordinates can sum to one.

For intervals on the real line, a target total of one is attainable exactly when the sum of the lower endpoints does not exceed one and the sum of the upper endpoints is at least one. Therefore radius $r$ is feasible if and only if

\[
\boxed{
A(r):=\sum_i\max(\ell_i,\widehat p_i-r)\le1
\le
C(r):=\sum_i\min(u_i,\widehat p_i+r).
}
\]

$A(r)$ is continuous, monotone nonincreasing, and piecewise linear. Its breakpoints are the positive rational values $\widehat p_i-\ell_i$. Similarly, $C(r)$ is continuous, monotone nondecreasing, and piecewise linear with positive rational breakpoints $u_i-\widehat p_i$.

Consequently the first radius at which $A(r)\le1$ and the first radius at which $C(r)\ge1$ can each be found exactly by linear interpolation on rational breakpoint intervals. If these radii are $r_A$ and $r_C$, then

\[
\boxed{
L_{80}(B)=\max(r_A,r_C).
}
\]

When $\widehat p$, $\ell$, and $u$ are rational, every breakpoint, slope, interpolation step, and final radius is rational. The implementation therefore uses `fractions.Fraction` throughout.

### 4. Global branch-and-bound certificate

Let $\mathcal B$ be any finite partition of the full parameter cube. Since

\[
\mathcal M_{4,2}
=
\bigcup_{B\in\mathcal B}\mathcal M(B),
\]

we have

\[
d_\infty(\widehat p,\mathcal M_{4,2})
=
\min_{B\in\mathcal B}
 d_\infty(\widehat p,\mathcal M(B)).
\]

Applying the boxwise P80 lower bound gives

\[
\boxed{
\min_{B\in\mathcal B}L_{80}(B)
\le
d_\infty(\widehat p,\mathcal M_{4,2}).
}
\]

Because $L_{80}(B)\ge L_{78}(B)$ for each active box,

\[
\boxed{
L_{80}(\mathcal B)
\ge
L_{78}(\mathcal B).
}
\]

Explicit admissible P75 parameter vectors remain valid upper-bound witnesses exactly as in P78. The implementation also retains the original P78 active-box lower bounds so P78's established mesh-width upper certificate can still be used without assuming a new convergence rate for the tightened relaxation.

This proves the proposition. $\square$

---

## Strict-improvement witness

A simple three-coordinate probability example shows why the normalization coupling can matter. Let

\[
\widehat p=(1/3,1/3,1/3),
\]

with coordinate intervals

\[
[0,3/10],\qquad [0,3/10],\qquad [0,1].
\]

The uncoupled product-box distance is

\[
L_{\square}=1/30,
\]

because the first two coordinates individually need only move down from $1/3$ to $3/10$.

But under the simplex constraint the third coordinate must absorb the total removed mass. The exact coupled distance is

\[
L_{\Delta}=1/15,
\]

so

\[
\boxed{L_{\Delta}=2L_{\square}.}
\]

This witness is algebraic and illustrative. It is not itself a P75 data example and makes no empirical claim about consciousness.

---

## P77/P79 rejection handoff

P80 changes only the model-distance lower-bound side of the already established rejection comparison. If $\overline\varepsilon_{79}$ is the P79 certified upper envelope for the P77 finite-alphabet sampling radius, then

\[
\boxed{
L_{80}(\mathcal B)>\overline\varepsilon_{79}
\Longrightarrow
 d_\infty(\widehat p,\mathcal M_{4,2})
>
\varepsilon_{n,K}(\alpha).
}
\]

Failure of this strict inequality is inconclusive. It does not validate the model.

---

## Scientific boundary

P80 is a tighter numerical certificate for one declared observed-law model family. It does **not** establish that the P75 latent variable is experiential, does **not** prove that the conditional-independence measurement model is correct in a new domain, and does **not** solve the physical-to-experiential bridge.

## Reproducibility links

- Implementation: [`simplex_coupled_model_separation.py`](../src/consciousness_bridge/simplex_coupled_model_separation.py)
- Tests: [`test_simplex_coupled_model_separation.py`](../tests/test_simplex_coupled_model_separation.py)
- P78 predecessor: [Proposition 78](proposition_78_certified_continuous_model_separation.md)
- P79 numerical handoff: [Proposition 79](proposition_79_certified_sampling_radius.md)
- Equation/provenance record: [P80 provenance](p80_equation_provenance.md)
- Theorem figure: [P80 simplex-coupled certificate](figures/p80_simplex_coupled_model_separation.svg)
