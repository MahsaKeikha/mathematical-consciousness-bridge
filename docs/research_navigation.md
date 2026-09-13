# Research Navigation

**Use this page when you know what kind of detail you want and need the shortest route to it.**

This page is an index, not another chapter. If you are still learning the overall story, go one layer up to the **[Research Map](research_map.md)**.

The public theorem frontier is **P88**. The formal release is **v0.82.0**. The final bridge from physical description to experience remains open.

---

## Choose by question

| I want to find... | Go here |
| --- | --- |
| The overall scientific story | [Research Map](research_map.md) |
| The formal physical and bridge architecture | [Technical Research Architecture](research_architecture.md) |
| The central sufficiency problem | [Bridge Problem](bridge_problem.md) |
| The dependency structure of the mathematics | [Theorem Roadmap](theorem_roadmap.md) |
| Every proposition in chronological order | [Detailed Proposition Record](detailed_proposition_record.md) |
| What could falsify a claim | [Falsification Program](falsification_program.md) |
| Equation and source provenance | [Equation and Citation Map](equation_and_citation_map.md) |
| All figures and their interpretation | [Figure Catalog](figure_catalog.md) |
| Code, tests, and reproducibility | [Reproducibility Guide](reproducibility.md) |
| Definitions of recurring terms | [Glossary](glossary.md) |
| Citation guidance | [Citation Guide](../CITATION.md) |

---

## Choose by scientific branch

### Physical foundations

**Question:** What physical structure is actually being described, and which parts are invariant, identifiable, causal, temporal, compositional, or dependent on scale?

**Results:** P1 through P18, and P25 through P37

**Start with:** [Technical Research Architecture](research_architecture.md) · [Theorem Roadmap](theorem_roadmap.md)

---

### Physical sufficiency

**Question:** Does the declared physical descriptor preserve every distinction required by an independently specified target?

**Results:** P19 through P24

**Start with:** [P19: Fundamental Physical Sufficiency](proposition_19_fundamental_physical_sufficiency.md)

Then use the [Theorem Roadmap](theorem_roadmap.md) for the extensions involving finite data, refinement, selection, and repeated analysis.

---

### Quantum operational branch

**Question:** What can a complete operational quantum description establish, and what still requires an independent bridge principle?

**Results:** P38 through P44

**Start with:** [Quantum Foundations and Bridge Test](quantum_foundations_and_bridge_test.md)

---

### Experiment design and calibration

**Question:** How should evidence be collected, scheduled, and allocated without losing statistical validity or wasting resources?

**Results:** P45 through P70

**Start with:** [Theorem Roadmap](theorem_roadmap.md) · [Calibration and Optimization Frontier](calibration_optimization_frontier_p61_p70.md)

---

### Target integrity and measurement

**Question:** Is the target independent of the physical descriptor, and can its measurement be trusted?

**Results:** P71 through P74

This branch addresses circular targets, noisy observation, identifiability of the measurement channel, and recovery from finite data.

**Start with:** [P71: Target Provenance Noncircularity](proposition_71_target_provenance_noncircularity.md)

Then follow P72 through P74 in the [Detailed Proposition Record](detailed_proposition_record.md).

---

### Model adequacy and exact separation

**Question:** Can the declared model of the target and its measurement actually reproduce the observations, or can it be rejected under its own assumptions?

**Results:** P75 through P87

This branch moves from model adequacy to rejection with finite data, separation from the complete declared model set, certified bounds for continuous families, and increasingly strong exact tests that preserve shared parameters.

**Start with:** [P75: Target Model Adequacy](proposition_75_target_model_adequacy_overidentification.md)

**Current frontier:** [P87: Exact Bounded Primitive Four Event Projection Parity Functional Certificate](proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md)

---

## Audit the current frontier without searching folders

For P87:

| What you want | Direct link |
| --- | --- |
| The theorem and proof | [P87 proposition](proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md) |
| Equation and method provenance | [P87 provenance](p87_equation_provenance.md) |
| Implementation | [`bounded_primitive_quad_projection_parity_functional_separation.py`](../src/consciousness_bridge/bounded_primitive_quad_projection_parity_functional_separation.py) |
| Regression tests | [`test_bounded_primitive_quad_projection_parity_functional_separation.py`](../tests/test_bounded_primitive_quad_projection_parity_functional_separation.py) |
| Figure | [P87 theorem figure](figures/p87_exact_bounded_primitive_quad_projection_parity.svg) |
| Repository reproduction | [Reproducibility Guide](reproducibility.md) |

P87 is a conditional model separation result for the declared P75 family. It does not identify the latent state with consciousness or close the final bridge from physical description to experience.

---

## How to audit any proposition

Every mature result is intended to follow the same chain:

**question → assumptions → theorem → proof → implementation → tests → provenance → scientific boundary**

You do not need every link for every purpose.

- If you want the **idea**, read the proposition introduction and conclusion.
- If you want the **mathematics**, read the theorem and proof.
- If you want to **verify the computation**, inspect the source and tests.
- If you want to know **where an equation came from**, open its provenance record.
- If you want to know **what the result does not establish**, read the scientific boundary section.

The [Detailed Proposition Record](detailed_proposition_record.md) is the complete proposition audit trail.

---

## Choose by background

| Your background | Suggested path |
| --- | --- |
| Physics | [Research Map](research_map.md) → [Technical Research Architecture](research_architecture.md) → [Quantum branch](quantum_foundations_and_bridge_test.md) |
| Mathematics | [Research Map](research_map.md) → [Theorem Roadmap](theorem_roadmap.md) → proposition proofs |
| Statistics and inference | [P19](proposition_19_fundamental_physical_sufficiency.md) → P20 through P24 → P74 through P87 via [Detailed Proposition Record](detailed_proposition_record.md) |
| Consciousness science | [Bridge Problem](bridge_problem.md) → [Falsification Program](falsification_program.md) → P71 through P87 |
| Software and reproducibility | [Reproducibility Guide](reproducibility.md) → [`src/`](../src/) → [`tests/`](../tests/) |
| Visual learner | [Figure Catalog](figure_catalog.md) → [Visual Atlas](../website/visual-atlas.html) |

---

## Where the complete detail lives

This page intentionally does **not** duplicate the full 87 proposition index.

Use:

- **[Detailed Proposition Record](detailed_proposition_record.md)** for the complete chronological record;
- **[Theorem Roadmap](theorem_roadmap.md)** for mathematical dependencies;
- **[Equation and Citation Map](equation_and_citation_map.md)** for provenance;
- **[Figure Catalog](figure_catalog.md)** for the complete visual record;
- **[Reproducibility Guide](reproducibility.md)** for code and verification.

That separation is deliberate: each page should have one job.

---

**One layer up:** [Research Map](research_map.md)  
**Formal dependency layer:** [Theorem Roadmap](theorem_roadmap.md)  
**Complete theorem archive:** [Detailed Proposition Record](detailed_proposition_record.md)
