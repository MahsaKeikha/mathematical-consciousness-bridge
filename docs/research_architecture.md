# Research Architecture

![Mathematical Consciousness Bridge research architecture](figures/research_architecture.svg)

The program separates physical modeling, candidate physical signatures, temporal physical organization, experiential formalization, bridge principles, observable predictions, finite-data certification, and falsification. This prevents a theorem about a physical quantity from being mistaken for independent support of a physical-to-experiential bridge.

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

## Layer 5 - temporal physical organization

A static signature does not yet specify how physical organization persists or changes through time.

For finite causal-structure fingerprint

\[
c_t=(g_t,a_t,k_t),
\]

[Proposition 14](proposition_14_temporal_continuation.md) defines the relabeling-invariant quotient metric

\[
\boxed{
\overline D_w([c],[c'])
=
\min_{h\in\mathcal H}D_w(c,hc'),
}
\]

and temporal path quantities

\[
\boxed{
V_{0:T}
=
\sum_{t=0}^{T-1}\overline D_w([c_t],[c_{t+1}]),
\qquad
J_{0:T}
=
\max_t\overline D_w([c_t],[c_{t+1}]).
}
\]

P14 proves that these quantities are invariant under time-dependent admissible relabelings and that endpoint equality does not replace path analysis.

[Proposition 15](proposition_15_finite_sample_temporal_certification.md) then propagates declared fingerprint-error radii through this geometry:

\[
\boxed{
|\widehat d_{st}-d_{st}|
\le
\varepsilon_s+\varepsilon_t.
}
\]

Thus temporal physical organization is both representation aware and finite-error certifiable under stated assumptions.

This layer remains physical. Temporal continuation is not identified with experiential continuity.

---

## Layer 6 - experiential formalization

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

This remains an essential open formalization problem. A convenient physical score or a smooth physical trajectory does not substitute for a definition of the experiential target.

---

## Layer 7 - bridge

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

## Layer 8 - empirical interface

A complete theory must generate observable probability laws under declared protocols:

\[
P_{\mathfrak T}^{\pi,q}.
\]

Propositions 2-4 establish exact identifiability and experiment-design results. [Candidate Theory Families](candidate_theory_families.md) translates IIT, GNWT, recurrent-processing, higher-order, predictive/neurorepresentational, and repository candidate families into a common comparison interface.

---

## Layer 9 - experimental recoverability and finite-data certification

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

P15 adds a separate temporal-certification layer. Given valid simultaneous fingerprint radii, it converts estimated temporal separations into certified intervals and explicitly preserves an unresolved region when the data do not determine whether a structural threshold is crossed.

---

## Layer 10 - falsification and counterexample search

Every candidate signature or bridge is exposed to:

1. representation counterexamples;
2. feature-sufficiency collisions;
3. observational non-identifiability;
4. recoverability failures;
5. one-component and pairwise-component collisions;
6. endpoint-only temporal failures;
7. finite-data overclaiming and unresolved temporal comparisons;
8. composition, splitting, merging, or coupling inconsistencies;
9. empirical prediction failures;
10. biological and artificial substrate counterexamples.

P12-P15 illustrate the architecture in practice: the physical candidate is attacked internally, temporally, and statistically before an experiential equivalence claim is attached.

---

## Layer 11 - conditional bridge theorem

Only after the physical domain, experiential domain, bridge principles, complete physical signature, empirical identifiability, recoverability, finite-data uncertainty, temporal consistency, composition rules, and falsification conditions are explicit should the program state a final bridge theorem.

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
