"""One-shot release polish for P71-P75 history and central provenance routing.

This helper is removed before the P75 pull request leaves draft.
"""

from pathlib import Path

CHANGELOG = Path("CHANGELOG.md")
MAP = Path("docs/equation_and_citation_map.md")


def update_changelog() -> None:
    text = CHANGELOG.read_text(encoding="utf-8")
    if text.startswith("# 0.75.0 - 2026-09-10"):
        return

    prefix = """# 0.75.0 - 2026-09-10

- Added P75 target-model adequacy and four-view overidentification as the population-level adequacy continuation of the P71-P74 target-side branch.
- Separated parameter identifiability from model validation by showing that the nondegenerate three-binary-view latent model is generically just-identified, while four binary views provide six generic overidentifying degrees of freedom.
- Derived observable covariance-tetrad, cross-triple latent-imbalance, and fourth-centered-moment consistency obligations and added a full sixteen-cell reconstruction audit.
- Added a synthetic residual-dependence counterexample that must fail the declared four-view target-measurement model.
- Added proof, implementation, regression tests, theorem visual, geometry guards, provenance record, v0.75.0 citation metadata, README integration, navigation/roadmap updates, and website integration.
- Kept the scientific boundary explicit: passing P75 establishes compatibility with the declared target-measurement model, not uniqueness, experiential semantics, or a physical-to-experiential bridge.

# 0.74.0 - 2026-09-10

- Added P74 finite-sample target-channel recovery certification as the finite-data continuation of P73.
- Propagated one simultaneous confidence event for the observed eight-cell law through the nonlinear P73 inversion.
- Added a covariance nondegeneracy gate that refuses unstable recovery near the P73 singular set.
- Certified latent-prevalence orbits, P72 stability coefficients, label-invariant loading-times-latent-mean products, channel offsets, and unordered latent-conditioned binary response-probability pairs.
- Added proof, implementation, tests, theorem visual, publication integration, and v0.74.0 release metadata while keeping semantic latent-label orientation external to the statistical recovery.

# 0.73.0 - 2026-09-10

- Added P73 three-view target-channel identifiability under a declared nondegenerate binary latent conditional-independence model.
- Derived explicit population moment inversion for latent prevalence and all three binary view channels up to the unavoidable global latent-label swap.
- Identified the P72 single-view target-channel stability coefficients despite that label symmetry.
- Added a constructive two-view non-identifiability boundary showing that two uncalibrated binary views do not generally determine their individual reliabilities.
- Added proof, implementation, tests, theorem visual, provenance, navigation, and v0.73.0 publication integration.

# 0.72.0 - 2026-09-10

- Added P72 target-measurement channel robustness, separating an independently justified latent target from its noisy observation.
- Proved one-way conditional-information residual transfer under the declared nondifferential target-channel condition and gave an explicit witness-erasure counterexample for the converse.
- Added total-variation contraction and target-channel stability bounds, including exact binary-symmetric attenuation.
- Added a conservative finite-sample target-separation certificate and explicit scientific boundaries on latent-target interpretation.
- Added proof, implementation, tests, theorem visual, provenance, navigation, and v0.72.0 publication integration.

# 0.71.0 - 2026-09-10

- Added P71 target-provenance non-circularity as a return from downstream calibration to the core P19 bridge-sufficiency problem.
- Proved deterministic descriptor-derived target vacuity, stochastic descriptor-only channel vacuity, and the learned-target corollary.
- Proved provenance non-identifiability: a zero observed conditional residual is observationally compatible with a descriptor-only target-generation mechanism.
- Added the non-vacuity rule that target provenance is a protocol/design requirement rather than a statistic inferred from the observed joint law alone.
- Added proof, implementation, tests, theorem visual, provenance, navigation, and v0.71.0 publication integration.

"""
    CHANGELOG.write_text(prefix + text, encoding="utf-8")


def update_equation_map() -> None:
    text = MAP.read_text(encoding="utf-8")
    marker = "# 60. P71-P75 target-side provenance routing"
    if marker in text:
        return

    addition = r'''

---

# 60. P71-P75 target-side provenance routing

P71-P75 return from the downstream calibration branch to the target side of the P19 physical-sufficiency problem. Their detailed equation classifications are maintained in dedicated proposition/provenance records because the target-side branch combines information theory, latent-variable identification, finite-sample inference, and algebraic model diagnostics.

| Result | Core equation or object | Status | Detailed provenance |
| --- | --- | --- | --- |
| P71 | \(E=h(T)\Rightarrow I(E;\Omega\mid T)=0\) for descriptor-derived targets | repository theorem assembled from standard factorization/CMI facts | [P71 proof](proposition_71_target_provenance_noncircularity.md) and [P71 equation/citation map](p71_equation_and_citation_map.md) |
| P72 | \(I(Y;\Omega\mid T)\le I(E^\star;\Omega\mid T)\) under the declared nondifferential measurement channel | conditional data-processing consequence plus repository target-measurement synthesis | [P72 provenance](p72_equation_provenance.md) |
| P73 | \(q=M_{123}^2/(C_{12}C_{13}C_{23})\), with explicit three-view latent-channel inversion | conditional population-identification theorem using standard latent-class/moment methodology | [P73 provenance](p73_equation_provenance.md) |
| P74 | simultaneous finite-sample confidence propagation through the P73 inversion and covariance nondegeneracy gate | repository finite-data certificate built from standard concentration plus explicit nonlinear interval propagation | [P74 provenance](p74_equation_provenance.md) |
| P75 | three-view just-identification, four-view six-degree overidentification, tetrads, cross-triple consistency, fourth-moment consistency, and full-law reconstruction | conditional model-adequacy theorem with established algebraic-statistics context | [P75 provenance](p75_equation_provenance.md) |

The target-side methodological chain is therefore:

\[
\boxed{
\text{non-circular provenance}
\to
\text{measurement robustness}
\to
\text{channel identifiability}
\to
\text{finite recovery}
\to
\text{model adequacy}
}
\]

This sequence does not identify the latent target with consciousness and does not close the physical-to-experiential bridge. It specifies additional obligations that any target-side evidence must satisfy before it can support a bridge claim.
'''
    MAP.write_text(text.rstrip() + addition + "\n", encoding="utf-8")


def main() -> None:
    update_changelog()
    update_equation_map()


if __name__ == "__main__":
    main()
