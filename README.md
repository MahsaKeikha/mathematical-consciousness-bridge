# Mathematical Consciousness Bridge

[![tests](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/test.yml/badge.svg)](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/test.yml)
[![version](https://img.shields.io/badge/version-0.70.0-2563eb)](CITATION.cff)
[![license](https://img.shields.io/badge/license-MIT-059669)](LICENSE)

**Mahsa Keikha, PhD**

> **What mathematical and physical conditions would be required for a complete physical description of a system to support a scientifically testable claim about consciousness?**

This repository is a mathematical-physics research program for the **physical-to-experiential bridge problem**. It does not begin by assuming what consciousness is. It asks what must be true before any proposed physical description can legitimately be called sufficient for an independently specified experiential target, how that sufficiency can be falsified, and how finite experiments can distinguish a real bridge from correlation, representation choice, coarse-graining, or statistical noise.

![Research architecture](docs/figures/research_architecture.svg)

**Figure 1. Scientific architecture of the project.** The research moves from physical dynamics to operationally measurable structure, then to mathematical sufficiency tests, finite-data certification, experimental design, and finally the still-open physical-to-experiential bridge. The arrows are logical dependencies, not claims that one layer has already been identified with consciousness.

---

# What this project is trying to achieve, in plain language

Physics can tell us how a system changes. Neuroscience can measure electrical, chemical, hemodynamic, behavioral, and perturbational responses. Information theory can quantify dependence. Causal inference can distinguish observation from intervention. Quantum mechanics can specify states, channels, and measurement statistics. None of these facts, by themselves, tell us whether a physical description contains **all and only the distinctions required to determine an experiential variable**.

The central problem is therefore not to search for a visually impressive scalar and label it consciousness. It is to ask a stricter question:

> Given a declared physical description, can an independently defined experiential target be determined from it, or can we construct a counterexample showing that physically indistinguishable cases remain experientially distinguishable?

The repository turns that question into mathematics, statistics, and experiment design. A serious bridge theory must survive representation changes, controlled interventions, temporal continuation, composition, scale changes, finite measurement error, model uncertainty, and independently specified falsification tests.

The working chain is

$$
\boxed{
\text{physical dynamics}
\to
\text{operational structure}
\to
\text{sufficiency / insufficiency test}
\to
\text{finite-data certificate}
\to
\text{experimental discrimination}
\to
\text{bridge law or falsification}
}
$$

The research currently contains **70 proposition-level results** and **61 equation-driven quantitative figures**. The theorem frontier is P70. The physical-to-experiential bridge itself remains open.

This project continues [Spatiotemporal Observer Mathematics](https://github.com/MahsaKeikha/spatiotemporal-observer-math), which addresses the prior physical problem of identifying a persistent moving subsystem from measured dynamics.

---

# Abstract

Let $\Omega$ denote the physically admissible state or history space, let $T:\Omega\to\mathcal T$ be a declared physical descriptor, and let $E:\Omega\to\mathcal E$ be an independently specified target representing the experiential distinctions a proposed theory claims to explain. The deterministic bridge question is whether there exists a map $B$ such that $E=B\circ T$. The stochastic version asks whether the conditional target law factors through $T$, equivalently whether the residual $I(E;\Omega\mid T)$ vanishes under the declared probabilistic model. The smooth version yields a differential obstruction through rank. These statements make physical sufficiency and insufficiency mathematically testable without assuming that any particular physical quantity is consciousness.

The program then develops the structures required to make those tests physically meaningful: intervention-conditioned response laws, causal influence, temporal continuation, composition defects, coarse-graining and reconstruction bounds, multiscale operational quotients, finite-sample confidence certificates, sequential and adaptive inference, quantum-state model-set tests, experiment scheduling, and certified resource allocation. The quantum branch asks what evidence would be required to reject factorization through a tomographically complete quantum description; it does not assume that consciousness is quantum or that quantum mechanics is incomplete.

The current results establish a rigorous **test architecture** for bridge claims, not a completed ontology of consciousness. Every result is labeled by whether it is a definition, theorem, implementation, numerical verification, empirical input, hypothesis, or open theorem target.

---

# Scientific status discipline

A reader should know the epistemic status of every object before reading the equations. The repository uses the following discipline throughout.

| Status | Meaning in this project |
| --- | --- |
| **Definition** | A mathematical object introduced for the framework. |
| **Proved** | A theorem derived from explicit assumptions. |
| **Implemented** | Executable code mirrors a stated theorem or procedure. |
| **Numerically verified** | A simulation or computation checks the implementation or an example. |
| **Empirically supported** | The statement depends on external published experimental evidence. |
| **Synthetic example** | A controlled example used to expose logic, failure modes, or calibration behavior. |
| **Hypothesis** | A scientifically motivated proposal not yet established by theorem or experiment. |
| **Open bridge problem** | A physical-to-experiential identification has not been derived. |

This distinction is central. The repository **does not assume that a physical quantity is consciousness**. It does not identify consciousness with entropy, integration, complexity, synchronization, entanglement, coherence, measurement, a state of matter, or an additional spacetime coordinate. Those possibilities require separate derivation and evidence.

**Quantum mechanics does not by itself imply consciousness.** A complete quantum state specifies the outcome statistics of declared measurements, but an experiential conclusion requires an additional bridge statement unless that bridge is independently derived.

---

# The core scientific thesis in one view

The bridge problem can be stated as a problem of **physical equivalence classes**.

A descriptor $T$ partitions the admissible physical domain into fibers

$$
[\omega]_T
=
\{\omega'\in\Omega:T(\omega')=T(\omega)\}.
$$

A deterministic bridge through $T$ can exist only if the target $E$ is constant on every such fiber. Therefore the physically decisive question is not whether $T$ correlates with $E$, but whether $T$ preserves every target distinction the theory claims matters.

$$
\boxed{
T(\omega_1)=T(\omega_2)
\quad\text{and}\quad
E(\omega_1)\ne E(\omega_2)
\quad\Longrightarrow\quad
E\ne B\circ T
}
$$

That single idea organizes the entire repository. The later theorem branches answer the scientific objections that immediately follow: What is an admissible physical descriptor? How should it be made representation invariant? How should interventions and time enter? What happens under coarse-graining? What if equality is only approximate because the data are finite? What if the physical description is quantum? How can a discriminating experiment be selected adaptively without invalidating inference?

| Layer | Mathematical object | Scientific question | Failure witness |
| --- | --- | --- | --- |
| Physical description | $T(\omega)$ | Does the descriptor represent the declared physics without arbitrary coordinate dependence? | Representation or identifiability failure |
| Operational structure | response laws and causal geometry | Do interventions distinguish physically meaningful structure? | Collision or missing causal distinction |
| Bridge sufficiency | $E=B\circ T$ | Is the target constant on physical fibers? | Same $T$, different $E$ |
| Stochastic sufficiency | $I(E;\Omega\mid T)$ | Is target-relevant information left outside $T$? | Certified positive residual |
| Scale stability | coarse-graining plus reconstruction | Does the relevant physical structure survive a change of resolution? | Uncontrolled reconstruction or distortion |
| Quantum sufficiency | $\rho$, channels, measurement statistics | Does the target factor through the declared operational quantum state? | Regularity-aware non-factorization witness |
| Finite experiment | confidence regions and stopping rules | Can the witness survive uncertainty, repeated looks, and adaptive sampling? | Confidence or design assumptions fail |

This is the scientific contribution of the project at its current stage: **a bridge claim is decomposed into separately auditable mathematical obligations instead of being hidden inside a single proposed consciousness quantity.**

---

# How to read this study

The main page is organized as a scientific argument rather than a chronological project log. A first-time reader can follow it in four passes: first identify the physical and experiential objects being compared; then inspect the intervention-resolved physical structure; next examine the exact and finite-data sufficiency tests; finally read the quantum, adaptive-experiment, falsification, and open-problem sections. Detailed proposition chronology and downstream calibration mathematics are linked separately so they do not interrupt the core argument.

| Reader question | Where the answer appears |
| --- | --- |
| **What is the scientific problem?** | [Abstract](#abstract), [core scientific thesis](#the-core-scientific-thesis-in-one-view), [Research at a glance](#research-at-a-glance), and [Section 1: Mathematical formulation of the bridge problem](#1-mathematical-formulation-of-the-bridge-problem). |
| **What exactly is being measured and compared?** | [Section 1](#1-mathematical-formulation-of-the-bridge-problem), [Section 2](#2-from-physical-dynamics-to-operational-structure), [Section 3](#3-time-composition-and-scale-cannot-be-ignored), [Section 4](#4-turning-a-population-theorem-into-a-finite-experiment), the [measurement map](docs/figures/conscious_state_measurement_map.svg), and the [response-geometry map](docs/figures/information_geometry_response_manifold.svg). |
| **What has actually been proved?** | [Scientific status discipline](#scientific-status-discipline), [Theorem roadmap](docs/theorem_roadmap.md), and [What has actually been established](#what-has-actually-been-established). |
| **What would falsify the framework or a candidate bridge?** | [Falsification logic](#falsification-logic) and the [Falsification program](docs/falsification_program.md). |
| **What remains unknown?** | [What remains open](#what-remains-open), [Current scientific status](#current-scientific-status), [Research navigation](docs/research_navigation.md), [Detailed proposition record](docs/detailed_proposition_record.md), and the [Calibration and Optimization Frontier](docs/calibration_optimization_frontier_p61_p70.md). |

![Universal proof ladder](docs/figures/universal_proof_ladder.svg)

**Figure 2. Scientific proof ladder.** A credible consciousness bridge must pass distinct layers: physical well-definedness, experiential well-definedness, non-circular bridge premises, representation invariance, physical-feature sufficiency, experimental recoverability, competing-theory discrimination, finite-data support, and explicit falsification. The figure is a requirements map, not a claim that every layer has already been closed.

---

# Research at a glance

The full program can be read as seven scientific stages. This table is the shortest complete map of the repository.

| Stage | Results | Scientific question | Status | Main entry point |
| --- | --- | --- | --- | --- |
| 1. Foundations and identifiability | **P1-P10** | What must be invariant, distinguishable, recoverable, and statistically testable before a physical descriptor can support a bridge claim? | Proved / implemented / tested | [Theorem roadmap](docs/theorem_roadmap.md) |
| 2. Causal, temporal, compositional, and scale structure | **P11-P18** | Which structured physical distinctions survive interventions, time, composition, and coarse-graining? | Proved / implemented / tested | [Quantitative physics and mathematics atlas](docs/quantitative_physics_mathematics_atlas.md) |
| 3. Bridge factorization and finite-data inference | **P19-P24** | Does an independently declared target factor through the physical descriptor, and can insufficiency be certified with finite data and repeated looks? | Proved under declared models | [Research navigation](docs/research_navigation.md) |
| 4. Multiscale operational structure | **P25-P37** | Which causal and response structures survive node, state, intervention, and delay quotients, and how much distortion is introduced? | Proved / implemented / tested | [Theorem roadmap](docs/theorem_roadmap.md) |
| 5. Quantum sufficiency and falsification | **P38-P44** | What follows from a declared tomographically complete quantum description, and what would count as evidence against factorization through it? | Conditional tests proved; ontology open | [Quantum foundations and bridge test](docs/quantum_foundations_and_bridge_test.md) |
| 6. Adaptive experiment design and scheduling | **P45-P58** | How should evidence gathering, stopping, service allocation, switching, and noisy transition measurement be organized while preserving statistical validity? | Proved / implemented / tested | [Equation and citation map](docs/equation_and_citation_map.md) |
| 7. Calibration and integer optimization | Downstream experimental layer | How should finite calibration resources be allocated and certified after the scientific witness and uncertainty model are declared? | Proved / implemented / tested | [Calibration and Optimization Frontier](docs/calibration_optimization_frontier_p61_p70.md) |

The dependency-oriented theorem map covers **P1 through P70 with explicit dependency branches**.

![Theorem roadmap](docs/figures/theorem_roadmap.svg)

**Figure 3. Theorem dependency map.** Read from foundational identifiability toward bridge tests and experimental-design branches. Each arrow is a mathematical dependency. Later optimization results improve how experiments are executed or certified; they do not retroactively strengthen an earlier ontological claim.

---

# 1. Mathematical formulation of the bridge problem

## 1.1 Physical states, descriptors, and targets

Let

$$
\Omega = \{\text{physically admissible states or histories}\}.
$$

A proposed physical theory chooses a descriptor

$$
T:\Omega\to\mathcal T.
$$

Examples of $T$ might include an intervention-response structure, a multiscale causal descriptor, a complete classical state under declared assumptions, or a tomographically reconstructed quantum state. The framework does not privilege one choice in advance.

Independently, let

$$
E:\Omega\to\mathcal E
$$

represent the target distinctions the proposed bridge claims to determine. The independence requirement matters: if $E$ is defined from $T$, factorization becomes circular and cannot test the physical description.

A useful way to keep the notation straight is:

| Symbol | Role | Scientific requirement |
| --- | --- | --- |
| $\Omega$ | admissible physical states or histories | must be declared relative to a physical model and experiment class |
| $T$ | physical descriptor | must be operationally defined, representation-aware, and recoverable |
| $E$ | experiential target | must be specified independently enough to avoid definitional circularity |
| $B$ | candidate bridge law | must state how physical equivalence classes map to target distinctions |
| $R_{\mathrm{stoch}}$ | residual target information outside $T$ | must be interpreted under an explicit probabilistic model |

The target $E$ is intentionally not equated with verbal report or overt responsiveness. Dreaming, anesthesia, perturbational complexity, and covert command-related brain activation show why behavior, report, neural evidence, and experiential inference must be kept distinct (Casali et al., 2013; Sarasso et al., 2015; Siclari et al., 2017; Claassen et al., 2019; see the references below).

![Conscious-state measurement and dissociation map](docs/figures/conscious_state_measurement_map.svg)

**Figure 4. Measurement and dissociation map.** Behavioral responsiveness, subjective report, perturbational complexity, and command-related brain activation are different evidence channels. A bridge theory must state which pattern of observables it predicts and must remain testable when report or behavior is unavailable. The figure motivates the independent-target requirement; it does not define consciousness by any single measurement.

## 1.2 Exact deterministic sufficiency

The physical descriptor is exactly sufficient for the target if there exists a bridge map $B$ such that

$$
\boxed{E=B\circ T.}
$$

This is equivalent to the fiber condition

$$
\boxed{
T(\omega_1)=T(\omega_2)
\Longrightarrow
E(\omega_1)=E(\omega_2).
}
$$

Therefore an exact counterexample has a simple form:

$$
T(\omega_1)=T(\omega_2),
\qquad
E(\omega_1)\ne E(\omega_2).
$$

One such pair is enough to show that the declared $T$ is insufficient for the declared $E$. This is the core logic behind the exact factorization branch formalized in Proposition 19.

## 1.3 Stochastic sufficiency

When the target is probabilistic, the relevant residual is

$$
\boxed{
R_{\mathrm{stoch}}(T)
=I(E;\Omega\mid T).
}
$$

Under the declared probabilistic model,

$$
R_{\mathrm{stoch}}(T)=0
$$

means that $T$ contains all target-relevant information available in $\Omega$. A positive residual means that target-relevant information remains outside the descriptor.

If $T_f$ refines $T_c$ through $T_c=c\circ T_f$, Proposition 21 gives the exact identity

$$
\boxed{
R_{\mathrm{stoch}}(T_c)-R_{\mathrm{stoch}}(T_f)
=I(E;T_f\mid T_c).
}
$$

This quantifies how much target-relevant information is gained by the refinement rather than merely stating that a finer representation is better.

## 1.4 Smooth differential obstruction

For smooth manifolds and differentiable maps, exact factorization implies

$$
dE_x=dB_{T(x)}\circ dT_x.
$$

Hence

$$
\boxed{
\operatorname{rank}(dE_x)
\le
\operatorname{rank}(dT_x).
}
$$

If the target varies locally in more independent directions than the proposed physical descriptor can represent, no smooth bridge of the declared form can exist near that point. The underlying differential-topology machinery is standard; the use of the rank condition as a bridge obstruction is part of the repository's P19 formulation. See Lee's *Introduction to Smooth Manifolds* for the mathematical background and the [equation provenance map](docs/equation_and_citation_map.md) for the repository-specific statement.

![Fundamental theory to consciousness map](docs/figures/fundamental_theory_consciousness_map.svg)

**Figure 5. The logical gap being tested.** Fundamental physical theory determines physical structure and operational predictions. A consciousness theory still requires a justified map from physical equivalence classes to experiential equivalence classes. The project makes that extra bridge explicit so its assumptions, regularity, uncertainty, and failure conditions can be tested rather than hidden inside terminology.

The mathematical point is deliberately modest but powerful: factorization gives a precise necessary-and-sufficient criterion for the declared descriptor and target. It does not tell us in advance which physical descriptor nature uses, or how an experiential target should ultimately be operationalized. Those are separate scientific obligations addressed by the next layers.

---

# 2. From physical dynamics to operational structure

A useful bridge test cannot depend only on coordinates or passive correlations. It should be built from physically meaningful distinctions that can, at least in principle, be interrogated experimentally.

## 2.1 Intervention-conditioned response laws

For subsystem or node $i$, delay $\ell$, and intervention $do(u)$, define an operational response law

$$
R_i^{(\ell)}(\cdot\mid do(u)).
$$

The P11 structured candidate collects three complementary objects:

$$
\boxed{
\mathcal C(S)
=
(\mathcal R,\mathcal I,\mathcal O),
}
$$

where $\mathcal R$ is response geometry, $\mathcal I$ measures irreducibility relative to declared partition-product null models, and $\mathcal O$ represents directed intervention influence.

This is deliberately richer than a scalar. Two systems can have similar entropy, complexity, or average activity while differing in which interventions affect which targets, over what delays, and with what response geometry.

![Causal structure anatomy](docs/figures/causal_structure_anatomy.svg)

**Figure 6. Anatomy of the operational physical candidate.** Controlled interventions generate response distributions. Distances among those distributions define response geometry; comparisons across sources define directed influence; comparisons with partitioned null models expose irreducibility. These are physical candidates to be tested for sufficiency, not definitions of consciousness.

![Information geometry of intervention-response laws](docs/figures/information_geometry_response_manifold.svg)

**Figure 7. Response laws as a physical geometry.** Parameterized intervention-conditioned probability laws can be studied with local statistical geometry and finite operational distances. Temporal trajectories, composition, and coarse-graining then become transformations of a physical response space. An experiential geometry would still require a separately justified bridge.

The intervention language is grounded in the causal distinction between observation and intervention developed in Pearl's causal framework (Pearl, 2009). Empirically, perturbational approaches such as TMS-EEG motivate direct probing of distributed neural response rather than relying only on passive correlation (Casali et al., 2013).

## 2.2 Why no single compressed component is enough

A central risk in consciousness research is to compress a rich physical system into one attractive number and then silently treat that number as the explanatory object. Proposition 12 uses constructive collisions to show how that can fail even inside the repository's own operational candidate.

![Constructive component collisions](docs/figures/p12_collision_map.svg)

**Figure 8. Constructive collision tests.** Response geometry, partition irreducibility, and directed marginal influence can each be held fixed while another component of the full intervention-resolved structure changes. The examples therefore demonstrate a general methodological lesson: a compressed feature must earn sufficiency by factorization or reconstruction, not by visual plausibility or correlation.

This collision logic is one reason the project treats causal structure as a structured object before asking whether any further compression is scientifically justified.

---

# 3. Time, composition, and scale cannot be ignored

A bridge that works only for one arbitrary representation, one instant, or one resolution is scientifically fragile. The physical structure must be tracked through temporal continuation, subsystem composition, and coarse-graining.

## 3.1 Temporal continuation is a path property

The P14 temporal branch compares representation-invariant structure classes across physical time. The key distinction is between endpoint similarity and continuity of the path taken between those endpoints.

![Temporal continuation](docs/figures/p14_temporal_continuation.svg)

**Figure 9. Temporal continuation of the operational structure.** Admissible relabelings are quotiented out, local structural changes are accumulated along the trajectory, and the largest local transition can be bounded. A system may return to the same endpoint after a large excursion, so endpoint equality alone cannot certify temporal continuity.

This does not identify experiential continuity. It establishes the physical bookkeeping that any later continuity claim would have to reference.

## 3.2 Coarse-graining and data processing

If a fine response law is mapped deterministically to a coarse observable, total variation cannot increase:

$$
\boxed{
\operatorname{TV}(K_\#P,K_\#Q)
\le
\operatorname{TV}(P,Q).
}
$$

This is a data-processing fact, not a consciousness result. Its role is to tell us what operational distinctions can disappear under coarse observation.

## 3.3 Approximate reconstruction as a scale certificate

Contraction alone is not enough. If a coarse representation can approximately reconstruct the relevant fine distributions with uniform error $\varepsilon$, Proposition 18 bounds the distortion of total-variation geometry:

$$
\boxed{
|D_f-D_c|\le 2\varepsilon.
}
$$

This converts a vague claim such as "the coarse scale preserves the important structure" into a quantitative condition that can be checked.

![Scale sufficiency certificate](docs/figures/p18_scale_sufficiency_certificate.svg)

**Figure 10. Scale sufficiency logic.** Coarse-graining can erase distinctions, but approximate reconstruction controls how much declared response geometry was lost. This provides a quantitative route to compare neural, subsystem, or experimental resolutions without pretending that all scales are equivalent.

The subsequent P25-P37 branch extends this logic to changing node sets, intervention labels, delays, partition structure, directed influence, and joint operational quotients.

![Multiscale physical hierarchy](docs/figures/multiscale_physical_hierarchy.svg)

**Figure 11. Multiscale hierarchy.** A scientifically credible descriptor must state which objects survive a change of scale, which require compatibility conditions, and which acquire bounded distortion. Zero numerical error cannot rescue a semantically invalid quotient.

---

# 4. Turning a population theorem into a finite experiment

Exact mathematical insufficiency is useful only if finite observations can support or reject it with controlled error.

Let $\widehat P$ denote an empirical law and $P$ the underlying population law. The finite-sample branch builds confidence events of the form

$$
\mathcal A_n
=
\left\{
\|P-\widehat P\|_{\mathrm{TV}}
\le \tau_n(\alpha)
\right\},
\qquad
\Pr(\mathcal A_n)\ge1-\alpha.
$$

On that event, the population bridge residual can be bounded from empirical data. Proposition 20 gives a finite-sample certificate for the P19 stochastic residual under the declared finite-alphabet IID model. Propositions 22 and 23 extend validity across refinement families and data-dependent selection. Proposition 24 allocates error over repeated looks to obtain an anytime-valid certificate.

![Finite-sample residual certificate](docs/figures/p20_finite_sample_residual_certificate.svg)

**Figure 12. From exact factorization to finite-data evidence.** The theoretical residual is not replaced by a point estimate. The experiment produces an uncertainty set, and a bridge claim is rejected only when the certified lower bound remains positive under the declared statistical assumptions.

This distinction is essential: numerical closeness is not exact equality, and an apparent residual is not evidence of non-reducibility until estimation uncertainty has been propagated through the bridge test.

---

# 4.4 Fundamental theory / Theory-of-Everything interface

The bridge framework must remain compatible with the possibility that future fundamental physics changes the declared physical state description. There is currently **no experimentally established Theory of Everything** that has been shown to unify all fundamental interactions and, separately, to determine experiential variables.

For bookkeeping, the repository can represent a broad physical descriptor schematically as

$$
\boxed{
T(\Omega)=\bigl(G(\Omega),Q(\Omega),C(\Omega)\bigr),
}
$$

where $G$ denotes gravitational or geometric information, $Q$ denotes quantum-operational information, and $C$ denotes effective causal or classical structure under the declared model. This notation does not assert that these three components are fundamental, complete, independent, or uniquely decomposed. It provides an interface through which a more complete future physical theory could replace the present descriptor without changing the logic of factorization testing.

A useful diagnostic symbol is $d_{\mathrm{TOE}}^{\perp}$: it denotes target-relevant variation that would remain transverse to the declared complete-physics descriptor under a specified bridge class. It is not an observed new force or dimension. A nonzero certified obstruction would have scientific meaning only after the physical descriptor, target, bridge class, and measurement uncertainty were all independently justified.

The repository also distinguishes scientific sources from speculative antecedents. Thomas W. Campbell's *My Big TOE* and similar consciousness-first proposals are **not treated as established scientific facts**. They may be discussed only as a **speculative, falsifiable antecedent**, but they are not used as assumptions in the theorem chain. The same evidential rule applies to any proposed consciousness-first ontology: conceptual inspiration and established physical evidence are different categories.

![Observer-to-bridge research handoff](docs/figures/observer_to_bridge_handoff.svg)

**Figure 13. Research handoff.** The preceding Spatiotemporal Observer Mathematics project identifies and statistically certifies a physical subsystem from measured dynamics. This repository begins only after that physical object has been established and asks what additional causal, temporal, multiscale, and bridge structure is required. No experiential property is inserted at the handoff.

---

# 5. Quantum mechanics enters as a physical description, not as an assumption about consciousness

For a finite-dimensional quantum system, a state is represented by a density operator $\rho$. A POVM $\{M_a\}$ gives

$$
\boxed{
p(a\mid M)=\operatorname{Tr}(\rho M_a).
}
$$

Admissible dynamics are represented by completely positive trace-preserving maps, and composite systems by density operators on tensor-product spaces. These are standard quantum-mechanical structures.

The bridge question is then sharpened:

> If the declared quantum descriptor is operationally complete for the chosen preparation, channels, and measurements, does an independently defined experiential target factor through that descriptor?

Proposition 38 states the exact non-factorization witness for a tomographically complete quantum descriptor. Proposition 39 propagates finite tomography and target uncertainty. Proposition 40 proves an important limitation: on a finite sampled set, an injective descriptor always permits an unrestricted lookup-table factorization. Therefore a meaningful continuous-region obstruction requires an explicit regularity class for the bridge. Propositions 41-44 make this program computable through trace-distance uncertainty regions, sample-complexity bounds, optimal quantum-versus-target allocation, and simultaneous candidate-pair validity.

![Quantum bridge completeness map](docs/figures/quantum_bridge_completeness_map.svg)

**Figure 14. What quantum completeness does and does not establish.** Tomographic completeness closes the declared operational description of the quantum state. It does not automatically close the physical-to-experiential map. The open question is whether the independently specified target factors through that operational state under a scientifically justified bridge class.

![Quantum operational sufficiency](docs/figures/p38_quantum_operational_sufficiency.svg)

**Figure 15. P38 quantum sufficiency test.** Equal declared quantum descriptors with unequal independently defined targets give an exact non-factorization witness. When descriptors are only approximately known, P39-P44 replace exact equality with uncertainty regions and regularity-aware inequalities.

![Trace-ball quantum envelope](docs/figures/p41_trace_ball_quantum_envelope.svg)

**Figure 16. Finite-data quantum envelope.** Quantum-state confidence regions and target uncertainty are propagated into an end-to-end obstruction. The scientific conclusion is conditional on the tomography model, confidence coverage, and declared regularity of the candidate bridge.

The significance of the quantum branch is methodological. It asks a difficult question in a form that can fail: even after the operational quantum state is reconstructed as completely as the declared model permits, is there independently supported target structure that cannot be represented by the admissible bridge class? Until such a witness is obtained, quantum incompleteness is not a conclusion of this project.

For the complete quantum visual sequence, including Bloch geometry, channels, entanglement, decoherence, tomography, contextuality, and open-system maps, see the [Quantum foundations and bridge test](docs/quantum_foundations_and_bridge_test.md) and the [Visual atlas](website/visual-atlas.html).

---

# 6. Adaptive experiment design: collecting the evidence without invalidating it

Once a family of possible bridge witnesses is declared, the next problem is experimental: which preparations should be sampled, when can a candidate be pruned, and when is there enough evidence to stop?

P45 converts pairwise witness requirements into a shared preparation graph, where one preparation-level sample stream can improve every incident candidate edge. P47 then combines time-uniform confidence sequences into a shared event that remains valid under non-anticipating adaptive sampling, graph refinement, witness selection, safe pruning, and stopping. P48-P53 turn those validity statements into stopping-time and service-allocation results. P54-P58 incorporate setup motion, switching costs, metric perturbation, and finite-data uncertainty in the switching metric itself.

![Sequential graph refinement](docs/figures/p47_sequential_graph_refinement.svg)

**Figure 17. Adaptive evidence collection.** The experiment may choose what to sample next based on previous observations, but validity is protected by a shared time-uniform confidence event. Adaptation changes efficiency, not the declared error guarantee.

This branch matters because a bridge theory should not depend on an unrealistic fixed experiment. It should specify how evidence can be gathered efficiently without turning optional stopping or data-dependent witness selection into hidden statistical bias.

---

# 7. Calibration and optimization as a downstream experimental layer

The later calibration and discrete-optimization results belong to the **experimental implementation layer**, not to the conceptual introduction to the consciousness bridge itself. Their role is to determine how finite calibration measurements should be allocated and how candidate integer designs can be certified once the bridge hypothesis, physical descriptor, witness family, uncertainty model, and experimental constraints have already been declared.

To keep this main page readable for a first-time scientific reader, the complete P61-P70 theorem sequence, derivations, figures, implementations, tests, assumptions, and primal-dual certificates are documented separately:

**[Read the complete Calibration and Optimization Frontier: P61-P70](docs/calibration_optimization_frontier_p61_p70.md).**

The main scientific conclusion does not depend on reading that optimization branch first. It is supporting machinery for executing and certifying experiments, not a proposed definition or measure of consciousness.

---

# What has actually been established

The project has established mathematical and computational machinery for testing a bridge claim without silently assuming the bridge. The strongest conclusions are methodological and conditional:

1. **Physical descriptors can be tested for exact sufficiency.** Exact factorization is equivalent to constancy of the target on physical-descriptor fibers.
2. **Stochastic insufficiency can be quantified.** Conditional mutual information measures target-relevant information left outside a descriptor under the declared model.
3. **Smooth factorization can fail for rank reasons.** The differential obstruction supplies a local no-go test.
4. **Operational structure can be made richer than a scalar.** Intervention response, directed influence, irreducibility, temporal continuation, composition, and scale can be treated explicitly.
5. **Compressed physical features can be tested by collision.** Constructive counterexamples show when a projection loses distinctions retained by the fuller operational structure.
6. **Coarse-graining losses can be bounded.** Reconstruction assumptions give quantitative scale certificates rather than qualitative claims.
7. **Finite-data uncertainty can be propagated into bridge tests.** Exact equalities are not replaced by numerical approximations without confidence control.
8. **Adaptive experiments can remain statistically valid.** Candidate selection, pruning, repeated looks, and stopping are handled on shared confidence events under declared assumptions.
9. **Quantum-state completeness can be separated from experiential completeness.** A complete operational quantum descriptor can be tested for target factorization without assuming the answer.
10. **Experimental resources can be optimized and certified.** The experiment-design branch develops allocation, scheduling, stopping, and calibration guarantees; the detailed P61-P70 calibration sequence is documented separately so it does not dominate the scientific introduction.

These statements do **not** prove that consciousness is reducible to the current physical descriptors, irreducible to physics, quantum, non-quantum, a field, a state of matter, or an additional dimension.

---

# What remains open

The central open theorem is still the bridge itself.

Suppose a physical description $T$ is complete relative to a declared physical theory and an independently defined experiential target $E$ is scientifically measurable. Then one of the following must eventually be supported:

$$
\boxed{
E=B\circ T
}
$$

for a scientifically justified bridge class $B$, or a reproducible obstruction must show that no bridge in that class can explain the declared target distinctions.

The open work is therefore not "find a mysterious consciousness number." It is to close the following scientific gaps:

- define experiential variables independently enough to avoid circularity;
- identify which physical descriptor is justified by experiment rather than convenience;
- test whether target distinctions factor through that descriptor across interventions, time, scale, and composition;
- quantify uncertainty strongly enough to rule out estimation artifacts;
- specify the regularity or structural class of admissible bridge laws;
- design decisive experiments for cases where competing bridge theories make different predictions.

A claim of non-reducibility would require a valid obstruction relative to a sufficiently complete physical description and a scientifically defensible bridge class. Failure of one coarse descriptor is not failure of physics.

This is the frontier at which mathematics, physics, neuroscience, and philosophy of science meet in the repository. The project has built increasingly strict conditions for what would count as evidence; it has intentionally not replaced the missing bridge with an assumption.

---

# Falsification logic

The framework is designed so that each scientific layer has a failure condition.

| Claim being tested | What would count against it? | What would *not* be enough? |
| --- | --- | --- |
| Descriptor $T$ is exactly sufficient for $E$ | Same $T$, different independently measured $E$ | Mere correlation between $T$ and $E$ |
| Descriptor $T$ is stochastically sufficient | Certified positive $I(E;\Omega\mid T)$ | Positive empirical estimate without uncertainty control |
| Compressed causal feature is sufficient | Constructive collision: same compressed feature, different fuller operational structure | High predictive performance on one dataset |
| Coarse scale preserves relevant response structure | Reconstruction or distortion bounds fail | Visual similarity of coarse and fine plots |
| Quantum descriptor is sufficient under bridge class $\mathcal B$ | Certified target separation exceeds what every admissible $B\in\mathcal B$ can map from the quantum uncertainty region | Two numerically close tomography estimates |
| Adaptive experiment is valid | Confidence event or non-anticipation assumptions are violated | Choosing samples adaptively by itself |
| Integer calibration candidate is optimal | A better feasible allocation is found or the exact solver disproves it | Failure of a sufficient certificate alone |

This is the intended scientific discipline: every positive claim should bring its own way of being wrong.

![Theory-comparative interface](docs/figures/theory_comparison_map.svg)

**Figure 18. Common interface for competing theory families.** Integrated Information Theory, Global Neuronal Workspace Theory, Recurrent Processing Theory, higher-order approaches, predictive / neurorepresentational families, and the repository's intervention-resolved physical candidate can be compared using the same categories: physical feature family, bridge architecture, measurement interface, and discriminating experiment. This framing follows the broader theory-comparison literature rather than treating any existing theory as the default answer (Seth & Bayne, 2022; Cogitate Consortium et al., 2025).

For the explicit repository-level failure conditions, see the [Falsification program](docs/falsification_program.md).

---

# Evidence, references, and provenance

The repository keeps mathematics, physical background, empirical evidence, and speculative antecedents distinct. The main provenance resources are:

| Resource | Purpose |
| --- | --- |
| [Equation and citation map](docs/equation_and_citation_map.md) | States which equations are standard, derived here, or dependent on external results. |
| [Foundational physics and mathematics bibliography](docs/foundational_physics_mathematics_bibliography.md) | Physics, information theory, causal inference, differential topology, thermodynamics, and empirical measurement sources. |
| [Literature map](docs/literature_map.md) | Consciousness-theory and empirical comparison literature. |
| [`fundamental_theory_references.bib`](docs/fundamental_theory_references.bib) | Machine-readable reference file for the fundamental-physics branch. |
| [Reference audit](docs/reference_audit.md) | Separates peer-reviewed evidence, mathematical background, and speculative antecedents. |
| [Citation and reference policy](docs/citation_and_reference_policy.md) | Rules for how repository-original results and external sources are attributed. |

## Selected scientific references

1. C. E. Shannon, "A Mathematical Theory of Communication," *Bell System Technical Journal* 27 (1948), 379-423 and 623-656. [DOI 10.1002/j.1538-7305.1948.tb01338.x](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x).
2. T. M. Cover and J. A. Thomas, *Elements of Information Theory*, 2nd ed., Wiley, 2006. [DOI 10.1002/047174882X](https://doi.org/10.1002/047174882X).
3. J. Pearl, *Causality: Models, Reasoning, and Inference*, 2nd ed., Cambridge University Press, 2009.
4. J. M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2013. [DOI 10.1007/978-1-4419-9982-5](https://doi.org/10.1007/978-1-4419-9982-5).
5. S. Amari, *Information Geometry and Its Applications*, Springer, 2016. [DOI 10.1007/978-4-431-55978-8](https://doi.org/10.1007/978-4-431-55978-8).
6. R. Landauer, "Irreversibility and Heat Generation in the Computing Process," *IBM Journal of Research and Development* 5(3) (1961), 183-191. [DOI 10.1147/rd.53.0183](https://doi.org/10.1147/rd.53.0183).
7. A. G. Casali et al., "A theoretically based index of consciousness independent of sensory processing and behavior," *Science Translational Medicine* 5(198) (2013), 198ra105. [DOI 10.1126/scitranslmed.3006294](https://doi.org/10.1126/scitranslmed.3006294).
8. M. Tegmark, "Consciousness as a State of Matter," *Chaos, Solitons & Fractals* 76 (2015), 238-270. [DOI 10.1016/j.chaos.2015.03.014](https://doi.org/10.1016/j.chaos.2015.03.014). This is treated as conceptual physics lineage, not as an established bridge theorem.
9. A. K. Seth and T. Bayne, "Theories of consciousness," *Nature Reviews Neuroscience* 23 (2022), 439-452. [DOI 10.1038/s41583-022-00587-4](https://doi.org/10.1038/s41583-022-00587-4).
10. Cogitate Consortium et al., "Adversarial testing of global neuronal workspace and integrated information theories of consciousness," *Nature* 642 (2025), 133-142. [DOI 10.1038/s41586-025-08888-1](https://doi.org/10.1038/s41586-025-08888-1).
11. A. I. Luppi et al., "Convergent transcriptomic and connectomic controllers of information integration and its anaesthetic breakdown across mammalian brains," *Nature Human Behaviour* 10 (2026), 777-802. [DOI 10.1038/s41562-025-02381-5](https://doi.org/10.1038/s41562-025-02381-5).
12. F. Siclari et al., "The neural correlates of dreaming," *Nature Neuroscience* 20 (2017), 872-878. [DOI 10.1038/nn.4545](https://doi.org/10.1038/nn.4545).
13. S. Sarasso et al., "Consciousness and Complexity during Unresponsiveness Induced by Propofol, Xenon, and Ketamine," *Current Biology* 25(23) (2015), 3099-3105. [DOI 10.1016/j.cub.2015.10.014](https://doi.org/10.1016/j.cub.2015.10.014).
14. J. Claassen et al., "Detection of Brain Activation in Unresponsive Patients with Acute Brain Injury," *New England Journal of Medicine* 380(26) (2019), 2497-2505. [DOI 10.1056/NEJMoa1812757](https://doi.org/10.1056/NEJMoa1812757).

The complete bibliography is maintained in the dedicated reference documents above so this page can remain readable while every major scientific dependency stays auditable.

---

# Complete visual evidence without front-page overload

The main page intentionally shows the figures needed to understand the argument in scientific order. A reader who scans only the figures and captions should still recover the main logic: define the bridge, separate evidence channels, build operational physical structure, expose collisions, preserve structure through time and scale, propagate uncertainty, test the quantum descriptor, and design valid experiments.

The complete visual record remains available for audit without forcing a first-time reader through every theorem-specific or calibration plot.

| Visual collection | What it contains |
| --- | --- |
| [Visual atlas](website/visual-atlas.html) | Browser-oriented gallery of the repository's scientific figures. |
| [Quantitative physics and mathematics atlas](docs/quantitative_physics_mathematics_atlas.md) | Full equation-driven classical, statistical, causal, dynamical, and multiscale sequence, including Q01-Q40. |
| [Quantum foundations and bridge test](docs/quantum_foundations_and_bridge_test.md) | Full QM01-QM18 quantum sequence plus P38-P44 bridge tests. |
| [Theorem roadmap](docs/theorem_roadmap.md) | Proposition dependencies and proof links. |
| [Equation evidence map](docs/figures/equation_evidence_map.svg) | Visual provenance from equations to assumptions, evidence, and theorem status. |

![Equation evidence map](docs/figures/equation_evidence_map.svg)

**Figure 19. Evidence provenance.** A mathematical identity, a theorem under assumptions, a numerical result, and an empirical observation are different kinds of evidence. The project keeps those routes explicit so a reader can see what supports each scientific claim.

---

# Numerical validation facts

The repository is executable rather than purely expository. The numerical layer is used to verify algorithms, finite examples, geometry, and regression behavior; it is not treated as empirical proof of a consciousness theory.

The current reproducibility surface includes:

- Python 3.10, 3.11, and 3.12 CI coverage;
- theorem-specific unit and regression tests;
- geometry tests for publication figures;
- documentation and local-link integrity tests;
- explicit publication-integration tests for the current proposition frontier;
- source implementations under [`src/consciousness_bridge/`](src/consciousness_bridge/).

A passing test proves only that the declared code and repository invariants behave as tested. It does not convert a mathematical or synthetic result into biological evidence.

---

# Reproducibility and audit path

A reader who wants to reproduce the code can use the repository directly:

```bash
git clone https://github.com/MahsaKeikha/mathematical-consciousness-bridge.git
cd mathematical-consciousness-bridge
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
```

For scientific auditing, use the shortest route appropriate to the question:

1. **Understand the argument:** read this README from top to bottom.
2. **Inspect dependencies:** open the [Theorem roadmap](docs/theorem_roadmap.md).
3. **Audit a derivation:** use the [Equation and citation map](docs/equation_and_citation_map.md) and the linked proposition document.
4. **Audit code:** follow the proof-to-implementation link into [`src/consciousness_bridge/`](src/consciousness_bridge/) and the corresponding test.
5. **Inspect every figure:** use the [Visual atlas](website/visual-atlas.html).
6. **Inspect external evidence:** use the [Foundational bibliography](docs/foundational_physics_mathematics_bibliography.md), [Literature map](docs/literature_map.md), and [Reference audit](docs/reference_audit.md).

<details>
<summary><strong>Permanent proof, figure, code, and test index: P39-P60</strong></summary>

This compact index preserves direct public traceability for the quantum and experiment-design continuation without placing every technical figure in the main reading flow. The P61-P70 calibration frontier is documented on its dedicated page.

- **Proposition 39**: [p39_finite_data_quantum_nonfactorization.svg](docs/figures/p39_finite_data_quantum_nonfactorization.svg), [`finite_data_quantum_nonfactorization.py`](src/consciousness_bridge/finite_data_quantum_nonfactorization.py), [`test_finite_data_quantum_nonfactorization.py`](tests/test_finite_data_quantum_nonfactorization.py).
- **Proposition 40**: [p40_continuous_quantum_region_regularity.svg](docs/figures/p40_continuous_quantum_region_regularity.svg), [`continuous_quantum_region_regularity.py`](src/consciousness_bridge/continuous_quantum_region_regularity.py), [`test_continuous_quantum_region_regularity.py`](tests/test_continuous_quantum_region_regularity.py).
- **Proposition 41**: [p41_trace_ball_quantum_envelope.svg](docs/figures/p41_trace_ball_quantum_envelope.svg), [`trace_ball_quantum_envelope.py`](src/consciousness_bridge/trace_ball_quantum_envelope.py), [`test_trace_ball_quantum_envelope.py`](tests/test_trace_ball_quantum_envelope.py).
- **Proposition 42**: [p42_quantum_regular_bridge_sample_complexity.svg](docs/figures/p42_quantum_regular_bridge_sample_complexity.svg), [`quantum_regular_bridge_sample_complexity.py`](src/consciousness_bridge/quantum_regular_bridge_sample_complexity.py), [`test_quantum_regular_bridge_sample_complexity.py`](tests/test_quantum_regular_bridge_sample_complexity.py).
- **Proposition 43**: [p43_optimal_quantum_target_allocation.svg](docs/figures/p43_optimal_quantum_target_allocation.svg), [`optimal_quantum_target_allocation.py`](src/consciousness_bridge/optimal_quantum_target_allocation.py), [`test_optimal_quantum_target_allocation.py`](tests/test_optimal_quantum_target_allocation.py).
- **Proposition 44**: [p44_pair_adaptive_sample_allocation.svg](docs/figures/p44_pair_adaptive_sample_allocation.svg), [`pair_adaptive_sample_allocation.py`](src/consciousness_bridge/pair_adaptive_sample_allocation.py), [`test_pair_adaptive_sample_allocation.py`](tests/test_pair_adaptive_sample_allocation.py).
- **Proposition 45**: [p45_shared_preparation_graph_allocation.svg](docs/figures/p45_shared_preparation_graph_allocation.svg), [`shared_preparation_graph_allocation.py`](src/consciousness_bridge/shared_preparation_graph_allocation.py), [`test_shared_preparation_graph_allocation.py`](tests/test_shared_preparation_graph_allocation.py).
- **Proposition 46**: [p46_budget_constrained_witness_graph.svg](docs/figures/p46_budget_constrained_witness_graph.svg), [`budget_constrained_witness_graph.py`](src/consciousness_bridge/budget_constrained_witness_graph.py), [`test_budget_constrained_witness_graph.py`](tests/test_budget_constrained_witness_graph.py).
- **Proposition 47 - P47 sequential graph refinement and stopping**: [p47_sequential_graph_refinement.svg](docs/figures/p47_sequential_graph_refinement.svg), [`sequential_witness_graph.py`](src/consciousness_bridge/sequential_witness_graph.py), [`test_sequential_witness_graph.py`](tests/test_sequential_witness_graph.py).
- **Proposition 48 - P48 - gap-dependent sequential stopping complexity**: [p48_gap_dependent_stopping_complexity.svg](docs/figures/p48_gap_dependent_stopping_complexity.svg), [`gap_stopping_complexity.py`](src/consciousness_bridge/gap_stopping_complexity.py), [`test_gap_stopping_complexity.py`](tests/test_gap_stopping_complexity.py).
- **Proposition 49 - P49 - dyadic certification schedules**: [p49_dyadic_stopping_overhead.svg](docs/figures/p49_dyadic_stopping_overhead.svg), [`dyadic_stopping_overhead.py`](src/consciousness_bridge/dyadic_stopping_overhead.py), [`test_dyadic_stopping_overhead.py`](tests/test_dyadic_stopping_overhead.py).
- **Proposition 50 - P50 - bounded-starvation asynchronous sampling**: [p50_bounded_starvation_asynchronous_sampling.svg](docs/figures/p50_bounded_starvation_asynchronous_sampling.svg), [`bounded_starvation_sampling.py`](src/consciousness_bridge/bounded_starvation_sampling.py), [`test_bounded_starvation_sampling.py`](tests/test_bounded_starvation_sampling.py).
- **Proposition 51 - P51 - heterogeneous finite-window service-rate stopping**: [p51_heterogeneous_service_rate_stopping.svg](docs/figures/p51_heterogeneous_service_rate_stopping.svg), [`heterogeneous_service_stopping.py`](src/consciousness_bridge/heterogeneous_service_stopping.py), [`test_heterogeneous_service_stopping.py`](tests/test_heterogeneous_service_stopping.py).
- **Proposition 52 - P52 - capacity-optimal service allocation**: [p52_capacity_optimal_service_allocation.svg](docs/figures/p52_capacity_optimal_service_allocation.svg), [`capacity_optimal_service_allocation.py`](src/consciousness_bridge/capacity_optimal_service_allocation.py), [`test_capacity_optimal_service_allocation.py`](tests/test_capacity_optimal_service_allocation.py).
- **Proposition 53 - P53 - residual-demand reoptimization after safe pruning**: [p53_residual_demand_reoptimization.svg](docs/figures/p53_residual_demand_reoptimization.svg), [`residual_demand_reoptimization.py`](src/consciousness_bridge/residual_demand_reoptimization.py), [`test_residual_demand_reoptimization.py`](tests/test_residual_demand_reoptimization.py).
- **Proposition 54 - P54 - metric switching-cost residual scheduling**: [p54_metric_switching_cost_residual_scheduling.svg](docs/figures/p54_metric_switching_cost_residual_scheduling.svg), [`metric_switching_residual_schedule.py`](src/consciousness_bridge/metric_switching_residual_schedule.py), [`test_metric_switching_residual_schedule.py`](tests/test_metric_switching_residual_schedule.py).
- **Proposition 55 - P55 - pruning-aware metric switching-cost monotonicity**: [p55_pruning_aware_switching_monotonicity.svg](docs/figures/p55_pruning_aware_switching_monotonicity.svg), [`pruning_aware_switching_monotonicity.py`](src/consciousness_bridge/pruning_aware_switching_monotonicity.py), [`test_pruning_aware_switching_monotonicity.py`](tests/test_pruning_aware_switching_monotonicity.py).
- **Proposition 56 - P56 - moving-start metric reoptimization stability**: [p56_moving_start_metric_reoptimization_stability.svg](docs/figures/p56_moving_start_metric_reoptimization_stability.svg), [`moving_start_metric_reoptimization.py`](src/consciousness_bridge/moving_start_metric_reoptimization.py), [`test_moving_start_metric_reoptimization.py`](tests/test_moving_start_metric_reoptimization.py).
- **Proposition 57 - P57 - switching-metric perturbation reoptimization stability**: [p57_switching_metric_perturbation.svg](docs/figures/p57_switching_metric_perturbation.svg), [`switching_metric_perturbation.py`](src/consciousness_bridge/switching_metric_perturbation.py), [`test_switching_metric_perturbation.py`](tests/test_switching_metric_perturbation.py).
- **Proposition 58 - P58 - finite-data switching-metric uncertainty**: [p58_finite_data_metric_uncertainty.svg](docs/figures/p58_finite_data_metric_uncertainty.svg), [`finite_data_metric_uncertainty.py`](src/consciousness_bridge/finite_data_metric_uncertainty.py), [`test_finite_data_metric_uncertainty.py`](tests/test_finite_data_metric_uncertainty.py).
- **Proposition 59 - P59 - optimal transition-calibration allocation**: [p59_optimal_transition_calibration.svg](docs/figures/p59_optimal_transition_calibration.svg), [`optimal_transition_calibration.py`](src/consciousness_bridge/optimal_transition_calibration.py), [`test_optimal_transition_calibration.py`](tests/test_optimal_transition_calibration.py).
- **Proposition 60 - P60 - integer transition-calibration allocation**: [p60_integer_transition_calibration.svg](docs/figures/p60_integer_transition_calibration.svg), [`integer_transition_calibration.py`](src/consciousness_bridge/integer_transition_calibration.py), [`test_integer_transition_calibration.py`](tests/test_integer_transition_calibration.py).

</details>

---

# Detailed proposition record

The full chronological development history is intentionally kept off the main scientific reading path.

**[Read the complete P1 to P70 detailed proposition record](docs/detailed_proposition_record.md).**

The dedicated record preserves the complete lineage from P1 through P70, while this page is organized by scientific dependency rather than by the order in which results were developed.

---

# Current scientific status

| Item | Current state |
| --- | --- |
| Public theorem frontier | **P70** |
| Documented version | **v0.70.0** |
| Proposition-level results | **70** |
| Equation-driven quantitative figures | **61** |
| Physical-to-experiential bridge | **Open physical-to-experiential bridge** |
| Quantum ontology claim | **Not assumed** |
| Consciousness identified with a scalar, state of matter, or spacetime coordinate | **Not claimed** |
| Reproducibility | Python 3.10, 3.11, and 3.12 test matrix plus theorem-specific regression guards |

The scientific target is therefore precise: continue reducing ambiguity in the physical description, the experiential target, the admissible bridge class, and the experiment until either a bridge is derived and survives falsification or a valid obstruction demonstrates exactly where the declared physical description is insufficient.

---

# Navigation

| If you want to... | Go here |
| --- | --- |
| Understand the complete dependency structure | [Theorem roadmap](docs/theorem_roadmap.md) |
| Read the proposition chronology | [Detailed proposition record](docs/detailed_proposition_record.md) |
| Inspect the P61-P70 calibration and optimization branch | [Calibration and Optimization Frontier](docs/calibration_optimization_frontier_p61_p70.md) |
| Follow work by scientific question | [Research navigation](docs/research_navigation.md) |
| Audit equations and citations | [Equation and citation map](docs/equation_and_citation_map.md) |
| Inspect all quantitative classical figures | [Quantitative physics and mathematics atlas](docs/quantitative_physics_mathematics_atlas.md) |
| Inspect the quantum branch | [Quantum foundations and bridge test](docs/quantum_foundations_and_bridge_test.md) |
| Inspect falsification conditions | [Falsification program](docs/falsification_program.md) |
| Browse the public research website | [Website entry point](website/index.html) |
| Browse every visual | [Visual atlas](website/visual-atlas.html) |
| Audit code and tests | [`src/consciousness_bridge/`](src/consciousness_bridge/) and [`tests/`](tests/) |
| Cite the research | [Citation guide](CITATION.md), [`CITATION.cff`](CITATION.cff), and [`CITATION.bib`](CITATION.bib) |

---

## Scope statement

This repository is an ongoing research program. Its purpose is to make physical-to-experiential claims harder to state vaguely and easier to test rigorously. It should be read as a sequence of explicit mathematical conditions, counterexample constructions, finite-data certificates, and experimental design tools. The final bridge remains a scientific target, not a conclusion assumed in advance.

---

# Citation

If this research program, one of its propositions, figures, algorithms, or implementations contributes to your work, please cite it. When a specific theorem or artifact is central to an argument, cite both the overall research program and the proposition or artifact used.

## Preferred scholarly citation

> **Keikha, M. (2026). *Mathematical Consciousness Bridge: A Mathematical-Physics Test Architecture for the Physical-to-Experiential Bridge Problem* (Version 0.70.0). GitHub research repository. https://github.com/MahsaKeikha/mathematical-consciousness-bridge**

## BibTeX

```bibtex
@misc{keikha2026mathematicalconsciousnessbridge,
  author       = {Keikha, Mahsa},
  title        = {Mathematical Consciousness Bridge: A Mathematical-Physics Test Architecture for the Physical-to-Experiential Bridge Problem},
  year         = {2026},
  version      = {0.70.0},
  howpublished = {GitHub research repository},
  url          = {https://github.com/MahsaKeikha/mathematical-consciousness-bridge},
  note         = {Ongoing research program. Current documented theorem frontier: P70.}
}
```

For theorem-level attribution, identify the proposition explicitly, for example: `Proposition PXX, "Proposition title," in Mathematical Consciousness Bridge, Version 0.70.0`, together with the direct proposition URL. The [Detailed proposition record](docs/detailed_proposition_record.md) and [Theorem roadmap](docs/theorem_roadmap.md) provide the canonical proposition titles and proof links.

Because the repository is an evolving scientific record, reproducible citations should include the **documented version** and, when a result depends on an exact repository state, the **Git commit SHA** used in the analysis. No DOI is currently asserted. A DOI should be added only after a versioned archival deposit has actually issued one.

Citation resources: **[full citation guide](CITATION.md)** | **[machine-readable CFF](CITATION.cff)** | **[BibTeX](CITATION.bib)**