# Theorem Roadmap

This roadmap records the proved mathematical chain and the open route toward a scientifically meaningful physical-to-experiential bridge. It is organized by **logical dependency**, not by development date.

The current documented theorem frontier is **P71**. The proposition record runs from **P1 through P71 with explicit dependency branches**. P71 returns to the core P19 bridge-sufficiency lineage; it does not extend the P61-P70 calibration branch.

![Core theorem roadmap](figures/theorem_roadmap.svg)

---

# 1. Scientific dependency map

The main logical structure is

\[
\boxed{
\begin{aligned}
&\text{P1-P10: invariance, identifiability, recovery, robust design}\\
&\Downarrow\\
&\text{P11-P18: intervention, time, composition, and scale}\\
&\Downarrow\\
&\text{P19: exact, stochastic, and differential physical sufficiency}\\
&\Downarrow\\
&\text{P20-P24: finite-data, refinement, selection, and anytime validity}\\
&\Downarrow\\
&\text{P71: target-provenance non-circularity}.
\end{aligned}
}
\]

Three major supporting branches attach to that core:

\[
\boxed{
\text{P25-P37: operational scale compatibility}
}
\]

\[
\boxed{
\text{P38-P44: quantum operational sufficiency and finite-data bridge tests}
}
\]

\[
\boxed{
\text{P45-P60: adaptive experiment design and scheduling}
\longrightarrow
\text{P61-P70: calibration and optimization}.
}
\]

The branches answer different questions. A later proposition number does not imply that its result is ontologically deeper. In particular, P61-P70 improves how a declared experiment is executed and certified; P71 addresses whether the target used by the bridge test was constructed in a scientifically non-circular way.

---

# 2. Complete proposition index

