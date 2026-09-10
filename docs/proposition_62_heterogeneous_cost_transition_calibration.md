# Proposition 62: heterogeneous-cost transition-calibration allocation

## Status

**Proved exact continuous resource-allocation theorem.** P59 solved the transition-calibration design problem when every additional measurement consumes the same unit of experimental budget. P62 removes that equal-cost assumption and permits each calibrated transition to have its own positive per-measurement cost.

The result remains deliberately narrow. It solves the declared separable inverse-square-root uncertainty surrogate exactly in the continuous domain. It does not solve the corresponding heterogeneous-cost integer problem, the full robust-route calibration problem, or any physical-to-experiential bridge question.

---

## 1. Why heterogeneous costs matter

Different physical transitions can have very different experimental costs.

One transition may require only a fast software-controlled change. Another may require hardware stabilization, thermal settling, subject repositioning, a different stimulus apparatus, a long washout period, or substantially more operator time.

P59 counts calibration effort in interchangeable units. P62 asks the more realistic question:

> If one measurement on transition \(e\) costs \(c_e\) units of time, money, or experimental capacity, how should a fixed total budget be divided?

---

## 2. Setup

For every calibrated transition edge \(e\), let

\[
\rho_e(n_e)=\frac{a_e}{\sqrt{n_e}},
\]

where \(a_e>0\) is the declared uncertainty coefficient and \(n_e>0\) is continuous calibration effort.

Let \(w_e>0\) be the declared sensitivity weight and define

\[
\boxed{b_e=w_ea_e.}
\]

Let

\[
\boxed{c_e>0}
\]

be the cost of one calibration observation on edge \(e\).

The uncertainty surrogate is

\[
\boxed{
U(n)=\sum_{e\in E}\frac{b_e}{\sqrt{n_e}}.
}
\]

The heterogeneous budget constraint is

\[
\boxed{
\sum_{e\in E}c_en_e=B,
\qquad n_e>0,
}
\]

for total budget \(B>0\).

---

## 3. Proposition 62A: unique heterogeneous-cost optimum

Define

\[
\boxed{
T=\sum_{j\in E}b_j^{2/3}c_j^{1/3}.
}
\]

Then the strictly convex P62 problem has the unique optimum

\[
\boxed{
n_e^*
=
\frac{B}{T}
b_e^{2/3}c_e^{-2/3}.
}
\]

The corresponding amount of total budget spent on edge \(e\) is

\[
\boxed{
c_en_e^*
=
B\frac{b_e^{2/3}c_e^{1/3}}{T}.
}
\]

The minimum achievable surrogate uncertainty is

\[
\boxed{
U^*(B)
=
\frac{T^{3/2}}{\sqrt B}.
}
\]

---

## 4. Proof

Because

\[
\frac{d^2}{dn_e^2}\left(b_en_e^{-1/2}\right)
=
\frac{3b_e}{4}n_e^{-5/2}>0,
\]

the objective is strictly convex on the positive orthant. The affine budget set therefore has at most one optimum.

Form the Lagrangian

\[
\mathcal L(n,\lambda)
=
\sum_e b_en_e^{-1/2}
+
\lambda\left(\sum_ec_en_e-B\right).
\]

The first-order condition is

\[
-\frac12b_en_e^{-3/2}+\lambda c_e=0.
\]

Hence

\[
n_e
=
\left(\frac{b_e}{2\lambda c_e}\right)^{2/3}.
\]

Write

\[
K=(2\lambda)^{-2/3}.
\]

Then

\[
n_e=K b_e^{2/3}c_e^{-2/3}.
\]

Substituting into the budget constraint gives

\[
B
=
K\sum_ec_e b_e^{2/3}c_e^{-2/3}
=
K\sum_e b_e^{2/3}c_e^{1/3}
=KT.
\]

Therefore

\[
K=\frac BT
\]

and

\[
\boxed{
n_e^*=\frac BT b_e^{2/3}c_e^{-2/3}.}
\]

For the objective,

\[
\begin{aligned}
U^*(B)
&=
\sum_e
\frac{b_e}
{\sqrt{(B/T)b_e^{2/3}c_e^{-2/3}}}\\
&=
\sqrt{\frac TB}
\sum_e b_e^{2/3}c_e^{1/3}\\
&=
\boxed{\frac{T^{3/2}}{\sqrt B}}.
\end{aligned}
\]

Strict convexity makes this stationary point the unique global optimum. \(\square\)

---

## 5. Two different allocation laws

P62 reveals an important distinction between **number of measurements** and **amount of budget spent**.

The optimal sample count obeys

\[
\boxed{
n_e^*\propto b_e^{2/3}c_e^{-2/3}.}
\]

So, all else equal, expensive edges receive fewer measurements.

But the budget share obeys

\[
\boxed{
c_en_e^*\propto b_e^{2/3}c_e^{1/3}.}
\]

So an expensive edge can still consume more total budget even while receiving fewer observations.

For example, if two edges have identical \(b_e\) values but one costs eight times more per observation, then

\[
\frac{n_{\rm cheap}^*}{n_{\rm expensive}^*}=8^{2/3}=4,
\]

while

