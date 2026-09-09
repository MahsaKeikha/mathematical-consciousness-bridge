# Changelog

This changelog records theorem-level scientific releases. Definitions, proofs, implementations, tests, figures, and documentation remain linked from the main research page.

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