| Proposition | Mathematical role | Scientific role | Status |
| --- | --- | --- | --- |
| [P1](proposition_1_representation_invariance.md) | quotient factorization | representation-independent bridge objects | proved |
| [P2](proposition_2_bridge_identifiability.md) | total-variation discriminability | exact theory non-identifiability criterion | proved |
| [P3](proposition_3_bridge_equivalence_classes.md) | quotient by observable fingerprints | identifies what an experiment class can resolve | proved |
| [P4](proposition_4_discriminating_experiment_design.md) | maximin and set-cover design | adversarial theory-discriminating experiments | proved |
| [P5](proposition_5_feature_sufficiency.md) | bridge factorization through physical features | exact sufficiency and counterexample criterion | proved |
| [P6](proposition_6_canonical_bridge_signature.md) | canonical bridge quotient | defines the exact completeness target | proved |
| [P7](proposition_7_experimental_signature_recovery.md) | observable-fingerprint factorization | exact recoverability and no-go condition | proved |
| [P8](proposition_8_robust_signature_recovery.md) | deterministic perturbation bound | finite-error signature recovery | proved |
| [P9](proposition_9_categorical_sample_complexity.md) | concentration plus union control | explicit finite trial requirement | proved |
| [P10](proposition_10_robust_experiment_design.md) | robust protocol optimization | separates discrimination from nuisance variation | proved |
| [P11](proposition_11_intervention_resolved_causal_structure.md) | structured intervention-response object | first structured candidate physical signature | proved construction and candidate |
| [P12](proposition_12_component_insufficiency.md) | projection-collision theorem | one-component and scalar reductions lose information | proved minimality and no-go |
| [P13](proposition_13_pairwise_component_irredundancy.md) | pairwise projection collisions | every major component is irredundant on the audit domain | proved irredundancy |
| [P14](proposition_14_temporal_continuation.md) | quotient metric and path variation | representation-invariant temporal continuation | proved temporal theorem |
| [P15](proposition_15_finite_sample_temporal_certification.md) | perturbation bounds | finite-error certification of temporal change | proved certification theorem |
| [P16](proposition_16_independent_composition_and_coupling.md) | product-response composition | distinguishes independent coexistence from coupling | proved composition theorem |
| [P17](proposition_17_coarse_graining_and_refinement.md) | deterministic pushforward and data processing | information loss under coarse-graining | proved scale-loss theorem |
| [P18](proposition_18_scale_sufficiency_certification.md) | approximate reconstruction | quantitative scale-sufficiency certificate | proved scale theorem |
| [P19](proposition_19_fundamental_physical_sufficiency.md) | fiber factorization, conditional mutual information, rank obstruction | tests whether an independently declared target is fixed by the physical descriptor | proved physical-sufficiency theorem |
| [P20](proposition_20_finite_sample_residual_certification.md) | finite-alphabet concentration and entropy continuity | finite-sample confidence interval for the P19 residual | proved finite-sample theorem |
| [P21](proposition_21_descriptor_refinement_residual_persistence.md) | nested descriptor factorization and CMI chain rule | omitted-physics audit and residual-persistence trajectory | proved refinement theorem |
| [P22](proposition_22_simultaneous_refinement_chain_certification.md) | shared confidence event | simultaneous finite-data confidence family for P21 | proved simultaneous theorem |
| [P23](proposition_23_adaptive_descriptor_selection_certification.md) | post-selection control | adaptive fixed-sample physical refinement with valid coverage | proved post-selection theorem |
| [P24](proposition_24_anytime_adaptive_refinement_certification.md) | time-uniform error control | repeated-look refinement and finite stopping-time validity | proved anytime-valid theorem |
| [P25](proposition_25_directed_influence_scale_certification.md) | influence plus reconstruction distortion | directed-influence preservation across scale | proved physical scale theorem |
| [P26](proposition_26_partition_irreducibility_scale_certification.md) | partition productization plus reconstruction | irreducibility preservation across scale | proved physical scale theorem |
| [P27](proposition_27_partition_lattice_node_aggregation.md) | node quotient and lattice transport | exact partition semantics under node aggregation | proved physical scale theorem |
| [P28](proposition_28_intervention_node_aggregation_compatibility.md) | source-incidence descent | intervention compatibility across aggregate nodes | proved physical scale theorem |
| [P29](proposition_29_response_geometry_node_aggregation.md) | response geometry transport | indexed response-pseudometric preservation | proved physical scale theorem |
| [P30](proposition_30_full_p11_scale_compatibility.md) | scale assembly | simultaneous declared P11 structure transport | proved assembly theorem |
| [P31](proposition_31_intervention_quotient_compatibility.md) | intervention quotient factorization | intervention-set change with ambiguity control | proved operational quotient theorem |
| [P32](proposition_32_delay_quotient_compatibility.md) | delay-fiber factorization | temporal quotient criterion and ambiguity budget | proved operational quotient theorem |
| [P33](proposition_33_joint_operational_quotient.md) | product quotient | joint intervention-delay descent | proved joint quotient theorem |
| [P34](proposition_34_joint_p11_operational_scale.md) | complete scale assembly | full P11 semantics under one declaration | proved assembly theorem |
| [P35](proposition_35_approximate_directed_influence_operational_quotient.md) | metric perturbation | approximate influence and edge stability | proved perturbation theorem |
| [P36](proposition_36_partition_irreducibility_operational_quotient.md) | marginal contraction and product telescoping | partition-reference stability | proved perturbation theorem |
| [P37](proposition_37_complete_approximate_p11_operational_scale.md) | max-norm assembly | complete approximate P11 scale certificate | proved complete scale theorem |
| [P38](proposition_38_quantum_operational_sufficiency.md) | factorization through density-operator fibers | exact quantum descriptor sufficiency and non-factorization witness | proved quantum sufficiency theorem |
| [P39](proposition_39_finite_data_quantum_nonfactorization.md) | tomography model-set coverage plus target confidence | finite-data quantum non-factorization test | proved finite-data model-set theorem |
| [P40](proposition_40_continuous_quantum_region_regularity.md) | injective-image factorization and bridge moduli | unrestricted-bridge no-go and regularity obstruction | proved no-go plus regularity theorem |
| [P41](proposition_41_trace_ball_quantum_envelope.md) | trace-distance uncertainty envelope | end-to-end regularity obstruction | proved confidence-envelope theorem |
| [P42](proposition_42_quantum_regular_bridge_sample_complexity.md) | tomography concentration plus reconstruction stability | explicit samples for a positive regularity obstruction | proved finite-sample design theorem |
| [P43](proposition_43_optimal_quantum_target_allocation.md) | strict convexity and weighted allocation | minimum-cost quantum-target uncertainty split | proved resource-allocation theorem |
| [P44](proposition_44_pair_adaptive_sample_allocation.md) | simultaneous finite-family coverage | valid data-dependent witness selection | proved post-selection theorem |
| [P45](proposition_45_shared_preparation_graph_allocation.md) | shared-vertex convex allocation | preparation-level resource design for overlapping witnesses | proved resource-allocation theorem |
| [P46](proposition_46_budget_constrained_witness_graph.md) | combinatorial selection and relaxation | hard-budget preparation selection with certified gap | proved combinatorial design theorem |
| [P47](proposition_47_anytime_sequential_witness_graph.md) | time-uniform graph confidence | adaptive sampling, pruning, witness selection, and stopping | proved sequential-design theorem |
| [P48](proposition_48_gap_dependent_stopping_complexity.md) | confidence-sequence inversion | gap-dependent stopping complexity | proved stopping-complexity theorem |
| [P49](proposition_49_dyadic_stopping_overhead.md) | dyadic checkpoint geometry | logarithmic certification schedule | proved scheduling theorem |
| [P50](proposition_50_bounded_starvation_asynchronous_sampling.md) | finite-window fairness | finite global stopping under asynchronous sampling | proved asynchronous theorem |
| [P51](proposition_51_heterogeneous_service_rate_stopping.md) | preparation-specific quotas | heterogeneous global stopping bounds | proved scheduling theorem |
| [P52](proposition_52_capacity_optimal_service_allocation.md) | capacity lower bound and minimax allocation | capacity-optimal service shares | proved scheduling theorem |
| [P53](proposition_53_residual_demand_reoptimization.md) | residual max-envelope demands | dynamic capacity reoptimization | proved scheduling theorem |
| [P54](proposition_54_metric_switching_cost_residual_scheduling.md) | metric shortcutting and Held-Karp recurrence | exact residual execution cost with switching overhead | proved scheduling theorem |
| [P55](proposition_55_pruning_aware_switching_monotonicity.md) | support-deletion shortcutting | pruning-aware route and acquisition release | proved scheduling theorem |
| [P56](proposition_56_moving_start_metric_reoptimization_stability.md) | first-edge perturbation | sharp moving-start stability | proved perturbation theorem |
| [P57](proposition_57_switching_metric_perturbation.md) | uniform finite-metric perturbation | switching-metric reoptimization stability | proved perturbation theorem |
| [P58](proposition_58_finite_data_metric_uncertainty.md) | transition confidence intervals and route envelopes | finite-data switching-metric uncertainty | proved finite-data theorem |
| [P59](proposition_59_optimal_transition_calibration.md) | strict convexity and KKT allocation | optimal transition-calibration allocation | proved resource-allocation theorem |
| [P60](proposition_60_integer_transition_calibration.md) | reserved-budget ceiling construction | whole-measurement calibration with overhead bound | proved integer-allocation theorem |
| [P61](proposition_61_exact_integer_transition_calibration.md) | discrete diminishing returns | exact equal-cost whole-measurement allocation | proved exact discrete theorem |
| [P62](proposition_62_heterogeneous_cost_transition_calibration.md) | unequal-cost KKT allocation | heterogeneous-cost continuous calibration | proved continuous theorem |
| [P63](proposition_63_exact_heterogeneous_integer_calibration.md) | Bellman recursion with gcd compression | exact unequal-cost integer calibration | proved pseudo-polynomial theorem |
| [P64](proposition_64_fast_heterogeneous_integer_approximation.md) | floor approximation | scalable heterogeneous integer certificate | proved approximation theorem |
| [P65](proposition_65_lower_bounded_heterogeneous_calibration.md) | active-set water filling | lower-bounded heterogeneous calibration | proved continuous theorem plus approximation certificate |
| [P66](proposition_66_residual_exact_calibration_augmentation.md) | bounded residual dynamic program | exact floor-dominating augmentation | proved restricted-exact theorem |
| [P67](proposition_67_global_integer_optimality_certificate.md) | common multiplier and marginal intervals | unrestricted integer global-optimality certificate | proved sufficient certificate theorem |
| [P68](proposition_68_lagrangian_optimality_gap.md) | Lagrangian weak duality | quantitative candidate-to-optimum upper certificate | proved dual lower-bound theorem |
| [P69](proposition_69_dual_optimal_multiplier.md) | concave dual and supergradient bracket | certified strongest P68 dual value | proved dual-optimization theorem |
| [P70](proposition_70_primal_dual_gap_decomposition.md) | exact primal-dual diagnostic decomposition | attributes certificate gap to edge regret and unused budget | proved primal-dual diagnostic decomposition |
| [P71](proposition_71_target_provenance_noncircularity.md) | deterministic factorization, Markov screening-off, and provenance non-identifiability | prevents descriptor-derived targets from being mistaken for independent bridge evidence | proved target-provenance non-circularity theorem |

