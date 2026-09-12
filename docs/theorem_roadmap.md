# Theorem Roadmap

This roadmap records the proved mathematical chain and the open route toward a scientifically meaningful physical-to-experiential bridge. It is organized by **logical dependency**, not by development date.

The current documented theorem frontier is **P84**. The proposition record runs from **P1 through P84 with explicit dependency branches**. P71-P84 return to the core P19 bridge-sufficiency lineage; they do not extend the P61-P70 calibration branch.

![Core theorem roadmap](figures/theorem_roadmap.svg)

## 1. Scientific dependency map

The main dependency structure is:

1. **P1-P10:** invariance, identifiability, recovery, finite-data foundations.
2. **P11-P18:** intervention-resolved, temporal, compositional, and scale-aware physical structure.
3. **P19-P24:** physical sufficiency, residuals, descriptor refinement, and adaptive validity.
4. **P25-P37:** operational quotient and scale-compatibility branch.
5. **P38-P44:** quantum operational sufficiency branch.
6. **P45-P60:** adaptive experiment design, scheduling, stopping, and transition calibration.
7. **P61-P70:** downstream calibration and optimization branch.
8. **P71-P84:** target provenance, target measurement, target-model adequacy, and certified continuous-family separation.

The proposition number is chronology. The dependency arrows, theorem statements, and explicit references determine the scientific structure.

## 2. Foundational branch: P1-P10

P1-P10 establish the representation and inference conditions needed before a physical descriptor can support a serious bridge claim. They cover representation invariance, bridge identifiability, theory equivalence classes, discriminating experiment design, feature sufficiency, canonical signatures, exact and robust signature recovery, categorical sample complexity, and robust experimental design.

The branch begins with [P1](proposition_1_representation_invariance.md) and is indexed proposition-by-proposition in the [Detailed Proposition Record](detailed_proposition_record.md).

## 3. Operational physical branch: P11-P18

P11-P18 replace a purely descriptive physical state with intervention-resolved causal, temporal, compositional, coarse-grained, and scale-aware physical structure. This branch asks what the declared physical description means operationally before any experiential interpretation is attached to it.

Start with [P11](proposition_11_intervention_resolved_causal_structure.md).

## 4. Physical sufficiency branch: P19-P24

[P19](proposition_19_fundamental_physical_sufficiency.md) states the deterministic, stochastic, and differential sufficiency conditions. P20-P24 convert that population-level question into finite-sample, refinement-aware, selection-aware, and repeated-look certificates.

This is the branch from which the target-side P71-P84 methodology descends.

## 5. Operational scale branch: P25-P37

P25-P37 track which causal, intervention, delay, response, and irreducibility structures survive aggregation and quotienting. The purpose is to prevent a bridge claim from silently changing when the physical description is rewritten at another operational scale.

## 6. Quantum branch: P38-P44

P38-P44 ask whether an independently specified target factors through a declared operational quantum description and how finite data, uncertainty regions, tomography, and regularity restrictions affect that test.

This branch does **not** assume that quantum completeness is experiential completeness. See [Quantum Foundations and Bridge Test](quantum_foundations_and_bridge_test.md).

## 7. Adaptive evidence branch: P45-P60

P45-P60 develop sequential witness selection, preparation allocation, stopping rules, service allocation, switching costs, metric perturbation, and transition-calibration machinery. These results concern how evidence is acquired once the scientific witness has been defined.

## 8. Calibration and optimization branch: P61-P70

P61-P70 form a separate downstream resource-allocation branch. They do not define consciousness and do not advance the target-side ontology. Their purpose is to solve and certify finite-resource calibration problems after a valid witness, cost model, and stopping objective have already been declared.

Use the [Calibration and Optimization Frontier](calibration_optimization_frontier_p61_p70.md) for the full P61-P70 chain.

## 9. Target-side methodology and continuous-family frontier: P71-P84

This branch contains the current theorem frontier.

### P71: target provenance must be non-circular

[P71](proposition_71_target_provenance_noncircularity.md) proves that a target constructed as a deterministic function or descriptor-only channel of the tested physical descriptor can satisfy the bridge or screening-off condition by construction. A successful bridge test is therefore meaningful only when target provenance is independently justified.

### P72: target measurement is a separate scientific layer

[P72](proposition_72_target_measurement_channel_robustness.md) separates the latent target from its observed measurement. Under the declared nondifferential channel model, measurement can attenuate or erase a genuine witness but cannot manufacture a positive population residual from a target already screened off by the physical descriptor.

### P73: target-channel reliability can sometimes be identified

[P73](proposition_73_target_channel_identifiability.md) gives an explicit population inversion for a nondegenerate binary latent target observed through three conditionally independent binary views, up to the unavoidable global latent-label swap. It also gives a constructive two-view non-identifiability result.

### P74: finite samples must certify target-channel recovery

[P74](proposition_74_finite_sample_target_channel_recovery.md) propagates one simultaneous eight-cell confidence event through the P73 inversion and introduces a covariance nondegeneracy gate so unstable recovery near the singular set is not reported as reliable.

### P75: identifiability does not imply adequacy

[P75](proposition_75_target_model_adequacy_overidentification.md) separates parameter recovery from model adequacy. Three binary views are generically just-identified, while a fourth view creates six generic overidentifying degrees of freedom, observable moment obligations, and a full-law reconstruction audit.

### P76: finite data can certify tracked model inadequacy

[P76](proposition_76_finite_sample_target_model_adequacy.md) propagates one simultaneous sixteen-cell empirical-law event through denominator-free P75 polynomial constraints. A tracked violation must remain separated from zero after uncertainty is included before the declared model is rejected.

### P77: full-law confidence regions can reject the complete declared model set

