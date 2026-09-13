# Technical Research Architecture

**This page is the formal layer beneath the [Research Map](research_map.md).**

The Research Map explains the scientific story without equations. This page introduces the mathematical objects that support that story and shows how the formal layers connect.

If you want theorem dependencies rather than architecture, use the **[Theorem Roadmap](theorem_roadmap.md)**. If you want every proposition in chronological order, use the **[Detailed Proposition Record](detailed_proposition_record.md)**.

![Mathematical Consciousness Bridge research architecture](figures/research_architecture.svg)

> **Reading rule:** each layer answers one question. A result at one layer does not automatically establish the next layer.

---

## 1. What physical system is being described?

A physical model must first say what counts as the system, how it changes, what can be done to it, and what can be observed.

A compact formal declaration is

\[
\boxed{p=(\mathcal X,\mathcal D,\mathfrak I,\mathcal O)}
\]

where \(\mathcal X\) is the state space, \(\mathcal D\) the dynamics, \(\mathfrak I\) the admissible interventions, and \(\mathcal O\) the observable map.

Typical dynamical descriptions include

\[
\dot x(t)=F(x(t),u(t)),
\qquad
y(t)=h(x(t)),
\]

or stochastic evolution

\[
X_{t+\Delta t}\sim K_{\Delta t}(\cdot\mid X_t,u_t).
\]

