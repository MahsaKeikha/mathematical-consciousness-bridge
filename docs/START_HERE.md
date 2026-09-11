# Start Here: A First-Time Reader Guide

## What is this repository trying to understand?

The **Mathematical Consciousness Bridge** asks a difficult scientific question in a deliberately careful way:

> If we had a very detailed physical description of a system, what would we need to prove before we could legitimately say that the description is sufficient to account for a distinction in experience?

The repository does **not** begin by assuming that consciousness is a particular brain signal, information quantity, quantum state, field, complexity measure, or mathematical object. It also does not assume that consciousness is outside physics.

Instead, the project asks what a scientifically defensible bridge between physical description and experiential description would have to satisfy.

The central problem is therefore not "find one equation for consciousness." The problem is:

1. define what physical information is being used;
2. define what experiential distinction is being tested;
3. make sure the experiential target was not secretly constructed from the same physical variables;
4. understand how that target is measured and how measurement errors can distort it;
5. test whether the physical description really contains enough information to determine the target;
6. quantify uncertainty from finite data;
7. design experiments that could prove the proposed bridge wrong;
8. separate what has been mathematically established from what remains scientifically open.

That is the organizing logic of the entire repository.

---

# The shortest possible summary

Suppose two physically admissible situations are represented by \(\omega_1\) and \(\omega_2\).

Let

\[
T(\omega)
\]

mean "the physical description we chose," and let

\[
E(\omega)
\]

mean "the independently justified experiential distinction we want the physical description to explain."

A deterministic physical-to-experiential bridge would require some rule \(B\) such that

\[
E=B\circ T.
\]

In plain language:

> once the physical description \(T\) is known, the target \(E\) must be determined by it.

This gives an immediate falsification principle:

\[
T(\omega_1)=T(\omega_2)
\quad\text{but}\quad
E(\omega_1)\neq E(\omega_2)
\]

means that the declared physical description is **not sufficient** for that declared target.

This is a statement about the adequacy of a particular physical description. It is **not** automatically a statement that experience is nonphysical. The physical description may simply be incomplete, too coarse, measured at the wrong scale, or missing an important variable.

The stochastic version of the same idea is expressed by the conditional-information residual

\[
I(E;\Omega\mid T).
\]

If this quantity is positive under the declared model, then the target still contains distinctions about the underlying physical situation that were not screened off by \(T\).

Everything else in the repository exists to make statements like these scientifically meaningful rather than merely formal.

---

# Why the project has so many propositions

The bridge question looks simple only if we ignore the assumptions hidden inside it.

For example, before testing whether \(T\) explains \(E\), we need to know:

- whether \(T\) changes when the same physics is represented in different coordinates;
- whether the important structure survives coarse-graining;
- whether interventions and time matter;
- whether the target \(E\) was defined independently from \(T\);
- whether the target can be observed reliably;
- whether several target measurements share hidden errors;
- whether a latent target-measurement model is actually identifiable;
- whether finite data are sufficient to distinguish a real violation from sampling noise;
- whether an optimizer has found a true global separation or only a local numerical fit;
- whether repeated looks at the data have invalidated the confidence guarantee.

The proposition sequence isolates these issues so that one hidden assumption does not silently contaminate the whole argument.

The propositions should therefore be read as **scientific obligations** and **mathematical safeguards**, not as 79 independent theories of consciousness.

---

# The research in eight layers

## Layer 1: What counts as the same physical description?

**P1-P10** establish representation invariance, experimental distinguishability, recoverability, and robust protocol design.

The purpose is to avoid confusing a change in coordinates, notation, or representation with a change in the underlying physical situation.

**Main idea:** a scientifically meaningful bridge should depend on physical structure, not arbitrary description choices.

Start with the [Theorem Roadmap](theorem_roadmap.md) if you want the exact proposition dependency chain.

---

## Layer 2: What physical structure should be included?

**P11-P18** build intervention-resolved, temporal, compositional, and multiscale physical structure.

A physical system is not only a static vector of measurements. It can respond differently to interventions, evolve through time, interact across components, and look different at different scales.

**Main idea:** before asking whether a physical description is sufficient, we must say what physical distinctions the description is actually preserving.

A visual entry point is the main README's research-architecture figure and the [quantitative physics and mathematics atlas](quantitative_physics_mathematics_atlas.md).

---

## Layer 3: What would physical sufficiency mathematically mean?

**P19-P24** contain the central bridge-test logic.

P19 asks whether the target factors through the physical descriptor. P20-P24 add finite-data confidence, descriptor refinement, and adaptive validity.

The core deterministic test is

