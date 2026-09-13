# P88 Equation Provenance

This record separates inherited mathematics, elementary derivations, standard external mathematics, repository-original constructions, exact computational evidence, and interpretation boundaries for Proposition 88.

## Scope

P88 uses the same declared P75 four-view binary latent target-measurement family and the same full-law $L_\infty$ distance as P75-P87. It introduces no new consciousness ontology and no new empirical assumption.

Its new object is the **convex hull of the complete sixteen-cell P75 law over one rational parameter box**. Because the P75 law map is vector-valued multi-affine, every law generated inside the box is a convex combination of box-vertex laws. Distance to this convex hull is therefore a rigorous lower bound on distance to the nonlinear model image.

P88 also proves that this convex-hull distance is the strongest possible certificate obtainable from arbitrary linear functionals of the full observed law, modulo constant shifts forced by probability-mass conservation.

The full hierarchy retains the recursive P87 baseline:

\[
L_{88}(B)=\max\{L_{87}(B),L_{88}^{\mathrm{ch}}(B)\}.
\]

Canonical dependencies:

- P75: declared four-view binary latent target-measurement family;
- P77: full-law model-set separation target;
- P78: exact multi-affine box structure and cellwise lower bounds;
- P79-P82: coupled and event-based box lower-bound refinements;
- P83-P87: parity-functional refinements;
- P88: complete full-law convex-hull linear certificate.

See [Proposition 88](proposition_88_exact_full_law_convex_hull_certificate.md), the [Claim-to-Source Scientific Audit Matrix](claim_source_matrix.md), and the [Claim, Evidence, and Citation Standard](claim_evidence_standard.md).

## 1. Inherited P75 law

For

\[
\theta=(\pi,q_{1,-},q_{1,+},\ldots,q_{4,-},q_{4,+}),
\]

P75 defines

\[
F_x(\theta)
=
(1-\pi)\prod_{j=1}^4q_{j,-}^{x_j}(1-q_{j,-})^{1-x_j}
+
\pi\prod_{j=1}^4q_{j,+}^{x_j}(1-q_{j,+})^{1-x_j}.
\]

This model assumption is inherited unchanged. P88 makes no new empirical assertion about the latent state.

## 2. Vector-valued multi-affinity

P78 already uses the fact that each scalar cell probability $F_x$ is multi-affine in the nine P75 parameters.

P88 uses the corresponding vector identity. On a box

\[
B=\prod_r[\ell_r,u_r],
\]

define the usual multilinear interpolation weights $w_v(\theta)$ on the box vertices. They satisfy

\[
w_v(\theta)\ge0,
\qquad
\sum_vw_v(\theta)=1.
\]

Coordinatewise multi-affinity gives, simultaneously for all sixteen cells,

\[
\boxed{
F(\theta)=\sum_{v\in\operatorname{Vert}(B)}w_v(\theta)F(v).
}
\]

Therefore

\[
F(B)\subseteq C_B:=\operatorname{conv}\{F(v):v\in\operatorname{Vert}(B)\}.
\]

Since every vertex image belongs to $F(B)$,

\[
\operatorname{conv}(F(B))=C_B.
\]

This vector-valued use of multi-affine interpolation is the structural basis of P88.

## 3. Convex-hull distance lower bound

Define

\[
L_{88}^{\mathrm{ch}}(B)
=
\inf_{Q\in C_B}\|\widehat P-Q\|_\infty.
\]

Because $F(B)\subseteq C_B$,

\[
\boxed{
L_{88}^{\mathrm{ch}}(B)
\le
\inf_{\theta\in B}\|\widehat P-F(\theta)\|_\infty.
}
\]

This is elementary set inclusion under distance minimization. It is a lower-bound statement, not an approximation of the nonlinear model family by equality.

## 4. Finite convex-combination LP

If the distinct vertex laws are $P^{(1)},\ldots,P^{(m)}$, then

\[
Q=\sum_k\lambda_kP^{(k)},
\qquad
\lambda_k\ge0,
\qquad
\sum_k\lambda_k=1
\]

parameterizes $C_B$.

Thus $L_{88}^{\mathrm{ch}}$ is exactly the LP

\[
\begin{aligned}
\min\;&t\\
\text{s.t. }&
-t\le\widehat P(x)-\sum_k\lambda_kP^{(k)}(x)\le t,
&&x\in\{0,1\}^4,\\
&\lambda_k\ge0,\\
&\sum_k\lambda_k=1.
\end{aligned}
\]

Finite-dimensional linear programming is standard external mathematics. The use of this LP as an exact P75 box lower bound is the P88 construction.

## 5. Complete linear full-law support form

For arbitrary $g\in\mathbb R^{16}$ define

\[
Q_g(P)=g^\top P.
\]

Probability-mass conservation gives

\[
\mathbf1^\top(P-Q)=0.
\]

Therefore, for any scalar $a$,

\[
Q_g(P)-Q_g(Q)
=(g-a\mathbf1)^\top(P-Q).
\]

The $\ell_1$-$\ell_\infty$ inequality yields

\[
|Q_g(P)-Q_g(Q)|
\le
\|g-a\mathbf1\|_1\|P-Q\|_\infty.
\]

Define

\[
\boxed{
D(g)=\min_a\|g-a\mathbf1\|_1.
}
\]

For nonconstant $g$, $D(g)>0$. Adding a constant to $g$ changes neither the separation nor $D(g)$, leaving a fifteen-dimensional quotient space.

Finite LP duality gives

