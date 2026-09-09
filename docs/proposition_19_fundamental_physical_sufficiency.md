# Proposition 19 — Fundamental Physical Sufficiency and Residual Tests

## Status

**Proved mathematical theorem for a declared physical descriptor.**

This proposition does **not** prove that consciousness is nonphysical, fundamental, quantum, or an additional spacetime dimension. It states exact mathematical conditions under which an independently defined target structure can or cannot be reconstructed from a declared physical description.

---

# 1. Setup

Let

\[
\Omega\in\mathcal M
\]

denote a state in a declared candidate fundamental state space. Let

\[
T:\mathcal M\to\mathcal Q_T
\]

be the declared physical descriptor. In the present research program it may collect geometric, quantum-operational, and intervention-resolved causal information,

\[
T(\Omega)=\bigl(G(\Omega),Q(\Omega),C(\Omega)\bigr),
\]

but Proposition 19 does not depend on that particular decomposition.

Let

\[
E:\mathcal M\to\mathcal Q_E
\]

be an independently defined target descriptor. When the target is experiential, \(\mathcal Q_E\) must be specified independently of \(T\); otherwise the bridge becomes definitional rather than explanatory.

The physical-sufficiency question is whether there exists a map

\[
B_T:\operatorname{Im}(T)\to\mathcal Q_E
\]

such that

\[
\boxed{E=B_T\circ T.}
\]

---

# 2. P19A — exact factorization theorem

## Proposition

There exists a unique map

\[
B_T:\operatorname{Im}(T)\to\mathcal Q_E
\]

satisfying \(E=B_T\circ T\) if and only if \(E\) is constant on every fiber of \(T\):

