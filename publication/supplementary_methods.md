# Supplementary Methods and Theorem Provenance

## S1. Purpose

This supplement connects the journal-facing manuscript to the complete P1-P100 proof, computation, test, and figure record. It is not a second independent theory. The manuscript summarizes a selected dependency spine; this document preserves the larger audit trail and states where each main-text claim originates.

The source scientific state is the verified P100 merge commit recorded in `publication/README.md`.

## S2. Proposition architecture

The full record is organized by logical function rather than by treating every proposition as an equal-sized manuscript result.

| Range | Primary function | Main-paper role |
| --- | --- | --- |
| P1-P10 | invariance, identifiability, equivalence classes, recovery, finite-sample foundations | foundational assumptions and notation |
| P11-P18 | intervention structure, component insufficiency, time, composition, coarse-graining, scale | physical representation support |
| P19-P24 | deterministic and stochastic sufficiency, finite-data residuals, refinement and repeated looks | core sufficiency theorem |
| P25-P37 | scale-compatible influence, partitions, graph and response geometry | supplementary operational structure |
| P38-P44 | quantum-operational sufficiency, finite-data quantum tests, regularity and allocation | quantum specialization |
| P45-P60 | evidence acquisition, graph allocation, stopping, service scheduling, metric uncertainty and transition calibration | supplementary experimental-design machinery |
| P61-P70 | exact and approximate integer calibration, residual augmentation, global optimality and duality | downstream optimization branch |
| P71-P76 | target provenance, measurement robustness, multi-view identifiability and adequacy | target-validity spine |
| P77-P82 | complete model-set distance and certified continuous-family lower bounds | global rejection machinery |
| P83-P89 | increasingly complete exact parity certificates | complete linear benchmark |
| P90-P92 | nonlinear product-mixture structure and exact full-cube separation | exact nonlinear result |
| P93-P95 | localized finite-sample rejection, dependence and drift | realistic sampling layer |
| P96-P98 | holdout selection, simultaneous candidate control and cross-fitting | selection validity |
| P99 | exact e-value aggregation | within-round evidence accumulation |
| P100 | predictable reserve factors and nonnegative e-process | anytime-valid sequential inference |

The theorem roadmap is maintained in [`../docs/theorem_roadmap.md`](../docs/theorem_roadmap.md), and the proposition-by-proposition record is maintained in [`../docs/detailed_proposition_record.md`](../docs/detailed_proposition_record.md).

## S3. Exact deterministic factorization theorem

Let \(T:\mathcal M\to\mathcal Q_T\) and \(E:\mathcal M\to\mathcal Q_E\). The statement

\[
E=B_T\circ T
\]

holds for a unique \(B_T\) on \(\operatorname{Im}(T)\) if and only if

