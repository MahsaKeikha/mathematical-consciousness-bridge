# Proposition 5: physical-feature sufficiency and counterexamples

## Physical question

Most theories of consciousness identify some physical, causal, computational, or representational structure as especially important.

Examples include intrinsic cause-effect structure, global neuronal workspace organization, recurrent processing, higher-order representation, and predictive or inferential structure.

The phrase

> "feature \(F\) is sufficient for consciousness"

is often scientifically ambiguous.

This proposition gives one exact mathematical meaning appropriate to a physical-to-experiential bridge:

> Does knowledge of the proposed physical feature completely determine the bridge assignment?

---

# 1. Setup

Let

\[
\mathcal Q_P
=
\mathcal P/{\sim_P}
\]

be the physical quotient from Proposition 1 and let

\[
\mathcal Q_E
=
\mathcal E/{\sim_E}
\]

be the experiential quotient.

Assume a candidate bridge

\[
\boxed{
\bar B:\mathcal Q_P\to\mathcal Q_E.
}
\]

Let a proposed representation-invariant physical feature be

\[
\boxed{
F:\mathcal Q_P\to\mathcal Z,
}
\]

where \(\mathcal Z\) may be a scalar, vector, graph, causal structure, dynamical object, equivalence class, or other mathematical feature space.

No scalar assumption is made.

---

# 2. Definition: bridge sufficiency

The feature \(F\) is **bridge-sufficient** for \(\bar B\) when there exists a map

\[
g:\operatorname{Im}(F)\to\mathcal Q_E
\]

such that

\[
\boxed{
\bar B=g\circ F.
}
\]

Thus once \(F(p)\) is known, no additional information about the physical realization \(p\) is required to determine the bridge output.

---

# 3. Proposition

## Proposition 5

For

\[
F:\mathcal Q_P\to\mathcal Z
\]

and

\[
\bar B:\mathcal Q_P\to\mathcal Q_E,
\]

the following statements are equivalent.

### A. Factorization

There exists a unique map

\[
g:\operatorname{Im}(F)\to\mathcal Q_E
\]

such that

\[
\boxed{
\bar B=g\circ F.
}
\]

### B. Fiber constancy

