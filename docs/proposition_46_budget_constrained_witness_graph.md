# Proposition 46: Budget-constrained witness-graph selection

## Status

**Proved combinatorial design theorem with a complexity result and certified upper bound.** P46 extends P45 from continuous shared-preparation precision allocation to the discrete question that arises when the available budget is too small to measure every preparation.

P46 asks which preparations should be included before data collection so that the total declared value of fully measurable candidate witness pairs is maximized.

This is an experimental-design theorem. It does not establish quantum incompleteness, physical completeness, or consciousness.

---

## 1. Setup

Let

\[
G=(V,E)
\]

be a finite undirected graph. Vertices are declared preparations and edges are candidate regularity-witness pairs.

Each preparation \(i\in V\) has positive measurement cost

\[
c_i>0,
\]

and each edge \(e\in E\) has nonnegative design value

\[
w_e\ge0.
\]

The value \(w_e\) can encode a declared scientific priority, anticipated P42 regularity gap, expected information gain, or another predeclared design score. P46 does not prescribe which interpretation is scientifically appropriate.

For a selected preparation set \(S\subseteq V\), an edge is available only when both endpoints are measured. Define

\[
\boxed{
F(S)=\sum_{\{i,j\}\in E}w_{ij}\mathbf 1\{i,j\in S\}.
}
\]

Given total budget \(B\ge0\), the discrete P46 design problem is

\[
\boxed{
\max_{S\subseteq V}
F(S)
\quad\text{subject to}\quad
\sum_{i\in S}c_i\le B.
}
\]

This objective is the total value of the witness subgraph induced by the measured preparations.

---

## 2. P46A: monotonicity and supermodularity

Because all edge weights are nonnegative,

\[
S\subseteq T
\Longrightarrow
F(S)\le F(T).
\]

Thus \(F\) is monotone.

For one vertex \(v\notin T\), the marginal value of adding \(v\) to \(S\) is

\[
F(S\cup\{v\})-F(S)
=
\sum_{u\in S:\{u,v\}\in E}w_{uv}.
\]

If \(S\subseteq T\), then

\[
\sum_{u\in S:\{u,v\}\in E}w_{uv}
\le
\sum_{u\in T:\{u,v\}\in E}w_{uv}.
\]

Therefore

\[
\boxed{
F(S\cup\{v\})-F(S)
\le
F(T\cup\{v\})-F(T).
}
\]

Hence \(F\) is supermodular.

### Interpretation

Preparation complementarity is mathematically explicit. A vertex can become more valuable after neighboring preparations are already selected because more witness edges become complete.

This also explains why the usual greedy guarantees for monotone submodular maximum coverage do not transfer to P46 without additional assumptions.

---

## 3. P46B: computational hardness

Consider the decision version:

> Is there a set \(S\subseteq V\) with total cost at most \(B\) and \(F(S)\ge W\)?

This problem is in NP because a proposed set \(S\) can be checked in polynomial time.

To prove NP-hardness, reduce from CLIQUE. Let \(H=(V_H,E_H)\) and integer \(k\) be an instance of CLIQUE. Construct a P46 instance with

\[
V=V_H,
\qquad
E=E_H,
\]

unit vertex costs

\[
c_i=1,
\]

unit edge weights

\[
w_e=1,
\]

budget

\[
B=k,
\]

and target value

\[
W=\binom{k}{2}.
\]

If \(H\) contains a \(k\)-clique, selecting its vertices gives cost \(k\) and exactly \(\binom{k}{2}\) induced edges.

Conversely, any feasible set has \(|S|\le k\), so

\[
F(S)\le\binom{|S|}{2}\le\binom{k}{2}.
\]

Achieving

\[
F(S)\ge\binom{k}{2}
\]

therefore forces \(|S|=k\) and every possible pair in \(S\) to be an edge. Thus \(S\) is a \(k\)-clique.

Hence the decision problem is NP-complete, and the optimization problem is NP-hard.

\[
\boxed{
\text{P46 budgeted witness selection is NP-hard even with unit costs and unit edge weights.}
}
\]

This justifies separating P45's convex continuous allocation from P46's discrete graph-selection layer.

---

## 4. P46C: weighted-degree upper bound

Define each vertex's full weighted degree

\[
\boxed{
d_i=\sum_{j:\{i,j\}\in E}w_{ij}.}
\]

For any selected set \(S\), each induced edge contributes its weight twice to the sum of selected internal degrees. Because the full degree can only be larger than the internal degree,

\[
2F(S)
\le
\sum_{i\in S}d_i.
\]

Therefore

\[
\boxed{
F(S)
\le
\frac12\sum_{i\in S}d_i.
}
\]

The right side is a linear 0-1 knapsack objective under the same vertex budget. Let

\[
K^*(B)
=
\max_{S:\sum_{i\in S}c_i\le B}
\sum_{i\in S}d_i.
\]

Then the optimal P46 value \(F^*(B)\) satisfies

\[
\boxed{
F^*(B)\le\frac12K^*(B).
}
\]

