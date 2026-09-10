# Proposition 58: Finite-data switching-metric uncertainty and robust reoptimization

## Status

**Proved finite-data confidence-envelope theorem under a declared bounded pairwise transition-observation model.** P58 extends P57 from known deterministic switching metrics to an unknown true metric whose pairwise transition costs are estimated from finite noisy measurements.

P58 is deliberately formulated so that the empirical pairwise cost table does **not** need to satisfy the triangle inequality. Sampling noise can make an empirical distance table nonmetric even when the underlying physical transition cost is metric. The theorem therefore places simultaneous confidence intervals around individual transition costs and optimizes directly over lower and upper route envelopes.

The result is an experimental scheduling theorem. It does not validate a transition-cost measurement model, justify adaptive pruning, prove minimax sequential efficiency, imply new physics, identify any scheduling variable with consciousness, or establish that quantum mechanics is incomplete.

---

## 1. Unknown true switching metric

Let

\[
X=\{x_1,\ldots,x_m\}
\]

be a finite set containing the preparations and any current setup state required by the scheduling problem.

Assume there exists an unknown true finite metric

\[
\boxed{
c:X\times X\to[0,\infty)
}
\]

with

\[
c(x,x)=0,
\qquad
c(x,y)=c(y,x),
\]

and

\[
c(x,z)\le c(x,y)+c(y,z).
\]

The metric assumption is the physical premise used by P54 to justify shortcutting arbitrary revisiting schedules into one contiguous block per positive-demand preparation.

P58 does **not** assume that the empirical estimator of \(c\) is itself a metric.

---

## 2. Pairwise finite-data model

For every unordered pair

\[
e=\{x,y\},
\qquad x\neq y,
\]

suppose the experiment obtains

\[
Z_{e,1},\ldots,Z_{e,n_e}
\]

with mean

\[
\mathbb E[Z_{e,k}]=c_e:=c(x,y).
\]

For the explicit concentration result below, assume the observations for each fixed pair are independent and lie in a declared interval of width

\[
B_e>0.
\]

Let

\[
\widehat c_e
=
\frac1{n_e}
\sum_{k=1}^{n_e}Z_{e,k}.
\]

Independence **between different transition pairs is not required** for the family-level union bound. What is required is a valid marginal concentration statement for every pair.

Allocate pairwise failure probabilities

\[
\alpha_e>0
\]

such that

\[
\boxed{
\sum_e\alpha_e\le\alpha.
}
\]

---

## 3. Proposition 58A: simultaneous pairwise metric-entry confidence event

Hoeffding's inequality gives, for every pair,

\[
\Pr\left(
|\widehat c_e-c_e|>\rho_e
\right)
\le\alpha_e
\]

for

\[
\boxed{
\rho_e
=
B_e
\sqrt{
\frac{1}{2n_e}
\log\frac{2}{\alpha_e}
}.
}
\]

Define

\[
\mathcal E_c
=
\bigcap_e
\left\{
|\widehat c_e-c_e|\le\rho_e
\right\}.
\]

By the union bound,

\[
\Pr(\mathcal E_c^c)
\le
\sum_e\alpha_e
\le\alpha.
\]

Therefore

\[
\boxed{
\Pr\left(
|\widehat c_e-c_e|\le\rho_e
\quad\forall e
\right)
\ge1-\alpha.
}
\]

This event contains all finite-data uncertainty needed for the remaining deterministic route arguments.

### Equal pairwise spending

If there are

\[
M=\binom{|X|}{2}
\]

unordered pairs and the error budget is split equally,

\[
\alpha_e=\frac\alpha M,
\]

then

\[
\boxed{
\rho_e
=
B_e
\sqrt{
\frac{1}{2n_e}
\log\frac{2M}{\alpha}
}.
}
\]

Positive predeclared pair weights may instead be used to allocate the total error budget nonuniformly.

---

## 4. Why the empirical center need not be a metric

The sample means

\[
\widehat c(x,y)
\]

can violate a triangle inequality such as

\[
\widehat c(x,z)
>
\widehat c(x,y)+\widehat c(y,z)
\]

purely because different pairwise measurements fluctuate in different directions.

