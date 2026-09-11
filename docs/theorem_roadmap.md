# Theorem Roadmap

This roadmap records the proved mathematical chain and the open route toward a scientifically meaningful physical-to-experiential bridge. It is organized by **logical dependency**, not by development date.

The current documented theorem frontier is **P75**. The proposition record runs from **P1 through P75 with explicit dependency branches**. P71-P75 return to the core P19 bridge-sufficiency lineage; they do not extend the P61-P70 calibration branch.

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
&\text{P73: target-channel stability can be identified under a declared three-view model}\\
&\Downarrow\\
&\text{P74: finite data can certify or refuse that channel recovery}\\
&\Downarrow\\
&\text{P75: the target-measurement model must face overidentifying adequacy tests}
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

The proposition number records development order. It does not imply that P75 depends on P70. P75 depends scientifically on P19 and the P71-P74 target-side lineage, especially the P73 binary latent model whose adequacy it tests.

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

Fix one physical stratum \(T=t\), let \(S\in\{-1,+1\}\) be a declared binary latent target, and let \(X_1,X_2,X_3\) be binary target views that are conditionally independent given \(S\). Write

\[
\mathbb E[X_j\mid S]=a_j+b_jS.
\]

With interior latent prevalence and nonzero loadings, P73 derives

\[
\boxed{C_{ij}=b_ib_j(1-m^2)}
\]

and

\[
\boxed{M_{123}=-2m(1-m^2)b_1b_2b_3.}
\]

The observable ratio

\[
q=\frac{M_{123}^2}{C_{12}C_{13}C_{23}}
\]

then gives

\[
\boxed{m^2=\frac{q}{q+4},\qquad 1-m^2=\frac4{q+4}.}
\]

Choosing one algebraic loading orientation recovers the three view channels and latent prevalence. The remaining global latent-label swap is an exact model symmetry and cannot be removed without an independent semantic anchor.

For each binary view, the P72 stability coefficient becomes

\[
\boxed{\gamma_j=|b_j|,}
\]

which is invariant under the label swap and is therefore identifiable from the observed three-view law in the declared nondegenerate model. The recovered joint channel also obeys

\[
\boxed{\gamma_{123}\ge\max\{\gamma_1,\gamma_2,\gamma_3\}.}
\]

P73 also gives a constructive two-view no-go result: in the balanced zero-intercept model, the full observed two-view law depends only on \(b_1b_2\), so different individual channel stabilities can produce exactly the same observable distribution.

![P73 target-channel identifiability](figures/p73_target_channel_identifiability.svg)

Direct proof: [P73](proposition_73_target_channel_identifiability.md). Provenance: [P73 equation record](p73_equation_provenance.md). Implementation: [`target_channel_identifiability.py`](../src/consciousness_bridge/target_channel_identifiability.py). Tests: [`test_target_channel_identifiability.py`](../tests/test_target_channel_identifiability.py).

### P74: finite-sample target-channel recovery

P73 is a population inversion. P74 adds an explicit finite-sample layer. From \(n\) IID observed triples, the empirical eight-cell law \(\widehat P\) satisfies one simultaneous Hoeffding event. Defining

\[
\delta_n(\alpha)
=
\min\left\{2,8\sqrt{\frac{\log(16/\alpha)}{2n}}\right\},
\]

P74 proves on that event

\[
\boxed{|\widehat C_{ij}-C_{ij}|\le3\delta_n}
\]

and

\[
\boxed{|\widehat M_{123}-M_{123}|\le13\delta_n.}
\]

The theorem then introduces a finite-data nondegeneracy gate. The P73 inversion is certified only when every absolute covariance confidence interval is bounded away from zero and the covariance sign product is compatible with the P73 model. If the gate fails, the output is "not certified by the current data," not a forced latent estimate.

When the gate passes, P74 propagates the simultaneous event through the P73 formulas to obtain confidence intervals for the latent imbalance, latent variance, the prevalence orbit under global label swapping, all three P72 stability coefficients, the label-invariant products \(b_jm\), the channel offsets, and the full unordered latent-conditioned binary response-probability pairs. It also gives a certified lower bound for joint three-view stability and a conservative sufficient sample-size condition for clearing a known population covariance margin.

![P74 finite-sample target-channel recovery](figures/p74_finite_sample_target_channel_recovery.svg)

Direct proof: [P74](proposition_74_finite_sample_target_channel_recovery.md). Provenance: [P74 equation record](p74_equation_provenance.md). Implementation: [`finite_sample_target_channel_recovery.py`](../src/consciousness_bridge/finite_sample_target_channel_recovery.py). Tests: [`test_finite_sample_target_channel_recovery.py`](../tests/test_finite_sample_target_channel_recovery.py).

### P75: target-model adequacy and four-view overidentification

P73 identifies parameters under a declared three-view conditional-independence model, and P74 certifies that recovery from finite data. P75 asks whether successful recovery also validates that model. It does not.

For \(k\) binary observed views, the full observed law has

