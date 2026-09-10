# Proposition 61: exact integer transition-calibration allocation by diminishing marginal gain

## Status

**Proved exact discrete resource-allocation theorem.** P60 gives a constructive whole-measurement allocation with a certified overhead relative to the P59 continuous optimum. P61 closes that gap for the declared separable calibration surrogate by solving the integer problem exactly.

The exact rule is simple: give every calibrated transition one initial measurement, then repeatedly assign the next available measurement to the transition whose current additional measurement produces the largest decrease in the uncertainty objective.

Because each transition exhibits strictly diminishing marginal gain, this greedy rule is globally optimal.

P61 is a resource-allocation theorem. It does not validate the underlying physical transition model, choose the scientific sensitivity weights, solve the full robust-routing design problem, or make any claim about consciousness or quantum incompleteness.

---

## 1. Integer calibration problem

For every calibrated transition edge \(e\), define the positive effective coefficient

\[
\boxed{b_e=w_ea_e>0.}
\]

Here \(a_e\) is the inverse-square-root uncertainty coefficient from P58-P59 and \(w_e\) is the declared sensitivity weight used by the P59 surrogate.

For integer calibration count

\[
k_e\in\{1,2,3,\ldots\},
\]

define

\[
\boxed{
U(k)=\sum_{e\in E}\frac{b_e}{\sqrt{k_e}}.
}
\]

Let

\[
m=|E|
\]

and let the hard total integer budget satisfy

\[
\boxed{B\ge m.}
\]

The exact discrete design problem is

\[
\boxed{
\min_{k_e\in\mathbb N,\ k_e\ge1}
\sum_e\frac{b_e}{\sqrt{k_e}}
\quad\text{subject to}\quad
\sum_e k_e\le B.
}
\]

Since every summand strictly decreases with \(k_e\), every optimum uses the full available budget:

\[
\boxed{
\sum_e k_e=B.
}
\]

---

## 2. Marginal benefit of one additional measurement

If edge \(e\) currently has \(k\ge1\) measurements, one additional calibration measurement changes its contribution from

\[
\frac{b_e}{\sqrt{k}}
\]

to

\[
\frac{b_e}{\sqrt{k+1}}.
\]

The corresponding reduction in uncertainty is

\[
\boxed{
\Delta_e(k)
=
b_e\left(
\frac1{\sqrt{k}}
-
\frac1{\sqrt{k+1}}
\right).
}
\]

This is the value of assigning the next measurement to edge \(e\).

---

## 3. Proposition 61A: strict diminishing marginal gain

For fixed \(b_e>0\),

\[
\boxed{
\Delta_e(k+1)<\Delta_e(k)
\qquad\forall k\ge1.
}
\]

### Proof

Consider

\[
f(x)=x^{-1/2},
\qquad x>0.
\]

Its derivative is

\[
f'(x)=-\frac{1}{2x^{3/2}},
\]

and

\[
f''(x)=\frac{3}{4x^{5/2}}>0.
\]

Thus \(f\) is strictly convex and decreasing.

For a convex function, consecutive forward differences

\[
f(k+1)-f(k)
\]

increase with \(k\). Since these differences are negative, their magnitudes decrease. Therefore

\[
f(k)-f(k+1)
>
f(k+1)-f(k+2).
\]

Multiplying by \(b_e>0\) gives

\[
\Delta_e(k)>\Delta_e(k+1).
\]

\(\square\)

---

## 4. Prefix representation of every integer allocation

Begin from the mandatory baseline allocation

\[
k_e=1
\qquad\forall e,
\]

which consumes \(m\) measurements.

Let

\[
R=B-m
\]

be the number of additional measurements available.

For edge \(e\), define its infinite decreasing marginal-gain sequence

\[
\boxed{
\Delta_e(1),\Delta_e(2),\Delta_e(3),\ldots
}
\]

If the final count is

\[
k_e=1+r_e,
\]

then exactly the first \(r_e\) gains from edge \(e\)'s sequence have been collected.

Therefore every feasible allocation corresponds to choosing a **prefix** from each edge's decreasing gain sequence, with total prefix length

\[
\sum_e r_e=R.
\]

The total uncertainty satisfies the telescoping identity

\[
\frac{b_e}{\sqrt{1+r_e}}
=
b_e-
\sum_{j=1}^{r_e}\Delta_e(j).
\]

Hence

\[
\boxed{
U(k)
=
\sum_e b_e
-
\sum_e\sum_{j=1}^{r_e}\Delta_e(j).
}
\]

Minimizing uncertainty is therefore equivalent to maximizing the total selected marginal gain subject to the prefix constraints.

---

## 5. P61 greedy algorithm

Initialize

\[
\boxed{k_e^{(0)}=1\quad\forall e.}
\]

For each of the \(R=B-m\) remaining units, choose

\[
\boxed{
e_t\in\arg\max_e\Delta_e(k_e^{(t)})}
\]

and update

\[
\boxed{
k_{e_t}^{(t+1)}=k_{e_t}^{(t)}+1.}
\]

All other counts remain unchanged.

In words:

> At each step, spend the next measurement where it reduces the declared uncertainty objective the most right now.

---

## 6. Proposition 61B: greedy selection is globally optimal

The P61 greedy allocation is an exact global minimizer of the integer problem.

### Exchange proof

Let \(k\) be any feasible full-budget allocation. Suppose there exist edges \(e\) and \(f\) such that

\[
k_e>1
\]

and

\[
\boxed{
\Delta_e(k_e-1)
<
\Delta_f(k_f).
}
\]

The quantity

\[
\Delta_e(k_e-1)
\]

is the uncertainty reduction contributed by the **last allocated extra measurement** on edge \(e\).

