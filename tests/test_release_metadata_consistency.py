import re
from pathlib import Path


def test_release_versions_are_synchronized():
    readme = Path("README.md").read_text(encoding="utf-8")
    pyproject = Path("pyproject.toml").read_text(encoding="utf-8")
    citation = Path("CITATION.cff").read_text(encoding="utf-8")
    assert "version-0.50.0-2563eb" in readme
    assert re.search(r'^version = "0\.50\.0"$', pyproject, re.MULTILINE)
    assert re.search(r'^version: 0\.50\.0$', citation, re.MULTILINE)


def test_quantum_publication_paths_are_visible():
    readme = Path("README.md").read_text(encoding="utf-8")
    for token in (
        "Proposition 39",
        "p39_finite_data_quantum_nonfactorization.svg",
        "finite_data_quantum_nonfactorization.py",
        "test_finite_data_quantum_nonfactorization.py",
        "Proposition 40",
        "p40_continuous_quantum_region_regularity.svg",
        "continuous_quantum_region_regularity.py",
        "test_continuous_quantum_region_regularity.py",
        "Proposition 41",
        "p41_trace_ball_quantum_envelope.svg",
        "trace_ball_quantum_envelope.py",
        "test_trace_ball_quantum_envelope.py",
        "Proposition 42",
        "p42_quantum_regular_bridge_sample_complexity.svg",
        "quantum_regular_bridge_sample_complexity.py",
        "test_quantum_regular_bridge_sample_complexity.py",
        "Proposition 43",
        "p43_optimal_quantum_target_allocation.svg",
        "optimal_quantum_target_allocation.py",
        "test_optimal_quantum_target_allocation.py",
        "Proposition 44",
        "p44_pair_adaptive_sample_allocation.svg",
        "pair_adaptive_sample_allocation.py",
        "test_pair_adaptive_sample_allocation.py",
        "Proposition 45",
        "p45_shared_preparation_graph_allocation.svg",
        "shared_preparation_graph_allocation.py",
        "test_shared_preparation_graph_allocation.py",
        "Proposition 46",
        "p46_budget_constrained_witness_graph.svg",
        "budget_constrained_witness_graph.py",
        "test_budget_constrained_witness_graph.py",
        "Proposition 47",
        "p47_sequential_graph_refinement.svg",
        "sequential_witness_graph.py",
        "test_sequential_witness_graph.py",
        "Proposition 48",
        "p48_gap_dependent_stopping_complexity.svg",
        "gap_stopping_complexity.py",
        "test_gap_stopping_complexity.py",
        "Proposition 49",
        "p49_dyadic_stopping_overhead.svg",
        "dyadic_stopping_overhead.py",
        "test_dyadic_stopping_overhead.py",
        "Proposition 50",
        "p50_bounded_starvation_asynchronous_sampling.svg",
        "bounded_starvation_sampling.py",
        "test_bounded_starvation_sampling.py",
    ):
        assert token in readme
