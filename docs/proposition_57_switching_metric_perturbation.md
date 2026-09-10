# Proposition 57: Switching-metric perturbation reoptimization stability

## Status

**Proved deterministic metric-perturbation theorem.** P57 removes the fixed-metric limitation stated explicitly in P56. It quantifies how much the exact P54 switching optimum can change when the declared transition metric itself changes between sequential reoptimization steps.

The theorem is conditional on two valid finite metrics defined on one common preparation/setup point set. It does not estimate the metric from data, justify pruning, establish statistical minimaxity of P48 thresholds, or attach experiential meaning to any scheduling quantity.

---

## 1. Setup

Let

\[
c
\quad\text{and}\quad
c'
\]

be two finite metrics on the same relevant point set. They may represent two deterministic switching geometries before and after recalibration, environmental change, apparatus drift, or another declared operational change.

For active preparation support

\[
S\subseteq V,
\]

and optional current setup state \(s\), let

\[
L_c^*(S;s)
\]

denote the exact P54 minimum switching path length under metric \(c\), beginning at \(s\) when a start is supplied, visiting every preparation in \(S\) exactly once, and requiring no return to the start.

Define the uniform metric perturbation size

\[
\boxed{
\delta(c,c';X)
=
\max_{x,y\in X}
|c(x,y)-c'(x,y)|,
}
\]

where \(X\) contains the active preparations and every setup state needed by the comparison.

---

## 2. Effective route-edge count

For nonempty support \(S\), define

\[
\boxed{
q(S;s)
=
\begin{cases}
|S|-1, & s=\varnothing,\\
|S|-1, & s\in S,\\
|S|, & s\notin S.
\end{cases}
}
\]

If no start is supplied, a Hamiltonian path through \(|S|\) preparations contains \(|S|-1\) edges.

If the setup start \(s\) lies outside the active support, the rooted path adds one initial edge and contains \(|S|\) switching edges.

If \(s\in S\), metric shortcutting permits an optimum that begins at \(s\) itself, so there are again only \(|S|-1\) nontrivial switching edges.

For empty support define

\[
q(\varnothing;s)=0.
\]

---

## 3. Proposition 57A: optimal route stability under metric perturbation

Let \(S\neq\varnothing\), and let \(X\) contain \(S\) and the supplied start state when that start lies outside \(S\). Then

\[
\boxed{
\left|
L_c^*(S;s)-L_{c'}^*(S;s)
\right|
\le
q(S;s)\,\delta(c,c';X).
}
\]

### Proof

Let

\[
\pi=(v_1,\ldots,v_m)
\]

be any feasible rooted block order. Its switching path contains at most

\[
q(S;s)
\]

nontrivial metric edges. Since every relevant edge satisfies

\[
|c(x,y)-c'(x,y)|\le\delta,
\]

the route lengths satisfy

\[
\boxed{
|\ell_c(\pi;s)-\ell_{c'}(\pi;s)|
\le
q(S;s)\delta.
}
\]

Let \(\pi_c^*\) be optimal under \(c\). Reuse the same route under \(c'\):

\[
L_{c'}^*(S;s)
\le
\ell_{c'}(\pi_c^*;s)
\le
L_c^*(S;s)+q(S;s)\delta.
\]

Interchanging \(c\) and \(c'\) gives

\[
L_c^*(S;s)
\le
L_{c'}^*(S;s)+q(S;s)\delta.
\]

Therefore

\[
\left|
L_c^*(S;s)-L_{c'}^*(S;s)
\right|
\le
q(S;s)\delta.
\]

\(\square\)

---

## 4. Sharpness

The coefficient \(q(S;s)\) cannot generally be improved under only a uniform entrywise metric perturbation bound.

Take an external start and a line metric on the required route points. Define a second metric by adding the same positive amount \(\delta\) to every off-diagonal distance while keeping the diagonal zero:

\[
c'(x,y)
=
\begin{cases}
0,&x=y,\\
c(x,y)+\delta,&x\neq y.
\end{cases}
\]

This remains a metric because

\[
c(x,z)+\delta
\le
c(x,y)+c(y,z)+2\delta.
\]

Every rooted route with \(q(S;s)\) nontrivial edges then increases by exactly

\[
q(S;s)\delta.
\]

Hence equality is achievable in P57A.

---

## 5. Proposition 57B: fixed residual demand inherits the same bound

For residual demand vector \(r\), P54 gives

\[
C_c^*(r;s)
=
a\sum_i r_i+L_c^*(S(r);s).
\]

If the residual demand and sample cost are unchanged while only the metric changes, the acquisition term cancels. Therefore

\[
\boxed{
|C_c^*(r;s)-C_{c'}^*(r;s)|
\le
q(S(r);s)\,\delta.
}
\]

Thus deterministic metric drift affects only the switching component of the exact P54 objective.

---

## 6. Proposition 57C: simultaneous residual decrease, start motion, and metric drift

Let

\[
r'\le r
\]

componentwise. Let the old state use metric \(c\) and setup start \(s\), while the new state uses metric \(c'\) and start \(s'\).

Define the P55 fixed-geometry release

\[
\boxed{
\Delta_{\rm fixed}
=
C_c^*(r;s)-C_c^*(r';s)
\ge0.
}
\]

Let

\[
S'=S(r').
\]

Suppose \(S'\neq\varnothing\), and let \(\delta\) be the P57 uniform metric perturbation on a common point set containing \(S'\), \(s\), and \(s'\).

There are two valid perturbation orders.

First move the start under the old metric and then perturb the metric:

\[
C_{c'}^*(r';s')
\le
C_c^*(r';s)
+c(s,s')
+q(S';s')\delta.
\]

Alternatively perturb the metric first and then move the start under the new metric:

\[
C_{c'}^*(r';s')
\le
C_c^*(r';s)
+q(S';s)\delta
+c'(s,s').
\]

Therefore define

\[
\boxed{
P_{57}
=
\min\left\{
 c(s,s')+q(S';s')\delta,
 q(S';s)\delta+c'(s,s')
\right\}.
}
\]

Then

\[
\boxed{
C_c^*(r;s)-C_{c'}^*(r';s')
\ge
\Delta_{\rm fixed}-P_{57}.
}
\]

Equivalently,

\[
\boxed{
C_{c'}^*(r';s')
\le
C_c^*(r;s)-\Delta_{\rm fixed}+P_{57}.
}
\]

This is the first theorem in the scheduling chain that permits all three deterministic changes simultaneously:

\[
\boxed{
\text{residual demand}
+
\text{setup origin}
+
\text{switching geometry}.
}
\]

---

## 7. Proposition 57D: strict-decrease certificate under metric drift

A sufficient condition for the new exact optimum to remain strictly lower is

\[
\boxed{
\Delta_{\rm fixed}>P_{57}.
}
\]

Then

\[
\boxed{
C_{c'}^*(r';s')<C_c^*(r;s).
}
\]

The converse is not claimed. The perturbation penalty is a worst-case certificate. The actual reoptimized route may exploit the new geometry and achieve a larger reduction.

---

## 8. Proposition 57E: route-reuse upper bound

The uniform \(q\delta\) bound ignores the actual route structure. A sharper one-sided certificate can be computed directly from the old optimum.

Let

\[
\pi_c^*
\]

be an optimal P54 order under \((c,s)\). Evaluate that exact order under the new geometry and start:

\[
\ell_{c'}(\pi_c^*;s').
\]

Since the new optimum cannot exceed the cost of this reused feasible route,

\[
\boxed{
L_{c'}^*(S;s')
\le
\ell_{c'}(\pi_c^*;s').
}
\]

Therefore

\[
\boxed{
L_{c'}^*(S;s')-L_c^*(S;s)
\le
\ell_{c'}(\pi_c^*;s')-L_c^*(S;s).
}
\]

This route-reuse bound can be substantially tighter than the uniform metric bound because it uses only the edges actually traversed by the old optimum.

It also remains valid when the right side is negative, in which case simply reusing the old route is already cheaper under the new geometry.

---

## 9. Complete P53-P57 deterministic scheduling chain

The sequential design branch now has the following structure:

\[
\boxed{
\begin{array}{c}
\text{P53: residual sample demand decreases}\\
\Downarrow\\
\text{P54: exact acquisition + metric route optimum}\\
\Downarrow\\
\text{P55: support deletion and acquisition release}\\
\Downarrow\\
\text{P56: moving-start stability}\\
\Downarrow\\
\text{P57: switching-metric perturbation stability.}
\end{array}
}
\]

P55 controls the change in what remains to be measured.

P56 controls where the apparatus currently is.

P57 controls how the deterministic transition geometry itself has changed.

Together they yield an auditable perturbation decomposition for sequential experimental reoptimization.

---

## 10. What P57 does not establish

P57 does not justify arbitrary changing cost tables. Both \(c\) and \(c'\) must satisfy the declared metric assumptions on the relevant common point set.

It also does not establish:

1. **Metric estimation validity.** If switching costs are themselves estimated from noisy observations, their uncertainty requires a separate statistical theorem.
2. **Nonmetric transition stability.** The P54-P57 geometric chain relies on metric structure. Directed, state-dependent, or hysteretic transition costs require another model.
3. **Pruning validity.** A preparation can only be removed from residual support when the statistical or experimental logic justifying that removal is valid.
4. **Minimax sequential efficiency.** P57 is deterministic perturbation analysis, not a lower-bound theorem for adaptive sampling.
5. **Physical or experiential ontology.** Switching cost, route length, metric drift, and residual burden are scheduling quantities only.

---

## 11. Next theorem target

P57 treats both switching metrics as known deterministic objects. In a real experiment, transition cost can itself be uncertain because of measurement noise, calibration error, thermal state, operator variability, hardware drift, or finite timing observations.

The next theorem should therefore place the switching metric inside a confidence set and derive a robust route certificate of the form

\[
\boxed{
\sup_{c\in\mathcal C_t}
L_c^*(S;s)
}
\]

or a computable upper envelope for it.

A natural P58 target is therefore:

\[
\boxed{
\text{finite-data switching-metric uncertainty}
\longrightarrow
\text{robust reoptimization certificate}.
}
\]

---

## 12. Implementation and reproducibility

The executable implementation is

[`src/consciousness_bridge/switching_metric_perturbation.py`](../src/consciousness_bridge/switching_metric_perturbation.py).

It provides:

- finite common-metric sup-distance evaluation;
- the sharp route-edge-count factor \(q(S;s)\);
- fixed-residual P57 metric perturbation certificates;
- combined P55-P56-P57 residual/start/metric reoptimization certificates;
- a tighter one-sided route-reuse certificate.

Regression tests are in

[`tests/test_switching_metric_perturbation.py`](../tests/test_switching_metric_perturbation.py).

The theorem visual is

[`docs/figures/p57_switching_metric_perturbation.svg`](figures/p57_switching_metric_perturbation.svg).

---

## 13. Scientific boundary

P57 is a deterministic robustness theorem for experimental scheduling under two declared finite metrics. It does not establish that any residual threshold is statistically optimal, does not independently validate pruning, does not infer hidden physics from a change in transition geometry, and does not identify any metric or route quantity with consciousness. It makes no claim that quantum mechanics is incomplete.
