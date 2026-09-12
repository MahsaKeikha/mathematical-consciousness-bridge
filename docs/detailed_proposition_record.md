# Detailed proposition record

## Complete P1 to P81 chronology

This page preserves the proposition-by-proposition development history of the Mathematical Consciousness Bridge research program. It is intentionally separate from the main README so a first-time reader can follow the scientific argument without first learning the internal chronology of the project.

The proposition record is an audit trail, not a substitute for the scientific narrative. For dependency structure, see the [Theorem roadmap](theorem_roadmap.md). For topic-oriented navigation, see [Research navigation](research_navigation.md). For equation provenance and external references, see the [Equation and citation map](equation_and_citation_map.md).

The scientific status rule is strict throughout: a theorem is only a theorem under its declared assumptions, an implementation is not empirical evidence, a simulation is not an ontological result, and the physical-to-experiential bridge remains open unless separately established.

---

## Complete P1 to P81 chronology

Propositions **P1-P10** establish representation invariance, empirical theory identifiability, observational equivalence, discriminating experiment design, feature sufficiency, canonical bridge completeness, experimental recoverability, finite-error recovery, sample complexity, and robust protocol design.

**P11** introduces intervention-resolved causal structure as a structured physical candidate rather than a scalar. **P12-P13** prove constructive insufficiency and component irredundancy results. **P14-P15** formalize temporal continuation and finite-error temporal certification. **P16** gives an independent-composition null model and response-level coupling defect. **P17** proves total-variation contraction and exact refinement ambiguity under deterministic coarse-graining. **P18** proves a quantitative scale-sufficiency certificate based on approximate reconstruction.

**P19** proves exact deterministic and stochastic criteria for whether an independently defined target factors through a declared physical descriptor, together with a differential no-go test. **P20** converts the P19 stochastic population residual into an explicit finite-sample confidence certificate under a declared finite-alphabet IID model. **P21** proves how that residual behaves under nested physical-descriptor refinement. **P22** gives a simultaneous finite-sample certificate for an entire declared refinement chain from one shared confidence event. **P23** protects fixed-sample data-dependent descriptor selection. **P24** converts the fixed-sample result into an anytime-valid certificate with repeated-look and finite stopping-time validity.

**P25-P30** return to the P11 physical candidate and transport directed influence, partition irreducibility, response geometry, and the combined P11 structure through controlled node/state aggregation. **P31-P34** add intervention and delay quotients and assemble one complete operational scale declaration. **P35-P37** propagate approximate quotient ambiguity through directed influence, partition irreducibility, and the complete P11 structure.

**P38** specializes physical sufficiency to a tomographically complete finite-dimensional quantum state descriptor. **P39** converts the exact criterion into a finite-data model-set certificate. **P40** proves that finite sampled-state injectivity permits unrestricted lookup-table factorization and therefore cannot by itself establish a meaningful continuous-region bridge. **P41** makes the regularity obstruction computable for trace-distance tomography balls. **P42** derives explicit finite-sample requirements. **P43** optimizes the quantum-versus-target uncertainty split. **P44** protects post-data witness selection across a predeclared finite candidate family.

**P45** moves resource allocation to a shared preparation graph. **P46** adds hard-budget preparation selection and proves the general discrete problem is NP-hard while providing a relaxation upper bound. **P47** makes adaptive sampling, graph refinement, pruning, witness selection, and stopping time-uniformly valid. **P48** derives gap-dependent stopping complexity. **P49** proves bounded dyadic-checkpoint overhead. **P50-P53** convert local evidence demands into asynchronous service guarantees, heterogeneous stopping bounds, capacity-optimal allocation, and residual-demand reoptimization.

**P54** adds metric preparation-switching costs and an exact Hamiltonian-path reduction. **P55** proves pruning-aware execution-cost monotonicity. **P56** adds moving-start stability. **P57** adds switching-metric perturbation stability. **P58** replaces a known metric with finite-data transition uncertainty and robust route envelopes.