Projecting \(\widehat c\) onto the metric cone could be useful computationally, but doing so changes the estimator and requires an additional error-propagation argument.

P58 avoids that extra assumption.

The unknown \(c\) remains metric. The empirical center only needs to be finite, symmetric, nonnegative, and accompanied by simultaneous valid entrywise radii.

---

## 5. Routewise confidence envelopes

Let

\[
S\subseteq X
\]

be the positive-demand preparation support, and let

\[
\pi=(v_1,\ldots,v_k)
\]

be one candidate block order.

Let

\[
T(\pi;s)
\]

denote the set of transition edges traversed by that route, including the initial edge from a supplied setup state \(s\) to \(v_1\).

Define the pairwise lower and upper transition bounds

\[
\boxed{
\underline c_e
=
\max\{0,\widehat c_e-\rho_e\},
\qquad
\overline c_e
=
\widehat c_e+\rho_e.
}
\]

Define the lower and upper route envelopes

\[
\boxed{
\underline\ell(\pi;s)
=
\sum_{e\in T(\pi;s)}\underline c_e,
}
\]

and

\[
\boxed{
\overline\ell(\pi;s)
=
\sum_{e\in T(\pi;s)}\overline c_e.
}
\]

On \(\mathcal E_c\), every traversed true edge lies inside its interval, so

\[
\boxed{
\underline\ell(\pi;s)
\le
\ell_c(\pi;s)
\le
\overline\ell(\pi;s)
}
\]

for **every** candidate block order \(\pi\) simultaneously.

---

## 6. Proposition 58B: confidence interval for the exact unknown P54 route optimum

Let

\[
\Pi(S)
\]

be the finite family of all permutations of the active preparation support.

Define

\[
\boxed{
L^-(S;s)
=
\min_{\pi\in\Pi(S)}
\underline\ell(\pi;s),
}
\]

and

\[
\boxed{
L^+(S;s)
=
\min_{\pi\in\Pi(S)}
\overline\ell(\pi;s).
}
\]

The true P54 switching optimum is

\[
L_c^*(S;s)
=
\min_{\pi\in\Pi(S)}
\ell_c(\pi;s).
\]

On \(\mathcal E_c\), for every route \(\pi\),

\[
\underline\ell(\pi;s)
\le
\ell_c(\pi;s).
\]

Taking the minimum on both sides gives

\[
L^-(S;s)
\le
L_c^*(S;s).
\]

For the upper bound, let

\[
\pi^+
\in
\arg\min_{\pi}\overline\ell(\pi;s).
\]

Then

\[
L_c^*(S;s)
\le
\ell_c(\pi^+;s)
\le
\overline\ell(\pi^+;s)
=
L^+(S;s).
\]

Hence

\[
\boxed{
L^-(S;s)
\le
L_c^*(S;s)
\le
L^+(S;s)
}
\]

simultaneously on the same pairwise confidence event.

Therefore

\[
\boxed{
\Pr\left(
L^-(S;s)
\le
L_c^*(S;s)
\le
L^+(S;s)
\right)
\ge1-\alpha.
}
\]

No empirical triangle inequality is used in this proof.

---

## 7. Exact computation of the two envelopes

The two route-envelope optima are finite shortest-permutation problems.

For the lower problem use the edge table

\[
\underline c_e.
\]

For the upper problem use

\[
\overline c_e.
\]

These tables need not themselves be metrics. That does not prevent exact Held-Karp dynamic programming because P58 is no longer using metric shortcutting to derive the route family. P54 already supplied the block-route family from the unknown true metric; P58 only optimizes confidence envelopes over that fixed finite family.

Thus the P54 Held-Karp state structure remains applicable even though its edge weights are now lower or upper uncertainty envelopes rather than a physical metric.

---

## 8. Proposition 58C: total residual execution-cost interval

For residual demand vector \(r\) and per-sample acquisition cost \(a>0\), define

\[
A(r)=a\sum_i r_i.
\]

The acquisition term is deterministic once \(r\) and \(a\) are declared.

The unknown true total P54 cost is

\[
C_c^*(r;s)
=
A(r)+L_c^*(S(r);s).
\]

Therefore P58B immediately yields

