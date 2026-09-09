import json
from pathlib import Path

import numpy as np
import pytest

from consciousness_bridge.causal_structure_coarse_graining import pushforward_tv_pair
from consciousness_bridge.causal_structure_scale_certification import (
    scale_separation_certificate,
)

ROOT = Path(__file__).resolve().parents[1]
FIGURE_DIR = ROOT / "docs" / "figures" / "quantitative"
MANIFEST = FIGURE_DIR / "quantitative_figure_manifest.json"


def test_quantitative_atlas_contains_at_least_33_equation_driven_figures():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    figures = sorted(FIGURE_DIR.glob("q*.svg"))

    assert len(manifest) >= 33
    assert len(figures) == len(manifest)
    assert len({item["file"] for item in manifest}) == len(manifest)


def test_every_manifest_figure_is_a_nonempty_svg():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    for item in manifest:
        path = FIGURE_DIR / item["file"]
        text = path.read_text(encoding="utf-8")
        assert path.stat().st_size > 5_000
        assert "<svg" in text
        assert item["equation"]
        assert item["fact"]
        assert item["status"]


def test_ou_stationary_variance_numeric_benchmark():
    theta = 1.4
    sigma = 0.65
    stationary_variance = sigma**2 / (2.0 * theta)

    assert stationary_variance == pytest.approx(0.15089285714285716)


def test_landauer_300_kelvin_numeric_benchmark():
    k_b = 1.380649e-23
    temperature = 300.0
    bound = k_b * temperature * np.log(2.0)

    assert bound == pytest.approx(2.870978885078724e-21)


def test_linear_state_space_example_is_asymptotically_stable():
    matrix = np.array([[-0.45, -1.10], [1.00, -0.35]])
    eigenvalues = np.linalg.eigvals(matrix)

    assert np.all(eigenvalues.real < 0.0)
    assert eigenvalues.real[0] == pytest.approx(-0.4)


def test_markov_example_has_declared_subdominant_eigenvalue():
    transition = np.array([[0.92, 0.08], [0.18, 0.82]])
    eigenvalues = sorted(np.abs(np.linalg.eigvals(transition)))

    assert eigenvalues[-1] == pytest.approx(1.0)
    assert eigenvalues[-2] == pytest.approx(0.74)


def test_p17_total_variation_contraction_example():
    first = {"a": 0.8, "b": 0.2, "c": 0.0, "d": 0.0}
    second = {"a": 0.2, "b": 0.8, "c": 0.0, "d": 0.0}
    coarse_map = {"a": "x", "b": "x", "c": "y", "d": "y"}

    fine, coarse = pushforward_tv_pair(first, second, coarse_map)

    assert fine == pytest.approx(0.6)
    assert coarse == pytest.approx(0.0)
    assert coarse <= fine


def test_p18_exact_family_sufficiency_example():
    coarse_map = {"a0": "A", "a1": "A", "b0": "B", "b1": "B"}
    decoder = {
        "A": {"a0": 0.7, "a1": 0.3},
        "B": {"b0": 0.2, "b1": 0.8},
    }
    family = {
        "low": {"a0": 0.07, "a1": 0.03, "b0": 0.18, "b1": 0.72},
        "mid": {"a0": 0.28, "a1": 0.12, "b0": 0.12, "b1": 0.48},
        "high": {"a0": 0.63, "a1": 0.27, "b0": 0.02, "b1": 0.08},
    }

    certificate = scale_separation_certificate(family, coarse_map, decoder)

    assert certificate.reconstruction_defect == pytest.approx(0.0, abs=1e-12)
    assert certificate.coarse_min_separation == pytest.approx(
        certificate.fine_min_separation
    )
    assert certificate.certified_identifiable


def test_sample_complexity_has_inverse_square_gap_scaling():
    k = 8
    n_p = 5
    n_pi = 6
    alpha = 0.05

    def requirement(gamma):
        return (
            8.0
            * k**2
            / gamma**2
            * np.log(2.0 * n_p * n_pi * k / alpha)
        )

    assert requirement(0.2) == pytest.approx(requirement(0.1) / 4.0)
    assert requirement(0.4) == pytest.approx(requirement(0.2) / 4.0)
