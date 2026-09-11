# Proposition 78: Certified Continuous Model Separation for the P75 Four-View Latent Family

## Status

**Proved conditional computational theorem with an exact-rational branch-and-bound implementation.**

P78 addresses the computational gap left explicit by [P77](proposition_77_full_law_model_set_separation.md).

P77 proves that a finite-sample confidence region can reject a complete declared model family when the confidence region is disjoint from that family. It also makes a critical optimization distinction: a numerical candidate fit supplies an **upper bound** on distance to the model set, whereas rejection requires a mathematically sound **lower bound** or an equivalent proof of infeasibility.

P78 supplies such a lower-bounding route for the specific continuous four-view binary latent family introduced in [P75](proposition_75_target_model_adequacy_overidentification.md). The key structural fact is that every observed cell probability is multi-affine in the nine P75 parameters.

The central conclusion is:

\[
\boxed{
L_{\mathcal B}(\widehat P)
\le
 d_\infty(\widehat P,\mathcal M_{4,2})
\le
U_{\mathcal B}(\widehat P)
}
\]

for every finite axis-aligned partition \(\mathcal B\) of the P75 parameter cube, where the lower bound is obtained from exact boxwise cell enclosures and the upper bound is supplied by explicit admissible parameter vectors.

If the certified lower bound exceeds a valid upper bound on the P77 sampling radius, then P77 full-law rejection is computationally certified.

P78 does not identify the latent state with consciousness, does not validate the target-measurement model when rejection fails, and does not solve the physical-to-experiential bridge.

---

## 1. P75 model parameterization

Let

\[
\theta
=
(\pi,q_{1,-},q_{1,+},\ldots,q_{4,-},q_{4,+})
\in
\Theta:=[0,1]^9.
\]

Here \(\pi=P(S=+1)\) is the latent prevalence and

\[
q_{j,s}=P(X_j=1\mid S=s)
\]

is the binary response probability of view \(j\) under latent state \(s\in\{-1,+1\}\).

For an observed pattern

\[
x=(x_1,x_2,x_3,x_4)\in\{0,1\}^4,
\]

define

\[
F_x(\theta)
=
(1-\pi)
\prod_{j=1}^4
q_{j,-}^{x_j}(1-q_{j,-})^{1-x_j}
+
\pi
\prod_{j=1}^4
q_{j,+}^{x_j}(1-q_{j,+})^{1-x_j}.
\]

The full observed-law map is

\[
F:\Theta\to\Delta_{15},
\qquad
F(\theta)=\bigl(F_x(\theta)\bigr)_{x\in\{0,1\}^4},
\]

and the P75 model family is

\[
\mathcal M_{4,2}=F(\Theta).
\]

Because every parameter appears with degree at most one while the other coordinates are held fixed, every component \(F_x\) is **multi-affine** on \([0,1]^9\).

This is a structural property of the declared latent-class parameterization. It is not a consciousness assumption.

---

## 2. P78A: exact cell ranges on a parameter box

Let

\[
B=\prod_{r=1}^9[\ell_r,u_r]\subseteq\Theta
\]

be an axis-aligned parameter box.

For each observed cell \(x\), write

\[
F_x(\theta)=(1-\pi)A_x(\theta_-)+\pi B_x(\theta_+),
\]

where \(A_x\) and \(B_x\) are products of four factors, each factor lying in \([0,1]\) and depending on a separate channel parameter.

For a fixed pattern \(x\), every factor has an exact interval over \(B\). Because all factors are nonnegative and independent across coordinates, the exact extrema of each product are the products of the corresponding factor endpoints. The remaining dependence on \(\pi\) is affine, so its extrema occur at the two prevalence endpoints.

Therefore the exact coordinatewise range is

\[
\boxed{
I_x(B)
=
[m_x(B),M_x(B)]
=
\{F_x(\theta):\theta\in B\}_{\rm interval\ hull}.
}
\]