\[
d_{\mathrm{obs}}(k)=2^k-1
\]

continuous degrees of freedom, while one binary latent state with \(k\) binary view channels has

\[
d_{\mathrm{model}}(k)=1+2k.
\]

Therefore

\[
\boxed{d_{\mathrm{obs}}(3)=7=d_{\mathrm{model}}(3),}
\]

so the nondegenerate three-view model is generically just-identified. This does not mean every three-view distribution belongs to the real stochastic model; positivity, nondegeneracy, and valid-channel inequalities still matter. It means there is no generic dimension-based reserve of equality constraints after fitting the model.

With a fourth binary view,

\[
\boxed{d_{\mathrm{obs}}(4)=15,\qquad d_{\mathrm{model}}(4)=9,\qquad d_{\mathrm{over}}=6.}
\]

The fourth view therefore creates six generic overidentifying degrees of freedom. Under the declared conditional-independence model, P75 derives

\[
\boxed{C_{12}C_{34}=C_{13}C_{24}=C_{14}C_{23}}
\]

and requires all nondegenerate three-view subsets to recover the same latent-imbalance quantity

\[
\boxed{
q_{ijk}=\frac{M_{ijk}^2}{C_{ij}C_{ik}C_{jk}}=\frac{4m^2}{1-m^2}.
}
\]

It also derives the higher-order consistency relation

\[
\boxed{M_{1234}=(1+q)C_{12}C_{34},}
\]

with the equivalent covariance pairings.

The executable P75 audit does not treat those displayed moments as a complete algebraic characterization. It recovers an anchor P73 triple, infers the fourth binary channel, reconstructs all 16 cells of the four-view observable law, and checks exact population compatibility. A synthetic residual-dependence example is required to fail this full-law reconstruction and the transparent moment diagnostics.

![P75 target-model adequacy and four-view overidentification](figures/p75_target_model_adequacy_overidentification.svg)

Direct proof: [P75](proposition_75_target_model_adequacy_overidentification.md). Provenance: [P75 equation record](p75_equation_provenance.md). Implementation: [`target_model_adequacy.py`](../src/consciousness_bridge/target_model_adequacy.py). Tests: [`test_target_model_adequacy.py`](../tests/test_target_model_adequacy.py).

## 3. Complete proposition index

| Proposition | Mathematical role | Scientific role | Status |
| --- | --- | --- | --- |
| [P1](proposition_1_representation_invariance.md) | quotient factorization | representation-independent bridge objects | proved |
| [P2](proposition_2_bridge_identifiability.md) | total-variation discriminability | exact theory identifiability | proved |
| [P3](proposition_3_bridge_equivalence_classes.md) | observable quotient | experiment-class equivalence | proved |
| [P4](proposition_4_discriminating_experiment_design.md) | maximin and set cover | adversarial experiment design | proved |
| [P5](proposition_5_feature_sufficiency.md) | feature factorization | exact feature sufficiency | proved |
| [P6](proposition_6_canonical_bridge_signature.md) | canonical quotient | completeness target | proved |
| [P7](proposition_7_experimental_signature_recovery.md) | observable recovery | exact recoverability criterion | proved |
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
| [P73](proposition_73_target_channel_identifiability.md) | three-view moment inversion and two-view no-go | target-channel stability identifiability under a declared latent model | proved conditional theorem |
| [P74](proposition_74_finite_sample_target_channel_recovery.md) | simultaneous concentration and nonlinear interval propagation | finite-data target-channel recovery with a nondegeneracy gate | proved conditional theorem |
| [P75](proposition_75_target_model_adequacy_overidentification.md) | dimension count, tetrads, cross-triple moments, full-law reconstruction | target-model adequacy and four-view overidentification | proved conditional theorem |

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

After P75, the target side has five explicit requirements:

1. the target must have non-circular provenance relative to the tested physical descriptor;
2. its observation channel must be valid and sufficiently informative for the claimed witness;
3. channel reliability must be identified or externally calibrated under a defensible target-measurement model;
4. finite data must resolve the channel parameters far enough from the model singularity to support a confidence-certified reliability statement;
5. the target-measurement model itself must survive adequacy tests rather than being accepted because it can be fit.

P75 closes the population-level fifth item for one binary four-view extension of the P73 model. It provides explicit observable restrictions and full-law reconstruction, but it does not yet attach finite-sample simultaneous uncertainty to those adequacy residuals. The next structural question is therefore **finite-sample model-adequacy certification**.

Beyond that, the broader open program remains:

- test target-model adequacy under finite data and residual dependence;
- define and justify experiential variables independently of the physical candidate;
- test descriptor sufficiency across interventions, time, composition, and scale;
- sharpen finite-data guarantees for continuous, dependent, hidden-state, and learned-descriptor settings;
- compare competing bridge theories on shared adversarial experiment families;
- search for biological and non-biological counterexamples;
- attempt a bridge theorem only after the physical, target, measurement, statistical, scale, and falsification layers are jointly defensible.

The physical-to-experiential bridge remains open.
