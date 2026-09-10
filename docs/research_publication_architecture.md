# Research Publication Architecture

This document defines the public scientific structure for the Mathematical Consciousness Bridge project. Its purpose is to keep a large and growing research program readable, auditable, reproducible, and appropriately cautious as new propositions, experiments, figures, and implementation results are added.

## 1. Scientific objective

The project asks a constrained question:

> What mathematical and physical conditions would be required for a complete physical description of a system to support a scientifically testable claim about consciousness?

The project does not assume that consciousness is a quantum variable, a state of matter, an information measure, a spacetime coordinate, or any other preferred physical object. Instead, it develops mathematical tests of physical sufficiency, distinguishability, reconstructability, scale consistency, temporal consistency, intervention structure, finite-data reliability, and experimental design.

Every public explanation should preserve this distinction.

## 2. Five-layer claim taxonomy

Every substantive scientific statement should belong to exactly one primary layer.

### Layer A. Standard mathematics

Examples include total variation distance, convexity, KKT conditions, concentration inequalities, Bellman recursion, graph quotients, trace distance, and standard asymptotic or optimization results.

Requirements:

- cite a standard primary or authoritative source when the result is not elementary;
- identify the result as standard mathematics;
- do not present the result as repository-original merely because it is used in a new context.

### Layer B. Established physical theory

Examples include density operators, quantum channels, POVMs, open-system dynamics, classical stochastic response laws, and standard operational predictions of quantum mechanics.

Requirements:

- cite authoritative physics literature;
- state the physical domain and assumptions;
- distinguish formal mathematical completeness from empirical completeness;
- avoid extrapolating beyond the cited physical framework.

### Layer C. External empirical evidence

Examples include measured neural signatures, behavioral discriminability, anesthesia or sleep-state evidence, perturbational studies, or clinical measurement literature.

Requirements:

- cite primary studies or major reviews;
- describe exactly what was measured;
- distinguish correlation, prediction, intervention, and causation;
- never describe empirical neural evidence as a proof of an experiential bridge.

### Layer D. Repository-original theorem or computational result

Examples include propositions P1-P64, repository-specific finite-data certificates, scale-compatibility theorems, and transition-calibration optimization results.

Requirements:

- cite the local proposition number;
- link directly to its proof, implementation, test, and visual when each exists;
- state all mathematical assumptions explicitly;
- give the strongest exact conclusion justified by the proof, and no stronger;
- include boundary cases and failure regimes.

### Layer E. Open hypothesis, research target, or conjecture

Examples include candidate bridge laws, physical-to-experiential nonfactorization targets, and possible future extensions involving quantum foundations.

Requirements:

- label the claim as open;
- state what evidence or theorem would be required to promote it to a stronger status;
- list known alternative explanations or unresolved dependencies;
- never format a conjecture so that it visually resembles a proved proposition.

## 3. Required structure for each proposition

Every proposition-level result should be documented with the following fields.

1. **Scientific question**: the exact problem being solved.
2. **Inputs and assumptions**: mathematical objects, probability model, physical assumptions, finite-data assumptions, and regularity conditions.
3. **Statement**: a compact theorem statement using stable notation.
4. **Interpretation**: what the theorem means operationally or physically.
5. **Proof**: complete derivation or a link to the complete derivation.
6. **Computation**: implementation path and algorithmic complexity when relevant.
7. **Validation**: tests, numerical checks, simulation regime, and failure cases.
8. **Figure**: at least one self-explanatory figure for nontrivial geometric, statistical, quantum, graph, or optimization results.
9. **Provenance**: standard results used and local propositions depended upon.
10. **Scientific boundary**: what the result does not establish.

The proposition is considered publication-complete only when these fields are mutually consistent.

## 4. Required structure for figures

A scientific figure should be understandable even when viewed before the surrounding prose.

Every figure should have:

- a descriptive title;
- labeled axes or labeled objects;
- units where units exist;
- a legend whenever multiple quantities appear;
- a short statement of the mathematical quantity being shown;
- the assumption regime;
- the proposition or equation it illustrates;
- a caption stating what the reader is allowed to conclude;
- a source note distinguishing generated data, simulation data, external data, or schematic content.

Decorative imagery should never substitute for a quantitative figure.

## 5. Required structure for physics pages

Every physics-facing page should use this order:

1. Physical system and state space.
2. Dynamical law or admissible channel family.
3. Interventions and measurements.
4. Operationally observable probability law.
5. Coarse-graining or scale map, if any.
6. Statistical uncertainty model.
7. Repository theorem applied to that physical structure.
8. Empirical observables that could instantiate the variables.
9. Explicit statement of what remains outside the physical formalism.

This prevents mathematical notation from being mistaken for a physical claim.

## 6. Required structure for consciousness-facing pages

A consciousness-facing page should distinguish three objects that are often conflated:

- the **physical descriptor** of a system;
- the **measured or reported target variable** used in an experiment;
- the **experiential interpretation** attached to that target.

The project can mathematically test whether a declared target factors through a declared physical descriptor. That is not automatically equivalent to proving an ontological theory of consciousness.

Any page discussing experiential interpretation must state the operational definition used to obtain the target data.

## 7. Citation and provenance requirements

The repository already maintains several reference layers. The public documentation should preserve them as distinct sources of evidence:

- `references.bib`: general research references;
- `foundational_physics_mathematics.bib`: standard physics and mathematics;
- `empirical_consciousness_measurement.bib`: empirical consciousness-related measurement literature;
- `docs/fundamental_theory_references.bib`: references used by the fundamental-theory interface;
- `docs/equation_and_citation_map.md`: equation-level provenance and proposition lineage;
- `docs/reference_audit.md`: metadata and evidence-role checks;
- `docs/literature_map.md`: conceptual role of external consciousness literature.

For every important equation, the reader should be able to determine whether it is:

- standard;
- adapted from a cited source;
- derived directly from earlier repository propositions;
- newly proved in the repository;
- only a declared modeling assumption.

## 8. Website information architecture

The public research website should have six primary entry points.

### Overview

A concise scientific statement of the problem, scope, nonclaims, and current status.

### Research program

A visual map of the proposition sequence grouped by scientific function rather than by chronology alone.

### Physics and mathematics

Foundational state descriptions, intervention structure, geometry, quantum operational framework, finite-sample statistics, graph and scale mathematics, and optimization.

### Evidence and falsification

Operational targets, empirical measurement interfaces, finite-data tests, failure modes, and what observations could count against a declared model.

### Results and figures

A figure-first atlas of theorem outputs, numerical demonstrations, and visual maps. Every figure should link back to the proposition and equation from which it was generated.

### Sources and reproducibility

Bibliographies, citation policy, theorem dependencies, code, tests, version information, and release history.

## 9. Reader paths

The site and repository should support at least four reader types.

### Physicist

Start with physical state description, interventions, operational equivalence, scale maps, quantum tomography, and the nonfactorization program.

### Mathematician

Start with the proposition roadmap, theorem dependencies, proofs, optimization structure, concentration bounds, graph quotients, and exact/approximate algorithms.

### Experimental scientist

Start with measurable variables, falsification program, finite-data certificates, sample-complexity results, adaptive sampling, and calibration design.

### Interdisciplinary reader

Start with the plain-language overview, scientific boundary, visual research map, and selected figures before entering formal notation.

## 10. Global coherence checks

Before a major release, automated checks should verify at minimum:

- proposition count agrees across README, roadmap, website, citation metadata, and release notes;
- latest version agrees across README, `pyproject.toml`, `CITATION.cff`, website, and changelog;
- every proposition link resolves;
- every figure referenced by a proposition exists;
- every repository-original result is labeled as such;
- external empirical claims have external references;
- open hypotheses are not labeled as established results;
- all equations referred to by number exist in the equation-and-citation map;
- website navigation has no dead local links.

## 11. Scientific language standard

Preferred language:

- "under the declared assumptions";
- "the theorem proves";
- "the data support";
- "the experiment can distinguish";
- "the model remains compatible with";
- "this result does not establish";
- "an additional bridge law would still be required".

Avoid language that implies importance, finality, or prestige as a substitute for evidence. The scientific strength of the project should come from explicit assumptions, transparent mathematics, reproducible computation, discriminating experiments, and accurate citation.

## 12. Long-term publication objective

The repository and website should function together as a living research monograph. A reader should be able to move from the physical foundations to the current theorem frontier without guessing what is assumed, what is proved, what is measured, or what remains unknown.

The goal is not maximal volume. The goal is a complete chain of justified inference.