\[
T(\omega_1)=T(\omega_2)
\Rightarrow
E(\omega_1)=E(\omega_2).
\]

The core stochastic residual is

\[
I(E;\Omega\mid T).
\]

**Main idea:** the repository turns "does physics explain the target?" into a falsifiable sufficiency statement relative to a declared physical description and a declared target.

Read [P19 Fundamental Physical Sufficiency](proposition_19_fundamental_physical_sufficiency.md) for the formal theorem.

---

## Layer 4: Can the target itself be trusted?

**P71-P79** form the target-side validity branch.

This branch is especially important because a bridge test is meaningless if the target was constructed circularly or measured unreliably.

- **P71:** a target built from the same descriptor being tested cannot serve as independent evidence for that descriptor's sufficiency.
- **P72:** target measurement noise can weaken or erase a real witness.
- **P73:** under a restricted three-view latent model, target-channel reliability can be identifiable in principle.
- **P74:** finite data must be strong enough before that recovered reliability is trusted.
- **P75:** identifiability does not automatically mean that the measurement model is adequate.
- **P76:** finite data can reject tracked necessary constraints when violations exceed uncertainty.
- **P77:** a stronger full-law test asks whether the entire confidence region is separated from the entire declared model family.
- **P78:** a certified global computation supplies rigorous lower and upper bounds for the continuous P75 model family.
- **P79:** the P77-P78 interface becomes a three-way decision: certified rejection, certified non-separation, or computationally unresolved.

**Main idea:** before using an experiential target to test a physical theory, the target's provenance, measurement, reliability, model adequacy, finite-data uncertainty, and computational certification must be examined explicitly.

This branch does **not** prove that its latent variable is consciousness. It is a measurement methodology branch.

---

## Layer 5: Does the result survive changes of physical scale?

**P25-P37** study operational coarse-graining and quotient structure.

**Main idea:** a bridge claim should not become true or false merely because we used a convenient but unjustified aggregation of the physical system.

These propositions track what happens to causal influence, intervention labels, temporal structure, and response geometry when physical descriptions are compressed.

---

## Layer 6: What changes if the physical description is quantum?

**P38-P44** repeat the sufficiency logic for declared operational quantum descriptions.

The basic quantum prediction rule

\[
p(a\mid M)=\operatorname{Tr}(\rho M_a)
\]

specifies physical measurement probabilities. It does **not** by itself specify experience.

**Main idea:** even a quantum-complete description of a declared experiment still requires an additional bridge rule if one wants to make a claim about experience.

Read [Quantum Foundations and Bridge Test](quantum_foundations_and_bridge_test.md) for the complete branch.

---

## Layer 7: How should decisive experiments be collected?

**P45-P60** develop adaptive experiment design, sequential validity, stopping rules, scheduling, and transition calibration.

**Main idea:** an elegant theorem is not enough if the experimental procedure used to test it invalidates the statistical guarantee.

This branch addresses repeated looks at data, adaptive sampling, resource constraints, switching costs, and experiment scheduling.

---

## Layer 8: How should finite resources be allocated after the scientific witness is defined?

**P61-P70** form a downstream calibration and optimization branch.

These propositions solve resource-allocation problems once the scientific target and witness structure have already been declared.

**Main idea:** optimization improves the efficiency of a valid scientific test; it does not create the validity of the bridge claim itself.

Read [Calibration and Optimization Frontier P61-P70](calibration_optimization_frontier_p61_p70.md) for this branch.

---

# What has actually been established?

The repository has established a growing mathematical test architecture. Among other things, it has formalized:

- exact, stochastic, and differential criteria for sufficiency relative to declared variables;
- collision-based falsification of descriptor sufficiency;
- finite-sample certification of information-theoretic residuals;
- descriptor-refinement identities that quantify what extra physical information adds;
- representation, intervention, temporal, compositional, and multiscale consistency requirements;
- target-provenance non-circularity;
- target-measurement attenuation and stability bounds;
- restricted latent target-channel identifiability results;
- finite-sample recovery and model-adequacy checks;
- full-law confidence-region model-set separation;
- certified global lower and upper bounds for a continuous four-view latent model family;
- a three-way full-law decision rule that separates rejection, non-separation, and unresolved computation;
- operational quantum sufficiency tests under explicit bridge classes;
- adaptive and resource-aware experimental design methods.

These are mathematical and methodological results. They are not a completed theory of consciousness.

---

# What has not been established?

The repository does **not** currently prove that consciousness:

- is a state of matter;
- is a quantum phenomenon;
- is a field;
- is a scalar quantity;
- is an additional spacetime dimension;
- is reducible to current physics;
- is irreducible to physics;
- is identical to any latent variable used in the target-measurement examples.