**P59** solves the continuous transition-calibration allocation problem. **P60** converts it into whole measurements with controlled rounding overhead. **P61** solves the equal-cost integer surrogate exactly through diminishing marginal gain. **P62** adds heterogeneous per-observation cost in the continuous problem. **P63** gives the unrestricted exact heterogeneous-cost integer Bellman solver. **P64** adds a scalable certified floor approximation. **P65** removes the one-sample regime restriction using lower-bounded water filling. **P66** spends the residual budget exactly inside the floor-dominating class. **P67** gives a sufficient common-multiplier certificate for unrestricted global integer optimality. **P68** turns the same Lagrangian construction into a quantitative lower bound and candidate-gap certificate. **P69** optimizes the dual multiplier family to a certified tolerance. **P70** makes the resulting certificate diagnostic rather than opaque: the candidate-to-dual gap decomposes exactly into nonnegative edgewise Lagrangian regret plus a multiplier-weighted unused-budget penalty.

**P71** returns from the downstream calibration branch to the core P19 bridge-sufficiency problem. It proves that a target constructed as \(E=h(T)\) automatically satisfies exact factorization through \(T\), that a descriptor-only stochastic target channel automatically gives \(I(E;\Omega\mid T)=0\), and that a learned rule \(h_D(T)\) remains descriptor-derived even on held-out data. P71 also proves a provenance non-identifiability result: an observed zero conditional residual can be reproduced by a descriptor-only channel, so independent target provenance cannot be inferred from the observed joint law alone.

**P72** adds the next target-side obligation: measurement robustness. Let \(E^\star\) be an independently justified latent target and \(Y\) its observed measurement. Under the declared nondifferential channel condition

\[
Y\perp\!\!\!\perp\Omega\mid(E^\star,T),
\]

P72 proves

\[
I(Y;\Omega\mid T)
\le
I(E^\star;\Omega\mid T).
\]

Thus a positive observed population residual transfers to the latent target, but a zero observed residual remains inconclusive because an erasing measurement channel can hide a positive latent residual. P72 further proves stochastic-channel contraction of pairwise target total variation, defines the target-channel stability coefficient

\[
\gamma_t
=
\inf_{\substack{v\ne0\\\mathbf1^\top v=0}}
\frac{\|K_tv\|_1}{\|v\|_1},
\]

and obtains

\[
\gamma_t\operatorname{TV}(p,q)
\le
\operatorname{TV}(K_tp,K_tq)
\le
\operatorname{TV}(p,q).
\]

For a binary symmetric target channel, the exact attenuation factor is \(|1-2\eta|\). P72 also gives a conservative finite-sample lower confidence bound for observed target separation and a sufficient equal-sample-size condition whose measurement penalty scales as \((\gamma_0\Delta_E)^{-2}\).

Direct P72 proof: [target-measurement channel robustness](proposition_72_target_measurement_channel_robustness.md). Equation classification: [P72 equation and provenance record](p72_equation_provenance.md).

**P73** closes the population identifiability step for one explicit target-measurement model. Inside a fixed physical stratum, let a binary latent target \(S\in\{-1,+1\}\) generate three binary target views \(X_1,X_2,X_3\) that are conditionally independent given \(S\), with

\[
\mathbb E[X_j\mid S]=a_j+b_jS.
\]

Writing \(m=\mathbb E[S]\), P73 derives the observable identities

\[
C_{ij}=b_ib_j(1-m^2),
\qquad
M_{123}=-2m(1-m^2)b_1b_2b_3.
\]

When all three pair covariances are nonzero, these moments recover the latent prevalence and all three binary view channels up to the unavoidable global latent-label swap. The P72 single-view stability coefficients are

\[
\gamma_j=|b_j|,
\]

so they are identifiable despite that label ambiguity. P73 also proves that the joint three-view channel has stability at least as large as the strongest single view and gives a constructive two-view non-identifiability result: with balanced latent prevalence and zero intercepts, the full two-view law depends only on \(b_1b_2\), so distinct individual reliabilities can produce the same observed distribution.

Direct P73 proof: [three-view target-channel identifiability](proposition_73_target_channel_identifiability.md). Equation classification: [P73 equation and provenance record](p73_equation_provenance.md). Implementation: [`target_channel_identifiability.py`](../src/consciousness_bridge/target_channel_identifiability.py).

**P74** converts the P73 population inversion into a finite-sample confidence certificate. From \(n\) IID observed triples it controls the full eight-cell empirical distribution on one simultaneous event, derives conservative perturbation bounds

\[
|\widehat C_{ij}-C_{ij}|\le3\delta_n,
\qquad
|\widehat M_{123}-M_{123}|\le13\delta_n,
\]