When a time-dependent subsystem has already been identified, the related project [Spatiotemporal Observer Mathematics](https://github.com/MahsaKeikha/spatiotemporal-observer-math) can supply a physical world-tube

\[
\boxed{\mathcal W=(S_0,\ldots,S_{T-1}).}
\]

**Boundary:** identifying a physical subsystem is not yet an experiential conclusion.

**Go deeper:** [P1 representation invariance](proposition_1_representation_invariance.md) · [Theorem Roadmap](theorem_roadmap.md)

---

## 2. Which descriptions count as the same physical situation?

A scientifically meaningful bridge should not change merely because we relabel variables or choose an equivalent representation.

Declare an equivalence relation

\[
\boxed{p\sim_P p'}
\]

and work with the physical quotient

\[
\boxed{\mathcal Q_P=\mathcal P/{\sim_P}.}
\]

P1 gives the exact condition under which a bridge descends consistently to this quotient.

This layer protects the research from confusing **representation choice** with **physical difference**.

**Go deeper:** [P1](proposition_1_representation_invariance.md)

---

## 3. What physical structure might matter?

A candidate physical signature is a representation-independent feature

\[
F_*:\mathcal Q_P\to\mathcal Z_*.
\]

One structured candidate developed in the repository is intervention-resolved causal structure:

\[
\boxed{F_{\mathrm{causal}}(p)=[\mathfrak C_p]_{\cong}}
\]

with

\[
\mathfrak C_p=(V,\mathcal U_p,\mathcal T,\mathcal G_p,\mathcal A_p,\mathcal K_p).
\]

Its components encode intervention-response geometry, directed perturbational influence, and partition-sensitive response irreducibility.

P12 and P13 then attack this candidate rather than protecting it: they show that individual components and several reduced summaries can lose information.

**Why this layer exists:** a single convenient scalar should not be promoted to a complete physical signature without surviving collision and insufficiency tests.

**Go deeper:** [P11](proposition_11_intervention_resolved_causal_structure.md) · [P12](proposition_12_component_insufficiency.md) · [P13](proposition_13_pairwise_component_irredundancy.md)

---

## 4. How does physical organization persist through time and scale?

A static physical signature is not enough when the system evolves.

For a finite fingerprint

\[
c_t=(g_t,a_t,k_t),
\]

P14 defines a relabeling-invariant distance

\[
\boxed{\overline D_w([c],[c'])=\min_{h\in\mathcal H}D_w(c,hc')}
\]

and path quantities such as

\[
\boxed{
V_{0:T}=\sum_{t=0}^{T-1}\overline D_w([c_t],[c_{t+1}]),
\qquad
J_{0:T}=\max_t\overline D_w([c_t],[c_{t+1}]).
}
\]

P15 then propagates finite estimation error:

\[
\boxed{|\widehat d_{st}-d_{st}|\le\varepsilon_s+\varepsilon_t.}
\]

Later physical branches study composition, coarse-graining, aggregation, intervention quotients, delay quotients, and multiscale compatibility.

**Boundary:** continuity of a physical structure is not automatically continuity of experience.

**Go deeper:** [P14](proposition_14_temporal_continuation.md) · [P15](proposition_15_finite_sample_temporal_certification.md) · [P25-P37 via the Theorem Roadmap](theorem_roadmap.md)

---

## 5. What is the target, and is it independent?

The physical side alone does not define what is being explained.

Let \(\mathcal E\) denote a declared target or experiential domain, with equivalence relation

\[
e\sim_E e'.
\]

The corresponding quotient is

\[
\boxed{\mathcal Q_E=\mathcal E/{\sim_E}.}
\]

The key scientific requirement is not merely to write down \(\mathcal E\), but to justify the target independently of the physical descriptor being tested.

This is why the later target-side branch returns explicitly to target provenance, noisy measurement, identifiability, and finite-data recovery.

**Boundary:** a latent variable, report channel, label, or learned target is not automatically an experiential ground truth.

**Go deeper:** [Bridge Problem](bridge_problem.md) · [P71-P74 via Research Navigation](research_navigation.md)

---

## 6. What would a bridge actually be?

The most general bridge begins as a relation

\[
\mathcal B\subseteq\mathcal P\times\mathcal E.
\]

When single-valuedness and invariance are justified, it can be represented as

\[
\boxed{\bar B:\mathcal Q_P\longrightarrow\mathcal Q_E.}
\]

The strongest physical-signature goal would be a signature that preserves exactly the distinctions the bridge preserves:

\[
\boxed{F_*(p)=F_*(p')\iff\bar B(p)=\bar B(p').}
\]

Propositions 5 and 6 formalize feature sufficiency and canonical bridge completeness in this sense.

P19 later asks a more directly testable sufficiency question: does an independently declared target factor through the chosen physical descriptor?

**Go deeper:** [P5](proposition_5_feature_sufficiency.md) · [P6](proposition_6_canonical_bridge_signature.md) · [P19](proposition_19_fundamental_physical_sufficiency.md)

---

## 7. How does the theory meet observable data?

A scientific theory must imply observable probability laws under declared experimental protocols.

Write those laws schematically as

\[
P_{\mathfrak T}^{\pi,q}.
\]

The early identifiability results ask whether competing theories or physical signatures can be distinguished by available experiments.

For a family of protocols \(\Pi\), an experimental fingerprint can be written as

\[
\Psi_\Pi(p)=(P^{\pi,p})_{\pi\in\Pi}.
\]

P7-P10 study recoverability, finite error, sample complexity, and robust experimental design.

One representative finite-data condition takes the form

\[
\boxed{\gamma_S=\delta_S-\omega_S>4\varepsilon}
\]

with corresponding sample-size guarantees under the declared finite-alphabet setting.

**Why this layer exists:** a bridge that cannot be connected to observable consequences cannot yet be scientifically tested.

**Go deeper:** [P2-P10 via the Theorem Roadmap](theorem_roadmap.md) · [Candidate Theory Families](candidate_theory_families.md)

---

## 8. Can the physical descriptor fail a sufficiency test?

This is the core transition from architecture to falsifiable bridge methodology.

P19 asks whether the target depends on the underlying state only through the declared physical descriptor. If not, the descriptor is insufficient for that target under the stated model.

Later results add finite-data confidence, refinement tests, adaptive selection protection, and repeated-look validity.

The important asymmetry is:

> **failure of a descriptor is evidence against that descriptor's sufficiency, not proof that no physical description could ever be sufficient.**

**Go deeper:** [P19](proposition_19_fundamental_physical_sufficiency.md) · [P20-P24 via the Theorem Roadmap](theorem_roadmap.md)

---

## 9. Can the target-measurement model itself fail?

A clean physical descriptor and an independently motivated target are still not enough if the measurement model is wrong.

P71-P74 protect target provenance and measurement. P75-P87 then progressively strengthen model-adequacy and model-separation tests.

The logic is:

**identify the model → test its restrictions → test the whole model family → strengthen the separating observables when weaker tests remain silent.**

This is where the current theorem frontier sits.

**Current frontier:** [P87](proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md)

**Audit route:** [Research Navigation](research_navigation.md)

---

## 10. How are uncertainty and computation certified?

Finite data and numerical optimization can create false confidence if their error direction is not controlled.

The repository therefore distinguishes:

- empirical point estimates from finite-sample certificates;
- numerical candidates from certified lower or upper bounds;
- model non-rejection from model validation;
- exploratory search from formally protected inference.

The reproducibility layer connects theorem statements to implementation, tests, figure generation, and repository-wide verification.

**Go deeper:** [Reproducibility Guide](reproducibility.md) · [Equation and Citation Map](equation_and_citation_map.md)

---

## 11. What would count as a completed bridge result?

Only after the physical domain, target domain, bridge premises, empirical interface, identifiability, finite-data uncertainty, model adequacy, and falsification conditions are explicit should a final bridge theorem be considered.

The schematic target remains

\[
\boxed{
\text{physical first principles}
+
\text{independently justified bridge premises}
+
\text{empirical and finite-data certification}
\Longrightarrow
\text{formal experiential property}.
}
\]

The repository has not established that final implication.

**Go deeper:** [Universal Consciousness Proof Target](universal_proof_target.md)

---

## Architecture at a glance

| Layer | Question | Status |
| --- | --- | --- |
| Physical realization | What system and dynamics are declared? | Formalized |
| Representation invariance | Which descriptions count as physically equivalent? | Formalized |
| Physical signature | What structured physical features are candidates? | Partially developed and stress-tested |
| Time / scale / composition | Which structures persist under change of description? | Developed across multiple branches |
| Target definition | What distinction is being explained? | Requires independent scientific justification |
| Bridge | What connects physical and target structure? | Open |
| Empirical interface | What observable laws follow? | Formalized for declared model classes |
| Sufficiency testing | Is the descriptor enough for the target? | Theorem and finite-data machinery developed |
| Target-model adequacy | Does the declared measurement model fit? | Active theorem frontier through P87 |
| Reproducibility | Can the reasoning and computation be audited? | Implemented repository-wide |
| Final physical-to-experiential bridge | Has the bridge itself been established? | **Open** |

---

## Where to go next

**Need less technical context?** Go back to the [Research Map](research_map.md).

**Want dependency structure?** Open the [Theorem Roadmap](theorem_roadmap.md).

**Want one proposition at a time?** Open the [Detailed Proposition Record](detailed_proposition_record.md).

**Want equations, sources, code, and tests?** Use [Research Navigation](research_navigation.md) and the [Equation and Citation Map](equation_and_citation_map.md).

**Want to reproduce the work?** Use the [Reproducibility Guide](reproducibility.md).
