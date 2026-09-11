# Theorem Roadmap

This roadmap records the proved mathematical chain and the open route toward a scientifically meaningful physical-to-experiential bridge. It is organized by **logical dependency**, not by development date.

The current documented theorem frontier is **P73**. The proposition record runs from **P1 through P73 with explicit dependency branches**. P71, P72, and P73 return to the core P19 bridge-sufficiency lineage; they do not extend the P61-P70 calibration branch.

![Core theorem roadmap](figures/theorem_roadmap.svg)

## 1. Scientific dependency map

\[
\boxed{
\begin{aligned}
&\text{P1-P10: invariance, identifiability, recovery, finite-data foundations}\\
&\Downarrow\\
&\text{P11-P18: intervention-resolved, temporal, compositional, scale-aware physics}\\
&\Downarrow\\
&\text{P19-P24: physical sufficiency, residuals, refinement, adaptive validity}\\
&\Downarrow\\
&\text{P71: target provenance must not impose the bridge}\\
&\Downarrow\\
&\text{P72: noisy target observation must preserve the claimed target distinction}\\
&\Downarrow\\
&\text{P73: repeated target views can identify channel stability under a declared model}
\end{aligned}
}
\]

Separate but connected branches refine the physical representation and experimental machinery:

\[
\boxed{
\begin{aligned}
&\text{P25-P37: operational scale compatibility},\\
&\text{P38-P44: quantum operational sufficiency and regularity-aware tests},\\
&\text{P45-P60: adaptive evidence acquisition, scheduling, and calibration setup},\\
&\text{P61-P70: downstream calibration and integer optimization}.
\end{aligned}
}
\]

The proposition number records development order. It does not imply that P73 depends on P70. P72 depends scientifically on P17, P19, P20, and P71. P73 then addresses one measurement-channel assumption left open by P72.

## 2. Target-side bridge lineage

### P19: declared physical sufficiency

For a declared physical descriptor \(T\) and independently specified target \(E\), P19 asks whether

\[
E=B\circ T
\]

and, in the finite stochastic formulation, whether

\[
I(E;\Omega\mid T)=0.
\]

A positive conditional-information residual rejects screening-off by the declared descriptor. It does not establish nonphysicality.

### P20-P24: finite data, refinement, selection, and stopping

P20 converts the P19 residual into a finite-sample confidence statement. P21 decomposes residual reduction under descriptor refinement. P22 makes an entire refinement chain simultaneously valid. P23 protects fixed-sample adaptive descriptor selection. P24 extends the guarantee to repeated looks and finite stopping times under the declared finite-alphabet IID model.

### P71: target-provenance non-circularity

If the target is constructed as

\[
E=h(T),
\]

then factorization and zero residual hold by construction. P71 therefore separates a mathematical fit from independent evidential target provenance.

![P71 target-provenance non-circularity](figures/p71_target_provenance_noncircularity.svg)

Direct proof: [P71](proposition_71_target_provenance_noncircularity.md).

### P72: noisy target-measurement robustness

Let \(E^\star\) be an independently justified latent target and \(Y\) its observed measurement. Under

\[
Y\perp\!\!\!\perp\Omega\mid(E^\star,T),
\]

P72 proves

\[
\boxed{
I(Y;\Omega\mid T)
\le
I(E^\star;\Omega\mid T).
}
\]

Thus a positive observed population residual transfers to the latent target under the declared measurement model. The converse fails because an erasing measurement channel can hide a real latent residual.

For pairwise target distributions and channel \(K_t\), P72 defines

\[
\gamma_t
=
\inf_{\substack{v\ne0\\\mathbf1^\top v=0}}
\frac{\|K_tv\|_1}{\|v\|_1}
\]

and proves

\[
\boxed{
\gamma_t\operatorname{TV}(p,q)
\le
\operatorname{TV}(K_tp,K_tq)
\le
\operatorname{TV}(p,q).
}
\]

For a binary symmetric target channel, \(\gamma=|1-2\eta|\). P72 also provides a finite categorical target-TV lower confidence bound and a conservative sufficient equal-sample-size condition scaling as \((\gamma_0\Delta_E)^{-2}\).

![P72 target-measurement channel robustness](figures/p72_target_measurement_channel_robustness.svg)

Direct proof: [P72](proposition_72_target_measurement_channel_robustness.md). Provenance: [P72 equation record](p72_equation_provenance.md). Implementation: [`target_measurement_channel_robustness.py`](../src/consciousness_bridge/target_measurement_channel_robustness.py). Tests: [`test_target_measurement_channel_robustness.py`](../tests/test_target_measurement_channel_robustness.py).

