# Proposition 56: Moving-start metric reoptimization stability

## Status

**Proved deterministic perturbation theorem.** P56 removes the fixed-start limitation stated explicitly in P55. It quantifies how much the exact P54 switching optimum can change when the current apparatus/setup state moves from one metric point to another between sequential reoptimization steps.

The theorem assumes one fixed metric switching geometry. It does not itself justify pruning, establish statistical minimaxity of P48 thresholds, or attach experiential meaning to the scheduling quantities.

---

## 1. Setup

For a nonempty active preparation support \(S\), let

\[
L^*(S;s)
\]

denote the minimum P54 switching cost of a path that begins at setup state \(s\) and visits every preparation in \(S\) exactly once, with no return-to-start requirement.

Let \(s\) and \(s'\) be two possible current setup states in the same finite metric space with switching metric \(c\).

For a residual demand vector \(r\), P54 gives

\[
C^*(r;s)
=
a\sum_i r_i+L^*(S(r);s),
\qquad
S(r)=\{i:r_i>0\}.
\]

P55 considered residual changes while holding \(s\) fixed. P56 allows \(s\) to move.

---

## 2. Proposition 56A: the optimal route is 1-Lipschitz in the start state

For every nonempty finite support \(S\),

\[
\boxed{
\left|L^*(S;s)-L^*(S;s')\right|
\le c(s,s').
}
\]

### Proof

Let

\[
\pi^*=(v_1,\ldots,v_m)
\]

be an optimal route for start state \(s\). Reuse exactly the same preparation order from start state \(s'\). Only the first route edge changes. By triangle inequality,

\[
c(s',v_1)
\le c(s',s)+c(s,v_1).
\]

Therefore

\[
L^*(S;s')
\le c(s',s)+L^*(S;s).
\]

Interchanging \(s\) and \(s'\) gives

\[
L^*(S;s)
\le c(s,s')+L^*(S;s').
\]

Symmetry of the metric then yields

\[
|L^*(S;s)-L^*(S;s')|
\le c(s,s').
\]

\(\square\)

The coefficient one is sharp. With a single required preparation \(v\) on a line and starts \(s,s'\) lying on the same side of \(v\), the difference in optimal route costs can equal \(c(s,s')\).

---

## 3. Proposition 56B: fixed residual demand inherits the same Lipschitz bound

If the residual vector \(r\) is unchanged, then the acquisition term is identical under both starts. Hence

\[
\boxed{
|C^*(r;s)-C^*(r;s')|
\le c(s,s').
}
\]

Thus apparatus/setup displacement enters the exact deterministic residual objective with Lipschitz constant at most one in the switching metric.

---

## 4. Proposition 56C: residual decrease with a moving start

Let \(r'\le r\) componentwise. Define the P55 fixed-start release

\[
\Delta_{\rm fixed}
=
C^*(r;s)-C^*(r';s).
\]

P55 proves \(\Delta_{\rm fixed}\ge0\). P56A applied to the new residual support gives

\[
C^*(r';s')
\le
C^*(r';s)+c(s,s').
\]

Therefore

\[
\boxed{
C^*(r;s)-C^*(r';s')
\ge
\Delta_{\rm fixed}-c(s,s').
}
\]

Equivalently,

\[
\boxed{
C^*(r';s')
\le
C^*(r;s)-\Delta_{\rm fixed}+c(s,s').
}
\]

The setup movement can therefore erase at most one metric displacement worth of the savings that P55 certified under a fixed start.

---

## 5. Proposition 56D: strict-decrease certificate

A simple sufficient condition for the new optimum to remain strictly lower despite moving the start is

\[
\boxed{
\Delta_{\rm fixed}>c(s,s').
}
\]

Under this condition,

\[
\boxed{
C^*(r';s')<C^*(r;s).
}
\]

This certificate is directly computable from the old state, the P55 fixed-start reoptimization, and the metric distance between the two setup states.

The converse is not claimed. If

\[
\Delta_{\rm fixed}\le c(s,s'),
\]

the lower bound may be nonpositive even though the actual moving-start reoptimization still decreases cost. The theorem gives a guarantee, not an iff criterion.

---

## 6. Combined P55-P56 decomposition

P55 gives

\[
\Delta_{\rm fixed}
=
a\left(\sum_i r_i-\sum_i r_i'\right)
+
\left[L^*(S(r);s)-L^*(S(r');s)\right].
\]

P56 therefore implies

\[
\boxed{
C^*(r;s)-C^*(r';s')
\ge
a\left(\sum_i r_i-\sum_i r_i'\right)
+
\left[L^*(S(r);s)-L^*(S(r');s)\right]
-c(s,s').
}
\]

This separates three experimentally meaningful effects:

1. **residual acquisition release** from additional data;
2. **route release** from active-support deletion;
3. **start-motion penalty** caused by ending up at a different setup state.

The first two are nonnegative in the P55 metric regime. The third can reduce the guaranteed improvement, but by no more than the metric displacement between setup states.

---

## 7. Tightness and interpretation

The start-state bound cannot generally be improved below coefficient one. Consider one remaining preparation at coordinate \(x=3\), with old start \(s=0\) and new start \(s'=1\) under the ordinary line metric. Then

\[
L^*(\{v\};s)=3,
\qquad
L^*(\{v\};s')=2,
\qquad
c(s,s')=1,
\]

so equality holds in P56A.

The theorem also clarifies why the start state must be treated separately from support deletion. P55's monotonicity is exact when the setup origin is fixed. Once the physical apparatus has moved, the residual optimization remains stable, but strict monotonicity can only be guaranteed after accounting for that movement.

---

## 8. Assumptions and boundary

P56 requires:

- the same declared metric switching geometry before and after reoptimization;
- finite route costs;
- the P54 block-routing model;
- componentwise residual decrease only when invoking the P55-P56 combined bound.

If the switching-cost geometry itself changes with time, temperature, calibration state, hardware degradation, operator effects, or other context, then \(c\) becomes a time-varying object and the present one-metric Lipschitz theorem does not by itself control the change. That requires a separate metric-perturbation result.

---

## 9. Implementation and reproducibility

The executable implementation is

[`src/consciousness_bridge/moving_start_metric_reoptimization.py`](../src/consciousness_bridge/moving_start_metric_reoptimization.py).

It provides:

- exact start-Lipschitz certificates;
- fixed-residual total-cost perturbation checks;
- combined residual-decrease and moving-start reoptimization certificates;
- a strict-decrease certificate when P55 savings exceed setup displacement.

Regression tests are in

[`tests/test_moving_start_metric_reoptimization.py`](../tests/test_moving_start_metric_reoptimization.py).

The theorem visual is

[`docs/figures/p56_moving_start_metric_reoptimization_stability.svg`](figures/p56_moving_start_metric_reoptimization_stability.svg).

---

## 10. Scientific boundary

P56 is a deterministic metric perturbation theorem for experimental scheduling. It does not establish that any residual threshold is statistically minimal, does not independently validate a pruning decision, and does not identify setup distance, path length, acquisition cost, or any other scheduling quantity with consciousness. It makes no claim that quantum mechanics is incomplete.