Now relax the linear knapsack to fractions \(x_i\in[0,1]\):

\[
K_{\rm frac}(B)
=
\max
\left\{
\sum_i d_i x_i:
\sum_i c_i x_i\le B,
0\le x_i\le1
\right\}.
\]

This fractional relaxation is solved by sorting vertices by

\[
\frac{d_i}{c_i}.
\]

Since

\[
K^*(B)\le K_{\rm frac}(B),
\]

we obtain the directly computable bound

\[
\boxed{
F^*(B)
\le
U_{\rm deg}(B)
:=
\min\left\{
\sum_{e\in E}w_e,
\frac12K_{\rm frac}(B)
\right\}.
}
\]

The total-edge-value cap prevents the degree relaxation from exceeding the value of measuring the full graph.

---

## 5. P46D: a posteriori optimality certificate

Suppose any algorithm returns a feasible selection \(S\). Define

\[
L(S)=F(S)
\]

and use the P46C bound \(U_{\rm deg}(B)\).

Then

\[
\boxed{
L(S)\le F^*(B)\le U_{\rm deg}(B).
}
\]

Hence

\[
\boxed{
0\le F^*(B)-F(S)
\le
U_{\rm deg}(B)-F(S).
}
\]

The quantity

\[
\boxed{
G_{\rm cert}(S)
=U_{\rm deg}(B)-F(S)
}
\]

is a valid upper bound on the unknown optimality gap.

If

\[
G_{\rm cert}(S)=0,
\]

then the selected design is globally optimal even if it was obtained by a heuristic method.

This certificate is inexpensive and remains useful when exact combinatorial optimization is not practical.

---

## 6. P46E: exact small-instance solution

For sufficiently small \(|V|\), exact optimization can enumerate all subsets:

\[
\mathcal S_B
=
\left\{
S\subseteq V:
\sum_{i\in S}c_i\le B
\right\}.
\]

Then

\[
\boxed{
F^*(B)=\max_{S\in\mathcal S_B}F(S).
}
\]

The repository implementation deliberately limits exact enumeration because P46B shows that exponential worst-case scaling is not an implementation accident but a property of the general problem.

For an exact solution \(S^*\), the degree-relaxation interval

\[
\boxed{
F(S^*)\le F^*(B)\le U_{\rm deg}(B)
}
\]

still provides a cross-check. The exact solver itself establishes

\[
F(S^*)=F^*(B).
\]

---

## 7. Relation to P45

P45 assumes a declared witness graph and allocates continuous preparation-level precision across all its vertices.

P46 handles the preceding discrete bottleneck:

\[
\boxed{
\text{hard total budget}
\longrightarrow
\text{P46 preparation subset}
\longrightarrow
\text{induced witness graph}
\longrightarrow
\text{P45 precision allocation}.
}
\]

After the selected preparation set is fixed independently of certification data, P45 can optimize quantum and target precision across that induced graph.

If P46 selection itself uses the same stochastic observations later used for certification, an additional post-selection or anytime-valid theorem is required. P44 cannot be invoked automatically unless its simultaneous-family premises cover the adaptive selection rule actually used.

---

## 8. Design values and scientific discipline

P46 is agnostic about the edge value \(w_e\). Possible predeclared choices include:

- anticipated population regularity gap,
- expected reduction in uncertainty,
- scientific priority weight,
- robustness reserve,
- or a composite design score fixed before certification data are examined.

The theorem does not prove that any one score is scientifically correct.

In particular, assigning an edge a large weight does not mean that the pair is more conscious, more fundamental, or more likely to reveal new physics. It means only that the declared design objective values that edge more highly.

---

## 9. Scientific boundary

P46 establishes a discrete optimization structure for selecting preparations under a hard budget. It proves monotonicity, supermodularity, NP-hardness, a computable weighted-degree upper bound, and a certified optimality-gap bound.

It does not establish that any selected witness is physically real. It does not establish that the declared quantum descriptor is complete. It does not establish that quantum mechanics is incomplete. It does not establish that the target is consciousness.

The result remains entirely conditional on the graph, costs, edge values, system boundary, statistical model, and bridge class declared by the experimenter.

---

## 10. Next theorem target

P46 exposes the next natural difficulty: adaptive sequential allocation.

A practical experiment will not always choose the full preparation subset once and then stop. It may collect initial data, identify promising witness edges, add samples to shared vertices, eliminate weak candidates, and stop when one family-level certificate is decisive.

The next theorem should therefore combine:

\[
\boxed{
\text{P24 anytime validity}
+
\text{P44 post-selection}
+
\text{P45 shared allocation}
+
\text{P46 discrete graph selection}
}
\]

into a sequential graph-refinement procedure with a valid stopping rule.

---

## 11. Reproducibility

Implementation:
[`budget_constrained_witness_graph.py`](../src/consciousness_bridge/budget_constrained_witness_graph.py)

Regression tests:
[`test_budget_constrained_witness_graph.py`](../tests/test_budget_constrained_witness_graph.py)
