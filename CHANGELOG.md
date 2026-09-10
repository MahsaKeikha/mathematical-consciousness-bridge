# Changelog

## 0.42.0 - 2026-09-09

### Added
- Proposition 42: finite-sample obstruction sample complexity for a fixed informationally complete POVM.
- Explicit simultaneous quantum trace-distance radius under a declared linear reconstruction stability constant.
- Explicit simultaneous finite-alphabet target-TV radius.
- Sufficient quantum and target sample-size formulas with inverse-square regularity-gap scaling.
- Executable implementation, regression tests, publication map, and public-paper integration.

### Corrected
- Proposition 41 population-level planning inequality now carries center-estimation error through the confidence envelopes correctly. The conservative sufficient condition is \(d_Y-Ld_Q>4\varepsilon+4Lr\), not the earlier factor-two expression.
- Malformed P41 LaTeX control characters in the target and quantum symbols were removed.

### Scientific boundary
- P42 is conditional on IID sampling, a fixed informationally complete measurement, a declared reconstruction stability constant, and a declared Lipschitz bridge class.
- The theorem gives a sufficient upper bound on sample complexity. It does not yet prove minimax optimality and does not establish quantum incompleteness or consciousness.

## 0.41.0 - 2026-09-09

### Added
- Proposition 41: trace-ball quantum envelopes and end-to-end regularity certification.
- Analytic upper bounds on the P40 continuous quantum confidence-region envelope.
- Target-TV lower confidence envelopes and a direct Lipschitz obstruction margin.
- A symmetric finite-error experiment-design inequality.
- Executable implementation, regression tests, publication map, and public-paper integration.

### Scientific boundary
- P41 assumes the declared quantum and target confidence balls have valid simultaneous coverage.
- A positive P41 obstruction rejects only the declared trace-ball region together with the declared bridge regularity class.

## 0.40.0 - 2026-09-09

### Added
- Proposition 40: continuous quantum confidence regions and bridge-regularity obstructions.
- A no-go theorem showing that injective finite descriptors always permit unrestricted factorization on the sampled image.
- A continuous confidence-region quantum-distance envelope.
- A modulus-of-continuity obstruction and Lipschitz corollary.
- Executable implementation, regression tests, publication map, and public-paper integration.

### Scientific boundary
- Bridge regularity is an additional modeling assumption and is not derived from quantum mechanics.
- A positive P40 obstruction rules out only the declared quantum confidence region together with the declared bridge-regularity class.

## 0.39.0 - 2026-09-09

### Added
- Proposition 39: finite-data quantum model-set non-factorization certification.
- A target-law separation lower bound with simultaneous total-variation uncertainty.
- A worst-model violation margin over a tomography-derived quantum confidence set.
- Explicit proof that numerical quantum-state closeness is not exact state equality.
- A guard showing that any surviving injective quantum model blocks the collision certificate.
- Executable implementation, nine regression tests, and a publication theorem map.

### Scientific boundary
- P39 certifies non-factorization only relative to the declared quantum hypothesis family and its confidence set.
- It does not prove quantum mechanics incomplete, consciousness nonphysical, or any target experiential without independent justification.

## 0.38.0 - 2026-09-09

### Integrated theorem sequence
- P32 exact delay-quotient compatibility.
- P33 joint intervention-delay operational quotient and additive ambiguity theorem.
- P34 joint node/state/intervention/time P11 scale assembly.
- P35 approximate directed-influence quotient stability.
- P36 partition-product and irreducibility quotient stability.
- P37 complete approximate P11 operational-scale distortion theorem.
- P38 quantum operational sufficiency and exact non-factorization criterion.

### Publication synchronization
- Main README updated through P38 with equations, scientific boundaries, proof links, code links, and visual maps.
- Theorem roadmap and research navigation synchronized through P38.
- P38 publication map added.
- Package and citation metadata synchronized to 0.38.0.
- Main-page visibility guards extended through P38.

### Scientific boundary
- P32-P37 certify a declared candidate physical signature across operational scale; they do not identify consciousness.
- P38 tests factorization through a declared tomographically complete quantum descriptor; failure of that declared factorization is not by itself evidence that quantum mechanics is incomplete or that consciousness is nonphysical.

