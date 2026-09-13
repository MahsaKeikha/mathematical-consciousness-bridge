# Research Traceability Index

This page is the **find-anything-in-two-clicks** index for the Mathematical Consciousness Bridge.

Use it when you know what question you want to audit but do not want to search folders manually. The landing pages stay intentionally simple; this page connects the scientific story to the detailed proof, provenance, implementation, tests, figures, and reproducibility record.

> **Navigation rule:** start from a scientific question, not from a file name.

## Quick routes

| If you want to know... | Start here |
| --- | --- |
| What is the overall research question? | [Start Here](../START_HERE.md) |
| How is the program structured scientifically? | [Research Architecture](research_architecture.md) |
| How do all propositions depend on one another? | [Theorem Roadmap](theorem_roadmap.md) |
| What does every proposition claim? | [Detailed Proposition Record](detailed_proposition_record.md) |
| Where did an equation or method come from? | [Equation and Citation Map](equation_and_citation_map.md) |
| What would falsify a bridge claim? | [Falsification Program](falsification_program.md) |
| How do I reproduce the computations? | [Reproducibility Guide](reproducibility.md) |
| Where are all the figures? | [Figure Catalog](figure_catalog.md) |
| What terminology does the repository use? | [Glossary](glossary.md) |

---

## The research program by scientific role

The proposition numbers record development history. They are not intended as the first reading path.

| Scientific layer | Results | Core question | Best entry point |
| --- | --- | --- | --- |
| Foundations | P1-P10 | What is invariant, identifiable, and experimentally recoverable? | [Theorem Roadmap](theorem_roadmap.md) |
| Operational physical structure | P11-P18 | What physical structure survives intervention, time, composition, and scale? | [P11](proposition_11_intervention_resolved_causal_structure.md) |
| Physical sufficiency | P19-P24 | Does a declared physical descriptor preserve every distinction in an independent target? | [P19](proposition_19_fundamental_physical_sufficiency.md) |
| Scale compatibility | P25-P37 | Which physical distinctions survive aggregation and quotienting? | [Theorem Roadmap](theorem_roadmap.md) |
| Quantum operational branch | P38-P44 | How can the same sufficiency logic be posed for declared quantum descriptions? | [Quantum Foundations and Bridge Test](quantum_foundations_and_bridge_test.md) |
| Experiment design | P45-P60 | How can evidence be gathered adaptively without losing validity? | [Theorem Roadmap](theorem_roadmap.md) |
| Calibration and optimization | P61-P70 | How can downstream finite resources be allocated once the scientific witness is defined? | [Calibration and Optimization Frontier](calibration_optimization_frontier_p61_p70.md) |
| Target integrity and measurement | P71-P74 | Is the target independent, measurable, identifiable, and recoverable from finite data? | [P71](proposition_71_target_provenance_noncircularity.md) |
| Model adequacy and exact separation | P75-P87 | Does the declared target-measurement model actually reproduce the observed law? | [P75](proposition_75_target_model_adequacy_overidentification.md) |
| Held-out validation | P88 | Can a discovery-selected incompatibility survive independent validation? | [P88](proposition_88_heldout_selected_parity_functional_certification.md) |

---

## Target-side research frontier: P71-P88

This is the most direct path into the current research frontier.

### Target integrity and measurement: P71-P74

**P71 - Is the target circular?**  
[Theorem](proposition_71_target_provenance_noncircularity.md)  
Prevents a target constructed from the tested physical descriptor from being mistaken for independent evidence.

**P72 - What does measurement noise do to the target?**  
[Theorem](proposition_72_target_measurement_channel_robustness.md) · [Equation provenance](p72_equation_provenance.md)  
Separates the latent target from its observation channel and quantifies attenuation, erasure, and contamination under the declared model.

**P73 - Can the target-measurement channels be identified?**  
[Theorem](proposition_73_target_channel_identifiability.md) · [Equation provenance](p73_equation_provenance.md)  
Shows population identifiability for a restricted three-view binary latent model under explicit nondegeneracy, up to the unavoidable latent-label swap.

**P74 - Can that recovery be trusted with finite data?**  
[Theorem](proposition_74_finite_sample_target_channel_recovery.md) · [Equation provenance](p74_equation_provenance.md)  
Adds simultaneous finite-sample uncertainty and refuses unstable inversion near the singular boundary.

### Model adequacy and exact separation: P75-P87

**P75 - Does identifiability imply the model is correct?**  
[Theorem](proposition_75_target_model_adequacy_overidentification.md) · [Equation provenance](p75_equation_provenance.md)  
No. A fourth binary view creates overidentifying restrictions and a full-law reconstruction audit.

**P76 - Is an apparent model failure larger than sampling noise?**  
[Theorem](proposition_76_finite_sample_target_model_adequacy.md)  
Turns population adequacy restrictions into finite-data rejection certificates.

**P77 - Is the full empirical law separated from the full declared model set?**  
[Theorem](proposition_77_full_law_model_set_separation.md)  
Defines the stronger full-law finite-sample separation problem.

**P78 - Can separation from a continuous model family be certified globally?**  
[Theorem](proposition_78_certified_continuous_model_separation.md) · [Equation provenance](p78_equation_provenance.md)  
Uses exact-rational branch-and-bound to obtain a global lower bound rather than relying on one numerical best fit.

