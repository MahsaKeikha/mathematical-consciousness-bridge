# P94 Equation Provenance and Novelty Boundary

## Scope

P94 extends P93 from IID observations to a declared finite-range dependent sequence with one common marginal four-view law.

The proposition does not claim a new general concentration inequality. The probability step is a specialized dependency-graph style Hoeffding argument. The repository-specific contribution is the exact integration of that dependence penalty with the P92 nonlinear sign-coherence obstruction, the P93 seven-cell localization, and the P79 rational certification layer.

## Provenance table

| Component | P94 use | Status |
| --- | --- | --- |
| Hoeffding's lemma for bounded independent variables | MGF bound inside each residue class | standard probability result |
| Holder's inequality | combines residue-class MGFs without assuming independence between classes | standard analysis result |
| finite-range coloring by residues modulo `m+1` | partitions an `m`-dependent sequence into independent classes | standard dependence technique |
| dependency-graph large-deviation method | external precedent for partition-based Hoeffding concentration under partial dependence | established literature |
| P92 determinant sign coherence | population model obstruction `D1 D2 D3 >= 0` | repository theorem P92 |
| P92 exact determinant sign-stability radius | converts cellwise perturbation control into sign preservation | repository theorem P92 |
| P93 seven-cell localization | restricts simultaneous concentration to exactly the cells used by the nonlinear witness | repository theorem P93 |
| P79 rational logarithm bracket | certifies the final strict squared-radius comparison | repository theorem P79 |

## External mathematical precedent

The main external precedent is:

- Svante Janson, "Large deviations for sums of partly dependent random variables," *Random Structures & Algorithms* 24(3), 234-248, 2004, DOI `10.1002/rsa.20008`.

Janson develops Hoeffding-type large-deviation bounds for variables with suitable dependency structure by decomposing the variables into independent collections. P94 does not present that concentration principle as new.

A recent finite-sample result by Chatchawan Panraksa also uses residue classes modulo `m+1` for an `m`-dependent family, in a Borel-Cantelli setting rather than the P94 concentration problem:

- Chatchawan Panraksa, "A finite-sample Borel-Cantelli inequality under m-dependence," *Statistics & Probability Letters* 236, 110775, 2026, DOI `10.1016/j.spl.2026.110775`.

This provides additional contemporary precedent for the residue-class decomposition itself.

## P94 derivation

For one selected cell indicator, P94 proves directly that

\[
\Pr\left(|\widehat P(x)-P(x)|>\varepsilon\right)
\le
2\exp\left(-\frac{2n\varepsilon^2}{m+1}\right).
\]

The proof is included in the proposition and does not depend on treating an external theorem as a black box.

A union bound over the seven P92 cells yields

\[
\varepsilon^{(m)}_{n,7}(\alpha)
=
\sqrt{\frac{(m+1)\log(14/\alpha)}{2n}}.
\]

The exact executable gate squares this radius and uses the P79 logarithm bracket:

\[
\frac{(m+1)\overline L}{2n}
<
\widehat r_{\min}^2.
\]

For the established witness, \(\widehat r_{\min}=1/24\), so at 95 percent confidence

\[
n>288(m+1)\log280.
\]

The exact code certifies the first crossings `3246` for `m=1` and `4869` for `m=2`, with first denominator-24 exact replications `3264` and `4872` respectively.

## Novelty boundary

P94 is new relative to P93 because P93's proof requires independent cell indicators across observations. P94 supplies a different MGF argument and a dependence-adjusted finite-sample certificate.

P94 is not claimed as a new universal theorem about `m`-dependent concentration. Its scientific value inside this program is narrower: the previously exact P92/P93 nonlinear model-rejection witness remains statistically usable under a declared class of short-range dependent data streams.

P94 deliberately does not extend to temporal drift. A changing marginal law creates a different inferential target because an average of time-specific P75 laws need not itself lie in the P75 family. Any later drift theorem must state and control that distinction explicitly.

## Scientific boundary

P94 is conditional on the declared dependence range and common marginal law. Non-rejection is inconclusive. The proposition does not identify the latent variable with consciousness, establish nonphysicality, validate an alternative ontology, or close the physical-to-experiential bridge.
