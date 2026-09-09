import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
QUANTUM = ROOT / "docs" / "figures" / "quantum"
MANIFEST = QUANTUM / "quantum_figure_manifest.json"


def test_quantum_atlas_contains_eighteen_equation_driven_figures():
    figures = sorted(QUANTUM.glob("qm*.svg"))
    assert len(figures) == 18
    assert all(path.stat().st_size > 1000 for path in figures)
    assert all("<svg" in path.read_text(encoding="utf-8")[:500] for path in figures)


def test_quantum_manifest_matches_generated_files_and_declares_boundaries():
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    figures = sorted(path.name for path in QUANTUM.glob("qm*.svg"))

    assert data["figure_count"] == len(figures) == 18
    assert sorted(item["file"] for item in data["figures"]) == figures
    assert "do not establish that consciousness is quantum" in data[
        "scientific_boundary"
    ]
    for item in data["figures"]:
        assert item["equation"].strip()
        assert item["fact"].strip()
        assert item["status"].strip()


def test_born_probabilities_are_normalized_for_rotated_qubit():
    theta = np.linspace(0.0, np.pi, 1001)
    p0 = np.cos(theta / 2.0) ** 2
    p1 = np.sin(theta / 2.0) ** 2
    assert np.allclose(p0 + p1, 1.0, atol=1e-12)
    assert np.isclose(p0[0], 1.0)
    assert np.isclose(p1[-1], 1.0)


def test_heisenberg_minimum_uncertainty_family_saturates_bound():
    hbar = 1.0
    sigma_x = np.array([0.2, 0.5, 1.0, 2.0, 4.0])
    sigma_p = hbar / (2.0 * sigma_x)
    assert np.allclose(sigma_x * sigma_p, hbar / 2.0)


def test_dephasing_reduces_coherence_and_purity_to_expected_limits():
    gamma = 0.45
    time = np.linspace(0.0, 50.0, 1000)
    coherence = 0.5 * np.exp(-gamma * time)
    purity = 0.5 * (1.0 + np.exp(-2.0 * gamma * time))

    assert np.all(np.diff(coherence) <= 1e-14)
    assert np.all(np.diff(purity) <= 1e-14)
    assert np.isclose(purity[0], 1.0)
    assert np.isclose(purity[-1], 0.5, atol=1e-9)


def test_von_neumann_and_entanglement_entropy_have_correct_extrema():
    probability = np.array([1e-12, 0.5, 1.0 - 1e-12])
    entropy = -probability * np.log2(probability) - (
        1.0 - probability
    ) * np.log2(1.0 - probability)
    assert np.isclose(entropy[1], 1.0)
    assert entropy[0] < 1e-9
    assert entropy[2] < 1e-9

    theta = np.pi / 4.0
    lam = np.cos(theta) ** 2
    entanglement = -lam * np.log2(lam) - (1.0 - lam) * np.log2(1.0 - lam)
    assert np.isclose(entanglement, 1.0)


def test_chsh_family_reaches_quantum_maximum_and_exceeds_local_bound():
    theta = np.linspace(0.0, np.pi / 2.0, 20001)
    value = np.abs(-3.0 * np.cos(theta) + np.cos(3.0 * theta))
    maximum = float(np.max(value))

    assert maximum > 2.0
    assert np.isclose(maximum, 2.0 * np.sqrt(2.0), rtol=2e-5)


def test_depolarizing_channel_contracts_trace_distance_exactly_for_qubits():
    p = np.linspace(0.0, 1.0, 101)
    initial_distance = 0.83
    output_distance = (1.0 - p) * initial_distance

    assert np.all(output_distance <= initial_distance + 1e-12)
    assert np.isclose(output_distance[0], initial_distance)
    assert np.isclose(output_distance[-1], 0.0)


def test_schmidt_reduced_state_is_normalized_and_maximally_mixed_at_pi_over_four():
    theta = np.linspace(0.0, np.pi / 2.0, 1001)
    lam1 = np.cos(theta) ** 2
    lam2 = np.sin(theta) ** 2

    assert np.allclose(lam1 + lam2, 1.0)
    midpoint = len(theta) // 2
    assert np.isclose(lam1[midpoint], 0.5)
    assert np.isclose(lam2[midpoint], 0.5)
