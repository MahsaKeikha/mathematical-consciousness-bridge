# Proposition 43: Optimal quantum-target uncertainty allocation

## Status

**Proved resource-allocation theorem for the P42 finite-sample design.** P43 removes the arbitrary choice of the P42 gap-allocation parameter and derives the unique allocation that minimizes a declared weighted sampling cost.

The theorem optimizes resources only within the assumptions of P42. It does not establish physical completeness, quantum incompleteness, or consciousness.

---

## 1. P42 sample-size family

P42 considers a preparation pair with positive population regularity gap

\[
\Delta=d_Y-Ld_Q>0.
\]

For a gap allocation

\[
\lambda\in(0,1),
\]

P42 gives sufficient per-preparation sample sizes

\[
n_Y\ge\frac{A_Y}{\lambda^2},
\qquad
n_Q\ge\frac{A_Q}{(1-\lambda)^2},
\]

where

\[
\boxed{
A_Y
=
\frac{2k^2}{\Delta^2}
\log\frac{2Kk}{\alpha_Y}
}
\]

and

\[
\boxed{
A_Q
=
\frac{8L^2\kappa_R^2m^2}{\Delta^2}
\log\frac{2Km}{\alpha_Q}.
}
\]

Here \(K\) is the number of preparations, \(k\) is the target alphabet size, \(m\) is the number of outcomes in the fixed informationally complete POVM, \(L\) is the declared bridge Lipschitz constant, and \(\kappa_R\) is the P42 linear-reconstruction stability constant.

P42 allowed any \(\lambda\in(0,1)\). P43 asks which choice uses the least declared experimental resource.

---

## 2. Weighted experimental cost

Let

\[
c_Y>0,
\qquad
c_Q>0
\]

be declared costs per target observation and quantum measurement repetition, respectively.

The continuous weighted per-preparation sampling cost is

\[
\boxed{
C(\lambda)
=
c_Y\frac{A_Y}{\lambda^2}
+
c_Q\frac{A_Q}{(1-\lambda)^2}.
}
\]

Multiplying by \(K\) gives total cost over all preparations and does not change the optimizing \(\lambda\).

Define

\[
a=c_YA_Y,
\qquad
b=c_QA_Q.
\]

Under the nondegenerate P42 regime \(a,b>0\),

\[
C(\lambda)=\frac{a}{\lambda^2}+\frac{b}{(1-\lambda)^2}.
\]

---

## 3. Strict convexity

The first derivative is

\[
C'(\lambda)
=-\frac{2a}{\lambda^3}
+\frac{2b}{(1-\lambda)^3}.
\]

The second derivative is

\[
\boxed{
C''(\lambda)
=
\frac{6a}{\lambda^4}
+
\frac{6b}{(1-\lambda)^4}
>0.
}
\]

Therefore \(C\) is strictly convex on \((0,1)\). Since

\[
C(\lambda)\to\infty
\]

as \(\lambda\to0^+\) or \(\lambda\to1^-\), there is one unique global minimizer.

---

## 4. P43A: cube-root allocation law

