# Proposition 45: Shared-preparation graph allocation

## Status

**Proved convex resource-allocation theorem with an incidence-weighted KKT characterization.** P45 extends the P42-P44 finite-sample quantum regularity program from pair-specific sample planning to shared preparation-level sampling. A single preparation can participate in several candidate witness pairs, so one quantum or target sample stream can improve multiple edge certificates at once.

P45 is a design theorem. It assumes valid preparation-level uncertainty radii and a declared family of population regularity gaps. It does not establish quantum incompleteness, physical completeness, or consciousness.

---

## 1. From pairwise certificates to a graph

Let

\[
G=(V,E)
\]

be a finite undirected graph whose vertices are declared preparations and whose edges are candidate regularity witnesses.

For an edge

\[
e=\{i,j\}\in E,
\]

define the population quantum and target distances

\[
d_{Q,e}=D(\rho_i,\rho_j),
\qquad
 d_{Y,e}=\|P_i-P_j\|_{\mathrm{TV}},
\]

and let \(L_e\ge0\) be the declared Lipschitz constant for that candidate bridge test.

The population regularity gap is

\[
\boxed{
\Delta_e=d_{Y,e}-L_e d_{Q,e}.
}
\]

Only edges with

\[
\Delta_e>0
\]

can have positive population regularity margin under the declared model.

For each preparation \(i\in V\), let

\[
\varepsilon_i\ge0
\]

be a target-law total-variation uncertainty radius and let

\[
r_i\ge0
\]

be a quantum reconstruction trace-norm radius in the P42 sense.

---

## 2. P45A: nonuniform P42 edge budget

The P42 power theorem was written for equal per-preparation uncertainty radii. The same proof with preparation-specific radii gives the sharper edgewise inequality

\[
\boxed{
\widehat M_e
\ge
\Delta_e
-2(\varepsilon_i+\varepsilon_j)
-2L_e(r_i+r_j).
}
\]

To see this, target estimation contributes one radius for the empirical pairwise distance and the same preparation radii again in the lower confidence envelope. Therefore the total target loss is

\[
2(\varepsilon_i+\varepsilon_j).
\]

Likewise, quantum reconstruction contributes the preparation radii once when comparing the raw reconstructed pair to the population trace distance and once more in the certified quantum upper envelope. Therefore the total quantum loss is

\[
2L_e(r_i+r_j).
\]

When

\[
\varepsilon_i=\varepsilon_j=\varepsilon,
\qquad
r_i=r_j=r,
\]

this reduces exactly to the P42 bound

\[
\widehat M_e
\ge
\Delta_e-4\varepsilon-4L_e r.
\]

Hence the edgewise sufficient design constraint is

\[
\boxed{
2(\varepsilon_i+\varepsilon_j)
+2L_e(r_i+r_j)
<
\Delta_e.
}
\]

For optimization, it is convenient to work with the closed feasible set

\[
\boxed{
2(\varepsilon_i+\varepsilon_j)
+2L_e(r_i+r_j)
\le
\Delta_e.
}
\]

A strict empirical obstruction margin is then obtained by designing with any positive reserve or by verifying strict inequality after allocation.

---

## 3. Preparation-level sample models

Suppose the declared concentration method supplies radii of the form

\[
\boxed{
\varepsilon_i=\frac{a_{Y,i}}{\sqrt{n_{Y,i}}},
\qquad
r_i=\frac{a_{Q,i}}{\sqrt{n_{Q,i}}},
}
\]

where \(a_{Y,i}>0\) and \(a_{Q,i}>0\) collect the confidence level, alphabet size, tomography conditioning, and other fixed design constants for preparation \(i\).

Let \(c_{Y,i}>0\) and \(c_{Q,i}>0\) denote declared per-sample costs. Then

\[
n_{Y,i}=\frac{a_{Y,i}^2}{\varepsilon_i^2},
\qquad
n_{Q,i}=\frac{a_{Q,i}^2}{r_i^2}.
\]

Define

\[
w_{Y,i}=c_{Y,i}a_{Y,i}^2,
\qquad
w_{Q,i}=c_{Q,i}a_{Q,i}^2.
\]

The continuous weighted sampling cost becomes

\[
\boxed{
C(\varepsilon,r)
=
\sum_{i\in V}\frac{w_{Y,i}}{\varepsilon_i^2}
+
\sum_{i\in V}\frac{w_{Q,i}}{r_i^2}.
}
\]

This inverse-square form is the preparation-level analogue of the P43 cost geometry.

---

## 4. P45B: shared-preparation convex allocation problem

The P45 design problem is