and propagates those intervals through the P73 nonlinear formulas. P74 introduces an explicit covariance nondegeneracy gate: if any lower confidence bound for \(|C_{12}|,|C_{13}|,|C_{23}|\) reaches zero, the P73 inversion is not certified from those finite data. When the gate passes and the covariance sign pattern is compatible with P73, the theorem gives simultaneous confidence bounds for the label-invariant latent imbalance, latent variance, the prevalence orbit under global label swapping, all three P72 stability coefficients, and a lower bound for joint three-view stability.

P74 then completes the finite-sample binary-channel recovery. Combining the P73 identities gives

\[
 b_jm=-\frac{M_{123}}{2C_{k\ell}},
\]

where \(k,\ell\) are the complementary views. The product \(b_jm\) is invariant under the common latent-label swap, so finite confidence intervals for the signed third centered moment and complementary covariance yield an interval for \(b_jm\). Together with \(a_j=\mu_j-b_jm\), this gives a confidence interval for each binary-channel offset. Combining that offset with \(\gamma_j=|b_j|\) produces simultaneous confidence sets for the unordered pair of latent-conditioned response probabilities. Reporting the pair as an unordered orbit is essential: it certifies the full binary measurement channel without pretending that the data determine which latent label has which experiential meaning. P74 also provides a conservative sufficient sample-size condition for separating a known population covariance margin from the P73 singular boundary.

Direct P74 proof: [finite-sample target-channel recovery](proposition_74_finite_sample_target_channel_recovery.md). Equation classification: [P74 equation and provenance record](p74_equation_provenance.md). Implementation: [`finite_sample_target_channel_recovery.py`](../src/consciousness_bridge/finite_sample_target_channel_recovery.py).

**P75** separates target-channel identifiability from target-model adequacy. For one binary latent state and three binary observed views, the observable simplex has \(2^3-1=7\) free probabilities and the declared conditional-independence latent model has \(1+2(3)=7\) continuous parameters. Thus the nondegenerate three-view model is generically just-identified: P73 can identify its parameters, but successful recovery does not create a generic independent equality-based goodness-of-fit test for the model assumption itself.

Adding a fourth binary view changes the count to

\[
2^4-1=15,
\qquad
1+2(4)=9,
\qquad
15-9=6,
\]

so the four-view model has six generic overidentifying degrees of freedom. P75 derives observable covariance tetrads

\[
C_{12}C_{34}=C_{13}C_{24}=C_{14}C_{23},
\]

requires all four three-view subsets to agree on the latent-imbalance ratio

\[
q_{ijk}=\frac{M_{ijk}^2}{C_{ij}C_{ik}C_{jk}}=\frac{4m^2}{1-m^2},
\]

and obtains the fourth-centered-moment relation

\[
M_{1234}=(1+q)C_{12}C_{34},
\]

with the equivalent covariance pairings. The executable P75 audit goes further than those displayed moment restrictions: it applies P73 to an anchor triple, infers the fourth channel, reconstructs the entire sixteen-cell observable law, and rejects compatibility when that full reconstruction fails. A synthetic direct-dependence perturbation between target views is required to fail this audit.

Direct P75 proof: [target-model adequacy and four-view overidentification](proposition_75_target_model_adequacy_overidentification.md). Equation classification: [P75 equation and provenance record](p75_equation_provenance.md). Implementation: [`target_model_adequacy.py`](../src/consciousness_bridge/target_model_adequacy.py).

**P76** converts the tracked P75 population adequacy restrictions into a finite-sample rejection certificate. From \(n\) IID four-view observations it places the entire sixteen-cell empirical law inside one simultaneous Hoeffding event. The induced \(L^1\) radius \(\delta_n\) controls every binary raw monomial moment simultaneously, which in turn gives conservative intervals for the centered moments used by P75.

For the two displayed covariance tetrads, P76 proves the explicit perturbation bound

\[
|\widehat D-D|\le12\delta_n.
\]

Thus \(|\widehat D|>12\delta_n\) certifies a nonzero population tetrad and rejects the declared four-view conditional-independence model with the shared confidence level. For the P75 cross-triple and fourth-moment conditions, P76 avoids unstable empirical ratios by cross-multiplying them into denominator-free polynomial equalities and propagating the same raw-moment confidence box through interval arithmetic. Any reported necessary-constraint interval that excludes zero is a valid rejection witness on the shared event.