\[
\boxed{
C^-(r;s)
:=A(r)+L^-(S(r);s)
\le
C_c^*(r;s)
\le
A(r)+L^+(S(r);s)
=:C^+(r;s).
}
\]

with confidence at least \(1-\alpha\).

This is the finite-data robust replacement for treating a noisy estimated switching table as though it were exact.

---

## 9. Proposition 58D: robust route selection and regret certificate

Use the upper-envelope minimizer

\[
\boxed{
\pi^{\rm rob}
\in
\arg\min_{\pi}
\overline\ell(\pi;s).
}
\]

This route minimizes the directly certified routewise upper bound.

On \(\mathcal E_c\),

\[
\ell_c(\pi^{\rm rob};s)
\le
L^+(S;s).
\]

Also

\[
L_c^*(S;s)
\ge
L^-(S;s).
\]

Subtracting gives

\[
\boxed{
0
\le
\ell_c(\pi^{\rm rob};s)-L_c^*(S;s)
\le
L^+(S;s)-L^-(S;s).
}
\]

Thus the width

\[
\boxed{
G_{\rm route}
=L^+-L^-
}
\]

is a finite-data upper bound on the unknown regret incurred by executing the robust upper-envelope route rather than the unknown true optimal route.

If

\[
G_{\rm route}=0,
\]

then the robust route is certified optimal for every true cost table consistent with the simultaneous intervals.

---

## 10. Proposition 58E: robust comparison of two reoptimization states

Suppose an old scheduling state has true unknown cost

\[
C_{c_0}^*(r_0;s_0)
\]

and a new scheduling state has true unknown cost

\[
C_{c_1}^*(r_1;s_1).
\]

Construct simultaneous P58 intervals

\[
[C_0^-,C_0^+]
\]

and

\[
[C_1^-,C_1^+].
\]

If the two underlying metric confidence events are jointly valid with failure probability at most \(\alpha\), then on that event

\[
C_{c_0}^*(r_0;s_0)
\ge C_0^-
\]

and

\[
C_{c_1}^*(r_1;s_1)
\le C_1^+.
\]

Therefore

\[
\boxed{
C_0^->C_1^+
\Longrightarrow
C_{c_0}^*(r_0;s_0)
>
C_{c_1}^*(r_1;s_1).
}
\]

The guaranteed reduction is at least

\[
\boxed{
\Delta_{\rm robust}
=C_0^- - C_1^+.
}
\]

If old and new confidence constructions use separate budgets \(\alpha_0\) and \(\alpha_1\), another union bound gives joint confidence at least

\[
1-\alpha_0-\alpha_1.
\]

No independence between the two states is needed for this coverage statement.

---

## 11. P57 as a metric-center special case

Suppose a postprocessed center

\[
\widetilde c
\]

is itself a valid metric and is known on the confidence event to satisfy

\[
\max_{x,y}|c(x,y)-\widetilde c(x,y)|
\le\eta.
\]

Then P57 applies directly:

\[
\boxed{
|L_c^*(S;s)-L_{\widetilde c}^*(S;s)|
\le
q(S;s)\eta.
}
\]

This gives a compact symmetric interval around the metric-center optimum.

P58 is more general because it does not require the empirical center to be metric and can exploit heterogeneous pair-specific radii \(\rho_e\).

---

## 12. Rectangular-envelope width under a common radius

Suppose

\[
\rho_e\le\eta
\]

for every relevant transition pair.

Let

\[
q_{\rm rect}(S;s)
=
\begin{cases}
|S|-1,&s\text{ is absent},\\
|S|,&s\text{ is supplied}.
\end{cases}
\]

Every candidate route in the rectangular-envelope optimization contains at most \(q_{\rm rect}\) listed transitions. Each transition interval has width at most \(2\eta\). Therefore

\[
\boxed{
0\le L^+(S;s)-L^-(S;s)
\le
2q_{\rm rect}(S;s)\eta.
}
\]

This bound is intentionally slightly more conservative than P57's sharp metric-center factor when the supplied start itself belongs to \(S\). P58 allows the lower and upper empirical envelope tables to be nonmetric, so it does not use metric shortcutting inside those auxiliary optimization problems.

---

## 13. Explicit common-sample sufficient condition