This changelog records theorem-level scientific releases. Definitions, proofs, implementations, tests, figures, and documentation remain linked from the main research page.

## 0.31.0 - 2026-09-09

### Proposition 31 - intervention-quotient compatibility

- Introduced a declared surjective intervention-label quotient \(b:\mathcal U_f\twoheadrightarrow\mathcal U_c\) after the physical response space has been fixed.
- Proved that a unique coarse response table exists if and only if all fine response laws are constant on every quotient fiber at every retained delay.
- Defined the intervention-quotient ambiguity defect \(\eta_b\) as the worst total-variation separation between response laws assigned the same coarse intervention label.
- Proved \(\eta_b=0\) if and only if exact response-law descent holds.
- Proved representative-selection stability \(\sup_{c,\tau}\|Q_s^{c,\tau}-Q_{s'}^{c,\tau}\|_{\mathrm{TV}}\le\eta_b\).
- Proved the induced response-geometry ambiguity bound \(\sup_{c,d,\tau}|G_s-G_{s'}|\le2\eta_b\).
- Explicitly separated operational intervention quotienting from physical actuator identity and simultaneous intervention.
- Added executable mathematics, nine dedicated regression tests, a publication theorem map, main-paper integration, theorem-roadmap integration, navigation, equation provenance, release guards, and synchronized 0.31.0 metadata.
- Preserved delay/time quotienting, physical completeness, genuine physical fusion, and experiential interpretation as separate open theorem burdens.

## 0.30.0 - 2026-09-09

### Proposition 30 - full declared P11 scale compatibility

- Assembled the P27 partition, P28 directed-influence, and P29 response-geometry scale branches under one shared node quotient and experiment declaration.
- Defined the full declared P11 distortion vector \(\mathbf D_{P11}=(D_G,D_A,D_K)\).
- Required partition compatibility, source-pair compatibility, a common intervention-delay grid, a common state map, and a common reconstruction declaration before assembly is certified.
- Proved \(\|\mathbf D_{P11}\|_\infty\le\max\{2\rho_G^*,2\rho_A^*,\rho_P^*+\rho_\Pi^*\}\).
- Proved exact simultaneous preservation when all relevant reconstruction defects vanish and the semantic compatibility conditions hold.
- Added the no-semantic-compensation guard: zero numerical component distortion does not certify valid transport when the compared structures are semantically incompatible.
- Added executable assembly certification, nine regression tests, a publication theorem map, main-paper integration, roadmap, navigation, provenance, release guards, and synchronized 0.30.0 metadata.
- Preserved the boundary that intervention/time quotienting, physical completeness, genuine physical fusion, and experiential interpretation remain open.

## 0.29.0 - 2026-09-09

### Proposition 29 - response-geometry transport under node aggregation

- Extended the P11 physical scale program to the complete response-geometry component under the P27 changing node set.
- Kept intervention labels and delay labels fixed so every fine geometry entry has one exact coarse counterpart.
- Defined the complete intervention-delay total-variation response geometry before and after aggregation-compatible state mapping.
- Proved entrywise total-variation contraction for every intervention pair at every retained delay.
- Applied P18 to obtain the law-specific bound \(0\le G_f-G_c\le\rho_{u,\tau}+\rho_{v,\tau}\).
- Proved the uniform whole-geometry certificate \(\|\mathcal G_f-\mathcal G_c\|_\infty\le2\rho_*\).
- Derived exact geometry preservation, response-diameter control, and per-edge threshold preservation as corollaries.
- Added executable implementation, nine regression tests, a publication theorem map, main-paper integration, theorem-roadmap integration, navigation, provenance, release guards, and synchronized 0.29.0 metadata.
- Preserved the boundary that intervention merging, temporal resampling, full P11 assembly, physical completeness, and experiential interpretation remain open.

## 0.28.0 - 2026-09-09

### Proposition 28 - intervention compatibility under node aggregation

- Extended the P25 directed-influence scale branch through the changing node set introduced by P27.
- Defined the fine source-incidence set of each matched intervention pair and proved the exact condition for unambiguous coarse source descent.
- Defined canonical coarse source pair families as unions of inherited fine pair families within each aggregation fiber, with duplicate comparisons removed.
- Explicitly separated aggregate source labeling from any claim of a new simultaneous aggregate actuator.
- Defined the fine target block as the full response marginal on the target aggregation fiber rather than an arbitrary constituent node.
- Proved directed-influence contraction under deterministic target-fiber state aggregation.
- Applied P18 reconstruction to prove \(0\le A_f-A_c\le2\rho\), with exact-preservation and threshold-edge corollaries.
- Added executable implementation, nine regression tests, a publication theorem map, main-paper integration, roadmap, navigation, provenance, release guards, and synchronized 0.28.0 metadata.
- Preserved the boundary that response-geometry alignment, genuinely new aggregate interventions, complete P11 scale equivalence, physical completeness, and experience remain open.

## 0.27.0 - 2026-09-09

### Proposition 27 - partition-lattice transport under node aggregation

- Introduced an explicit surjective node-aggregation map \(a:V_f\twoheadrightarrow V_c\) and its fine aggregation fibers.
- Proved that a fine partition has an exact coarse descent if and only if every aggregation fiber lies wholly inside one fine partition block.
- Proved that coarse partitions are in one-to-one correspondence with aggregation-saturated fine partitions through inverse lift/descent maps.
- Proved preservation of refinement order, meet, and join, yielding a lattice isomorphism between \(\operatorname{Part}(V_c)\) and the saturated sublattice of \(\operatorname{Part}(V_f)\).
- Defined aggregation-compatible state maps that distinguish node-count reduction from within-fiber state compression.
- Proved partition-product commutation for descendable partitions under aggregation-compatible state maps.
- Proved irreducibility contraction across node aggregation and inherited the P18 reconstruction bound \(0\le\kappa_f-\kappa_c\le\rho(P)+\rho(P_{\pi_f})\).
- Added exact-preservation and complete-loss examples, separating structural non-descendability from observational attenuation.
- Added executable mathematics, nine dedicated tests, a publication theorem map, main-paper integration, navigation, provenance, release guards, and synchronized 0.27.0 metadata.
- Corrected the P26 README and theorem-roadmap transcription of the second reconstruction term from a malformed `ho(...)` token to \(\rho(...)\).
- Preserved the boundary that intervention aggregation, directed influence under source aggregation, full P11 scale equivalence, physical completeness, genuine physical fusion, and experience remain open.

## 0.26.0 - 2026-09-09

### Proposition 26 - partition-irreducibility scale certification

- Extended the P11 physical scale program from response geometry and directed influence to the partition-irreducibility component.
- Formalized block-compatible deterministic observation so the declared partition has the same physical meaning at fine and coarse scales.
- Proved that partition productization commutes with block-compatible pushforward.
- Proved contraction \(\kappa_c\le\kappa_f\), so compatible coarse observation cannot manufacture additional partition irreducibility.
- Applied P18 to the response law and its partition-product null to prove \(0\le\kappa_f-\kappa_c\le\rho(P)+\rho(P_\pi)\).
- Kept the two reconstruction terms separate to expose the actual-response and factorized-null reconstruction burdens.
- Proved exact preservation under exact reconstruction and a threshold-survival margin under bounded reconstruction error.
- Added a binary counterexample in which fine irreducibility \(0.4\) collapses to zero after one coordinate is observationally erased.
- Added executable utilities, regression tests, a publication theorem map, README paper integration, theorem-roadmap integration, navigation, provenance, and release guards.
- Preserved the boundary that P26 does not yet solve partition-lattice transport, physical node aggregation, genuine fusion, physical completeness, or experience.

## 0.25.0 - 2026-09-09

### Proposition 25 - directed-influence scale certification

- Returned to the P11 structured physical candidate and isolated the directed perturbational influence component for scale analysis.
- Proved that deterministic target observation coarse-graining cannot increase matched-intervention directed influence.
- Specialized the P18 fiber-consistent reconstruction defect to the intervention-conditioned target response family.
- Proved the sharp additive bound \(0\le A^f-A^c\le2\rho\).
- Proved exact directed-influence preservation when the declared response family reconstructs exactly.
- Derived the threshold-edge margin \(A^f>\theta+2\rho\Rightarrow A^c>\theta\) and the no-false-positive implication \(A^c>\theta\Rightarrow A^f>\theta\).
- Added an explicit binary counterexample saturating the \(2\rho\) loss bound.
- Added executable certification, regression tests, a publication theorem map, and an explicit P11+P18 dependency branch in the global roadmap.
- Preserved the boundary that P25 does not certify partition irreducibility, node fusion, changed intervention semantics, physical completeness, or experience.
- Integrated P25 into the README paper, navigation, equation provenance, release metadata, theorem guards, and visual-quality guards.

## 0.24.0 - 2026-09-09

### Proposition 24 - anytime-valid adaptive physical-refinement certification

- Converted P23 fixed-sample post-selection validity into a time-uniform certificate for one finite-alphabet IID stream.
- Introduced the explicit summable error schedule \(\alpha_n=6\alpha/(\pi^2n^2)\) with total mass exactly \(\alpha\).
- Derived the anytime base-law radius \(\tau_n^{\mathrm{any}}(\alpha)\) by applying the P20 categorical bound at local level \(\alpha_n\).
- Proved one confidence event valid simultaneously for every positive sample size using a countable union bound.
- Lifted P23 adaptive descriptor-selection coverage to every time on that event.
- Proved validity at any realized finite data-dependent stopping time.
- Extended the P23 refinement-regret and excess-residual certificates to the full time-uniform path.
- Added executable anytime certification, dedicated regression tests, a publication-style P24 theorem map, and a P1-P24 global roadmap.
- Preserved the interpretation boundary that anytime statistical validity does not establish physical completeness or experiential interpretation.
- Integrated P24 into the README paper, reader navigation, equation provenance, release metadata, proposition guards, and visual-quality guards.

## 0.23.0 - 2026-09-09

### Proposition 23 - adaptive physical-descriptor selection certification

- Extended the P22 shared-base-law confidence event from fixed refinement chains to fixed-sample data-dependent selection among admissible deterministic refinements.
- Used pathwise total-variation contraction to show that one base confidence event controls every deterministic candidate pushforward simultaneously.
- Proved that the residual and refinement-gain confidence intervals remain valid for the descriptor selected from the same finite sample.
- Proved the generic post-selection regret bound \(0\le G^*-G_{\widehat f}\le2\Gamma_{\max}\).
- Added the sharper observable certificate \(G^*-G_{\widehat f}\le\max_fU_f^G-L_{\widehat f}^G\).
- Used P21 to identify the same quantity with selected residual excess: \(R_{\widehat f}-\min_fR_f=G^*-G_{\widehat f}\).
- Made the distinction between statistical post-selection validity and physical admissibility explicit.
- Preserved the fixed-sample boundary: optional stopping across growing sample sizes remains outside P23.
- Added executable adaptive-selection certification, fourteen dedicated regression tests, and a publication-style P23 theorem map.
- Extended the README paper, global theorem roadmap, research navigation, equation provenance, release metadata, proposition guards, and figure-quality guards through P23.

## 0.22.0 - 2026-09-09

### Proposition 22 - simultaneous finite-sample certification of physical-refinement chains

- Rebased P20 finite-sample concentration on one declared base law \((\Omega,E)\) for a fixed nested physical-descriptor chain.
- Proved that deterministic pushforward contraction transfers one base total-variation confidence event to every residual law and every refinement-gain law simultaneously.
- Derived simultaneous confidence intervals for the complete P21 residual trajectory \(R_k=I(E;\Omega\mid T_k)\).
- Derived simultaneous confidence intervals for every refinement gain \(G_k=I(E;T_k\mid T_{k-1})\).
- Used the P21 identity \(G_k=R_{k-1}-R_k\) to intersect direct and difference-based gain certificates without weakening coverage.
- Proved joint coverage \(\Pr(R_k\in\mathcal I_k^R\ \forall k,\ G_k\in\mathcal I_k^G\ \forall k)\ge1-\alpha\).
- Established that this shared-base-event construction requires no separate \(\alpha/(2m+1)\) confidence split over descriptor levels, while preserving the alphabet-size limitations of the conservative finite-alphabet bound.
- Added executable simultaneous chain certification and twelve regression tests.
- Added a publication-style P22 theorem map and extended the global theorem roadmap through P22.
- Integrated P22 into the README paper, reader navigation, equation provenance, release metadata, proposition guards, and figure-quality guards.

## 0.21.0 - 2026-09-09

### Proposition 21 - physical-descriptor refinement and residual persistence

- Formalized nested deterministic physical descriptors through \(T_c=c\circ T_f\) with \(T_f=f(\Omega)\).
- Proved deterministic collision monotonicity \(\mathcal C(T_f,E)\subseteq\mathcal C(T_c,E)\), so valid physical refinement can remove unresolved target collisions but cannot create new ones.
- Defined the descriptor-relative stochastic residual \(R(T)=I(E;\Omega\mid T)\).
- Proved the exact refinement identity \(R(T_c)=I(E;T_f\mid T_c)+R(T_f)\) and therefore \(R(T_f)\le R(T_c)\).
- Extended the result to nested refinement chains with exact telescoping \(R_0-R_m=\sum_k I(E;T_k\mid T_{k-1})\).
- Added executable refinement validation, collision audits, pairwise residual decomposition, nested residual trajectories, and twelve regression tests.
- Added a publication-style P21 theorem map and extended the public theorem roadmap through P21.
- Added the identity-descriptor boundary \(I(E;\Omega\mid\Omega)=0\) as an explicit guard against treating conditional screening-off as a proof of nonphysical ontology.
- Integrated P21 into the README paper, reader navigation, equation provenance, visual guards, theorem-chain guards, changelog, and release metadata.

## 0.20.0 - 2026-09-09

### Proposition 20 - finite-sample residual certification

- Converted the P19 population condition \(I(E;\Omega\mid T)=0\) into an explicit finite-sample confidence certificate for declared finite-alphabet IID data.
- Derived a simultaneous joint-distribution total-variation radius from cellwise Hoeffding concentration and a union bound.
- Added a finite-alphabet entropy-continuity lemma that remains valid when only an upper TV radius is known.
- Propagated the joint-distribution confidence radius through the entropy representation of conditional mutual information.
- Proved a confidence interval \([L_n,U_n]\) for the population residual and the decision rule \(L_n>0\Rightarrow I_P(E;\Omega\mid T)>0\) at confidence at least \(1-\alpha\).
- Added a synthetic binary numerical checkpoint, executable implementation, claim-level regression tests, and a publication-style P20 theorem map.
- Extended the README, theorem roadmap, reader navigation, equation provenance, release metadata, and link-integrity guards through P20.
- Preserved the interpretation boundary that a certified residual first challenges the completeness of the declared physical descriptor and sampling model.

## 0.19.0 - 2026-09-09

### Proposition 19 - fundamental physical sufficiency and residual tests

- Proved the exact factorization criterion \(E=B_T\circ T\) if and only if the target is constant on every fiber of the declared physical descriptor.
- Added exact collision witnesses that rule out deterministic factorization through an incomplete descriptor.
- Proved the finite stochastic equivalence between physical screening-off and \(I(E;\Omega\mid T)=0\).
- Added the deterministic-target corollary \(I(E;\Omega\mid T)=H(E\mid T)\).
- Added a differential no-go criterion based on \(\operatorname{rank}D(T,E)-\operatorname{rank}DT\).
- Added executable factorization and conditional-information utilities with regression tests.
- Added a P19 theorem map and synchronized the public P1-P19 dependency map.
- Added a complete reader-navigation index and automated internal-link integrity checks.
- Extended the equation and citation map through P19 so standard mathematics, repository results, and interpretation boundaries remain explicit.

## 0.18.0 - 2026-09-09

### Proposition 18 - scale sufficiency by approximate reconstruction

- Introduced a fiber-consistent stochastic decoder \(R\) for reconstructing fine response laws from a declared coarse-graining map \(C\).
- Defined the reconstruction defect
  \[
  \rho(P)=\|P-R_\#C_\#P\|_{\mathrm{TV}}
  \]
  and the uniform declared-family defect \(\rho_{\mathcal F}\).
- Proved the quantitative response-geometry distortion bound
  \[
  0\le
  \|P-Q\|_{\mathrm{TV}}-
  \|C_\#P-C_\#Q\|_{\mathrm{TV}}
  \le 2\rho_{\mathcal F}.
  \]
- Proved exact family sufficiency when \(\rho_{\mathcal F}=0\), even for globally many-to-one coarse maps.
- Proved the finite-family separation guarantee
  \[
  \delta_c\ge\delta_f-2\rho_{\mathcal F},
  \]
  so \(\delta_f>2\rho_{\mathcal F}\) certifies coarse-family identifiability.
- Added a sharp collapsed-fiber witness attaining the factor-two bound.
- Added executable scale-certification utilities and dedicated regression tests.
- Added a publication-style P18 figure and integrated P18 into the theorem roadmap, multiscale hierarchy, citation metadata, and visual-quality guards.
- Added a reproducible **40-figure quantitative physics and mathematics atlas** spanning stochastic dynamics, diffusion, thermodynamics, probability geometry, intervention-response structure, composition, coarse-graining, temporal certification, sample complexity, Monte Carlo tests, perturbational propagation, and world-tube examples.
- Added deterministic figure generation, a machine-readable figure manifest, a quantitative validation report, and automated tests that require at least 33 quantitative scientific figures and verify numerical checkpoints.
- Rebuilt the main README as a complete visual research-paper narrative with the quantitative figures embedded where the equations and propositions are introduced.
- Rebuilt the theorem roadmap through **P18** and tightened canonical SVG publication-quality checks.
- Updated the research-software version to **0.18.0**.

## 0.17.0 - 2026-09-09

### Proposition 17 - coarse-graining, refinement, and recoverability

- Defined deterministic response-law coarse-graining
  \[
  C:\Omega_f\to\Omega_c,
  \qquad
  C_\#P(y)=\sum_{x:C(x)=y}P(x).
  \]
- Proved total-variation contraction
  \[
  \|C_\#P-C_\#Q\|_{\mathrm{TV}}
  \le
  \|P-Q\|_{\mathrm{TV}}.
  \]
- Proved exact preservation under bijective reparameterization on the observed support.
- Constructed exact many-to-one information-collision witnesses with fine-scale TV distance one and coarse-scale TV distance zero.
- Formalized refinement ambiguity as an identifiability problem rather than a computational inconvenience.
- Distinguished descriptive coarse-graining from genuine physical fusion or splitting, which can alter dynamics, intervention channels, and state variables.
- Added executable coarse-graining utilities, regression tests, a publication-style P17 figure, and multiscale documentation.

## 0.16.0 - 2026-09-09

### Proposition 16 - independent composition and controlled coupling

- Defined the independent product-response composition
  \[
  P_{A\otimes B}^{(u_A,u_B),\tau}=P_A^{u_A,\tau}\otimes P_B^{u_B,\tau}.
  \]
- Proved the composed response-geometry bounds
  \[
  \max\{d_A,d_B\}\le d_{AB}\le d_A+d_B-d_Ad_B.
  \]
- Proved exact preservation of one-factor total-variation distance when the other subsystem intervention is held fixed.
- Proved zero cross-system directed influence under independent product-response composition.
- Proved zero partition irreducibility across the complete \(A|B\) subsystem split.
- Defined the response-level coupling defect
  \[
  \chi_{A|B}(\tau)
  =
  \sup_{u_A,u_B}
  \left\|
  P_{AB}-P_{A,\mathrm{marg}}\otimes P_{B,\mathrm{marg}}
  \right\|_{\mathrm{TV}},
  \]
  and identified it exactly with the Proposition 11 partition irreducibility for the \(A|B\) split.
- Clarified the identifiability boundary: zero response-factorization defect does not by itself establish absence of every hidden mechanistic interaction outside the declared intervention-observable regime.
- Added executable composition utilities and eight claim-level tests, increasing the suite to 92 tests.
- Added a publication-style composition/coupling figure and rebuilt the theorem roadmap through P16.
- Extended repository structure and visual-quality guards to protect the complete P16 artifact set.

## 0.15.0 - 2026-09-09

### Proposition 15 - finite-sample temporal certification

- Proved the quotient-distance stability inequality
  \[
  |\widehat d_{st}-d_{st}|\le\varepsilon_s+\varepsilon_t
  \]
  under simultaneous fingerprint-error radii.
- Derived exact lower and upper finite-error bounds for every pairwise temporal separation.
- Derived cumulative path-variation uncertainty
  \[
  |\widehat V-V|\le\varepsilon_0+2\sum_{t=1}^{T-1}\varepsilon_t+\varepsilon_T.
  \]
- Derived maximum-step uncertainty
  \[
  |\widehat J-J|\le\max_t(\varepsilon_t+\varepsilon_{t+1}).
  \]
- Added a three-way threshold certificate: certified above threshold, certified below threshold, or unresolved.
- Added a limited explicit Hoeffding corollary for bounded IID sample-mean fingerprint coordinates, while keeping estimator-specific concentration requirements explicit for the general causal-structure coordinates.
- Added executable certification utilities and eight claim-level regression tests.
- Added a publication-style finite-sample temporal-certification figure and extended the theorem and visual roadmaps through P15.
- Expanded repository structure and visual-quality guards so all P15 artifacts are required and audited.

## 0.14.0 - 2026-09-09

### Proposition 14 - temporal continuation of intervention-resolved causal structure

- Defined a positive-weight max metric over response geometry, directed influence, and partition irreducibility fingerprints.
- Defined the relabeling-quotient distance
  \[
  \overline D_w([c],[c'])=\min_{h\in\mathcal H}D_w(c,hc')
  \]
  for a declared finite group acting by isometries.
- Proved that the quotient distance is a metric on the orbit space.
- Defined cumulative temporal path variation and maximum local structural jump.
- Proved the endpoint bound
  \[
  \overline D_w([c_s],[c_t])\le V_{s:t}.
  \]
- Proved invariance of path variation and maximum-step distance under time-dependent admissible relabelings.
- Added an explicit excursion counterexample showing that identical start and end signatures do not imply a trivial intervening temporal path.
- Added executable temporal-geometry utilities and seven claim-level tests.
- Added the publication-style temporal-continuation figure and established the future interface with certified moving world-tubes from the companion observer project.

## 0.13.0 - 2026-09-09

### Proposition 13 - pairwise component irredundancy

- Proved, on an explicit finite audit domain, that each two-component projection of the intervention-resolved causal-structure fingerprint admits a collision.
- Constructed one family with matched response geometry and directed influence but different partition irreducibility.
- Constructed one family with matched response geometry and partition irreducibility but different directed influence.
- Constructed one family with matched directed influence and partition irreducibility but different response geometry.
- Established component-level irredundancy of \(\mathcal G\), \(\mathcal A\), and \(\mathcal K\) on the declared audit domain.
- Added executable pairwise-minimality utilities and claim-level regression tests.
- Rebuilt the public research figures on larger publication-style canvases with consistent typography, spacing, terminology, and equation presentation.
- Standardized the codebase and documentation on the term **intervention-resolved causal structure** and the notation \(F_{\mathrm{causal}}\).
- Removed obsolete acronym-named and geometry-named duplicate files so the repository has one canonical terminology and one canonical path for each research object.

## 0.12.0 - 2026-09-09

### Proposition 12 - component insufficiency and minimal-feature audit

- Proved a general projection-collision no-go theorem: if a compressed feature identifies two systems that the target signature distinguishes, the target cannot factor through that compression.
- Constructed realizable collision pairs proving that response geometry alone, directed marginal influence alone, and partition irreducibility alone are each insufficient to reconstruct the full intervention-resolved causal structure.
- Added explicit counterexamples showing that response diameter, a minimum irreducibility scalar, and a cycle/no-cycle recurrence flag are not complete descriptors of the full physical candidate.
- Added executable minimality-audit utilities and regression tests for projection collisions and completeness on finite declared domains.
- Added the first visual research system: research architecture, theorem roadmap, causal-structure anatomy, component-collision map, universal-proof criteria, theory-comparison map, and Visual Research Guide.
- Synchronized the public research narrative with the P1-P12 theorem state.

## 0.11.0 - 2026-09-09

### Proposition 11 - intervention-resolved causal structure

- Introduced the first original candidate physical signature in the program as a structured intervention-response object rather than a scalar score.
- Defined intervention-conditioned response laws, response pseudometric geometry, directed interventional influence, and the complete partition-irredundancy landscape.
- Defined the representation-invariant causal-structure signature as a compatible isomorphism class of the full causal-response structure.
- Proved invariance under compatible bijective physical reparameterization.
- Proved an exact partition-factorization certificate using total-variation distance to the product of partition marginals.
- Proved the feedforward no-return certificate for acyclic directed perturbational influence graphs.
- Added executable finite discrete tools for response geometry, marginals, partition product models, directed influence, cycle detection, and outcome relabeling.
- Added claim-level tests separating response differentiation, partition irreducibility, and recurrent directed influence.
- Expanded the physical evidence base with perturbational-complexity, synergistic-information, network-controllability, causal-modeling, and non-neural causal-emergence sources.

## 0.10.0 - 2026-09-09

### Propositions 5-10 - complete-signature recovery and robust experiment design

- Proposition 5 characterized exactly when a physical feature is sufficient for a declared bridge and established a direct feature-matched counterexample criterion.
- Proposition 6 constructed the canonical complete bridge signature and proved that its fibers coincide exactly with the bridge fibers.
- Proposition 7 characterized experimental recoverability of a proposed complete signature through observable fingerprints and established the corresponding no-go condition.
- Proposition 8 introduced within-signature spread, between-signature separation, the robust signature gap, and a finite-error threshold for exact partition recovery.
- Proposition 9 converted the robust gap into an explicit categorical finite-sample sufficient bound using Hoeffding concentration and a union bound.
- Proposition 10 introduced robust protocol-family design, proved finite optimum existence, proved nonmonotonicity under added protocols, and linked the robust gap directly to the Proposition 9 trial requirement.
- Added a source-faithful comparison of IIT, GNWT, recurrent-processing, higher-order, predictive-processing, and related bridge families.
- Expanded the bibliography and equation/citation map to distinguish repository constructions, standard mathematical tools, physical assumptions, and external empirical evidence.
- Corrected the Proposition 10 controlled example to use explicitly realizable Bernoulli probability laws rather than an abstract pair-distance table.

## 0.5.0 - 2026-09-09

### Proposition 4 - optimal discriminating experiment families

- Defined pairwise protocol separation by total-variation distance.
- Defined worst-pair experiment-family separation.
- Proved the exact equivalence between positive complete separation and coverage of every distinguishable theory pair.
- Reduced minimum complete experiment-family design to a finite set-cover problem.
- Implemented finite maximin and minimum-cover experiment-design utilities.

## 0.4.0 - 2026-09-09

### Proposition 3 - observational bridge-equivalence classes

- Defined complete observable fingerprints across a declared experiment class.
- Proved observational indistinguishability is an equivalence relation on complete bridge theories.
- Proved the quotient of theory space is isomorphic to the image of the observable-fingerprint map.
- Added exact finite observational-fiber utilities and tests.

## 0.3.0 - 2026-09-09

### Proposition 2 - experiment-class bridge identifiability

- Defined experiment-class discriminability using total-variation distance.
- Proved the exact non-identifiability criterion.
- Connected one-shot equal-prior discrimination error to total variation.
- Proved repeated-experiment amplification under independent repeatability using Hoeffding concentration.
- Added the Universal Consciousness Proof Target.

## 0.2.0 - 2026-09-09

### Proposition 1 - representation-invariant consciousness bridges

- Defined the physical quotient and experiential quotient.
- Proved the bridge descends uniquely to physical equivalence classes if and only if it is constant on those classes.
- Added the physical foundation, equation/citation map, executable finite invariance checks, and tests.

## 0.1.0 - 2026-09-09

- Established the consciousness-bridge problem.
- Added candidate bridge axioms, theorem roadmap, falsification program, research architecture, and initial literature map.
