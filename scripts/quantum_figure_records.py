from __future__ import annotations

import json
from collections.abc import Callable
from pathlib import Path
from typing import Any

READING_GUIDES: dict[str, str] = {
    "qm01_free_gaussian_wavepacket.svg": (
        "The horizontal axis is position and the plotted profiles are the position-probability density at successive times. "
        "Compare the width and peak height of the profiles: free evolution preserves total probability while the packet broadens and its peak decreases."
    ),
    "qm02_infinite_well_eigenstates.svg": (
        "Read position from 0 to L along the horizontal axis and compare the stationary eigenfunctions by mode number n. "
        "Each higher n adds nodes inside the well, while the associated energy increases as n squared; the wavefunction vanishes at both walls."
    ),
    "qm03_double_slit_interference.svg": (
        "Read detector angle or screen coordinate horizontally and intensity vertically. "
        "The rapid bright-dark fringe oscillations come from the two-slit phase difference, while the slower single-slit envelope limits their overall amplitude."
    ),
    "qm04_uncertainty_frontier.svg": (
        "The axes are position uncertainty and momentum uncertainty. The boundary curve marks Delta x Delta p = hbar/2; points on it are minimum-uncertainty Gaussian states. "
        "Moving along the boundary squeezes one uncertainty only by enlarging the conjugate uncertainty, and the physically allowed region lies on or above the bound."
    ),
    "qm05_bloch_sphere.svg": (
        "Treat the sphere as the geometric state space of one qubit. The north and south poles represent the computational-basis pure states, equatorial directions represent coherent superpositions, and the state vector gives the Bloch coordinates. "
        "Pure states lie on the surface; mixed states would lie inside the sphere rather than on it."
    ),
    "qm06_born_probabilities.svg": (
        "Follow the state angle theta and compare the two complementary outcome probabilities. "
        "As theta rotates the qubit from one basis pole toward the other, P(0) decreases as cos squared(theta/2) while P(1) increases as sin squared(theta/2); the two curves always sum to one."
    ),
    "qm07_rabi_oscillations.svg": (
        "Read time horizontally and excited-state population vertically. "
        "The repeated rise from zero toward one and return to zero is coherent population transfer under resonant driving; the oscillation period is fixed by the Rabi frequency Omega."
    ),
    "qm08_dephasing_coherence.svg": (
        "Read time horizontally and the magnitude of the off-diagonal density-matrix element vertically. "
        "Its exponential decay shows loss of phase coherence at rate Gamma; in the pure-dephasing model this decay does not imply population relaxation between the basis states."
    ),
    "qm09_purity_under_dephasing.svg": (
        "Read time horizontally and Tr(rho squared) vertically. "
        "The curve starts at purity one for the initial pure |+> state and approaches one half as phase information is erased, which is the purity of the corresponding fully dephased equal mixture."
    ),
    "qm10_von_neumann_entropy.svg": (
        "Read one eigenvalue p horizontally; the other is 1-p. The vertical axis is entropy in bits. "
        "Entropy is zero at p=0 or p=1 because the state is pure, and it reaches one bit at p=1/2 because a qubit with equal eigenvalues is maximally mixed."
    ),
    "qm11_entanglement_entropy.svg": (
        "Read the Schmidt mixing angle theta horizontally and the entropy of either one-qubit reduced state vertically. "
        "The entropy vanishes at product-state endpoints and reaches one bit when the two Schmidt weights are equal, marking maximal entanglement for this two-qubit family."
    ),
    "qm12_chsh_violation.svg": (
        "Read the plotted Bell-correlation parameter against the indicated measurement-setting angle or family. "
        "Use the horizontal classical threshold |S|=2 as the local-hidden-variable limit and the quantum ceiling 2 sqrt(2) as the Tsirelson bound; values above 2 are Bell-CHSH violations, not faster-than-light signals."
    ),
    "qm13_wigner_negativity.svg": (
        "The two axes are dimensionless phase-space position and momentum, and the surface or color field is the Wigner quasiprobability. "
        "The central region below zero is the key feature: unlike an ordinary classical probability density, the Wigner function of the first excited oscillator state can be negative."
    ),
    "qm14_hilbert_space_dimension.svg": (
        "Read qubit count N horizontally and state-space dimension vertically. "
        "Each added qubit doubles the tensor-product dimension, so the plotted growth follows 2^N rather than a linear law; the figure concerns representation size, not computational hardness by itself."
    ),
    "qm15_trace_distance_contraction.svg": (
        "Read depolarizing-noise strength p horizontally and trace distance between the two output states vertically. "
        "The distance shrinks by the factor 1-p, so stronger noise makes the states operationally less distinguishable; the curve visualizes data-processing contraction under this channel."
    ),
    "qm16_fidelity_trace_distance.svg": (
        "Read the projective angle between two pure states horizontally and compare fidelity with trace distance vertically. "
        "As the states separate, fidelity falls while trace distance rises according to D=sqrt(1-F); the two quantities encode complementary notions of similarity and distinguishability."
    ),
    "qm17_quantum_zeno_survival.svg": (
        "Read the number or frequency of ideal survival measurements together with the plotted survival probability. "
        "For a fixed total evolution time, increasing the number of projective checks drives the ideal survival probability upward, illustrating suppression of coherent departure from the initial state in the Zeno limit."
    ),
    "qm18_reduced_density_spectrum.svg": (
        "Read the Schmidt parameter or angle and track the two eigenvalues of the reduced density matrix. "
        "They remain nonnegative and sum to one; they are unequal near a product state and become equal at maximal entanglement, showing how a globally pure bipartite state can look mixed locally."
    ),
}


