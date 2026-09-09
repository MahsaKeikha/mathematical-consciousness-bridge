# Visual Research Guide

This guide provides the fastest visual route through the Mathematical Consciousness Bridge program. Every figure is a research diagram: labels correspond to physical objects, equations, theorem statements, evidence classes, or open problems defined elsewhere in the repository.

## 1. Entire research architecture

![Research architecture](figures/research_architecture.svg)

The project separates physical realization, representation-invariant physical structure, candidate physical signatures, bridge principles, experiential structure, observable predictions, finite-data certification, composition, and falsification.

The key distinction is

\[
\boxed{
\text{physical structure}
\neq
\text{experiential interpretation}
}
\]

until an independently justified bridge connects them.

## 2. Theorem dependency map

![Theorem roadmap](figures/theorem_roadmap.svg)

Propositions 1-10 establish the general mathematical infrastructure. Proposition 11 introduces the first original physical candidate, **intervention-resolved causal structure**. Proposition 12 proves that its individual components and several scalar reductions are incomplete. Proposition 13 proves that no pair of the three major components reconstructs the omitted component on the declared finite audit domain. Proposition 14 turns the static physical candidate into a representation-invariant temporal trajectory. Proposition 15 propagates finite fingerprint uncertainty through that temporal geometry. Proposition 16 establishes the independent-composition null model and a response-level coupling defect.

## 3. Anatomy of the causal-structure candidate

![Causal-structure anatomy](figures/causal_structure_anatomy.svg)

The candidate begins from intervention-conditioned response laws

\[
P_p^{u,\tau}
=
\mathcal L(Y_{t+\tau}^{V}\mid do(u),p),
\]

and retains

\[
\boxed{
\mathcal G_p
\quad
\mathcal A_p
\quad
\mathcal K_p
}
\]

for response geometry, directed interventional influence, and partition irreducibility.

Its representation-independent form is

\[
\boxed{
F_{\mathrm{causal}}(p)
=
[\mathfrak C_p]_{\cong}.
}
\]

## 4. Why one component is not enough

![Proposition 12 collisions](figures/p12_collision_map.svg)

Proposition 12 gives explicit realizable collision pairs showing that the full physical candidate cannot generally be reconstructed from response geometry alone, partition irreducibility alone, directed marginal influence alone, response diameter, one scalar irreducibility value, or a cycle/no-cycle recurrence flag.

## 5. Why two components are still not enough

![Proposition 13 pairwise irredundancy](figures/p13_component_irredundancy.svg)

Proposition 13 constructs three independent collision families:

\[
(\mathcal G,\mathcal A)\text{ fixed},\quad\mathcal K\text{ changes},
\]

\[
(\mathcal G,\mathcal K)\text{ fixed},\quad\mathcal A\text{ changes},
\]

\[
(\mathcal A,\mathcal K)\text{ fixed},\quad\mathcal G\text{ changes}.
\]

Therefore each component carries information not reconstructible from the other two on the explicit audit domain.

## 6. Temporal continuation of the physical candidate

![Proposition 14 temporal continuation](figures/p14_temporal_continuation.svg)

Proposition 14 defines a weighted metric on the full three-component fingerprint and removes physically irrelevant relabeling by minimizing over the declared finite isometry group:

