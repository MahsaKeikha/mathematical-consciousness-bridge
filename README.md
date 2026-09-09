# Mathematical Consciousness Bridge

[![tests](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/test.yml/badge.svg)](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/test.yml)
[![version](https://img.shields.io/badge/version-0.17.0-2563eb)](CITATION.cff)
[![license](https://img.shields.io/badge/license-MIT-059669)](LICENSE)

**Mahsa Keikha, PhD**

> **What mathematical and physical conditions would be required for a physical description of a system to support a scientifically testable claim about consciousness?**

This repository develops a formal mathematical-physics program for the **consciousness bridge problem**: connecting physical organization to formal experiential structure through explicit bridge principles, theorem-level consequences, empirical identifiability, controlled intervention, finite-data certification, temporal structure, composition, scale analysis, and falsification.

It is the next research layer after **[Spatiotemporal Observer Mathematics](https://github.com/MahsaKeikha/spatiotemporal-observer-math)**. The companion project asks when a persistent moving physical subsystem can be inferred from measured dynamics. This repository begins from such physically defined systems and asks what further mathematical, causal, statistical, empirical, and experiential structure would be required before a consciousness bridge could be justified.

The research sequence is

\[
\boxed{
\text{measured dynamics}
\longrightarrow
\text{certified moving subsystem}
\longrightarrow
\text{intervention-resolved causal structure}
\longrightarrow
\text{temporal, compositional, and scale structure}
\longrightarrow
\text{mathematical consciousness bridge}.
}
\]

---

# Visual overview

![Mathematical Consciousness Bridge research architecture](docs/figures/research_architecture.svg)

**Figure 1. Research architecture.** Physical realization, representation-independent physical structure, candidate physical signatures, bridge principles, experiential structure, observable predictions, finite-data certification, and falsification are treated as distinct scientific layers.

The central target is

\[
\boxed{
\text{physical first principles}
+
\text{bridge principles}
+
\text{empirically discriminating evidence}
+
\text{finite-data certification}
\Longrightarrow
\text{formal experiential property}.
}
\]

The mathematical implication must follow from explicit premises. The physical-to-experiential premises must also generate consequences capable of empirical discrimination.

---

# Start here

| Reader goal | Entry point |
| --- | --- |
| See the complete visual program | **[Visual Research Guide](docs/visual_research_guide.md)** |
| Enter from physics or mathematics | **[Physics and Mathematics Atlas](docs/physics_mathematics_consciousness_atlas.md)** |
| Trace foundational physics, mathematics, and NASA sources | **[Foundational Physics, Mathematics, and Spaceflight Bibliography](docs/foundational_physics_mathematics_bibliography.md)** |
| Understand the strongest theorem target | **[Universal Consciousness Proof Target](docs/universal_proof_target.md)** |
| Understand the physical input | **[Physical Foundation](docs/physical_foundation.md)** |
| Read the exact bridge problem | **[Consciousness Bridge Problem](docs/bridge_problem.md)** |
| Follow the theorem chain | **[Theorem Roadmap](docs/theorem_roadmap.md)** |
| Read the original physical candidate | **[P11 - Intervention-Resolved Causal Structure](docs/proposition_11_intervention_resolved_causal_structure.md)** |
| Read the current composition result | **[P16 - Independent Composition and Coupling](docs/proposition_16_independent_composition_and_coupling.md)** |
| Read the current scale-change result | **[P17 - Coarse-Graining and Refinement](docs/proposition_17_coarse_graining_and_refinement.md)** |
| Compare major consciousness theories | [Candidate Theory Families](docs/candidate_theory_families.md) |
| Audit equation provenance | [Equation and Citation Map](docs/equation_and_citation_map.md) |
| Inspect falsification criteria | [Falsification Program](docs/falsification_program.md) |
| Trace consciousness literature | [Literature Map](docs/literature_map.md) |
| Read machine-readable references | [`references.bib`](references.bib) |
| Cite the program | [`CITATION.cff`](CITATION.cff) |

---

# Abstract

A physical theory can specify states, dynamics, interventions, causal response laws, probability distributions, thermodynamic constraints, and measurement procedures without specifying why any physical organization should correspond to subjective experience. A mathematical theory of consciousness therefore requires an additional object: a bridge from physically meaningful equivalence classes to formally defined experiential equivalence classes.

This repository makes that bridge itself the object of mathematics. Propositions 1-10 establish representation invariance, theory identifiability, observational equivalence classes, experiment design, physical-feature sufficiency, canonical bridge completeness, experimental recoverability, robust finite-error recovery, explicit sample complexity, and robust protocol design.

Proposition 11 introduces the first original candidate physical signature: **intervention-resolved causal structure**. It is deliberately structured rather than scalar. Propositions 12-13 then construct counterexamples proving that no single major component and no two-component projection can reconstruct the complete candidate on the declared audit domains. Propositions 14-15 add representation-invariant temporal continuation and finite-error temporal certification. Proposition 16 establishes the independent-composition null model and a measurable response-level coupling defect. Proposition 17 proves total-variation contraction under deterministic coarse-graining and gives exact information-collision witnesses for non-injective scale reduction.

Alongside the theorem sequence, the repository develops a visual **Physics and Mathematics Atlas for Consciousness Research**, connecting stochastic dynamics, information theory, information geometry, causal inference, thermodynamics, neural complexity, perturbational measurement, competing consciousness theories, and extreme-environment research.

The current record therefore separates:

1. **proved mathematical structure** - P1-P17;
2. **candidate physical structure** - intervention-resolved causal structure and its temporal/compositional/scale behavior;
3. **empirical measurement interfaces** - perturbation, anesthesia, EEG, imaging, behavioral and extreme-environment studies;
4. **open bridge problem** - determining whether an independently justified physical equivalence structure can be connected to formal experiential equivalence and survive competing-theory, cross-substrate, temporal, compositional, scale, and empirical tests.

---

# 1. Physics and Mathematics Atlas

![Physics and mathematics atlas](docs/figures/physics_mathematics_atlas.svg)

**Figure 2. Physics and mathematics atlas.** Physical law and measurable dynamics are separated from mathematical invariants, empirical evidence, and bridge interpretation.

The atlas follows

\[
\boxed{
\text{physical law}
\longrightarrow
\text{measurable structure}
\longrightarrow
\text{mathematical invariant}
\longrightarrow
\text{empirical discrimination}
\longrightarrow
\text{bridge test}.
}
\]

## 1.1 Physical dynamics

A controlled stochastic system may be represented by

\[
\boxed{
dX_t
=
f(X_t,u_t)\,dt
+G(X_t,u_t)\,dW_t,
}
\]

or more generally by a transition law

\[
\boxed{
X_{t+\Delta t}
\sim
K_{\Delta t}(\cdot\mid X_t,u_t).
}
\]

The physical model must specify state variables, observables, interventions, noise, timescale, and boundary conditions.

## 1.2 Information theory

For random variables \(X,Y\),

\[
\boxed{
I(X;Y)
=
D_{\mathrm{KL}}(P_{XY}\Vert P_XP_Y).
}
\]

This quantifies statistical dependence. It does not by itself determine causal direction or experiential structure.

**Primary lineage:** Shannon 1948; Cover and Thomas 2006.

## 1.3 Information geometry

For a statistical model \(p(x\mid\theta)\), the Fisher metric is

\[
\boxed{
g_{ij}(\theta)
=
\mathbb E_\theta
\left[
\partial_i\log p(X\mid\theta)
\partial_j\log p(X\mid\theta)
\right].
}
\]

This gives a representation of local statistical distinguishability on a manifold of probability laws.

**Primary lineage:** Amari 2016; Ay, Jost, Le, and Schwachhofer 2017.

## 1.4 Thermodynamics of information

Landauer's bound for logically irreversible erasure is

\[
\boxed{
W_{\mathrm{erase}}
\ge
k_B T\ln 2.
}
\]

Stochastic thermodynamics extends work, heat, and entropy production to fluctuating nonequilibrium trajectories.

**Primary lineage:** Landauer 1961; Seifert 2012.

These are physical constraints on information processing, not consciousness criteria.

## 1.5 Causal intervention

For physical system \(p\), intervention \(u\), and response delay \(\tau\),

\[
\boxed{
P_p^{u,\tau}
=
\mathcal L(Y_{t+\tau}^{V}\mid do(u),p).
}
\]

The \(do(u)\) notation distinguishes intervention from passive conditioning.

**Primary lineage:** Pearl 2009; Peters, Bauer, and Pfister 2020.

---

# 2. Equation-to-evidence discipline

![Equation to evidence map](docs/figures/equation_evidence_map.svg)

**Figure 3. Equation-to-evidence map.** A valid equation, physical interpretation, measurement model, empirical observation, and experiential conclusion are different scientific objects.

The repository applies

\[
\boxed{
\text{equation}
\neq
\text{physical interpretation}
\neq
\text{measurement model}
\neq
\text{empirical evidence}
\neq
\text{bridge conclusion}.
}
\]

For every major proposed relation, the project asks:

1. What is the equation?
2. What physical object does it describe?
3. How is the object measured?
4. What evidence supports the measurement-model relation?
5. What additional principle would be required to infer an experiential property?

---

# 3. Physical and experiential domains

A physical input is modeled abstractly as

\[
\boxed{
p=(\mathcal X,\mathcal D,\mathfrak I,\mathcal O),
}
\]

where \(\mathcal X\) is state space, \(\mathcal D\) dynamics, \(\mathfrak I\) admissible interventions, and \(\mathcal O\) the observable map.

Physical descriptions are quotiented by an equivalence relation

\[
\boxed{
p\sim_Pp',
\qquad
\mathcal Q_P=\mathcal P/{\sim_P}.
}
\]

Let \(\mathcal E\) be a formal experiential space with experiential equivalence

\[
e\sim_Ee',
\qquad
\boxed{
\mathcal Q_E=\mathcal E/{\sim_E}.
}
\]

The target bridge is

\[
\boxed{
\bar B:
\mathcal Q_P
\longrightarrow
\mathcal Q_E.
}
\]

A complete empirical bridge theory must also specify a measurement interface and experiment family:

\[
\boxed{
\mathfrak T
=
(\mathcal P,\mathcal E,\sim_P,\sim_E,\mathcal B,\mathcal M,\Pi).
}
\]

---

# 4. Universal proof target

![Universal proof ladder](docs/figures/universal_proof_ladder.svg)

**Figure 4. Universal proof ladder.** The strongest target is decomposed into physical, mathematical, empirical, and finite-data requirements.

| Criterion | Requirement | Current support |
| --- | --- | --- |
| U1 | physical well-definedness | physical foundation + P1 |
| U2 | experiential well-definedness | open formalization problem |
| U3 | non-definitional bridge | architectural requirement |
| U4 | representation invariance | P1 |
| U5 | physical-feature sufficiency | P5 |
| U6 | bridge completeness | P6 |
| U7 | empirical identifiability | P2-P3 |
| U8 | cross-theory discrimination | P4 + theory interface |
| U9 | experimental recoverability | P7 |
| U10 | finite-measurement certification | P8, P15 |
| U11 | explicit sample complexity | P9 + restricted P15 corollary |
| U12 | temporal, compositional, scale, substrate, and falsification consistency | P14-P17 partially address this layer |

A strong conditional theorem would have the form

\[
\boxed{
\begin{aligned}
& p\in\mathcal Q_P,\\
& A_1,\ldots,A_k\text{ bridge principles hold},\\
& F_*(p)\text{ is a complete physical signature},\\
& \widehat F_*(p)\text{ is recovered with declared confidence},\\
& V_1,\ldots,V_r\text{ discriminating validation conditions hold}
\\[1mm]
&\qquad\Longrightarrow
\bar B(p)\in\mathcal C_E.
\end{aligned}
}
\]

The stronger biconditional target is

\[
\boxed{
\bar B(p)\in\mathcal C_E
\iff
F_*(p)\in\mathcal R_C.
}
\]

Both directions require independent justification.

---

# 5. Theorem roadmap - Propositions 1 through 17

![Propositions 1 through 17 theorem roadmap](docs/figures/theorem_roadmap.svg)

**Figure 5. Theorem roadmap.** The program moves from physical well-definedness and empirical identifiability to candidate structure, temporal continuation, composition, and scale change.

| Proposition | Core result | Status | Proof |
| --- | --- | --- | --- |
| **P1** | representation-invariant bridge descends to physical quotient | Proved | [P1](docs/proposition_1_representation_invariance.md) |
| **P2** | exact experiment-class bridge identifiability using total variation | Proved | [P2](docs/proposition_2_bridge_identifiability.md) |
| **P3** | observational theory-equivalence classes | Proved | [P3](docs/proposition_3_bridge_equivalence_classes.md) |
| **P4** | maximin and set-cover discriminating experiment design | Proved | [P4](docs/proposition_4_discriminating_experiment_design.md) |
| **P5** | exact physical-feature sufficiency criterion | Proved | [P5](docs/proposition_5_feature_sufficiency.md) |
| **P6** | canonical complete bridge signature | Proved | [P6](docs/proposition_6_canonical_bridge_signature.md) |
| **P7** | exact experimental recoverability criterion | Proved | [P7](docs/proposition_7_experimental_signature_recovery.md) |
| **P8** | robust finite-error signature recovery | Proved | [P8](docs/proposition_8_robust_signature_recovery.md) |
| **P9** | explicit categorical sample-complexity guarantee | Proved | [P9](docs/proposition_9_categorical_sample_complexity.md) |
| **P10** | robust protocol-family design | Proved | [P10](docs/proposition_10_robust_experiment_design.md) |
| **P11** | intervention-resolved causal structure | Proved construction / candidate | [P11](docs/proposition_11_intervention_resolved_causal_structure.md) |
| **P12** | single-component and scalar insufficiency | Proved no-go | [P12](docs/proposition_12_component_insufficiency.md) |
| **P13** | pairwise component irredundancy | Proved no-go | [P13](docs/proposition_13_pairwise_component_irredundancy.md) |
| **P14** | representation-invariant temporal continuation | Proved | [P14](docs/proposition_14_temporal_continuation.md) |
| **P15** | finite-error temporal certification | Proved | [P15](docs/proposition_15_finite_sample_temporal_certification.md) |
| **P16** | independent composition and response-level coupling defect | Proved | [P16](docs/proposition_16_independent_composition_and_coupling.md) |
| **P17** | coarse-graining contraction and refinement non-recoverability | Proved | [P17](docs/proposition_17_coarse_graining_and_refinement.md) |

---

# 6. P1-P10 - bridge, identifiability, recovery, and finite data

## 6.1 Representation invariance

There exists a unique quotient bridge

\[
\bar B:\mathcal Q_P\to\mathcal Q_E
\]

with \(B=\bar B\circ\pi_P\) if and only if

\[
\boxed{
p\sim_Pp'
\Longrightarrow
B(p)=B(p').
}
\]

## 6.2 Theory identifiability

For complete theories \(\mathfrak T_1,\mathfrak T_2\), define

\[
\boxed{
\Delta_\Pi
=
\sup_{\pi\in\Pi}
\|P_1^{\pi,q}-P_2^{\pi,q}\|_{\mathrm{TV}}.
}
\]

Then

\[
\boxed{
\Delta_\Pi=0
\iff
P_1^{\pi,q}=P_2^{\pi,q}
\quad\forall\pi\in\Pi.
}
\]

With equal priors, optimal one-shot discrimination error is

\[
\boxed{
R_\pi^*
=
\frac12
\left(1-\|P_1^{\pi,q}-P_2^{\pi,q}\|_{\mathrm{TV}}\right).
}
\]

## 6.3 Physical-feature sufficiency

For proposed physical feature \(F:\mathcal Q_P\to\mathcal Z\),

\[
\boxed{
\bar B=g\circ F
\iff
F(p)=F(p')
\Longrightarrow
\bar B(p)=\bar B(p').
}
\]

A feature-matched, bridge-different pair is therefore a direct sufficiency counterexample.

## 6.4 Canonical complete bridge signature

Define

\[
p\sim_Bp'
\iff
\bar B(p)=\bar B(p'),
\]

\[
\boxed{
C_B(p)=[p]_{\sim_B}.
}
\]

Then

\[
\boxed{
C_B(p)=C_B(p')
\iff
\bar B(p)=\bar B(p').
}
\]

The strongest physical-signature target is

\[
\boxed{
F_*(p)=F_*(p')
\iff
C_B(p)=C_B(p').
}
\]

## 6.5 Robust finite-data recovery

For protocol family \(S\), define within-signature spread \(\omega_S\), between-signature separation \(\delta_S\), and

\[
\boxed{
\gamma_S=\delta_S-\omega_S.
}
\]

Under uniform total-variation estimation error \(\varepsilon\), P8 gives the sufficient exact-recovery condition

\[
\boxed{
\gamma_S>4\varepsilon.
}
\]

For the categorical benchmark, P9 gives

\[
\boxed{
n
\ge
\frac{8K^2}{\gamma_S^2}
\log\left(\frac{2N_PN_\pi K}{\alpha}\right).
}
\]

---

# 7. P11 - intervention-resolved causal structure

![Anatomy of intervention-resolved causal structure](docs/figures/causal_structure_anatomy.svg)

**Figure 6. Causal-structure anatomy.** The candidate retains response differentiation, directed causal influence, and partition-specific irreducibility rather than compressing the physics into one scalar.

Let the physical subsystem have blocks \(V=\{1,\ldots,m\}\). For intervention \(u\) and delay \(\tau\),

\[
\boxed{
P_p^{u,\tau}
=
\mathcal L(Y_{t+\tau}^{V}\mid do(u),p).
}
\]

## Response geometry

\[
\boxed{
d_p^\tau(u,v)
=
\left\|P_p^{u,\tau}-P_p^{v,\tau}\right\|_{\mathrm{TV}}.
}
\]

The family is \(\mathcal G_p\).

## Directed interventional influence

For source-pair family \(\mathcal E_i\),

\[
\boxed{
A_{ij}^{p}(\tau)
=
\sup_{(u,v)\in\mathcal E_i}
\left\|P_{p,j}^{u,\tau}-P_{p,j}^{v,\tau}\right\|_{\mathrm{TV}}.
}
\]

The full tensor is \(\mathcal A_p\).

## Partition irreducibility

For partition \(\pi\), let

\[
P_{p,\pi}^{u,\tau}
=
\bigotimes_{B\in\pi}P_{p,B}^{u,\tau}.
\]

Then

\[
\boxed{
\kappa_p^\tau(\pi)
=
\sup_u
\left\|P_p^{u,\tau}-P_{p,\pi}^{u,\tau}\right\|_{\mathrm{TV}}.
}
\]

The complete partition landscape is \(\mathcal K_p\).

The raw physical candidate is

\[
\boxed{
\mathfrak C_p
=
(V,\mathcal U_p,\mathcal T,\mathcal G_p,\mathcal A_p,\mathcal K_p),
}
\]

and its representation-independent form is

\[
\boxed{
F_{\mathrm{causal}}(p)
=
[\mathfrak C_p]_{\cong}.
}
\]

---

# 8. P12-P13 - internal minimality and no-go tests

![Proposition 12 constructive collision map](docs/figures/p12_collision_map.svg)

**Figure 7. One-component collision map.** Explicit finite response laws show that response geometry, directed influence, partition irreducibility, and several simple scalar reductions are incomplete individually.

The general collision theorem is

\[
\boxed{
H(x)=H(x')
\quad\text{and}\quad
F(x)\ne F(x')
\Longrightarrow
\nexists g\text{ with }F=g\circ H.
}
\]

![Proposition 13 pairwise component irredundancy](docs/figures/p13_component_irredundancy.svg)

**Figure 8. Pairwise irredundancy.** Every two-component projection admits a collision on the declared audit domain:

\[
(\mathcal G,\mathcal A)\text{ fixed},\quad\mathcal K\text{ changes},
\]

\[
(\mathcal G,\mathcal K)\text{ fixed},\quad\mathcal A\text{ changes},
\]

\[
(\mathcal A,\mathcal K)\text{ fixed},\quad\mathcal G\text{ changes}.
\]

These results prevent a premature reduction to a one-number consciousness score.

---

# 9. P14-P15 - temporal continuation and finite-error certification

![Proposition 14 temporal continuation](docs/figures/p14_temporal_continuation.svg)

**Figure 9. Temporal continuation.** Causal-structure states are compared after quotienting admissible relabelings.

For fingerprint \(c=(g,a,k)\), define

\[
D_w(c,c')
=
\max\left\{
w_G\|g-g'\|_\infty,
\;w_A\|a-a'\|_\infty,
\;w_K\|k-k'\|_\infty
\right\}.
\]

For finite relabeling group \(\mathcal H\),

\[
\boxed{
\overline D_w([c],[c'])
=
\min_{h\in\mathcal H}D_w(c,hc').
}
\]

Temporal path variation is

\[
\boxed{
V_{0:T}
=
\sum_{t=0}^{T-1}
\overline D_w([c_t],[c_{t+1}]).
}
\]

![Proposition 15 finite-sample temporal certification](docs/figures/p15_finite_sample_temporal_certification.svg)

**Figure 10. Finite-error temporal certification.** If

\[
D_w(c_t,\widehat c_t)\le\varepsilon_t,
\]

then

\[
\boxed{
|\widehat d_{st}-d_{st}|
\le
\varepsilon_s+\varepsilon_t.
}
\]

This produces explicit lower and upper bounds rather than forcing uncertain comparisons into binary classifications.

---

# 10. P16 - independent composition and coupling

![Proposition 16 independent composition and coupling](docs/figures/p16_composition_coupling.svg)

**Figure 11. Composition and coupling.** The independent product-response model provides a physical null model for two coexisting systems.

Define

\[
\boxed{
P_{A\otimes B}^{(u_A,u_B),\tau}
=
P_A^{u_A,\tau}\otimes P_B^{u_B,\tau}.
}
\]

For response distances

\[
d_A,
\qquad d_B,
\qquad d_{AB},
\]

P16 proves

\[
\boxed{
\max\{d_A,d_B\}
\le d_{AB}
\le d_A+d_B-d_Ad_B.
}
\]

If only one subsystem intervention changes, the corresponding response distance is preserved exactly.

For independent composition, cross-system directed influence is zero and the top-level partition factorizes:

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

For an observed joint response, define the coupling defect

\[
\boxed{
\chi_{A|B}(\tau)
=
\kappa_{AB}^{\tau}(\pi_{A|B}).
}
\]

Positive defect certifies departure from response factorization on the declared intervention-observation regime.

---

# 11. P17 - coarse-graining, refinement, and recoverability

![Proposition 17 coarse-graining and refinement](docs/figures/p17_coarse_graining_refinement.svg)

**Figure 12. Scale change.** Deterministic coarse-graining cannot create total-variation distinctions, while many-to-one maps can erase them completely.

Let

\[
C:\Omega_f\to\Omega_c
\]

be a deterministic coarse-graining map. For fine response law \(P\), define

\[
\boxed{
C_\#P(y)
=
\sum_{x:C(x)=y}P(x).
}
\]

Then P17 proves

\[
\boxed{
\|C_\#P-C_\#Q\|_{\mathrm{TV}}
\le
\|P-Q\|_{\mathrm{TV}}.
}
\]

If \(C\) is bijective on the relevant support, equality is preserved. If \(C\) is non-injective, there exist exact collision witnesses:

\[
x\ne x',
\qquad C(x)=C(x'),
\]

with

\[
\|\delta_x-\delta_{x'}\|_{\mathrm{TV}}=1
\]

but

\[
\boxed{
\|C_\#\delta_x-C_\#\delta_{x'}\|_{\mathrm{TV}}=0.
}
\]

Thus a coarse representation can make distinct intervention responses observationally identical. Refinement from the coarse law is not generally identifiable without additional physical structure.

This result is a representation-theoretic baseline for future work on genuine physical splitting and merging.

---

# 12. Candidate consciousness theories in a common interface

![Candidate theory comparison map](docs/figures/theory_comparison_map.svg)

**Figure 13. Theory comparison.** Major theory families and the repository candidate are translated into one comparison interface:

\[
\boxed{
\mathfrak T_j
=
(\mathcal F_j,\mathcal B_j,\mathcal M_j,\Pi_j).
}
\]

| Theory family | Physical feature family | Bridge style | Empirical exposure |
| --- | --- | --- | --- |
| **IIT 4.0** | intrinsic cause-effect structure, maximal substrate, distinctions and relations | phenomenal axioms to physical postulates | transition / causal structure and perturbational model |
| **GNWT** | multilevel workspace organization, ignition, amplification, long-range availability | conscious access/content associated with workspace dynamics | timing, report, long-range and multilevel neural dynamics |
| **RPT** | recurrent processing in relevant neural circuits | recurrence proposed as central to phenomenal processing | local temporal disruption and recurrent interactions |
| **Higher-order** | theory-specific higher-order representational relation | state is conscious in virtue of a higher-order relation | first-order / higher-order dissociation |
| **Predictive / neurorepresentational / active-inference families** | hierarchical prediction, inference, precision, multimodal representation | heterogeneous, theory-specific bridge | prediction, precision, representation, hierarchical perturbation |
| **Repository causal-structure candidate** | intervention-resolved response geometry, directed influence, partition landscape, temporal trajectory, composition and scale behavior | experiential bridge not supplied by the physical construction | controlled perturbation, counterexamples, recovery, temporal, composition, scale and substrate tests |

The comparison is not a ranking. P2-P6 provide exact mathematical questions about identifiability, sufficiency, and completeness.

---

# 13. Empirical consciousness measurement

The physical candidate is motivated by empirical work but is not identified with any one published index.

## 13.1 Perturbational complexity

Casali et al. developed a perturbational complexity approach using controlled cortical stimulation and distributed EEG response across conscious and unconscious conditions.

**Source:** Casali et al., *Science Translational Medicine* 5(198) (2013), 198ra105. DOI `10.1126/scitranslmed.3006294`.

## 13.2 Critical dynamics

Maschke et al. reported relationships among spontaneous EEG critical dynamics, anesthesia-induced loss of consciousness, and perturbational complexity.

**Source:** Maschke et al., *Communications Biology* 7 (2024): 946. DOI `10.1038/s42003-024-06613-8`.

## 13.3 Synergistic information integration

Luppi et al. used Integrated Information Decomposition to study a synergistic workspace whose organization changes across conscious-state conditions.

**Source:** Luppi et al., *eLife* 12 (2024): RP88173. DOI `10.7554/eLife.88173`.

## 13.4 Adversarial theory testing

The Cogitate Consortium compared key predictions of Global Neuronal Workspace Theory and Integrated Information Theory using fMRI, MEG, and intracranial EEG.

**Source:** Cogitate Consortium et al., *Nature* 642 (2025): 133-142. DOI `10.1038/s41586-025-08888-1`.

---

# 14. Spaceflight and extreme-environment research

![Spaceflight and extreme-environment relevance map](docs/figures/spaceflight_extreme_environment_map.svg)

**Figure 14. Extreme-environment map.** Spaceflight is included as a demanding validation environment for cognition, physiology, temporal state estimation, and human-system monitoring.

The relevant stressor structure includes

\[
\boxed{
\text{altered gravity}
+
\text{radiation}
+
\text{sleep/circadian disruption}
+
\text{isolation}
+
\text{workload}.
}
\]

NASA's Human Research Program studies health and performance risks associated with human spaceflight. Its Human Factors and Behavioral Performance program addresses behavioral health, sleep, cognitive function, team performance, human-robotic interaction, and mission-readiness issues relevant to Moon, Mars, and deep-space exploration.

Authoritative resources:

- [NASA Human Research Program](https://www.nasa.gov/hrp/)
- [NASA Human Factors and Behavioral Performance](https://www.nasa.gov/reference/about-human-factors-and-behavioral-performance/)
- [NASA HFBP Spaceflight Risks](https://www.nasa.gov/hrp/human-factors-and-behavioral-performance/hfbp-risks/)
- [NASA Sleep, Circadian Desynchronization, and Work Overload Risk](https://www.nasa.gov/directorates/esdmd/hhp/risk-of-performance-decrements-and-adverse-health-outcomes-resulting-from-sleep-loss-circadian-desynchronization-and-work-overload/)
- [NASA ARCHeR - Artemis Research for Crew Health & Readiness](https://www.nasa.gov/reference/archer/)

The role of this layer is **robustness testing and application**, not independent evidence for a consciousness bridge.

---

# 15. Relationship to Spatiotemporal Observer Mathematics

The two repositories form one research sequence:

```text
physical measurements
        |
        v
effective dynamical model
        |
        v
certified persistent moving subsystem
        |
        |  Spatiotemporal Observer Mathematics
        v
physical equivalence class [p]
        |
        v
intervention-resolved causal structure
        |
        v
temporal continuation + finite-error certification
        |
        v
composition + coupling + scale analysis
        |
        v
candidate physical-to-experiential bridge
        |
        v
empirical discrimination / falsification
```

The companion repository supplies candidate world-tubes

\[
\mathcal W=(S_0,\ldots,S_{T-1}),
\]

with recovery, identifiability, temporal calibration, and finite-sample certification. This repository develops the subsequent causal, temporal, compositional, scale, and bridge program.

**Foundation repository:** [MahsaKeikha/spatiotemporal-observer-math](https://github.com/MahsaKeikha/spatiotemporal-observer-math)

---

# 16. Evidence and claim hierarchy

| Status | Meaning |
| --- | --- |
| **Definition** | mathematical object introduced by the framework |
| **Proved** | theorem derived from explicit assumptions |
| **Identifiability / no-go result** | theorem about what observations, projections, or scale transformations can or cannot determine |
| **Candidate physical signature** | physical structure proposed for testing, not an experiential conclusion |
| **Finite-error certificate** | conclusion guaranteed under explicitly declared estimation-error bounds |
| **Empirical result** | evidence reported by a cited experiment or dataset |
| **Application domain** | environment in which physical or cognitive markers may be stress-tested |
| **Counterexample** | explicit construction defeating a sufficiency, compression, recoverability, or scale-preservation claim |
| **Open bridge problem** | unresolved relation between physical and experiential equivalence structure |

---

# 17. Falsification program

A candidate bridge or physical signature is exposed to several failure classes.

## Representation failure

\[
p\sim_Pp'
\quad\text{but}\quad
F(p)\ne F(p').
\]

## Feature-sufficiency failure

\[
F(p)=F(p')
\quad\text{but}\quad
\bar B(p)\ne\bar B(p').
\]

## Observational identifiability failure

\[
\Delta_\Pi=0.
\]

## Experimental-recoverability failure

\[
\Psi_\Pi(p)=\Psi_\Pi(p')
\quad\text{but}\quad
F_*(p)\ne F_*(p').
\]

## Compression failure

P12-P13 give explicit projection collisions.

## Temporal failure

P14 shows that equal endpoints can conceal nonzero path variation. P15 prevents finite-error uncertainty from being hidden by forced classification.

## Composition failure

P16 supplies the independent-composition null model. Any proposed higher-level theory must distinguish mere coexistence from cross-system coupling.

## Scale failure

P17 shows that coarse-graining can erase distinctions. A bridge theory must therefore state which physical scale is relevant and how information lost under coarse-graining affects its claims.

[Read the complete falsification program](docs/falsification_program.md).

---

# 18. Scholarly lineage

The repository maintains source-role separation.

## Physics and mathematics

- Shannon 1948 - information theory.
- Cover and Thomas 2006 - information-theoretic foundations.
- Amari 2016 - information geometry.
- Ay, Jost, Le, and Schwachhofer 2017 - rigorous statistical-manifold geometry.
- Landauer 1961 - thermodynamics of logically irreversible information processing.
- Seifert 2012 - stochastic thermodynamics.
- Pearl 2009 - causal intervention and structural causal models.
- Le Cam and Yang 2000 - statistical experiment and decision theory.
- Tsybakov 2009 - minimax testing and nonparametric inference.
- Hoeffding 1963 - finite-sample concentration.
- Burago, Burago, and Ivanov 2001 - metric geometry.

## Mathematical and theoretical consciousness

- Tegmark 2015 - physical factorization and state-of-matter perspective.
- Tononi 2004; Albantakis et al. 2023 - integrated information theory.
- Dehaene and Changeux 2011; Mashour et al. 2020 - global neuronal workspace.
- Lamme 2006 - recurrent processing.
- Brown, Lau, and LeDoux 2019 - higher-order approaches.
- Seth and Bayne 2022 - major theory comparison.
- Kleiner 2019; Kleiner and Tull 2020 - mathematical consciousness formalisms.
- Doerig et al. 2019 - unfolding and empirical identifiability challenge.
- Cogitate Consortium et al. 2025 - adversarial theory testing.

## Empirical consciousness science

- Casali et al. 2013 - perturbational complexity.
- Maschke et al. 2024 - critical dynamics and anesthesia.
- Luppi et al. 2024 - synergistic information integration.
- Luppi et al. 2026 - integration, controllability, and anesthesia across mammalian brains.

For complete source roles, see:

- [Literature Map](docs/literature_map.md)
- [Foundational Physics, Mathematics, and Spaceflight Bibliography](docs/foundational_physics_mathematics_bibliography.md)
- [Equation and Citation Map](docs/equation_and_citation_map.md)
- [`references.bib`](references.bib)

---

# 19. Research record

| Research record | Current state |
| --- | ---: |
| proposition-level results | **17** |
| original structured physical candidate | **1 - intervention-resolved causal structure** |
| universal-proof criteria | **12** |
| current collected test suite | **99 tests before the latest documentation-only atlas additions** |
| canonical visual research figures | **14** |
| CI matrix | **Python 3.10, 3.11, 3.12** |
| research-software version | **0.17.0** |

The current research-software release includes bridge mathematics, empirical identifiability, finite-data recovery, candidate-structure construction, minimality audits, temporal continuation, composition/coupling, and coarse-graining/refinement theorems.

---

# 20. Reproducibility and audit path

```bash
python -m pip install -e ".[dev]"
pytest
ruff check .
```

The code audits:

- representation invariance;
- theory discriminability and optimal binary testing;
- observational theory-equivalence classes;
- maximin and set-cover experiment design;
- physical-feature sufficiency and canonical bridge signatures;
- experimental recoverability;
- finite-error partition recovery;
- explicit categorical sample complexity;
- robust protocol-family optimization;
- intervention-response geometry;
- partition-product models and irreducibility;
- directed perturbational influence and cycle detection;
- one-component and pairwise projection collisions;
- quotient temporal metrics and temporal path variation;
- finite-error temporal certification;
- independent product-response composition;
- cross-system influence and coupling defects;
- deterministic coarse-graining and pushforward laws;
- total-variation contraction and refinement collisions;
- documentation-link integrity;
- publication-style figure quality and terminology consistency.

The repository structure guard protects P1-P17, the physics/mathematics atlas, the foundational bibliography, and all canonical visual assets.

---

# 21. Current frontier

P16 establishes the independent-composition null model. P17 establishes the representation-theoretic baseline for scale change. The next frontier is therefore more physical and more demanding:

1. **genuine splitting and merging dynamics** - distinguish descriptive coarse-graining from a physical change in dynamics, state space, and intervention channels;
2. **observer-to-causal-structure interface** - connect certified moving world-tubes from the companion repository directly to time-indexed intervention-response systems;
3. **estimator-specific concentration** - derive finite-sample radii for the actual response-geometry, directed-influence, and irreducibility estimators;
4. **irregular physical time** - normalize structural path variation by physical cadence and continuous-time limits;
5. **thermodynamic constraints** - connect candidate physical structure to measurable energy flow, entropy production, and nonequilibrium organization without assuming a bridge conclusion;
6. **information-geometric structure** - determine whether the family of intervention-conditioned laws admits useful invariant manifold geometry beyond total variation;
7. **cross-theory adversarial experiments** - design protocols that maximize empirical separation among IIT, GNWT, recurrent-processing, higher-order, predictive/neurorepresentational, and repository candidate families;
8. **clinical and extreme-environment testing** - evaluate robustness across anesthesia, sleep, disorders of consciousness, cognitive stress, and spaceflight-relevant perturbations;
9. **biological and artificial counterexamples** - search actively for systems matching rich physical causal structure while differing in the relevant experiential evidence;
10. **experiential formalization** - sharpen \(\mathcal Q_E\), experiential invariances, and candidate bridge axioms independently of the physical candidate;
11. **bridge theorem** - pursue a final conditional implication only after the physical, experiential, identifiability, finite-data, composition, scale, and falsification layers are jointly explicit.

The current mathematical research chain is

\[
\boxed{
\text{controlled physical response}
\longrightarrow
\text{intervention-resolved causal structure}
\longrightarrow
\text{representation-invariant temporal trajectory}
\longrightarrow
\text{finite-error certification}
\longrightarrow
\text{composition and coupling}
\longrightarrow
\text{scale-change analysis}.
}
\]

The next scientific problem is to determine what additional independently justified structure is required to connect that physical chain to a formal experiential domain.