\[
T(\omega)=T(\omega')
\Rightarrow
E(\omega)=E(\omega').
\]

### Proof

Necessity follows by substitution:

\[
T(\omega)=T(\omega')
\Rightarrow
B_T(T(\omega))=B_T(T(\omega'))
\Rightarrow
E(\omega)=E(\omega').
\]

For sufficiency, assume target constancy on every fiber of \(T\). For each \(t\in\operatorname{Im}(T)\), choose any \(\omega\) such that \(T(\omega)=t\) and define

\[
B_T(t)=E(\omega).
\]

Fiber constancy makes this definition independent of the representative, so \(B_T\) is well defined and \(E=B_T\circ T\). Uniqueness follows because every point in \(\operatorname{Im}(T)\) has a preimage.

The direct scientific corollary is the exact collision witness

\[
T(\omega)=T(\omega'),
\qquad
E(\omega)\ne E(\omega').
\]

Such a collision rejects deterministic factorization through the declared \(T\). It does not reject every possible physical refinement of \(T\).

Source: [`../docs/proposition_19_fundamental_physical_sufficiency.md`](../docs/proposition_19_fundamental_physical_sufficiency.md).

## S4. Stochastic screening-off

For a finite joint law, stochastic sufficiency is

\[
E\perp\!\!\!\perp\Omega\mid T.
\]

Conditional mutual information has the representation

\[
I(E;\Omega\mid T)
=
\sum_tP(t)
D_{\rm KL}
\left(
P_{E,\Omega\mid t}
\middle\|
P_{E\mid t}P_{\Omega\mid t}
\right).
\]

Each divergence is nonnegative. Therefore

\[
I(E;\Omega\mid T)=0
\]

if and only if every positive-mass conditional joint law factorizes. A positive population residual rejects the corresponding conditional-independence model.

P20-P24 add finite-data confidence, descriptor-refinement decomposition, simultaneous refinement-chain validity, adaptive descriptor selection, and repeated-look validity under their stated assumptions.

## S5. Quantum-operational specialization

P38 specializes the same theorem to a finite-dimensional density operator \(\rho_x\). Under a declared tomographically complete measurement family,

\[
\rho_x=\rho_{x'}
\iff
\operatorname{Tr}(M\rho_x)=\operatorname{Tr}(M\rho_{x'})
\quad\forall M\in\mathcal M_{\rm tom}.
\]

An independently specified deterministic target factors through the quantum descriptor if and only if it is constant across density-operator fibers. Therefore

\[
\rho_x=\rho_{x'},
\qquad
Y(x)\ne Y(x')
\]

is an exact obstruction to factorization through the declared density operator.

The theorem does not infer that consciousness violates quantum mechanics. Omitted environmental variables, incomplete system boundaries, preparation context, inadequate tomography, or target-model error remain possible explanations.

Source: [`../docs/proposition_38_quantum_operational_sufficiency.md`](../docs/proposition_38_quantum_operational_sufficiency.md).

## S6. Target provenance and measurement channel

P71 records the circularity condition explicitly. If the target is constructed as

\[
E=h(T),
\]

then factorization through \(T\) is guaranteed by definition. Such a construction cannot independently test whether \(T\) is sufficient for a target that was supposed to have evidential status outside \(T\).

P72 separates a latent target \(E^\star\) from an observed measurement \(Y\). Under

\[
Y\perp\!\!\!\perp\Omega\mid(E^\star,T),
\]

it proves

\[
I(Y;\Omega\mid T)
\le
I(E^\star;\Omega\mid T).
\]

A positive observed residual can therefore imply a positive latent residual under the declared measurement model, while a null observed residual cannot establish latent sufficiency because the channel may erase a target distinction.

P73-P76 develop one explicit route for testing the target channel itself. Three binary views identify channel quantities under a declared conditional-independence model up to a global latent-label swap. A fourth view provides overidentifying restrictions, and P76 converts necessary restrictions into finite-sample rejection statements.

## S7. The four-view two-component product-mixture family

The worked model family is

\[
P_\theta(x)
=(1-\pi)
\prod_{j=1}^{4}P(X_j=x_j\mid S=-)
+
\pi
\prod_{j=1}^{4}P(X_j=x_j\mid S=+).
\]

There are nine continuous parameters: one prevalence and eight binary response probabilities. The observable four-bit law has 15 free probabilities. The family is therefore generically overidentified in observable space, although dimension counting alone does not characterize the real stochastic image.

P75 derives transparent moment restrictions and performs full-law reconstruction. P77 states the general confidence-set separation criterion. P78-P82 construct certified continuous-family lower bounds through exact parameter-box bounds, simplex coupling, projected events, and nested residual contrasts.

The family is a worked statistical measurement model. Its latent state is not identified with consciousness by theorem.

## S8. P89 complete linear parity benchmark

Let the 11 canonical parity coordinates be

\[
y(p)=\bigl(P_p(H_J)\bigr)_{|J|\ge2}.
\]

For real coefficients \(c\in\mathbb R^{11}\setminus\{0\}\), define

\[
Q_c(p)=c^\top y(p).
\]

For one parameter box \(B\), multi-affinity implies that the exact range of every linear parity functional is achieved at parameter vertices. With the centered transfer norm

\[
D(c)=\min_{a\in\mathbb R}
\sum_x|(Ac)_x-a|,
\]

any empirical mismatch yields

\[
\|\widehat p-q\|_\infty
\ge
\frac{\Delta_B(c)}{D(c)}.
\]

Optimizing over every real \(c\ne0\) gives the complete linear-parity certificate. On the established rational witness, matching lower and upper certificates give

\[
L_{89}=\frac{5}{168}.
\]

Source: [`../docs/proposition_89_complete_linear_parity_duality.md`](../docs/proposition_89_complete_linear_parity_duality.md).

## S9. P92 nonlinear sign-coherence theorem

### S9.1 Product-mixture invariant

Condition on \(X_1=1\) and write \(A=X_2\), \(B=X_3\), and \(C=X_4\). Every P75 law induces a nonnegative two-component product mixture on this \(2\times2\times2\) subtensor.

Define component differences

\[
\Delta_A=a_+-a_-,
\qquad
\Delta_B=b_+-b_-,
\qquad
\Delta_C=c_+-c_-.
\]

Three selected conditional determinants factor as

\[
D_{AB\mid C=1}
=
\lambda_-\lambda_+c_-c_+\Delta_A\Delta_B,
\]

\[
D_{AC\mid B=0}
=
\lambda_-\lambda_+(1-b_-)(1-b_+)\Delta_A\Delta_C,
\]

\[
D_{BC\mid A=0}
=
\lambda_-\lambda_+(1-a_-)(1-a_+)\Delta_B\Delta_C.
\]

Their product is

\[
K(\Delta_A\Delta_B\Delta_C)^2
\]

with \(K\ge0\). Hence every law in the declared family satisfies

\[
D_{AB\mid C=1}
D_{AC\mid B=0}
D_{BC\mid A=0}
\ge0.
\]

### S9.2 Synthetic violation

For the exact count law

```text
(0, 1, 0, 2, 0, 2, 1, 3, 3, 1, 0, 5, 0, 3, 0, 3) / 24
```

the three determinants are

\[
D_{AB\mid C=1}=-\frac1{48},
\qquad
D_{AC\mid B=0}=\frac1{64},
\qquad
D_{BC\mid A=0}=\frac5{192}.
\]

Their sign product is negative, so the law lies outside the complete declared family. The exact lower certificate and an explicit mixed rational P75 point meet at

\[
\boxed{
d_\infty(P_{\rm emp},\mathcal M_{75})=\frac1{24}.}
\]

This is a nonlinear model-image result. Since the complete P75 cube contains every deterministic four-bit law, its convex hull is the full simplex. Global linear separation of the complete family is therefore impossible even though nonlinear exact separation is possible.

Source: [`../docs/proposition_92_exact_global_mixed_prevalence_distance.md`](../docs/proposition_92_exact_global_mixed_prevalence_distance.md).

## S10. Finite-sample continuation P93-P95

P93 localizes the P92 witness to the cells needed by the sign-coherence calculation and derives a finite-sample rejection gate. P94 replaces independent observations with a declared finite-range dependence structure while retaining one common marginal law. P95 allows multiple predeclared drift regimes and controls their combined error.

The role of this sequence is to prevent a population-level algebraic impossibility from being reported as a finite-sample conclusion without a sampling theorem.

A finite-data outcome has three possible scientific interpretations:

1. **certified rejection:** the valid lower certificate clears its uncertainty gate;
2. **not certified:** data are insufficient to separate the model from the sampling region;
3. **assumptions violated:** dependence, drift, target validity, or another required condition does not hold.

Only the first is a rejection. The second is not acceptance.

## S11. Selection validity P96-P98

### S11.1 P96 pilot-holdout separation

A pilot sample may select a regime plan or analysis. That plan is then frozen. Independent holdout information supplies the certification event. Conditional on the pilot-selected plan, the holdout guarantee remains valid under the stated model.

### S11.2 P97 finite candidate family

A finite predeclared candidate family can support same-data selection when the rejection thresholds or evidence accounting are simultaneous across all candidates. The selected candidate does not receive a fixed-analysis guarantee for free.

### S11.3 P98 cross-fitted rotation

Independent blocks can be rotated through selection and certification roles. Each certification block must be excluded from the information used to select its own test. The resulting fold contributions can then be combined under the P98/P99 contract.

## S12. P99 e-value aggregation

An e-value is a nonnegative random variable satisfying

\[
\mathbb E_{H_0}[E]\le1.
\]

P99 constructs such a value from the cross-fitted certification record. The e-value framework is standard; the repository-specific contribution is its exact integration with the P92-P98 target-model and selection-validity chain.

For the balanced exact checkpoint, one of two folds rejects at \(\tau=1/25\). The aggregate round value is

\[
E=\frac{25}{2}.
\]

This is below the direct 5 percent threshold 20 and is therefore deliberately moderate evidence for the sequential example.

Standard references are Vovk and Wang (2021) for e-values and the broader e-value framework recorded in `references.bib`.

## S13. P100 anytime-valid e-process

Let \(E_t\) be the P99 e-value from fresh round \(t\). The essential conditional validity assumption is

\[
\mathbb E[E_t\mid\mathcal F_{t-1}]\le1.
\]

Choose a predictable stake \(\eta_t\in[0,1]\) before current certification data are revealed and define

\[
F_t=(1-\eta_t)+\eta_tE_t,
\]

\[
M_t=M_{t-1}F_t,
\qquad M_0=1.
\]

Because \(\eta_t\) is measurable with respect to the past,

\[
\mathbb E[F_t\mid\mathcal F_{t-1}]
=(1-\eta_t)+\eta_t\mathbb E[E_t\mid\mathcal F_{t-1}]
\le1.
\]

Hence

\[
\mathbb E[M_t\mid\mathcal F_{t-1}]
\le M_{t-1},
\]

and \((M_t)\) is a nonnegative supermartingale. Ville's inequality gives

\[
\Pr\left(\sup_{t\ge0}M_t\ge1/\alpha\right)\le\alpha.
\]

The first crossing of \(1/\alpha\) is therefore an anytime-valid rejection time.

### S13.1 Exact moderate-evidence checkpoint

For

\[
E_t=\frac{25}{2},
\qquad
\eta_t=\frac12,
\]

the round factor is

\[
F_t
=\frac12+\frac12\frac{25}{2}
=\frac{27}{4}.
\]

Two fresh rounds give

\[
M_2=\left(\frac{27}{4}\right)^2
=\frac{729}{16}
=45.5625.
\]

At \(\alpha=0.05\), the Ville threshold is 20, so the second round crosses while each isolated \(E_t=12.5\) remains below 20.

### S13.2 Reserve property

With \(\eta_t=1/2\) and \(E_t=0\),

\[
F_t=\frac12.
\]

A zero-evidence round reduces the accumulated process without forcing it to zero. No optimality claim is made for this stake.

### S13.3 Freshness contract

The theorem permits:

- future plans to adapt to past information;
- future stakes to adapt to past information;
- inspection after every completed round;
- stopping at a data-dependent threshold crossing.

It does not permit:

- choosing \(\eta_t\) after observing current \(E_t\);
- leaking current certification outcomes into the current plan;
- violating P98 own-fold exclusion;
- relabeling previously inspected certification data as a fresh round;
- treating unconditional per-round validity as sufficient when conditional validity fails.

Source: [`../docs/proposition_100_anytime_sequential_eprocess.md`](../docs/proposition_100_anytime_sequential_eprocess.md).

## S14. Exact synthetic sample accounting

The inherited P99 sample checkpoint has two closely related exact accounting conventions:

- mathematical crossing at 3,774 observations per relevant base accounting unit;
- exact denominator-24 replication at 3,792.

One P100 two-fold fresh round therefore requires:

\[
15096
\]

or

\[
15168
\]

unique observations, respectively. Two fresh rounds require:

\[
30192
\]

or

\[
30336.
\]

These counts are properties of the worked exact construction. They are not a universal power calculation, not an estimate of a biological effect, and not a recommended sample size for a future consciousness experiment.

## S15. Main manuscript claim-to-source map

| Main-text claim | Status | Primary repository source |
| --- | --- | --- |
| deterministic factorization iff target is constant on descriptor fibers | repository theorem | P19 |
| finite stochastic sufficiency iff conditional mutual information vanishes | standard information identity specialized in P19 | P19 plus standard information theory |
| density-operator target factorization criterion | repository specialization of factorization theorem | P38 |
| target constructed from descriptor is circular as evidence | repository methodological theorem/criterion | P71 |
| observed residual is bounded by latent residual under declared target channel | repository theorem using data processing | P72 |
| three-view channel identification up to label swap | repository theorem | P73 |
| four-view model has overidentifying restrictions | repository theorem/construction | P75 |
| complete linear parity certificate \(5/168\) on exact witness | repository computational theorem | P89 |
| complete P75 global distance \(1/24\) on exact witness | repository nonlinear theorem | P92 |
| finite-range dependence and drift-aware rejection | repository theorems | P94-P95 |
| holdout and cross-fitted selection validity | repository theorems | P96-P98 |
| e-value aggregation | standard e-value theory plus repository construction | P99 |
| predictable reserve product is an anytime-valid e-process | standard supermartingale/Ville argument plus repository integration | P100 |

## S16. Reproducibility record

The scientific source state has already passed the permanent repository validation suite on Python 3.10, 3.11, and 3.12, together with Ruff, publication-surface verification, figure regeneration with zero drift, and the end-to-end reproducibility workflow.

The publication branch does not alter the P1-P100 source theorems. Journal-facing prose should link back to the frozen proof record rather than modifying a theorem to fit the manuscript narrative.

The relevant audit files include:

- [`../docs/equation_and_citation_map.md`](../docs/equation_and_citation_map.md)
- [`../docs/claim_source_matrix.md`](../docs/claim_source_matrix.md)
- [`../docs/reference_audit.md`](../docs/reference_audit.md)
- [`../docs/figure_catalog.md`](../docs/figure_catalog.md)
- [`../docs/reproducibility.md`](../docs/reproducibility.md)
- [`../references.bib`](../references.bib)

## S17. Scientific interpretation boundary

The strongest permitted conclusion has the form:

> Under the declared descriptor, independently specified target, target-measurement model, candidate family, and statistical assumptions, the observed target law is incompatible with that declared model at the stated error level.

The following conclusions do not follow without additional evidence:

- consciousness is nonphysical;
- consciousness requires a new spacetime dimension;
- consciousness violates quantum mechanics;
- a rejected computational descriptor establishes one unique implementationist theory;
- a compatible model is true;
- a latent variable recovered by the measurement model is phenomenal consciousness itself.

These nonclaims are part of the manuscript's inferential contract.