\[
\boxed{
T(\Omega)=T(\Omega')
\Longrightarrow
E(\Omega)=E(\Omega').
}
\]

Equivalently, with kernel equivalence relations induced by the two maps,

\[
\boxed{
\ker T\subseteq\ker E.
}
\]

## Proof

If \(E=B_T\circ T\), then

\[
T(\Omega)=T(\Omega')
\]

implies

\[
E(\Omega)
=B_T(T(\Omega))
=B_T(T(\Omega'))
=E(\Omega').
\]

Conversely, suppose \(E\) is constant on every fiber of \(T\). For \(t\in\operatorname{Im}(T)\), choose any \(\Omega\) with \(T(\Omega)=t\) and define

\[
B_T(t)=E(\Omega).
\]

Fiber constancy makes this definition independent of the representative. Therefore \(B_T\) is well defined and \(E=B_T\circ T\). Uniqueness on \(\operatorname{Im}(T)\) follows because every \(t\) in that image has at least one preimage. \(\square\)

---

# 3. P19B — exact no-factorization witness

A single exact collision

\[
\boxed{
T(\Omega)=T(\Omega')
\quad\text{and}\quad
E(\Omega)\ne E(\Omega')
}
\]

is sufficient to rule out every deterministic bridge through that declared physical descriptor:

\[
\boxed{
\nexists B_T
\text{ such that }
E=B_T\circ T.
}
\]

This is an exact logical no-go result relative to the declared \(T\).

It does **not** establish that no richer physical descriptor exists. A collision may instead reveal omitted physical variables, inadequate temporal resolution, an incorrect system boundary, an incomplete intervention class, measurement error, or a poorly defined target variable.

---

# 4. P19C — stochastic physical sufficiency

A deterministic bridge may be unnecessarily restrictive. Let \((\Omega,T,E)\) be random variables with a finite joint law. Physical sufficiency in the stochastic case means that the conditional distribution of \(E\) depends on the underlying state only through \(T\):

\[
\boxed{
P(E\in A\mid\Omega,T)
=P(E\in A\mid T)
}
\]

for every measurable target event \(A\), almost surely.

Equivalently,

\[
\boxed{
E\perp\!\!\!\perp\Omega\mid T.
}
\]

For finite alphabets this is equivalent to

\[
\boxed{
I(E;\Omega\mid T)=0.
}
\]

Thus define the **fundamental conditional-information residual**

\[
\boxed{
\mathcal I_{\perp}^{\mathrm{fund}}
:=I(E;\Omega\mid T).
}
\]

By non-negativity of conditional mutual information,

\[
\mathcal I_{\perp}^{\mathrm{fund}}\ge0.
\]

A strictly positive population value rules out the conditional-independence model associated with that declared physical descriptor.

## Proof of the equivalence in the finite case

Conditional mutual information can be written as

\[
I(E;\Omega\mid T)
=
\sum_t P(t)
D_{\mathrm{KL}}
\left(
P_{E,\Omega\mid t}
\middle\|
P_{E\mid t}P_{\Omega\mid t}
\right).
\]

Every term is non-negative. The sum is zero if and only if every positive-mass conditional joint law factorizes,

\[
P_{E,\Omega\mid t}
=P_{E\mid t}P_{\Omega\mid t},
\]

which is exactly conditional independence. \(\square\)

---

# 5. Deterministic-target corollary

If both \(T=T(\Omega)\) and \(E=E(\Omega)\) are deterministic functions of \(\Omega\), then

\[
H(E\mid\Omega,T)=0,
\]

so

\[
\boxed{
I(E;\Omega\mid T)=H(E\mid T).
}
\]

Therefore, in the finite deterministic setting,

\[
\boxed{
I(E;\Omega\mid T)=0
\iff
E\text{ is a function of }T
\quad\text{almost surely}.
}
\]

The deterministic fiber theorem and the information-theoretic criterion are therefore two views of the same sufficiency problem.

---

# 6. P19D — differential no-go criterion

Suppose \(\mathcal M\), \(\mathcal Q_T\), and \(\mathcal Q_E\) are smooth manifolds in a neighborhood of \(\Omega_0\), and \(T\) and \(E\) are differentiable there.

If there exists a differentiable local factorization

\[
E=B_T\circ T,
\]

then by the chain rule

\[
DE_{\Omega_0}
=DB_{T(\Omega_0)}\,DT_{\Omega_0}.
\]

Consequently the row space contributed by \(DE\) is contained in that already available from \(DT\), and hence

\[
\boxed{
\operatorname{rank}D(T,E)_{\Omega_0}
=
\operatorname{rank}DT_{\Omega_0}.
}
\]

Define

\[
\boxed{
d_{\perp}(\Omega_0)
=
\operatorname{rank}D(T,E)_{\Omega_0}
-
\operatorname{rank}DT_{\Omega_0}.
}
\]

Then

\[
\boxed{
d_{\perp}(\Omega_0)>0
\Longrightarrow
\text{no differentiable local factorization through }T
\text{ exists at }\Omega_0.
}
\]

The converse is **not** claimed: \(d_{\perp}=0\) is necessary for local smooth factorization but is not sufficient in general.

---

# 7. Scientific interpretation hierarchy

A residual relative to \(T\) has several possible explanations. They should be investigated in the following order:

1. **measurement or estimator error**;
2. **target-variable ambiguity or reporting noise**;
3. **omitted physical variables**;
4. **incorrect system boundary or timescale**;
5. **incomplete intervention or measurement class**;
6. **failure of the chosen physical model family**;
7. only after those controls, a possible need for a genuinely additional primitive.

The theorem therefore supports a disciplined expansion rule:

\[
\boxed{
\text{residual found}
\Longrightarrow
\text{enlarge/test }T
\Longrightarrow
\text{re-estimate residual}.
}
\]

If a candidate variable \(Z\) removes the residual after defining

\[
T'=(T,Z),
\]

then the result is evidence that \(T\) was physically incomplete—not evidence for a nonphysical entity.

---

# 8. Relation to the Theory-of-Everything interface

P19 does not require a completed Theory of Everything. It provides a common test that any candidate fundamental physical theory must face.

If a candidate theory supplies a physical descriptor \(T_{\mathrm{candidate}}\), then the same questions apply:

\[
E=B\circ T_{\mathrm{candidate}}\ ?
\]

and, in the stochastic case,

\[
I(E;\Omega\mid T_{\mathrm{candidate}})=0\ ?
\]

This makes competing fundamental theories comparable by a shared sufficiency criterion rather than by metaphysical preference.

---

# 9. What P19 does not establish

P19 does not show that:

- consciousness has been mathematically defined;
- the current \(T\) is a complete description of physics;
- quantum mechanics is insufficient;
- consciousness is a fifth spatial or spacetime dimension;
- consciousness is a new substance;
- simulation ontology is correct;
- a nonzero empirical estimate of conditional mutual information is automatically a population residual.

The theorem establishes the exact mathematical **form of the sufficiency test**. Scientific conclusions require independently justified experiential variables, physically adequate descriptors, finite-sample certification, and replication.

---

# 10. Computational audit

The implementation is in

`src/consciousness_bridge/fundamental_physical_sufficiency.py`.

The tests cover:

- exact fiber consistency;
- constructive no-factorization collisions;
- unique induced bridge maps on the observed physical image;
- zero conditional information under a Markov-sufficient descriptor;
- a positive residual of \(\log 2\) nats when a constant physical descriptor fails to screen off a binary target;
- restoration of zero residual when the physical descriptor fully distinguishes the underlying states;
- validation of finite probability inputs.

See `tests/test_fundamental_physical_sufficiency.py`.
