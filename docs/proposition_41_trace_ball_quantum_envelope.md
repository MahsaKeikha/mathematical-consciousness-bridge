# Proposition 41: Trace-ball quantum envelopes and end-to-end regularity certification

## Status

**Proved confidence-region envelope theorem and end-to-end Lipschitz obstruction.** P41 makes the continuous-region P40 certificate directly computable when quantum tomography supplies simultaneous trace-distance balls around estimated density operators and target estimation supplies simultaneous total-variation balls.

The theorem is intentionally geometric. It does not prescribe a particular tomography estimator or claim that a chosen trace-ball radius is valid. Coverage of those balls is an explicit statistical premise.

P41 does not establish that quantum mechanics is incomplete and does not identify the target with consciousness.

---

## 1. Setup

Let \(\mathcal X\) be a finite preparation set. For every preparation \(x\), let

\[
\rho_x
\]

be the true declared quantum state and let

\[
\widehat\rho_x
\]

be an estimated state.

Assume a simultaneous quantum confidence event

\[
\boxed{
D(\rho_x,\widehat\rho_x)\le r_x
\quad\forall x\in\mathcal X
}
\]

with probability at least

\[
1-\alpha_Q.
\]

Here

\[
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1
\]

is quantum trace distance.

For independently defined target distributions \(P_x\), let \(\widehat P_x\) be the corresponding estimates and assume

\[
\boxed{
\|P_x-\widehat P_x\|_{\mathrm{TV}}\le\varepsilon_x
\quad\forall x\in\mathcal X
}
\]

with probability at least

\[
1-\alpha_Y.
\]

---

## 2. P41A: trace-ball pairwise quantum envelope