The inference is deliberately asymmetric. A rejection is evidence that the declared P75 model is incompatible with the population under the stated IID sampling assumption. A failure to reject is not model acceptance: finite power may be inadequate, the violation may be small, or a misspecified law may satisfy the tracked necessary polynomials while failing the stronger P75 full-law membership audit.

Direct P76 proof: [finite-sample target-model adequacy rejection](proposition_76_finite_sample_target_model_adequacy.md). Equation classification: [P76 equation and provenance record](p76_equation_provenance.md). Implementation: [`finite_sample_target_model_adequacy.py`](../src/consciousness_bridge/finite_sample_target_model_adequacy.py).

**P77** closes the finite-data full-law gap left explicit by P76. Let \(\mathcal M\) be the complete declared observed-law model set and let \(\mathcal C_n(\widehat P)\) be a simultaneous confidence region for the population law. P77 proves that

\[
\mathcal C_n(\widehat P)\cap\mathcal M=\varnothing
\]

is a valid finite-sample rejection certificate at the confidence level used to construct \(\mathcal C_n\). For a finite alphabet of size \(K\), the same Hoeffding event used by P76 gives explicit \(L^\infty\) and \(L^1\) radii. Distance to a nonempty set is 1-Lipschitz, so empirical model distance and population model distance differ by at most the corresponding sampling radius on that event.

P77 also makes the computational direction explicit. A candidate model found by numerical optimization provides an upper bound on the minimum distance to a continuous model family. It cannot be treated as a rejection lower bound. Full-law rejection therefore requires a sound global distance lower bound or an equivalent certified feasibility argument. Exhaustive comparison is exact only when the declared model family itself is finite.

Direct P77 proof: [finite-sample full-law model-set separation](proposition_77_full_law_model_set_separation.md). Equation classification: [P77 equation and provenance record](p77_equation_provenance.md). Implementation: [`full_law_model_set_separation.py`](../src/consciousness_bridge/full_law_model_set_separation.py).

**P78** supplies the continuous-family optimization certificate required by P77 for the specific P75 four-view binary latent model. Each of the sixteen cell probabilities is multi-affine in nine parameters. On every axis-aligned parameter box, P78 computes exact coordinatewise cell ranges and converts them into a rigorous L-infinity lower bound on the distance from the empirical law to every model law generated inside that box.

Because the active boxes form a partition of the complete parameter cube, the minimum active-box lower bound is a global lower bound on distance to the entire continuous P75 model family. Explicit admissible parameter vectors provide upper bounds. A parameter-space Lipschitz argument gives an explicit mesh-gap certificate, so the global lower bound converges under refinement. The implementation keeps empirical count laws and dyadic branch points in exact rational arithmetic.

The P77 handoff remains directional: full-law rejection requires the P78 global lower bound to exceed a separately valid upper bound on the P77 sampling radius. A small lower bound is inconclusive and does not validate the target model.

Direct P78 proof: [certified continuous model separation](proposition_78_certified_continuous_model_separation.md). Equation classification: [P78 equation and provenance record](p78_equation_provenance.md). Implementation: [`certified_continuous_model_separation.py`](../src/consciousness_bridge/certified_continuous_model_separation.py).


---

## Proposition 79: Certified Rational Sampling-Radius Envelope

**P79** closes the numerical-direction gap in the P77/P78 rejection handoff. P78 supplies a certified lower bound on empirical distance to the complete continuous P75 model family. P79 supplies a mathematically valid exact-rational upper envelope for the P77 sampling radius by combining rational logarithm brackets with an integer-certified dyadic square-root enclosure. A strict lower-bound versus upper-bound comparison can therefore certify rejection without assuming the direction of floating-point rounding.

Proof: [Proposition 79](proposition_79_certified_sampling_radius.md). Provenance: [P79 equation record](p79_equation_provenance.md). Figure: [P79 theorem figure](figures/p79_certified_sampling_radius.svg). Implementation: [`certified_sampling_radius.py`](../src/consciousness_bridge/certified_sampling_radius.py). Tests: [`test_certified_sampling_radius.py`](../tests/test_certified_sampling_radius.py).

P79 does not validate non-rejected models and does not close the physical-to-experiential bridge.


