# Proposition 88: Exact Full-Law Convex-Hull Linear Certificate

## Status

**Proved conditional theorem with an exact rational strict-witness optimality certificate.** P88 strengthens the P87 boxwise model-separation hierarchy for the same declared P75 four-view binary latent target-measurement family and the same full-law $L_\infty$ distance.

The key step is not another parity coefficient enumeration. P88 uses the fact that the complete sixteen-cell P75 law is **vector-valued multi-affine** in the nine model parameters. On every axis-aligned parameter box $B$, the entire nonlinear model image lies inside the convex hull of the finitely many parameter-box vertex laws.

P88 therefore introduces the exact convex-hull lower bound

\[
\boxed{
L_{88}^{\mathrm{ch}}(B)
=
\operatorname{dist}_\infty\!\left(
\widehat P,
\operatorname{conv}\{F(v):v\in\operatorname{Vert}(B)\}
\right).
}
\]

Because the convex hull contains every P75 law generated inside $B$,

\[
L_{88}^{\mathrm{ch}}(B)
\le
\inf_{\theta\in B}\|\widehat P-F(\theta)\|_\infty.
\]

Moreover, $L_{88}^{\mathrm{ch}}$ is exactly the strongest lower bound obtainable from **all linear functionals of the full sixteen-cell observed law**, modulo probability-mass conservation.

To preserve every specialized earlier lower bound without making an unnecessary subsumption claim, define the published hierarchy value

\[
\boxed{
L_{88}(B)=\max\{L_{87}(B),L_{88}^{\mathrm{ch}}(B)\}.
}
\]

On the same exact rational witness box and empirical law used for P86 and P87,

\[
\boxed{
L_{87}(B)=\frac1{96}
<
L_{88}^{\mathrm{ch}}(B)=L_{88}(B)=\frac1{16}.
}
\]

Thus the new exact certificate is six times the P87 lower bound on the common witness.

P88 is a conditional model-separation theorem. It does not identify the P75 latent state with consciousness, prove that the convex hull equals the nonlinear P75 family, establish nonphysicality, or solve the physical-to-experiential bridge.

---

## 1. P75 full-law map

For

\[
\theta=(\pi,q_{1,-},q_{1,+},\ldots,q_{4,-},q_{4,+})\in[0,1]^9,
\]

and observed pattern

\[
x=(x_1,x_2,x_3,x_4)\in\{0,1\}^4,
\]

the declared P75 law is

\[
F_x(\theta)
=
(1-\pi)
\prod_{j=1}^4q_{j,-}^{x_j}(1-q_{j,-})^{1-x_j}
+
\pi
\prod_{j=1}^4q_{j,+}^{x_j}(1-q_{j,+})^{1-x_j}.
\]

Collecting all sixteen cells gives

\[
F(\theta)\in\Delta_{15}.
\]

Every coordinate of $F$ is multi-affine in the nine parameters.

---

## 2. Vector-valued multi-affine interpolation

Let

\[
B=\prod_{r=1}^9[\ell_r,u_r]
\]

be an axis-aligned parameter box. For a nondegenerate coordinate define

\[
t_r=\frac{\theta_r-\ell_r}{u_r-\ell_r}\in[0,1].
\]

For each box vertex indexed by $b\in\{0,1\}^9$, define the standard multilinear interpolation weight

\[
w_b(\theta)
=
\prod_{r=1}^9
 t_r^{b_r}(1-t_r)^{1-b_r},
\]

with degenerate coordinates omitted in the obvious way.

These weights satisfy

\[
w_b(\theta)\ge0,
\qquad
\sum_bw_b(\theta)=1.
\]

Because $F$ is vector-valued multi-affine,

\[
\boxed{
F(\theta)=\sum_bw_b(\theta)F(v_b).
}
\]

Therefore

\[
\boxed{
F(B)
\subseteq
C_B:=\operatorname{conv}\{F(v):v\in\operatorname{Vert}(B)\}.
}
\]