Equivalently, this follows from the standard multi-affine hyperrectangle property: a multi-affine function on a box is determined by repeated affine interpolation of its vertex values, so every scalar component reaches its minimum and maximum at box vertices.

P78 uses the product structure above to compute the same exact cell extrema without enumerating all \(2^9\) vertices.

---

## 3. P78B: a certified boxwise L-infinity lower bound

Let \(\widehat P\in\Delta_{15}\) be an empirical observed law.

For a scalar \(z\) and closed interval \([a,b]\), define

\[
\operatorname{dist}(z,[a,b])
=
\begin{cases}
a-z,&z<a,\\
0,&a\le z\le b,\\
z-b,&z>b.
\end{cases}
\]

Define the box lower bound

\[
\boxed{
L_\infty(B;\widehat P)
=
\max_x
\operatorname{dist}\bigl(\widehat P(x),I_x(B)\bigr).
}
\]

For every \(\theta\in B\),

\[
F_x(\theta)\in I_x(B)
\]

for every cell \(x\). Hence

\[
|\widehat P(x)-F_x(\theta)|
\ge
\operatorname{dist}\bigl(\widehat P(x),I_x(B)\bigr).
\]

Taking the maximum over cells gives

\[
\boxed{
\|\widehat P-F(\theta)\|_\infty
\ge
L_\infty(B;\widehat P)
\qquad\forall\theta\in B.
}
\]

Therefore

\[
\boxed{
L_\infty(B;\widehat P)
\le
\inf_{\theta\in B}
\|\widehat P-F(\theta)\|_\infty.
}
\]

This is a genuine lower bound. It is not a best-fit objective value and does not rely on a local optimizer reaching the global minimum.

---

## 4. P78C: a finite box cover gives a global lower bound

Let

\[
\mathcal B=\{B_1,\ldots,B_m\}
\]

be a finite partition of \(\Theta=[0,1]^9\).

Define

\[
\boxed{
L_{\mathcal B}(\widehat P)
=
\min_{B\in\mathcal B}
L_\infty(B;\widehat P).
}
\]

Since every admissible parameter vector belongs to one active box,

\[
\begin{aligned}
d_\infty(\widehat P,\mathcal M_{4,2})
&=
\inf_{\theta\in\Theta}
\|\widehat P-F(\theta)\|_\infty\\
&=
\min_{B\in\mathcal B}
\inf_{\theta\in B}
\|\widehat P-F(\theta)\|_\infty\\
&\ge
\min_{B\in\mathcal B}
L_\infty(B;\widehat P).
\end{aligned}
\]

Thus

\[
\boxed{
L_{\mathcal B}(\widehat P)
\le
d_\infty(\widehat P,\mathcal M_{4,2}).
}
\]

Any explicit parameter vector \(\theta_c\in\Theta\) simultaneously gives

\[
\boxed{
d_\infty(\widehat P,\mathcal M_{4,2})
\le
U(\theta_c)
:=
\|\widehat P-F(\theta_c)\|_\infty.}
\]

This gives the certified bracket

\[
\boxed{
L_{\mathcal B}
\le
d_\infty
\le U.
}
\]

The direction of these inequalities is the central P78 safeguard. A candidate model gives the **upper** side of the bracket. Only the box cover gives the required **lower** side.

---

## 5. P78D: quantitative mesh-gap bound

P78 also gives an explicit reason the box lower bound converges under refinement.

For each cell map \(F_x\), every first partial derivative satisfies

\[
\left|\frac{\partial F_x}{\partial\theta_r}\right|\le1
\]

throughout \([0,1]^9\). For the prevalence coordinate this follows from

\[
\frac{\partial F_x}{\partial\pi}=B_x-A_x
\]

with \(A_x,B_x\in[0,1]\). For each channel coordinate, the derivative is a prevalence weight times a product of three factors in \([0,1]\), up to sign.

Hence

