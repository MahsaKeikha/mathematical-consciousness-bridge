# Proposition 39: Finite-data quantum model-set non-factorization certification

## Status

**Proved finite-data model-set theorem.** P39 converts the exact P38 quantum
factorization criterion into a confidence statement that remains valid when the
quantum operational description and the independently defined target are both
uncertain.

The theorem is deliberately relative to a declared finite quantum hypothesis
class and a tomography-derived confidence set. It does not claim that finite noisy
tomography can prove exact equality of arbitrary density operators. It does not
claim that quantum mechanics is incomplete, and it does not identify the target
with consciousness.

---

## 1. Why the P38 exact collision is not directly a finite-data test

P38 gives the exact deterministic obstruction

\[
\rho_x=\rho_{x'}
\quad\text{but}\quad
y(x)\neq y(x').
\]

For stochastic targets it gives the fiberwise condition

\[
\rho_x=\rho_{x'}
\Longrightarrow
P(Y\mid x)=P(Y\mid x').
\]

In a finite experiment, however, density operators are inferred from noisy
measurement frequencies. A small estimated trace distance is not a theorem of
exact state equality.

For example, for any \(0<\delta<1/2\), the qubit states

\[
\rho_0=
\begin{pmatrix}
1/2&0\\
0&1/2
\end{pmatrix},
\qquad
\rho_\delta=
\begin{pmatrix}
1/2+\delta&0\\
0&1/2-\delta
\end{pmatrix}
\]

satisfy

\[
D(\rho_0,\rho_\delta)=\delta
\]

but

\[
\rho_0\neq\rho_\delta.
\]

Since \(\delta\) can be arbitrarily small,

\[
\boxed{
\text{small state-estimation distance}
\not\Rightarrow
\text{exact quantum-state equality}.
}
\]

P39 therefore does not threshold a continuous tomography estimate and call the
result an exact P38 collision.

---

## 2. Declared finite quantum hypothesis class

Let \(\mathcal X\) be a finite preparation set and let

\[
\mathfrak H_Q
=\{h_1,\ldots,h_K\}
\]

be a declared finite family of quantum operational hypotheses.

Each hypothesis \(h\) contains an exact operational-state labeling

\[
q_h:\mathcal X\to\mathcal Q_h.
\]

The equality

\[
q_h(x)=q_h(x')
\]

means that hypothesis \(h\) asserts exact equality of the declared quantum
operational state for those two preparations. Such equality may arise from a
physical symmetry, a constrained preparation model, a discrete model family, or
another independently justified model restriction. It must not be manufactured
by declaring two noisy estimates "close enough."

Let the tomography analysis return a random confidence set

\[
\mathcal C_Q\subseteq\mathfrak H_Q
\]

such that, for the true declared hypothesis \(h_*\),

\[
\boxed{
\Pr(h_*\in\mathcal C_Q)\ge1-\alpha_Q.
}
\]

P39 takes this coverage property as an explicit input. It does not prescribe one
particular tomography procedure.

---

## 3. Independent target uncertainty

For every preparation \(x\), let the true target law be \(P_x\), and let
\(\widehat P_x\) be its empirical or estimated distribution.

Assume simultaneous total-variation radii \(\varepsilon_x\) satisfy

\[
\boxed{
\Pr\left(
\|P_x-\widehat P_x\|_{\mathrm{TV}}
\le\varepsilon_x
\quad\forall x\in\mathcal X
\right)
\ge1-\alpha_Y.
}
\]

The target analysis is independent in definition from the quantum state labels.
Statistical independence of the two data sets is not required for the union-bound
argument below.

---

## 4. Pairwise target-separation lower bound

For preparations \(x,x'\), define

\[
\boxed{
L_{xx'}
=
\left[
\|\widehat P_x-\widehat P_{x'}\|_{\mathrm{TV}}
-\varepsilon_x-\varepsilon_{x'}
\right]_+.
}
\]

On the simultaneous target-confidence event, the triangle inequality gives

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

Therefore

\[
\boxed{
\|P_x-P_{x'}\|_{\mathrm{TV}}
\ge L_{xx'}.
}
\]

A positive \(L_{xx'}\) certifies that the true target laws differ.

---

## 5. Model-specific P38 violation margin

For quantum hypothesis \(h\), define

\[
\boxed{
V(h)
=
\max_{\substack{x,x'\in\mathcal X\\q_h(x)=q_h(x')}}
L_{xx'},
}
\]

with \(V(h)=0\) when the hypothesis contains no distinct same-state preparation
pair.

### Proposition 39A

On the simultaneous target-confidence event,

\[
\boxed{
V(h)>0
\Longrightarrow
h\text{ violates the P38 stochastic factorization criterion}.
}
\]

### Proof

If \(V(h)>0\), there exists a pair \(x,x'\) with

\[
q_h(x)=q_h(x')
\]

and

\[
L_{xx'}>0.
\]

The target-confidence event implies

\[
\|P_x-P_{x'}\|_{\mathrm{TV}}>0,
\]

so the target laws differ. Hypothesis \(h\) therefore assigns the same declared
quantum operational state to two preparations with different target laws. This is
exactly the stochastic P38 non-factorization witness for that hypothesis.
\(\square\)

---

## 6. Robust confidence-set theorem

Define the robust model-set margin

\[
\boxed{
V_*
=
\min_{h\in\mathcal C_Q}V(h).
}
\]

### Proposition 39B

If

\[
\boxed{V_*>0,}
\]

then, with probability at least

\[
\boxed{1-\alpha_Q-\alpha_Y,}
\]

the true declared quantum operational hypothesis fails the P38 stochastic
factorization criterion.

### Proof

Let \(A_Q\) be the event \(h_*\in\mathcal C_Q\), and let \(A_Y\) be the
simultaneous target-confidence event. By the union bound,

\[
\Pr(A_Q\cap A_Y)
\ge1-\alpha_Q-\alpha_Y.
\]

On \(A_Q\), the true hypothesis belongs to \(\mathcal C_Q\). If \(V_*>0\),
then every hypothesis in \(\mathcal C_Q\), including \(h_*\), has positive
model-specific violation margin. On \(A_Y\), Proposition 39A converts that positive
margin into a true same-state, different-target-law witness. Hence \(h_*\) fails
P38 factorization on \(A_Q\cap A_Y\). \(\square\)

If \(\alpha_Q+\alpha_Y>1\), the elementary union-bound lower confidence is clipped
at zero and is scientifically uninformative.

---

## 7. Why one injective model blocks the certificate

Suppose \(h\in\mathcal C_Q\) assigns a distinct state label to every preparation:

\[
q_h(x)\neq q_h(x')
\quad\forall x\neq x'.
\]

Then no P38 same-state collision is available and

\[
V(h)=0.
\]

Therefore

\[
V_*=0.
\]

This is not a weakness of the theorem. It exposes the exact scientific burden.
If the physically admissible confidence set still contains a model in which every
preparation has a distinct quantum operational state, finite target differences
alone do not refute quantum-state factorization.

The experiment must either constrain that model physically or move to a different
non-factorization statistic whose assumptions are explicit.

---

## 8. Relation to trace distance and tomography

For any quantum states \(\rho,\sigma\) and any POVM measurement \(M\), quantum
data processing gives

\[
\|p_M^\rho-p_M^\sigma\|_{\mathrm{TV}}
\le
D(\rho,\sigma),
\]

where

\[
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
\]

This makes trace-distance confidence regions a natural ingredient for constructing
\(\mathcal C_Q\). P39 nevertheless keeps the confidence-set construction external
because a valid method depends on the measurement design, state dimension,
preparation constraints, sampling model, and tomography estimator.

Most importantly, an overlap of two trace-distance confidence balls does not prove
that their true states are equal. It only means equality has not been excluded by
those regions.

---

## 9. Scientific boundary

P39 can establish only the following type of conclusion:

\[
\boxed{
\text{all quantum operational hypotheses in the declared confidence set}
\text{ fail target factorization}.
}
\]

It does not establish

\[
\text{quantum mechanics is incomplete},
\]

nor

\[
\text{the target is nonphysical}.
\]

A positive P39 certificate can still reflect an inadequately broad hypothesis
class, an incorrect system boundary, omitted environment degrees of freedom,
misspecified preparations, insufficient interventions, target-measurement error,
nonstationarity, or an invalid tomography coverage guarantee.

For a consciousness application, the target must additionally be independently
and operationally justified as experiential structure rather than constructed from
the same physical variables being tested.

---

## 10. What P39 adds beyond P38

P38 states an exact population factorization criterion. P39 adds three finite-data
protections:

1. exact quantum-state equality must come from a declared model hypothesis, not a
   numerical closeness threshold;
2. target differences are reduced by simultaneous total-variation uncertainty
   before they count as violations;
3. non-factorization must hold for every quantum hypothesis surviving tomography,
   not only for a selected convenient model.

The resulting logic is

\[
\boxed{
\text{tomography confidence set}
+
\text{simultaneous target confidence}
+
V_*>0
\Longrightarrow
\text{descriptor-relative P38 non-factorization}
}
\]

with confidence at least \(1-\alpha_Q-\alpha_Y\).

---

## 11. Next theorem target

P39 still assumes a finite hypothesis family whose members encode exact operational
state equalities. The next theorem burden is to move from a finite model set to a
continuous quantum confidence region without pretending that confidence-region
overlap establishes exact state equality.

A natural route is a **robust quantum sufficiency residual** that minimizes an
appropriate target-factorization discrepancy over every physically admissible
quantum descriptor in a continuous confidence region. A positive infimum would
rule out the whole region without requiring any exact equality test between noisy
state estimates.

---

## 12. Reproducibility

Implementation:
[`finite_data_quantum_nonfactorization.py`](../src/consciousness_bridge/finite_data_quantum_nonfactorization.py)

Regression tests:
[`test_finite_data_quantum_nonfactorization.py`](../tests/test_finite_data_quantum_nonfactorization.py)