\[
\boxed{
\begin{aligned}
\text{minimize}\quad
&C(\varepsilon,r)\\
\text{subject to}\quad
&2(\varepsilon_i+\varepsilon_j)
+2L_e(r_i+r_j)
\le\Delta_e,
\qquad e=\{i,j\}\in E,\\
&\varepsilon_i>0,
\qquad r_i>0.
\end{aligned}
}
\]

Every edge couples only its two endpoint preparations. Consequently, one reduction in \(\varepsilon_i\) or \(r_i\) can improve every candidate edge incident to vertex \(i\).

The objective is strictly convex on the positive orthant because each term \(w/u^2\) has second derivative

\[
\frac{6w}{u^4}>0.
\]

Every edge constraint is affine. Therefore the feasible set is convex.

If every optimized vertex is incident to at least one edge and the feasible set contains a positive point, the objective diverges as any radius approaches zero and also prevents a finite optimum from escaping toward arbitrarily large radii along constrained directions. Hence a minimizer exists. Strict convexity implies that the minimizer is unique.

### Proposition 45B

Under positive weights, positive edge gaps, graph coverage of all optimized vertices, and nonempty positive feasibility, the continuous P45 shared-preparation allocation problem has a unique global minimizer.

No combinatorial search over witness pairs is needed to establish uniqueness. The combinatorial structure enters through the graph incidence pattern in the constraints.

---

## 5. P45C: KKT incidence law

Associate a multiplier

\[
\lambda_e\ge0
\]

with every edge constraint. The Lagrangian is

\[
\mathcal L
=
\sum_i\frac{w_{Y,i}}{\varepsilon_i^2}
+
\sum_i\frac{w_{Q,i}}{r_i^2}
+
\sum_{e=\{i,j\}}
\lambda_e
\left[
2(\varepsilon_i+\varepsilon_j)
+2L_e(r_i+r_j)
-\Delta_e
\right].
\]

Differentiating with respect to \(\varepsilon_i\) gives

\[
-\frac{2w_{Y,i}}{\varepsilon_i^3}
+2\sum_{e\ni i}\lambda_e
=0.
\]

Thus

\[
\boxed{
\frac{w_{Y,i}}{\varepsilon_i^3}
=
\sum_{e\ni i}\lambda_e.
}
\]

Differentiating with respect to \(r_i\) gives

\[
-\frac{2w_{Q,i}}{r_i^3}
+2\sum_{e\ni i}\lambda_eL_e
=0,
\]

so

\[
\boxed{
\frac{w_{Q,i}}{r_i^3}
=
\sum_{e\ni i}\lambda_eL_e.
}
\]

Therefore any optimum satisfies the incidence-weighted cube-root relations

\[
\boxed{
\varepsilon_i
=
\left(
\frac{w_{Y,i}}
{\sum_{e\ni i}\lambda_e}
\right)^{1/3},
}
\]

and, whenever the quantum denominator is positive,

\[
\boxed{
r_i
=
\left(
\frac{w_{Q,i}}
{\sum_{e\ni i}\lambda_eL_e}
\right)^{1/3}.
}
\]

These equations are the graph generalization of the P43 cube-root allocation law. A preparation receives more precision when it is incident to strongly active edge constraints, especially edges with larger \(L_e\) on the quantum side.

The remaining KKT conditions are primal feasibility,

\[
2(\varepsilon_i+\varepsilon_j)
+2L_e(r_i+r_j)
\le\Delta_e,
\]

dual feasibility,

\[
\lambda_e\ge0,
\]

and complementary slackness,

\[
\boxed{
\lambda_e
\left[
\Delta_e
-2(\varepsilon_i+\varepsilon_j)
-2L_e(r_i+r_j)
\right]
=0.
}
\]

Because the optimization problem is convex and the objective is strictly convex, any feasible point and nonnegative multiplier family satisfying these conditions is the unique global optimum, under the usual constraint qualification supplied by a strictly feasible positive point.

---

## 6. Active edges and scientific meaning

An edge with

\[
\lambda_e>0
\]

is active at the optimum and exactly consumes its declared uncertainty budget:

\[
2(\varepsilon_i+\varepsilon_j)
+2L_e(r_i+r_j)
=
\Delta_e.
\]

An edge with positive slack can have

\[
\lambda_e=0.
\]

Thus the graph optimum automatically identifies which candidate witness constraints actually determine the required preparation-level precision.

This is a resource-allocation statement, not a scientific ranking of preparation pairs. A large multiplier means an edge is binding in the declared optimization problem. It does not mean that the corresponding preparation pair is more fundamental or more directly related to consciousness.

---

## 7. P45D: exact single-edge closed form

For one edge \(e=\{i,j\}\) with \(L_e>0\), write the four positive radius variables as

\[
u=(\varepsilon_i,\varepsilon_j,r_i,r_j)
\]

