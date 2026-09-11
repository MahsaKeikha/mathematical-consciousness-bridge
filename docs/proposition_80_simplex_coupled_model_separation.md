# Proposition 80: Simplex-Coupled Box Certificate for Continuous P75 Separation

## Status

**Proved conditional computational theorem.** P80 strengthens the boxwise lower-bound relaxation introduced in [P78](proposition_78_certified_continuous_model_separation.md) for the same declared [P75](proposition_75_target_model_adequacy_overidentification.md) four-view binary latent family and the same $L_\infty$ observed-law metric. It changes neither the latent model nor the statistical assumptions of [P77](proposition_77_full_law_model_set_separation.md) and [P79](proposition_79_certified_sampling_radius.md).

The result is a **numerical-certification improvement**. It is not a theorem identifying a latent state with consciousness, and it does not close the physical-to-experiential bridge.

---

## 1. Motivation

P78 encloses each of the sixteen observed-cell probabilities over a parameter box $B\subset[0,1]^9$ by exact rational intervals

\[
\ell_i(B)\le q_i(\theta)\le u_i(B),\qquad i=1,\ldots,16.
\]

The original P78 boxwise lower bound treats those intervals as an uncoupled Cartesian product. Every P75 law, however, is a probability vector and therefore also satisfies

\[
\sum_{i=1}^{16}q_i=1.
\]

P80 retains this normalization constraint inside the relaxation. The resulting feasible set is smaller than the P78 Cartesian-product relaxation but still contains every P75 law generated inside the parameter box. Its distance from the empirical law is therefore a valid lower bound on distance to the true nonlinear model image, and it can only improve the corresponding P78 box bound.

---

## 2. Definitions

Let $\widehat p\in\Delta_{15}$ be the empirical sixteen-cell probability law. For a P78 parameter box $B$, define the true box image

\[
\mathcal M(B)=\{q(\theta):\theta\in B\},
\]

where $q(\theta)$ is the P75 four-view observed-law map.

Let $[\ell_i(B),u_i(B)]$ denote the exact P78 range of observed cell $i$ over $B$. The P78 uncoupled relaxation is

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
\ell_i(B)\le q_i\le u_i(B),\quad
\sum_{i=1}^{16}q_i=1
\right\}.
}
\]

Because every P75 observed law is normalized,

\[
\boxed{
\mathcal M(B)
\subseteq
\mathcal R_{\Delta}(B)
\subseteq
\mathcal R_{\square}(B).
}
\]

Define the P80 box lower bound

\[
L_{80}(B)
=
d_\infty\!\left(\widehat p,\mathcal R_{\Delta}(B)\right).
\]

The corresponding P78 product-box lower bound is

\[
L_{78}(B)
=
d_\infty\!\left(\widehat p,\mathcal R_{\square}(B)\right)
=
\max_i d\!\left(\widehat p_i,[\ell_i(B),u_i(B)]\right).
\]

---

## 3. Theorem

For every admissible P78 parameter box $B$:

1. $L_{80}(B)$ is a rigorous lower bound on the distance from $\widehat p$ to the true P75 model image over $B$;
2. $L_{80}(B)\ge L_{78}(B)$;
3. $L_{80}(B)$ is exactly computable in rational arithmetic from $\widehat p$, $\ell(B)$, and $u(B)$;
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

where $\mathcal M_{4,2}$ denotes the complete continuous P75 four-view binary latent family;
5. on the same active partition,

\[
\boxed{
L_{80}(\mathcal B)\ge L_{78}(\mathcal B).
}
\]

The exact boxwise distance is

\[
\boxed{
L_{80}(B)=\max(r_{\square},r_A,r_C),
}
\]

where $r_{\square}=L_{78}(B)$ is the coordinatewise overlap threshold, $r_A$ is the first radius at which the summed lower endpoints fall to at most one, and $r_C$ is the first radius at which the summed upper endpoints rise to at least one.

---

## 4. Proof

### 4.1 Set inclusion fixes the certification direction

For every $\theta\in B$, the exact P78 cell enclosure gives

\[
\ell_i(B)\le q_i(\theta)\le u_i(B)
\]

for every observed cell. Because $q(\theta)$ is a probability law,

\[
\sum_iq_i(\theta)=1.
\]

Therefore

\[
q(\theta)\in\mathcal R_{\Delta}(B),
\]

hence

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

### 4.2 P80 dominates the P78 product-interval relaxation

By construction,

\[
\mathcal R_{\Delta}(B)
\subseteq
\mathcal R_{\square}(B).
\]

Distance is monotone under nested feasible sets in the opposite direction, therefore

\[
d_\infty(\widehat p,\mathcal R_{\Delta}(B))
\ge
d_\infty(\widehat p,\mathcal R_{\square}(B)).
\]

The right-hand side is exactly the P78 coordinatewise interval lower bound. Hence

\[
\boxed{L_{80}(B)\ge L_{78}(B).}
\]

The inequality can be strict because the nearest point in the Cartesian product need not satisfy probability normalization.

### 4.3 Exact $L_\infty$ feasibility characterization

Fix a radius $r\ge0$. A vector $q\in\mathcal R_{\Delta}(B)$ can satisfy

\[
\|q-\widehat p\|_\infty\le r
\]

only if every clipped coordinate interval

\[
I_i(r)
=
\left[
\max(\ell_i,\widehat p_i-r),
\min(u_i,\widehat p_i+r)
\right]
\]