### P73: three-view target-channel identifiability

P73 asks whether the stability coefficient used by P72 can be identified from repeated target measurements rather than assumed. In the declared binary symmetric three-view model,

\[
Y_i=ZN_i,
\qquad
r_i=\mathbb E[N_i],
\qquad
\gamma_i=|r_i|,
\]

with mutually independent noises independent of the latent binary target \(Z\). The observable pairwise moments satisfy

\[
\boxed{m_{ij}=\mathbb E[Y_iY_j]=r_ir_j.}
\]

Two heterogeneous views identify only the product \(\gamma_1\gamma_2\), so individual stabilities are not identifiable. With three nonzero compatible views,

\[
\boxed{
\gamma_1=\sqrt{\frac{m_{12}m_{13}}{m_{23}}},
\quad
\gamma_2=\sqrt{\frac{m_{12}m_{23}}{m_{13}}},
\quad
\gamma_3=\sqrt{\frac{m_{13}m_{23}}{m_{12}}}.
}
\]

The signed reliabilities remain ambiguous under one simultaneous global sign flip, but the stability magnitudes needed by P72 are unique. P73 also gives simultaneous finite-sample intervals from Hoeffding bounds on the three empirical pair moments and shows how an independently calibrated lower stability bound can be handed to P72 with explicit confidence accounting.

![P73 three-view target-channel identifiability](figures/p73_three_view_target_channel_identifiability.svg)

Direct proof: [P73](proposition_73_three_view_target_channel_identifiability.md). Provenance: [P73 equation record](p73_equation_provenance.md). Implementation: [`three_view_target_channel_identifiability.py`](../src/consciousness_bridge/three_view_target_channel_identifiability.py). Tests: [`test_three_view_target_channel_identifiability.py`](../tests/test_three_view_target_channel_identifiability.py).

## 3. Complete proposition index

