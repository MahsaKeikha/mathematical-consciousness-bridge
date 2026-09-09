# Research Architecture

![Mathematical Consciousness Bridge research architecture](figures/research_architecture.svg)

The program separates physical modeling, candidate physical signatures, experiential formalization, bridge principles, observable predictions, finite-data certification, and falsification. This prevents a theorem about a physical quantity from being mistaken for independent support of a physical-to-experiential bridge.

---

## Layer 1 - physical realization

A physical description specifies

\[
\boxed{
p=(\mathcal X,\mathcal D,\mathfrak I,\mathcal O),
}
\]

with state space, dynamics, admissible interventions, and observable map.

Examples include

\[
\dot x(t)=F(x(t),u(t)),
\qquad
y(t)=h(x(t)),
\]

or

\[
X_{t+\Delta t}
\sim
K_{\Delta t}(\cdot\mid X_t,u_t).
\]

---

## Layer 2 - certified physical subsystem

When applicable, [Spatiotemporal Observer Mathematics](https://github.com/MahsaKeikha/spatiotemporal-observer-math) can supply a statistically certified time-dependent physical subsystem or world-tube

\[
\boxed{
\mathcal W=(S_0,\ldots,S_{T-1}).
}
\]

The world-tube is a physical domain candidate, not an experiential conclusion.

---

## Layer 3 - physical equivalence

Declare which representation changes leave the physically relevant system unchanged:

\[
\boxed{
p\sim_Pp'.}
\]

Then

\[
\boxed{
\mathcal Q_P
=
\mathcal P/{\sim_P}.
}
\]

[Proposition 1](proposition_1_representation_invariance.md) gives the exact condition under which a bridge descends to this quotient.

---

## Layer 4 - candidate physical signature

A candidate physical signature is a representation-independent feature

\[
F_*:\mathcal Q_P\to\mathcal Z_*.
\]

The first original candidate is [intervention-resolved causal structure](proposition_11_intervention_resolved_causal_structure.md):

\[
\boxed{
F_{\mathrm{causal}}(p)
=
[\mathfrak C_p]_{\cong},
}
\]

with

\[
\mathfrak C_p
=
(V,\mathcal U_p,\mathcal T,\mathcal G_p,\mathcal A_p,\mathcal K_p).
\]

The three components encode intervention-response geometry, directed perturbational influence, and partition-specific response irreducibility.

[Proposition 12](proposition_12_component_insufficiency.md) proves that each component alone, and several scalar summaries, are incomplete. [Proposition 13](proposition_13_pairwise_component_irredundancy.md) proves that each component remains irredundant relative to the other two on an explicit finite audit domain.

---

## Layer 5 - experiential formalization

Define

\[
\mathcal E
\]

and experiential equivalence

\[
e\sim_Ee'.
\]

The experiential quotient is

\[
\boxed{
\mathcal Q_E
=
\mathcal E/{\sim_E}.
}
\]

This remains an essential open formalization problem. A convenient physical score does not substitute for a definition of the experiential target.

---

## Layer 6 - bridge

The most general bridge begins as a relation

\[
\mathcal B
\subseteq
\mathcal P\times\mathcal E.
\]

When single-valuedness and invariance are justified,

\[
\boxed{
\bar B:
\mathcal Q_P
\longrightarrow
\mathcal Q_E.
}
\]

Propositions 5 and 6 formalize physical-feature sufficiency and bridge completeness. The strongest physical-signature target is

\[
\boxed{
F_*(p)=F_*(p')
\iff
\bar B(p)=\bar B(p').
}
\]

---

## Layer 7 - empirical interface

A complete theory must generate observable probability laws under declared protocols:

\[
P_{\mathfrak T}^{\pi,q}.
\]

Propositions 2-4 establish exact identifiability and experiment-design results. [Candidate Theory Families](candidate_theory_families.md) translates IIT, GNWT, recurrent-processing, higher-order, predictive/neurorepresentational, and repository candidate families into a common comparison interface.

---

## Layer 8 - experimental recoverability and finite-data certification

For physical fingerprint

\[
\Psi_\Pi(p)
=
(P^{\pi,p})_{\pi\in\Pi},
\]

Proposition 7 gives the exact recoverability criterion. Propositions 8-10 add finite-error certification, explicit sample complexity, and robust protocol design:

\[
\boxed{
\gamma_S
=
\delta_S-\omega_S
>4\varepsilon,
}
\]

and

\[
\boxed{
n
\ge
\frac{8K^2}{\gamma_S^2}
\log\left(
\frac{2N_PN_\pi K}{\alpha}
\right).
}
\]

---

## Layer 9 - falsification and counterexample search

Every candidate signature or bridge is exposed to:

1. representation counterexamples;
2. feature-sufficiency collisions;
3. observational non-identifiability;
4. recoverability failures;
5. one-component and pairwise-component collisions;
6. temporal or composition inconsistencies;
7. empirical prediction failures;
8. biological and artificial substrate counterexamples.

P12-P13 illustrate the architecture in practice: the first physical candidate is attacked internally before an experiential equivalence claim is attached.

---

## Layer 10 - conditional bridge theorem

Only after the physical domain, experiential domain, bridge principles, complete physical signature, empirical identifiability, recoverability, finite-data uncertainty, and falsification conditions are explicit should the program state a final bridge theorem.

The schematic target is

\[
\boxed{
\text{physical first principles}
+
\text{validated bridge premises}
+
\text{finite-data certification}
\Longrightarrow
\text{formal experiential property}.
}
\]

See [Universal Consciousness Proof Target](universal_proof_target.md).