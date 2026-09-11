import re
from pathlib import Path


def test_release_versions_are_synchronized():
    readme = Path("README.md").read_text(encoding="utf-8")
    pyproject = Path("pyproject.toml").read_text(encoding="utf-8")
    citation = Path("CITATION.cff").read_text(encoding="utf-8")
    assert "version-0.70.0-2563eb" in readme
    assert re.search(r'^version = "0\.70\.0"$', pyproject, re.MULTILINE)
    assert re.search(r'^version: 0\.70\.0$', citation, re.MULTILINE)


def test_quantum_and_experiment_publication_paths_are_visible_on_reader_appropriate_surfaces():
    readme = Path("README.md").read_text(encoding="utf-8")
    calibration = Path("docs/calibration_optimization_frontier_p61_p70.md").read_text(encoding="utf-8")

    main_artifacts = {
        39: ("p39_finite_data_quantum_nonfactorization.svg", "finite_data_quantum_nonfactorization.py", "test_finite_data_quantum_nonfactorization.py"),
        40: ("p40_continuous_quantum_region_regularity.svg", "continuous_quantum_region_regularity.py", "test_continuous_quantum_region_regularity.py"),
        41: ("p41_trace_ball_quantum_envelope.svg", "trace_ball_quantum_envelope.py", "test_trace_ball_quantum_envelope.py"),
        42: ("p42_quantum_regular_bridge_sample_complexity.svg", "quantum_regular_bridge_sample_complexity.py", "test_quantum_regular_bridge_sample_complexity.py"),
        43: ("p43_optimal_quantum_target_allocation.svg", "optimal_quantum_target_allocation.py", "test_optimal_quantum_target_allocation.py"),
        44: ("p44_pair_adaptive_sample_allocation.svg", "pair_adaptive_sample_allocation.py", "test_pair_adaptive_sample_allocation.py"),
        45: ("p45_shared_preparation_graph_allocation.svg", "shared_preparation_graph_allocation.py", "test_shared_preparation_graph_allocation.py"),
        46: ("p46_budget_constrained_witness_graph.svg", "budget_constrained_witness_graph.py", "test_budget_constrained_witness_graph.py"),
        47: ("p47_sequential_graph_refinement.svg", "sequential_witness_graph.py", "test_sequential_witness_graph.py"),
        48: ("p48_gap_dependent_stopping_complexity.svg", "gap_stopping_complexity.py", "test_gap_stopping_complexity.py"),
        49: ("p49_dyadic_stopping_overhead.svg", "dyadic_stopping_overhead.py", "test_dyadic_stopping_overhead.py"),
        50: ("p50_bounded_starvation_asynchronous_sampling.svg", "bounded_starvation_sampling.py", "test_bounded_starvation_sampling.py"),
        51: ("p51_heterogeneous_service_rate_stopping.svg", "heterogeneous_service_stopping.py", "test_heterogeneous_service_stopping.py"),
        52: ("p52_capacity_optimal_service_allocation.svg", "capacity_optimal_service_allocation.py", "test_capacity_optimal_service_allocation.py"),
        53: ("p53_residual_demand_reoptimization.svg", "residual_demand_reoptimization.py", "test_residual_demand_reoptimization.py"),
        54: ("p54_metric_switching_cost_residual_scheduling.svg", "metric_switching_residual_schedule.py", "test_metric_switching_residual_schedule.py"),
        55: ("p55_pruning_aware_switching_monotonicity.svg", "pruning_aware_switching_monotonicity.py", "test_pruning_aware_switching_monotonicity.py"),
        56: ("p56_moving_start_metric_reoptimization_stability.svg", "moving_start_metric_reoptimization.py", "test_moving_start_metric_reoptimization.py"),
        57: ("p57_switching_metric_perturbation.svg", "switching_metric_perturbation.py", "test_switching_metric_perturbation.py"),
        58: ("p58_finite_data_metric_uncertainty.svg", "finite_data_metric_uncertainty.py", "test_finite_data_metric_uncertainty.py"),
        59: ("p59_optimal_transition_calibration.svg", "optimal_transition_calibration.py", "test_optimal_transition_calibration.py"),
        60: ("p60_integer_transition_calibration.svg", "integer_transition_calibration.py", "test_integer_transition_calibration.py"),
    }

    for proposition, artifacts in main_artifacts.items():
        assert f"Proposition {proposition}" in readme
        for token in artifacts:
            assert token in readme

    calibration_artifacts = {
        61: ("p61_exact_integer_transition_calibration.svg", "exact_integer_transition_calibration.py", "test_exact_integer_transition_calibration.py"),
        62: ("p62_heterogeneous_cost_transition_calibration.svg", "heterogeneous_cost_transition_calibration.py", "test_heterogeneous_cost_transition_calibration.py"),
        63: ("p63_exact_heterogeneous_integer_calibration.svg", "exact_heterogeneous_integer_calibration.py", "test_exact_heterogeneous_integer_calibration.py"),
        64: ("p64_fast_heterogeneous_integer_approximation.svg", "fast_heterogeneous_integer_approximation.py", "test_fast_heterogeneous_integer_approximation.py"),
        65: ("p65_lower_bounded_heterogeneous_calibration.svg", "lower_bounded_heterogeneous_calibration.py", "test_lower_bounded_heterogeneous_calibration.py"),
        66: ("p66_residual_exact_calibration_augmentation.svg", "residual_exact_calibration_augmentation.py", "test_residual_exact_calibration_augmentation.py"),
        67: ("p67_global_integer_optimality_certificate.svg", "global_integer_optimality_certificate.py", "test_global_integer_optimality_certificate.py"),
        68: ("p68_lagrangian_optimality_gap.svg", "lagrangian_optimality_gap.py", "test_lagrangian_optimality_gap.py"),
        69: ("p69_dual_optimal_multiplier.svg", "dual_optimal_multiplier.py", "test_dual_optimal_multiplier.py"),
        70: ("p70_primal_dual_gap_decomposition.svg", "primal_dual_gap_decomposition.py", "test_primal_dual_gap_decomposition.py"),
    }

    assert "docs/calibration_optimization_frontier_p61_p70.md" in readme
    for proposition, artifacts in calibration_artifacts.items():
        assert f"P{proposition}" in calibration
        for token in artifacts:
            assert token in calibration