Since all vertex laws themselves belong to $F(B)$,

\[
\boxed{
\operatorname{conv}(F(B))=C_B.
}
\]

This is stronger than taking sixteen independent coordinatewise interval hulls: the same convex weights must be used across all cells simultaneously.

---

## 3. Convex-hull distance is a certified model-distance lower bound

Define

\[
\boxed{
L_{88}^{\mathrm{ch}}(B)
=
\inf_{Q\in C_B}\|\widehat P-Q\|_\infty.
}
\]

Because

\[
F(B)\subseteq C_B,
\]

minimizing over the larger convex set can only reduce distance:

\[
\boxed{
L_{88}^{\mathrm{ch}}(B)
\le
\inf_{\theta\in B}\|\widehat P-F(\theta)\|_\infty.
}
\]

Thus $L_{88}^{\mathrm{ch}}$ is a valid lower bound for branch-and-bound or any other certified model-set separation computation.

---

## 4. Finite exact primal LP

Let the distinct vertex laws be

\[
P^{(1)},\ldots,P^{(m)}.
\]

Every $Q\in C_B$ has representation

\[
Q=\sum_{k=1}^m\lambda_kP^{(k)},
\qquad
\lambda_k\ge0,
\qquad
\sum_k\lambda_k=1.
\]

Hence $L_{88}^{\mathrm{ch}}$ is the finite LP

\[
\begin{aligned}
\text{minimize }&t\\
\text{subject to }&
-t
\le
\widehat P(x)-\sum_k\lambda_kP^{(k)}(x)
\le t,
&&x\in\{0,1\}^4,\\
&\lambda_k\ge0,\\
&\sum_k\lambda_k=1.
\end{aligned}
\]

For rational box endpoints and rational empirical frequencies, every coefficient of this LP is rational.

P88's exact strict result does not depend on trusting a floating-point LP solver: the repository stores a rational feasible convex combination and a matching rational separating functional.

---

## 5. Complete full-law linear dual

Let

\[
g\in\mathbb R^{16}
\]

be arbitrary sixteen-cell coefficients and define

\[
Q_g(P)=\sum_xg_xP(x).
\]

For probability laws $P,Q$,

\[
\sum_x(P(x)-Q(x))=0.
\]

Therefore for any constant $a$,

\[
Q_g(P)-Q_g(Q)
=
\sum_x(g_x-a)(P(x)-Q(x)).
\]

Define the centered transfer norm

\[
\boxed{
D(g)=\min_{a\in\mathbb R}\sum_x|g_x-a|.
}
\]

Then

\[
\boxed{
|Q_g(P)-Q_g(Q)|
\le
D(g)\|P-Q\|_\infty.
}
\]

Adding a constant to every entry of $g$ changes neither the separation nor $D(g)$. Thus the effective coefficient space has dimension $16-1=15$, exactly matching the affine dimension of the full probability simplex.

Finite-dimensional LP duality yields

\[
\boxed{
L_{88}^{\mathrm{ch}}(B)
=
\sup_{D(g)\le1}
\left[
 g^\top\widehat P
 -
 \max_{v\in\operatorname{Vert}(B)}g^\top F(v)
\right].
}
\]

Because $-g$ is also allowed, this single oriented formula includes both sides of every support interval.

Therefore P88 closes the **entire linear full-law witness class** on a P75 box. Any future strengthening of the box lower bound must use nonlinear information, a smaller valid relaxation, or further subdivision of the parameter box rather than merely adding another linear event or coefficient pattern.

---

## 6. Exact certificate principle

A rational linear functional $g$ supplies a lower witness

\[
\ell
=
\frac{
\operatorname{dist}\left(
 g^\top\widehat P,
 [\min_vg^\top F(v),\max_vg^\top F(v)]
\right)
}{D(g)}.
\]