is nonempty.

The smallest radius that guarantees coordinatewise nonemptiness is precisely the P78 product-box distance

\[
\boxed{
r_{\square}
=
\max_i d\!\left(\widehat p_i,[\ell_i,u_i]\right)
=L_{78}(B).
}
\]

Once every $I_i(r)$ is nonempty, a choice $q_i\in I_i(r)$ with total mass one exists if and only if one lies between the sum of the lower endpoints and the sum of the upper endpoints. Define

\[
A(r)
:=
\sum_i\max(\ell_i,\widehat p_i-r),
\qquad
C(r)
:=
\sum_i\min(u_i,\widehat p_i+r).
\]

Then radius $r$ is feasible exactly when

\[
\boxed{
r\ge r_{\square},
\qquad
A(r)\le1\le C(r).
}
\]

The function $A(r)$ is continuous, monotone nonincreasing, and piecewise linear. Its positive breakpoints are among the rational values $\widehat p_i-\ell_i$. The function $C(r)$ is continuous, monotone nondecreasing, and piecewise linear, with positive breakpoints among $u_i-\widehat p_i$.

Let $r_A$ be the first radius at which $A(r)\le1$, and let $r_C$ be the first radius at which $C(r)\ge1$. These crossing radii are obtained by exact linear interpolation inside rational breakpoint intervals. Therefore

\[
\boxed{
L_{80}(B)=\max(r_{\square},r_A,r_C).
}
\]

When $\widehat p$, $\ell$, and $u$ are rational, every breakpoint, slope, interpolation step, and final radius is rational. The implementation therefore uses [`fractions.Fraction`](https://docs.python.org/3/library/fractions.html) throughout and does not require a floating-point optimizer.

### 4.4 Global branch-and-bound certificate

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

Explicit admissible P75 parameter vectors remain valid global upper-bound witnesses exactly as in P78. The implementation also retains the original P78 active-box lower bounds so that the established P78 mesh-width upper certificate can still be used without assuming a new convergence rate for the tightened P80 relaxation.

This proves the proposition. $\square$

---

## 5. Strict-improvement witness

A three-coordinate probability example shows why normalization coupling can matter. Let

\[
\widehat p=(1/3,1/3,1/3)
\]

with coordinate intervals

\[
[0,3/10],\qquad [0,3/10],\qquad [0,1].
\]

The uncoupled product-box distance is

\[
L_{\square}=1/30,
\]

because the first two coordinates individually need move only from $1/3$ to $3/10$.

Under the simplex constraint, however, the third coordinate must absorb the total mass removed from the first two coordinates. The exact coupled distance is

\[
L_{\Delta}=1/15,
\]

and therefore

\[
\boxed{L_{\Delta}=2L_{\square}.}
\]

This witness establishes that strict improvement is possible. It is an algebraic illustration, not a P75 empirical data claim and not evidence about consciousness.

---

## 6. P77/P79 rejection handoff

P80 changes only the model-distance lower-bound side of the established rejection comparison. Let $\overline\varepsilon_{79}$ be the [P79](proposition_79_certified_sampling_radius.md) certified upper envelope for the P77 finite-alphabet sampling radius. Then

\[
\boxed{
L_{80}(\mathcal B)>\overline\varepsilon_{79}
\Longrightarrow
 d_\infty(\widehat p,\mathcal M_{4,2})
>
\varepsilon_{n,K}(\alpha).
}
\]

The direction is deliberately one-sided: P80 supplies a certified **lower** bound on model distance and P79 supplies a certified **upper** bound on sampling uncertainty. Failure of the strict inequality is inconclusive and must not be reported as model validation.

---

## 7. What P80 adds and what it does not add

P80 adds a tighter exact-rational relaxation for the same continuous P75 observed-law family used in P78. The new ingredient is probability-simplex coupling inside each exact interval box. The theorem does **not** change the target model, introduce a new consciousness variable, validate conditional independence, prove the P75 latent state is experiential, or establish that a failed P75 model implies physics is incomplete.

The physical-to-experiential bridge therefore remains open.

---

## 8. Reproducibility map

| Research object | Direct route |
| --- | --- |
| P80 implementation | [`src/consciousness_bridge/simplex_coupled_model_separation.py`](../src/consciousness_bridge/simplex_coupled_model_separation.py) |
| P80 unit and certificate tests | [`tests/test_simplex_coupled_model_separation.py`](../tests/test_simplex_coupled_model_separation.py) |
| Figure geometry guard | [`tests/test_p80_figure_geometry.py`](../tests/test_p80_figure_geometry.py) |
| P80 equation and provenance classification | [`docs/p80_equation_provenance.md`](p80_equation_provenance.md) |
| P80 theorem figure | [`docs/figures/p80_simplex_coupled_model_separation.svg`](figures/p80_simplex_coupled_model_separation.svg) |
| P78 continuous-family predecessor | [Proposition 78](proposition_78_certified_continuous_model_separation.md) |
| P79 one-sided sampling-radius certificate | [Proposition 79](proposition_79_certified_sampling_radius.md) |
| P77 full-law separation criterion | [Proposition 77](proposition_77_full_law_model_set_separation.md) |
| P75 declared target-model family | [Proposition 75](proposition_75_target_model_adequacy_overidentification.md) |

For equation-level provenance and source classification, use the [P80 equation and provenance record](p80_equation_provenance.md).