\[
\boxed{
\overline D_w([c],[c'])
=
\min_{h\in\mathcal H}D_w(c,hc').
}
\]

A physical trajectory is then described by cumulative variation

\[
\boxed{
V_{0:T}
=
\sum_t\overline D_w([c_t],[c_{t+1}])
}
\]

and maximum local jump

\[
\boxed{
J_{0:T}
=
\max_t\overline D_w([c_t],[c_{t+1}]).
}
\]

The theorem proves representation invariance and shows why identical endpoints cannot replace analysis of the intervening path.

## 7. Finite-sample temporal certification

![Proposition 15 finite-sample temporal certification](figures/p15_finite_sample_temporal_certification.svg)

Proposition 15 assumes simultaneous fingerprint radii

\[
D_w(c_t,\widehat c_t)\le\varepsilon_t
\]

and proves

\[
\boxed{
|\widehat d_{st}-d_{st}|
\le\varepsilon_s+\varepsilon_t.
}
\]

This yields a certified interval for the true physical change:

\[
\boxed{
\max\{0,\widehat d_{st}-\varepsilon_s-\varepsilon_t\}
\le d_{st}\le
\widehat d_{st}+\varepsilon_s+\varepsilon_t.
}
\]

Relative to a declared threshold \(\eta\), every comparison is classified as **certified above**, **certified below**, or **unresolved**. The unresolved region is kept explicit rather than hidden behind a forced binary decision.

## 8. Independent composition and controlled coupling

![Proposition 16 independent composition and controlled coupling](figures/p16_composition_coupling.svg)

Proposition 16 defines the independent response-level composition

\[
\boxed{
P_{A\otimes B}^{(u_A,u_B),\tau}
=
P_A^{u_A,\tau}\otimes P_B^{u_B,\tau}.
}
\]

Under this null model, cross-system directed influence vanishes and the partition separating the two complete subsystems has zero irreducibility:

\[
\boxed{
A_{ij}^{A\otimes B}(\tau)=0
\quad(i\in A,j\in B),
}
\]

\[
\boxed{
\kappa_{A\otimes B}^{\tau}(\pi_{A|B})=0.
}
\]

The composed response distance obeys

\[
\boxed{
\max\{d_A,d_B\}
\le d_{AB}
\le d_A+d_B-d_Ad_B.
}
\]

For an arbitrary observed joint response, the response-level coupling defect is

\[
\boxed{
\chi_{A|B}(\tau)
=
\kappa_{AB}^{\tau}(\pi_{A|B}).
}
\]

A positive defect certifies departure from response factorization on the declared intervention-observable regime. A zero defect does not by itself establish universal mechanistic independence outside that regime.

## 9. Universal proof criteria

![Universal proof ladder](figures/universal_proof_ladder.svg)

The project uses twelve criteria to separate a theorem internal to a framework from a scientifically exposed physical-to-experiential result. Full statements are in [Universal Consciousness Proof Target](universal_proof_target.md).

## 10. Competing theory families

![Theory comparison map](figures/theory_comparison_map.svg)

The project compares contemporary theory families through one common interface

\[
\mathfrak T_j
=
(\mathcal F_j,\mathcal B_j,\mathcal M_j,\Pi_j).
\]

This allows theory-specific physical features, bridge architectures, measurements, and interventions to be compared using the same identifiability and experiment-design theorems.

## 11. Recommended reading order

| Stage | Read | Main question |
| --- | --- | --- |
| 1 | [README](../README.md) | What is the complete research program? |
| 2 | [Bridge Problem](bridge_problem.md) | What is missing between physics and experience? |
| 3 | [Physical Foundation](physical_foundation.md) | What counts as a physical system and admissible intervention? |
| 4 | [Theorem Roadmap](theorem_roadmap.md) | What has actually been proved? |
| 5 | [P11 - Intervention-Resolved Causal Structure](proposition_11_intervention_resolved_causal_structure.md) | What is the first original candidate physical signature? |
| 6 | [P12 - Component Insufficiency](proposition_12_component_insufficiency.md) | Which one-component reductions fail? |
| 7 | [P13 - Pairwise Component Irredundancy](proposition_13_pairwise_component_irredundancy.md) | Can any two components reconstruct the third? |
| 8 | [P14 - Temporal Continuation](proposition_14_temporal_continuation.md) | How is the physical candidate compared through time after relabeling? |
| 9 | [P15 - Finite-Sample Temporal Certification](proposition_15_finite_sample_temporal_certification.md) | When is an apparent temporal change larger than measurement uncertainty? |
| 10 | [P16 - Independent Composition and Coupling](proposition_16_independent_composition_and_coupling.md) | When do two systems merely coexist, and when does observed response structure depart from factorization? |
| 11 | [Candidate Theory Families](candidate_theory_families.md) | How are major consciousness theories compared? |
| 12 | [Universal Proof Target](universal_proof_target.md) | What would the final theorem-and-evidence package require? |
| 13 | [Equation and Citation Map](equation_and_citation_map.md) | Which equations are original, standard, assumed, or externally sourced? |
| 14 | [Literature Map](literature_map.md) | What role does each cited source play? |

## 12. Reading-status convention

| Label | Meaning |
| --- | --- |
| **Definition** | mathematical object introduced by the program |
| **Proved** | theorem derived from declared assumptions |
| **Candidate physical signature** | physical structure under test, not an experiential conclusion |
| **Empirical result** | evidence reported by a cited experiment or dataset |
| **Counterexample / no-go** | a sufficiency, compression, or recoverability claim fails on an explicit construction |
| **Finite-error certificate** | statement guaranteed under explicitly declared estimation-error radii |
| **Physical composition theorem** | theorem about factorization, coupling, or decomposition of the physical response structure |
| **Open bridge problem** | unresolved connection between physical and experiential structure |

This convention is essential for reading every figure and theorem in the repository correctly.
