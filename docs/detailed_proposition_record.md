# Detailed proposition record

This page preserves the proposition-by-proposition development history of the Mathematical Consciousness Bridge research program. It is intentionally separate from the main README so a first-time reader can follow the scientific argument without first learning the internal chronology of the project.

The proposition record is an audit trail, not a substitute for the scientific narrative. For dependency structure, see the [Theorem roadmap](theorem_roadmap.md). For topic-oriented navigation, see [Research navigation](research_navigation.md). For equation provenance and external references, see the [Equation and citation map](equation_and_citation_map.md).

The scientific status rule is strict throughout: a theorem is only a theorem under its declared assumptions, an implementation is not empirical evidence, a simulation is not an ontological result, and the physical-to-experiential bridge remains open unless separately established.

---

## Complete P1 to P73 chronology

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

**P73** addresses one assumption left open by P72: whether a binary target-channel stability can be identified without directly observing the latent target. Under the declared three-view model \(Y_i=ZN_i\), with mutually independent binary noises independent of \(Z\), the observable pair moments satisfy

\[
m_{ij}=\mathbb E[Y_iY_j]=r_ir_j,
\qquad
r_i=\mathbb E[N_i].
\]

P73 first proves a negative result: two heterogeneous views identify only the product \(|m_{12}|=\gamma_1\gamma_2\), leaving a continuum of compatible individual stabilities. With three nonzero compatible views, however,

\[
\gamma_1=\sqrt{\frac{m_{12}m_{13}}{m_{23}}},
\qquad
\gamma_2=\sqrt{\frac{m_{12}m_{23}}{m_{13}}},
\qquad
\gamma_3=\sqrt{\frac{m_{13}m_{23}}{m_{12}}}.
\]

The stability magnitudes are unique, while the signed reliability vector remains ambiguous under one simultaneous global sign flip. P73 also gives simultaneous finite-sample intervals for the three stability magnitudes using Hoeffding bounds on the pairwise moments, and it states the confidence accounting required to hand an independently calibrated lower stability bound into the P72 bridge experiment.

Direct P73 proof: [three-view target-channel identifiability](proposition_73_three_view_target_channel_identifiability.md). Equation classification: [P73 equation and provenance record](p73_equation_provenance.md).

---

## Scientific interpretation of the chronology

The proposition numbers preserve development order, not one linear chain. The scientific dependency structure has several branches:

- P1-P24 build the formal bridge, physical-sufficiency, finite-data, and adaptive-refinement core.
- P25-P37 build operational scale compatibility.
- P38-P44 build the quantum operational interface.
- P45-P60 build adaptive evidence acquisition and execution machinery.
- P61-P70 build downstream calibration and optimization.
- P71-P73 return to the target side of the P19 bridge and formalize non-circular target provenance, noisy target measurement, and three-view binary channel-stability identifiability.

P73 closes only a narrow identifiability model. The next target-side problem is **model adequacy and correlated-error robustness**: determine how shared bias, conditional dependence, class-asymmetric errors, temporal drift, or physical-state-dependent measurement can distort the P73 stability reconstruction, and develop diagnostics or sensitivity bounds that make those violations visible.

---

## How to audit any proposition

Each proposition should be read through the same four-way distinction:

1. **Statement and assumptions:** the proposition document states the exact mathematical claim and its domain.
2. **Proof:** derivations establish what follows from those assumptions.
3. **Implementation and tests:** executable code checks the declared computational construction and regression behavior.
4. **Scientific interpretation:** the result is not promoted beyond its scope.

The complete dependency graph is maintained in the [Theorem roadmap](theorem_roadmap.md), equation provenance in the [Equation and citation map](equation_and_citation_map.md), and cross-disciplinary sources in the [Foundational physics and mathematics bibliography](foundational_physics_mathematics_bibliography.md) and [Literature map](literature_map.md).
