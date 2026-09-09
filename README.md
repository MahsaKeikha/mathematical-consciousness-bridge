# Mathematical Consciousness Bridge

[![tests](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/test.yml/badge.svg)](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/test.yml)
[![version](https://img.shields.io/badge/version-0.15.0-2563eb)](CITATION.cff)
[![license](https://img.shields.io/badge/license-MIT-059669)](LICENSE)

**Mahsa Keikha, PhD**

> **What mathematical and physical conditions would be required for a physical description of a system to support a scientifically testable claim about consciousness?**

This repository develops a formal mathematical-physics program for the **consciousness bridge problem**: connecting physical organization to formal experiential structure through explicit bridge principles, theorem-level consequences, empirical identifiability, controlled intervention, finite-data certification, temporal structure, and falsification.

The program builds on, but remains logically distinct from, [Spatiotemporal Observer Mathematics](https://github.com/MahsaKeikha/spatiotemporal-observer-math), which studies whether a persistent moving subsystem can be inferred and certified from dynamics. That companion project can supply a candidate physical subsystem. The present project studies the additional physical-to-experiential bridge.

---

## Visual overview

![Mathematical Consciousness Bridge research architecture](docs/figures/research_architecture.svg)

**Figure 1. Research architecture.** Physics, representation-independent physical structure, candidate physical signatures, bridge principles, experiential structure, observable predictions, finite-data certification, and falsification are treated as distinct scientific layers.

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

The mathematical implication must be proved from explicit premises. The bridge premises must also generate consequences that can be tested against serious alternatives.

---

# Start here

| Reader goal | Entry point |
| --- | --- |
| See the whole program visually | **[Visual Research Guide](docs/visual_research_guide.md)** |
| Understand the strongest proof target | **[Universal Consciousness Proof Target](docs/universal_proof_target.md)** |
| Understand the physical input | **[Physical Foundation](docs/physical_foundation.md)** |
| Read the exact bridge problem | **[Consciousness Bridge Problem](docs/bridge_problem.md)** |
| Follow the theorem dependency chain | **[Theorem Roadmap](docs/theorem_roadmap.md)** |
| Read the original physical candidate | **[P11 - Intervention-Resolved Causal Structure](docs/proposition_11_intervention_resolved_causal_structure.md)** |
| Read the single-component no-go result | **[P12 - Component Insufficiency](docs/proposition_12_component_insufficiency.md)** |
| Read the pairwise irredundancy result | **[P13 - Pairwise Component Irredundancy](docs/proposition_13_pairwise_component_irredundancy.md)** |
| Read the temporal continuation theorem | **[P14 - Temporal Continuation](docs/proposition_14_temporal_continuation.md)** |
| Read the finite-sample temporal certificate | **[P15 - Finite-Sample Temporal Certification](docs/proposition_15_finite_sample_temporal_certification.md)** |
| Compare major consciousness theories | [Candidate Theory Families](docs/candidate_theory_families.md) |
| Audit equation provenance | [Equation and Citation Map](docs/equation_and_citation_map.md) |
| Inspect falsification criteria | [Falsification Program](docs/falsification_program.md) |
| Trace the literature | [Literature Map](docs/literature_map.md) |
| Read machine-readable references | [`references.bib`](references.bib) |
| Cite the program | [`CITATION.cff`](CITATION.cff) |

---

# Abstract

A physical theory can specify states, dynamics, interventions, causal response laws, and observable probability distributions without specifying why any physical organization should correspond to subjective experience. A mathematical theory of consciousness therefore requires an additional object: a bridge from physically meaningful equivalence classes to formally defined experiential equivalence classes.

This repository makes that bridge itself the object of mathematics. Propositions 1-10 establish representation invariance, exact theory identifiability, observational equivalence classes, discriminating experiment design, physical-feature sufficiency, canonical bridge completeness, experimental recoverability, robust finite-error recovery, explicit sample complexity, and robust protocol design.

Proposition 11 introduces the first original candidate physical signature: **intervention-resolved causal structure**. It is not a scalar. It retains the structure of controlled perturbational response through three complementary objects:

\[
\boxed{
\mathcal G_p
\quad\text{response geometry},
\qquad
\mathcal A_p
\quad\text{directed interventional influence},
\qquad
\mathcal K_p
\quad\text{partition irreducibility}.
}
\]

Proposition 12 proves constructively that no one of these components, and several natural scalar reductions, can reconstruct the full physical candidate on explicit finite domains. Proposition 13 strengthens this by proving that **no pair of the three components can reconstruct the omitted component** on a declared finite audit domain.

Proposition 14 turns the candidate from a sequence of disconnected snapshots into a representation-invariant temporal object. It defines a metric on causal-structure fingerprints, quotients physically irrelevant relabelings, and proves path-variation and endpoint bounds. Proposition 15 then propagates finite fingerprint uncertainty through that temporal geometry and gives explicit lower/upper confidence bounds for pairwise change, cumulative variation, and maximum local jumps.

The present record therefore separates:

1. **proved mathematical structure** - P1-P15;
2. **candidate physical structure** - intervention-resolved causal structure and its temporal trajectory;
3. **finite-error experimental certification** - P8-P10 and P15 under explicit assumptions;
4. **open bridge problem** - determining whether an independently justified physical equivalence structure can be connected to formal experiential equivalence and survive competing-theory, cross-substrate, temporal, compositional, and empirical tests.

---

# 1. The scientific problem

The program studies the chain

```text
physical realization
        |
        v
physical equivalence class
        |
        v
candidate physical signature
        |
        v
explicit bridge principles
        |
        v
experiential equivalence class
        |
        v
observable predictions
        |
        v
finite-data certification
        |
        v
empirical discrimination / falsification
```

Mathematically,

\[
\boxed{
\text{physical system}
\longrightarrow
\text{mathematical structure}
\longrightarrow
\text{bridge principles}
\longrightarrow
\text{experiential claim}.
}
\]

The central difficulty is the third arrow. Integration, complexity, recurrence, global broadcasting, causal structure, criticality, subsystem persistence, or temporal smoothness can all be mathematically meaningful without yet constituting a bridge to experience.

---

# 2. Physical foundation

A physical input is modeled abstractly as

\[
\boxed{
p=(\mathcal X,\mathcal D,\mathfrak I,\mathcal O),
}
\]

where

| Object | Physical role |
| --- | --- |
| \(\mathcal X\) | physical state space |
| \(\mathcal D\) | deterministic or stochastic dynamics |
| \(\mathfrak I\) | admissible intervention class |
| \(\mathcal O\) | observable / measurement map |

A deterministic continuous-time realization may be written

\[
\dot x(t)=F(x(t),u(t)),
\qquad
y(t)=h(x(t)),
\]

while a stochastic realization may take the form

\[
dX_t=f(X_t,u_t)\,dt+G(X_t,u_t)\,dW_t,
\]

or

\[
X_{t+\Delta t}
\sim
K_{\Delta t}(\cdot\mid X_t,u_t).
\]

The bridge must state which physical level is primitive and which interventions are physically admissible.

## 2.1 Physical representation equivalence

If

\[
z=\varphi(x)
\]

is only an invertible change of physical coordinates, then

\[
\dot z
=
D\varphi(x)F(x,u),
\qquad
x=\varphi^{-1}(z),
\]

represents the same underlying realization. We therefore introduce

\[
\boxed{
p\sim_Pp'
}
\]

and the physical quotient

\[
\boxed{
\mathcal Q_P
=
\mathcal P/{\sim_P}.
}
\]

A physically meaningful signature should ultimately operate on \(\mathcal Q_P\), not on arbitrary coordinate descriptions.

---

# 3. Experiential domain and bridge

Let

\[
\mathcal E
\]

be a formal space of candidate experiential structures, with experiential equivalence

\[
e\sim_Ee'.
\]

Define

\[
\boxed{
\mathcal Q_E
=
\mathcal E/{\sim_E}.
}
\]

A general starting bridge is a relation

\[
\boxed{
\mathcal B
\subseteq
\mathcal P\times\mathcal E.
}
\]

When single-valuedness and representation invariance are justified, the target quotient-level bridge is

\[
\boxed{
\bar B:
\mathcal Q_P
\longrightarrow
\mathcal Q_E.
}
\]

A complete empirical theory must also specify its measurement model and experiment class. The repository therefore uses

\[
\boxed{
\mathfrak T
=
(\mathcal P,\mathcal E,\sim_P,\sim_E,\mathcal B,\mathcal M,\Pi).
}
\]

---

# 4. Universal proof target

![Universal consciousness proof criteria](docs/figures/universal_proof_ladder.svg)

**Figure 2. Universal proof ladder.** The final target is decomposed into distinct mathematical, physical, empirical, and finite-data requirements.

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
| U10 | finite-measurement certification | P8 + P15 temporal extension |
| U11 | explicit sample complexity | P9 + restricted P15 bounded-coordinate corollary |
| U12 | temporal, compositional, substrate, and falsification consistency | temporal layer P14-P15; composition/substrate still active frontier |

A strong conditional theorem would have the form

\[
\boxed{
\begin{aligned}
& p\in\mathcal Q_P,\\
& A_1,\ldots,A_k\text{ bridge principles hold},\\
& F_*(p)\text{ is a complete physical signature},\\
& \widehat F_*(p)\text{ is recovered with declared confidence},\\
& V_1,\ldots,V_r\text{ discriminating validation conditions hold}
\\[2mm]
&\qquad\Longrightarrow
\bar B(p)\in\mathcal C_E.
\end{aligned}
}
\]

A stronger biconditional target is

\[
\boxed{
\bar B(p)\in\mathcal C_E
\iff
F_*(p)\in\mathcal R_C.
}
\]

Both directions require independent justification.

---

# 5. Theorem roadmap: P1-P15

![Propositions 1 through 15 theorem roadmap](docs/figures/theorem_roadmap.svg)

**Figure 3. Theorem dependency map.** P1-P10 establish the general bridge and finite-data machinery. P11 introduces the physical candidate. P12-P13 test internal compression. P14 establishes representation-invariant temporal continuation. P15 propagates finite fingerprint uncertainty through that temporal geometry.

| Proposition | Core result | Status | Full proof |
| --- | --- | --- | --- |
| **P1** | representation-invariant bridges descend to physical quotient classes | Proved | [P1](docs/proposition_1_representation_invariance.md) |
| **P2** | exact experiment-class bridge identifiability and TV discrimination | Proved | [P2](docs/proposition_2_bridge_identifiability.md) |
| **P3** | observational bridge-equivalence classes and theory quotient | Proved | [P3](docs/proposition_3_bridge_equivalence_classes.md) |
| **P4** | maximin / set-cover discriminating experiment design | Proved | [P4](docs/proposition_4_discriminating_experiment_design.md) |
| **P5** | exact physical-feature sufficiency criterion | Proved | [P5](docs/proposition_5_feature_sufficiency.md) |
| **P6** | canonical complete bridge signature | Proved | [P6](docs/proposition_6_canonical_bridge_signature.md) |
| **P7** | exact experimental recoverability criterion | Proved | [P7](docs/proposition_7_experimental_signature_recovery.md) |
| **P8** | robust finite-error signature recovery | Proved | [P8](docs/proposition_8_robust_signature_recovery.md) |
| **P9** | explicit categorical sample-complexity guarantee | Proved | [P9](docs/proposition_9_categorical_sample_complexity.md) |
| **P10** | robust experiment design for signature recovery | Proved | [P10](docs/proposition_10_robust_experiment_design.md) |
| **P11** | intervention-resolved causal structure + structural certificates | Proved construction / candidate | [P11](docs/proposition_11_intervention_resolved_causal_structure.md) |
| **P12** | single-component insufficiency and scalar collision theorems | Proved no-go / minimality result | [P12](docs/proposition_12_component_insufficiency.md) |
| **P13** | all three pairwise component projections are incomplete on an explicit audit domain | Proved irredundancy result | [P13](docs/proposition_13_pairwise_component_irredundancy.md) |
| **P14** | quotient metric, temporal path variation, relabeling invariance, endpoint bound | Proved temporal-structure theorem | [P14](docs/proposition_14_temporal_continuation.md) |
| **P15** | finite-error bounds for temporal distance, path variation, and maximum jump | Proved certification theorem | [P15](docs/proposition_15_finite_sample_temporal_certification.md) |

---

# 6. P1 - representation invariance

Let

\[
B:\mathcal P\to\mathcal Q_E
\]

be a bridge assignment and \(\pi_P:\mathcal P\to\mathcal Q_P\) the quotient projection.

There exists a unique

\[
\bar B:\mathcal Q_P\to\mathcal Q_E
\]

with

\[
B=\bar B\circ\pi_P
\]

if and only if

\[
\boxed{
p\sim_Pp'
\Longrightarrow
B(p)=B(p').
}
\]

This prevents arbitrary coordinates, units, labels, or equivalent encodings from changing the bridge assignment.

---

# 7. P2-P4 - theory identifiability and discriminating experiments

For complete theory \(\mathfrak T_i\), protocol \(\pi\), and physical input \(q\), let

\[
P_i^{\pi,q}
\]

be the predicted observable law.

Define total variation

\[
\boxed{
\|P-Q\|_{\mathrm{TV}}
=
\sup_A|P(A)-Q(A)|.
}
\]

## P2 - experiment-class discriminability

\[
\boxed{
\Delta_\Pi(\mathfrak T_1,\mathfrak T_2;q)
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

With equal priors, the optimal one-shot theory-discrimination error is

\[
\boxed{
R_\pi^*
=
\frac12
\left(1-\|P_1^{\pi,q}-P_2^{\pi,q}\|_{\mathrm{TV}}\right).
}
\]

## P3 - observational theory quotient

Define

\[
\boxed{
\Phi_{\Pi,q}(\mathfrak T)
=
(P_{\mathfrak T}^{\pi,q})_{\pi\in\Pi}.
}
\]

Then

\[
\boxed{
\Theta/{\sim_{\Pi,q}}
\cong
\operatorname{Im}(\Phi_{\Pi,q}).
}
\]

The empirically identifiable object may therefore be an equivalence class of theories rather than one named theory.

## P4 - experiment design

For theory pair \(i,j\),

\[
d_{ij}(\pi)
=
\|P_i^{\pi,q}-P_j^{\pi,q}\|_{\mathrm{TV}}.
\]

For protocol family \(S\),

\[
U(S)
=
\min_{\{i,j\}\in\mathcal U}
\max_{\pi\in S}d_{ij}(\pi).
\]

Then

\[
\boxed{
U(S)>0
\iff
\bigcup_{\pi\in S}C_\pi=\mathcal U.
}
\]

Finite complete theory discrimination therefore becomes a set-cover problem over distinguishable theory pairs.

---

# 8. P5-P6 - physical-feature sufficiency and completeness

Suppose

\[
F:\mathcal Q_P\to\mathcal Z
\]

is a proposed physical feature.

## P5 - exact sufficiency criterion

\[
\boxed{
\bar B=g\circ F
\iff
F(p)=F(p')
\Longrightarrow
\bar B(p)=\bar B(p').
}
\]

One pair with equal feature values but different bridge classes directly refutes sufficiency on the declared domain.

## P6 - canonical complete bridge signature

Define

\[
p\sim_Bp'
\iff
\bar B(p)=\bar B(p')
\]

and

\[
\boxed{
C_B(p)
=
[p]_{\sim_B}.
}
\]

Then

\[
\boxed{
C_B(p)=C_B(p')
\iff
\bar B(p)=\bar B(p'),
}
\]

and

\[
\boxed{
\mathcal Q_B
\cong
\operatorname{Im}(\bar B).
}
\]

The strongest physical-signature target is therefore

\[
\boxed{
F_*(p)=F_*(p')
\iff
C_B(p)=C_B(p').
}
\]

---

# 9. P7-P10 - recovery, finite data, and experiment design

For experiment family \(\Pi\), define

\[
\boxed{
\Psi_\Pi(p)
=
(P^{\pi,p})_{\pi\in\Pi}.
}
\]

## P7 - recoverability

A target physical signature \(F_*\) is recoverable when

\[
\boxed{
\Psi_\Pi(p)=\Psi_\Pi(p')
\Longrightarrow
F_*(p)=F_*(p').
}
\]

## P8 - robust finite-error recovery

For protocol family \(S\), define

\[
d_S(p,p')
=
\max_{\pi\in S}
\|P^{\pi,p}-P^{\pi,p'}\|_{\mathrm{TV}}.
\]

Let

\[
\omega_S
=
\max_{F_*(p)=F_*(p')}d_S(p,p')
\]

and

\[
\delta_S
=
\min_{F_*(p)\ne F_*(p')}d_S(p,p').
\]

The robust signature gap is

\[
\boxed{
\gamma_S
=
\delta_S-\omega_S.
}
\]

If uniform estimation error is at most \(\varepsilon\), exact partition recovery is guaranteed under the theorem when

\[
\boxed{
\gamma_S>4\varepsilon.
}
\]

## P9 - explicit sample complexity

For \(N_P\) physical systems, \(N_\pi\) protocols, at most \(K\) categorical outcomes, confidence target \(1-\alpha\), and \(n\) IID repetitions per cell, a sufficient condition is

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

## P10 - robust protocol design

Define

\[
\boxed{
\Gamma(S)
=
\delta(S)-\omega(S).
}
\]

For newly added protocol \(\rho\),

\[
\boxed{
\Gamma(S\cup\{\rho\})-\Gamma(S)
=
a_\rho(S)-b_\rho(S).
}
\]

Hence an added measurement helps exactly when its between-signature gain exceeds its within-signature inflation.

---

# 10. P11 - intervention-resolved causal structure

![Anatomy of the intervention-resolved causal structure](docs/figures/causal_structure_anatomy.svg)

**Figure 4. Causal-structure anatomy.** The physical candidate is deliberately structured rather than reduced to one complexity, integration, or recurrence score.

## 10.1 Controlled response laws

Let the physical subsystem be divided into blocks

\[
V=\{1,\ldots,m\}.
\]

For admissible intervention \(u\in\mathcal U_p\) and physical delay \(\tau\in\mathcal T\), define

\[
\boxed{
P_p^{u,\tau}
=
\mathcal L\!\left(Y_{t+\tau}^{V}\mid do(u),p\right).
}
\]

The \(do(u)\) notation distinguishes controlled causal intervention from passive correlation.

## 10.2 Response geometry

\[
\boxed{
d_p^\tau(u,v)
=
\left\|P_p^{u,\tau}-P_p^{v,\tau}\right\|_{\mathrm{TV}}.
}
\]

The family

\[
\boxed{
\mathcal G_p
=
\{d_p^\tau:\tau\in\mathcal T\}
}
\]

records intervention-dependent response differentiation through physical time.

## 10.3 Directed interventional influence

Let \(\mathcal E_i\) contain intervention pairs differing only at source block \(i\). Define

\[
\boxed{
A_{ij}^{p}(\tau)
=
\sup_{(u,v)\in\mathcal E_i}
\left\|
P_{p,j}^{u,\tau}
-
P_{p,j}^{v,\tau}
\right\|_{\mathrm{TV}}.
}
\]

The tensor

\[
\boxed{
\mathcal A_p
=
\{A_{ij}^{p}(\tau)\}_{i,j,\tau}
}
\]

records the strength, direction, and timing of perturbational influence.

## 10.4 Partition response irreducibility

For partition

\[
\pi=\{B_1,\ldots,B_k\},
\]

define

\[
P_{p,\pi}^{u,\tau}
=
\bigotimes_{r=1}^{k}P_{p,B_r}^{u,\tau}
\]

and

\[
\boxed{
\kappa_p^\tau(\pi)
=
\sup_{u\in\mathcal U_p}
\left\|
P_p^{u,\tau}
-
P_{p,\pi}^{u,\tau}
\right\|_{\mathrm{TV}}.
}
\]

The complete landscape is

\[
\boxed{
\mathcal K_p
=
\left\{
\kappa_p^\tau(\pi)
:
\pi\in\mathfrak P(V),\tau\in\mathcal T
\right\}.
}
\]

## 10.5 Full physical candidate

Define

\[
\boxed{
\mathfrak C_p
=
(V,\mathcal U_p,\mathcal T,\mathcal G_p,\mathcal A_p,\mathcal K_p).
}
\]

After quotienting compatible relabelings and response-space reparameterizations,

\[
\boxed{
F_{\mathrm{causal}}(p)
=
[\mathfrak C_p]_{\cong}.
}
\]

The strongest candidate-completeness target is

\[
\boxed{
F_{\mathrm{causal}}(p)
=
F_{\mathrm{causal}}(p')
\iff
C_B(p)=C_B(p').
}
\]

This is an open target, not an assumption.

## 10.6 What P11 proves

P11 establishes:

1. representation invariance under compatible physical reparameterization;
2. exact partition-factorization certificate
   \[
   \boxed{
   \kappa_p^\tau(\pi)=0
   \iff
   P_p^{u,\tau}
   =
   \bigotimes_{B\in\pi}P_{p,B}^{u,\tau}
   \quad\forall u;
   }
   \]
3. feedforward no-return certificate: an acyclic aggregated directed-influence graph cannot contain a causal return loop through distinct blocks.

---

# 11. P12 - why one-component and scalar reductions fail

![Proposition 12 constructive collision map](docs/figures/p12_collision_map.svg)

**Figure 5. Constructive collision map.** Explicit realizable response laws show which information is lost by one-component compression.

Let \(F:X\to Z\) be a target signature and \(H:X\to W\) a compression. If

\[
\boxed{
H(x)=H(x')
\qquad\text{but}\qquad
F(x)\ne F(x'),
}
\]

then no map \(g\) satisfies \(F=g\circ H\) throughout that domain.

P12 constructs three key collisions:

### Same response geometry, different partition structure

\[
\mathcal G_C=\mathcal G_P,
\qquad
d_C(u_0,u_1)=d_P(u_0,u_1)=1,
\]

but

\[
\boxed{
\kappa_C^\tau(\pi)=\frac12,
\qquad
\kappa_P^\tau(\pi)=0.
}
\]

### Same partition landscape, different response geometry

\[
\boxed{
\mathcal K_D=\mathcal K_S,
\qquad
\mathcal G_D\ne\mathcal G_S.
}
\]

### Same directed marginal influence, different joint response geometry

\[
\boxed{
\mathcal A_R=\mathcal A_I,
\qquad
\mathcal G_R\ne\mathcal G_I.
}
\]

The theorem also gives explicit collisions for

\[
\operatorname{Diam}_p(\tau),
\qquad
\kappa_p^*,
\qquad
\mathbf 1\{\text{directed cycle exists}\}.
\]

Thus response diameter, one scalar irreducibility value, or a recurrence yes/no flag cannot reconstruct the full physical candidate.

---

# 12. P13 - pairwise component irredundancy

![Proposition 13 pairwise component irredundancy](docs/figures/p13_component_irredundancy.svg)

**Figure 6. Pairwise irredundancy.** Every two-component projection has an explicit collision on the declared finite audit domain.

Let

\[
F_C(p)
=
(\mathcal G_p,\mathcal A_p,\mathcal K_p).
\]

Define

\[
H_{GA}(p)=(\mathcal G_p,\mathcal A_p),
\]

\[
H_{GK}(p)=(\mathcal G_p,\mathcal K_p),
\]

\[
H_{AK}(p)=(\mathcal A_p,\mathcal K_p).
\]

P13 constructs three families:

\[
\boxed{
\mathcal G_L=\mathcal G_H,
\quad
\mathcal A_L=\mathcal A_H,
\quad
\mathcal K_L\ne\mathcal K_H,
}
\]

\[
\boxed{
\mathcal G_0=\mathcal G_+,
\quad
\mathcal K_0=\mathcal K_+,
\quad
\mathcal A_0\ne\mathcal A_+,
}
\]

and

\[
\boxed{
\mathcal A_D=\mathcal A_S,
\quad
\mathcal K_D=\mathcal K_S,
\quad
\mathcal G_D\ne\mathcal G_S.
}
\]

Therefore

\[
\boxed{
H_{GA},
\quad
H_{GK},
\quad
H_{AK}
\text{ are all incomplete on }D_{13}.
}
\]

Equivalently, each of the three major components is irredundant relative to the other two on the declared domain:

\[
\boxed{
\mathcal G
\not\preceq
(\mathcal A,\mathcal K),
\qquad
\mathcal A
\not\preceq
(\mathcal G,\mathcal K),
\qquad
\mathcal K
\not\preceq
(\mathcal G,\mathcal A).
}
\]

This does not prove that the chosen representation is globally minimal on every physical domain. It proves that none of the three components can simply be dropped without loss on the explicit audit domain.

---

# 13. P14 - representation-invariant temporal continuation

![Proposition 14 temporal continuation](docs/figures/p14_temporal_continuation.svg)

**Figure 7. Temporal continuation.** Causal-structure fingerprints are compared after quotienting physically irrelevant relabelings, and continuation is treated as a path property rather than an endpoint similarity score.

For a finite fingerprint

\[
c=(g,a,k),
\]

define the weighted metric

\[
\boxed{
D_w(c,c')
=
\max\left\{
w_G\|g-g'\|_\infty,
w_A\|a-a'\|_\infty,
w_K\|k-k'\|_\infty
\right\}.
}
\]

Let \(\mathcal H\) be a finite declared group of admissible relabelings acting by isometries. P14 proves that

\[
\boxed{
\overline D_w([c],[c'])
=
\min_{h\in\mathcal H}D_w(c,hc')
}
\]

is a metric on the orbit space.

For a temporal path \([c_0],\ldots,[c_T]\), define

\[
\boxed{
V_{0:T}
=
\sum_{t=0}^{T-1}
\overline D_w([c_t],[c_{t+1}])
}
\]

and

\[
\boxed{
J_{0:T}
=
\max_t
\overline D_w([c_t],[c_{t+1}]).
}
\]

P14 proves

\[
\boxed{
\overline D_w([c_s],[c_t])
\le
V_{s:t},
}
\]

and shows that both \(V\) and \(J\) remain unchanged under arbitrary time-dependent admissible relabelings.

An explicit excursion construction

\[
[a]\longrightarrow[b]\longrightarrow[a]
\]

has zero endpoint distance but positive path variation. Endpoint equality therefore does not certify a trivial intervening physical trajectory.

**Interpretation boundary:** P14 is a theorem about temporal organization of the physical candidate. It does not equate temporal continuity with experiential continuity.

---

# 14. P15 - finite-sample temporal certification

![Proposition 15 finite-sample temporal certification](docs/figures/p15_finite_sample_temporal_certification.svg)

**Figure 8. Finite-sample temporal certification.** Estimated temporal separation is converted into a certified interval using explicit fingerprint-error radii; comparisons are classified as above threshold, below threshold, or unresolved.

Let \(\widehat c_t\) estimate \(c_t\), and suppose a simultaneous event gives

\[
\boxed{
D_w(c_t,\widehat c_t)
\le
\varepsilon_t
\qquad\text{for all }t.
}
\]

Define

\[
d_{st}=\overline D_w([c_s],[c_t]),
\qquad
\widehat d_{st}=\overline D_w([\widehat c_s],[\widehat c_t]).
\]

P15 proves the exact perturbation inequality

\[
\boxed{
|\widehat d_{st}-d_{st}|
\le
\varepsilon_s+arepsilon_t.
}
\]

Hence

\[
\boxed{
\max\{0,\widehat d_{st}-\varepsilon_s-\varepsilon_t\}
\le d_{st}
\le
\widehat d_{st}+\varepsilon_s+\varepsilon_t.
}
\]

A nonzero physical separation is therefore certified whenever

\[
\boxed{
\widehat d_{st}>\varepsilon_s+\varepsilon_t.
}
\]

For cumulative path variation,

\[
\boxed{
|\widehat V_{0:T}-V_{0:T}|
\le
\varepsilon_0
+2\sum_{t=1}^{T-1}\varepsilon_t
+\varepsilon_T.
}
\]

For the maximum adjacent structural change,

\[
\boxed{
|\widehat J_{0:T}-J_{0:T}|
\le
\max_t(\varepsilon_t+\varepsilon_{t+1}).
}
\]

Given a declared physical threshold \(\eta\), the theorem yields three outcomes:

- lower confidence bound above \(\eta\): **certified above threshold**;
- upper confidence bound at or below \(\eta\): **certified below threshold**;
- otherwise: **unresolved**.

For the restricted case of \(M\) coordinates in \([0,1]\), each estimated as an IID sample mean from \(n\) repetitions at each of \(T+1\) times, Hoeffding plus a union bound gives

\[
\boxed{
\delta_n(\alpha)
=
\sqrt{
\frac{1}{2n}
\log\left(
\frac{2M(T+1)}{\alpha}
\right)
}.
}
\]

Then \(\varepsilon_t=w_{\max}\delta_n(\alpha)\) for the P14 weighted max metric. This is a deliberately limited corollary; the general P11 quantities may require estimator-specific concentration results.

**Interpretation boundary:** P15 certifies physical structural change under declared uncertainty. It does not establish that smoothness implies consciousness, that a large jump implies loss of consciousness, or that the threshold \(\eta\) is universal.

---

# 15. Candidate theory families in one common interface

![Candidate theory comparison map](docs/figures/theory_comparison_map.svg)

**Figure 9. Theory-comparative interface.** Existing theory families and the repository's physical candidate are represented through one common mathematical interface.

\[
\boxed{
\mathfrak T_j
=
(\mathcal F_j,\mathcal B_j,\mathcal M_j,\Pi_j).
}
\]

| Theory family | Physical feature family used in the comparison | Bridge style | Important empirical exposure |
| --- | --- | --- | --- |
| **IIT 4.0** | intrinsic cause-effect structure, maximal substrate, distinctions and relations | phenomenal axioms to physical postulates | causal / transition structure and perturbational model |
| **GNWT** | multilevel workspace organization, ignition, amplification, long-range availability | conscious access/content associated with workspace dynamics | timing, report, long-range and multilevel neural dynamics |
| **RPT** | recurrent processing in relevant neural circuits | recurrence proposed as central to phenomenal processing | local temporal disruption and recurrent interactions |
| **Higher-order** | theory-specific higher-order representational relation | state is conscious in virtue of an appropriate higher-order relation | first-order / higher-order dissociation |
| **Predictive / neurorepresentational / active-inference families** | hierarchical prediction, inference, precision, multimodal representation | heterogeneous; theory-specific bridge required | prediction, precision, representation, hierarchical perturbation |
| **Causal-structure candidate** | full intervention-resolved response geometry, directed influence, partition landscape, temporal trajectory | no experiential bridge assumed | controlled perturbation, compression counterexamples, temporal certification, substrate tests |

The comparison is not a popularity ranking. P2-P6 ask whether theories are empirically identifiable, whether proposed physical features are sufficient, and whether any candidate approaches bridge completeness.

---

# 16. Relationship to Spatiotemporal Observer Mathematics

The intended dependency is

```text
physical measurements
        |
        v
dynamical model
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
representation-invariant temporal trajectory
        |
        v
finite-error physical continuation certificate
        |
        v
candidate bridge
        |
        v
experiential equivalence class [e]
        |
        v
empirical discrimination / falsification
```

The companion repository supplies candidate physical objects such as a certified world-tube

\[
\mathcal W=(S_0,\ldots,S_{T-1}).
\]

The present repository can treat \(p_{\mathcal W}\in\mathcal P\) as the physical input to the bridge program. P14 now supplies a temporal-geometry interface for the causal structure carried by successive world-tube states, while P15 supplies finite-error certification once valid fingerprint radii are available.

The combined statement remains physical. A separate bridge principle would still be required to connect persistent physical-process structure to experiential continuity.

---

# 17. Evidence and claim hierarchy

| Status | Meaning |
| --- | --- |
| **Definition** | mathematical object introduced by the framework |
| **Proved** | theorem derived from explicit assumptions |
| **Identifiability / no-go result** | theorem about what observations or compressed features can or cannot determine |
| **Candidate physical signature** | physical structure proposed for testing, not an experiential conclusion |
| **Finite-error certificate** | conclusion guaranteed under explicitly declared estimation-error bounds |
| **Empirical result** | evidence reported by a cited experiment or dataset |
| **Counterexample** | explicit construction defeating a sufficiency, completeness, compression, or endpoint-only claim |
| **Open bridge problem** | unresolved relation between physical and experiential equivalence structure |

This separation keeps mathematical validity, physical modeling, empirical evidence, statistical uncertainty, and experiential interpretation visible as different kinds of support.

---

# 18. Falsification program

A candidate bridge or physical signature is exposed to several classes of failure.

## 18.1 Representation failure

\[
p\sim_Pp'
\quad\text{but}\quad
F(p)\ne F(p').
\]

## 18.2 Feature-sufficiency failure

\[
F(p)=F(p')
\quad\text{but}\quad
\bar B(p)\ne\bar B(p').
\]

## 18.3 Observational identifiability failure

\[
\Delta_\Pi=0.
\]

## 18.4 Experimental-recoverability failure

\[
\Psi_\Pi(p)=\Psi_\Pi(p')
\quad\text{but}\quad
F_*(p)\ne F_*(p').
\]

## 18.5 Physical compression failure

P12-P13 provide explicit examples in which a reduced component set identifies systems that the richer physical signature distinguishes.

## 18.6 Temporal endpoint failure

P14 gives an explicit path with identical start and end signatures but positive intervening structural variation. Any temporal criterion based only on endpoint agreement therefore fails on that construction.

## 18.7 Finite-data overclaiming failure

P15 makes the unresolved region explicit. If an estimated temporal separation is not larger than its uncertainty budget, the theorem does not permit the analyst to declare true equality or true nonzero change.

## 18.8 Composition and substrate failure

Future composition theorems must remain consistent under splitting, merging, independent composition, controlled coupling, and changes of physical substrate.

[Read the full falsification program](docs/falsification_program.md).

---

# 19. Empirical and theoretical lineage

External work is cited for the exact role it supplies: conceptual origin, bridge architecture, physical mechanism, empirical evidence, causal modeling, metric geometry, or statistical theorem support.

## 19.1 Observer factorization and physical organization

**Max Tegmark.** "Consciousness as a State of Matter." *Chaos, Solitons & Fractals* 76 (2015): 238-270. DOI: [10.1016/j.chaos.2015.03.014](https://doi.org/10.1016/j.chaos.2015.03.014).

**Role:** conceptual background for factorization, information, integration, independence, dynamics, and observer-like physical organization.

## 19.2 Integrated Information Theory

**Larissa Albantakis et al.** "Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms." *PLOS Computational Biology* 19(10) (2023): e1011465. DOI: [10.1371/journal.pcbi.1011465](https://doi.org/10.1371/journal.pcbi.1011465).

**Role:** major example of an explicit phenomenal-axiom to physical-postulate bridge architecture.

## 19.3 Mathematical formalization

**Johannes Kleiner.** "Mathematical Models of Consciousness." arXiv:1907.03223.

**Johannes Kleiner and Sean Tull.** "The Mathematical Structure of Integrated Information Theory." arXiv:2002.07655.

**Role:** mathematical representation of experiential structure and axiomatic/formal consciousness theory.

## 19.4 Major competing-theory sources

**Anil K. Seth and Tim Bayne.** "Theories of consciousness." *Nature Reviews Neuroscience* 23 (2022): 439-452. DOI: [10.1038/s41583-022-00587-4](https://doi.org/10.1038/s41583-022-00587-4).

**Stanislas Dehaene and Jean-Pierre Changeux.** "Experimental and theoretical approaches to conscious processing." *Neuron* 70(2) (2011): 200-227. DOI: [10.1016/j.neuron.2011.03.018](https://doi.org/10.1016/j.neuron.2011.03.018).

**George A. Mashour et al.** "Conscious Processing and the Global Neuronal Workspace Hypothesis." *Neuron* 105(5) (2020): 776-798. DOI: [10.1016/j.neuron.2020.01.026](https://doi.org/10.1016/j.neuron.2020.01.026).

**Jean-Pierre Changeux and Michele Farisco.** "The Global Neuronal Workspace as a multilevel model of conscious processing." *Trends in Cognitive Sciences* 30(6) (2026): 477-479. DOI: [10.1016/j.tics.2026.03.004](https://doi.org/10.1016/j.tics.2026.03.004).

**Victor A. F. Lamme.** "Towards a true neural stance on consciousness." *Trends in Cognitive Sciences* 10(11) (2006): 494-501. DOI: [10.1016/j.tics.2006.09.001](https://doi.org/10.1016/j.tics.2006.09.001).

**Richard Brown, Hakwan Lau, and Joseph E. LeDoux.** "Understanding the Higher-Order Approach to Consciousness." *Trends in Cognitive Sciences* 23(9) (2019): 754-768. DOI: [10.1016/j.tics.2019.06.009](https://doi.org/10.1016/j.tics.2019.06.009).

**Anil K. Seth and Jakob Hohwy.** "Predictive processing as an empirical theory for consciousness science." *Cognitive Neuroscience* 12(2) (2021): 89-90. DOI: [10.1080/17588928.2020.1838467](https://doi.org/10.1080/17588928.2020.1838467).

**Cyriel M. A. Pennartz.** "What is neurorepresentationalism? From neural activity and predictive processing to multi-level representations and consciousness." *Behavioural Brain Research* 432 (2022): 113969. DOI: [10.1016/j.bbr.2022.113969](https://doi.org/10.1016/j.bbr.2022.113969).

## 19.5 Identifiability and adversarial testing

**Adrien Doerig et al.** "The unfolding argument: Why IIT and other causal structure theories cannot explain consciousness." *Consciousness and Cognition* 72 (2019): 49-59. DOI: [10.1016/j.concog.2019.04.002](https://doi.org/10.1016/j.concog.2019.04.002).

**Cogitate Consortium et al.** "Adversarial testing of global neuronal workspace and integrated information theories of consciousness." *Nature* 642 (2025): 133-142. DOI: [10.1038/s41586-025-08888-1](https://doi.org/10.1038/s41586-025-08888-1).

**Andrew W. Corcoran et al.** "Integrated information and predictive processing theories of consciousness: An adversarial collaborative review." *Neuroscience and Biobehavioral Reviews* 187 (2026): 106742. DOI: [10.1016/j.neubiorev.2026.106742](https://doi.org/10.1016/j.neubiorev.2026.106742).

## 19.6 Perturbational, integration, and temporal evidence motivating the physical candidate

**Adenauer G. Casali et al.** "A theoretically based index of consciousness independent of sensory processing and behavior." *Science Translational Medicine* 5(198) (2013): 198ra105. DOI: [10.1126/scitranslmed.3006294](https://doi.org/10.1126/scitranslmed.3006294).

**Charlotte Maschke et al.** "Critical dynamics in spontaneous EEG predict anesthetic-induced loss of consciousness and perturbational complexity." *Communications Biology* 7 (2024): 946. DOI: [10.1038/s42003-024-06613-8](https://doi.org/10.1038/s42003-024-06613-8).

**George A. Mashour.** "Anesthesia and the neurobiology of consciousness." *Neuron* 112(10) (2024): 1553-1567. DOI: [10.1016/j.neuron.2024.03.002](https://doi.org/10.1016/j.neuron.2024.03.002).

**Andrea I. Luppi et al.** "A synergistic workspace for human consciousness revealed by Integrated Information Decomposition." *eLife* 12 (2024): RP88173. DOI: [10.7554/eLife.88173](https://doi.org/10.7554/eLife.88173).

**Andrea I. Luppi et al.** "Convergent transcriptomic and connectomic controllers of information integration and its anaesthetic breakdown across mammalian brains." *Nature Human Behaviour* 10 (2026): 777-802. DOI: [10.1038/s41562-025-02381-5](https://doi.org/10.1038/s41562-025-02381-5).

## 19.7 Causal modeling, metric geometry, and statistical decision theory

**Judea Pearl.** *Causality: Models, Reasoning, and Inference*, 2nd ed. Cambridge University Press, 2009.

**Jonas Peters, Stefan Bauer, and Niklas Pfister.** "Causal Models for Dynamical Systems." arXiv:2001.06208 (2020).

**Dmitri Burago, Yuri Burago, and Sergei Ivanov.** *A Course in Metric Geometry*. Graduate Studies in Mathematics 33, American Mathematical Society, 2001. DOI: [10.1090/gsm/033](https://doi.org/10.1090/gsm/033).

**Lucien Le Cam and Grace Lo Yang.** *Asymptotics in Statistics: Some Basic Concepts*, 2nd ed. Springer, 2000. DOI: [10.1007/978-1-4612-1166-2](https://doi.org/10.1007/978-1-4612-1166-2).

**Alexandre B. Tsybakov.** *Introduction to Nonparametric Estimation*. Springer, 2009. DOI: [10.1007/b13794](https://doi.org/10.1007/b13794).

**Wassily Hoeffding.** "Probability Inequalities for Sums of Bounded Random Variables." *Journal of the American Statistical Association* 58(301) (1963): 13-30. DOI: [10.1080/01621459.1963.10500830](https://doi.org/10.1080/01621459.1963.10500830).

The full role-aware bibliography is maintained in [Literature Map](docs/literature_map.md), with machine-readable references in [`references.bib`](references.bib).

No citation is used to imply endorsement of the repository's bridge hypothesis.

---

# 20. Research record

| Research record | Current state |
| --- | ---: |
| proposition-level results | **15** |
| original physical candidate families | **1 - intervention-resolved causal structure** |
| candidate bridge principles | **8** |
| universal-proof criteria | **12** |
| claim-level / regression tests | **84** |
| canonical visual research figures | **9** |
| CI matrix | **Python 3.10, 3.11, 3.12** |
| research-software version | **0.15.0** |

The v0.15.0 checkpoint extends the bridge, recovery, finite-data, and physical-minimality record with a representation-invariant temporal geometry and a finite-error temporal certification theorem.

---

# 21. Reproducibility and audit path

```bash
python -m pip install -e ".[dev]"
pytest
ruff check .
```

The code audits:

- representation invariance;
- bridge discriminability and optimal binary testing;
- observational theory-equivalence classes;
- maximin and set-cover experiment design;
- physical-feature sufficiency and canonical bridge signatures;
- experimental signature recoverability;
- finite-error partition recovery;
- explicit categorical sample complexity;
- robust protocol-family optimization;
- intervention-response geometry;
- block marginals and partition-product models;
- partition response irreducibility;
- directed perturbational influence and cycle detection;
- single-component projection collisions;
- pairwise component irredundancy;
- weighted causal-structure metrics;
- quotient alignment under admissible relabelings;
- temporal path variation and endpoint bounds;
- temporal invariance under time-dependent relabeling;
- pairwise finite-error temporal intervals;
- cumulative-variation and maximum-jump uncertainty bounds;
- three-way temporal threshold certification;
- the bounded-coordinate Hoeffding corollary.

The documentation integrity test checks local Markdown links and image targets. The repository structure guard protects P1-P15 and all current visual research assets. The visual-quality guard enforces large publication canvases, accessibility metadata, consistent fonts, and the absence of obsolete shorthand in canonical figures.

---

# 22. Current frontier

P13 resolves the immediate component-level question on the declared finite domain: none of the three major components is reconstructible from the other two without additional assumptions. P14 resolves the first fixed-dimension temporal-geometry problem under a finite isometric relabeling group. P15 resolves deterministic propagation of declared fingerprint-error radii through that geometry and adds a limited bounded-coordinate finite-sample corollary.

The next frontier is therefore structural and estimator-specific:

1. **composition:** characterize independent composition and weak or controlled coupling of causal-structure systems;
2. **splitting and merging:** extend temporal continuation when the number or identity of physical blocks changes;
3. **observer-to-bridge interface:** connect certified moving world-tubes to the time-indexed causal-structure domain;
4. **estimator-specific concentration:** derive valid finite-sample radii for the actual response-geometry, directed-influence, and irreducibility estimators rather than relying on the restricted P15 sample-mean corollary;
5. **irregular-time normalization:** determine how structural variation should depend on sampling cadence and physical time;
6. **cross-theory adversarial experiments:** derive protocol-level divergences among IIT, GNWT, RPT, higher-order, predictive/neurorepresentational, and repository candidate families;
7. **biological and non-biological counterexamples:** actively search for systems that match rich physical causal structure while differing in the relevant experiential evidence;
8. **experiential formalization:** sharpen \(\mathcal Q_E\) and its invariances independently of the physical candidate;
9. **bridge theorem:** pursue a final implication only after the physical signature, experiential space, identifiability, recoverability, finite-data uncertainty, composition, and falsification requirements have survived the preceding program.

The current research chain is therefore

\[
\boxed{
\text{controlled physical response}
\longrightarrow
\text{intervention-resolved causal structure}
\longrightarrow
\text{representation-invariant temporal trajectory}
\longrightarrow
\text{finite-error temporal certification}.
}
\]

That chain is a physical and mathematical result. The physical-to-experiential bridge remains an open scientific problem.