\[
\boxed{
L_{88}^{\mathrm{ch}}(B)
=
\sup_{D(g)\le1}
\left[g^\top\widehat P-\max_vg^\top F(v)\right].
}
\]

This is the complete linear-support representation. It contains every individual cell indicator, event indicator, parity event, and finite linear combination thereof as a special case.

## 6. Exact certificate logic

A rational $g$ gives the exact lower witness

\[
\ell
=
\frac{
\operatorname{dist}(g^\top\widehat P,
[\min_vg^\top F(v),\max_vg^\top F(v)])
}{D(g)}.
\]

Thus

\[
L_{88}^{\mathrm{ch}}(B)\ge\ell.
\]

A rational convex combination of vertex laws gives $\bar P\in C_B$ and therefore

\[
L_{88}^{\mathrm{ch}}(B)
\le
\|\widehat P-\bar P\|_\infty.
\]

Matching exact rational values prove the optimum without requiring a floating-point solver to be trusted.

## 7. Why the P87 baseline is retained

$L_{88}^{\mathrm{ch}}$ is the strongest **linear-support** certificate against the convexified box image. P87 is a recursive published hierarchy containing a variety of earlier specialized lower bounds.

Rather than require a separate proof that every recursive predecessor is analytically dominated, P88 defines

\[
\boxed{
L_{88}(B)=\max\{L_{87}(B),L_{88}^{\mathrm{ch}}(B)\}.
}
\]

This preserves all previous guarantees and makes

\[
L_{88}(B)\ge L_{87}(B)
\]

pointwise by construction.

## 8. Exact strict linear witness

Use the common P86-P87 exact witness box and empirical law. In lexicographic four-bit outcome order, let

\[
g=\mathbf1_{1000}-\mathbf1_{1010}.
\]

The empirical law has

\[
\widehat P(1000)=\frac18,
\qquad
\widehat P(1010)=0,
\]

so

\[
g^\top\widehat P=\frac18.
\]

On the witness box $\pi=0$, and

\[
F_{1000}-F_{1010}
=q_{1,-}(1-q_{2,-})(1-q_{4,-})(1-2q_{3,-}).
\]

Because

\[
q_{3,-}\in\left[\frac12,1\right],
\]

this contrast is nonpositive throughout the box. Exact vertex enumeration gives

\[
[\min_vg^\top F(v),\max_vg^\top F(v)]
=
\left[-\frac9{16},0\right].
\]

The support gap is $1/8$.

The coefficient vector has one $+1$, one $-1$, and fourteen zeros. A median is zero, giving

\[
D(g)=2.
\]

Therefore

\[
\boxed{
ell=\frac{1/8}{2}=\frac1{16}.}
\]

## 9. Exact strict convex-hull point

P88 stores seven rational box vertices with weights

\[
\left(
\frac{10}{27},
\frac2{27},
\frac29,
\frac7{54},
\frac1{18},
\frac1{27},
\frac19
\right).
\]

They sum exactly to one. Their weighted law is

\[
\bar P=
\left(
0,\frac5{48},0,\frac5{48},
0,\frac1{16},0,\frac1{16},
\frac1{16},\frac5{48},\frac1{16},\frac7{48},
\frac1{48},\frac1{16},\frac1{48},\frac3{16}
\right).
\]

Direct exact evaluation gives

\[
\boxed{
\|\widehat P-\bar P\|_\infty=\frac1{16}.
}
\]

Thus the lower and upper witnesses match:

\[
\boxed{L_{88}^{\mathrm{ch}}(B)=\frac1{16}.}
\]

The recursive P87 value on the same box is

\[
L_{87}(B)=\frac1{96},
\]

so

\[
\boxed{
L_{88}(B)=\frac1{16}>\frac1{96}=L_{87}(B).
}
\]

## 10. Evidence classification

| P88 ingredient | Scientific role | Support |
| --- | --- | --- |
| P75 latent family | declared modeling assumption | P75 definition and implementation |
| scalar multi-affinity | inherited exact structure | P78 |
| vector convex-hull interpolation | elementary extension of multi-affinity | direct P88 derivation |
| convex-hull distance lower bound | elementary set inclusion | direct derivation |
| finite convex-combination LP | standard finite-dimensional optimization | direct P88 formulation |
| centered full-law transfer norm | mass conservation plus $\ell_1$-$\ell_\infty$ inequality | direct derivation; analogous to P85-P87 |
| equality with complete linear support optimum | standard finite LP duality | P88 dual derivation |
| two-cell $1/16$ lower witness | repository-original exact construction | exact implementation/tests |
| seven-vertex $1/16$ upper witness | repository-original exact construction | exact implementation/tests |
| strict $L_{87}<L_{88}$ | repository-original exact result | P87 regression plus matching P88 witnesses |

## 11. Reproducibility

Implementation:

`src/consciousness_bridge/full_law_convex_hull_certificate.py`

Tests:

`tests/test_full_law_convex_hull_certificate.py`

Proposition:

`docs/proposition_88_exact_full_law_convex_hull_certificate.md`

Figure:

`docs/figures/p88_exact_full_law_convex_hull_certificate.svg`

All strict-witness values are represented and verified with exact `fractions.Fraction` arithmetic.

## 12. Interpretation boundary

P88 is a conditional theorem about separation from the declared P75 model family. The convex hull is an outer relaxation of the nonlinear P75 box image, not a claim about ontology or consciousness.

P88 does not identify the P75 latent state with experience, prove consciousness nonphysical, establish that the convex hull equals the true model family, exhaust all possible physical descriptions, or solve the physical-to-experiential bridge.