For any two preparations \(x,x'\), trace-distance triangle inequality gives

\[
D(\rho_x,\rho_{x'})
\le
D(\rho_x,\widehat\rho_x)
+
D(\widehat\rho_x,\widehat\rho_{x'})
+
D(\widehat\rho_{x'},\rho_{x'}).
\]

On the simultaneous quantum confidence event,

\[
D(\rho_x,\rho_{x'})
\le
D(\widehat\rho_x,\widehat\rho_{x'})
+r_x+r_{x'}.
\]

Because trace distance between density operators is at most one,

\[
\boxed{
D(\rho_x,\rho_{x'})
\le
U^{\mathrm{ball}}_{xx'}
:=
\min\left\{
1,
D(\widehat\rho_x,\widehat\rho_{x'})+r_x+r_{x'}
\right\}.
}
\]

### Interpretation

The bound is an outer envelope for every pair of true states compatible with the declared trace balls. It is not a point estimate and it does not assert that the upper bound is achieved.

---

## 3. Relation to the P40 continuous-region envelope

Let the P40 confidence region be the Cartesian intersection of the declared per-preparation trace balls,

\[
\mathcal C_Q^{\mathrm{ball}}
=
\left\{
Q:
D(\rho_x^Q,\widehat\rho_x)\le r_x
\ \forall x
\right\}.
\]

P40 defines

\[
U_{xx'}
=
\sup_{Q\in\mathcal C_Q^{\mathrm{ball}}}
D(\rho_x^Q,\rho_{x'}^Q).
\]

P41A immediately implies

\[
\boxed{
U_{xx'}
\le
U^{\mathrm{ball}}_{xx'}.
}
\]

Thus the exact region supremum need not be solved in order to obtain a sound P40 certificate. The trace-ball expression is a conservative analytically available upper bound.

---

## 4. P41B: target-law lower envelope

Target total variation obeys the reverse triangle inequality in the same way. On the simultaneous target-confidence event,

\[
\begin{aligned}
\|P_x-P_{x'}\|_{\mathrm{TV}}
&\ge
\|\widehat P_x-\widehat P_{x'}\|_{\mathrm{TV}}\\
&\quad-
\|P_x-\widehat P_x\|_{\mathrm{TV}}
-
\|P_{x'}-\widehat P_{x'}\|_{\mathrm{TV}}.
\end{aligned}
\]

Hence

\[
\boxed{
\|P_x-P_{x'}\|_{\mathrm{TV}}
\ge
L^{\mathrm{ball}}_{xx'}
:=
\left[
\|\widehat P_x-\widehat P_{x'}\|_{\mathrm{TV}}
-\varepsilon_x-\varepsilon_{x\'}
\right]_+.
}
\]

---

## 5. P41C: end-to-end modulus obstruction

Let the declared bridge class satisfy the P40 regularity condition

\[
\|g(\rho)-g(\sigma)\|_{\mathrm{TV}}
\le
\omega(D(\rho,\sigma)),
\]

where \(\omega\) is nondecreasing and \(\omega(0)=0\).

For any descriptor in the trace-ball confidence region,

\[
D(\rho_x,
ho_{x'})
\le
U^{\mathrm{ball}}_{xx'}.
\]

Therefore every bridge in the declared regularity class would require

\[
\|P_x-P_{x'}\|_{\mathrm{TV}}
\le
\omega(U^{\mathrm{ball}}_{xx'}).
\]

Combining this with P41B gives the sufficient obstruction condition

\[
\boxed{
L^{\mathrm{ball}}_{xx'}
>
\omega(U^{\mathrm{ball}}_{xx'}).
}
\]

If this inequality holds for any preparation pair, then no quantum descriptor inside the declared trace-ball region supports a bridge in the declared regularity class that reproduces the true target laws on the joint confidence event.

---

## 6. Lipschitz corollary

For an \(L\)-Lipschitz bridge,

\[
\omega(r)=Lr.
\]

Define the pairwise certified margin

\[
\boxed{
M^{\mathrm{ball}}_{xx'}
=
L^{\mathrm{ball}}_{xx'}
-
L U^{\mathrm{ball}}_{xx'}.
}
\]

Then

\[
\boxed{
M^{\mathrm{ball}}_{xx'}>0
}
\]

is sufficient to rule out the declared \(L\)-Lipschitz bridge class throughout the complete trace-ball quantum confidence region.

Across all pairs define

\[
\boxed{
M^{\mathrm{ball}}_*
=
\max_{x\ne x'}M^{\mathrm{ball}}_{xx'}.
}
\]

Thus

\[
\boxed{
M^{\mathrm{ball}}_*>0
}
\]

is the global P41 end-to-end obstruction certificate.

---

## 7. Confidence statement

Let \(A_Q\) be the simultaneous quantum trace-ball event and \(A_Y\) the simultaneous target-TV event. If

\[
\Pr(A_Q)\ge1-\alpha_Q,
\qquad
\Pr(A_Y)\ge1-\alpha_Y,
\]

then the union bound gives

\[
\boxed{
\Pr(A_Q\cap A_Y)
\ge
1-\alpha_Q-\alpha_Y.
}
\]

Therefore a positive P41 global obstruction margin is valid with confidence at least

\[
\boxed{
\max\{0,1-\alpha_Q-\alpha_Y\}.
}
\]

No independence assumption is required for this coverage statement.

---

## 8. Radius sensitivity

The theorem makes the cost of uncertainty transparent. For one pair,

\[
U^{\mathrm{ball}}_{xx'}
=
\min\{1,\widehat D^Q_{xx'}+r_x+r_{x'}\},
\]

while

\[
L^{\mathrm{ball}}_{xx'}
=
[\widehat D^Y_{xx'}-\varepsilon_x-\varepsilon_{x'}]_+.
\]

For the unsaturated Lipschitz regime,

\[
\widehat D^Q_{xx'}+r_x+r_{x'}<1,
\]

the obstruction margin becomes

\[
\boxed{
M^{\mathrm{ball}}_{xx'}
=
[\widehat D^Y_{xx'}-\varepsilon_x-\varepsilon_{x'}]_+
-L(\widehat D^Q_{xx'}+r_x+r_{x'}).
}
\]

Quantum uncertainty reduces the margin through \(L(r_x+r_{x'})\). Target uncertainty reduces it through \(\varepsilon_x+\varepsilon_{x'}\).

This decomposition directly identifies which experiment needs more precision.

---

## 9. A deterministic sufficient design inequality

Suppose a planned experiment has anticipated population separations

\[
d_Y=\|P_x-P_{x'}\|_{\mathrm{TV}},
\qquad
d_Q=D(\rho_x,\rho_{x'}),
\]

and symmetric error budgets

\[
r_x,r_{x'}\le r,
\qquad
\varepsilon_x,\varepsilon_{x'}\le\varepsilon.
\]

A conservative sufficient condition for a positive \(L\)-Lipschitz obstruction is

\[
\boxed{
d_Y-2\varepsilon>L(d_Q+2r),}
\]

provided the quantum upper envelope does not saturate at one.

Equivalently,

\[
\boxed{
d_Y-Ld_Q>2\varepsilon+2Lr.}
\]

The left side is the population regularity gap. The right side is the combined uncertainty budget.

This is the point from which an explicit sample-complexity theorem can be derived once concrete rates for \(r\) and \(\varepsilon\) are declared.

---

## 10. Scientific boundary

P41 can establish only

\[
\boxed{
\text{no bridge in the declared regularity class fits any quantum descriptor inside the declared trace-ball confidence region}.
}
\]

It does not establish that no richer quantum descriptor exists. It does not establish that the system boundary is complete. It does not establish that the bridge regularity class is physically mandatory. It does not establish that the target is consciousness.

The result should therefore be interpreted as a rigorous falsification certificate for one explicit model class, not as an ontological conclusion.

---

## 11. Next theorem target

P41 isolates the remaining statistical ingredient. To obtain a true sample-complexity theorem, one needs explicit finite-sample radii of the form

\[
r_x=r_x(n_Q,\alpha_Q,d,\mathcal M),
\qquad
\varepsilon_x=\varepsilon_x(n_Y,\alpha_Y,|\mathcal Y|),
\]

for the chosen tomography design and target observation model.

The next theorem should substitute valid concentration radii into

\[
d_Y-Ld_Q>2\varepsilon+2Lr
\]

and solve for sufficient quantum and target sample sizes.

---

## 12. Reproducibility

Implementation:
[`trace_ball_quantum_envelope.py`](../src/consciousness_bridge/trace_ball_quantum_envelope.py)

Regression tests:
[`test_trace_ball_quantum_envelope.py`](../tests/test_trace_ball_quantum_envelope.py)
