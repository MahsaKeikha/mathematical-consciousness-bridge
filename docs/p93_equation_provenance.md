# P93 Equation Provenance

## Scope

This note records the origin and status of the equations used in Proposition 93, the localized finite-sample sign-coherence rejection theorem.

P93 is repository-original as a specific finite-sample handoff from the P92 nonlinear three-minor invariant to an exact, seven-cell, confidence-valid rejection gate. Its ingredients include standard Hoeffding concentration, a standard union bound, the P92 determinant sign-stability formula, and the P79 exact-rational numerical envelope.

P93 does not claim those standard probability tools as new mathematics.

---

## Equation record

| Equation or construction | Status | Provenance |
| --- | --- | --- |
| Seven selected P92 cells | repository-specific reduction | direct audit of the three P92 minors |
| \(\varepsilon_{n,7}(\alpha)=\sqrt{\log(14/\alpha)/(2n)}\) | standard concentration consequence | Hoeffding inequality plus union bound over seven Bernoulli cell indicators |
| \(r(M)=|ad-bc|/(a+b+c+d)\) | inherited exact theorem | P92 determinant sign-stability lemma |
| Negative empirical three-minor product | inherited witness structure | P92 empirical sign-coherence obstruction |
| \(\overline\varepsilon_{n,7,\alpha}<\min_i\widehat r_i\) | P93 rejection gate | simultaneous seven-cell confidence event plus P92 sign stability plus P79 one-sided radius certification |
| Confidence level at least \(1-\alpha\) | standard confidence-set logic | one simultaneous union-bound event, with no later multiplicity spending |
| Witness condition \(n>288\log(14/\alpha)\) | direct algebra | substitute the exact P92 minimum radius \(1/24\) into the seven-cell radius inequality |
| 1622/1623 crossing at \(\alpha=1/20\) | P93 exact numerical certificate | P79 rational lower envelope at 1622 and rational upper envelope at 1623 |
| First exact profile replication \(n=1632=68\times24\) | arithmetic corollary | smallest multiple of 24 at or above the 1623 mathematical crossing |
| Generic P77 comparison 7443/7444 | comparison corollary | P77 fixed-margin condition with \(K=16\), \(\tau=1/24\), and P79 exact radius envelopes |

---

## Why P93 is not a restatement of P76

P76 propagates one sixteen-cell confidence event through a selected family of covariance tetrads, cross-triple polynomials, and fourth-moment polynomial constraints inherited from P75.

P92 discovered a different nonlinear obstruction after P76: a sign-coherence product across three conditional two-by-two determinants. P93 is the first finite-sample theorem specialized to that later invariant.

Therefore P93 adds a new rejection route rather than renaming a P76 interval.

---

## Why P93 is not a restatement of P77

P77 gives the generic full-law model-set rule

\[
d_\infty(\widehat P,\mathcal M)>arepsilon_{n,16}(\alpha)
\]

and a fixed-population-margin design theorem.

P93 does not recompute the full model distance. It uses only seven selected empirical cell frequencies and the local sign geometry of three P92 minors. Its rejection event can therefore clear at a substantially smaller sample size for the established profile.

The P77 and P93 guarantees remain different:

- P77 is a generic complete-model-set separation theorem.
- P93 is a specialized observed-data certificate for one exact nonlinear model invariant.

---

## Why P93 still needs P79

The sign-stability radii are exact rational quantities. The simultaneous Hoeffding radius contains logarithm and square root operations.

An ordinary floating result is not sufficient for a strict rejection comparison. P93 therefore uses P79 to obtain

\[
\varepsilon_{n,7}(\alpha)
\le
\overline\varepsilon_{n,7,\alpha}
\]

with an exact rational upper endpoint.

For the threshold audit, P79 also gives exact rational lower endpoints, allowing P93 to prove that 1622 is still above \(1/24\) while 1623 is below it.

---

## Reproducibility

Executable implementation:

- `src/consciousness_bridge/localized_sign_coherence_rejection.py`

Regression tests:

- `tests/test_localized_sign_coherence_rejection.py`

Immediate mathematical dependencies:

- `docs/proposition_92_exact_global_mixed_prevalence_distance.md`
- `docs/proposition_77_full_law_model_set_separation.md`
- `docs/proposition_79_certified_sampling_radius.md`

---

## Scientific boundary

P93 is a conditional finite-sample model-rejection theorem under IID sampling and the declared P75 statistical model family.

It does not establish that the latent state is consciousness, that non-rejection validates the model, that consciousness is nonphysical, or that the physical-to-experiential bridge has been solved.

The physical-to-experiential bridge remains open.