For every \(p,p'\in\mathcal Q_P\),

\[
\boxed{
F(p)=F(p')
\Longrightarrow
\bar B(p)=\bar B(p').
}
\]

### C. Equivalence-relation refinement

Define

\[
p\sim_F p'
\iff
F(p)=F(p')
\]

and

\[
p\sim_B p'
\iff
\bar B(p)=\bar B(p').
\]

Then

\[
\boxed{
\sim_F\;\subseteq\;\sim_B.
}
\]

Equivalently, every fiber of \(F\) is contained in one experiential fiber of the bridge.

---

# 4. Proof

## A implies B

Assume

\[
\bar B=g\circ F.
\]

If

\[
F(p)=F(p'),
\]

then

\[
\bar B(p)
=
g(F(p))
=
g(F(p'))
=
\bar B(p').
\]

Therefore the bridge is constant on every feature fiber.

## B implies A

Assume

\[
F(p)=F(p')
\Longrightarrow
\bar B(p)=\bar B(p').
\]

For any

\[
z\in\operatorname{Im}(F),
\]

choose a physical class \(p\) satisfying

\[
F(p)=z
\]

and define

\[
\boxed{
g(z)=\bar B(p).}
\]

This is well defined. If another \(p'\) satisfies

\[
F(p')=z,
\]

then

\[
F(p)=F(p'),
\]

so by assumption

\[
\bar B(p)=\bar B(p').
\]

Hence the value of \(g(z)\) does not depend on the chosen representative.

For every \(p\in\mathcal Q_P\),

\[
g(F(p))=\bar B(p),
\]

therefore

\[
\bar B=g\circ F.
\]

Uniqueness follows because every \(z\in\operatorname{Im}(F)\) has the form \(F(p)\), forcing

\[
g(z)=\bar B(p).
\]

## B if and only if C

By definition,

\[
p\sim_Fp'
\]

means

\[
F(p)=F(p'),
\]

while

\[
p\sim_Bp'
\]

means

\[
\bar B(p)=\bar B(p').
\]

Thus B is exactly the inclusion

\[
\sim_F\subseteq\sim_B.
\]

\[
\boxed{\text{QED}}
\]

---

# 5. Counterexample corollary

A single pair

\[
p,p'\in\mathcal Q_P
\]

satisfying

\[
\boxed{
F(p)=F(p')
\quad\text{and}\quad
\bar B(p)\ne\bar B(p')
}
\]

is sufficient to prove that no map

\[
g:\operatorname{Im}(F)\to\mathcal Q_E
\]

can satisfy

\[
\bar B=g\circ F.
\]

Therefore one exact route for challenging a proposed consciousness signature is to construct **feature-matched, bridge-different counterexamples**.

This is stronger than merely finding systems with different numerical values of the proposed feature.

---

# 6. What this theorem does and does not establish

The proposition is a factorization theorem.

It establishes the mathematical meaning of the statement:

\[
\boxed{
\text{"the bridge depends only on }F\text{"}.
}
\]

It does not by itself establish that any particular physical feature is the true bridge to consciousness.

If a theory defines its own bridge directly as

\[
\bar B=g\circ F,
\]

then Proposition 5 is satisfied internally by construction. The scientific burden remains to justify the bridge and test its consequences against alternatives.

This distinction is crucial. Internal mathematical coherence is not the same as empirical validation of the bridge premise.

---

# 7. Relation to major theory families

The common translation developed in [Candidate Theory Families](candidate_theory_families.md) permits the same theorem to be asked of structurally different proposals.

| Theory family | Schematic proposed feature class | P5 question |
| --- | --- | --- |
| IIT 4.0 | intrinsic cause-effect structure | are experiential assignments constant on fibers of the proposed intrinsic structure? |
| GNWT | multilevel workspace/ignition/global-availability structure | are bridge assignments constant whenever the relevant GNW structure is identical? |
| RPT | recurrent-processing structure | can two systems share the relevant recurrence structure while receiving different bridge assignments? |
| HOT | higher-order representational relation | does the bridge factor completely through the proposed higher-order relation? |
| predictive/NR/active-inference families | theory-specific hierarchical inferential or representational structure | which precise feature, if any, has bridge-sufficient fibers? |

These are theorem templates, not claims that the source theories have already been reduced to the displayed notation.

---

# 8. Physical interpretation

A proposed physical signature of consciousness should not merely correlate with consciousness labels.

If it is claimed to be sufficient for the bridge, then every physically admissible system with the same value of that signature must receive the same experiential assignment:

\[
F(p)=F(p')
\Longrightarrow
\bar B(p)=\bar B(p').
\]

This creates a powerful search strategy.

Instead of asking only

> "Does feature \(F\) correlate with conscious reports?"

we can ask

> "Can we construct physically realizable systems that preserve \(F\) while changing another structure that a competing bridge theory says matters?"

If the competing theory predicts a different experiential assignment and Proposition 2/P4 identify an experiment capable of exposing that difference, the feature-sufficiency claim becomes empirically testable.

---

# 9. Relation to representation invariance

The domain of \(F\) is already

\[
\mathcal Q_P,
\]

not raw physical descriptions.

Therefore a candidate feature must first survive Proposition 1. A quantity that changes under physically irrelevant coordinates or encodings is not yet suitable as a universal physical consciousness signature.

The logical sequence is

\[
\boxed{
\text{representation invariance}
\xrightarrow{\mathrm{P1}}
\text{feature sufficiency}
\xrightarrow{\mathrm{P5}}
\text{empirical discriminability}
\xrightarrow{\mathrm{P2-P4}}
\text{bridge testing}.
}
\]

---

# 10. A stronger target: bridge completeness

Sufficiency requires only

\[
F(p)=F(p')
\Longrightarrow
\bar B(p)=\bar B(p').
\]

A stronger condition is

\[
\boxed{
F(p)=F(p')
\iff
\bar B(p)=\bar B(p').
}
\]

Under this biconditional, the feature fibers coincide exactly with the bridge fibers.

Such a feature is a **complete invariant of the bridge** on the declared physical domain.

This stronger structure is the subject of the next theorem layer, Proposition 6.

---

# 11. Mathematical lineage

The factorization-through-fibers result is standard elementary quotient/factorization mathematics. The contribution of Proposition 5 is its explicit use as a theory-comparison criterion for physical-to-experiential consciousness bridges and as a counterexample template connected to the repository's identifiability and experiment-design framework.

The theory-family interpretation is grounded in the source-specific literature catalogued in [Candidate Theory Families](candidate_theory_families.md) and [Literature Map](literature_map.md).

---

# 12. Status

| Item | Status |
| --- | --- |
| bridge-sufficiency definition | defined |
| factorization/fiber equivalence | proved |
| equivalence-relation refinement characterization | proved |
| single-pair counterexample corollary | proved |
| application to any named consciousness theory | requires source-faithful feature formalization and empirical bridge specification |
| next result | Proposition 6: canonical complete bridge signature |
