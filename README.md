# Mathematical Consciousness Bridge

[![tests](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/test.yml/badge.svg)](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/test.yml)
[![version](https://img.shields.io/badge/version-0.12.0-2563eb)](CITATION.cff)
[![license](https://img.shields.io/badge/license-MIT-059669)](LICENSE)

**Mahsa Keikha, PhD**

> **What mathematical and physical conditions would be required for a physical description of a system to support a scientifically testable claim about consciousness?**

This repository develops a formal mathematical-physics program for the **consciousness bridge problem**: the problem of connecting physical organization to formal experiential structure through explicit bridge principles, theorem-level consequences, empirical identifiability, falsification, and finite-data certification.

The program is designed as an ongoing research study. It builds on, but remains logically distinct from, [Spatiotemporal Observer Mathematics](https://github.com/MahsaKeikha/spatiotemporal-observer-math), which studies whether a persistent moving subsystem can be inferred and certified from dynamics. That companion project can supply a candidate physical subsystem. The present project studies the additional physical-to-experiential bridge.

---

## Visual overview

![Mathematical Consciousness Bridge research architecture](docs/figures/research_architecture.svg)

**Figure 1. Research architecture.** Physics, mathematical structure, candidate physical signatures, bridge principles, experiential structure, empirical predictions, finite-data certification, and falsification are kept as distinct layers.

The central logical target is

\[
\boxed{
\text{physical first principles}
+
\text{bridge principles}
+
\text{empirically validated discriminants}
+
\text{finite-data certification}
\Longrightarrow
\text{formal experiential property}.
}
\]

The mathematical implication must be proved from explicit premises. The bridge premises must also be exposed to empirical failure rather than introduced only by definition.

---

# Start here

| Reader goal | Entry point |
| --- | --- |
| See the entire program visually | **[Visual Research Guide](docs/visual_research_guide.md)** |
| Understand what would count as the strongest proof target | **[Universal Consciousness Proof Target](docs/universal_proof_target.md)** |
| Understand the physical input | **[Physical Foundation](docs/physical_foundation.md)** |
| Read the exact bridge problem | **[Consciousness Bridge Problem](docs/bridge_problem.md)** |
| Follow the theorem dependency chain | **[Theorem Roadmap](docs/theorem_roadmap.md)** |
| Read the original physical candidate | **[P11 - Intervention-Resolved Causal Geometry](docs/proposition_11_intervention_resolved_causal_geometry.md)** |
| Read the current minimality/no-go result | **[P12 - Component Insufficiency](docs/proposition_12_component_insufficiency.md)** |
| Compare major consciousness theories | [Candidate Theory Families](docs/candidate_theory_families.md) |
| Inspect candidate bridge principles | [Axiom Ledger](docs/axiom_ledger.md) |
| Audit equation provenance | [Equation and Citation Map](docs/equation_and_citation_map.md) |
| Inspect falsification criteria | [Falsification Program](docs/falsification_program.md) |
| Trace the literature | [Literature Map](docs/literature_map.md) |
| Read machine-readable references | [`references.bib`](references.bib) |
| Cite this research program | [`CITATION.cff`](CITATION.cff) |

---

# Abstract

A physical theory can specify states, dynamics, interventions, and observable probability laws without specifying why any physical organization should correspond to subjective experience. A mathematical consciousness theory therefore requires an additional object: a bridge from physically meaningful equivalence classes to formal experiential equivalence classes.

This repository makes that bridge itself the object of mathematics. The program first defines the physical and experiential domains, representation equivalences, admissible experiment classes, and observable laws. It then proves representation-invariance conditions, exact experiment-class identifiability criteria, observational theory-equivalence theorems, optimal experiment-design results, physical-feature sufficiency and completeness theorems, finite-data signature-recovery guarantees, and sample-complexity bounds.

Proposition 11 introduces the first original candidate physical signature: **Intervention-Resolved Causal Geometry (IRCG)**, a structured object built from controlled perturbational response laws, directed causal influence, and partition-specific irreducibility. Proposition 12 immediately subjects IRCG to an internal minimality audit and constructively proves that its individual components and several tempting scalar reductions are insufficient to reconstruct the full object.

The present mathematical record therefore has three deliberately separated parts:

1. **proved mathematical structure** - P1-P12;
2. **candidate physical signature** - IRCG;
3. **open bridge program** - establishing whether a physically defined equivalence structure can be connected to a formally justified experiential equivalence structure and survive competing-theory and counterexample tests.

---

# 1. The scientific problem

The central chain is

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

The central difficulty is the bridge arrow. A theorem about integration, complexity, recurrence, global broadcasting, causal structure, criticality, or subsystem persistence does not by itself determine an experiential interpretation. The project therefore asks what additional principles, identifiability conditions, and experiments are required.

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

The bridge must state which physical level is primitive and which interventions count as physically admissible.

## 2.1 Physical representation equivalence

The same physical process can be represented in different coordinates. If

\[
z=\varphi(x)
\]

is an invertible reparameterization, then

\[
\dot z
=
D\varphi(x)F(x,u),
\qquad
x=\varphi^{-1}(z).
\]

If this is only a change of description, it should not alter the physical input supplied to a bridge. We therefore introduce

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

This quotient is the domain on which a representation-independent physical signature or bridge should ultimately operate.

---

# 3. Experiential domain and bridge object

Let

\[
\mathcal E
\]

be a formal space of candidate experiential structures, with experiential equivalence relation

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

A complete empirical bridge theory must also specify how its physical and bridge structure produces observable probability laws. The repository therefore uses the abstract theory object

\[
\boxed{
\mathfrak T
=
(\mathcal P,\mathcal E,\sim_P,\sim_E,\mathcal B,\mathcal M,\Pi),
}
\]

where \(\mathcal M\) is the measurement interface and \(\Pi\) is the admissible experiment class.

---

# 4. Universal proof target

![Universal consciousness proof criteria](docs/figures/universal_proof_ladder.svg)

**Figure 2. Universal proof ladder.** The project tracks twelve separate requirements rather than collapsing them into one metric.

The twelve criteria are:

| Criterion | Requirement | Current mathematical support |
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

The strongest theorem template pursued by the program is

\[
\boxed{
\begin{aligned}
& p\in\mathcal Q_P,\\
& A_1,\ldots,A_k\text{ bridge principles hold},\\
& F_*(p)\text{ is a representation-invariant complete physical signature},\\
& \widehat F_*(p)\text{ is recovered with declared finite-data confidence},\\
& V_1,\ldots,V_r\text{ discriminating empirical validation conditions hold}
\\[2mm]
&\qquad\Longrightarrow
\bar B(p)\in\mathcal C_E,
\end{aligned}
}
\]

where

\[
\mathcal C_E\subseteq\mathcal Q_E
\]

is a formally specified class of experiential structures.

A stronger biconditional target is

\[
\boxed{
\bar B(p)\in\mathcal C_E
\iff
F_*(p)\in\mathcal R_C,
}
\]

for a mathematically characterized region

\[
\mathcal R_C
\subseteq
\operatorname{Im}(F_*).
\]

Both directions require separate justification.

[Read the complete proof target](docs/universal_proof_target.md).

---

# 5. Theorem roadmap: P1-P12

![Propositions 1 through 12 theorem roadmap](docs/figures/theorem_roadmap.svg)

**Figure 3. Theorem dependency map.** P1-P10 establish the general bridge, identifiability, completeness, recovery, and experiment-design machinery. P11 introduces IRCG. P12 begins the candidate's internal falsification/minimality program.

## 5.1 Complete proposition index

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
| **P11** | Intervention-Resolved Causal Geometry candidate + structural certificates | Proved construction / candidate physical signature | [P11](docs/proposition_11_intervention_resolved_causal_geometry.md) |
| **P12** | component insufficiency and minimal-feature collision theorems | Proved no-go / minimality result | [P12](docs/proposition_12_component_insufficiency.md) |

---

# 6. Layer A - representation invariance

Let

\[
B:\mathcal P\to\mathcal Q_E
\]

be a bridge assignment and

\[
\pi_P:\mathcal P\to\mathcal Q_P
\]

the physical quotient projection.

## Proposition 1

There exists a unique

\[
\bar B:\mathcal Q_P\to\mathcal Q_E
\]

such that

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

This is the exact mathematical condition preventing arbitrary coordinates, unit conventions, labels, or physically irrelevant encodings from changing the bridge assignment.

---

# 7. Layer B - identifiability and theory no-go structure

For a complete theory \(\mathfrak T_i\), protocol \(\pi\), and physical input \(q\), write

\[
P_i^{\pi,q}
\]

for the predicted observable law.

Define total variation

\[
\boxed{
\|P-Q\|_{\mathrm{TV}}
=
\sup_A|P(A)-Q(A)|.
}
\]

## Proposition 2 - experiment-class discriminability

\[
\boxed{
\Delta_\Pi(\mathfrak T_1,\mathfrak T_2;q)
=
\sup_{\pi\in\Pi}
\|P_1^{\pi,q}-P_2^{\pi,q}\|_{\mathrm{TV}}.
}
\]

The exact non-identifiability criterion is

\[
\boxed{
\Delta_\Pi=0
\iff
P_1^{\pi,q}=P_2^{\pi,q}
\quad\forall\pi\in\Pi.
}
\]

With equal theory priors, the optimal one-shot discrimination error is

\[
\boxed{
R_\pi^*
=
\frac12
\left(1-\|P_1^{\pi,q}-P_2^{\pi,q}\|_{\mathrm{TV}}\right).
}
\]

For independently repeated discriminating experiments with event-probability gap \(\eta>0\), Hoeffding concentration gives

\[
\boxed{
P(\mathrm{error})
<
\exp\left(-\frac{n\eta^2}{2}\right).
}
\]

## Proposition 3 - observational bridge-equivalence classes

Define the full observable fingerprint

\[
\boxed{
\Phi_{\Pi,q}(\mathfrak T)
=
(P_{\mathfrak T}^{\pi,q})_{\pi\in\Pi}.
}
\]

Then observational indistinguishability defines an equivalence relation and

\[
\boxed{
\Theta/{\sim_{\Pi,q}}
\cong
\operatorname{Im}(\Phi_{\Pi,q}).
}
\]

Thus the empirically identifiable object may be an entire equivalence class of theories rather than a named individual theory.

## Proposition 4 - discriminating experiment design

For theory pair \(i,j\), define

\[
d_{ij}(\pi)
=
\|P_i^{\pi,q}-P_j^{\pi,q}\|_{\mathrm{TV}}.
\]

For a protocol family \(S\),

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
\bigcup_{\pi\in S}C_\pi=\mathcal U,
}
\]

so finite complete theory discrimination reduces to a set-cover problem over distinguishable theory pairs.

---

# 8. Layer C - physical-feature sufficiency and completeness

Suppose a physical feature is proposed:

\[
F:\mathcal Q_P\to\mathcal Z.
\]

## Proposition 5 - feature sufficiency

\[
\boxed{
\bar B=g\circ F
\iff
F(p)=F(p')
\Longrightarrow
\bar B(p)=\bar B(p').
}
\]

Therefore a single pair satisfying

\[
F(p)=F(p')
\qquad\text{but}\qquad
\bar B(p)\ne\bar B(p')
\]

is a direct counterexample to the claim that \(F\) is sufficient on the declared domain.

## Proposition 6 - canonical complete bridge signature

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
\bar B(p)=\bar B(p').
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

This turns the phrase "complete physical signature" into a precise equivalence-class target. The scientific discovery problem is to define a physical feature independently of the bridge labels whose fibers match these canonical bridge fibers.

---

# 9. Layer D - experimental recovery and finite-data certification

For an experiment family \(\Pi\), define the physical observable fingerprint

\[
\boxed{
\Psi_\Pi(p)
=
(P^{\pi,p})_{\pi\in\Pi}.
}
\]

## Proposition 7 - recoverability

A target signature \(F_*\) is recoverable from the declared experiments exactly when

\[
\boxed{
\Psi_\Pi(p)=\Psi_\Pi(p')
\Longrightarrow
F_*(p)=F_*(p').
}
\]

A signature-different pair with identical observable fingerprints is therefore an exact no-go counterexample for that experiment class.

## Proposition 8 - robust finite-error recovery

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

be maximum within-signature spread and

\[
\delta_S
=
\min_{F_*(p)\ne F_*(p')}d_S(p,p')
\]

minimum between-signature separation. Define

\[
\boxed{
\gamma_S
=
\delta_S-\omega_S.
}
\]

If

\[
\sup_{p,\pi}
\|\widehat P^{\pi,p}-P^{\pi,p}\|_{\mathrm{TV}}
\le\varepsilon,
\]

then exact partition recovery is guaranteed when

\[
\boxed{
\gamma_S>4\varepsilon.
}
\]

## Proposition 9 - explicit categorical sample complexity

For \(N_P\) physical systems, \(N_\pi\) protocols, at most \(K\) categorical outcomes, confidence target \(1-\alpha\), and \(n\) IID repetitions per physical-system/protocol cell, a sufficient condition is

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

The current bound is conservative but explicit and auditable.

## Proposition 10 - robust protocol design

Define

\[
\boxed{
\Gamma(S)
=
\delta(S)-\omega(S).
}
\]

For a newly added protocol \(\rho\), define

\[
a_\rho(S)
=
\delta(S\cup\{\rho\})-\delta(S),
\]

\[
b_\rho(S)
=
\omega(S\cup\{\rho\})-\omega(S).
\]

Then

\[
\boxed{
\Gamma(S\cup\{\rho\})-\Gamma(S)
=
a_\rho(S)-b_\rho(S).
}
\]

Hence

\[
\boxed{
\Gamma(S\cup\{\rho\})>\Gamma(S)
\iff
a_\rho(S)>b_\rho(S).
}
\]

More modalities or perturbations are therefore not automatically better. An added protocol can increase nuisance within-signature variation more than bridge-relevant separation.

---

# 10. Candidate A - Intervention-Resolved Causal Geometry

![Anatomy of Intervention-Resolved Causal Geometry](docs/figures/ircg_anatomy.svg)

**Figure 4. IRCG anatomy.** The candidate is a structured intervention-response object rather than a single complexity or integration score.

## 10.1 Controlled response laws

Let the physical subsystem be divided into blocks

\[
V=\{1,\ldots,m\}.
\]

For admissible intervention \(u\in\mathcal U_p\) and delay \(\tau\in\mathcal T\), define

\[
\boxed{
P_p^{u,\tau}
=
\mathcal L\!\left(Y_{t+\tau}^{V}\mid do(u),p\right).
}
\]

The \(do(u)\) notation indicates controlled intervention semantics rather than passive association.

## 10.2 Response geometry

For interventions \(u,v\),

\[
\boxed{
d_p^\tau(u,v)
=
\left\|P_p^{u,\tau}-P_p^{v,\tau}\right\|_{\mathrm{TV}}.
}
\]

The complete family

\[
\boxed{
\mathcal G_p
=
\{d_p^\tau:\tau\in\mathcal T\}
}
\]

records how differentiated the physical responses are across interventions and time.

## 10.3 Directed interventional influence

Let \(\mathcal E_i\) contain intervention pairs differing only at source block \(i\). Then

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

records strength, direction, and timing of perturbational influence.

## 10.4 Partition response irreducibility

For a nontrivial partition

\[
\pi=\{B_1,\ldots,B_k\},
\]

define the productized partition response

\[
P_{p,\pi}^{u,\tau}
=
\bigotimes_{r=1}^{k}P_{p,B_r}^{u,\tau}.
\]

Then

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

The full partition landscape is

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

## 10.5 Full IRCG signature

The raw object is

\[
\mathfrak C_p
=
\left(
V,
\mathcal U_p,
\mathcal T,
\mathcal G_p,
\mathcal A_p,
\mathcal K_p
\right).
\]

After quotienting compatible relabelings and response-space reparameterizations,

\[
\boxed{
F_{\mathrm{IRCG}}(p)
=
[\mathfrak C_p]_{\cong}.
}
\]

The strongest candidate-completeness target would be

\[
\boxed{
F_{\mathrm{IRCG}}(p)=F_{\mathrm{IRCG}}(p')
\iff
C_B(p)=C_B(p').
}
\]

This biconditional is a research target, not an assumption in P11.

## 10.6 What P11 proves

P11 establishes three structural results:

1. **representation invariance** under compatible physical reparameterization;
2. **exact partition-factorization certificate**
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
3. **feedforward no-return certificate**: a directed acyclic aggregated influence graph cannot contain a causal return loop through distinct blocks.

The candidate is then subjected to the P5-P10 counterexample and recoverability machinery rather than being granted a bridge interpretation by construction.

---

# 11. Proposition 12 - why simple reductions fail

![Proposition 12 constructive collision map](docs/figures/p12_collision_map.svg)

**Figure 5. Constructive collision map.** Each example uses realizable intervention-conditioned probability laws and demonstrates loss of physical information under a proposed compression.

Let

\[
F:X\to Z
\]

be the target signature and

\[
H:X\to W
\]

a proposed compression.

## Proposition 12A - projection collision no-go theorem

If

\[
\boxed{
H(x)=H(x')
\qquad\text{but}\qquad
F(x)\ne F(x'),
}
\]

then no map

\[
g:W\to Z
\]

can satisfy

\[
F=g\circ H
\]

on the declared domain.

### Collision 1: response geometry alone

Two systems can satisfy

\[
\boxed{
\mathcal G_C=\mathcal G_P
}
\]

with

\[
d_C(u_0,u_1)=d_P(u_0,u_1)=1,
\]

while

\[
\boxed{
\kappa_C^\tau(\pi)=\frac12,
\qquad
\kappa_P^\tau(\pi)=0.
}
\]

Thus whole-response distinguishability does not determine internal factorization.

### Collision 2: partition irreducibility alone

Two systems can satisfy

\[
\boxed{
\mathcal K_D=\mathcal K_S
}
\]

while

\[
\boxed{
\mathcal G_D\ne\mathcal G_S.
}
\]

Thus factorization information does not determine whether perturbations generate differentiated responses.

### Collision 3: directed marginal influence alone

Two systems can satisfy

\[
\boxed{
\mathcal A_R=\mathcal A_I
}
\]

while differing in their joint response geometry. Marginal causal effects can therefore miss differences that live only in joint dependence structure.

## 11.1 Scalar insufficiency results

The current constructive audit also shows that, on explicit declared domains, the following are not complete descriptors of IRCG:

\[
\operatorname{Diam}_p(\tau),
\qquad
\kappa_p^*,
\qquad
\mathbf 1\{\text{directed cycle exists}\}.
\]

This is why the repository does not compress the candidate into a one-number "consciousness score" at the current stage.

---

# 12. Candidate theory families in one common interface

![Candidate theory comparison map](docs/figures/theory_comparison_map.svg)

**Figure 6. Theory-comparative interface.** Existing consciousness theories are represented by the physical features, bridge architecture, measurement interface, and experiment class they actually require.

The common interface is

\[
\boxed{
\mathfrak T_j
=
(\mathcal F_j,\mathcal B_j,\mathcal M_j,\Pi_j).
}
\]

| Theory family | Physical feature family used in this repository's source-faithful abstraction | Bridge style | Important experimental exposure |
| --- | --- | --- | --- |
| **IIT 4.0** | intrinsic cause-effect structure, maximal substrate, distinctions and relations | phenomenal axioms to physical postulates; constitutive intrinsic structure | causal / transition structure and perturbational model |
| **GNWT** | multilevel workspace organization, ignition, amplification, long-range availability | conscious access/content associated with global neuronal workspace dynamics | timing, report, long-range and multilevel neural dynamics |
| **RPT** | recurrent processing in relevant neural circuits | recurrent processing proposed as central for phenomenal consciousness | local temporal disruption and recurrent interactions |
| **Higher-order** | higher-order representational relation | state is conscious in virtue of an appropriate higher-order relation | dissociation of first-order and higher-order representation |
| **Predictive / neurorepresentational / active-inference families** | hierarchical prediction, inference, precision, multimodal representation | heterogeneous; bridge remains theory specific | prediction, precision, representation and hierarchical perturbations |
| **IRCG candidate** | full intervention-resolved response geometry, directed influence, partition landscape | no experiential bridge assumed yet | controlled perturbation, counterexamples, recoverability, substrate tests |

The comparison is deliberately not a popularity ranking. P2-P6 ask whether the theories are empirically identifiable, whether their proposed physical features are sufficient, and whether any candidate approaches bridge completeness.

[Read the full theory translation](docs/candidate_theory_families.md).

---

# 13. Relationship to Spatiotemporal Observer Mathematics

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
IRCG or another candidate physical signature
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
\mathcal W
=
(S_0,\ldots,S_{T-1}).
\]

The present repository can treat

\[
p_{\mathcal W}\in\mathcal P
\]

as a physical input to the bridge program. This creates a clean separation between **finding the physical subsystem** and **testing what physical structure, if any, supports the experiential bridge**.

---

# 14. Evidence and claim hierarchy

Every central statement is intended to fit one of the following categories.

| Status | Meaning |
| --- | --- |
| **Definition** | mathematical object introduced by the framework |
| **Proved** | theorem derived from explicit assumptions |
| **Identifiability / no-go result** | theorem about what observations or compressed features can or cannot determine |
| **Candidate physical signature** | physical structure proposed for testing, not yet an experiential conclusion |
| **Empirical result** | evidence reported by a cited experiment or dataset |
| **Counterexample** | explicit construction defeating a sufficiency, completeness, or recoverability claim |
| **Open bridge problem** | unresolved relation between physical and experiential equivalence structure |

This hierarchy is essential to the project. It keeps mathematical validity, physical modeling, empirical evidence, and experiential interpretation visible as distinct kinds of support.

---

# 15. Falsification program

A candidate bridge or candidate physical signature is exposed to multiple classes of failure.

## 15.1 Representation failure

Physically equivalent descriptions generate nonequivalent candidate assignments.

## 15.2 Feature-sufficiency failure

There exists a pair

\[
F(p)=F(p')
\qquad\text{but}\qquad
\bar B(p)\ne\bar B(p').
\]

P5 makes this a direct factorization counterexample.

## 15.3 Experimental recoverability failure

There exists a signature-different pair with

\[
\Psi_\Pi(p)=\Psi_\Pi(p').
\]

P7 then proves that the declared experiment class cannot recover the proposed signature.

## 15.4 Component-minimality failure

A compressed component or scalar collides on systems with different full candidate signatures. P12 provides explicit examples for IRCG.

## 15.5 Composition or temporal failure

Subsystem, composite, or time-continuation assignments violate the theory's own declared bridge or signature laws.

## 15.6 Prediction failure

A bridge-dependent or signature-dependent empirical prediction fails under an explicitly declared protocol.

[Read the falsification program](docs/falsification_program.md).

---

# 16. Empirical and theoretical lineage

The project is intentionally theory-comparative. External work is cited for the role it supplies: conceptual starting point, bridge architecture, physical mechanism, empirical evidence, causal modeling, or statistical theorem support.

## 16.1 Observer factorization and physical organization

**Max Tegmark.** "Consciousness as a State of Matter." *Chaos, Solitons & Fractals* 76 (2015): 238-270. DOI: [10.1016/j.chaos.2015.03.014](https://doi.org/10.1016/j.chaos.2015.03.014).

**Role:** conceptual background for factorization, information, integration, independence, dynamics, and observer-like physical organization.

## 16.2 Integrated Information Theory

**Larissa Albantakis et al.** "Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms." *PLOS Computational Biology* 19(10) (2023): e1011465. DOI: [10.1371/journal.pcbi.1011465](https://doi.org/10.1371/journal.pcbi.1011465).

**Role:** major example of an explicit phenomenal-axiom to physical-postulate bridge architecture and high-dimensional intrinsic causal structure.

## 16.3 Mathematical formalization of consciousness theories

**Johannes Kleiner.** "Mathematical Models of Consciousness." arXiv:1907.03223.

**Johannes Kleiner and Sean Tull.** "The Mathematical Structure of Integrated Information Theory." arXiv:2002.07655.

**Role:** mathematical representation of experiential structure and axiomatic/formal consciousness theory.

## 16.4 Theory surveys and competing mechanisms

**Anil K. Seth and Tim Bayne.** "Theories of consciousness." *Nature Reviews Neuroscience* 23 (2022): 439-452. DOI: [10.1038/s41583-022-00587-4](https://doi.org/10.1038/s41583-022-00587-4).

**Stanislas Dehaene and Jean-Pierre Changeux.** "Experimental and theoretical approaches to conscious processing." *Neuron* 70(2) (2011): 200-227. DOI: [10.1016/j.neuron.2011.03.018](https://doi.org/10.1016/j.neuron.2011.03.018).

**George A. Mashour, Pieter Roelfsema, Jean-Pierre Changeux, and Stanislas Dehaene.** "Conscious Processing and the Global Neuronal Workspace Hypothesis." *Neuron* 105(5) (2020): 776-798. DOI: [10.1016/j.neuron.2020.01.026](https://doi.org/10.1016/j.neuron.2020.01.026).

**Jean-Pierre Changeux and Michele Farisco.** "The Global Neuronal Workspace as a multilevel model of conscious processing." *Trends in Cognitive Sciences* 30(6) (2026): 477-479. DOI: [10.1016/j.tics.2026.03.004](https://doi.org/10.1016/j.tics.2026.03.004).

**Victor A. F. Lamme.** "Towards a true neural stance on consciousness." *Trends in Cognitive Sciences* 10(11) (2006): 494-501. DOI: [10.1016/j.tics.2006.09.001](https://doi.org/10.1016/j.tics.2006.09.001).

**Richard Brown, Hakwan Lau, and Joseph E. LeDoux.** "Understanding the Higher-Order Approach to Consciousness." *Trends in Cognitive Sciences* 23(9) (2019): 754-768. DOI: [10.1016/j.tics.2019.06.009](https://doi.org/10.1016/j.tics.2019.06.009).

**Anil K. Seth and Jakob Hohwy.** "Predictive processing as an empirical theory for consciousness science." *Cognitive Neuroscience* 12(2) (2021): 89-90. DOI: [10.1080/17588928.2020.1838467](https://doi.org/10.1080/17588928.2020.1838467).

**Cyriel M. A. Pennartz.** "What is neurorepresentationalism? From neural activity and predictive processing to multi-level representations and consciousness." *Behavioural Brain Research* 432 (2022): 113969. DOI: [10.1016/j.bbr.2022.113969](https://doi.org/10.1016/j.bbr.2022.113969).

## 16.5 Adversarial theory testing and identifiability

**Adrien Doerig, Aaron Schurger, Kathryn Hess, and Michael H. Herzog.** "The unfolding argument: Why IIT and other causal structure theories cannot explain consciousness." *Consciousness and Cognition* 72 (2019): 49-59. DOI: [10.1016/j.concog.2019.04.002](https://doi.org/10.1016/j.concog.2019.04.002).

**Cogitate Consortium et al.** "Adversarial testing of global neuronal workspace and integrated information theories of consciousness." *Nature* 642 (2025): 133-142. DOI: [10.1038/s41586-025-08888-1](https://doi.org/10.1038/s41586-025-08888-1).

**Andrew W. Corcoran et al.** "Integrated information and predictive processing theories of consciousness: An adversarial collaborative review." *Neuroscience and Biobehavioral Reviews* 187 (2026): 106742. DOI: [10.1016/j.neubiorev.2026.106742](https://doi.org/10.1016/j.neubiorev.2026.106742).

**Role:** motivates theorem-level treatment of empirical identifiability, observational equivalence, and cross-theory discriminating experiments.

## 16.6 Perturbational and information-integration evidence motivating IRCG

**Adenauer G. Casali et al.** "A theoretically based index of consciousness independent of sensory processing and behavior." *Science Translational Medicine* 5(198) (2013): 198ra105. DOI: [10.1126/scitranslmed.3006294](https://doi.org/10.1126/scitranslmed.3006294).

**Charlotte Maschke et al.** "Critical dynamics in spontaneous EEG predict anesthetic-induced loss of consciousness and perturbational complexity." *Communications Biology* 7 (2024): 946. DOI: [10.1038/s42003-024-06613-8](https://doi.org/10.1038/s42003-024-06613-8).

**Andrea I. Luppi et al.** "A synergistic workspace for human consciousness revealed by Integrated Information Decomposition." *eLife* 12 (2024): RP88173. DOI: [10.7554/eLife.88173](https://doi.org/10.7554/eLife.88173).

**Andrea I. Luppi et al.** "Convergent transcriptomic and connectomic controllers of information integration and its anaesthetic breakdown across mammalian brains." *Nature Human Behaviour* 10 (2026): 777-802. DOI: [10.1038/s41562-025-02381-5](https://doi.org/10.1038/s41562-025-02381-5).

**Role:** motivates intervention-resolved differentiation, distributed integration, causal propagation, and controllability as physical quantities worth testing without treating any one measure as the bridge itself.

## 16.7 Causal modeling and statistical decision theory

**Judea Pearl.** *Causality: Models, Reasoning, and Inference*, 2nd ed. Cambridge University Press, 2009.

**Lucien Le Cam and Grace Lo Yang.** *Asymptotics in Statistics: Some Basic Concepts*, 2nd ed. Springer, 2000. DOI: [10.1007/978-1-4612-1166-2](https://doi.org/10.1007/978-1-4612-1166-2).

**Alexandre B. Tsybakov.** *Introduction to Nonparametric Estimation*. Springer, 2009. DOI: [10.1007/b13794](https://doi.org/10.1007/b13794).

**Wassily Hoeffding.** "Probability Inequalities for Sums of Bounded Random Variables." *Journal of the American Statistical Association* 58(301) (1963): 13-30. DOI: [10.1080/01621459.1963.10500830](https://doi.org/10.1080/01621459.1963.10500830).

**Role:** intervention semantics, total-variation testing, statistical experiment comparison, minimax reasoning, and finite-sample concentration.

The full role-aware bibliography is maintained in [Literature Map](docs/literature_map.md), and machine-readable references are in [`references.bib`](references.bib).

---

# 17. Research record

| Research record | Current state |
| --- | ---: |
| proposition-level results | **12** |
| original physical candidate families | **1 - IRCG** |
| candidate bridge principles | **8** |
| universal-proof criteria | **12** |
| claim-level / regression tests | **60** |
| visual research figures | **6** |
| CI matrix | **Python 3.10, 3.11, 3.12** |
| research-software version | **0.12.0** |

The v0.12.0 checkpoint includes representation, identifiability, completeness, recoverability, finite-data, experiment-design, IRCG construction, and IRCG minimality/collision tests.

---

# 18. Reproducibility and audit path

```bash
python -m pip install -e ".[dev]"
pytest
ruff check .
```

The code currently audits:

- representation invariance on declared physical equivalence classes;
- discrete total-variation bridge discriminability;
- optimal equal-prior theory discrimination;
- repeated-event concentration bounds;
- observational theory fingerprints and equivalence partitions;
- maximin and set-cover experiment design;
- physical-feature sufficiency and canonical bridge-signature constructions;
- experimental signature recoverability;
- robust finite-error partition recovery;
- categorical finite-sample trial requirements;
- robust protocol-family optimization;
- IRCG response geometry;
- block marginals and partition-product models;
- partition irreducibility;
- directed perturbational influence and cycle detection;
- IRCG projection collisions and minimality tests.

The documentation integrity test checks local Markdown targets, and the repository structure guard now protects P1-P12 plus the visual research assets.

---

# 19. Current frontier

The mathematical framework is now strong enough that the next work should **not** be another arbitrary scalar measure. The immediate frontier is to determine which combinations of IRCG components are necessary, redundant, or jointly complete on progressively richer physical domains.

The next theorem program is:

1. **P13 - pairwise-component minimality:** test \((\mathcal G,\mathcal A)\), \((\mathcal G,\mathcal K)\), and \((\mathcal A,\mathcal K)\) for reconstructibility of full IRCG;
2. **temporal continuation:** characterize when time-indexed physical-signature states define one persistent physical process relevant to the bridge;
3. **composition consistency:** determine how signatures behave under independent composition, controlled coupling, splitting, and merging;
4. **observer-to-bridge interface:** connect a certified moving world-tube from Spatiotemporal Observer Mathematics to the IRCG physical domain;
5. **cross-theory adversarial experiments:** derive protocol-level divergences among IIT, GNWT, RPT, higher-order, predictive/neurorepresentational, and IRCG-constrained bridge families;
6. **biological and non-biological counterexample program:** search for physically rich systems that match parts of IRCG while differing in the target experiential evidence;
7. **bridge theorem:** only after the physical signature, experiential formalization, identifiability, recoverability, and falsification requirements have survived the preceding tests.

The strongest open structural target remains

\[
\boxed{
F_*(p)=F_*(p')
\iff
C_B(p)=C_B(p').
}
\]

The scientific task is to determine whether an independently physical feature \(F_*\) can satisfy that equivalence on an empirically meaningful domain.

---

# 20. Repository map

| Area | Main files |
| --- | --- |
| Visual navigation | [`docs/visual_research_guide.md`](docs/visual_research_guide.md), [`docs/figures/`](docs/figures/) |
| Problem definition | [`docs/bridge_problem.md`](docs/bridge_problem.md), [`docs/research_architecture.md`](docs/research_architecture.md) |
| Physical modeling | [`docs/physical_foundation.md`](docs/physical_foundation.md) |
| Universal theorem target | [`docs/universal_proof_target.md`](docs/universal_proof_target.md) |
| Theorem chain | [`docs/theorem_roadmap.md`](docs/theorem_roadmap.md), P1-P12 proof pages |
| Original candidate | [`docs/proposition_11_intervention_resolved_causal_geometry.md`](docs/proposition_11_intervention_resolved_causal_geometry.md) |
| Minimality / no-go audit | [`docs/proposition_12_component_insufficiency.md`](docs/proposition_12_component_insufficiency.md) |
| Competing theories | [`docs/candidate_theory_families.md`](docs/candidate_theory_families.md) |
| Assumptions / bridge principles | [`docs/axiom_ledger.md`](docs/axiom_ledger.md) |
| Equation provenance | [`docs/equation_and_citation_map.md`](docs/equation_and_citation_map.md) |
| Falsification | [`docs/falsification_program.md`](docs/falsification_program.md) |
| Bibliography | [`docs/literature_map.md`](docs/literature_map.md), [`references.bib`](references.bib) |
| Reproducibility | [`src/consciousness_bridge/`](src/consciousness_bridge/), [`tests/`](tests/), [CI workflow](.github/workflows/test.yml) |
| Release history | [`CHANGELOG.md`](CHANGELOG.md), [`CITATION.cff`](CITATION.cff) |

---

## Citation

Use [`CITATION.cff`](CITATION.cff) for the repository-level citation and [`references.bib`](references.bib) for method-specific scientific references. Conceptual lineage, mathematical tools, empirical evidence, and repository-original constructions are kept distinct in the [Equation and Citation Map](docs/equation_and_citation_map.md) and [Literature Map](docs/literature_map.md).