**P79 - Can the sampling radius itself be upper-certified in the correct numerical direction?**  
[Theorem](proposition_79_certified_sampling_radius.md) · [Equation provenance](p79_equation_provenance.md) · [Figure](figures/p79_certified_sampling_radius.svg)  
Provides an exact-rational upper enclosure for the Hoeffding-style sampling radius.

**P80 - Can probability normalization tighten the continuous-family bound?**  
[Theorem](proposition_80_simplex_coupled_model_separation.md) · [Equation provenance](p80_equation_provenance.md)  
Adds the probability-simplex constraint inside the box relaxation.

**P81 - Can projected events reveal incompatibility hidden at the cellwise level?**  
[Theorem](proposition_81_projection_event_model_separation.md) · [Equation provenance](p81_equation_provenance.md) · [Implementation](../src/consciousness_bridge/projection_event_model_separation.py) · [Tests](../tests/test_projection_event_model_separation.py)  
Adds exact event-probability ranges and transfers event mismatch back to full-law distance.

**P82 - Can nested event contrasts retain more shared-parameter structure?**  
[Theorem](proposition_82_exact_nested_projection_contrast.md)  
Adds exact nested residual-event contrasts beyond separate projected events.

**P83 - Can parity expose a dependency constraint missed by previous event families?**  
[Theorem](proposition_83_exact_projection_parity.md) · [Equation provenance](p83_equation_provenance.md) · [Figure](figures/p83_exact_projection_parity.svg)  
Adds exact parity observables with multi-affine box extrema.

**P84 - Are two separately compatible parity events jointly realizable by one parameter assignment?**  
[Theorem](proposition_84_exact_projection_parity_contrast.md) · [Equation provenance](p84_equation_provenance.md) · [Figure](figures/p84_exact_joint_projection_parity_contrast.svg)  
Adds exact pairwise shared-parameter parity contrasts.

**P85 - Can a three-event functional reveal incompatibility beyond every P84 pair?**  
[Theorem](proposition_85_exact_triple_projection_parity_functional.md) · [Equation provenance](p85_equation_provenance.md) · [Figure](figures/p85_exact_triple_projection_parity_functional.svg)  
Audits 660 sign-normalized three-event functionals.

**P86 - Does the smallest nonuniform four-event weighting add power?**  
[Theorem](proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md) · [Equation provenance](p86_equation_provenance.md) · [Figure](figures/p86_exact_minimally_weighted_quad_projection_parity.svg)  
Adds the primitive coefficient-magnitude pattern `{1,1,1,2}`.

**P87 - What happens when the bounded primitive four-event family is completed?**  
[Theorem](proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md) · [Equation provenance](p87_equation_provenance.md) · [Implementation](../src/consciousness_bridge/bounded_primitive_quad_projection_parity_functional_separation.py) · [Tests](../tests/test_bounded_primitive_quad_projection_parity_functional_separation.py) · [Figure](figures/p87_exact_bounded_primitive_quad_projection_parity.svg)  
Completes all nonzero primitive four-event coefficient vectors with `|c_i| <= 2`, yielding 39,600 exact functionals.

### Held-out validation: P88

**P88 - Can a discovery-selected P87 witness be validated on fresh data without pretending selection never occurred?**

- [Theorem](proposition_88_heldout_selected_parity_functional_certification.md)
- [Equation provenance](p88_equation_provenance.md)
- [Implementation](../src/consciousness_bridge/heldout_selected_parity_functional_certification.py)
- [Regression tests](../tests/test_heldout_selected_parity_functional_certification.py)
- [Frontier figure](figures/p88_heldout_selected_parity_functional_certification.svg)
- [Reproducibility guide](reproducibility.md)

The P88 result is **box-specific** unless the tested box covers the full admissible P75 parameter domain or a separately valid covering argument is supplied. Genuine discovery/validation independence is part of the theorem conditions.

---

## How to audit any mature result

For a technical result, follow the same chain every time:

**Question → theorem → equation provenance → implementation → tests → figure → reproducibility → scientific boundary**

This separation is intentional. It lets a reader distinguish mathematical proof, executable realization, regression evidence, numerical visualization, and scientific interpretation instead of treating them as one undifferentiated claim.

---

## Visual exploration

Use the [Figure Catalog](figure_catalog.md) when you want to understand the research visually before reading proofs. The catalog is the preferred route for discovering figures; proposition pages remain the authoritative source for theorem assumptions and conclusions.

The current frontier visual is [P88 held-out selected parity functional certification](figures/p88_heldout_selected_parity_functional_certification.svg).

---

## Complete records

For full-depth review, these pages intentionally contain more information than the landing pages:

- [Theorem Roadmap](theorem_roadmap.md): dependency structure for P1-P88.
- [Detailed Proposition Record](detailed_proposition_record.md): proposition-by-proposition scientific record.
- [Equation and Citation Map](equation_and_citation_map.md): equation provenance and literature lineage.
- [Research Navigation](research_navigation.md): legacy comprehensive navigation and complete proposition index.
- [Claim Source Matrix](claim_source_matrix.md): source classification for public scientific claims.
- [Reference Audit](reference_audit.md): audited literature references.

These are reference pages, not required first reads.

---

## Scientific boundary

The repository develops methods for making bridge claims more precise, more falsifiable, and more auditable. It does **not** establish that consciousness is a new physical dimension, that it is outside physics, that a statistical latent variable is consciousness, or that the physical-to-experiential bridge has already been solved.
