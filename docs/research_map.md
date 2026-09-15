# Research Map

**A guided map of the Mathematical Consciousness Bridge research program.**

If the main README tells you **what the project is about**, this page shows you **how the pieces fit together**.

You do not need to know the theorem numbers, equations, or implementation details to use this map. Those are available one layer deeper whenever you want them.

> ## The big idea
>
> **Before claiming that a physical description explains something about experience, we should be able to say exactly what was described, what was measured, what could falsify the model, and how uncertainty was handled.**

The research turns that broad requirement into a sequence of smaller questions.

![Research architecture](figures/research_architecture.svg)

The arrows in this figure show **research dependencies**. They do not mean that consciousness has already been reduced to physics.

---

## Chapter 1: What physical system are we talking about?

Before asking whether a physical description explains anything, we need to know what the description actually contains.

The early part of the project asks questions such as:

- Which physical variables matter?
- Which changes are merely changes of coordinates or labels?
- What can be measured or intervened on?
- How does the system persist through time?
- What happens when we describe it at a different scale?

The goal is to prevent a convenient representation from being mistaken for the physical system itself.

**Continue deeper:** [Technical research architecture](research_architecture.md) · [Theorem roadmap](theorem_roadmap.md)

---

## Chapter 2: Is the physical description actually enough?

A description can be extremely useful and still leave something out.

A road map, for example, may be perfect for navigation while saying nothing about temperature. In the same way, a physical descriptor can predict many observations while still losing a distinction relevant to the target we want to explain.

This part of the research asks a precise version of a simple question:

> **If two situations look identical according to the physical description, could the target still distinguish them?**

If the answer is yes, the chosen physical description is not sufficient for that target.

**Continue deeper:** [Bridge problem](bridge_problem.md) · [P19 physical sufficiency](proposition_19_fundamental_physical_sufficiency.md)

---

## Chapter 3: Is the target independent, or did we build the answer into it?

A bridge test can become circular if the target is created from the same physical information that is then claimed to explain it.

The project therefore separates the **physical description** from the **target being explained**.

This is a basic scientific safeguard: the evidence should not contain the conclusion by construction.

The target also needs a clear relationship to what is actually observed. Reports, behavior, labels, clinical judgments, and other measurements can all be incomplete or noisy.

**Continue deeper:** [Target research path](research_navigation.md) · [Glossary](glossary.md)

---

## Chapter 4: Can the proposed model be wrong?

A model becomes scientifically interesting when it risks failure.

Fitting data is not enough. A flexible model can sometimes reproduce observations without making a strong explanatory claim.

The later research therefore asks whether a proposed model of the target and its measurement imposes restrictions that the observed data can violate.

The progression is intentional:

**fit a model → test its assumptions → test the whole family → strengthen the test when simpler checks miss incompatibility.**

This is where much of the later proposition sequence becomes mathematically detailed. You do not need those details to understand the purpose: **the model must face evidence that could reject it.**

**Continue deeper:** [Falsification program](falsification_program.md) · [Detailed proposition record](detailed_proposition_record.md)

---

## Chapter 5: Does the conclusion survive uncertainty?

Real data are finite. Numerical calculations have approximation error. A result found after searching many possibilities can look stronger than it really is.

So the project asks another question:

> **Would the conclusion still be justified after we account for the ways uncertainty enters the analysis?**

This includes statistical uncertainty, numerical certification, model selection, and reproducibility.

The goal is not merely to obtain a striking number. It is to know **which direction the evidence actually supports and how strongly**.

**Continue deeper:** [Reproducibility guide](reproducibility.md) · [Equation and citation map](equation_and_citation_map.md)

---

## Chapter 6: What remains open?

Even a mathematically correct rejection of a model does not tell us automatically what consciousness is.

It may show that a particular physical descriptor is incomplete, that a measurement model is inadequate, or that a declared model family cannot reproduce the observations under its assumptions.

Those are meaningful scientific results. They are not the same as proving that consciousness is nonphysical, identifying a latent variable with experience, or completing the final bridge from physical description to experience.

That final bridge remains open.

This is not a weakness hidden by the repository. It is one of the central organizing principles of the research.

---

## Where the current work sits

The public theorem frontier is **P97** and the formal release remains **v0.82.0**.

P94 extends the P93 localized seven-cell rejection theorem from IID observations to a declared finite-range dependent sequence with one common marginal four-view law. The squared finite-sample radius carries the exact factor `m+1` for dependence range `m`, while the P92 determinant geometry is unchanged.

P94 also proves an exact temporal-pooling no-go: two individually valid interior P75 regimes can pool to a law with the negative determinant-product sign pattern used for rejection. Arbitrary marginal drift is therefore a separate problem and is not silently treated as finite-range dependence.

If you want the current result itself, open **[P97](proposition_97_simultaneous_candidate_family_selection.md)**. For the previous independent-holdout frontier, open **[P96](proposition_96_selection_valid_holdout_stratification.md)**. For the finite-range single-marginal predecessor, open **[P94](proposition_94_finite_range_dependent_sign_coherence.md)**. For the IID predecessor, open **[P93](proposition_93_localized_sign_coherence_rejection.md)**. For the complete dependency chain, use the **[Theorem Roadmap](theorem_roadmap.md)**.

---