Assume every unordered pair uses the same sample count \(n\), every observation range has width at most \(B\), and the \(M\) pairwise failure probabilities are allocated equally.

Then

\[
\eta
=
B
\sqrt{
\frac{1}{2n}
\log\frac{2M}{\alpha}
}.
\]

To guarantee a P58 rectangular route interval of width at most \(\varepsilon>0\), it is sufficient that

\[
2q_{\rm rect}\eta
\le\varepsilon.
\]

Solving for \(n\) gives

\[
\boxed{
n
\ge
\frac{2B^2q_{\rm rect}^2}{\varepsilon^2}
\log\frac{2M}{\alpha}.
}
\]

This is a sufficient design inequality, not a minimax lower bound.

It shows explicitly how transition-metric calibration burden scales with:

- the squared route-edge count;
- the squared observation range;
- inverse squared desired route precision;
- logarithmically with the number of calibrated pairs and inverse confidence level.

---

## 14. Relationship to P53-P57

The scheduling chain is now

\[
\boxed{
\begin{array}{c}
\text{P53: residual demand}\\
\Downarrow\\
\text{P54: exact metric acquisition + routing}\\
\Downarrow\\
\text{P55: support-deletion monotonicity}\\
\Downarrow\\
\text{P56: setup-origin perturbation}\\
\Downarrow\\
\text{P57: deterministic metric perturbation}\\
\Downarrow\\
\text{P58: finite-data metric uncertainty and robust routing.}
\end{array}
}
\]

P57 says what happens when two metric tables are known.

P58 says what can still be certified when the true metric table is not known exactly.

The distinction is essential in an experiment where switching costs are measured rather than assumed.

---

## 15. What P58 does not establish

P58 does not establish:

1. **Validity under unrestricted drift.** The explicit Hoeffding construction assumes a fixed pairwise mean during the calibration sample for each transition pair.
2. **Validity under arbitrary dependence within a pair.** The stated radius uses independent bounded observations for that pair. Other dependence models require other concentration results.
3. **Metric truth from noisy observations.** The true-metric property is a declared physical/model assumption, not a consequence of the sample means.
4. **Optimal metric projection.** P58 deliberately does not require projecting the empirical table onto the metric cone.
5. **Adaptive pair-selection validity.** If transition pairs or their calibration sample sizes are chosen using the same noisy measurements in a way not covered by a simultaneous or anytime-valid construction, additional accounting is required.
6. **Pruning validity.** Residual support reduction must still be justified by the relevant P47-P53 statistical logic.
7. **Minimax optimality.** The Hoeffding-union construction and robust upper-envelope route are transparent valid methods, not claims of optimal statistical efficiency.
8. **Physical or experiential interpretation.** Transition costs and their confidence intervals are operational scheduling quantities only.

---

## 16. Next theorem target

P58 treats pairwise calibration sample counts

\[
n_e
\]

as already chosen.

But not every transition pair contributes equally to the final route uncertainty. Some edges never appear in competitive routes; some are common to many near-optimal routes; some have much larger measurement variance or calibration cost.

The next natural problem is therefore to allocate a finite transition-calibration budget across edges so as to minimize a robust route uncertainty criterion.

A P59 target is

\[
\boxed{
\text{edge-specific calibration budget}
\longrightarrow
\text{optimal reduction of robust route uncertainty}.
}
\]

That would convert P58 from a finite-data certification theorem into a principled metric-calibration design theorem.

---

## 17. Reproducibility

Implementation:
[`finite_data_metric_uncertainty.py`](../src/consciousness_bridge/finite_data_metric_uncertainty.py)

Regression tests:
[`test_finite_data_metric_uncertainty.py`](../tests/test_finite_data_metric_uncertainty.py)

Theorem visual:
[`p58_finite_data_metric_uncertainty.svg`](figures/p58_finite_data_metric_uncertainty.svg)

---

## 18. Scientific boundary

P58 supplies finite-data uncertainty propagation for a declared experimental switching metric. It does not turn a scheduling distance into a physical state variable, does not infer an experiential dimension, and does not weaken the repository's distinction between operational mathematics and a physical-to-experiential bridge. The theorem makes no claim that quantum mechanics is incomplete.