---

# 3. Foundations and identifiability: P1-P10

The first ten propositions establish the requirements that precede any consciousness interpretation: representation invariance, theory distinguishability, experimental equivalence classes, discriminating protocol design, feature sufficiency, canonical signatures, recoverability, robust recovery, finite sampling, and nuisance-aware experimental design.

Their role is methodological. They make it possible to state what an experiment can identify before asking what the identified object means experientially.

---

# 4. Structured physical candidate: P11-P18

P11 defines an intervention-resolved physical candidate built from response geometry, directed intervention influence, and partition irreducibility. P12 and P13 prove constructive insufficiency results for compressed projections. P14-P15 add representation-invariant temporal continuation and uncertainty propagation. P16 handles independent composition and coupling. P17-P18 quantify coarse-graining loss and reconstruction-controlled scale sufficiency.

A representative scale certificate is

\[
\boxed{
0\le
\|P-Q\|_{\mathrm{TV}}
-
\|C_{\#}P-C_{\#}Q\|_{\mathrm{TV}}
\le2\rho_{\mathcal F}.
}
\]

This branch builds physical structure. It does not define consciousness.

---

# 5. Core bridge sufficiency: P19

P19 asks whether an independently specified target descriptor \(E\) is determined by the declared physical descriptor \(T\).

The deterministic criterion is

\[
\boxed{
E=B_T\circ T
\iff
T(\omega)=T(\omega')\Rightarrow E(\omega)=E(\omega').
}
\]

The stochastic residual is

\[
\boxed{
R_{\mathrm{stoch}}(T)=I(E;\Omega\mid T).
}
\]

For differentiable local coordinates, smooth factorization requires

\[
\boxed{
\operatorname{rank}D(T,E)=\operatorname{rank}DT.
}
\]

A failure of these conditions challenges the declared descriptor. It does not, without further controls, establish a nonphysical ontology.

---

# 6. Finite and adaptive residual certification: P20-P24

P20 propagates finite-sample uncertainty into the P19 conditional-information residual. P21 decomposes residual reduction across nested physical refinements. P22 supplies simultaneous confidence over a refinement chain. P23 permits fixed-sample data-dependent descriptor selection. P24 makes repeated looks and finite stopping times valid under its declared anytime construction.

These results control inference after the physical descriptor and target have been declared. They do not determine whether the target itself was constructed non-circularly.

---

# 7. Target-provenance non-circularity: P71

P71 closes that logical gap.

If the target is constructed as

\[
\boxed{E_h=h(T),}
\]

then exact factorization is automatic and

\[
\boxed{I(E_h;\Omega\mid T)=0.}
\]

If a stochastic target is generated by a descriptor-only channel

\[
P(\omega,t,e)=P(\omega,t)K(e\mid t),
\]

then

\[
\boxed{E\perp\!\!\!\perp\Omega\mid T}
\]

by construction.

P71 further proves that a fixed learned target \(\widehat E=h_D(T)\) remains descriptor-derived conditional on the training artifact, and that an observed joint law with zero conditional residual can itself be represented using the channel \(K(e\mid t)=P(E=e\mid T=t)\). Therefore target provenance cannot be recovered from the observed joint law alone.

![P71 target-provenance non-circularity](figures/p71_target_provenance_noncircularity.svg)

**P71 scientific meaning:** successful factorization has evidential content only when the target-construction protocol did not already impose the factorization. This is a necessary non-circularity condition, not a solution to the measurement problem of consciousness.

Direct proof: [Proposition 71](proposition_71_target_provenance_noncircularity.md). Implementation: [target_provenance_noncircularity.py](../src/consciousness_bridge/target_provenance_noncircularity.py). Tests: [test_target_provenance_noncircularity.py](../tests/test_target_provenance_noncircularity.py).

---

# 8. Operational scale branch: P25-P37

P25-P37 extend the structured P11 candidate through observation scale, node aggregation, intervention quotients, delay quotients, and approximate joint operational quotients. The branch distinguishes semantic compatibility from numerical closeness: zero numerical reconstruction error cannot repair an invalid quotient of interventions, nodes, or partitions.

Key branch figure links:

- [P30-P37 operational scale map](../figures/p30_p37_operational_scale_map.svg)

---

# 9. Quantum operational sufficiency: P38-P44

P38 asks whether a declared operationally complete quantum descriptor is sufficient for an independently declared target. P39-P44 add finite tomography, continuous-region regularity, trace-distance envelopes, sample-complexity requirements, optimal quantum-target resource allocation, and simultaneous candidate-pair validity.

This branch does not assume that consciousness is quantum and does not infer that quantum mechanics is incomplete.

The theorem figures are:

- [P38 quantum operational sufficiency](figures/p38_quantum_operational_sufficiency.svg)
- [P39 finite-data quantum non-factorization](figures/p39_finite_data_quantum_nonfactorization.svg)
- [P40 continuous quantum-region regularity](figures/p40_continuous_quantum_region_regularity.svg)
- [P41 trace-ball quantum envelope](figures/p41_trace_ball_quantum_envelope.svg)
- [P42 quantum regular-bridge sample complexity](figures/p42_quantum_regular_bridge_sample_complexity.svg)
- [P43 optimal quantum-target allocation](figures/p43_optimal_quantum_target_allocation.svg)
- [P44 pair-adaptive sample allocation](figures/p44_pair_adaptive_sample_allocation.svg)

---

# 10. Adaptive experiment-design branch: P45-P60

P45-P60 address how evidence can be gathered after a candidate witness family has been declared. The branch covers shared preparation graphs, hard-budget selection, anytime-valid sequential sampling, gap-dependent stopping, asynchronous fairness, heterogeneous service rates, capacity allocation, pruning-aware reoptimization, switching costs, metric uncertainty, and transition calibration.

The corresponding theorem figures are:

- [P45 shared-preparation graph allocation](figures/p45_shared_preparation_graph_allocation.svg)
- [P46 budget-constrained witness graph](figures/p46_budget_constrained_witness_graph.svg)
- [P47 sequential graph refinement](figures/p47_sequential_graph_refinement.svg)
- [P48 gap-dependent stopping complexity](figures/p48_gap_dependent_stopping_complexity.svg)
- [P49 dyadic stopping overhead](figures/p49_dyadic_stopping_overhead.svg)
- [P50 bounded-starvation asynchronous sampling](figures/p50_bounded_starvation_asynchronous_sampling.svg)
- [P51 heterogeneous service-rate stopping](figures/p51_heterogeneous_service_rate_stopping.svg)
- [P52 capacity-optimal service allocation](figures/p52_capacity_optimal_service_allocation.svg)
- [P53 residual-demand reoptimization](figures/p53_residual_demand_reoptimization.svg)
- [P54 metric switching-cost residual scheduling](figures/p54_metric_switching_cost_residual_scheduling.svg)
- [P55 pruning-aware switching monotonicity](figures/p55_pruning_aware_switching_monotonicity.svg)
- [P56 moving-start reoptimization stability](figures/p56_moving_start_metric_reoptimization_stability.svg)
- [P57 switching-metric perturbation](figures/p57_switching_metric_perturbation.svg)
- [P58 finite-data metric uncertainty](figures/p58_finite_data_metric_uncertainty.svg)
- [P59 optimal transition calibration](figures/p59_optimal_transition_calibration.svg)
- [P60 integer transition calibration](figures/p60_integer_transition_calibration.svg)

---

# 11. Calibration and optimization branch: P61-P70

P61-P70 is a downstream implementation branch. It assumes that the scientific witness, uncertainty model, and experimental objective have already been declared. The branch improves resource allocation and certification; it does not define consciousness or strengthen the ontology of the earlier bridge claim.

The complete derivations are kept in the dedicated [Calibration and Optimization Frontier](calibration_optimization_frontier_p61_p70.md).

The theorem figures are:

- [P61 exact integer transition calibration](figures/p61_exact_integer_transition_calibration.svg)
- [P62 heterogeneous-cost transition calibration](figures/p62_heterogeneous_cost_transition_calibration.svg)
- [P63 exact heterogeneous-cost integer calibration](figures/p63_exact_heterogeneous_integer_calibration.svg)
- [P64 fast heterogeneous integer approximation](figures/p64_fast_heterogeneous_integer_approximation.svg)
- [P65 lower-bounded heterogeneous calibration](figures/p65_lower_bounded_heterogeneous_calibration.svg)
- [P66 residual-exact calibration augmentation](figures/p66_residual_exact_calibration_augmentation.svg)
- [P67 global integer optimality certificate](figures/p67_global_integer_optimality_certificate.svg)
- [P68 Lagrangian optimality gap](figures/p68_lagrangian_optimality_gap.svg)
- [P69 dual-optimal multiplier](figures/p69_dual_optimal_multiplier.svg)
- [P70 primal-dual gap decomposition](figures/p70_primal_dual_gap_decomposition.svg)

P70 proves the exact identity

\[
\boxed{
U(k)-q(\lambda)
=
\sum_e r_e(k_e;\lambda)
+\lambda\left(B-\sum_e c_ek_e\right),
}
\]

which is a diagnostic decomposition of the declared integer calibration certificate.

---

# 12. What P71 changes in the bridge program

Before P71, P19 required an independently defined target as a scientific premise. P71 turns one major failure mode of that premise into an explicit theorem.

The resulting logic is

\[
\boxed{
\begin{array}{c}
\text{declare physical descriptor }T\\
\Downarrow\\
\text{declare target protocol independently of the tested factorization}\\
\Downarrow\\
\text{apply P19 exact or stochastic sufficiency test}\\
\Downarrow\\
\text{apply P20-P24 finite/adaptive certification as needed}\\
\Downarrow\\
\text{attempt falsification across interventions, time, scale, and theory families.}
\end{array}
}
\]

A zero residual is not enough to establish target provenance. A positive residual is not enough to establish nonphysicality. Both conclusions require the scientific provenance and physical-completeness assumptions to be audited separately.

---

# 13. Current frontier after P71

P71 closes the **descriptor-derived target vacuity** failure mode. It does not yet define a scientifically adequate experiential space. The next structural problems are therefore:

1. formalize target-side experiential equivalence classes from observations whose construction does not use the tested physical descriptor;
2. define target reliability and inter-observer or repeated-measurement consistency without collapsing the target into a physical proxy by definition;
3. distinguish target measurement error from genuine within-fiber experiential variation;
4. extend P20-P24 to continuous, dependent, hidden-state, noisy-descriptor, and learned-descriptor settings;
5. model genuine physical split and merge dynamics where state variables and intervention channels change;
6. formalize the moving world-tube and causal-structure interface;
7. normalize temporal geometry under irregular observation time;
8. run cross-theory adversarial experiments on shared perturbational protocol families;
9. search biological and non-biological counterexamples with preregistered target provenance;
10. attempt a bridge theorem only after physical completeness, target validity, finite-data control, scale compatibility, and falsification have been jointly addressed.

The next core theorem should therefore address **target-side measurement reliability and noise** rather than return immediately to calibration optimization.

---

# 14. Scientific boundary

The roadmap contains proved mathematical results, implementations, numerical checks, and open scientific targets. None of P1-P71 establishes that consciousness is a scalar, a state of matter, an additional spacetime coordinate, intrinsically quantum, or nonphysical.

The central physical-to-experiential bridge remains open. The purpose of the theorem chain is to make any future bridge claim more explicit, falsifiable, and difficult to obtain by circular definition or uncontrolled inference.
