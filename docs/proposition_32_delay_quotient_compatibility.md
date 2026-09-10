# Proposition 32 - delay-quotient compatibility

## Status

**Proved operational quotient theorem.** P32 concerns the declared intervention-delay response family used by the P11 physical candidate signature. It does not identify a consciousness measure, establish physical completeness, or equate distinct physical times.

---

## 1. Problem

P31 establishes when a many-to-one map on intervention labels preserves a unique response law. The remaining coordinate of the P11 experiment grid is delay. A coarse analysis may group several fine delays into one label, for example several nearby sampling times into one temporal bin, but that relabeling is scientifically legitimate only if it does not make the response law depend on which fine delay was silently chosen.

Let

\[
\mathcal U
\]

be a fixed declared intervention set, let \(\mathcal T_f\) and \(\mathcal T_c\) be finite fine and coarse delay sets, and let

\[
\boxed{q:\mathcal T_f\twoheadrightarrow\mathcal T_c}
\]

be a declared surjective delay-label quotient.

For every \(u\in\mathcal U\) and \(\tau\in\mathcal T_f\), let

\[
P^{u,\tau}
\]

be the response law on one already-declared common response space. Any node/state coarse-graining needed to create that common response space is logically prior to P32.

---

## 2. Exact delay descent

### Proposition 32A - exact factorization criterion

There exists a unique coarse-delay response table

\[
Q^{u,t},\qquad u\in\mathcal U,\;t\in\mathcal T_c,
\]

such that

\[
\boxed{P^{u,\tau}=Q^{u,q(\tau)}\quad\forall u,\tau}
\]

if and only if

\[
\boxed{
q(\tau)=q(\tau')
\Longrightarrow
P^{u,\tau}=P^{u,\tau'}
\quad\forall u\in\mathcal U.
}
\]

### Proof

If the factorization exists and \(q(\tau)=q(\tau')=t\), then

\[
P^{u,\tau}=Q^{u,t}=P^{u,\tau'}
\]

for every intervention \(u\). Hence response laws are constant on every delay fiber.

Conversely, suppose the fiber-constancy condition holds. For each coarse delay \(t\), choose any \(\tau_t\in q^{-1}(t)\) and define

\[
Q^{u,t}:=P^{u,\tau_t}.
\]

Fiber constancy makes this definition independent of the chosen representative. Therefore \(P^{u,\tau}=Q^{u,q(\tau)}\) for all \(u,\tau\). Uniqueness follows because surjectivity gives at least one fine representative for each coarse delay. \(\square\)

---

## 3. Delay-quotient ambiguity

Define

\[
\boxed{
\eta_q
=
\sup_{u\in\mathcal U}
\sup_{\tau,\tau':\,q(\tau)=q(\tau')}
\|P^{u,\tau}-P^{u,\tau'}\|_{\mathrm{TV}}.
}
\]

This quantity measures the largest response-law variation hidden inside one proposed coarse delay label.

### Corollary 32B - zero ambiguity criterion

\[
\boxed{
\eta_q=0
\iff
\text{exact delay-quotient descent holds}.
}
\]

For finite probability laws, total variation vanishes exactly when the distributions are equal. Applying that fact over every intervention and every quotient fiber gives the result immediately. \(\square\)

---

## 4. Representative dependence when exact descent fails

Suppose exact descent is not available but one nevertheless selects a representative

\[
s(t)\in q^{-1}(t)
\]

for each coarse delay and defines

\[
Q_s^{u,t}:=P^{u,s(t)}.
\]

For another selection \(s'\), both selected delays lie in the same quotient fiber. Therefore

\[
\boxed{
\sup_{u,t}
\|Q_s^{u,t}-Q_{s'}^{u,t}\|_{\mathrm{TV}}
\le \eta_q.
}
\]

Thus \(\eta_q\) directly controls how much the coarse response table can change solely because a different hidden time representative was chosen.

---

## 5. Consequence for P11 response geometry

P11 uses pairwise response geometry

\[
G(u,v,\tau)
=
\|P^{u,\tau}-P^{v,\tau}\|_{\mathrm{TV}}.
\]

A representative selection induces

\[
G_s(u,v,t)
=
\|Q_s^{u,t}-Q_s^{v,t}\|_{\mathrm{TV}}.
\]

By the reverse triangle inequality for a metric,

\[
|G_s(u,v,t)-G_{s'}(u,v,t)|
\le
\|Q_s^{u,t}-Q_{s'}^{u,t}\|_{\mathrm{TV}}
+
\|Q_s^{v,t}-Q_{s'}^{v,t}\|_{\mathrm{TV}}.
\]

Hence

\[
\boxed{
\sup_{u,v,t}
|G_s(u,v,t)-G_{s'}(u,v,t)|
\le 2\eta_q.
}
\]

This is a stability theorem for coarse temporal labeling. It does not assert that time itself is coarse-grained physically.

---

## 6. Exact and approximate certificates

The executable certificate reports two logically distinct statements. Exact descent is certified only when

\[
\boxed{\eta_q=0.}
\]

Separately, for a declared numerical tolerance \(\varepsilon\ge0\), it may report

\[
\boxed{\eta_q\le\varepsilon}
\]

as a tolerance-relative operational certificate. When \(\varepsilon>0\), this second statement must not be described as literal equality of the fine response laws. The unique descended response table is constructed only under exact descent.

---

## 7. Scientific boundary

P32 establishes only a response-law descent criterion relative to the declared experiment family. In particular,

\[
\boxed{
\text{same coarse delay label}
\neq
\text{same physical time}
\neq
\text{dynamical equivalence}.
}
\]

A zero or small \(\eta_q\) can arise because the measured response is stable over a temporal interval, because the measurement is insensitive to existing dynamics, or because the declared experiment lacks temporal resolution. It does not prove that the underlying physical states at two times are identical.

P32 also does not establish:

- a fundamental discretization or quantization of time;
- temporal stationarity outside the retained experiment family;
- equality of generators, propagators, trajectories, or path measures;
- physical completeness of the response descriptor;
- a consciousness variable or experiential bridge.

---

## 8. Role in the theorem chain

P27 formalizes node/partition transport, P28 source semantics, P29 response geometry under node aggregation, P30 assembles the retained P11 components under one shared scale declaration, and P31 permits exact or controlled intervention-label quotienting. P32 now supplies the corresponding criterion for the retained delay coordinate.

Together, P31 and P32 expose a general principle:

\[
\boxed{
\text{coarse labels are legitimate mathematical quotients only when the observable structure factors through them.}
}
\]

The next theorem burden is to assemble node, intervention, and delay quotienting into one joint experiment-grid compatibility statement without allowing error budgets from incompatible quotient constructions to be mixed.

---

## Reproducibility

Executable implementation: [`src/consciousness_bridge/delay_quotient_compatibility.py`](../src/consciousness_bridge/delay_quotient_compatibility.py)

Regression tests: [`tests/test_delay_quotient_compatibility.py`](../tests/test_delay_quotient_compatibility.py)

Publication map: [`docs/figures/p32_delay_quotient_compatibility.svg`](figures/p32_delay_quotient_compatibility.svg)
