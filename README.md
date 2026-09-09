# Mathematical Consciousness Bridge

[![tests](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/test.yml/badge.svg)](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/test.yml)
[![version](https://img.shields.io/badge/version-0.13.0-2563eb)](CITATION.cff)
[![license](https://img.shields.io/badge/license-MIT-059669)](LICENSE)

**Mahsa Keikha, PhD**

> **What mathematical and physical conditions would be required for a physical description of a system to support a scientifically testable claim about consciousness?**

This repository develops a formal mathematical-physics program for the **consciousness bridge problem**: connecting physical organization to formal experiential structure through explicit bridge principles, theorem-level consequences, empirical identifiability, controlled intervention, finite-data certification, and falsification.

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

Proposition 11 then introduces the first original candidate physical signature: **intervention-resolved causal structure**. It is not a scalar. It retains the structure of controlled perturbational response through three complementary objects:

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

Proposition 12 constructively proves that no one of these components, and several natural scalar reductions, can reconstruct the full physical candidate on explicit finite domains. Proposition 13 strengthens this result by proving that **no pair of the three components can reconstruct the omitted component** on a declared finite audit domain.

The present record therefore separates:

1. **proved mathematical structure** - P1-P13;
2. **candidate physical structure** - the intervention-resolved causal-structure candidate;
3. **open bridge problem** - determining whether an independently justified physical equivalence structure can be connected to formal experiential equivalence and survive competing-theory, cross-substrate, temporal, compositional, and empirical tests.

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

The central difficulty is the third arrow. Integration, complexity, recurrence, global broadcasting, causal structure, criticality, or subsystem persistence can all be mathematically meaningful without yet constituting a bridge to experience.

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
| U10 | finite-measurement certification | P8 |
| U11 | explicit sample complexity | P9 |
| U12 | temporal, compositional, substrate, and falsification consistency | active frontier |

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

# 5. Theorem roadmap: P1-P13

![Propositions 1 through 13 theorem roadmap](docs/figures/theorem_roadmap.svg)

**Figure 3. Theorem dependency map.** P1-P10 establish the general bridge and finite-data machinery. P11 introduces the physical candidate. P12 and P13 test whether that candidate can be compressed without losing physical information.

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

# 13. Candidate theory families in one common interface

![Candidate theory comparison map](docs/figures/theory_comparison_map.svg)

**Figure 7. Theory-comparative interface.** Existing theory families and the repository's physical candidate are represented through one common mathematical interface.

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
| **Causal-structure candidate** | full intervention-resolved response geometry, directed influence, partition landscape | no experiential bridge assumed | controlled perturbation, counterexamples, recoverability, substrate tests |

The comparison is not a popularity ranking. P2-P6 ask whether theories are empirically identifiable, whether proposed physical features are sufficient, and whether any candidate approaches bridge completeness.

---

# 14. Relationship to Spatiotemporal Observer Mathematics

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

The present repository can treat \(p_{\mathcal W}\in\mathcal P\) as the physical input to the bridge program.

---

# 15. Evidence and claim hierarchy

| Status | Meaning |
| --- | --- |
| **Definition** | mathematical object introduced by the framework |
| **Proved** | theorem derived from explicit assumptions |
| **Identifiability / no-go result** | theorem about what observations or compressed features can or cannot determine |
| **Candidate physical signature** | physical structure proposed for testing, not an experiential conclusion |
| **Empirical result** | evidence reported by a cited experiment or dataset |
| **Counterexample** | explicit construction defeating a sufficiency, completeness, or recoverability claim |
| **Open bridge problem** | unresolved relation between physical and experiential equivalence structure |

This separation keeps mathematical validity, physical modeling, empirical evidence, and experiential interpretation visible as different kinds of support.

---

# 16. Falsification program

A candidate bridge or physical signature is exposed to several classes of failure.

## 16.1 Representation failure

\[
p\sim_Pp'
\quad\text{but}\quad
F(p)\ne F(p').
\]

## 16.2 Feature-sufficiency failure

\[
F(p)=F(p')
\quad\text{but}\quad
\bar B(p)\ne\bar B(p').
\]

## 16.3 Observational identifiability failure

\[
\Delta_\Pi=0.
\]

## 16.4 Experimental-recoverability failure

\[
\Psi_\Pi(p)=\Psi_\Pi(p')
\quad\text{but}\quad
F_*(p)\ne F_*(p').
\]

## 16.5 Physical compression failure

P12-P13 provide explicit examples in which a reduced component set identifies systems that the richer physical signature distinguishes.

## 16.6 Temporal and composition failure

Future continuation and composition theorems must remain consistent under splitting, merging, independent composition, coupling, and physical evolution.

[Read the full falsification program](docs/falsification_program.md).

---

# 17. Empirical and theoretical lineage

External work is cited for the exact role it supplies: conceptual origin, bridge architecture, physical mechanism, empirical evidence, causal modeling, or statistical theorem support.

## 17.1 Observer factorization and physical organization

**Max Tegmark.** "Consciousness as a State of Matter." *Chaos, Solitons & Fractals* 76 (2015): 238-270. DOI: [10.1016/j.chaos.2015.03.014](https://doi.org/10.1016/j.chaos.2015.03.014).

**Role:** conceptual background for factorization, information, integration, independence, dynamics, and observer-like physical organization.

## 17.2 Integrated Information Theory

**Larissa Albantakis et al.** "Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms." *PLOS Computational Biology* 19(10) (2023): e1011465. DOI: [10.1371/journal.pcbi.1011465](https://doi.org/10.1371/journal.pcbi.1011465).

**Role:** major example of an explicit phenomenal-axiom to physical-postulate bridge architecture.

## 17.3 Mathematical formalization

**Johannes Kleiner.** "Mathematical Models of Consciousness." arXiv:1907.03223.

**Johannes Kleiner and Sean Tull.** "The Mathematical Structure of Integrated Information Theory." arXiv:2002.07655.

**Role:** mathematical representation of experiential structure and axiomatic/formal consciousness theory.

## 17.4 Major competing-theory sources

**Anil K. Seth and Tim Bayne.** "Theories of consciousness." *Nature Reviews Neuroscience* 23 (2022): 439-452. DOI: [10.1038/s41583-022-00587-4](https://doi.org/10.1038/s41583-022-00587-4).

**Stanislas Dehaene and Jean-Pierre Changeux.** "Experimental and theoretical approaches to conscious processing." *Neuron* 70(2) (2011): 200-227. DOI: [10.1016/j.neuron.2011.03.018](https://doi.org/10.1016/j.neuron.2011.03.018).

**George A. Mashour et al.** "Conscious Processing and the Global Neuronal Workspace Hypothesis." *Neuron* 105(5) (2020): 776-798. DOI: [10.1016/j.neuron.2020.01.026](https://doi.org/10.1016/j.neuron.2020.01.026).

**Jean-Pierre Changeux and Michele Farisco.** "The Global Neuronal Workspace as a multilevel model of conscious processing." *Trends in Cognitive Sciences* 30(6) (2026): 477-479. DOI: [10.1016/j.tics.2026.03.004](https://doi.org/10.1016/j.tics.2026.03.004).

**Victor A. F. Lamme.** "Towards a true neural stance on consciousness." *Trends in Cognitive Sciences* 10(11) (2006): 494-501. DOI: [10.1016/j.tics.2006.09.001](https://doi.org/10.1016/j.tics.2006.09.001).

**Richard Brown, Hakwan Lau, and Joseph E. LeDoux.** "Understanding the Higher-Order Approach to Consciousness." *Trends in Cognitive Sciences* 23(9) (2019): 754-768. DOI: [10.1016/j.tics.2019.06.009](https://doi.org/10.1016/j.tics.2019.06.009).

**Anil K. Seth and Jakob Hohwy.** "Predictive processing as an empirical theory for consciousness science." *Cognitive Neuroscience* 12(2) (2021): 89-90. DOI: [10.1080/17588928.2020.1838467](https://doi.org/10.1080/17588928.2020.1838467).

**Cyriel M. A. Pennartz.** "What is neurorepresentationalism? From neural activity and predictive processing to multi-level representations and consciousness." *Behavioural Brain Research* 432 (2022): 113969. DOI: [10.1016/j.bbr.2022.113969](https://doi.org/10.1016/j.bbr.2022.113969).

## 17.5 Identifiability and adversarial testing

**Adrien Doerig et al.** "The unfolding argument: Why IIT and other causal structure theories cannot explain consciousness." *Consciousness and Cognition* 72 (2019): 49-59. DOI: [10.1016/j.concog.2019.04.002](https://doi.org/10.1016/j.concog.2019.04.002).

**Cogitate Consortium et al.** "Adversarial testing of global neuronal workspace and integrated information theories of consciousness." *Nature* 642 (2025): 133-142. DOI: [10.1038/s41586-025-08888-1](https://doi.org/10.1038/s41586-025-08888-1).

**Andrew W. Corcoran et al.** "Integrated information and predictive processing theories of consciousness: An adversarial collaborative review." *Neuroscience and Biobehavioral Reviews* 187 (2026): 106742. DOI: [10.1016/j.neubiorev.2026.106742](https://doi.org/10.1016/j.neubiorev.2026.106742).

## 17.6 Perturbational and integration evidence motivating the physical candidate

**Adenauer G. Casali et al.** "A theoretically based index of consciousness independent of sensory processing and behavior." *Science Translational Medicine* 5(198) (2013): 198ra105. DOI: [10.1126/scitranslmed.3006294](https://doi.org/10.1126/scitranslmed.3006294).

**Charlotte Maschke et al.** "Critical dynamics in spontaneous EEG predict anesthetic-induced loss of consciousness and perturbational complexity." *Communications Biology* 7 (2024): 946. DOI: [10.1038/s42003-024-06613-8](https://doi.org/10.1038/s42003-024-06613-8).

**Andrea I. Luppi et al.** "A synergistic workspace for human consciousness revealed by Integrated Information Decomposition." *eLife* 12 (2024): RP88173. DOI: [10.7554/eLife.88173](https://doi.org/10.7554/eLife.88173).

**Andrea I. Luppi et al.** "Convergent transcriptomic and connectomic controllers of information integration and its anaesthetic breakdown across mammalian brains." *Nature Human Behaviour* 10 (2026): 777-802. DOI: [10.1038/s41562-025-02381-5](https://doi.org/10.1038/s41562-025-02381-5).

## 17.7 Causal modeling and statistical decision theory

**Judea Pearl.** *Causality: Models, Reasoning, and Inference*, 2nd ed. Cambridge University Press, 2009.

**Lucien Le Cam and Grace Lo Yang.** *Asymptotics in Statistics: Some Basic Concepts*, 2nd ed. Springer, 2000. DOI: [10.1007/978-1-4612-1166-2](https://doi.org/10.1007/978-1-4612-1166-2).

**Alexandre B. Tsybakov.** *Introduction to Nonparametric Estimation*. Springer, 2009. DOI: [10.1007/b13794](https://doi.org/10.1007/b13794).

**Wassily Hoeffding.** "Probability Inequalities for Sums of Bounded Random Variables." *Journal of the American Statistical Association* 58(301) (1963): 13-30. DOI: [10.1080/01621459.1963.10500830](https://doi.org/10.1080/01621459.1963.10500830).

The full role-aware bibliography is maintained in [Literature Map](docs/literature_map.md), with machine-readable references in [`references.bib`](references.bib).

---

# 18. Research record

| Research record | Current state |
| --- | ---: |
| proposition-level results | **13** |
| original physical candidate families | **1 - intervention-resolved causal structure** |
| candidate bridge principles | **8** |
| universal-proof criteria | **12** |
| claim-level / regression tests | **66** after terminology cleanup and P13 consolidation |
| visual research figures | **7** |
| CI matrix | **Python 3.10, 3.11, 3.12** |
| research-software version | **0.13.0** |

The v0.13.0 checkpoint extends the previous bridge, recovery, and finite-data record with P13 pairwise component irredundancy and replaces opaque internal shorthand with plain scientific terminology.

---

# 19. Reproducibility and audit path

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
- pairwise component irredundancy.

The documentation integrity test checks local Markdown links and image targets, and the repository structure guard protects P1-P13 and all current visual research assets.

---

# 20. Current frontier

P13 resolves the immediate component-level question on the declared finite domain: none of the three major components is reconstructible from the other two without additional assumptions.

The next frontier is therefore temporal and compositional structure:

1. **temporal continuation:** define when neighboring time-indexed causal-structure states belong to one persistent physical process;
2. **composition:** characterize independent composition, weak and strong coupling, splitting, and merging;
3. **observer-to-bridge interface:** connect certified moving world-tubes to the causal-structure domain;
4. **cross-theory adversarial experiments:** derive protocol-level divergences among IIT, GNWT, RPT, higher-order, predictive/neurorepresentational, and repository candidate families;
5. **biological and non-biological counterexamples:** actively search for systems that match rich physical causal structure while differing in the relevant experiential evidence;
6. **experiential formalization:** sharpen \(\mathcal Q_E\) and its invariances independently of the physical candidate;
7. **bridge theorem:** pursue a final implication only after the physical signature, experiential space, identifiability, recoverability, finite-data uncertainty, and falsification requirements have survived the preceding program.

The strongest open structural target remains

\[
\boxed{
F_*(p)=F_*(p')
\iff
C_B(p)=C_B(p').
}
\]

The scientific task is to determine whether an independently physical feature \(F_*\) can satisfy this equivalence on an empirically meaningful domain.

---

# 21. Repository map

| Area | Main files |
| --- | --- |
| Visual navigation | [`docs/visual_research_guide.md`](docs/visual_research_guide.md), [`docs/figures/`](docs/figures/) |
| Problem definition | [`docs/bridge_problem.md`](docs/bridge_problem.md), [`docs/research_architecture.md`](docs/research_architecture.md) |
| Physical modeling | [`docs/physical_foundation.md`](docs/physical_foundation.md) |
| Universal theorem target | [`docs/universal_proof_target.md`](docs/universal_proof_target.md) |
| Theorem chain | [`docs/theorem_roadmap.md`](docs/theorem_roadmap.md), P1-P13 proof pages |
| Physical candidate | [`docs/proposition_11_intervention_resolved_causal_structure.md`](docs/proposition_11_intervention_resolved_causal_structure.md) |
| Single-component no-go audit | [`docs/proposition_12_component_insufficiency.md`](docs/proposition_12_component_insufficiency.md) |
| Pairwise irredundancy audit | [`docs/proposition_13_pairwise_component_irredundancy.md`](docs/proposition_13_pairwise_component_irredundancy.md) |
| Competing theories | [`docs/candidate_theory_families.md`](docs/candidate_theory_families.md) |
| Bridge principles | [`docs/axiom_ledger.md`](docs/axiom_ledger.md) |
| Equation provenance | [`docs/equation_and_citation_map.md`](docs/equation_and_citation_map.md) |
| Falsification | [`docs/falsification_program.md`](docs/falsification_program.md) |
| Bibliography | [`docs/literature_map.md`](docs/literature_map.md), [`references.bib`](references.bib) |
| Reproducibility | [`src/consciousness_bridge/`](src/consciousness_bridge/), [`tests/`](tests/), [CI workflow](.github/workflows/test.yml) |
| Release history | [`CHANGELOG.md`](CHANGELOG.md), [`CITATION.cff`](CITATION.cff) |

---

## Citation

Use [`CITATION.cff`](CITATION.cff) for the repository-level citation and [`references.bib`](references.bib) for method-specific scientific references. Conceptual lineage, mathematical tools, empirical evidence, and repository-original constructions are distinguished in the [Equation and Citation Map](docs/equation_and_citation_map.md) and [Literature Map](docs/literature_map.md).
