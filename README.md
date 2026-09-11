# Mathematical Consciousness Bridge

[![tests](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/test.yml/badge.svg)](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/test.yml)
[![version](https://img.shields.io/badge/version-0.73.0-2563eb)](CITATION.cff)
[![license](https://img.shields.io/badge/license-MIT-059669)](LICENSE)

**Mahsa Keikha, PhD**

> **What mathematical and physical conditions would be required for a complete physical description of a system to support a scientifically testable claim about consciousness?**

This repository is a mathematical-physics research program for the **physical-to-experiential bridge problem**. It does not begin by assuming what consciousness is. It asks what must be true before any proposed physical description can legitimately be called sufficient for an independently specified experiential target, how that sufficiency can be falsified, and how finite experiments can distinguish a real bridge from correlation, representation choice, coarse-graining, target circularity, target-measurement error, measurement-channel non-identifiability, or statistical noise.

![Research architecture](docs/figures/research_architecture.svg)

**Figure 1. Scientific architecture of the project.** The research moves from physical dynamics to operationally measurable structure, then to mathematical sufficiency tests, target-side validity, finite-data certification, experimental design, and finally the still-open physical-to-experiential bridge. The arrows are logical dependencies, not claims that one layer has already been identified with consciousness.

---

# What this project is trying to achieve, in plain language

Physics can tell us how a system changes. Neuroscience can measure electrical, chemical, hemodynamic, behavioral, and perturbational responses. Information theory can quantify dependence. Causal inference can distinguish observation from intervention. Quantum mechanics can specify states, channels, and measurement statistics. None of these facts, by themselves, tell us whether a physical description contains all distinctions required to determine an experiential variable.

The central problem is therefore not to search for an impressive scalar and label it consciousness. It is to ask a stricter question:

> Given a declared physical description, can an independently justified target be determined from it, or can we construct a reproducible counterexample showing that physically indistinguishable cases remain target-distinguishable?

The word **independently** is now formalized through a target-side sequence. P71 proves that a target constructed from the tested physical descriptor makes the bridge test circular. P72 shows that even a non-circular latent target may be observed through a noisy channel that attenuates or erases evidence. P73 then asks whether the binary channel-stability quantity used by P72 can itself be identified from repeated target views rather than merely assumed. Under a declared three-view binary symmetric, conditionally independent model, it can; with only two heterogeneous views, it cannot.

A credible bridge experiment must therefore justify the **target-construction protocol**, the **target-measurement protocol**, and any assumptions used to calibrate the target-measurement channel.

The working chain is

$$
\boxed{
\text{physical dynamics}
\to
\text{operational structure}
\to
\text{non-circular target}
\to
\text{measurement-aware target observation}
\to
\text{measurement-channel calibration}
\to
\text{sufficiency / insufficiency test}
\to
\text{finite-data certificate}
\to
\text{bridge law or falsification}
}
$$

The research currently contains **73 proposition-level results** and **62 equation-driven quantitative figures**. The theorem frontier is P73. The physical-to-experiential bridge itself remains open.

This project continues [Spatiotemporal Observer Mathematics](https://github.com/MahsaKeikha/spatiotemporal-observer-math), which addresses the prior physical problem of identifying a persistent moving subsystem from measured dynamics.

---

# Abstract

Let $\Omega$ denote the physically admissible state or history space, let $T:\Omega\to\mathcal T$ be a declared physical descriptor, and let $E:\Omega\to\mathcal E$ be an independently specified target representing the distinctions a proposed bridge claims to explain. The deterministic bridge question is whether there exists a map $B$ such that $E=B\circ T$. The stochastic version asks whether the conditional target law factors through $T$, equivalently whether the residual $I(E;\Omega\mid T)$ vanishes under the declared probabilistic model. The smooth version yields a differential rank obstruction.

The program develops the structures required to make those tests scientifically meaningful: intervention-conditioned response laws, causal influence, temporal continuation, composition defects, coarse-graining and reconstruction bounds, multiscale operational quotients, finite-sample confidence certificates, quantum-state model-set tests, adaptive experiment design, scheduling, and certified resource allocation.

P71 adds a non-circularity theorem: if a target is constructed as $E=h(T)$, or through a descriptor-only stochastic channel, successful factorization is guaranteed by construction and has no independent evidential force. P72 adds a target-measurement theorem. If an independently justified latent target $E^\star$ is observed as $Y$ through a declared nondifferential channel satisfying $Y\perp\!\!\!\perp\Omega\mid(E^\star,T)$, then

$$
\boxed{I(Y;\Omega\mid T)\le I(E^\star;\Omega\mid T).}
$$

Target measurement can therefore attenuate or erase a genuine population witness, but under that model it cannot create a positive observed residual from a latent target already screened off by $T$.

P73 addresses one assumption left open by P72. For a latent binary target $Z$ and three repeated target views $Y_i=ZN_i$ with mutually independent binary noises independent of $Z$, define $r_i=\mathbb E[N_i]$, $\gamma_i=|r_i|$, and $m_{ij}=\mathbb E[Y_iY_j]$. Then

$$
\boxed{m_{ij}=r_ir_j.}
$$

Two heterogeneous views identify only one product and therefore do not identify the two individual channel stabilities. Three nonzero compatible views identify

$$
\boxed{
\gamma_1=\sqrt{\frac{m_{12}m_{13}}{m_{23}}},
\quad
\gamma_2=\sqrt{\frac{m_{12}m_{23}}{m_{13}}},
\quad
\gamma_3=\sqrt{\frac{m_{13}m_{23}}{m_{12}}}.
}
$$

The signed reliability vector remains ambiguous under one global latent-label orientation, but the P72 stability magnitudes are unique. P73 also gives simultaneous finite-sample stability intervals. These results are conditional on the declared repeated-view model and do not establish that real experiential measurements satisfy it.

These results establish a rigorous **test architecture**, not a completed ontology of consciousness.

---

# Scientific status discipline

| Status | Meaning in this project |
| --- | --- |
| **Definition** | A mathematical object introduced for the framework. |
| **Proved** | A theorem derived from explicit assumptions. |
| **Implemented** | Executable code mirrors a stated theorem or procedure. |
| **Numerically verified** | A simulation or computation checks an implementation or example. |
| **Empirically supported** | The statement depends on external published experimental evidence. |
| **Synthetic example** | A controlled example used to expose logic, failure modes, or calibration behavior. |
| **Hypothesis** | A scientifically motivated proposal not yet established by theorem or experiment. |
| **Open bridge problem** | A physical-to-experiential identification has not been derived. |

This distinction is central. The repository **does not assume that a physical quantity is consciousness**. It does not identify consciousness with entropy, integration, complexity, synchronization, entanglement, coherence, measurement, a state of matter, or an additional spacetime coordinate.

**Quantum mechanics does not by itself imply consciousness.** A complete quantum state specifies the outcome statistics of declared measurements, but an experiential conclusion requires an additional bridge statement unless that bridge is independently derived.

Likewise, a latent target symbol such as $E^\star$ is not a declaration of experiential ground truth. P71-P73 formalize target-side obligations that must be satisfied before such a target can carry bridge evidence.

---

# The core scientific thesis in one view

A descriptor $T$ partitions the admissible physical domain into fibers

$$
[\omega]_T=\{\omega'\in\Omega:T(\omega')=T(\omega)\}.
$$

A deterministic bridge through $T$ can exist only if the target is constant on every fiber:

$$
\boxed{
T(\omega_1)=T(\omega_2),
\quad
E(\omega_1)\ne E(\omega_2)
\quad\Longrightarrow\quad
E\ne B\circ T.
}
$$

The stochastic analogue uses

$$
\boxed{R_{\mathrm{stoch}}(T)=I(E;\Omega\mid T).}
$$

But those equations have evidential content only after target provenance and target measurement are justified. If the target is latent, any claimed channel-stability bound must also be supported by calibration data or by explicit assumptions whose adequacy can be challenged.

| Layer | Mathematical object | Scientific question | Failure witness |
| --- | --- | --- | --- |
| Physical description | $T(\omega)$ | Is the declared physics represented without arbitrary coordinate dependence? | Representation or identifiability failure |
| Operational structure | response laws and causal geometry | Do interventions expose physically meaningful distinctions? | Collision or missing causal distinction |
| Target provenance | target-construction protocol | Was the target defined independently of the tested descriptor? | Descriptor-derived target, P71 |
| Target measurement | $K_t(y\mid e)$ | Does noisy observation preserve the relevant target distinctions? | Erasure or differential measurement, P72 |
| Channel calibration | repeated-view moments or other calibration data | Is the stability used by the bridge test identified rather than assumed? | Two-view underdetermination or model failure, P73 |
| Bridge sufficiency | $E=B\circ T$ | Is the target constant on physical fibers? | Same $T$, different $E$ |
| Stochastic sufficiency | $I(E;\Omega\mid T)$ | Is target-relevant information left outside $T$? | Certified positive residual |
| Scale stability | coarse-graining plus reconstruction | Does relevant physical structure survive a change of resolution? | Uncontrolled reconstruction or distortion |
| Quantum sufficiency | $\rho$, channels, measurement statistics | Does the target factor through the declared operational quantum state? | Regularity-aware non-factorization witness |
| Finite experiment | confidence regions and stopping rules | Can a witness survive uncertainty and adaptive sampling? | Confidence or design assumptions fail |

This is the scientific contribution of the project at its current stage: **a bridge claim is decomposed into separately auditable mathematical obligations instead of being hidden inside a single proposed consciousness quantity.**

---

# How to read this study

The main page is organized as a scientific argument rather than a chronological project log. A first-time reader can follow the core argument and use the direct links below for details. Detailed proposition chronology and downstream calibration mathematics remain on separate pages so they do not interrupt the main scientific path.

| Reader question | Where the answer appears |
| --- | --- |
| **What is the scientific problem?** | [Abstract](#abstract), [core scientific thesis](#the-core-scientific-thesis-in-one-view), [Research at a glance](#research-at-a-glance), and [Section 1: Mathematical formulation of the bridge problem](#1-mathematical-formulation-of-the-bridge-problem) |
| **What exactly is being measured and compared?** | [Section 1](#1-mathematical-formulation-of-the-bridge-problem), [Section 2](#2-from-physical-dynamics-to-operational-structure), [Section 3](#3-time-composition-and-scale-cannot-be-ignored), [Section 4](#4-turning-a-population-theorem-into-a-finite-experiment), [measurement map](docs/figures/conscious_state_measurement_map.svg), and [response-geometry map](docs/figures/information_geometry_response_manifold.svg) |
| **How do we avoid circular targets?** | [P71](docs/proposition_71_target_provenance_noncircularity.md) |
| **How does noisy target measurement affect evidence?** | [P72](docs/proposition_72_target_measurement_channel_robustness.md) |
| **When can a binary target channel be calibrated without latent ground truth?** | [P73](docs/proposition_73_three_view_target_channel_identifiability.md) and its [provenance record](docs/p73_equation_provenance.md) |
| **What has actually been proved?** | [Scientific status discipline](#scientific-status-discipline), [Theorem roadmap](docs/theorem_roadmap.md), and [What has actually been established](#what-has-actually-been-established) |
| **What would falsify the framework or a candidate bridge?** | [Falsification logic](#falsification-logic) and the [Falsification program](docs/falsification_program.md) |
| **What remains unknown?** | [What remains open](#what-remains-open), [Current scientific status](#current-scientific-status), [Research navigation](docs/research_navigation.md), [Detailed proposition record](docs/detailed_proposition_record.md), and the [Calibration and Optimization Frontier](docs/calibration_optimization_frontier_p61_p70.md) |

![Universal proof ladder](docs/figures/universal_proof_ladder.svg)

**Figure 2. Scientific proof ladder.** A credible consciousness bridge must pass distinct layers: physical well-definedness, experiential well-definedness, non-circular bridge premises, representation invariance, physical-feature sufficiency, experimental recoverability, competing-theory discrimination, finite-data support, and explicit falsification. The figure is a requirements map, not a claim that every layer has already been closed.

---

# Research at a glance

| Stage | Results | Scientific question | Status | Main entry point |
| --- | --- | --- | --- | --- |
| 1. Foundations and identifiability | **P1-P10** | What must be invariant, distinguishable, recoverable, and statistically testable? | Proved / implemented / tested | [Theorem roadmap](docs/theorem_roadmap.md) |
| 2. Causal, temporal, compositional, and scale structure | **P11-P18** | Which structured physical distinctions survive interventions, time, composition, and coarse-graining? | Proved / implemented / tested | [Quantitative atlas](docs/quantitative_physics_mathematics_atlas.md) |
| 3. Bridge sufficiency and target validity | **P19-P24, P71-P73** | Does an independently justified, adequately measured, and defensibly calibrated target factor through the physical descriptor? | Proved under declared models | [Research navigation](docs/research_navigation.md) |
| 4. Multiscale operational structure | **P25-P37** | Which causal and response structures survive node, state, intervention, and delay quotients? | Proved / implemented / tested | [Theorem roadmap](docs/theorem_roadmap.md) |
| 5. Quantum sufficiency and falsification | **P38-P44** | What follows from a declared operational quantum description, and what does not? | Conditional tests proved; ontology open | [Quantum foundations](docs/quantum_foundations_and_bridge_test.md) |
| 6. Adaptive experiment design and scheduling | **P45-P60** | How should evidence gathering, stopping, service allocation, switching, and calibration be organized? | Proved / implemented / tested | [Equation and citation map](docs/equation_and_citation_map.md) |
| 7. Calibration and integer optimization | **P61-P70** | How should downstream finite calibration resources be allocated and certified? | Proved / implemented / tested | [Calibration and Optimization Frontier](docs/calibration_optimization_frontier_p61_p70.md) |

The dependency-oriented theorem map covers **P1 through P73 with explicit dependency branches**.

![Theorem roadmap](docs/figures/theorem_roadmap.svg)

**Figure 3. Theorem dependency map.** Proposition numbers preserve development order, while the dependency map shows scientific order. P71-P73 return to the P19 target-sufficiency lineage; P61-P70 remains a separate downstream optimization branch.

---

# 1. Mathematical formulation of the bridge problem

## 1.1 Physical states, descriptors, and targets

Let

$$
\Omega=\{\text{physically admissible states or histories}\},
\qquad
T:\Omega\to\mathcal T.
$$

Independently, let

$$
E:\Omega\to\mathcal E
$$

represent the target distinctions the proposed bridge claims to determine.

| Symbol | Role | Scientific requirement |
| --- | --- | --- |
| $\Omega$ | admissible states or histories | declared relative to a physical model and experiment class |
| $T$ | physical descriptor | operationally defined, representation-aware, and recoverable |
| $E$ | target | justified independently enough to avoid definitional circularity |
| $E^\star$ or $Z$ | latent target in P72-P73 | not assumed to be consciousness; provenance and measurement must be justified |
| $Y$ or $Y_i$ | observed target measurement | related to the latent target through an explicit observation model |
| $B$ | candidate bridge law | maps physical equivalence classes to target distinctions |

The target is intentionally not equated with verbal report or overt responsiveness. Dreaming, anesthesia, perturbational complexity, and covert command-related brain activation motivate keeping behavior, report, neural evidence, and experiential inference distinct.

![Conscious-state measurement and dissociation map](docs/figures/conscious_state_measurement_map.svg)

**Figure 4. Measurement and dissociation map.** Behavioral responsiveness, subjective report, perturbational complexity, and command-related brain activation are different evidence channels. A bridge theory must state which observable pattern it predicts and what target those observations are claimed to measure.

## 1.2 Exact deterministic sufficiency

The physical descriptor is exactly sufficient for the target if

$$
\boxed{E=B\circ T.}
$$

Equivalently,

$$
\boxed{
T(\omega_1)=T(\omega_2)
\Longrightarrow
E(\omega_1)=E(\omega_2).
}
$$

One exact same-$T$/different-$E$ pair rules out factorization through the declared descriptor.

## 1.3 Stochastic sufficiency

For finite stochastic variables,

$$
\boxed{R_{\mathrm{stoch}}(T)=I(E;\Omega\mid T).}
$$

If $T_f$ refines $T_c$ through $T_c=c\circ T_f$, P21 gives

$$
\boxed{
R_{\mathrm{stoch}}(T_c)-R_{\mathrm{stoch}}(T_f)
=I(E;T_f\mid T_c).
}
$$

## 1.4 Smooth differential obstruction

If a differentiable local bridge exists, then

$$
dE_x=dB_{T(x)}\circ dT_x,
$$

so

$$
\boxed{\operatorname{rank}(dE_x)\le\operatorname{rank}(dT_x).}
$$

A positive rank excess supplies a local obstruction to the declared smooth factorization.

![Fundamental theory to consciousness map](docs/figures/fundamental_theory_consciousness_map.svg)

**Figure 5. The logical gap being tested.** Fundamental physical theory determines physical structure and operational predictions. A consciousness theory still requires a justified map from physical equivalence classes to target equivalence classes.

## 1.5 P71: target provenance cannot be circular

If the target is defined from the tested descriptor,

$$
E_h=h(T),
$$

then

$$
E_h=h\circ T,
\qquad
I(E_h;\Omega\mid T)=0
$$

hold by construction. A held-out learned rule $h_D(T)$ remains descriptor-derived after training. P71 also proves that an observed zero residual cannot, from the joint law alone, establish that the target had independent provenance.

![P71 target-provenance non-circularity](docs/figures/p71_target_provenance_noncircularity.svg)

**Figure 6. P71 non-circularity theorem.** A descriptor-derived target automatically respects descriptor fibers, whereas a separately declared synthetic target can expose same-descriptor/different-target collisions. The synthetic example illustrates theorem logic; it is not claimed to be an experiential variable.

Direct proof: [Proposition 71](docs/proposition_71_target_provenance_noncircularity.md).

## 1.6 P72: noisy target observation is a separate scientific layer

Let $E^\star$ be a latent target that has passed the P71 provenance requirement and let $Y$ be its observation. Under

$$
\boxed{Y\perp\!\!\!\perp\Omega\mid(E^\star,T),}
$$

P72 proves

$$
\boxed{I(Y;\Omega\mid T)\le I(E^\star;\Omega\mid T).}
$$

Thus a certified positive observed population residual transfers to the latent target under the measurement model. A zero observed residual does not transfer in the opposite direction because an erasing channel can hide a positive latent residual.

For a finite target channel $K_t$, P72 defines the stability coefficient

$$
\gamma_t=
\inf_{\substack{v\ne0\\\mathbf1^\top v=0}}
\frac{\|K_tv\|_1}{\|v\|_1}
$$

and obtains

$$
\boxed{
\gamma_t\operatorname{TV}(p,q)
\le
\operatorname{TV}(K_tp,K_tq)
\le
\operatorname{TV}(p,q).
}
$$

For binary symmetric measurement noise with error rate $\eta$,

$$
\boxed{\gamma=|1-2\eta|.}
$$

![P72 target-measurement channel robustness](docs/figures/p72_target_measurement_channel_robustness.svg)

**Figure 7. P72 target-measurement theorem.** Nondifferential target noise can attenuate or erase a real bridge witness, but cannot create a positive population residual from a screened-off latent target. The binary channel exposes the exact erasure point at $\eta=1/2$, and the finite-data panel shows how measurement stability enters the sample burden.

Direct proof: [Proposition 72](docs/proposition_72_target_measurement_channel_robustness.md). Equation classification: [P72 provenance record](docs/p72_equation_provenance.md).

## 1.7 P73: three repeated views can identify binary channel stability under a declared model

Let $Z\in\{-1,+1\}$ be the latent target and let

$$
Y_i=ZN_i,
\qquad i\in\{1,2,3\},
$$

where the binary noises $N_i$ are mutually independent and independent of $Z$. With

$$
r_i=\mathbb E[N_i],
\qquad
\gamma_i=|r_i|,
\qquad
m_{ij}=\mathbb E[Y_iY_j],
$$

P73 gives

$$
\boxed{m_{ij}=r_ir_j.}
$$

Two heterogeneous views reveal only $|m_{12}|=\gamma_1\gamma_2$, so their individual stabilities remain underdetermined. Three nonzero compatible pair moments identify all three magnitudes:

$$
\boxed{
\gamma_1=\sqrt{\frac{m_{12}m_{13}}{m_{23}}},
\quad
\gamma_2=\sqrt{\frac{m_{12}m_{23}}{m_{13}}},
\quad
\gamma_3=\sqrt{\frac{m_{13}m_{23}}{m_{12}}}.
}
$$

The signed reliabilities remain ambiguous under one global sign flip. P73 also constructs simultaneous finite-sample intervals for the three stability magnitudes from empirical pair moments. These conclusions fail if the repeated-view independence or binary symmetric channel assumptions fail.

![P73 three-view target-channel identifiability](docs/figures/p73_three_view_target_channel_identifiability.svg)

**Figure 8. P73 identifiability boundary.** Two heterogeneous views leave a continuum of compatible stability pairs. Under the declared three-view model, three nonzero pair moments identify the P72 stability magnitudes, and finite moment bands propagate into calibration intervals. This is a measurement-model theorem, not empirical evidence that any particular report, rater, or neural measure is a valid experiential target.

Direct proof: [Proposition 73](docs/proposition_73_three_view_target_channel_identifiability.md). Equation classification: [P73 provenance record](docs/p73_equation_provenance.md).

---

# 2. From physical dynamics to operational structure

A useful bridge test cannot depend only on coordinates or passive correlations. P11 builds an intervention-resolved physical candidate from response geometry, directed influence, and partition irreducibility.

![Causal structure anatomy](docs/figures/causal_structure_anatomy.svg)

**Figure 9. Anatomy of the operational physical candidate.** Controlled interventions generate response distributions. Distances define response geometry; matched perturbations define directed influence; comparisons with partition-product nulls expose irreducibility. These are physical candidates to be tested for sufficiency, not definitions of consciousness.

![Information geometry of intervention-response laws](docs/figures/information_geometry_response_manifold.svg)

**Figure 10. Response laws as a physical geometry.** Parameterized intervention-conditioned probability laws can be studied using operational distances and local statistical geometry. An experiential geometry would still require a separately justified bridge.

P12 then uses constructive collisions to show why compressed components or attractive scalars cannot simply be assumed sufficient.

![Constructive component collisions](docs/figures/p12_collision_map.svg)

**Figure 11. Constructive collision tests.** A compressed physical feature must earn sufficiency by factorization or reconstruction, not by visual plausibility or correlation.

---

# 3. Time, composition, and scale cannot be ignored

P14 treats temporal continuation as a path property rather than endpoint identity.

![Temporal continuation](docs/figures/p14_temporal_continuation.svg)

**Figure 12. Temporal continuation.** Representation-equivalent descriptions are quotiented out while local structural changes are accumulated along a trajectory. Endpoint equality alone cannot certify a continuous physical history.

For deterministic coarse observation, total variation contracts. P18 adds an approximate reconstruction condition that bounds the distortion of the relevant response geometry.

![Scale sufficiency certificate](docs/figures/p18_scale_sufficiency_certificate.svg)

**Figure 13. Scale sufficiency logic.** Coarse-graining can erase distinctions, but reconstruction control bounds how much declared response geometry was lost.

![Multiscale physical hierarchy](docs/figures/multiscale_physical_hierarchy.svg)

**Figure 14. Multiscale hierarchy.** A scientifically credible descriptor must state which objects survive changes of scale, which require compatibility conditions, and which acquire bounded distortion.

---

# 4. Turning a population theorem into a finite experiment

Exact mathematical insufficiency becomes scientifically useful only when finite observations support it with controlled error.

P20 constructs a finite-sample confidence interval for the P19 conditional-information residual under a declared finite-alphabet IID model. P22-P24 extend the same discipline across refinement families, adaptive selection, repeated looks, and finite stopping times.

![Finite-sample residual certificate](docs/figures/p20_finite_sample_residual_certificate.svg)

**Figure 15. From exact factorization to finite-data evidence.** A bridge claim is rejected only when a confidence-controlled lower bound remains positive under the declared sampling assumptions.

P72 applies the same philosophy on the target side. P73 then adds a separate calibration confidence event when a binary measurement stability is estimated from repeated views. If calibration data and bridge-test data are independent, their failure probabilities can be combined explicitly. If the same data are reused, a joint or sample-split analysis is required.

---

# 4.4 Fundamental theory / Theory-of-Everything interface

The bridge framework remains compatible with future changes in fundamental physics. There is currently no experimentally established Theory of Everything that has separately been shown to determine experiential variables.

For bookkeeping, a broad physical descriptor may be written schematically as

$$
\boxed{T(\Omega)=\bigl(G(\Omega),Q(\Omega),C(\Omega)\bigr),}
$$

where $G$ denotes geometric information, $Q$ quantum-operational information, and $C$ effective causal or classical structure under the declared model. This notation is an interface, not a claim that these components are fundamental or complete.

Thomas W. Campbell's *My Big TOE* and similar consciousness-first proposals are treated, if mentioned, only as speculative falsifiable antecedents, not as established premises in the theorem chain.

![Observer-to-bridge research handoff](docs/figures/observer_to_bridge_handoff.svg)

**Figure 16. Research handoff.** The preceding observer-mathematics project identifies and statistically certifies a physical subsystem. This repository begins after that physical object is declared and asks what additional physical, target, and bridge conditions are required. No experiential property is inserted at the handoff.

---

# 5. Quantum mechanics enters as a physical description, not as an assumption about consciousness

For a finite-dimensional quantum system, a state is represented by a density operator $\rho$. A POVM $\{M_a\}$ gives

$$
\boxed{p(a\mid M)=\operatorname{Tr}(\rho M_a).}
$$

The bridge question is whether an independently justified target factors through the declared operational quantum state under an explicitly declared bridge class.

![Quantum bridge completeness map](docs/figures/quantum_bridge_completeness_map.svg)

**Figure 17. Quantum completeness versus experiential completeness.** Tomographic completeness closes the declared operational quantum description. It does not automatically close the physical-to-experiential map.

![Quantum operational sufficiency](docs/figures/p38_quantum_operational_sufficiency.svg)

**Figure 18. P38 quantum sufficiency test.** Equal declared quantum descriptors with unequal independently defined targets give an exact non-factorization witness. Finite data require uncertainty-aware replacements for exact equality.

P40 proves that finite sampled-state injectivity alone permits unrestricted lookup-table factorization, so meaningful continuous-region non-factorization requires a declared regularity class.

![Trace-ball quantum envelope](docs/figures/p41_trace_ball_quantum_envelope.svg)

**Figure 19. Finite-data quantum envelope.** Quantum-state confidence regions and target uncertainty are propagated into an end-to-end regularity obstruction. The scientific conclusion is conditional on tomography coverage, the target measurement model, and the declared bridge regularity.

For the complete QM01-QM18 visual sequence, see [Quantum foundations and bridge test](docs/quantum_foundations_and_bridge_test.md).

---

# 6. Adaptive experiment design: collecting evidence without invalidating it

P45-P58 develop shared preparation graphs, time-uniform confidence sequences, adaptive sampling, safe pruning, stopping complexity, service allocation, switching costs, and finite-data transition uncertainty. P59-P60 begin the transition-calibration branch.

![Sequential graph refinement](docs/figures/p47_sequential_graph_refinement.svg)

**Figure 20. Adaptive evidence collection.** The experiment may choose what to sample next based on previous observations, but validity is protected by a shared time-uniform confidence event.

---

# 7. Calibration and optimization as a downstream experimental layer

The detailed P61-P70 sequence belongs to the experimental implementation layer. It allocates and certifies finite calibration resources after the bridge hypothesis, physical descriptor, target protocol, witness family, uncertainty model, and experimental constraints have been declared.

**[Read the complete Calibration and Optimization Frontier: P61-P70](docs/calibration_optimization_frontier_p61_p70.md).**

This branch remains intentionally separate from P71-P73. Better optimization can make an experiment more efficient; it cannot rescue a circular target, an erasing target-measurement channel, or a channel-calibration model whose assumptions are false.

---

# What has actually been established

The strongest current conclusions are methodological and conditional:

1. Exact physical sufficiency is equivalent to constancy of the target on descriptor fibers.
2. Stochastic insufficiency can be quantified with $I(E;\Omega\mid T)$ under a declared model.
3. Smooth factorization has a local rank obstruction.
4. Operational physical structure can include intervention response, directed influence, irreducibility, temporal continuation, composition, and scale.
5. Coarse-graining loss can be bounded under explicit reconstruction assumptions.
6. Finite-data uncertainty can be propagated into bridge tests.
7. Adaptive evidence collection can remain valid under declared non-anticipating procedures.
8. Quantum operational completeness can be separated from experiential completeness.
9. P71 proves that descriptor-derived targets cannot independently validate sufficiency of the same descriptor.
10. P72 proves that, under a nondifferential target channel, $I(Y;\Omega\mid T)\le I(E^\star;\Omega\mid T)$, while an erasing channel can hide a positive latent residual.
11. P72 also provides target-TV contraction, a channel-stability lower bound, exact binary-symmetric attenuation, and a finite-sample target-separation certificate.
12. P73 proves that two heterogeneous repeated binary views do not identify their individual channel stabilities, while three nondegenerate views identify the three stability magnitudes under the declared independent binary symmetric model.
13. P73 also gives the global label-orientation ambiguity and simultaneous finite-sample stability intervals needed for a calibrated P72 handoff.
14. The experiment-design branch provides scheduling, stopping, calibration, integer optimization, and primal-dual certification without promoting those results into consciousness ontology.

These statements do **not** prove that consciousness is reducible to the current physical descriptors, irreducible to physics, quantum, non-quantum, a field, a state of matter, or an additional dimension.

---

# What remains open

The central bridge remains open. Before a strong bridge claim can be made, the project still needs to close several distinct gaps:

- define experiential variables independently enough to satisfy P71;
- justify how those latent targets are observed and whether the P72 channel premise is defensible;
- test whether the P73 repeated-view independence and binary symmetric assumptions are adequate for the target measurements actually used;
- extend stability identification or sensitivity analysis to correlated, asymmetric, state-dependent, temporal, or multi-class target channels where scientifically justified;
- identify which physical descriptor is justified by experiment rather than convenience;
- test target distinctions across interventions, time, scale, and composition;
- quantify uncertainty strongly enough to rule out estimation artifacts;
- specify the regularity or structural class of admissible bridge laws;
- design decisive experiments for competing bridge theories.

The immediate target-side problem after P73 is **target-channel model adequacy and correlated-error robustness**. Shared bias can make repeated measurements agree even when the conditional-independence model is false. A scientifically useful next theorem should quantify how such dependence perturbs the inferred stability and state observable diagnostics or sensitivity bounds rather than treating agreement as automatic evidence of reliability.

A claim of non-reducibility would require a valid obstruction relative to a sufficiently complete physical description, a scientifically defensible target, a controlled measurement channel, and an admissible bridge class. Failure of one coarse descriptor is not failure of physics.

---

# Falsification logic

| Claim being tested | What would count against it? | What would not be enough? |
| --- | --- | --- |
| Descriptor $T$ is exactly sufficient for $E$ | Same $T$, different independently justified $E$ | Mere correlation |
| Descriptor $T$ is stochastically sufficient | Certified positive $I(E;\Omega\mid T)$ | Positive empirical estimate without uncertainty control |
| Target is independently evidential | Provenance shows it was not constructed from tested $T$ | Train/test separation alone |
| Observed target faithfully supports latent witness | Channel premise or stability fails | Treating a report or label as transparent ground truth |
| P73 repeated-view calibration is valid | Pair moments or external evidence contradict the declared repeated-view model | High raw agreement by itself |
| Coarse scale preserves relevant structure | Reconstruction/distortion bounds fail | Visual similarity |
| Quantum descriptor is sufficient under class $\mathcal B$ | Certified target separation exceeds every admissible bridge image from the quantum confidence region | Numerically close tomography estimates |
| Adaptive experiment is valid | Confidence or non-anticipation assumptions are violated | Adaptivity by itself |
| Integer calibration candidate is optimal | Better feasible allocation or exact solver disproves it | Failure of a sufficient certificate alone |

![Theory-comparative interface](docs/figures/theory_comparison_map.svg)

**Figure 21. Common interface for competing theory families.** Existing consciousness theories and the repository's intervention-resolved physical candidate can be compared through physical feature family, bridge architecture, target construction, measurement interface, and discriminating experiment rather than by assuming one theory is the default answer.

See the [Falsification program](docs/falsification_program.md) for explicit repository-level failure conditions.

---

# Evidence, references, and provenance

The repository keeps standard mathematics, physical theory, empirical evidence, repository-original derivations, and speculative antecedents distinct.

| Resource | Purpose |
| --- | --- |
| [Equation and citation map](docs/equation_and_citation_map.md) | Standard versus repository-derived equations and theorem lineage |
| [P72 equation and provenance record](docs/p72_equation_provenance.md) | Target-measurement theorem equation classification and external context |
| [P73 equation and provenance record](docs/p73_equation_provenance.md) | Repeated-view identifiability, finite stability calibration, and methodological provenance |
| [Foundational physics and mathematics bibliography](docs/foundational_physics_mathematics_bibliography.md) | Mathematics, physics, information theory, and causal inference sources |
| [Literature map](docs/literature_map.md) | Consciousness theory and empirical comparison literature |
| [`fundamental_theory_references.bib`](docs/fundamental_theory_references.bib) | Machine-readable fundamental-physics references |
| [Reference audit](docs/reference_audit.md) | Evidence-role and metadata audit |
| [Citation and reference policy](docs/citation_and_reference_policy.md) | Attribution and scientific sourcing rules |

Selected foundations include Shannon (1948), Cover and Thomas (2006), Pearl (2009), Lee (2013), Amari (2016), Landauer (1961), Casali et al. (2013), Tegmark (2015), Seth and Bayne (2022), Cogitate Consortium et al. (2025), Luppi et al. (2026), Siclari et al. (2017), Sarasso et al. (2015), and Claassen et al. (2019). P73 additionally uses Dawid and Skene (1979) and Allman, Matias, and Rhodes (2009) as methodological context for observer-error and latent-structure identifiability, while deriving its narrow binary formulas directly from the declared model.

---

# Complete visual evidence without front-page overload

The main page shows only the figures needed to recover the scientific argument. The complete visual record remains available separately.

| Visual collection | What it contains |
| --- | --- |
| [Visual atlas](website/visual-atlas.html) | Browser-oriented gallery of scientific figures |
| [Quantitative physics and mathematics atlas](docs/quantitative_physics_mathematics_atlas.md) | Full Q01-Q40 classical/statistical/causal sequence |
| [Quantum foundations and bridge test](docs/quantum_foundations_and_bridge_test.md) | Full QM01-QM18 quantum sequence plus P38-P44 |
| [Theorem roadmap](docs/theorem_roadmap.md) | Proposition dependencies and proof links |
| [Equation evidence map](docs/figures/equation_evidence_map.svg) | Visual provenance from equations to assumptions and evidence |

![Equation evidence map](docs/figures/equation_evidence_map.svg)

**Figure 22. Evidence provenance.** A mathematical identity, a theorem under assumptions, a numerical result, an empirical observation, and a target-measurement premise are different kinds of evidence. The project keeps those routes explicit.

---

# Numerical validation facts

The repository is executable rather than purely expository. The numerical layer verifies algorithms, finite examples, geometry, and regression behavior; it is not treated as empirical proof of a consciousness theory.

The reproducibility surface includes Python 3.10, 3.11, and 3.12 CI coverage, theorem-specific tests, figure geometry tests, link integrity tests, publication-integration guards, and source implementations under [`src/consciousness_bridge/`](src/consciousness_bridge/).

A passing test proves only that the declared code and repository invariants behave as tested. It does not convert a mathematical or synthetic result into biological evidence.

---

# Reproducibility and audit path

```bash
git clone https://github.com/MahsaKeikha/mathematical-consciousness-bridge.git
cd mathematical-consciousness-bridge
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
```

For scientific auditing, use the shortest route appropriate to the question: the [Theorem roadmap](docs/theorem_roadmap.md) for dependencies, [Research navigation](docs/research_navigation.md) for topic-oriented entry points, [Equation and citation map](docs/equation_and_citation_map.md) for provenance, [Visual atlas](website/visual-atlas.html) for figures, and the source/tests directories for executable contracts.

<details>
<summary><strong>Permanent proof, figure, code, and test index: P39-P60</strong></summary>

This compact index preserves direct traceability for the quantum and experiment-design continuation. The P61-P70 calibration frontier is documented on its dedicated page.

- **Proposition 39**: [p39_finite_data_quantum_nonfactorization.svg](docs/figures/p39_finite_data_quantum_nonfactorization.svg), [`finite_data_quantum_nonfactorization.py`](src/consciousness_bridge/finite_data_quantum_nonfactorization.py), [`test_finite_data_quantum_nonfactorization.py`](tests/test_finite_data_quantum_nonfactorization.py).
- **Proposition 40**: [p40_continuous_quantum_region_regularity.svg](docs/figures/p40_continuous_quantum_region_regularity.svg), [`continuous_quantum_region_regularity.py`](src/consciousness_bridge/continuous_quantum_region_regularity.py), [`test_continuous_quantum_region_regularity.py`](tests/test_continuous_quantum_region_regularity.py).
- **Proposition 41**: [p41_trace_ball_quantum_envelope.svg](docs/figures/p41_trace_ball_quantum_envelope.svg), [`trace_ball_quantum_envelope.py`](src/consciousness_bridge/trace_ball_quantum_envelope.py), [`test_trace_ball_quantum_envelope.py`](tests/test_trace_ball_quantum_envelope.py).
- **Proposition 42**: [p42_quantum_regular_bridge_sample_complexity.svg](docs/figures/p42_quantum_regular_bridge_sample_complexity.svg), [`quantum_regular_bridge_sample_complexity.py`](src/consciousness_bridge/quantum_regular_bridge_sample_complexity.py), [`test_quantum_regular_bridge_sample_complexity.py`](tests/test_quantum_regular_bridge_sample_complexity.py).
- **Proposition 43**: [p43_optimal_quantum_target_allocation.svg](docs/figures/p43_optimal_quantum_target_allocation.svg), [`optimal_quantum_target_allocation.py`](src/consciousness_bridge/optimal_quantum_target_allocation.py), [`test_optimal_quantum_target_allocation.py`](tests/test_optimal_quantum_target_allocation.py).
- **Proposition 44**: [p44_pair_adaptive_sample_allocation.svg](docs/figures/p44_pair_adaptive_sample_allocation.svg), [`pair_adaptive_sample_allocation.py`](src/consciousness_bridge/pair_adaptive_sample_allocation.py), [`test_pair_adaptive_sample_allocation.py`](tests/test_pair_adaptive_sample_allocation.py).
- **Proposition 45**: [p45_shared_preparation_graph_allocation.svg](docs/figures/p45_shared_preparation_graph_allocation.svg), [`shared_preparation_graph_allocation.py`](src/consciousness_bridge/shared_preparation_graph_allocation.py), [`test_shared_preparation_graph_allocation.py`](tests/test_shared_preparation_graph_allocation.py).
- **Proposition 46**: [p46_budget_constrained_witness_graph.svg](docs/figures/p46_budget_constrained_witness_graph.svg), [`budget_constrained_witness_graph.py`](src/consciousness_bridge/budget_constrained_witness_graph.py), [`test_budget_constrained_witness_graph.py`](tests/test_budget_constrained_witness_graph.py).
- **Proposition 47**: [p47_sequential_graph_refinement.svg](docs/figures/p47_sequential_graph_refinement.svg), [`sequential_witness_graph.py`](src/consciousness_bridge/sequential_witness_graph.py), [`test_sequential_witness_graph.py`](tests/test_sequential_witness_graph.py).
- **Proposition 48**: [p48_gap_dependent_stopping_complexity.svg](docs/figures/p48_gap_dependent_stopping_complexity.svg), [`gap_stopping_complexity.py`](src/consciousness_bridge/gap_stopping_complexity.py), [`test_gap_stopping_complexity.py`](tests/test_gap_stopping_complexity.py).
- **Proposition 49**: [p49_dyadic_stopping_overhead.svg](docs/figures/p49_dyadic_stopping_overhead.svg), [`dyadic_stopping_overhead.py`](src/consciousness_bridge/dyadic_stopping_overhead.py), [`test_dyadic_stopping_overhead.py`](tests/test_dyadic_stopping_overhead.py).
- **Proposition 50**: [p50_bounded_starvation_asynchronous_sampling.svg](docs/figures/p50_bounded_starvation_asynchronous_sampling.svg), [`bounded_starvation_sampling.py`](src/consciousness_bridge/bounded_starvation_sampling.py), [`test_bounded_starvation_sampling.py`](tests/test_bounded_starvation_sampling.py).
- **Proposition 51**: [p51_heterogeneous_service_rate_stopping.svg](docs/figures/p51_heterogeneous_service_rate_stopping.svg), [`heterogeneous_service_stopping.py`](src/consciousness_bridge/heterogeneous_service_stopping.py), [`test_heterogeneous_service_stopping.py`](tests/test_heterogeneous_service_stopping.py).
- **Proposition 52**: [p52_capacity_optimal_service_allocation.svg](docs/figures/p52_capacity_optimal_service_allocation.svg), [`capacity_optimal_service_allocation.py`](src/consciousness_bridge/capacity_optimal_service_allocation.py), [`test_capacity_optimal_service_allocation.py`](tests/test_capacity_optimal_service_allocation.py).
- **Proposition 53**: [p53_residual_demand_reoptimization.svg](docs/figures/p53_residual_demand_reoptimization.svg), [`residual_demand_reoptimization.py`](src/consciousness_bridge/residual_demand_reoptimization.py), [`test_residual_demand_reoptimization.py`](tests/test_residual_demand_reoptimization.py).
- **Proposition 54**: [p54_metric_switching_cost_residual_scheduling.svg](docs/figures/p54_metric_switching_cost_residual_scheduling.svg), [`metric_switching_residual_schedule.py`](src/consciousness_bridge/metric_switching_residual_schedule.py), [`test_metric_switching_residual_schedule.py`](tests/test_metric_switching_residual_schedule.py).
- **Proposition 55**: [p55_pruning_aware_switching_monotonicity.svg](docs/figures/p55_pruning_aware_switching_monotonicity.svg), [`pruning_aware_switching_monotonicity.py`](src/consciousness_bridge/pruning_aware_switching_monotonicity.py), [`test_pruning_aware_switching_monotonicity.py`](tests/test_pruning_aware_switching_monotonicity.py).
- **Proposition 56**: [p56_moving_start_metric_reoptimization_stability.svg](docs/figures/p56_moving_start_metric_reoptimization_stability.svg), [`moving_start_metric_reoptimization.py`](src/consciousness_bridge/moving_start_metric_reoptimization.py), [`test_moving_start_metric_reoptimization.py`](tests/test_moving_start_metric_reoptimization.py).
- **Proposition 57**: [p57_switching_metric_perturbation.svg](docs/figures/p57_switching_metric_perturbation.svg), [`switching_metric_perturbation.py`](src/consciousness_bridge/switching_metric_perturbation.py), [`test_switching_metric_perturbation.py`](tests/test_switching_metric_perturbation.py).
- **Proposition 58**: [p58_finite_data_metric_uncertainty.svg](docs/figures/p58_finite_data_metric_uncertainty.svg), [`finite_data_metric_uncertainty.py`](src/consciousness_bridge/finite_data_metric_uncertainty.py), [`test_finite_data_metric_uncertainty.py`](tests/test_finite_data_metric_uncertainty.py).
- **Proposition 59**: [p59_optimal_transition_calibration.svg](docs/figures/p59_optimal_transition_calibration.svg), [`optimal_transition_calibration.py`](src/consciousness_bridge/optimal_transition_calibration.py), [`test_optimal_transition_calibration.py`](tests/test_optimal_transition_calibration.py).
- **Proposition 60**: [p60_integer_transition_calibration.svg](docs/figures/p60_integer_transition_calibration.svg), [`integer_transition_calibration.py`](src/consciousness_bridge/integer_transition_calibration.py), [`test_integer_transition_calibration.py`](tests/test_integer_transition_calibration.py).

</details>

---

# Detailed proposition record

The proposition-by-proposition development history is intentionally kept off the main scientific reading path.

**[Read the complete P1 to P73 detailed proposition record](docs/detailed_proposition_record.md).**

---

# Current scientific status

| Item | Current state |
| --- | --- |
| Public theorem frontier | **P73** |
| Documented version | **v0.73.0** |
| Proposition-level results | **73** |
| Equation-driven quantitative figures | **62** |
| Target-provenance guard | **P71 proved under declared construction model** |
| Target-measurement robustness | **P72 proved under declared nondifferential channel model** |
| Target-channel identifiability | **P73 proved under declared three-view binary symmetric independent-noise model** |
| Physical-to-experiential bridge | **Open physical-to-experiential bridge** |
| Quantum ontology claim | **Not assumed** |
| Consciousness identified with a scalar, state of matter, or spacetime coordinate | **Not claimed** |
| Reproducibility | Python 3.10, 3.11, and 3.12 test matrix plus theorem-specific regression guards |

The scientific target is precise: continue reducing ambiguity in the physical description, target provenance, target measurement, measurement-model adequacy, admissible bridge class, and experiment until either a bridge is derived and survives falsification or a valid obstruction demonstrates exactly where the declared description is insufficient.

---

# Navigation

| If you want to... | Go here |
| --- | --- |
| Understand theorem dependencies | [Theorem roadmap](docs/theorem_roadmap.md) |
| Read the proposition chronology | [Detailed proposition record](docs/detailed_proposition_record.md) |
| Inspect target non-circularity | [P71](docs/proposition_71_target_provenance_noncircularity.md) |
| Inspect noisy target measurement | [P72](docs/proposition_72_target_measurement_channel_robustness.md) |
| Audit P72 equations | [P72 equation and provenance record](docs/p72_equation_provenance.md) |
| Inspect target-channel identifiability | [P73](docs/proposition_73_three_view_target_channel_identifiability.md) |
| Audit P73 equations | [P73 equation and provenance record](docs/p73_equation_provenance.md) |
| Inspect P61-P70 calibration | [Calibration and Optimization Frontier](docs/calibration_optimization_frontier_p61_p70.md) |
| Follow work by scientific question | [Research navigation](docs/research_navigation.md) |
| Audit equations and citations | [Equation and citation map](docs/equation_and_citation_map.md) |
| Inspect classical quantitative figures | [Quantitative physics and mathematics atlas](docs/quantitative_physics_mathematics_atlas.md) |
| Inspect the quantum branch | [Quantum foundations and bridge test](docs/quantum_foundations_and_bridge_test.md) |
| Inspect falsification conditions | [Falsification program](docs/falsification_program.md) |
| Browse the website | [Website entry point](website/index.html) |
| Browse every visual | [Visual atlas](website/visual-atlas.html) |
| Audit code and tests | [`src/consciousness_bridge/`](src/consciousness_bridge/) and [`tests/`](tests/) |
| Cite the research | [Citation guide](CITATION.md), [`CITATION.cff`](CITATION.cff), and [`CITATION.bib`](CITATION.bib) |

---

## Scope statement

This repository is an ongoing research program. Its purpose is to make physical-to-experiential claims harder to state vaguely and easier to test rigorously. It should be read as a sequence of explicit mathematical conditions, counterexample constructions, finite-data certificates, target-validity requirements, and experimental design tools. The final bridge remains a scientific target, not a conclusion assumed in advance.

---

# Citation

If this research program, one of its propositions, figures, algorithms, or implementations contributes to your work, please cite it. When a specific theorem or artifact is central to an argument, cite both the overall research program and the proposition or artifact used.

## Preferred scholarly citation

> **Keikha, M. (2026). *Mathematical Consciousness Bridge: A Mathematical-Physics Test Architecture for the Physical-to-Experiential Bridge Problem* (Version 0.73.0). GitHub research repository. https://github.com/MahsaKeikha/mathematical-consciousness-bridge**

## BibTeX

```bibtex
@misc{keikha2026mathematicalconsciousnessbridge,
  author       = {Keikha, Mahsa},
  title        = {Mathematical Consciousness Bridge: A Mathematical-Physics Test Architecture for the Physical-to-Experiential Bridge Problem},
  year         = {2026},
  version      = {0.73.0},
  howpublished = {GitHub research repository},
  url          = {https://github.com/MahsaKeikha/mathematical-consciousness-bridge},
  note         = {Ongoing research program. Current documented theorem frontier: P73.}
}
```

For theorem-level attribution, identify the proposition explicitly and preserve its declared assumptions. Because the repository evolves, reproducible citations should include the documented version and, when relevant, the exact Git commit SHA. No DOI is currently asserted.

Citation resources: **[full citation guide](CITATION.md)** | **[machine-readable CFF](CITATION.cff)** | **[BibTeX](CITATION.bib)**