| Proposition | Mathematical role | Scientific role | Status |
| --- | --- | --- | --- |
| [P1](proposition_1_representation_invariance.md) | quotient factorization | representation-independent bridge objects | proved |
| [P2](proposition_2_bridge_identifiability.md) | total-variation discriminability | exact theory identifiability | proved |
| [P3](proposition_3_bridge_equivalence_classes.md) | observable quotient | experiment-class equivalence | proved |
| [P4](proposition_4_discriminating_experiment_design.md) | maximin and set cover | adversarial experiment design | proved |
| [P5](proposition_5_feature_sufficiency.md) | feature factorization | exact feature sufficiency | proved |
| [P6](proposition_6_canonical_bridge_signature.md) | canonical quotient | completeness target | proved |
| [P7](proposition_7_experimental_signature_recovery.md) | observable recovery | exact recoverability | proved |
| [P8](proposition_8_robust_signature_recovery.md) | perturbation bounds | finite-error recovery | proved |
| [P9](proposition_9_categorical_sample_complexity.md) | Hoeffding plus union bound | finite trial requirement | proved |
| [P10](proposition_10_robust_experiment_design.md) | robust protocol optimization | nuisance-aware discrimination | proved |
| [P11](proposition_11_intervention_resolved_causal_structure.md) | intervention-response structure | structured physical candidate | proved construction / candidate |
| [P12](proposition_12_component_insufficiency.md) | projection collisions | scalar/component insufficiency | proved no-go |
| [P13](proposition_13_pairwise_component_irredundancy.md) | pairwise projection collisions | component irredundancy | proved |
| [P14](proposition_14_temporal_continuation.md) | quotient temporal metric | representation-invariant continuation | proved |
| [P15](proposition_15_finite_sample_temporal_certification.md) | temporal perturbation bounds | finite-error temporal certification | proved |
| [P16](proposition_16_independent_composition_and_coupling.md) | product-response composition | independence null and coupling | proved |
| [P17](proposition_17_coarse_graining_and_refinement.md) | stochastic-map contraction | information loss under coarse-graining | proved |
| [P18](proposition_18_scale_sufficiency_certification.md) | approximate reconstruction | scale sufficiency | proved |
| [P19](proposition_19_fundamental_physical_sufficiency.md) | factorization, CMI, rank obstruction | declared physical sufficiency | proved |
| [P20](proposition_20_finite_sample_residual_certification.md) | finite CMI confidence interval | finite-data residual certification | proved |
| [P21](proposition_21_descriptor_refinement_residual_persistence.md) | conditional-information chain rule | omitted-physics refinement audit | proved |
| [P22](proposition_22_simultaneous_refinement_chain_certification.md) | shared confidence event | simultaneous refinement certification | proved |
| [P23](proposition_23_adaptive_descriptor_selection_certification.md) | post-selection control | adaptive descriptor choice | proved |
| [P24](proposition_24_anytime_adaptive_refinement_certification.md) | alpha spending | repeated-look validity | proved |
| [P25](proposition_25_directed_influence_scale_certification.md) | influence contraction | directed-influence scale stability | proved |
| [P26](proposition_26_partition_irreducibility_scale_certification.md) | product-null contraction | partition scale stability | proved |
| [P27](proposition_27_partition_lattice_node_aggregation.md) | lattice transport | node-aggregation semantics | proved |
| [P28](proposition_28_intervention_node_aggregation_compatibility.md) | source-label descent | aggregate influence compatibility | proved |
| [P29](proposition_29_response_geometry_node_aggregation.md) | pseudometric transport | response geometry under aggregation | proved |
| [P30](proposition_30_full_p11_scale_compatibility.md) | branch assembly | complete declared P11 scale transport | proved |
| [P31](proposition_31_intervention_quotient_compatibility.md) | intervention quotient | exact label descent | proved |
| [P32](proposition_32_delay_quotient_compatibility.md) | delay quotient | temporal descent | proved |
| [P33](proposition_33_joint_operational_quotient.md) | product quotient | joint intervention-delay descent | proved |
| [P34](proposition_34_joint_p11_operational_scale.md) | scale assembly | complete operational declaration | proved |
| [P35](proposition_35_approximate_directed_influence_operational_quotient.md) | metric perturbation | approximate influence stability | proved |
| [P36](proposition_36_partition_irreducibility_operational_quotient.md) | product-measure perturbation | approximate irreducibility stability | proved |
| [P37](proposition_37_complete_approximate_p11_operational_scale.md) | max-norm assembly | complete approximate P11 certificate | proved |
| [P38](proposition_38_quantum_operational_sufficiency.md) | quantum-state factorization | quantum operational sufficiency | proved conditional theorem |
| [P39](proposition_39_finite_data_quantum_nonfactorization.md) | tomography model-set bounds | finite-data quantum non-factorization | proved |
| [P40](proposition_40_continuous_quantum_region_regularity.md) | regularity obstruction | continuous-region bridge test | proved |
| [P41](proposition_41_trace_ball_quantum_envelope.md) | trace-ball envelope | computable quantum uncertainty | proved |
| [P42](proposition_42_quantum_regular_bridge_sample_complexity.md) | finite IC concentration | quantum-target sample design | proved |
| [P43](proposition_43_optimal_quantum_target_allocation.md) | convex allocation | optimal quantum-target split | proved |
| [P44](proposition_44_pair_adaptive_sample_allocation.md) | simultaneous pair coverage | post-data witness selection | proved |
| [P45](proposition_45_shared_preparation_graph_allocation.md) | shared convex allocation | preparation graph design | proved |
| [P46](proposition_46_budget_constrained_witness_graph.md) | combinatorial optimization | hard-budget witness selection | proved |
| [P47](proposition_47_anytime_sequential_witness_graph.md) | time-uniform graph inference | adaptive sampling and stopping | proved |
| [P48](proposition_48_gap_dependent_stopping_complexity.md) | confidence-sequence inversion | stopping complexity | proved |
| [P49](proposition_49_dyadic_stopping_overhead.md) | dyadic checkpoint geometry | logarithmic certification looks | proved |
| [P50](proposition_50_bounded_starvation_asynchronous_sampling.md) | fairness service bound | asynchronous stopping | proved |
| [P51](proposition_51_heterogeneous_service_rate_stopping.md) | heterogeneous quotas | service-rate stopping | proved |
| [P52](proposition_52_capacity_optimal_service_allocation.md) | minimax service allocation | capacity-optimal sampling | proved |
| [P53](proposition_53_residual_demand_reoptimization.md) | residual reoptimization | dynamic service release | proved |
| [P54](proposition_54_metric_switching_cost_residual_scheduling.md) | Hamiltonian-path reduction | metric switching schedule | proved |
| [P55](proposition_55_pruning_aware_switching_monotonicity.md) | metric shortcutting | pruning-aware cost release | proved |
| [P56](proposition_56_moving_start_metric_reoptimization_stability.md) | start-state perturbation | moving setup stability | proved |
| [P57](proposition_57_switching_metric_perturbation.md) | metric perturbation | switching geometry robustness | proved |
| [P58](proposition_58_finite_data_metric_uncertainty.md) | route envelopes | finite-data switching uncertainty | proved |
| [P59](proposition_59_optimal_transition_calibration.md) | strict convexity and KKT | optimal continuous calibration | proved |
| [P60](proposition_60_integer_transition_calibration.md) | ceiling construction | hard-budget integer calibration | proved |
| [P61](proposition_61_exact_integer_transition_calibration.md) | diminishing returns | exact equal-cost integer calibration | proved |
| [P62](proposition_62_heterogeneous_cost_transition_calibration.md) | heterogeneous KKT allocation | unequal-cost calibration | proved |
| [P63](proposition_63_exact_heterogeneous_integer_calibration.md) | Bellman dynamic program | exact unequal-cost integer calibration | proved |
| [P64](proposition_64_fast_heterogeneous_integer_approximation.md) | floor approximation | scalable certified approximation | proved |
| [P65](proposition_65_lower_bounded_heterogeneous_calibration.md) | active-set water filling | baseline-safe heterogeneous calibration | proved |
| [P66](proposition_66_residual_exact_calibration_augmentation.md) | residual dynamic program | exact floor-dominating augmentation | proved |
| [P67](proposition_67_global_integer_optimality_certificate.md) | common multiplier | global integer optimality certificate | proved |
| [P68](proposition_68_lagrangian_optimality_gap.md) | weak duality | quantitative candidate-gap certificate | proved |
| [P69](proposition_69_dual_optimal_multiplier.md) | concave dual optimization | strongest P68 lower-bound search | proved |
| [P70](proposition_70_primal_dual_gap_decomposition.md) | exact gap identity | certificate attribution | proved primal-dual diagnostic decomposition |
| [P71](proposition_71_target_provenance_noncircularity.md) | descriptor-derived target vacuity | independent target provenance guard | proved |
| [P72](proposition_72_target_measurement_channel_robustness.md) | conditional DPI, TV stability, finite target confidence | noisy target-measurement robustness | proved |
| [P73](proposition_73_three_view_target_channel_identifiability.md) | three-view moment factorization and finite stability intervals | target-channel stability identifiability | proved under declared binary symmetric repeated-view model |