The quantity

\[
\Delta_f(k_f)
\]

is the reduction available from the **next unallocated measurement** on edge \(f\).

Move one measurement from \(e\) to \(f\). The total budget remains unchanged. The objective change is

\[
\Delta_e(k_e-1)-\Delta_f(k_f)<0,
\]

so the new allocation has strictly smaller uncertainty.

Therefore no optimum can contain a removable selected marginal gain smaller than an available unselected marginal gain.

The greedy algorithm terminates exactly when every selected final marginal gain is at least every currently available next marginal gain. Because each edge's gain sequence decreases, this condition also implies that every earlier selected gain on that edge is at least as large.

Thus no one-unit exchange can improve the greedy allocation, and all selected prefixes collectively contain the largest feasible set of \(R\) marginal gains.

Therefore the greedy allocation is globally optimal.

\(\square\)

---

## 7. Proposition 61C: exact discrete optimality condition

A full-budget integer allocation \(k\) is optimal if and only if

\[
\boxed{
\Delta_e(k_e-1)
\ge
\Delta_f(k_f)
}
\]

for every edge \(e\) with \(k_e>1\) and every edge \(f\).

Equivalently,

\[
\boxed{
\min_{e:k_e>1}\Delta_e(k_e-1)
\ge
\max_f\Delta_f(k_f).
}
\]

The left side is the smallest marginal gain among the last extra measurements currently used.

The right side is the largest marginal gain available from any next unused measurement.

If the inequality fails, a profitable one-unit exchange exists.

If it holds, no selected suffix gain can be replaced by a larger feasible unselected next gain, so the allocation is optimal.

This gives a directly checkable certificate of exact integer optimality.

---

## 8. Ties and uniqueness

The objective value of the greedy solution is always globally optimal.

The allocation vector itself need not be unique if two different edges have exactly equal marginal gains at a decision boundary.

If every marginal-gain comparison encountered at the boundary between selected and unselected gains is strict, then the exact allocation is unique.

Thus P61 distinguishes

\[
\boxed{
\text{exact optimal value}
}
\]

from

\[
\boxed{
\text{possible multiplicity of equally optimal allocations}.
}
\]

---

## 9. Algorithmic complexity

Maintain the currently available next gain for every edge in a max-priority queue.

There are \(m\) initial queue entries and

\[
R=B-m
\]

additional allocations.

Each allocation performs one extraction and one insertion, each costing

\[
O(\log m).
\]

Therefore the greedy solver runs in

\[
\boxed{
O(m+(B-m)\log m)
}
\]

time and

\[
\boxed{O(m)}
\]

memory.

For fixed \(m\), this is linear in the number of additional measurement units up to the priority-queue logarithm.

---

## 10. P60 versus P61

P60 gives a very simple closed-form integer construction:

\[
k_e^{\rm P60}
=
\left\lceil
n_e^*(B-m)
\right\rceil.
\]

Its strength is an immediate explicit approximation guarantee relative to the P59 continuous optimum.

P61 instead uses the full hard budget and solves the integer problem exactly.

Therefore

\[
\boxed{
U(k^{\rm P61})
\le
U(k^{\rm P60})
}
\]

for every instance in which both constructions are defined under the same total budget.

P60 remains useful because it gives a closed-form performance ratio.

P61 is stronger when exact discrete implementation matters.

---

## 11. Relationship to P58-P61

The transition-calibration design chain is now

\[
\boxed{
\begin{array}{c}
\text{P58: finite-data transition uncertainty}\\
\Downarrow\\
\text{P59: exact continuous calibration allocation}\\
\Downarrow\\
\text{P60: feasible integer construction with overhead control}\\
\Downarrow\\
\text{P61: exact integer optimum by diminishing marginal gain.}
\end{array}
}
\]

This closes the continuous-to-discrete resource-allocation problem for the declared separable uncertainty surrogate.

---

## 12. What P61 does not establish

P61 does not establish:

1. that the P59 weights \(w_e\) are uniquely correct for every route-design objective;
2. that the true experiment follows the P58 bounded-observation model;
3. that transition edges should be discovered adaptively without additional statistical accounting;
4. that the full route-envelope width from P58 is separable in the calibration counts;
5. that a scheduling or calibration quantity has experiential meaning;
6. that quantum mechanics is incomplete.

The exactness claim applies to the explicitly declared separable integer surrogate only.

---

## 13. Next theorem target

P61 closes exact integer allocation when every calibration measurement has equal unit cost.

Real transition measurements may have unequal acquisition costs. One edge may require more apparatus time, energy, reset overhead, or experimental resources than another.

The next natural target is therefore a cost-weighted integer calibration problem

\[
\boxed{
\min_k U(k)
\quad\text{subject to}\quad
\sum_e c_e k_e\le B,
}
\]

with edge-specific costs \(c_e>0\).

Unlike P61's unit-cost case, a naive largest-marginal-gain rule is no longer automatically exact. A P62 theorem should characterize what can be solved exactly, what becomes knapsack-like, and which relaxation or approximation guarantees remain valid.

---

## 14. Reproducibility

Implementation:
[`exact_integer_transition_calibration.py`](../src/consciousness_bridge/exact_integer_transition_calibration.py)

Regression tests:
[`test_exact_integer_transition_calibration.py`](../tests/test_exact_integer_transition_calibration.py)

Theorem visual:
[`p61_exact_integer_transition_calibration.svg`](figures/p61_exact_integer_transition_calibration.svg)

---

## 15. Scientific boundary

P61 is an exact discrete optimization theorem for experimental calibration effort under a declared mathematical surrogate. It does not identify the surrogate with consciousness, does not establish a new physical variable, and does not imply any failure of quantum theory.