and coefficients

\[
a=(2,2,2L_e,2L_e).
\]

Let the corresponding positive cost weights be

\[
w=(w_{Y,i},w_{Y,j},w_{Q,i},w_{Q,j}).
\]

The problem becomes

\[
\min_{u_l>0}
\sum_{l=1}^4\frac{w_l}{u_l^2}
\quad\text{subject to}\quad
\sum_{l=1}^4a_lu_l\le\Delta_e.
\]

Define

\[
\boxed{
S_e
=
\sum_{l=1}^4a_l^{2/3}w_l^{1/3}.
}
\]

Strict convexity gives the unique solution

\[
\boxed{
u_l^*
=
\frac{\Delta_e}{S_e}
\left(
\frac{w_l}{a_l}
\right)^{1/3}.
}
\]

Substitution gives the exact minimum cost

\[
\boxed{
C_e^*
=
\frac{S_e^3}{\Delta_e^2}.
}
\]

This makes the connection to P43 explicit. P43 optimized a two-component uncertainty split. P45D resolves the four preparation-specific streams of a single edge and then P45C extends the same cube-root geometry to a full shared graph through incidence-weighted dual variables.

---

## 8. Integer sample counts

The optimization above is continuous in uncertainty radii. Once an optimal continuous radius \(\varepsilon_i^*\) or \(r_i^*\) is obtained, the corresponding nominal sample counts are

\[
 n_{Y,i}^*=\frac{a_{Y,i}^2}{(\varepsilon_i^*)^2},
\qquad
n_{Q,i}^*=\frac{a_{Q,i}^2}{(r_i^*)^2}.
\]

A conservative integer design uses

\[
\boxed{
N_{Y,i}=\left\lceil n_{Y,i}^*\right\rceil,
\qquad
N_{Q,i}=\left\lceil n_{Q,i}^*\right\rceil.
}
\]

Increasing a sample count can only decrease a radius of the form \(a/\sqrt n\), so ceiling each continuous count preserves every edge feasibility inequality.

The total rounding overhead is at most one extra target sample and one extra quantum sample per optimized preparation when unit sample costs are used. With nonunit per-sample costs, the overhead is bounded by the sum of the corresponding per-sample costs over the rounded streams.

---

## 9. Relation to P44 post-selection

P44 and P45 solve different problems.

P44 proves that after a finite candidate family is declared and simultaneous confidence is established, a witness can be selected from that family after observing the data without invalidating the family-level confidence guarantee.

P45 asks how to distribute samples before certification when different candidate edges share preparation-level data.

The logical combination is

\[
\boxed{
\text{P45 shared preparation allocation}
+
\text{valid simultaneous confidence}
+
\text{P44 post-selection}
\Longrightarrow
\text{resource-aware valid selected witness}.
}
\]

P45 does not replace P44's simultaneous confidence requirement. It only improves the design geometry by respecting shared data streams.

---

## 10. What P45 does not solve

P45 assumes the graph, population design gaps, Lipschitz constants, concentration constants, confidence allocation, and sample costs are declared before using the certification data.

If the graph itself, the edge gaps, the confidence weights, or the allocation policy are adapted using the same data later used for certification, additional time-uniform or post-selection control is required.

Likewise, P45 does not solve the discrete combinatorial problem in which one must choose only a subset of preparations or candidate edges under a hard budget. That is a separate experimental-design problem.

---

## 11. Scientific boundary

P45 can establish only that a declared family of quantum regularity tests admits a unique minimum-cost shared preparation-level design under the stated inverse-square uncertainty model and edge constraints.

A successful allocation or positive later witness does not establish that quantum mechanics is incomplete. It does not show that every physically richer descriptor fails. It does not establish that the declared system boundary is complete. It does not make Lipschitz regularity physically mandatory. It does not establish that the independently defined target is consciousness.

The theorem is about experimental resource allocation for an explicit model class.

---

## 12. Next theorem target

The natural next target is a discrete or adaptive graph-design theorem. Two important directions are:

1. **Budget-constrained edge discovery:** choose which preparations or candidate edges to measure when the total available sample budget cannot satisfy every edge.
2. **Anytime graph refinement:** allow samples to be added sequentially to selected preparations while preserving simultaneous family validity under data-dependent stopping and allocation.

The second direction would connect P24's anytime methodology with the quantum finite-sample program developed in P42-P45.

---

## 13. Reproducibility

Implementation:
[`shared_preparation_graph_allocation.py`](../src/consciousness_bridge/shared_preparation_graph_allocation.py)

Regression tests:
[`test_shared_preparation_graph_allocation.py`](../tests/test_shared_preparation_graph_allocation.py)