## 4. Calibration branch remains separate

The complete P61-P70 derivations, theorem figures, implementations, and tests are maintained on the dedicated [Calibration and Optimization Frontier](calibration_optimization_frontier_p61_p70.md).

The theorem visuals remain permanently available, including:

- `figures/p61_exact_integer_transition_calibration.svg`
- `figures/p62_heterogeneous_cost_transition_calibration.svg`
- `figures/p63_exact_heterogeneous_integer_calibration.svg`
- `figures/p64_fast_heterogeneous_integer_approximation.svg`
- `figures/p65_lower_bounded_heterogeneous_calibration.svg`
- `figures/p66_residual_exact_calibration_augmentation.svg`
- `figures/p67_global_integer_optimality_certificate.svg`
- `figures/p68_lagrangian_optimality_gap.svg`
- `figures/p69_dual_optimal_multiplier.svg`
- `figures/p70_primal_dual_gap_decomposition.svg`

These results optimize downstream experimental resources. They do not define consciousness and do not supply the missing physical-to-experiential bridge law.

## 5. Current open frontier

After P73, the target-side chain now makes three separate obligations explicit:

1. the target must have non-circular provenance relative to the tested physical descriptor;
2. its observation channel must preserve enough of the claimed target distinction to support the inference;
3. when stability is estimated from repeated views, the assumptions that make the repeated-view channel identifiable must themselves be justified or tested.

P73 closes target-channel stability identification only for a narrow binary symmetric, conditionally independent three-view model. The immediate next structural problem is therefore **target-channel model adequacy and correlated-error robustness**: how much can shared bias, conditional dependence, class asymmetry, or state-dependent measurement distort the inferred stability, and what observable diagnostics or sensitivity bounds can expose that failure?

Beyond that, the broader open program remains:

- define and justify experiential variables independently of the physical candidate;
- extend target-channel identification beyond the binary symmetric independent-view setting where scientifically justified;
- test descriptor sufficiency across interventions, time, composition, and scale;
- sharpen finite-data guarantees for continuous, dependent, hidden-state, and learned-descriptor settings;
- compare competing bridge theories on shared adversarial experiment families;
- search for biological and non-biological counterexamples;
- attempt a bridge theorem only after the physical, target, measurement, statistical, scale, and falsification layers are jointly defensible.

The physical-to-experiential bridge remains open.
