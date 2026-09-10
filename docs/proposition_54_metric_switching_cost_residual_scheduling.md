# Proposition 54: Metric switching-cost residual scheduling

## Status

**Proved deterministic scheduling theorem.** This result extends the residual-demand layer of P53 by adding a declared preparation-switching metric. It concerns deterministic experimental execution cost after residual sample demands have been specified. It does not establish statistical minimaxity of the P48 thresholds and does not make an ontological claim about consciousness or quantum mechanics.

---

## 1. Problem

P53 reduces the remaining complete-family certification task at a sequential state to nonnegative integer preparation demands

\[
r_i\in\mathbb Z_{\ge 0}.
\]

If every sample selection had identical execution cost and changing preparation were free, the unit-capacity residual acquisition burden would simply be

\[
R=\sum_i r_i.
\]

Real experiments may also pay a setup or transition cost when moving from one preparation to another. P54 asks whether repeated alternation between preparations can ever be necessary when those switching costs form a metric.

Let

\[
V_+=\{i:r_i>0\}
\]

be the positive-demand preparations. Let \(s\) denote an optional current setup state. Let

\[
c(u,v)\ge 0
\]

be a switching cost on the declared preparation/setup points satisfying

\[
c(u,u)=0,\qquad c(u,v)=c(v,u),\qquad
c(u,w)\le c(u,v)+c(v,w).
\]

Thus \(c\) is a finite metric on the relevant point set.

For a feasible expanded sample schedule

\[
\sigma=(\sigma_1,\ldots,\sigma_R),
\]

containing preparation \(i\) exactly \(r_i\) times, define switching cost

\[
C_{\rm sw}(\sigma)
=
\mathbf 1_{s\text{ declared}}c(s,\sigma_1)
+
\sum_{t=1}^{R-1}c(\sigma_t,\sigma_{t+1}).
\]

If each acquired sample has deterministic cost \(a>0\), then

\[
C_{\rm total}(\sigma)=aR+C_{\rm sw}(\sigma).
\]

The acquisition term \(aR\) is fixed across all feasible schedules. Only switching cost remains to optimize.

---

## 2. Proposition 54A: metric batching theorem

For any feasible expanded schedule \(\sigma\), let

\[
\pi(\sigma)=(v_1,\ldots,v_m)
\]

be the positive-demand preparations in order of first appearance, with every preparation retained exactly once.

Construct the block schedule

\[
\bar\sigma
=
(v_1^{\times r_{v_1}},v_2^{\times r_{v_2}},\ldots,v_m^{\times r_{v_m}}).
\]

Then

\[
\boxed{
C_{\rm sw}(\bar\sigma)
\le
C_{\rm sw}(\sigma).
}
\]

Therefore there always exists an optimal residual schedule in which every positive-demand preparation appears in exactly one contiguous block.

### Proof

Delete from the route \(\sigma\) every occurrence of a preparation after its first appearance. Each deletion replaces a route segment

\[
u\to x_1\to\cdots\to x_k\to v
\]

by the shortcut \(u\to v\). Repeated application of the triangle inequality gives

\[
c(u,v)
\le
c(u,x_1)+\cdots+c(x_k,v).
\]

Hence deleting repeated visits cannot increase route length. The retained route is exactly the first-visit order \(\pi(\sigma)\). Expanding each retained preparation into \(r_i\) consecutive copies adds only zero-cost self transitions because \(c(i,i)=0\). The acquisition count remains exactly \(R\), so total deterministic cost also cannot increase. \(\square\)

---

## 3. Proposition 54B: exact reduction to a shortest Hamiltonian path

Because an optimum may be restricted to one block per preparation, the residual scheduling problem separates exactly into acquisition and routing:

\[
\boxed{
C_{\rm total}^*
=
a\sum_{i\in V_+}r_i
+
L^*(V_+;s),
}
\]

where

\[
L^*(V_+;s)
=
\min_{(v_1,\ldots,v_m)\in\operatorname{Perm}(V_+)}
\left[
\mathbf 1_{s\text{ declared}}c(s,v_1)
+
\sum_{k=1}^{m-1}c(v_k,v_{k+1})
\right].
\]