Every $Q\in C_B$ obeys the corresponding support inequality, so

\[
L_{88}^{\mathrm{ch}}(B)\ge\ell.
\]

A rational convex combination

\[
\bar P=\sum_k\lambda_kP^{(k)}\in C_B
\]

supplies the upper witness

\[
L_{88}^{\mathrm{ch}}(B)
\le
\|\widehat P-\bar P\|_\infty.
\]

If the two exact rational values match, then

\[
\boxed{
L_{88}^{\mathrm{ch}}(B)=\ell
=\|\widehat P-\bar P\|_\infty.
}
\]

This is an exact primal-dual-style certificate requiring only rational arithmetic to verify.

---

## 7. Full P88 hierarchy

The published P87 value recursively retains all earlier lower bounds. Although $L_{88}^{\mathrm{ch}}$ is the strongest full-law **linear support** certificate against the box model image, P88 does not need to assert that every specialized predecessor is analytically subsumed.

Define

\[
\boxed{
L_{88}(B)=\max\{L_{87}(B),L_{88}^{\mathrm{ch}}(B)\}.
}
\]

Then

\[
\boxed{L_{88}(B)\ge L_{87}(B)}
\]

pointwise by construction, while the new theorem remains precisely characterized.

---

## 8. Exact strict witness: a two-cell contrast

Use the same exact rational parameter box and empirical law as the P86-P87 strict witness.

The empirical sixteen-cell counts are

\[
(0,1,0,2,0,2,1,3,3,1,0,5,0,3,0,3),
\]

with total count $24$.

Use lexicographic binary outcome order and define

\[
\boxed{
g=\mathbf1_{1000}-\mathbf1_{1010}.}
\]

The empirical value is

\[
Q_g(\widehat P)
=
\widehat P(1000)-\widehat P(1010)
=
\frac3{24}-0
=
\boxed{\frac18}.
\]

On this P75 box the latent prevalence is fixed at $\pi=0$, so the observed law is the minus branch. Therefore

\[
\begin{aligned}
F_{1000}-F_{1010}
&=
q_{1,-}(1-q_{2,-})(1-q_{4,-})
\left[(1-q_{3,-})-q_{3,-}\right]\\
&=
q_{1,-}(1-q_{2,-})(1-q_{4,-})(1-2q_{3,-}).
\end{aligned}
\]

The strict witness box has

\[
q_{3,-}\in\left[\frac12,1\right],
\]

so

\[
F_{1000}-F_{1010}\le0
\]

throughout the box. The exact vertex interval is

\[
\boxed{
Q_g(F(B))\subseteq\left[-\frac9{16},0\right].
}
\]

Hence the exact support gap is

\[
\boxed{\Delta_g=\frac18}.
\]

The coefficient vector has one $+1$, one $-1$, and fourteen zeros. Its minimizing center is $a=0$, so

\[
\boxed{D(g)=2.}
\]

Thus

\[
\boxed{
L_{88}^{\mathrm{ch}}(B)
\ge
\frac{1/8}{2}
=
\frac1{16}.
}
\]

---

## 9. Exact convex-hull upper witness

The repository stores an exact convex combination of seven P75 box-vertex laws with weights

\[
\boxed{
\left(
\frac{10}{27},
\frac2{27},
\frac29,
\frac7{54},
\frac1{18},
\frac1{27},
\frac19
\right),
}
\]

which sum exactly to one.

The resulting convex-hull law is

\[
\bar P=
\left(
0,\frac5{48},0,\frac5{48},
0,\frac1{16},0,\frac1{16},
\frac1{16},\frac5{48},\frac1{16},\frac7{48},
\frac1{48},\frac1{16},\frac1{48},\frac3{16}
\right).
\]

Direct exact comparison with the empirical law gives

\[
\boxed{
\|\widehat P-\bar P\|_\infty=\frac1{16}.
}
\]

Therefore