TAKEAWAYS: dict[str, str] = {
    "qm01_free_gaussian_wavepacket.svg": "Unitary free-particle evolution can spread a localized quantum state without destroying normalization.",
    "qm02_infinite_well_eigenstates.svg": "Confining boundary conditions produce discrete stationary modes and an n-squared energy spectrum.",
    "qm03_double_slit_interference.svg": "Superposed amplitudes generate interference, while diffraction controls the envelope of observable intensity.",
    "qm04_uncertainty_frontier.svg": "Squeezing redistributes conjugate uncertainty; it does not evade the Heisenberg product bound.",
    "qm05_bloch_sphere.svg": "A qubit state has a compact geometric representation in which purity corresponds to distance from the sphere center.",
    "qm06_born_probabilities.svg": "Quantum measurement probabilities arise from squared projection amplitudes and obey normalization.",
    "qm07_rabi_oscillations.svg": "Coherent driving can reversibly transfer population between two quantum levels.",
    "qm08_dephasing_coherence.svg": "Pure dephasing removes phase coherence even when basis-state populations are unchanged.",
    "qm09_purity_under_dephasing.svg": "Dephasing converts the chosen pure superposition into a mixed state and lowers purity toward one half.",
    "qm10_von_neumann_entropy.svg": "For a qubit, spectral balance maximizes von Neumann entropy and spectral certainty minimizes it.",
    "qm11_entanglement_entropy.svg": "For a globally pure bipartite state, reduced-state entropy quantifies entanglement across the partition.",
    "qm12_chsh_violation.svg": "Quantum correlations can exceed the local-hidden-variable CHSH bound while remaining compatible with no-signalling.",
    "qm13_wigner_negativity.svg": "Negative Wigner quasiprobability is a standard signature of nonclassical phase-space structure.",
    "qm14_hilbert_space_dimension.svg": "Tensor-product state spaces grow exponentially with qubit count.",
    "qm15_trace_distance_contraction.svg": "A noisy quantum channel cannot increase the distinguishability of this state pair and here contracts it exactly by 1-p.",
    "qm16_fidelity_trace_distance.svg": "For pure states, fidelity and trace distance are linked exactly and move in opposite directions with state separation.",
    "qm17_quantum_zeno_survival.svg": "In the ideal projective model, sufficiently frequent interrogation can suppress coherent transitions.",
    "qm18_reduced_density_spectrum.svg": "Partial trace can turn global purity into local mixedness when the global state is entangled.",
}


