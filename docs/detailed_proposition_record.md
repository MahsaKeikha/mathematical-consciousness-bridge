# Detailed proposition record

This page preserves the proposition-by-proposition development history of the Mathematical Consciousness Bridge research program. It is intentionally separate from the main README so a first-time reader can follow the scientific argument without first learning the internal chronology of the project.

The proposition record is an audit trail, not a substitute for the scientific narrative. For dependency structure, see the [Theorem roadmap](theorem_roadmap.md). For topic-oriented navigation, see [Research navigation](research_navigation.md). For equation provenance and external references, see the [Equation and citation map](equation_and_citation_map.md).

The scientific status rule is strict throughout: a theorem is only a theorem under its declared assumptions, an implementation is not empirical evidence, a simulation is not an ontological result, and the physical-to-experiential bridge remains open unless separately established.

---

## Complete P1 to P75 chronology

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

---

## Scientific interpretation of the chronology

The proposition numbers preserve development order, not one linear chain. The scientific dependency structure has several branches:

- P1-P24 build the formal bridge, physical-sufficiency, finite-data, and adaptive-refinement core.
- P25-P37 build operational scale compatibility.
- P38-P44 build the quantum operational interface.
- P45-P60 build adaptive evidence acquisition and execution machinery.
- P61-P70 build downstream calibration and optimization.
- P71-P75 return to the target side of the P19 bridge and formalize non-circular target provenance, noisy target measurement, population target-channel identification, finite-sample target-channel recovery, and target-model adequacy.

P75 does not make an experiential ontology claim. Passing its four-view restrictions establishes compatibility with the declared target-measurement model, not uniqueness or truth of that model. Failure identifies inadequacy of the declared conditional-independence model for the observed law; it does not prove that the latent target is nonphysical or that the physical-to-experiential bridge has been solved.

The next target-side problem is finite-sample adequacy certification: turn the P75 population tetrad, cross-triple, fourth-moment, and full-law reconstruction residuals into simultaneous uncertainty-aware tests.

---

## How to audit any proposition

Each proposition should be read through the same four-way distinction:

1. **Statement and assumptions:** the proposition document states the exact mathematical claim and its domain.
2. **Proof:** derivations establish what follows from those assumptions.
3. **Implementation and tests:** executable code checks the declared computational construction and regression behavior.
4. **Scientific interpretation:** the result is not promoted beyond its scope.

The complete dependency graph is maintained in the [Theorem roadmap](theorem_roadmap.md), equation provenance in the [Equation and citation map](equation_and_citation_map.md), and cross-disciplinary sources in the [Foundational physics and mathematics bibliography](foundational_physics_mathematics_bibliography.md) and [Literature map](literature_map.md).