\[
\boxed{
|F_x(\theta)-F_x(\theta')|
\le
\|\theta-\theta'\|_1.
}
\]

For a box \(B\), define its summed side width

\[
w(B)=\sum_{r=1}^9(u_r-\ell_r).
\]

Then every exact cell interval satisfies

\[
M_x(B)-m_x(B)\le w(B).
\]

Let \(c_B\) be any point in \(B\), such as its center. Since \(F_x(c_B)\in I_x(B)\),

\[
|\widehat P(x)-F_x(c_B)|
\le
\operatorname{dist}(\widehat P(x),I_x(B))
+
\bigl(M_x(B)-m_x(B)\bigr).
\]

Therefore

\[
\boxed{
\|\widehat P-F(c_B)\|_\infty
\le
L_\infty(B;\widehat P)+w(B).
}
\]

If

\[
\eta(\mathcal B)=\max_{B\in\mathcal B}w(B),
\]

then choosing a box attaining \(L_{\mathcal B}\) gives

\[
\boxed{
0
\le
d_\infty(\widehat P,\mathcal M_{4,2})
-L_{\mathcal B}(\widehat P)
\le
\eta(\mathcal B).
}
\]

Thus any sequence of partitions with

\[
\eta(\mathcal B_r)\to0
\]

forces

\[
L_{\mathcal B_r}(\widehat P)
\to
d_\infty(\widehat P,\mathcal M_{4,2}).
\]

This is a deterministic global-optimization statement. It is separate from the statistical coverage statement in P77.

---

## 6. P78E: exact-rational branch-and-bound implementation

The implementation

[`certified_continuous_model_separation.py`](../src/consciousness_bridge/certified_continuous_model_separation.py)

uses the following protocol:

1. represent a sixteen-cell empirical law exactly as integer counts divided by their total;
2. begin with the complete parameter cube \([0,1]^9\);
3. compute exact rational cell intervals for each active box;
4. compute the exact boxwise lower bound \(L_\infty(B;\widehat P)\);
5. evaluate the exact rational model law at each box center to maintain a valid upper bound;
6. split an active box with the smallest current lower bound along its widest coordinate;
7. preserve all active boxes as a partition of the complete parameter cube;
8. report the global lower and upper bracket at every finite iteration.

All empirical probabilities and dyadic parameter points are represented with Python `Fraction` arithmetic. Therefore the optimization lower bound is not inferred from ordinary floating-point local optimization.

The implementation does **not** claim that the branch-and-bound search is dimension-free or computationally cheap. Nine dimensions can still require many boxes before the lower bound becomes sharp.

---

## 7. P78F: direct P77 rejection interface

Suppose P78 returns

\[
L_{\mathcal B}
\le
d_\infty(\widehat P,\mathcal M_{4,2}).
\]

Suppose separately that

\[
\overline\varepsilon
\ge
\varepsilon_{n,16}(\alpha)
\]

is a mathematically valid upper bound on the P77 simultaneous sampling radius.

Then

\[
\boxed{
L_{\mathcal B}>\overline\varepsilon
\quad\Longrightarrow\quad
 d_\infty(\widehat P,\mathcal M_{4,2})
>
\varepsilon_{n,16}(\alpha),
}
\]

which triggers the P77 full-law rejection theorem.

The implementation deliberately accepts a **certified sampling-radius upper bound** as a separate input. Converting an ordinary floating approximation of the Hoeffding radius into a rational number does not make that approximation mathematically certified.

This separation of responsibilities is intentional:

- P77 supplies the finite-sample statistical theorem;
- P78 supplies a certified continuous-model optimization lower bound;
- a rigorous rejection claim requires both sides of the comparison to be valid in the required direction.

---

## 8. Why naive convexification does not solve the full problem

For any linear functional \(a\cdot F(\theta)\), multi-affinity implies that its extrema over the full parameter cube occur at parameter vertices. However, the full cube contains degenerate channel parameters. Those vertices include deterministic point-mass observed laws, and their convex hull is the entire sixteen-cell simplex.

Therefore a naive convex-hull relaxation over the complete P75 parameter cube cannot separate an arbitrary observed probability law from the model: the convex relaxation is too large.

This is why P78 keeps the nonconvex box structure and refines it locally instead of replacing the complete model image by one global convex hull.

This observation also clarifies where independent parameter restrictions could help. If a protocol supplies externally justified nondegeneracy or calibration bounds that shrink the admissible parameter region, tighter convex or interval relaxations may become useful. Such restrictions must not be introduced from the same data merely to force rejection.

---

## 9. Relation to standard global optimization

P78 is not a claim that multi-affine branch-and-bound is new.

Standard global-optimization literature already provides complete branch-and-bound and interval methods for continuous nonconvex problems. Likewise, the P75 distance problem can be written as a compact polynomial optimization problem by introducing an epigraph variable \(t\):

\[
\begin{aligned}
\min_{\theta,t}\quad & t\\
\text{subject to}\quad
&-t\le \widehat P(x)-F_x(\theta)\le t,
\qquad x\in\{0,1\}^4,\\
&0\le\theta_r\le1.
\end{aligned}
\]

This is a polynomial optimization problem on a compact semialgebraic set. Standard moment and sum-of-squares hierarchies provide convergent global lower-bounding frameworks for such problems under their usual assumptions.

P78's repository-specific contribution is narrower:

- identify the exact multi-affine structure of the P75 model map;
- derive a dependency-light exact-rational box lower bound specialized to that map;
- prove a direct global bracket and mesh-gap bound;
- connect that certified lower bound to the strict P77 rejection gate without reversing the optimizer-bound direction.

---

## 10. Synthetic parity stress test

As a controlled non-model-shaped example, consider the empirical law that places equal mass on the eight even-parity patterns in \(\{0,1\}^4\) and zero mass on the eight odd-parity patterns.

This example is **synthetic**. It is not an experiential target and is not evidence about consciousness.

The exact-rational implementation can refine the complete nine-dimensional parameter cube until it obtains a positive global lower bound on the L-infinity distance to the P75 model family. The test suite uses this example to verify that the lower bound can become strictly positive while remaining below an explicit admissible upper bound.

The purpose of the example is computational: it verifies lower-bound direction, global coverage of the parameter cube, monotonic refinement behavior, and the P77 interface.

---

## 11. Scientific boundaries

P78 establishes a computational certification theorem under the declared P75 statistical model family. It does **not** establish that:

- the P75 latent variable is consciousness;
- four binary reports are a complete measurement theory of experience;
- conditional independence is empirically true;
- a failure to reject validates the P75 model;
- the current branch-and-bound procedure is computationally optimal;
- a local optimizer value is a certified lower bound;
- a floating approximation to the P77 sampling radius is automatically rigorous;
- consciousness is reducible to current physics;
- consciousness is irreducible to physics;
- the physical-to-experiential bridge has been solved.

The physical-to-experiential bridge remains open.

---

## 12. References and provenance context

The multi-affine hyperrectangle property used by P78 is standard. See, for example:

- C. Belta, L. C. G. J. M. Habets, and V. Kumar, "Control of multi-affine systems on rectangles with applications to hybrid biomolecular networks," *Proceedings of the 41st IEEE Conference on Decision and Control*, 2002, DOI: 10.1109/CDC.2002.1184551.

For complete continuous global search and interval branch-and-bound context:

- A. Neumaier, "Complete Search in Continuous Global Optimization and Constraint Satisfaction," *Acta Numerica*, 2004.

For compact polynomial global optimization through moment and semidefinite relaxations:

- J. B. Lasserre, "Global Optimization with Polynomials and the Problem of Moments," *SIAM Journal on Optimization* 11(3), 796-817, 2001, DOI: 10.1137/S1052623400366802.

For broader finite latent-structure and Bernoulli-product-mixture identifiability context:

- E. S. Allman, C. Matias, and J. A. Rhodes, "Identifiability of parameters in latent structure models with many observed variables," *The Annals of Statistics* 37(6A), 3099-3132, 2009, DOI: 10.1214/09-AOS689.

Equation-level classification is recorded in [the P78 equation and provenance record](p78_equation_provenance.md).