BOUNDARY = (
    "This is a standard quantum-mechanics or quantum-information figure. It does not show that consciousness is quantum, "
    "that consciousness causes wave-function collapse, that quantum mechanics is incomplete, or that consciousness is an additional physical dimension."
)


def _plain(text: str) -> str:
    return " ".join(str(text).replace("`", "").split())


def load_manifest(root: Path) -> dict[str, Any]:
    path = root / "docs" / "figures" / "quantum" / "quantum_figure_manifest.json"
    return json.loads(path.read_text(encoding="utf-8"))


def build_quantum_records(
    root: Path,
    figure_record_type: type,
    plain: Callable[[str], str] | None = None,
) -> dict[str, Any]:
    normalize = plain or _plain
    manifest = load_manifest(root)
    records: dict[str, Any] = {}
    for item in manifest["figures"]:
        filename = item["file"]
        guide = READING_GUIDES[filename]
        takeaway = TAKEAWAYS[filename]
        records[f"docs/figures/quantum/{filename}"] = figure_record_type(
            title=normalize(item["title"]),
            description=(
                f"What this figure shows: {normalize(item['fact'])} "
                f"Governing relation: {normalize(item['equation'])}. "
                f"How to read it: {guide} "
                f"Main takeaway: {takeaway}"
            ),
            status=f"{normalize(item['status'])}. {BOUNDARY}",
        )
    return records


def write_quantum_visual_guide(root: Path) -> None:
    manifest = load_manifest(root)
    lines = [
        "# Quantum Figure Visual Guide",
        "",
        "This page is the direct visual companion to the [Quantum Foundations and the Physical-to-Experiential Completeness Test](quantum_foundations_and_bridge_test.md). Every quantum figure is shown with its governing relation, a literal reading guide, the permitted takeaway, and an explicit scientific boundary. A reader should not need to infer the meaning of a curve, surface, threshold, or state-space diagram from appearance alone.",
        "",
        f"> **Scientific boundary.** {manifest['scientific_boundary']}",
        "",
    ]

    for index, item in enumerate(manifest["figures"], start=1):
        filename = item["file"]
        lines.extend(
            [
                f"## QM{index:02d}. {item['title']}",
                "",
                f"![QM{index:02d}. {item['title']}](figures/quantum/{filename})",
                "",
                f"**Figure QM{index:02d}. What this figure shows.** {item['fact']}",
                "",
                f"**Governing relation.** `{item['equation']}`",
                "",
                f"**How to read it.** {READING_GUIDES[filename]}",
                "",
                f"**Main takeaway.** {TAKEAWAYS[filename]}",
                "",
                f"**Scientific status.** {item['status']}. {BOUNDARY}",
                "",
                "**Formal context.** [Quantum foundations and bridge test](quantum_foundations_and_bridge_test.md) · [Foundational physics/mathematics bibliography](foundational_physics_mathematics_bibliography.md) · [Complete figure catalog](figure_catalog.md)",
                "",
            ]
        )

    (root / "docs" / "quantum_visual_guide.md").write_text("\n".join(lines), encoding="utf-8")

    foundations = root / "docs" / "quantum_foundations_and_bridge_test.md"
    text = foundations.read_text(encoding="utf-8")
    marker = (
        "This document formalizes the role of quantum mechanics in the Mathematical Consciousness Bridge program. Quantum theory is treated as part of the physical description to be tested for sufficiency. It is **not** assumed that consciousness is quantum, that consciousness causes wave-function collapse, or that quantum mechanics is incomplete.\n"
    )
    addition = (
        "\nFor a figure-by-figure visual explanation of the quantum background, including the governing equation, how to read each plot, the exact takeaway, and the scientific boundary, use the [Quantum Figure Visual Guide](quantum_visual_guide.md).\n"
    )
    if addition.strip() not in text:
        if marker not in text:
            raise RuntimeError("quantum-foundations scope marker not found")
        text = text.replace(marker, marker + addition, 1)
        foundations.write_text(text, encoding="utf-8")