## Choose a trail

| Your interest | Best route |
| --- | --- |
| **I am new to consciousness research** | [Bridge Problem](bridge_problem.md) → [Glossary](glossary.md) → [Falsification Program](falsification_program.md) |
| **I come from physics** | [Technical Research Architecture](research_architecture.md) → [Quantum Foundations](quantum_foundations_and_bridge_test.md) → [Theorem Roadmap](theorem_roadmap.md) |
| **I come from mathematics or statistics** | [Theorem Roadmap](theorem_roadmap.md) → [Detailed Proposition Record](detailed_proposition_record.md) → individual proposition proofs |
| **I want the visuals first** | [Figure Catalog](figure_catalog.md) → [Visual Atlas](../website/visual-atlas.html) |
| **I want to audit the code** | [Reproducibility Guide](reproducibility.md) → [`src/consciousness_bridge/`](../src/consciousness_bridge/) → [`tests/`](../tests/) |
| **I want sources and provenance** | [Equation and Citation Map](equation_and_citation_map.md) → [Citation Guide](../CITATION.md) |
| **I want the complete research record** | [Research Navigation](research_navigation.md) → [Detailed Proposition Record](detailed_proposition_record.md) |

---

## How the layers are meant to work

| Layer | Purpose |
| --- | --- |
| **README** | Spark the question and explain why the project exists. |
| **Start Here** | Explain the research logic in plain language. |
| **Research Map** | Show how the major scientific questions connect. |
| **Technical architecture / theorem roadmap** | Show formal structure and mathematical dependencies. |
| **Individual proposition pages** | State assumptions, theorem, proof, implementation, and limits. |
| **Provenance / code / tests** | Make each technical result auditable and reproducible. |

If a page feels too technical for the question you are asking, move **one layer up**. If it feels too shallow, move **one layer down**.

---

## The scientific promise of the repository

The aim is not to make consciousness sound mysterious by adding more mathematics.

The aim is to make every proposed bridge claim easier to question:

**What exactly was assumed? What was measured? What could make the claim fail? What uncertainty remains? What conclusion is actually justified?**

That is the thread connecting the entire project.

---

**Previous layer:** [Start Here](../START_HERE.md)
**Next formal layer:** [Technical Research Architecture](research_architecture.md)
**Full mathematical dependency map:** [Theorem Roadmap](theorem_roadmap.md)
**Complete audit record:** [Detailed Proposition Record](detailed_proposition_record.md)


### P89 complete linear parity-functional closure

P89 closes the complete real linear parity-functional class on the eleven canonical P83 parity coordinates for a fixed rational P75 parameter box. Matching exact rational lower and upper certificates give `L89 = 5/168` on the published strict witness, strictly above `L88 = 1/64`. Nonlinear model constraints and the physical-to-experiential bridge remain open.

### P93 historical IID finite-sample sign-coherence rejection

P93 is the historical IID finite-sample handoff from P92. It uses only seven selected cells and exact P79 sampling-radius certification. [Read P93](proposition_93_localized_sign_coherence_rejection.md).

### P94 finite-range dependent sign-coherence rejection

P94 is a historical finite-range Research II step. It preserves the seven-cell P92/P93 nonlinear witness under a declared finite-range dependent sequence with one common marginal law, using exact rational certification of the dependence-adjusted confidence radius. Its exact pooling counterexample also marks the limit of that extension: arbitrary temporal drift remains outside the theorem. [Read P94](proposition_94_finite_range_dependent_sign_coherence.md).

### P95: What if the marginal law drifts across predeclared regimes?

P95 does not pool those regimes. It gives each predeclared regime its own marginal law, finite-range dependence assumption, sample size, and error budget. Local P94 certificates are then combined by a familywise union bound. If any regime is certified outside P75, the all-regimes P75 null is rejected at the declared familywise confidence. [Read P95](proposition_95_drift_aware_stratified_sign_coherence.md).


## P96: selection-valid holdout stratification

P96 closes one explicit adaptive-selection gap left by P95. Pilot information may select the finite regime plan, dependence ranges, and rational error allocation. The plan is frozen before a genuinely independent certification sample is evaluated. Conditioning on the pilot information makes the selected P95 plan fixed, and the tower property preserves the same unconditional familywise bound.

This is a sample-separation theorem, not a general same-data post-selection result. Pilot observations do not count as certification observations, and a naive split of one temporally dependent stream is not automatically independent.


## P97: simultaneous finite candidate-family selection

P97 addresses a complementary selection problem to P96. Instead of separating pilot and holdout data, it permits the same certification data to be reused across a finite family of candidate regime plans, provided the complete family is fixed before the certification statistics are inspected.

Each candidate receives its own exact P95 familywise error budget. A second union bound across candidates produces one simultaneous event on which every candidate certificate is valid. The final candidate may therefore be selected after inspection without invalidating the selected certificate.

For two equally budgeted candidates with two one-step-dependent regimes each, the 95 percent threshold is 4045 observations per regime, with first exact denominator-24 replication at 4056. The multiplicity cost replaces P96's sample-separation cost.

P97 does not justify creating a new candidate after inspection, unbounded same-data search, unrestricted within-regime drift, model acceptance after non-rejection, consciousness identification, nonphysicality, or completion of the physical-to-experiential bridge.
