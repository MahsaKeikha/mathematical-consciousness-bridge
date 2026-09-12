from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import Any

RECORDS: dict[str, dict[str, str]] = {
    "docs/figures/p55_pruning_aware_switching_monotonicity.svg": {
        "title": "P55 pruning-aware metric switching-cost monotonicity",
        "description": (
            "What this figure shows: P55 proves deterministic monotonicity of the exact P54 execution optimum when a valid sequential update makes every residual demand weakly smaller, while acquisition cost, switching metric, and setup start remain fixed. The metric shortcutting argument makes the optimal route value nonincreasing under support deletion, so total cost release decomposes exactly into nonnegative acquisition release plus nonnegative route release. "
            "How to read it: the three upper cards specify the fixed comparison regime, the earlier residual state, and the later componentwise-smaller state. Their attached arrows feed the central support-deletion theorem and exact cost-release identity. The lower cards separate the support-preserving case, the computable shortcut lower certificate, and the sequential experimental implication. "
            "Main takeaway: every released residual sample saves its acquisition cost, while deleting a preparation from the positive-demand support can add further switching savings. This monotonicity depends on a fixed metric and fixed start."
        ),
        "status": (
            "Deterministic scheduling theorem conditional on valid residual demands and valid pruning decisions. It does not justify pruning, prove statistical minimaxity of the underlying thresholds, identify a route or graph quantity with consciousness, establish a physical-to-experiential bridge, or imply quantum incompleteness."
        ),
    },
    "docs/figures/p56_moving_start_metric_reoptimization_stability.svg": {
        "title": "P56 moving-start metric reoptimization stability",
        "description": (
            "What this figure shows: P56 controls exact P54 reoptimization when the apparatus or setup start moves from s to s-prime while one declared finite switching metric remains fixed. The exact route optimum is one-Lipschitz in the start state, and the coefficient one is sharp. "
            "How to read it: the three upper cards specify the fixed metric geometry and the two alternative start states for the same active support. Their attached arrows feed the central route-reuse proof and one-Lipschitz theorem. The lower cards then transfer the bound to fixed residual demand, combine it with the P55 fixed-start release after componentwise residual decrease, and state a sufficient strict-decrease certificate. "
            "Main takeaway: start motion can erase at most one metric displacement worth of the saving certified by P55. Therefore a fixed-start release larger than c(s,s-prime) guarantees that the new exact total cost remains strictly lower, while failure of that sufficient inequality is inconclusive."
        ),
        "status": (
            "Deterministic one-metric scheduling perturbation theorem. It assumes the same valid finite switching metric before and after reoptimization. It does not validate pruning, establish statistical minimaxity of residual thresholds, identify a scheduling quantity with consciousness, establish a physical-to-experiential bridge, or imply quantum incompleteness."
        ),
    },
    "docs/figures/p57_switching_metric_perturbation.svg": {
        "title": "P57 deterministic switching-metric perturbation stability",
        "description": (
            "What this figure shows: P57 controls exact P54 reoptimization when residual demand, setup origin, and a declared finite switching metric all change. The theorem assumes two valid finite metrics on one common relevant point set and measures their uniform difference by delta. "
            "How to read it: the three upper input cards specify the old exact state, the new exact state, and the sharp q-times-delta stability bound for changing only the metric at a fixed support and start. All three feed the central P55-P56-P57 certificate, where the fixed-geometry release is reduced by the smaller of two valid start-motion-plus-metric-drift penalties. The lower cards explain the sharp route-edge factor, the sufficient strict-decrease condition, and a route-reuse upper bound that can be tighter than the uniform perturbation penalty. "
            "Main takeaway: if the fixed-geometry release exceeds the certified perturbation penalty then the new exact total cost is strictly smaller, but the converse is not claimed because the penalty is worst-case."
        ),
        "status": (
            "Deterministic robustness theorem for operational scheduling under two declared finite metrics. It does not estimate a metric from data, validate pruning, prove minimax adaptive efficiency, identify a metric or route quantity with consciousness, establish a physical-to-experiential bridge, or imply quantum incompleteness."
        ),
    },
    "docs/figures/p58_finite_data_metric_uncertainty.svg": {
        "title": "P58 finite-data switching-metric uncertainty and robust routing",
        "description": (
            "What this figure shows: P58 turns noisy pairwise transition measurements into a simultaneous confidence envelope for an unknown true switching metric and propagates that envelope through the exact P54 block-route family. The empirical pairwise center is allowed to violate triangle inequalities; the true metric property remains a declared physical/model assumption. "
            "How to read it: move left to right across the upper row from the bounded pairwise observation model, to the simultaneous Hoeffding event, to lower and upper transition envelopes. The center theorem panel brackets the unknown exact P54 route optimum with lower and upper envelope optima computed over the same fixed route family. Follow the three lower branches to the robust-route regret certificate, the strict comparison of two reoptimization states, and the common-radius sample-size certificate. "
            "Main takeaway: finite noisy transition data can support valid route-level uncertainty and regret statements without treating the empirical cost table as an exact metric. The common-sample inequality is sufficient, not a minimax lower bound, and adaptive pair selection requires separate statistical accounting."
        ),
        "status": (
            "Finite-data scheduling and confidence-envelope theorem under the declared bounded pairwise observation model. It does not validate the transition-cost measurement model, infer metric truth from noisy observations, justify unrestricted adaptive pruning, identify a scheduling variable with consciousness, establish a physical-to-experiential bridge, or imply quantum incompleteness."
        ),
    },
    "docs/figures/p59_optimal_transition_calibration.svg": {
        "title": "P59 exact continuous transition-calibration allocation",
        "description": (
            "What this figure shows: P59 solves one declared continuous calibration resource-allocation problem exactly. P58 supplies an inverse-square-root uncertainty law for each calibrated transition, a predeclared positive sensitivity weight converts that uncertainty into the chosen separable route surrogate, and a fixed continuous budget must be divided across the edges. Strict convexity then gives a unique two-thirds-power allocation, the exact minimum surrogate uncertainty, and an exact target-budget threshold. "
            "How to read it: read the three upper cards as the declared ingredients: P58 uncertainty scale, scientific sensitivity weight, and continuous total budget. Their attached arrows feed the central optimization theorem. From that theorem, follow the three lower branches to the two-thirds allocation law, the necessary-and-sufficient target-budget condition, and the continuous-to-integer handoff to P60 and P61. "
            "Main takeaway: P59 is an exact continuous optimum for the stated separable surrogate; the weights must be justified independently and fractional allocations require a separate integer implementation."
        ),
        "status": (
            "Continuous convex resource-allocation theorem for experimental calibration. It does not establish that the declared weights are uniquely scientifically correct, solve the full minimax robust-routing design problem, identify a physical quantity with consciousness, establish a physical-to-experiential bridge, or imply quantum incompleteness."
        ),
    },
    "docs/figures/p60_integer_transition_calibration.svg": {
        "title": "P60 hard-budget integer rounding with certified overhead",
        "description": (
            "What this figure shows: P60 converts the exact P59 continuous unit-cost calibration design into executable whole-measurement counts while respecting a hard integer budget. It solves P59 at the deliberately reduced budget N0 = B - m, rounds every edge count upward, and certifies both feasibility and the resulting uncertainty overhead relative to the full-budget continuous optimum. "
            "How to read it: move left to right across the top row from the hard budget to the reduced P59 allocation and then to ceiling rounding. The center theorem panel combines the budget-feasibility proof with the deterministic uncertainty guarantee. Follow the three lower branches to the full-budget multiplicative overhead, the sufficient target-uncertainty budget, and the distinction between this constructive guarantee and P61 exact integer optimality. "
            "Main takeaway: P60 gives a closed-form auditable integer construction with an explicit worst-case overhead; it is conservative and is not claimed to be the exact integer optimum."
        ),
        "status": (
            "Deterministic rounding and experimental-budget theorem for the declared calibration surrogate. It does not validate the observation model or sensitivity weights, identify a transition metric with consciousness, establish a physical-to-experiential bridge, or imply quantum incompleteness."
        ),
    },
    "docs/figures/p61_exact_integer_transition_calibration.svg": {
        "title": "P61 exact unit-cost integer transition calibration",
        "description": (
            "What this figure shows: P61 solves the declared equal-unit-cost whole-measurement calibration problem exactly. It starts from one mandatory measurement per calibrated edge, assigns each remaining unit to the edge with the largest current marginal reduction in the separable uncertainty objective, and proves global optimality from strictly diminishing per-edge gains and prefix feasibility. "
            "How to read it: move left to right across the top row from the mandatory baseline to the current marginal gain and the greedy allocation step. The center theorem panel explains why diminishing gain sequences make that rule exact. Follow the three lower branches to the checkable exchange certificate, the exact global optimum and tie behavior, and the priority-queue complexity. "
            "Main takeaway: P61 closes the equal-unit-cost integer allocation problem for the declared separable surrogate; it does not extend the same greedy proof to heterogeneous costs."
        ),
        "status": (
            "Exact discrete resource-allocation theorem for experimental calibration. It does not validate the full robust-route model, identify a calibration quantity with consciousness, establish a physical-to-experiential bridge, or imply quantum incompleteness."
        ),
    },
    "docs/figures/p62_heterogeneous_cost_transition_calibration.svg": {
        "title": "P62 exact heterogeneous-cost continuous calibration",
        "description": (
            "What this figure shows: P62 solves the declared separable inverse-square-root calibration surrogate exactly in the continuous domain when each transition edge has its own positive per-observation cost. "
            "How to read it: the two upper input cards feed the central constrained problem, which then feeds the unique strict-convexity optimum. From the theorem panel, follow the three lower branches to the optimal measurement-count law, the distinct optimal budget-share law, and the exact target-budget threshold. "
            "Main takeaway: expensive edges receive fewer observations all else equal, yet can still consume more total budget because sample count and budget share scale with different powers of cost. P62 is a continuous theorem; heterogeneous integer counts are a separate P63 problem."
        ),
        "status": (
            "Continuous resource-allocation theorem for the declared calibration surrogate. It does not validate the full robust-route uncertainty model, identify an operational variable with consciousness, establish a physical-to-experiential bridge, or imply quantum incompleteness."
        ),
    },
    "docs/figures/p63_exact_heterogeneous_integer_calibration.svg": {
        "title": "P63 exact heterogeneous-cost integer calibration",
        "description": (
            "What this figure shows: P63 solves the declared heterogeneous-cost whole-measurement calibration problem exactly when transition costs and the total budget are positive integers. It replaces the equal-cost P61 greedy argument with an exact-spend Bellman dynamic program because unequal costs destroy the exchange proof behind the equal-unit rule. "
            "How to read it: move left to right across the top row from the failure of the P61 greedy argument to the exact integer problem and its exact-spend Bellman state. The two attached center arrows feed the exact Bellman recurrence and final hard-budget optimum. From that theorem panel, follow the three lower branches to exact gcd cost compression, pseudo-polynomial complexity, and the P62 continuous lower bound. "
            "Main takeaway: P63 is an exact unrestricted integer solver for the declared integer-cost separable calibration problem; its straightforward running time is pseudo-polynomial in the compressed numeric budget, which by itself is not an NP-hardness claim."
        ),
        "status": (
            "Discrete optimization theorem for the declared calibration surrogate. It does not validate the uncertainty model as an experiential law, identify a calibration variable with consciousness, establish a physical-to-experiential bridge, or imply quantum incompleteness."
        ),
    },
    "docs/figures/p64_fast_heterogeneous_integer_approximation.svg": {
        "title": "P64 fast certified heterogeneous-cost integer approximation",
        "description": (
            "What this figure shows: P64 gives a scalable certified integer approximation by flooring the exact P62 continuous heterogeneous-cost allocation, but only in the regime where every continuous count is at least one. "
            "How to read it: move left to right across the top row from the P62 continuous solution to the explicit P64 applicability gate and then to the feasible integer floor. The center panel defines the instance-specific floor ratios and transfers the continuous optimum into a certified multiplicative bound relative to the exact P63 integer optimum. The lower panels show the simpler uniform guarantee and the scalability/regime boundary. "
            "Main takeaway: P64 is a fast approximation theorem, not an exact-integer theorem; when its at-least-one gate fails, P65 provides the baseline-safe continuous route and P63 remains the unrestricted exact integer solver."
        ),
        "status": (
            "Calibration resource-allocation theorem for the declared separable surrogate. It does not identify a calibration variable with consciousness, establish a physical-to-experiential bridge, or imply quantum incompleteness."
        ),
    },
    "docs/figures/p65_lower_bounded_heterogeneous_calibration.svg": {
        "title": "P65 lower-bounded heterogeneous calibration",
        "description": (
            "What this figure shows: P65 removes the regime restriction in P64 by solving the heterogeneous-cost continuous allocation problem with the mandatory one-observation lower bound built in before rounding. "
            "How to read it: move left to right across the top row from the P64 failure mode to the constrained P65 problem and its thresholded active set. The two center arrows then feed the exact lower-bounded water-filling theorem. From that theorem, follow the two lower arrows to the baseline-safe integer floor and its certified objective-quality bound. "
            "Main takeaway: the continuous P65 allocation is uniquely optimal for the declared lower-bounded problem; flooring it is always feasible and is certified within an instance-specific factor no worse than square-root two, but the floor is not claimed to be the exact unrestricted integer optimum."
        ),
        "status": (
            "Calibration resource-allocation theorem for the declared separable surrogate. It does not identify a calibration variable with consciousness, establish a physical-to-experiential bridge, or imply that quantum mechanics is incomplete."
        ),
    },
    "docs/figures/p66_residual_exact_calibration_augmentation.svg": {
        "title": "P66 residual-exact augmentation after P65 flooring",
        "description": (
            "What this figure shows: P66 starts from the exact lower-bounded continuous P65 optimum, floors it to an executable baseline-safe integer design, proves that the leftover budget R is strictly smaller than one baseline cost B0, and solves the best floor-dominating integer augmentation exactly by dynamic programming on that residual budget. "
            "How to read it: move left to right across the three upper cards from the P65 optimum to the residual-budget identity and then to the exact residual dynamic program. From the DP card, follow the two attached lower branches: the left panel records objective and approximation improvements over the P65 floor; the right panel records why the computation stays localized to the residual scale. "
            "Main takeaway: P66 is globally exact only inside the class k greater than or equal to the P65 floor f; it does not replace P63 as the unrestricted exact integer solver."
        ),
        "status": (
            "Discrete resource-allocation theorem for the declared calibration surrogate. It is not a consciousness theorem, empirical consciousness result, physical-to-experiential bridge theorem, or quantum-ontology claim."
        ),
    },
    "docs/figures/theorem_roadmap.svg": {
        "title": "Theorem dependency map for P1-P31",
        "description": (
            "What this figure shows: the theorem roadmap for Propositions 1 through 31, with arrows encoding actual mathematical or scientific prerequisites rather than mere numerical sequence or vertical proximity. "
            "How to read it: follow the arrows, not just the page order. The central target-sufficiency lineage runs from P19 through P24. P25-P31 are physical-scale, aggregation, metric, and quotient branches whose prerequisites are shown explicitly by the connectors. An absent arrow means that the figure is not asserting a prerequisite. "
            "Main takeaway: proposition numbering records development order, whereas the arrow topology records dependency structure. Later P61-P70 and P71-P80 are separate continuations documented in the theorem index."
        ),
        "status": (
            "Research-orientation figure. It summarizes dependency structure among the displayed theorem branches; it does not add a theorem, empirical consciousness result, or physical-to-experiential bridge claim."
        ),
    },
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
    "docs/figures/p68_lagrangian_optimality_gap.svg": {
        "title": "P68 Lagrangian lower bounds and quantitative integer optimality gaps",
        "description": (
            "What this figure shows: P68 gives a rigorous quality certificate for any feasible integer calibration candidate even when P67 does not prove exact optimality. The top row starts from a feasible candidate, chooses any positive Lagrange multiplier, and solves every one-edge integer Lagrangian subproblem exactly by strict convexity. Those exact edge minima assemble the weak-duality lower bound q(lambda), which is no larger than the unrestricted P63 optimum. Comparing that lower bound with the candidate objective yields a certified additive optimality-gap upper bound and, only when q(lambda) is positive, a multiplicative factor bound. "
            "How to read it: follow the attached arrows through stages 1 to 4, then split into the additive and multiplicative certificates. The P67 band shows the zero-gap special case: tight budget plus one common edgewise multiplier makes q(lambda), the candidate objective, and the unrestricted optimum coincide. "
            "Main takeaway: every positive multiplier gives a valid lower bound; multiplier quality affects tightness, not validity, and no dual-maximizer claim is needed for P68."
        ),
        "status": (
            "Optimization-certificate figure for the declared heterogeneous-cost separable calibration surrogate. It is not a consciousness theorem, does not validate the surrogate as an experiential law, and the physical-to-experiential bridge remains open."
        ),
    },
    "docs/figures/p71_target_provenance_noncircularity.svg": {
        "title": "P71 target-provenance non-circularity",
        "description": (
            "What this figure shows: P71 separates mathematical factorization from scientific target provenance. The left panel shows a descriptor-derived target E=h(T), for which the exact bridge and zero conditional residual are guaranteed by construction. The right panel uses the repository's synthetic four-state example to show that a separately declared target can create a same-descriptor/different-target collision and a positive conditional residual. The lower comparison states the provenance limitation: a zero residual observed from values alone cannot establish that the target was independently specified. "
            "How to read it: read the left and right panels as contrasting target-construction protocols, follow only the attached labeled arrows, then compare the two synthetic residual cards. "
            "Main takeaway: a target manufactured from the tested descriptor cannot serve as independent evidence that the same descriptor is sufficient for that target."
        ),
        "status": (
            "Proved target-provenance non-circularity theorem plus a synthetic finite example. The synthetic target is not asserted to represent experience; passing P71 is necessary but not sufficient for a serious physical-to-experiential bridge test."
        ),
    },
    "docs/figures/p72_target_measurement_channel_robustness.svg": {
        "title": "P72 target-measurement channel robustness",
        "description": (
            "What this figure shows: P72 separates an independently declared latent target from the noisy process used to observe it. The top-left panel gives conditional data processing, the top-right panel shows that measurement noise can erase a real witness, the lower-left panel gives the binary symmetric channel stability factor, and the lower-right panel transfers an observed finite-sample witness back to the latent target. "
            "How to read it: read each panel as a distinct theorem component; inside panel A, follow the attached state-to-target-to-observation arrows. "
            "Main takeaway: nondifferential target noise can weaken or erase evidence but cannot create a positive population residual from a screened-off latent target."
        ),
        "status": (
            "Target-measurement robustness theorem figure. The latent target is declared for testing and is not an assumed definition of consciousness; channel validity and the physical-to-experiential bridge remain separate obligations."
        ),
    },
    "docs/figures/p73_target_channel_identifiability.svg": {
        "title": "P73 target-channel identifiability",
        "description": (
            "What this figure shows: P73 identifies the parameters of one declared nondegenerate three-view binary latent target-channel model at the population level, up to a common latent-label swap. The upper-left panel defines the model, the upper-right panel gives the observable moment inversion, the lower-left panel shows that P72 stability becomes identifiable, and the lower-right panel gives a constructive two-view non-identifiability example. "
            "How to read it: follow the attached latent-to-view connectors in panel A, then move clockwise through recovery, stability, and the two-view boundary. "
            "Main takeaway: three suitable views can identify this declared measurement model, but two views generally cannot identify individual reliabilities."
        ),
        "status": (
            "Population identifiability theorem figure. Statistical identification does not identify the latent class with consciousness, validate the model assumptions, or solve the physical-to-experiential bridge."
        ),
    },
    "docs/figures/p74_finite_sample_target_channel_recovery.svg": {
        "title": "P74 finite-sample target-channel recovery",
        "description": (
            "What this figure shows: P74 converts one finite-sample confidence event for the observed eight-cell law into a guarded version of the P73 target-channel inversion. "
            "How to read it: follow the four attached top-row stages from observed data to the shared confidence event, then to the nondegeneracy gate, and finally to certified output. The lower-left panel shows the interval inversion formulas; the lower-right panel states what successful certification and gate failure mean. "
            "Main takeaway: recovery is reported only when finite-sample uncertainty stays away from the covariance singularity. Gate failure means not certified by the current data, not population degeneracy."
        ),
        "status": (
            "Finite-sample certification theorem figure conditional on the P73 model. It does not validate conditional independence, identify the latent state with consciousness, or close the physical-to-experiential bridge."
        ),
    },
    "docs/figures/p75_target_model_adequacy_overidentification.svg": {
        "title": "P75 target-model adequacy and four-view overidentification",
        "description": (
            "What this figure shows: P75 separates parameter identifiability from model adequacy. Three binary views provide seven observable degrees of freedom for seven latent-model parameters and are therefore generically just-identified. A fourth binary view provides fifteen observable degrees of freedom for nine parameters, creating six overidentifying degrees of freedom and independent observable restrictions. "
            "How to read it: compare the two upper panels first, then follow the attached arrows into the lower adequacy panel. The three lower cards list covariance-tetrad, cross-triple, and fourth-moment obligations; the bottom audit band states the full-law reconstruction check. "
            "Main takeaway: the fourth view makes the declared target model falsifiable beyond mere parameter fitting."
        ),
        "status": (
            "Theorem-summary figure for the declared P75 latent model. Passing means compatibility with that model, not proof of truth and not identification of the latent state with consciousness."
        ),
    },
    "docs/figures/p76_finite_sample_target_model_adequacy.svg": {
        "title": "P76 finite-sample target-model adequacy rejection",
        "description": (
            "What this figure shows: P76 carries one simultaneous sixteen-cell confidence event into denominator-free intervals for the P75 adequacy constraints. "
            "How to read it: follow the four attached top-row stages from observed data through the shared confidence event and moment box into the P75 polynomial intervals. Then compare the two lower outcomes: excluding zero from any required interval certifies incompatibility, while retaining zero in every tracked interval means only that the current certificate does not reject. "
            "Main takeaway: P76 is a one-sided finite-sample falsification procedure, not a model-acceptance rule."
        ),
        "status": (
            "Finite-sample theorem figure. It does not prove conditional independence, validate latent semantics, identify the latent state with consciousness, or close the physical-to-experiential bridge."
        ),
    },
    "docs/figures/p77_full_law_model_set_separation.svg": {
        "title": "P77 finite-sample full-law model-set separation",
        "description": (
            "What this figure shows: P77 strengthens the P76 finite-sample adequacy audit from selected necessary polynomial constraints to separation of the entire simultaneous confidence region from the entire declared model set. The left panel summarizes the P76 constraint route and its limitation; the right panel shows the full-law geometric separation condition. "
            "How to read it: move from the P76 panel through the attached stronger-audit arrow to the P77 panel, then use the lower optimization-direction band to distinguish certified lower bounds from ordinary best-fit upper bounds. "
            "Main takeaway: full-law rejection requires a sound lower bound proving that every admissible model is farther away than the sampling radius; a candidate best fit alone cannot certify rejection."
        ),
        "status": (
            "Finite-sample model-set separation theorem figure. Non-rejection is not model acceptance; the theorem does not identify the latent state with consciousness, and the physical-to-experiential bridge remains open."
        ),
    },
    "docs/figures/p78_certified_continuous_model_separation.svg": {
        "title": "P78 certified continuous model separation",
        "description": (
            "What this figure shows: P78 turns the P77 full-law rejection requirement into a certified global optimization procedure for the continuous nine-parameter P75 model. Adaptive boxes cover the full parameter cube, exact multi-affine cell enclosures produce boxwise lower bounds, and the minimum active-box bound gives a global lower bound while any explicit admissible parameter gives an upper bound. "
            "How to read it: follow the attached stage arrows from parameter partitioning to exact box certification to the final global distance bracket, then use the P77 handoff only when the certified lower bound strictly exceeds a valid sampling-radius upper bound. "
            "Main takeaway: a best fit supplies only the upper side of the distance bracket; a formal rejection requires the certified lower side."
        ),
        "status": (
            "Exact-rational continuous-family optimization certificate under the declared P75 model. Non-rejection is not model acceptance, and the physical-to-experiential bridge remains open."
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