[P77](proposition_77_full_law_model_set_separation.md) strengthens selected necessary-constraint testing to separation from the entire declared observed-law model set. For a continuous family, an ordinary best fit is only an upper bound on minimum distance, so certified rejection requires a valid lower bound or equivalent feasibility proof.

### P78: continuous P75 separation can be globally certified

[P78](proposition_78_certified_continuous_model_separation.md) exploits the P75 model's nine-parameter multi-affine structure. Exact rational parameter-box enclosures yield certified global lower bounds on full-law L-infinity distance, explicit admissible parameter points yield upper bounds, and a mesh-width bound controls convergence under refinement.

### P79: the sampling-radius side can also be certified exactly

[P79](proposition_79_certified_sampling_radius.md) replaces an ordinary floating-point sampling-radius evaluation with a one-sided exact-rational upper certificate using rational logarithm bracketing and integer-certified square-root enclosure.

### P80: probability normalization tightens P78

[P80](proposition_80_simplex_coupled_model_separation.md) intersects the exact P78 cell intervals with the probability simplex and computes the resulting interval-simplex L-infinity relaxation distance exactly. The P80 lower bound is never weaker than P78 on the same parameter box.

### P81: projected events retain additional exact box structure

[P81](proposition_81_projection_event_model_separation.md) adds exact parameter-box ranges for every nonempty projected binary event and transfers event mismatch back to a full-law L-infinity lower bound. The combined P81 certificate is never weaker than P80 and can be strictly stronger.

### P82: nested residual events restore more common-parameter structure

[P82](proposition_82_exact_nested_projection_contrast.md) computes exact ranges for 256 residual events formed from nested projected cylinders, directly from the P75 factorization. Its exact witness improves the declared lower certificate from `L81 = 1/16` to `L82 = 1/12`.

### P83: parity observables expose another hidden dependency constraint

[P83](proposition_83_exact_projection_parity.md) adds 22 exact parity observables on two, three, and four views. The branchwise parity probability has a closed multi-affine product form. A strict exact-rational witness has `L82 = 0` but `L83 = 1/16`.

### P84: joint parity contrasts preserve shared P75 parameter compatibility

[P84](proposition_84_exact_joint_projection_parity_contrast.md) asks the compatibility question P83 still relaxes: can two separately feasible parity probabilities be produced by one common P75 response-parameter assignment?

For two parity events with different view sets, P84 computes the signed probability contrast directly. The branchwise contrast is multi-affine in the union of the response coordinates, so its exact parameter-box range is attained at common endpoint vertices. The two latent branches use disjoint response coordinates, and prevalence enters affinely, so the full contrast interval remains exact.

The standard P84 family contains **220 genuinely coupled parity contrasts**. The box certificate is

\[
L_{84}(B)
=
\max\{L_{83}(B),L_{\mathrm{joint-parity}}(B)\}.
\]

It is therefore never weaker than P83. The exact rational strict witness gives

\[
\boxed{L_{83}(B)=0<L_{84}(B)=\frac1{32}.}
\]

For the named witness, the exact model contrast interval is `[0, 1/2]`, the empirical contrast is `-1/4`, the interval gap is `1/4`, and the signed coefficient support contains eight full-law cells. The proof, implementation, tests, and provenance are linked below:

- proof: [P84 exact joint projection-parity contrast](proposition_84_exact_joint_projection_parity_contrast.md)
- provenance: [P84 equation and provenance record](p84_equation_provenance.md)
- implementation: [`joint_projection_parity_contrast_separation.py`](../src/consciousness_bridge/joint_projection_parity_contrast_separation.py)
- tests: [`test_joint_projection_parity_contrast_separation.py`](../tests/test_joint_projection_parity_contrast_separation.py)
- figure: [P84 joint projection-parity contrast certificate](figures/p84_joint_projection_parity_contrast.svg)

P84 preserves the P78 global upper-certificate logic and the P79 finite-data rejection handoff. It claims no new convergence-rate theorem.

## 10. Current frontier chain

The target-side certification chain is now:

\[
\text{P71 provenance}
\to
\text{P72 measurement}
\to
\text{P73 identifiability}
\to
\text{P74 finite recovery}
\to
\text{P75 adequacy}
\to
\text{P76 finite inadequacy rejection}
\to
\text{P77 full-law separation}
\to
\text{P78 certified continuous distance}
\to
\text{P79 certified sampling radius}
\to
\text{P80 simplex coupling}
\to
\text{P81 projection events}
\to
\text{P82 nested residuals}
\to
\text{P83 parity events}
\to
\text{P84 joint parity contrasts}.
\]

The chain establishes progressively stronger obligations and model-distance certificates. It does **not** establish a physical-to-experiential bridge.

## 11. What the roadmap means scientifically

A theorem can be mathematically correct while a stronger interpretation remains unjustified. The roadmap therefore distinguishes:

- mathematical consequences under declared assumptions;
- executable computational certificates;
- finite-data rejection statements;
- empirical adequacy of the declared measurement model;
- the still-open interpretation linking physical description to experience.

A failed descriptor or rejected latent model does not prove that consciousness is outside physics. The physical description or measurement model may simply be incomplete or wrong. Conversely, non-rejection does not validate the model or identify its latent state with consciousness.

## 12. Audit and reproduction

For a full chronological record, use the [Detailed Proposition Record](detailed_proposition_record.md). For equation-level classification, use the [Equation and Citation Map](equation_and_citation_map.md) and proposition-specific provenance records. For executable validation, use the [Reproducibility Guide](reproducibility.md).

The current documented theorem frontier is **P84**.

**Current frontier:** **P84 - Exact Joint Projection-Parity Contrast Certificate for Continuous P75 Separation.**

**Current frontier provenance:** [P84 equation and provenance record](p84_equation_provenance.md).

The physical-to-experiential bridge remains open.