Thus the only combinatorial part of the exact deterministic residual schedule is a **shortest Hamiltonian path** through the positive-demand preparations, optionally rooted at the current setup state, with no return-to-start requirement.

### Proof

Proposition 54A shows that every feasible schedule is weakly dominated by a block schedule. Every block schedule is uniquely characterized, up to the fixed within-block multiplicities, by a permutation of \(V_+\). Its acquisition cost is the fixed quantity \(a\sum_i r_i\), and its switching cost is exactly the path length displayed above. Minimizing over all feasible schedules is therefore equivalent to minimizing over permutations of \(V_+\). \(\square\)

---

## 4. Proposition 54C: exact finite-instance dynamic program

For \(m=|V_+|\), define

\[
D(S,j)
\]

as the minimum switching cost of a path that starts from \(s\) when declared, visits exactly the subset \(S\subseteq V_+\), and ends at \(j\in S\).

The boundary condition is

\[
D(\{j\},j)=
\begin{cases}
c(s,j),& s\text{ declared},\\
0,& s\text{ absent},
\end{cases}
\]

and the Held-Karp recurrence is

\[
\boxed{
D(S,j)
=
\min_{k\in S\setminus\{j\}}
\left[D(S\setminus\{j\},k)+c(k,j)\right].
}
\]

Therefore

\[
\boxed{
L^*(V_+;s)=\min_{j\in V_+}D(V_+,j).
}
\]

This yields an exact algorithm with the standard subset dynamic-programming complexity

\[
O(m^2 2^m)
\]

time and

\[
O(m2^m)
\]

state storage, suitable for exact small-instance audits.

---

## 5. Relation to P52-P53

P52 proves that without transition overhead the deterministic capacity-constrained service problem is governed only by aggregate preparation demand. P53 makes that burden sequential through residual demands after additional samples and valid safe pruning. P54 adds a qualitatively different resource: **configuration movement between preparations**.

The resulting chain is

\[
\boxed{
\text{P48 local thresholds}
\to
\text{P52 static demand allocation}
\to
\text{P53 residual reoptimization}
\to
\text{P54 metric switching-cost routing}.
}
\]

An important consequence is that the **magnitudes** \(r_i\) determine acquisition cost, while the **support geometry** \(V_+\) and metric \(c\) determine switching cost. Safe pruning can therefore save experimental time in two distinct ways: by reducing residual sample demand and by deleting preparation visits from the routing problem.

---

## 6. Why the metric assumption matters

The batching theorem uses the triangle inequality. Without it, a detour through a previously visited preparation could be cheaper than the direct transition between two preparations. In that nonmetric regime, deleting repeated visits need not preserve or reduce switching cost, and the Hamiltonian-path reduction is not justified.

P54 therefore does not claim that batching is universally optimal for arbitrary setup-cost matrices. The theorem applies only when the declared switching costs satisfy the metric assumptions above.

---

## 7. Implementation and reproducibility

The executable implementation is

[`src/consciousness_bridge/metric_switching_residual_schedule.py`](../src/consciousness_bridge/metric_switching_residual_schedule.py).

It provides:

- complete finite-metric validation;
- arbitrary expanded-route switching-cost evaluation;
- first-visit batching certificates;
- exact block-schedule expansion;
- an exact Held-Karp solver for the minimum switching path.

Regression tests are in

[`tests/test_metric_switching_residual_schedule.py`](../tests/test_metric_switching_residual_schedule.py).

The theorem visual is

[`docs/figures/p54_metric_switching_cost_residual_scheduling.svg`](figures/p54_metric_switching_cost_residual_scheduling.svg).

---

## 8. Scientific boundary

P54 is a deterministic experimental scheduling result conditional on a declared residual-demand vector and switching metric. It does not prove that P48 local thresholds are information-theoretically minimal. It does not validate a pruning decision; that validity comes from the preceding sequential certification framework. It does not identify any scheduling quantity, graph, metric, or optimization objective with consciousness, and it makes no claim that quantum mechanics is incomplete.
