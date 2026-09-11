from __future__ import annotations

from pathlib import Path
from typing import Any, Callable


RECORDS: dict[str, dict[str, str]] = {
    "docs/figures/fundamental_theory_consciousness_map.svg": {
        "title": "Fundamental Theory to Consciousness map",
        "description": (
            "What this figure shows: the logical gap between a complete declared physical theory, its physical equivalence classes and operational predictions, and an independently defined experiential or target structure. "
            "How to read it: move from fundamental physical law to the physical state/observable layer and then to equivalence classes induced by the chosen physical descriptor. The final arrow toward target equivalence classes is intentionally a separate bridge requirement, not something supplied automatically by the physical equations. "
            "Main takeaway: physical completeness and operational predictability do not by themselves establish experiential completeness; a justified, testable physical-to-target map is still required."
        ),
        "status": (
            "Research-architecture figure. It formalizes a sufficiency question and an open bridge requirement; it does not assert a fifth spatial dimension, nonphysical substance, simulation ontology, or failure of quantum mechanics."
        ),
    },
    "docs/figures/physics_mathematics_atlas.svg": {
        "title": "Physics and mathematics atlas for consciousness research",
        "description": (
            "What this figure shows: a left-to-right and top-to-bottom map of the physical and mathematical toolkits used in the research, including dynamical systems, information geometry, causal intervention structure, thermodynamics, integration/segregation measures, neural dynamics, empirical consciousness measures, and the still-separate bridge problem. "
            "How to read it: treat each numbered box as a distinct scientific layer. Read the equations inside a box as representative formal objects for that layer, and read arrows only as research dependencies or interfaces, not as equivalences between physical quantities and experience. "
            "Main takeaway: the repository combines several mature physical/mathematical frameworks, but none of those frameworks by itself supplies the physical-to-experiential map."
        ),
        "status": (
            "Architecture/synthesis figure. It organizes established mathematical and physical ingredients plus open research interfaces; it is not an empirical consciousness result and does not assert that any displayed equation defines consciousness."
        ),
    },
    "docs/figures/proposition_32_delay_quotient.svg": {
        "title": "Proposition 32 delay-quotient compatibility",
        "description": (
            "What this figure shows: fine-delay response laws on the left are grouped by a temporal quotient in the center and represented by coarse-delay response laws on the right. "
            "How to read it: follow each fine delay tau into its coarse fiber c. If two fine delays tau_0 and tau_1 map to the same fiber c_0, a unique coarse response Q^{u,c_0} exists only when their fine response laws agree; a separate fiber such as c_1 may carry a different response. Approximate compatibility is controlled by the within-fiber discrepancy eta_a. "
            "Main takeaway: temporal coarse-graining is representation-independent only when the response law is constant, or explicitly controlled, within every identified delay fiber."
        ),
        "status": (
            "Visual statement of Proposition 32's exact/approximate quotient-compatibility condition. The formal assumptions and proof are in the proposition record; the diagram is not an empirical consciousness measurement."
        ),
    },
    "docs/figures/spaceflight_extreme_environment_map.svg": {
        "title": "Spaceflight and extreme-environment relevance map",
        "description": (
            "What this figure shows: spaceflight hazards feed into measurable physical and behavioral observables, which can be analyzed with the repository's dynamical, temporal, interventional, and finite-error tools before asking whether a proposed consciousness-relevant marker remains stable or dissociates under stress. "
            "How to read it: move from the hazard box to observables, then to the mathematical research interface, and only then to the consciousness-science questions. The lower panels list falsifiable research questions and source roles. The arrow sequence is an experimental-design pipeline, not evidence that spaceflight variables are consciousness variables. "
            "Main takeaway: extreme environments are demanding validation settings for state monitoring and marker robustness, not a shortcut to a physical-to-experiential bridge."
        ),
        "status": (
            "Application/research-design map. It proposes how established spaceflight measurements can stress-test physical markers; it does not present new astronaut data or establish a consciousness bridge."
        ),
    },
    "docs/figures/state_space_dynamics_map.svg": {
        "title": "State-space dynamics, perturbations, and empirical regimes",
        "description": (
            "What this figure shows: a schematic two-coordinate measured state space containing several empirically motivated regimes, together with local dynamics, intervention-response geometry, spontaneous transitions, and a controlled perturbation. "
            "How to read it: the ellipses are illustrative regions in measured-variable space, not a universal scalar ordering of consciousness. Dashed arrows represent possible state transitions; the red perturbation arrow represents an intervention whose response can be compared with the stated response-distance formalism. Distances on the page are schematic unless separately measured. "
            "Main takeaway: measured dynamical regimes and their perturbational responses can be represented geometrically while remaining distinct from any claim about experiential identity."
        ),
        "status": (
            "Schematic state-space research figure. Region placement and geometry are illustrative, not fitted empirical boundaries and not a universal consciousness scale."
        ),
    },
    "docs/figures/thermodynamics_information_processing.svg": {
        "title": "Thermodynamics of information processing and consciousness research",
        "description": (
            "What this figure shows: a chain from stochastic physical dynamics through information-bearing states, Landauer erasure cost, and nonequilibrium entropy production, followed by measurable intervention-response and thermodynamic quantities and a separate bridge question. "
            "How to read it: the top row summarizes standard physical/information-theoretic relations; the lower measurement layer shows quantities that can be operationalized. Follow the arrows as dependencies between physical descriptions. The final bridge boundary means that energy, entropy, information, and causal-response structure constrain a physical substrate but do not automatically define experiential structure. "
            "Main takeaway: thermodynamic and information-theoretic quantities are rigorous physical observables and constraints, yet an additional justified mapping is still required before making experiential claims."
        ),
        "status": (
            "Physics-synthesis figure based on standard thermodynamics/information theory plus repository operational structure. It is not evidence that thermodynamic information equals consciousness."
        ),
    },
    "docs/figures/p79_certified_sampling_radius.svg": {
        "title": "P79 certified rational sampling-radius envelope",
        "description": (
            "What this figure shows: the one-sided exact-rational certification of the P77 finite-alphabet sampling radius and its safe comparison with the P78 continuous-model distance lower bound. "
            "How to read it: start with the exact statistical inputs, follow the positive atanh-series and integer-certified dyadic square-root steps to the certified upper radius, then compare that upper bound only against the P78 lower bound. A strict lower-bound-greater-than-upper-bound inequality certifies rejection; failure of that strict gate is inconclusive. "
            "Main takeaway: P79 removes unsafe floating-point rounding direction from the rejection handoff without changing the statistical model or turning non-rejection into model acceptance."
        ),
        "status": (
            "Numerical-certification theorem figure. It certifies an exact-rational upper bound on sampling uncertainty; it does not validate the P75 latent model or close the physical-to-experiential bridge."
        ),
    },
    "docs/figures/p80_simplex_coupled_model_separation.svg": {
        "title": "P80 simplex-coupled model separation",
        "description": (
            "What this figure shows: P80 tightens each P78 parameter-box relaxation by intersecting its exact coordinate intervals with probability normalization. The complete feasibility radius is the maximum of the coordinate-overlap radius r_box and the two normalization-crossing radii r_A and r_C. "
            "How to read it: move from the P78 box enclosure to the simplex-coupled set, then read L80(B)=max(r_box,r_A,r_C) as a certified lower bound that is never weaker than L78(B). At the rejection handoff, compare the P80 lower bound with the P79 certified upper sampling radius; rejection requires a strict separation. "
            "Main takeaway: simplex coupling strengthens continuous-family separation while preserving the one-sided logic of the P78-P79 certificate chain."
        ),
        "status": (
            "Exact-rational computational-certification theorem figure. It does not establish that the P75 latent variable is experiential, and non-rejection remains inconclusive; the physical-to-experiential bridge remains open."
        ),
    },
}


def build_special_conceptual_records(
    _root: Path,
    figure_record_type: type,
    plain: Callable[[str], str] | None = None,
) -> dict[str, Any]:
    normalize = plain or (lambda value: " ".join(value.split()))
    return {
        path: figure_record_type(
            title=normalize(record["title"]),
            description=normalize(record["description"]),
            status=normalize(record["status"]),
        )
        for path, record in RECORDS.items()
    }
