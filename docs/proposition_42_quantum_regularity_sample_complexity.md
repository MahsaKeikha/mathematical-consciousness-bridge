# Proposition 42: Sample complexity for quantum regularity obstruction

## Status

**Proved conditional sample-complexity theorem.** P42 converts the P41 finite-error design inequality into explicit sufficient sample sizes under declared square-root confidence-radius laws.

The theorem deliberately does not claim a universal quantum tomography concentration rate. The radius constants and logarithmic factors are inputs that must be justified by the actual tomography design, estimator, state dimension, measurement class, and target observation model.

P42 is a planning theorem for one declared model class. It does not establish quantum incompleteness and does not identify the target with consciousness.

---

## 1. Population regularity gap

For one preparation pair, let

\[
d_Y
=
\|P_x-P_{x'}\|_{\mathrm{TV}}
\]

be the population target-law separation and let

\[
d_Q
=
D(\rho_x,\rho_{x'})
\]

be the population quantum trace distance.

For an \(L\)-Lipschitz bridge class, define

\[
\boxed{
\Gamma
=
d_Y-Ld_Q.
}
\]

The population pair is incompatible with the declared bridge class only when

\[
\boxed{\Gamma>0.}
\]

If \(\Gamma\le0\), no amount of sampling can make the P41 sufficient inequality positive without changing the model class or the underlying population separation.

---

## 2. Declared finite-sample radius laws

Assume a target confidence analysis provides a simultaneous radius law

\[
\boxed{
\varepsilon_Y(n_Y,\alpha_Y)
=
c_Y
\sqrt{
\frac{\log(A_Y/\alpha_Y)}{n_Y}
},
}
\]

and a quantum tomography analysis provides a simultaneous trace-distance radius law

\[
\boxed{
r_Q(n_Q,\alpha_Q)
=
c_Q
\sqrt{
\frac{\log(A_Q/\alpha_Q)}{n_Q}
}.
}
\]

Here

\[
c_Y,c_Q\ge0,
\qquad
A_Y>\alpha_Y,
\qquad
A_Q>\alpha_Q.
\]

These constants are not universal. They summarize whatever externally validated concentration theorem applies to the chosen experiment.

---

## 3. P41 finite-error requirement

In the symmetric unsaturated regime, P41 gives the sufficient condition

\[
\boxed{
\Gamma
>
2\varepsilon_Y
+2Lr_Q.
}
\]

The two uncertainty sources are logically distinct. Target sampling consumes the term \(2\varepsilon_Y\). Quantum tomography consumes the term \(2Lr_Q\).

---

## 4. Gap allocation

Choose any

\[
\lambda\in(0,1).
\]

Allocate a fraction \(\lambda\) of the population gap to target uncertainty and the remaining fraction to quantum uncertainty:

\[
2\varepsilon_Y
\le
\lambda\Gamma,
\]

\[
2Lr_Q
\le
(1-\lambda)\Gamma.
\]

If both inequalities hold strictly in the observed experiment, then their sum is strictly below \(\Gamma\) and the P41 obstruction is positive.

For sample-size planning, the non-strict allocated inequalities give conservative integer lower bounds. The final observed certificate must still verify a positive P41 margin rather than treating equality at the planning boundary as evidence.

---

## 5. P42A: target sample complexity

Substituting the declared target radius gives

\[
2c_Y
\sqrt{
\frac{\log(A_Y/\alpha_Y)}{n_Y}
}
\le
\lambda\Gamma.
\]

Squaring and solving for \(n_Y\) yields

\[
\boxed{
n_Y
\ge
\frac{4c_Y^2}{\lambda^2\Gamma^2}
\log\left(\frac{A_Y}{\alpha_Y}\right).
}
\]

Thus target sample complexity scales as

\[
\boxed{n_Y=O(\Gamma^{-2})}
\]

for fixed confidence and radius-law constants.

---

## 6. P42B: quantum sample complexity

Likewise,

\[
2Lc_Q
\sqrt{
\frac{\log(A_Q/\alpha_Q)}{n_Q}
}
\le
(1-\lambda)\Gamma
\]

implies

\[
\boxed{
n_Q
\ge
\frac{4L^2c_Q^2}{(1-\lambda)^2\Gamma^2}
\log\left(\frac{A_Q}{\alpha_Q}\right).
}
\]

For fixed confidence and tomography constants,

\[
\boxed{n_Q=O(L^2\Gamma^{-2}).}
\]

The \(L^2\) factor is not a property of quantum mechanics. It appears because a more rapidly varying allowed bridge converts a given quantum-state uncertainty into a larger allowable target variation.

---

## 7. Joint sufficient sample theorem

### Proposition 42

Assume:

1. \(\Gamma=d_Y-Ld_Q>0\);
2. the target and quantum analyses have the declared simultaneous square-root radius laws;
3. the P41 trace-ball envelope remains in the unsaturated regime for the preparation pair;
4. the bridge class is declared \(L\)-Lipschitz.

Choose \(\lambda\in(0,1)\). If

\[
\boxed{
n_Y
\ge
\frac{4c_Y^2}{\lambda^2\Gamma^2}
\log\left(\frac{A_Y}{\alpha_Y}\right)}
\]

and

\[
\boxed{
n_Q
\ge
\frac{4L^2c_Q^2}{(1-\lambda)^2\Gamma^2}
\log\left(\frac{A_Q}{\alpha_Q}\right),}
\]

then the allocated P41 uncertainty budget is at most \(\Gamma\).

Any observed strict improvement over the planning boundary yields a positive P41 regularity obstruction on the joint confidence event.

The joint confidence lower bound is inherited from P41:

\[
\boxed{
\max\{0,1-\alpha_Q-\alpha_Y\}.
}
\]

---

## 8. Confidence cost

The sample sizes depend logarithmically on inverse failure probability:

\[
n_Y
\propto
\log(A_Y/\alpha_Y),
\qquad
n_Q
\propto
\log(A_Q/\alpha_Q).
\]

Therefore making the confidence requirement stricter increases the sufficient sample count, but only logarithmically under the declared square-root radius laws.

This statement is conditional on those radius laws. Different tomography or target concentration results can produce different dependence.

---

## 9. P42C: cost-aware optimal gap allocation

The choice \(\lambda=1/2\) is simple but need not minimize experimental cost.

Let one target sample have cost \(w_Y>0\) and one quantum sample have cost \(w_Q>0\). Ignoring integer ceilings and the common factor \(4/\Gamma^2\), the weighted sufficient-sample objective has the form

\[
\mathcal C(\lambda)
=
\frac{a}{\lambda^2}
+
\frac{b}{(1-\lambda)^2},
\]

where

\[
a
=
w_Yc_Y^2
\log(A_Y/\alpha_Y),
\]

\[
b
=
w_QL^2c_Q^2
\log(A_Q/\alpha_Q).
\]

For \(a,b>0\), differentiation gives the unique interior optimum

\[
\boxed{
\lambda_*
=
\frac{a^{1/3}}{a^{1/3}+b^{1/3}}.
}
\]

### Proof

Differentiate:

\[
\mathcal C'(\lambda)
=
-\frac{2a}{\lambda^3}
+
\frac{2b}{(1-\lambda)^3}.
\]

Setting \(\mathcal C'(\lambda)=0\) gives

\[
\frac{\lambda}{1-\lambda}
=
\left(\frac{a}{b}\right)^{1/3},
\]

which yields the stated formula. The objective diverges at both endpoints and is strictly convex on \((0,1)\), so the stationary point is the unique minimum. \(\square\)

This allocation gives more uncertainty budget to the experimentally expensive side, reducing the sample count required there while forcing the cheaper side to be estimated more precisely.

---

## 10. Equal-cost symmetric case

If

\[
w_Y=w_Q,
\qquad
c_Y=Lc_Q,
\qquad
\log(A_Y/\alpha_Y)
=
\log(A_Q/\alpha_Q),
\]

then

\[
a=b
\]

and

\[
\boxed{\lambda_*=1/2.}
\]

Thus equal gap splitting is optimal only under a corresponding symmetry of statistical difficulty and sampling cost.

---

## 11. What P42 does not supply

P42 does not supply a universal value of \(c_Q\) or \(A_Q\). Quantum tomography rates depend on details such as Hilbert-space dimension, measurement design, state rank assumptions, estimator, and the norm in which coverage is proved.

Similarly, \(c_Y\) and \(A_Y\) depend on the target observation model and the form of the simultaneous confidence guarantee.

Consequently,

\[
\boxed{
\text{P42 algebra}
+
\text{unjustified radius constants}
\neq
\text{valid sample-complexity certificate}.
}
\]

The theorem becomes experimentally meaningful only after those ingredients are sourced or proved for the actual protocol.

---

## 12. Scientific boundary

Even with valid concentration radii and a positive P41 obstruction, the conclusion remains

\[
\boxed{
\text{declared quantum confidence region}
+
\text{declared regular bridge class}
\text{ are incompatible with the target data}.
}
\]

It does not establish that quantum mechanics is incomplete. It does not establish that a larger system or environment cannot explain the target. It does not establish that the regularity class is physically mandatory. It does not establish that the target is consciousness.

---

## 13. Next theorem target

P42 isolates exactly where experiment-specific quantum statistics must enter. A natural next step is to instantiate the abstract radius law for a precisely declared tomography protocol, beginning with a finite-dimensional informationally complete measurement model where a finite-alphabet concentration theorem can be proved transparently from measurement frequencies to a reconstruction norm.

That theorem should state every dimension and conditioning constant explicitly rather than hiding them inside a generic tomography rate.

---

## 14. Reproducibility

Implementation:
[`quantum_regularity_sample_complexity.py`](../src/consciousness_bridge/quantum_regularity_sample_complexity.py)

Regression tests:
[`test_quantum_regularity_sample_complexity.py`](../tests/test_quantum_regularity_sample_complexity.py)