\[
L_{88}^{\mathrm{ch}}(B)\le\frac1{16}.
\]

Combining Sections 8 and 9 gives the exact optimum

\[
\boxed{
L_{88}^{\mathrm{ch}}(B)=\frac1{16}.
}
\]

No numerical optimizer is needed to verify this equality.

---

## 10. Strict hierarchy on the common witness

The previously certified values are

\[
L_{85}(B)=0,
\qquad
L_{86}(B)=\frac1{192},
\qquad
L_{87}(B)=\frac1{96}.
\]

P88 gives

\[
L_{88}^{\mathrm{ch}}(B)=\frac1{16}.
\]

Hence

\[
\boxed{
0=L_{85}(B)
<\frac1{192}=L_{86}(B)
<\frac1{96}=L_{87}(B)
<\frac1{16}=L_{88}(B).
}
\]

The exact additive improvement over P87 is

\[
\boxed{
L_{88}-L_{87}
=
\frac1{16}-\frac1{96}
=
\frac5{96}.
}
\]

The multiplicative improvement is

\[
\boxed{
\frac{L_{88}}{L_{87}}=6.
}
\]

---

## 11. Proposition 88

For every empirical sixteen-cell law $\widehat P$ and rational axis-aligned P75 parameter box $B$:

1. the vector-valued P75 law map is multi-affine;
2. every P75 law generated inside $B$ is a convex combination of the parameter-box vertex laws;
3. the exact distance from $\widehat P$ to the convex hull of those vertex laws is a certified lower bound on distance to the nonlinear P75 model restricted to $B$;
4. that convex-hull distance is a finite rational LP;
5. it is also the optimum over all linear full-law separating functionals normalized by the centered transfer norm $D(g)$;
6. matching rational linear and convex-combination witnesses certify its value exactly;
7. the full hierarchy

\[
L_{88}(B)=\max\{L_{87}(B),L_{88}^{\mathrm{ch}}(B)\}
\]

is valid and pointwise dominates P87;
8. on the explicit common P86-P88 witness,

\[
\boxed{
L_{87}(B)=\frac1{96}
<
L_{88}^{\mathrm{ch}}(B)=L_{88}(B)=\frac1{16}.
}
\]

---

## 12. Why P88 is a conceptual closure

P83-P87 searched increasingly rich families of event and parity functionals. P88 no longer asks which event family or integer coefficient box to add next. It optimizes over the **entire 15-dimensional space of linear functionals of the observed four-bit law, modulo constants**.

Equivalently, it replaces separate scalar box constraints by one coupled convex-hull relaxation of the complete sixteen-cell law.

This gives a natural stopping point for the linear-witness branch. A genuinely stronger P89 direction should exploit information not captured by convexifying the box image, for example:

- nonlinear polynomial constraints among the sixteen cells;
- a tighter nonconvex relaxation of the P75 image;
- exact facets or semialgebraic constraints of the latent-class model;
- or a certified subdivision rule showing how the convex-hull gap contracts under box refinement.

---

## 13. Reproducibility record

Implementation:

`src/consciousness_bridge/full_law_convex_hull_certificate.py`

Regression tests:

`tests/test_full_law_convex_hull_certificate.py`

Equation provenance:

`docs/p88_equation_provenance.md`

Theorem figure:

`docs/figures/p88_exact_full_law_convex_hull_certificate.svg`

All strict-witness quantities are represented and checked with exact `fractions.Fraction` arithmetic.

---

## 14. Scientific interpretation boundary

P88 is a conditional theorem about separation from the declared P75 target-measurement family. Convexifying the P75 box image is a mathematical relaxation used to certify model distance; it is not an ontological statement.

P88 does not show that the P75 latent state is consciousness, that a failure of P75 implies consciousness is nonphysical, that the convex hull is the true physical model family, that all possible physical descriptions have been exhausted, or that the physical-to-experiential bridge has been solved.
