# Stochastic Fundamental Bridge and Conditional-Information Test

## Purpose

The deterministic bridge question

\[
E=B_T(T)
\]

is useful but unnecessarily restrictive. Physical measurements are noisy, experiential reports are noisy, and a future formal experiential state may itself require a probabilistic measurement model. A more general bridge should therefore be a **Markov kernel**.

This note turns the fundamental-theory factorization problem into a probabilistic sufficiency and conditional-independence problem that can, in principle, be estimated from finite data.

---

## 1. Fundamental variables

Let

\[
\Omega\sim P_\Omega
\]

be a state sampled from a declared candidate fundamental theory, and let

\[
T=t(\Omega)
\]

be the complete declared physical descriptor. In the current program,

\[
T=(G,Q,C),
\]

with geometric, quantum-operational, and intervention-resolved causal components.

Let \(E\) denote an independently defined experiential variable or equivalence-class coordinate. This variable must not be constructed from \(T\) by definition.

---

## 2. Stochastic bridge kernel

A stochastic physical-to-experiential bridge is a Markov kernel

\[
\boxed{
\kappa_E(de\mid t)
}
\]

such that

\[
\boxed{
P(E\in de\mid\Omega=\omega)
=
\kappa_E(de\mid t(\omega)).
}
\]

The deterministic bridge \(E=B_T(T)\) is recovered as the special case

\[
\kappa_E(de\mid t)=\delta_{B_T(t)}(de).
\]

Thus the stochastic framework strictly contains the deterministic one.

---

## 3. Physical sufficiency as a Markov condition

If the complete physical descriptor \(T\) is sufficient for the experiential variable, then

\[
\boxed{
\Omega\longrightarrow T\longrightarrow E
}
\]

forms a Markov chain. Equivalently,

\[
\boxed{
E\perp\!\!\!\perp\Omega\mid T.
}
\]

Under standard regularity assumptions this is equivalent to

\[
\boxed{
I(E;\Omega\mid T)=0.
}
\]

Define the **fundamental conditional-information residual**

\[
\boxed{
\mathcal I_{\perp}^{\mathrm{fund}}
:=I(E;\Omega\mid T).
}
\]

The reduction hypothesis predicts \(\mathcal I_{\perp}^{\mathrm{fund}}=0\).

A robust positive residual would show that the chosen \(T\) is not sufficient for \(E\). It would not, by itself, show that the missing information is nonphysical: the first scientific interpretation must be that the declared physical descriptor may be incomplete.

---

## 4. Observable omitted-variable test

The fundamental state \(\Omega\) may not be directly observable. Let \(Z=z(\Omega)\) be a candidate coordinate or invariant supplied by a fundamental theory but omitted from the current physical bridge descriptor.

Then test

\[
\boxed{
\mathcal I_{Z\perp T}
:=I(E;Z\mid T).
}
\]

If

\[
\mathcal I_{Z\perp T}>0
\]

with a valid finite-sample lower confidence bound, then \(Z\) contains experiential predictive information not captured by \(T\).

This produces a disciplined discovery loop:

