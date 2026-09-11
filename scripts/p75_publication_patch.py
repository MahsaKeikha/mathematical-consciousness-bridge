"""One-shot publication patch for integrating P75 into the existing README.

The script intentionally performs asserted, targeted edits instead of rebuilding the
long research page. It is removed before the P75 pull request leaves draft.
"""

from __future__ import annotations

import re
from pathlib import Path

README = Path("README.md")


def replace_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"expected exactly one match, found {count}: {old[:80]!r}")
    return text.replace(old, new, 1)


def insert_after(text: str, marker: str, addition: str) -> str:
    return replace_once(text, marker, marker + addition)


def main() -> None:
    text = README.read_text(encoding="utf-8")

    # Release/frontier metadata that can be updated safely wherever it occurs.
    text = text.replace("version-0.74.0-2563eb", "version-0.75.0-2563eb")
    text = text.replace("Version 0.74.0", "Version 0.75.0")
    text = text.replace("version      = {0.74.0}", "version      = {0.75.0}")
    text = text.replace("v0.74.0", "v0.75.0")
    text = text.replace("P1 through P74", "P1 through P75")
    text = text.replace("P1 to P74", "P1 to P75")
    text = text.replace("P71-P74", "P71-P75")
    text = text.replace("P73-P74", "P73-P75")
    text = text.replace("74 proposition-level results", "75 proposition-level results")
    text = text.replace("**62 equation-driven quantitative figures**", "**63 equation-driven quantitative figures**")
    text = text.replace("theorem frontier is P74", "theorem frontier is P75")
    text = text.replace("frontier: P74", "frontier: P75")

    plain_marker = (
        "In plain language, P73 asks when recovery is possible in principle; "
        "P74 asks when the available finite data justify trusting that recovery."
    )
    plain_addition = (
        "\n\nP75 asks whether successful recovery also validates the measurement model itself. "
        "It shows why the answer cannot be assumed from three binary views alone: "
        "that model is generically just-identified, so fitting it does not leave a "
        "generic independent equality check. A fourth binary view creates additional "
        "observable constraints. If those constraints fail, the target-measurement "
        "model is inadequate even if a three-view recovery looked mathematically "
        "well behaved. Passing the new checks means only that the data are compatible "
        "with the declared model, not that the model is uniquely true or that the "
        "latent state has been identified with consciousness."
    )
    text = insert_after(text, plain_marker, plain_addition)

    text = replace_once(
        text,
        "P74 adds the requirement that such recovery survive finite-data uncertainty. Others examine changes of physical scale, test quantum descriptions, design experiments, protect validity under adaptive sampling, or make experiments more efficient.",
        "P74 adds the requirement that such recovery survive finite-data uncertainty. P75 then asks whether the recovered target-measurement model survives independent adequacy checks rather than merely fitting the observations used to identify it. Others examine changes of physical scale, test quantum descriptions, design experiments, protect validity under adaptive sampling, or make experiments more efficient.",
    )

    abstract_marker = (
        "P74 is conditional on the P73 model and IID sampling; it does not validate "
        "conditional independence or the semantic meaning of the latent target."
    )
    abstract_addition = (
        "\n\nP75 separates identifiability from target-model adequacy. Three binary views "
        "and one binary latent state have equal generic continuous dimension, so "
        "successful P73 recovery does not by itself provide an independent equality-based "
        "goodness-of-fit test. A fourth binary view creates six generic overidentifying "
        "degrees of freedom. P75 derives covariance tetrads, cross-triple latent-imbalance "
        "consistency, a fourth-centered-moment relation, and a full sixteen-cell "
        "reconstruction audit. These are conditional statistical model checks, not an "
        "experiential ontology."
    )
    text = insert_after(text, abstract_marker, abstract_addition)

    finite_row = (
        "| Finite target-channel recovery | confidence set for latent and channel parameters | "
        "Are the recovered target-channel quantities supported away from the inversion singularity? | "
        "Nondegeneracy gate failure or model incompatibility, P74 |"
    )
    adequacy_row = (
        "\n| Target-model adequacy | four-view latent-model restrictions | Does the identified "
        "target-measurement model survive independent observable constraints? | Tetrad, "
        "cross-triple, fourth-moment, or full-law reconstruction failure, P75 |"
    )
    text = insert_after(text, finite_row, adequacy_row)

    p74_reading = (
        "| When is finite-sample target-channel recovery trustworthy? | "
        "[P74](docs/proposition_74_finite_sample_target_channel_recovery.md) |"
    )
    p75_reading = (
        "\n| How is the target-measurement model itself tested? | "
        "[P75](docs/proposition_75_target_model_adequacy_overidentification.md) |"
    )
    text = insert_after(text, p74_reading, p75_reading)

    text = text.replace("**P19-P24, P71-P74**", "**P19-P24, P71-P75**")
    text = text.replace("P71-P74 return to the P19 target-sufficiency lineage", "P71-P75 return to the P19 target-sufficiency lineage")
    text = text.replace("$S$ | binary latent target in P73-P74", "$S$ | binary latent target in P73-P75")
    text = text.replace("$X_j$ | target view in P73-P74", "$X_j$ | target view in P73-P75")

    # Make room for the new P75 figure while keeping sequential figure numbering.
    def bump_figure(match: re.Match[str]) -> str:
        number = int(match.group(1))
        if number >= 10:
            number += 1
        return f"**Figure {number}."

    text = re.sub(r"\*\*Figure (\d+)\.", bump_figure, text)

    p74_end = (
        "Direct proof: [Proposition 74](docs/proposition_74_finite_sample_target_channel_recovery.md). "
        "Equation classification: [P74 provenance record](docs/p74_equation_provenance.md)."
    )
    p75_section = r'''

## 1.9 P75: identifiability does not by itself validate the target model

P73 identifies a nondegenerate three-view binary latent model, and P74 asks when finite data certify that recovery. P75 asks the logically separate adequacy question: does a recovered model satisfy observable constraints that were not already consumed by identification?

For \(k\) binary observed target views, the complete observed law has

$$
d_{\mathrm{obs}}(k)=2^k-1
$$

free probabilities. One binary latent state with \(k\) binary view channels has

$$
d_{\mathrm{model}}(k)=1+2k
$$

continuous parameters. Therefore

$$
\boxed{d_{\mathrm{obs}}(3)=7=d_{\mathrm{model}}(3),}
$$

so the nondegenerate three-view model is generically just-identified. This does not mean every three-view probability law belongs to the real stochastic model. Positivity, nondegeneracy, and valid-channel restrictions still matter. It means successful three-view parameter recovery does not generically leave an independent equality constraint with which to validate the conditional-independence assumption.

A fourth binary view changes the dimension count to

$$
\boxed{15-9=6}
$$

generic overidentifying degrees of freedom. Under the declared conditional-independence model, observable pair covariances must satisfy

$$
\boxed{C_{12}C_{34}=C_{13}C_{24}=C_{14}C_{23}.}
$$

Every nondegenerate three-view subset must also recover the same latent-imbalance ratio,

$$
\boxed{
q_{ijk}=\frac{M_{ijk}^2}{C_{ij}C_{ik}C_{jk}}
=\frac{4m^2}{1-m^2},
}
$$

and the fourth centered moment must satisfy

$$
\boxed{M_{1234}=(1+q)C_{12}C_{34}}
$$

with the equivalent covariance pairings.

The executable P75 audit is stricter than checking only those displayed moment identities. It recovers an anchor P73 triple, infers the fourth binary channel, reconstructs all sixteen cells of the four-view observable law, and compares that complete reconstruction with the observed law. A synthetic residual-dependence perturbation is required to fail the audit.

![P75 target-model adequacy and four-view overidentification](docs/figures/p75_target_model_adequacy_overidentification.svg)

**Figure 10. P75 target-model adequacy theorem.** Three binary views are generically just-identified under the declared latent model. A fourth view creates six generic overidentifying degrees of freedom and observable adequacy obligations. Passing means compatibility with the declared model, not proof that the model is uniquely true, and not identification of the latent state with consciousness.

Direct proof: [Proposition 75](docs/proposition_75_target_model_adequacy_overidentification.md). Equation and literature classification: [P75 provenance record](docs/p75_equation_provenance.md).
'''
    text = insert_after(text, p74_end, p75_section)

    text = replace_once(
        text,
        "P72 applies the same philosophy on the target side. P73 establishes population identifiability for its declared three-view model, and P74 now propagates finite empirical-law uncertainty through that nonlinear inversion. This closes the specific finite-sample recovery gap left by P73 while leaving the P73 model assumptions themselves open to empirical challenge.",
        "P72 applies the same philosophy on the target side. P73 establishes population identifiability for its declared three-view model, and P74 propagates finite empirical-law uncertainty through that nonlinear inversion. P75 then makes the conditional-independence model itself falsifiable at population level by adding a fourth view and overidentifying restrictions. The remaining adequacy gap is finite-sample uncertainty around those P75 residuals and reconstruction checks.",
    )

    text = replace_once(
        text,
        "This branch remains intentionally separate from P71-P75. Better optimization can make an experiment more efficient; it cannot rescue a circular target, an invalid target-measurement channel, a nonidentified reliability model, or a finite-data recovery whose nondegeneracy gate has failed.",
        "This branch remains intentionally separate from P71-P75. Better optimization can make an experiment more efficient; it cannot rescue a circular target, an invalid target-measurement channel, a nonidentified reliability model, a finite-data recovery whose nondegeneracy gate has failed, or a target model rejected by independent adequacy constraints.",
    )

    established_marker = (
        "15. P74 certifies the latent-prevalence orbit, stability coefficients, channel offsets, "
        "and unordered latent-conditioned binary response probabilities under the declared P73 model.\n"
        "16. The experiment-design branch provides scheduling, stopping, calibration, integer optimization, "
        "and primal-dual certification without promoting those results into consciousness ontology."
    )
    established_new = (
        "15. P74 certifies the latent-prevalence orbit, stability coefficients, channel offsets, "
        "and unordered latent-conditioned binary response probabilities under the declared P73 model.\n"
        "16. P75 proves that the three-view binary latent model is generically just-identified, while a fourth binary view creates six generic overidentifying degrees of freedom.\n"
        "17. P75 derives observable tetrad, cross-triple, and fourth-moment adequacy constraints and implements a full sixteen-cell reconstruction audit for the declared four-view model.\n"
        "18. The experiment-design branch provides scheduling, stopping, calibration, integer optimization, "
        "and primal-dual certification without promoting those results into consciousness ontology."
    )
    text = replace_once(text, established_marker, established_new)

    text = text.replace(
        "- test the P73 conditional-independence and binary latent-class assumptions rather than treating them as automatically valid;",
        "- extend the P75 population adequacy restrictions into simultaneous finite-sample tests before treating conditional independence as empirically supported;",
    )
    text = text.replace(
        "- quantify uncertainty strongly enough to rule out estimation artifacts outside the present P74 model;",
        "- quantify uncertainty strongly enough to rule out estimation artifacts in the P75 adequacy residuals and in broader dependent-view models;",
    )
    old_open = (
        "The most immediate target-side problem after P74 is **model diagnostics for the three-view assumption**. "
        "P74 can certify finite-data recovery if the P73 conditional-independence model is correct, but it does not test that assumption itself. "
        "Shared rater bias, correlated reports, contextual dependence, temporal drift, or hidden common causes can violate the factorization while still producing superficially persuasive agreement."
    )
    new_open = (
        "The most immediate target-side problem after P75 is **finite-sample certification of model adequacy**. "
        "P75 makes the P73-P74 conditional-independence model falsifiable at population level by adding a fourth view, but finite experiments still need simultaneous uncertainty bounds for the tetrad, cross-triple, fourth-moment, and full-law reconstruction discrepancies. Shared rater bias, correlated reports, contextual dependence, temporal drift, or hidden common causes remain important alternatives that a target-measurement protocol must be designed to expose."
    )
    text = replace_once(text, old_open, new_open)

    p74_falsification = (
        "| Finite target-channel recovery is certified | P74 covariance gate fails, sign structure is incompatible, "
        "or confidence sets remain too wide | Nonzero plug-in covariance or a precise-looking point estimate |"
    )
    p75_falsification = (
        "\n| Target-measurement model is adequate | P75 tetrad, cross-triple, fourth-moment, or full-law reconstruction constraints fail | Successful three-view parameter recovery by itself |"
    )
    text = insert_after(text, p74_falsification, p75_falsification)

    p74_evidence = (
        "| [P74 equation and provenance record](docs/p74_equation_provenance.md) | Finite-sample concentration, "
        "nondegeneracy, full-channel interval recovery, and equation classification |"
    )
    p75_evidence = (
        "\n| [P75 equation and provenance record](docs/p75_equation_provenance.md) | Just-identification, four-view overidentification, model-invariant context, moment consistency, and full-law reconstruction provenance |"
    )
    text = insert_after(text, p74_evidence, p75_evidence)

    text = text.replace(
        "Dawid and Skene (1979) and Allman, Matias, and Rhodes (2009) provide methodological context for latent observer-error models and latent-structure identifiability. Their general results are not claimed as repository-original contributions.",
        "Dawid and Skene (1979) and Allman, Matias, and Rhodes (2009) provide methodological context for latent observer-error models and latent-structure identifiability. Garcia, Stillman, and Sturmfels (2005) and Drton, Sturmfels, and Sullivant (2009) provide algebraic-statistics context for hidden-variable model constraints and invariants. Their general results are not claimed as repository-original contributions.",
    )

    text = replace_once(
        text,
        "**[Read the complete P1 to P75 detailed proposition record](docs/detailed_proposition_record.md).**",
        "**[Read the complete P1 to P75 detailed proposition record](docs/detailed_proposition_record.md).**",
    )

    text = text.replace("| Public theorem frontier | **P74** |", "| Public theorem frontier | **P75** |")
    text = text.replace("| Proposition-level results | **74** |", "| Proposition-level results | **75** |")
    text = text.replace("| Equation-driven quantitative figures | **62** |", "| Equation-driven quantitative figures | **63** |")

    p74_status = (
        "| Finite-sample target-channel recovery | **P74 proved under the P73 model plus IID sampling, with explicit nondegeneracy gating** |"
    )
    p75_status = (
        "\n| Target-model adequacy | **P75 proved at population level for the declared binary four-view extension, with six generic overidentifying degrees of freedom and full-law reconstruction** |"
    )
    text = insert_after(text, p74_status, p75_status)

    text = text.replace(
        "channel identifiability, finite-data recovery, admissible bridge class, and experiment",
        "channel identifiability, finite-data recovery, target-model adequacy, admissible bridge class, and experiment",
    )

    p74_nav = (
        "| Inspect finite-sample target-channel recovery | [P74](docs/proposition_74_finite_sample_target_channel_recovery.md) |"
    )
    p75_nav = (
        "\n| Inspect target-model adequacy and four-view overidentification | [P75](docs/proposition_75_target_model_adequacy_overidentification.md) |"
    )
    text = insert_after(text, p74_nav, p75_nav)

    p74_prov_nav = (
        "| Audit P74 finite-data recovery equations | [P74 equation and provenance record](docs/p74_equation_provenance.md) |"
    )
    p75_prov_nav = (
        "\n| Audit P75 model-adequacy equations | [P75 equation and provenance record](docs/p75_equation_provenance.md) |"
    )
    text = insert_after(text, p74_prov_nav, p75_prov_nav)

    # Final explicit citation/frontier replacements not covered by contextual edits.
    text = text.replace("Current documented theorem frontier: P74", "Current documented theorem frontier: P75")

    if "P75 target-model adequacy theorem" not in text:
        raise RuntimeError("P75 section was not inserted")
    if "P1 through P75 with explicit dependency branches" not in text:
        raise RuntimeError("README frontier phrase not advanced")
    if "75 proposition-level results" not in text:
        raise RuntimeError("README result count not advanced")
    if "p75_target_model_adequacy_overidentification.svg" not in text:
        raise RuntimeError("P75 figure missing from README")
    if "\u2013" in text or "\u2014" in text:
        raise RuntimeError("forbidden dash character introduced")

    README.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
