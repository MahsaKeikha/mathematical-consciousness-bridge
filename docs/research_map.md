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

The public theorem frontier is **P89** and the formal release is **v0.82.0**.

P87 belongs to the later **model testing** part of the program. It strengthens a declared family of exact model separation tests. Its importance is methodological: it asks whether a more complete family of constraints that share the same parameters can expose incompatibility that weaker tests miss.

If you want the result itself, open **[P87](proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md)**.

If you want to understand how P87 emerged from earlier work, use the **[Theorem Roadmap](theorem_roadmap.md)**.

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