## Proposition 80: Simplex-Coupled Box Certificate for Continuous P75 Separation

**P80** strengthens the P78 boxwise lower-bound relaxation without changing the P75 model family. P78 supplies exact coordinate intervals for every observed-law cell over a parameter box. P80 intersects those intervals with the probability-simplex constraint, computes the exact L-infinity distance to that interval-simplex relaxation in rational arithmetic, and proves that the resulting box lower bound is never weaker than P78's coordinatewise bound. The active-box minimum remains a valid global lower bound on distance to the complete continuous P75 family, while P79 continues to supply the one-sided sampling-radius upper certificate used for strict finite-data rejection.

Proof: [Proposition 80](proposition_80_simplex_coupled_model_separation.md). Provenance: [P80 equation record](p80_equation_provenance.md). Figure: [P80 theorem figure](figures/p80_simplex_coupled_model_separation.svg). Implementation: [`simplex_coupled_model_separation.py`](../src/consciousness_bridge/simplex_coupled_model_separation.py). Tests: [`test_simplex_coupled_model_separation.py`](../tests/test_simplex_coupled_model_separation.py).

P80 is a computational tightening of a declared observed-law model test. It does not identify the P75 latent variable with consciousness and does not close the physical-to-experiential bridge.


## Proposition 81: Projection-Event Certificate for Continuous P75 Separation

**P81** strengthens P80 by retaining exact parameter-box ranges for all nonempty projected binary events of the four observed views. For each cylinder event, its empirical mismatch from the exact box interval is divided by the event's number of full cells to obtain a valid full-law L-infinity lower bound. The combined P81 certificate is the maximum of this projection bound and the P80 simplex-coupled bound, so it is never weaker than P80. A fixed-marginal witness gives `L80=0` but `L81=1/80`, proving strict improvement is possible. [Proof](proposition_81_projection_event_model_separation.md) | [provenance](p81_equation_provenance.md) | [figure](figures/p81_projection_event_model_separation.svg). P81 does not identify the P75 latent variable with consciousness and does not close the physical-to-experiential bridge.

---

## Scientific interpretation of the chronology

The proposition numbers preserve development order, not one linear chain. The scientific dependency structure has several branches:

- P1-P24 build the formal bridge, physical-sufficiency, finite-data, and adaptive-refinement core.
- P25-P37 build operational scale compatibility.
- P38-P44 build the quantum operational interface.
- P45-P60 build adaptive evidence acquisition and execution machinery.
- P61-P70 build downstream calibration and optimization.
- P71-P81 return to the target side of the P19 bridge and formalize non-circular target provenance, noisy target measurement, population target-channel identification, finite-sample target-channel recovery, target-model adequacy, and finite-sample model rejection.

P75 does not make an experiential ontology claim. Passing its four-view restrictions establishes compatibility with the declared target-measurement model, not uniqueness or truth of that model. Failure identifies inadequacy of the declared conditional-independence model for the observed law; it does not prove that the latent target is nonphysical or that the physical-to-experiential bridge has been solved.

P76 adds a finite-sample rejection layer for a tracked family of necessary P75 polynomial constraints. Its non-rejection output is explicitly inconclusive. P77 defines the stronger full-law criterion. P78 supplies the global exact-rational lower-bound certificate for the continuous P75 family. P79 gives the sampling-radius side a certified upper direction. P80 retains probability-simplex coupling, and P81 adds exact projected-event constraints that can strictly strengthen P80. The next problems are tighter simultaneous event coupling, computational efficiency, sharper power, and robust alternatives for residually dependent or learned target-view systems.

---

## How to audit any proposition

Each proposition should be read through the same four-way distinction:

1. **Statement and assumptions:** the proposition document states the exact mathematical claim and its domain.
2. **Proof:** derivations establish what follows from those assumptions.
3. **Implementation and tests:** executable code checks the declared computational construction and regression behavior.
4. **Scientific interpretation:** the result is not promoted beyond its scope.

The complete dependency graph is maintained in the [Theorem roadmap](theorem_roadmap.md), equation provenance in the [Equation and citation map](equation_and_citation_map.md), and cross-disciplinary sources in the [Foundational physics and mathematics bibliography](foundational_physics_mathematics_bibliography.md) and [Literature map](literature_map.md).