Set \(C'(\lambda)=0\):

\[
\frac{a}{\lambda^3}
=
\frac{b}{(1-\lambda)^3}.
\]

Taking positive cube roots gives

\[
\frac{\lambda}{1-\lambda}
=
\left(\frac{a}{b}\right)^{1/3}.
\]

Hence the unique optimal target-side gap fraction is

\[
\boxed{
\lambda_*
=
\frac{a^{1/3}}
{a^{1/3}+b^{1/3}}
}
\]

or, in the original experimental quantities,

\[
\boxed{
\lambda_*
=
\frac{(c_YA_Y)^{1/3}}
{(c_YA_Y)^{1/3}+(c_QA_Q)^{1/3}}.
}
\]

The quantum-side fraction is

\[
\boxed{
1-\lambda_*
=
\frac{(c_QA_Q)^{1/3}}
{(c_YA_Y)^{1/3}+(c_QA_Q)^{1/3}}.
}
\]

This is the central P43 allocation theorem.

The cube-root dependence matters. If one modality becomes eight times more expensive after all statistical coefficients are included, its optimal share of the uncertainty budget changes by a factor of two at the ratio level, not by a factor of eight.

---

## 5. P43B: exact minimum continuous cost

Let

\[
s=a^{1/3}+b^{1/3}.
\]

At the optimizer,

\[
\lambda_*=\frac{a^{1/3}}{s},
\qquad
1-\lambda_*=\frac{b^{1/3}}{s}.
\]

Therefore

\[
\begin{aligned}
C(\lambda_*)
&=
\frac{a}{a^{2/3}/s^2}
+
\frac{b}{b^{2/3}/s^2}\\
&=
(a^{1/3}+b^{1/3})s^2.
\end{aligned}
\]

Thus

\[
\boxed{
C_*
=
\left[
(c_YA_Y)^{1/3}
+
(c_QA_Q)^{1/3}
\right]^3.
}
\]

This is the exact continuous optimum for the declared P42 weighted cost.

---

## 6. Integer sample sizes and rounding overhead

Experiments use integer sample counts. Define

\[
\boxed{
N_Y
=
\left\lceil\frac{A_Y}{\lambda_*^2}\right\rceil,
\qquad
N_Q
=
\left\lceil\frac{A_Q}{(1-\lambda_*)^2}\right\rceil.
}
\]

These remain sufficient for the P42 finite-sample certificate because rounding is upward.

The integer weighted cost is

\[
C_{\mathrm{int}}
=c_YN_Y+c_QN_Q.
\]

Using \(\lceil z\rceil\le z+1\),

\[
\boxed{
C_*
\le
C_{\mathrm{int}}
\le
C_*+c_Y+c_Q.
}
\]

Thus conversion from the exact continuous optimum to sufficient integer sample sizes costs at most one additional weighted sample from each modality per preparation.

For all \(K\) preparations, the corresponding total rounding overhead is at most

\[
K(c_Y+c_Q).
\]

---

## 7. Balanced allocation as a controlled baseline

P42 highlighted the convenient choice \(\lambda=1/2\). Its continuous cost is

\[
C_{1/2}=4(a+b).
\]

P43 shows exactly when that choice is optimal:

\[
\boxed{
\lambda_*=\frac12
\iff
a=b
\iff
c_YA_Y=c_QA_Q.
}
\]

So balanced allocation is optimal only when the two weighted statistical burdens match.

It nevertheless has a universal approximation guarantee. Since

\[
(a^{1/3}+b^{1/3})^3
\ge a+b,
\]

we obtain

\[
\boxed{
1
\le
\frac{C_{1/2}}{C_*}
\le4.
}
\]

The upper factor is approached only in an extremely imbalanced limit. P43 replaces this potentially wasteful default with the exact optimum.

---

## 8. Comparative statics

The allocation law has direct experimental interpretation.

If \(c_YA_Y\) increases while \(c_QA_Q\) is fixed, then \(\lambda_*\) increases. More of the allowable regularity gap is assigned to target uncertainty, which relaxes the target precision requirement and spends relatively more precision on the quantum side.

If \(c_QA_Q\) increases while \(c_YA_Y\) is fixed, then \(\lambda_*\) decreases. More of the gap is assigned to quantum uncertainty, reducing the number of costly quantum repetitions required at the expense of tighter target estimation.

Because

\[
A_Q\propto L^2\kappa_R^2m^2,
\]

poor tomography conditioning, a larger regularity constant, or a larger IC measurement outcome count shifts the optimum toward a larger quantum uncertainty allowance.

Because

\[
A_Y\propto k^2,
\]

a larger target alphabet shifts the optimum toward a larger target uncertainty allowance.

---

## 9. Confidence remains unchanged

P43 changes only how the deterministic P42 uncertainty budget is divided. It does not change the P42 confidence accounting.

If the quantum and target concentration events have failure probabilities \(\alpha_Q\) and \(\alpha_Y\), then the optimized design retains confidence at least

\[
\boxed{
\max\{0,1-\alpha_Q-\alpha_Y\}.
}
\]

No additional post-selection penalty is introduced because \(\lambda_*\) is computed from the declared design parameters before observing the data.

If costs or coefficients are estimated from the same data used for the final obstruction test, that becomes an adaptive-design problem and requires a separate theorem.

---

## 10. Scientific boundary

P43 is an optimization theorem inside the P42 experimental model. It can answer:

> Given this declared quantum measurement, reconstruction stability, target alphabet, regularity class, confidence allocation, population design gap, and sample costs, how should the P42 uncertainty budget be split to minimize sufficient weighted sampling cost?

It cannot answer whether the physical descriptor is complete, whether the Lipschitz bridge class is physically mandatory, whether quantum mechanics is incomplete, or whether the independently defined target is consciousness.

The quantities \(c_Q\) and \(c_Y\) are design weights, not physical observables. A different experimental objective may require a different optimization problem.

---

## 11. Reproducibility

Implementation:
[`optimal_quantum_target_allocation.py`](../src/consciousness_bridge/optimal_quantum_target_allocation.py)

Regression tests:
[`test_optimal_quantum_target_allocation.py`](../tests/test_optimal_quantum_target_allocation.py)

---

## 12. Next theorem target

P43 optimizes the split between quantum and target precision while retaining one common sample count within each modality across all preparations.

The next mathematical burden is preparation-specific allocation. For a collection of candidate preparation pairs, the experiment should distribute samples across individual preparations according to their contribution to the strongest certified obstruction while preserving valid confidence after pair selection. That requires a joint optimization and post-selection theorem rather than an informal adaptive heuristic.