1. identify a residual \(Z\);
2. test whether it survives conditioning on the current complete physical descriptor;
3. if it does, incorporate it into an enriched descriptor \(T'=(T,Z)\);
4. repeat the sufficiency test;
5. stop adding variables when the residual disappears within certified uncertainty, or when a genuine no-factorization witness survives a physically complete theory class.

This prevents an unexplained residual from being prematurely labeled "nonphysical" or "consciousness itself."

---

## 5. Intervention-strengthened criterion

Passive correlation is not enough. For admissible interventions \(u\), define

\[
\boxed{
\mathcal I_{\perp}^{(u)}
=I(E;Z\mid T,do(u)).
}
\]

A candidate residual becomes scientifically more interesting only if it is stable or predictively useful across a declared intervention family rather than appearing under a single observational distribution.

One robust aggregate is

\[
\boxed{
\mathcal I_{\mathrm{rob}}
=
\inf_{u\in\mathcal U_*}
I(E;Z\mid T,do(u)),
}
\]

for a preregistered set \(\mathcal U_*\) of informative interventions. A positive lower confidence bound on \(\mathcal I_{\mathrm{rob}}\) would be much stronger than an ordinary correlation.

---

## 6. Finite-data model comparison

Conditional mutual information is difficult to estimate in high dimensions. A complementary operational test compares predictive bridge models on held-out data.

Let

\[
\widehat\kappa_0(E\mid T)
\]

be the best model from a preregistered bridge class using the current physical descriptor, and let

\[
\widehat\kappa_1(E\mid T,Z)
\]

use an additional candidate fundamental coordinate.

Define held-out log-loss improvement

\[
\boxed{
\Delta\mathcal L
=
\mathbb E_{\mathrm{test}}
\left[
-\log\widehat\kappa_0(E\mid T)
+
\log\widehat\kappa_1(E\mid T,Z)
\right].
}
\]

A reliable positive \(\Delta\mathcal L\), replicated across interventions, subjects, laboratories, and measurement modalities where appropriate, is evidence that \(T\) was not sufficient for the chosen experiential variable.

Cross-fitting, held-out evaluation, preregistration, negative controls, and permutation or conditional-randomization tests are required to limit overfitting and post-hoc discovery.

---

## 7. Relation to the deterministic rank residual

The deterministic local rank criterion

\[
d_{\mathrm{TOE}}^{\perp}
=
\operatorname{rank}D(\Psi_T,\Psi_E)
-
\operatorname{rank}D\Psi_T
\]

and the stochastic information criterion

\[
\mathcal I_{\perp}^{\mathrm{fund}}
=I(E;\Omega\mid T)
\]

probe the same broad question from different mathematical directions.

- The **rank residual** detects a local smooth degree of freedom that cannot be generated by the declared physical coordinates.
- The **conditional-information residual** detects predictive information about \(E\) left outside the declared physical descriptor.

Agreement between both criteria on carefully controlled systems would be much stronger than either criterion alone.

---

## 8. Connection to the existing P1-P18 chain

This test inherits the repository's existing scientific safeguards:

- **P1:** representation invariance;
- **P5-P7:** feature sufficiency, completeness, and recoverability;
- **P8-P9:** finite-error and sample-complexity control;
- **P11-P13:** rich intervention-resolved structure and compression no-go tests;
- **P14-P15:** temporal continuation and uncertainty;
- **P16:** composition and coupling;
- **P17-P18:** coarse-graining loss and scale sufficiency.

A future bridge result must satisfy all of these simultaneously, not only achieve high predictive accuracy.

---

## 9. Falsification hierarchy

A positive residual must be challenged in this order:

1. **measurement failure** - is \(E\) unreliable or circularly defined?
2. **representation failure** - does the result disappear under equivalent coordinates?
3. **omitted physical variable** - does an enriched physical descriptor absorb the residual?
4. **scale failure** - was relevant information destroyed by coarse-graining?
5. **temporal failure** - was the alignment between physical and experiential states wrong?
6. **intervention failure** - does the residual disappear under controlled perturbation?
7. **generalization failure** - does it fail out of sample or across laboratories?
8. **bridge-class failure** - was the allowed mapping class too restrictive?

Only after surviving those tests should a residual be considered evidence of a deeper structural problem for the declared physical bridge.

---

## Scientific boundary

Neither

\[
d_{\mathrm{TOE}}^{\perp}>0
\]

nor

\[
I(E;\Omega\mid T)>0
\]

would automatically prove that consciousness is nonphysical, fundamental, quantum, gravitational, simulated, or an additional spacetime dimension. Both are **diagnostics of insufficiency or non-factorization relative to a declared model**. Their scientific value is precisely that they force increasingly complete physical explanations before any stronger ontology is entertained.