It also does not claim that quantum mechanics is incomplete because consciousness exists.

The central physical-to-experiential bridge remains open.

This boundary is not a weakness in the project. It is part of the scientific design. The repository is intended to make it difficult to accidentally "prove" a conclusion that was already hidden inside the assumptions.

---

# A simple example

Imagine a researcher proposes a physical descriptor \(T\) that groups two experimental situations together because, according to the chosen measurements, they are physically indistinguishable.

Suppose an independently justified target \(E\) distinguishes them.

Then the proposed descriptor has failed a sufficiency test.

But what should we conclude?

Not immediately that "consciousness is beyond physics."

A scientifically careful interpretation is:

> The declared physical descriptor is not sufficient for the declared target under the declared assumptions.

The next question is whether the physical description should be refined, whether the target measurement is trustworthy, whether the system boundary was chosen correctly, whether the scale was too coarse, or whether the bridge class itself was overly restrictive.

The repository is designed to keep those possibilities separate.

---

# How to read the mathematics without getting lost

You do not need to understand every equation to understand the research logic.

When you encounter a theorem, ask four questions:

1. **What are the objects?** For example, a physical descriptor \(T\), a target \(E\), an empirical distribution, or a model family.
2. **What is being assumed?** For example, IID sampling, conditional independence, a bridge regularity class, or an independently constructed target.
3. **What is being proved?** Look for an implication, bound, obstruction, or certificate.
4. **What is explicitly not being claimed?** Each major proposition records its scientific boundary.

A proof in this repository is always conditional on its stated assumptions. That is especially important in the target-measurement branch, where latent-variable assumptions are methodological models rather than ontological declarations.

---

# Three recommended reading paths

## If you are new to the subject

Read in this order:

1. this page;
2. the [main README](../README.md), especially the research architecture and plain-language sections;
3. the [Plain-Language Glossary](plain_language_glossary.md);
4. [Bridge Problem](bridge_problem.md);
5. [P19 Fundamental Physical Sufficiency](proposition_19_fundamental_physical_sufficiency.md);
6. [P71 Target-Provenance Non-Circularity](proposition_71_target_provenance_noncircularity.md);
7. [P72-P79 target-side branch](research_navigation.md);
8. the [Falsification Program](falsification_program.md).

You can understand the scientific argument without reading every proposition.

## If you are a technical reader

Read:

1. [Theorem Roadmap](theorem_roadmap.md);
2. [Detailed Proposition Record](detailed_proposition_record.md);
3. the proposition documents relevant to your branch of interest;
4. [Equation and Citation Map](equation_and_citation_map.md);
5. implementation and regression tests linked from each proposition.

## If you are auditing rigor or reproducibility

Read:

1. [Scientific Status Discipline](../README.md#scientific-status-discipline);
2. [Equation and Citation Map](equation_and_citation_map.md);
3. proposition-specific provenance records;
4. [Falsification Program](falsification_program.md);
5. [Citation and Reference Policy](citation_and_reference_policy.md);
6. source files and tests linked from each theorem;
7. GitHub Actions results for the current branch or release.

---

# Key words in one paragraph

A **descriptor** is the physical information being tested. A **target** is the independently justified distinction the descriptor is supposed to explain. A **bridge** is a rule connecting descriptor to target. A **fiber** is the set of physical situations that share the same descriptor value. A **collision** occurs when two situations have the same descriptor but different target values. A **residual** measures target information that remains after conditioning on the descriptor. A **certificate** is a mathematically justified finite-data or computational conclusion under stated assumptions. **Non-rejection** or **non-separation** means the current test could not rule out the model; it is not the same as proving the model true.

For more definitions, use the [Plain-Language Glossary](plain_language_glossary.md).

---

# Where the project stands now

The current development frontier is **P79**, built on the P77-P78 full-law testing framework. The public release metadata is promoted only after the new frontier passes its complete regression and documentation checks.

P79 sharpens the computational interpretation of full-law testing. Given a certified P78 distance bracket and certified bounds on the P77 sampling radius, the result is one of three states:

\[
\text{rejection},\qquad
\text{non-separation},\qquad
\text{or unresolved computation}.
\]

The important scientific point is that **non-separation is not model acceptance**. It means only that the current P77 confidence region still intersects the declared model family.

The physical-to-experiential bridge itself remains open.

---

# One sentence to remember

> This repository is not trying to assume an answer to consciousness and mathematize it. It is trying to define what would have to be measured, proved, falsified, and independently validated before a physical-to-experiential claim could deserve scientific confidence.