\[
\frac{\text{budget}_{\rm expensive}}
{\text{budget}_{\rm cheap}}
=8^{1/3}=2.
\]

The expensive transition receives one quarter as many measurements but consumes twice as much money or time.

---

## 6. Proposition 62B: P59 is an exact special case

If

\[
c_e=c>0
\qquad\forall e,
\]

then

\[
T=c^{1/3}\sum_e b_e^{2/3}.
\]

Therefore

\[
n_e^*
=
\frac{B/c}{\sum_jb_j^{2/3}}b_e^{2/3}.
\]

Thus P62 reduces exactly to P59 with total interchangeable measurement count

\[
N=\frac Bc.
\]

In particular, when \(c=1\), the P59 formula is recovered verbatim.

---

## 7. Proposition 62C: exact target-budget threshold

For target surrogate uncertainty

\[
\varepsilon>0,
\]

P62 gives

\[
U^*(B)\le\varepsilon
\iff
\frac{T^{3/2}}{\sqrt B}\le\varepsilon.
\]

Therefore the continuous heterogeneous-cost budget requirement is exactly

\[
\boxed{
B
\ge
\frac{T^3}{\varepsilon^2}.
}
\]

If the external budget must be recorded as an integer number of cost units, then

\[
\boxed{
B_{\rm sufficient}
=
\left\lceil\frac{T^3}{\varepsilon^2}\right\rceil
}
\]

is sufficient.

This ceiling concerns the **total cost budget**, not integer per-edge sample counts. Integer sample counts with heterogeneous costs remain a separate discrete problem.

---

## 8. Scientific interpretation

P62 answers a practical experimental-design question that the earlier equal-cost formulas could not answer.

It tells the experimenter how to balance three ingredients:

1. how noisy a transition is to estimate, through \(a_e\);
2. how strongly that uncertainty matters to the declared route surrogate, through \(w_e\);
3. how expensive one observation is, through \(c_e\).

The exact allocation law is

\[
\boxed{
\text{measure more when an edge matters more or is noisier,}
\quad
\text{measure less often when each observation is more expensive.}
}
\]

But those effects are not linear. They enter through two-thirds and one-third powers because the uncertainty itself decreases only as the inverse square root of sample count.

---

## 9. P58-P62 calibration chain

The transition-calibration branch now reads

\[
\boxed{
\begin{array}{c}
\text{P58: finite-data metric uncertainty}\\
\Downarrow\\
\text{P59: equal-cost continuous optimal calibration}\\
\Downarrow\\
\text{P60: certified equal-cost integer rounding}\\
\Downarrow\\
\text{P61: exact equal-cost integer allocation}\\
\Downarrow\\
\text{P62: heterogeneous-cost continuous optimal calibration.}
\end{array}
}
\]

P62 deliberately returns to the continuous domain because heterogeneous integer costs create a qualitatively different discrete optimization problem.

---

## 10. What P62 does not establish

P62 does not establish:

1. that \(w_e\) is the only scientifically meaningful sensitivity model;
2. that transition observations really obey the inverse-square-root uncertainty law outside the declared P58 concentration model;
3. that per-edge measurement costs remain fixed under arbitrary adaptive histories;
4. that fractional \(n_e\) values are directly executable;
5. that greedy marginal-gain allocation remains exact when per-measurement costs differ;
6. that the heterogeneous integer problem is easy;
7. that the separable uncertainty surrogate is identical to the full robust-route uncertainty;
8. any experiential or quantum-ontological conclusion.

These boundaries matter because the equal-unit-cost exchange argument of P61 cannot simply be reused when one selected measurement consumes more budget than another.

---

## 11. Next theorem target

The natural next step is the heterogeneous-cost integer problem

\[
\min_{k_e\in\mathbb N,\ k_e\ge1}
\sum_e\frac{b_e}{\sqrt{k_e}}
\quad\text{subject to}\quad
\sum_ec_ek_e\le B.
\]

Unlike P61, one additional measurement no longer consumes the same amount of budget on every edge. Ranking solely by marginal uncertainty decrease is therefore not enough.

A scientifically careful P63 should first determine the computational structure of that discrete problem. Depending on the allowed cost representation, the next result may be an exact dynamic program, a pseudo-polynomial algorithm, an approximation guarantee, or a hardness result rather than another closed-form rule.

---

## 12. Reproducibility

Implementation:
[`heterogeneous_cost_transition_calibration.py`](../src/consciousness_bridge/heterogeneous_cost_transition_calibration.py)

Regression tests:
[`test_heterogeneous_cost_transition_calibration.py`](../tests/test_heterogeneous_cost_transition_calibration.py)

Theorem visual:
[`p62_heterogeneous_cost_transition_calibration.svg`](figures/p62_heterogeneous_cost_transition_calibration.svg)

---

## 13. Scientific boundary

P62 is a continuous resource-allocation theorem for experimental calibration. It does not identify transition cost, uncertainty, routing geometry, or any other operational variable with consciousness. It does not demonstrate quantum incompleteness and does not establish a new physical dimension. Its role is to make the experimental machinery supporting the broader bridge program more efficient and auditable under realistic heterogeneous costs.
