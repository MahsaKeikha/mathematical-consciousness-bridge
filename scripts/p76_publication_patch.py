from pathlib import Path
import re


def load(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def save(path: str, text: str) -> None:
    Path(path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, *, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


def replace_all(text: str, old: str, new: str, *, minimum: int = 1, label: str) -> str:
    count = text.count(old)
    if count < minimum:
        raise RuntimeError(f"{label}: expected at least {minimum} matches, found {count}")
    return text.replace(old, new)


def increment_readme_figures(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        number = int(match.group(1))
        if number >= 11:
            return f"**Figure {number + 1}."
        return match.group(0)

    return re.sub(r"\*\*Figure (\d+)\.", repl, text)


def patch_source() -> None:
    path = "src/consciousness_bridge/finite_sample_target_model_adequacy.py"
    text = load(path)
    text = replace_once(
        text,
        "P76 propagates one simultaneous\nsixteen-cell confidence event through those polynomial restrictions.",
        "P76 propagates one shared sixteen-cell Hoeffding event through those polynomial restrictions. This is not an acceptance test.",
        label="source shared-event wording",
    )
    save(path, text)


def patch_readme() -> None:
    path = "README.md"
    text = load(path)
    text = increment_readme_figures(text)
    text = replace_once(text, "version-0.75.0-2563eb", "version-0.76.0-2563eb", label="README badge")
    text = replace_all(text, "P71-P75", "P71-P76", minimum=2, label="README target range")
    text = replace_all(text, "P73-P75", "P73-P76", minimum=2, label="README latent range")
    text = replace_all(text, "P1 through P75", "P1 through P76", minimum=1, label="README full range")
    text = replace_all(text, "75 proposition-level results", "76 proposition-level results", minimum=1, label="README proposition count")
    text = replace_all(text, "63 equation-driven quantitative figures", "64 equation-driven quantitative figures", minimum=1, label="README figure count prose")

    p75_plain = "P75 asks whether successful recovery also validates the measurement model itself. It shows why the answer cannot be assumed from three binary views alone: that model is generically just-identified, so fitting it does not leave a generic independent equality check. A fourth binary view creates additional observable constraints. If those constraints fail, the target-measurement model is inadequate even if a three-view recovery looked mathematically well behaved. Passing the new checks means only that the data are compatible with the declared model, not that the model is uniquely true or that the latent state has been identified with consciousness."
    p76_plain = """P76 asks the next practical question: **if those model checks are applied to finite data, is an apparent failure large enough to distinguish from ordinary sampling noise?** It places the complete sixteen-cell observed table inside one shared confidence event and carries that uncertainty into the P75 adequacy constraints. If a required constraint is separated from zero even after uncertainty is included, the declared measurement model can be rejected with controlled confidence. If the data do not reject it, P76 deliberately does not call the model validated: non-rejection is not model acceptance. The sample may simply be too small, the violation may be too subtle, or the failure may lie outside the particular constraints being tested. In plain language, P75 explains what a valid four-view model must satisfy at the population level; P76 asks when finite data are strong enough to demonstrate that one of those requirements has genuinely failed."""
    text = replace_once(text, p75_plain, p75_plain + "\n\n" + p76_plain, label="README plain P76")

    architecture_old = "P74 adds the requirement that such recovery survive finite-data uncertainty. P75 then asks whether the recovered target-measurement model survives independent adequacy checks rather than merely fitting the observations used to identify it. Others examine changes of physical scale, test quantum descriptions, design experiments, protect validity under adaptive sampling, or make experiments more efficient."
    architecture_new = "P74 adds the requirement that such recovery survive finite-data uncertainty. P75 then asks whether the recovered target-measurement model survives independent adequacy checks rather than merely fitting the observations used to identify it. P76 adds the requirement that an apparent adequacy failure survive finite-sample uncertainty before it is called a model rejection. Others examine changes of physical scale, test quantum descriptions, design experiments, protect validity under adaptive sampling, or make experiments more efficient."
    text = replace_once(text, architecture_old, architecture_new, label="README plain architecture")

    status_old = "The research currently contains **76 proposition-level results** and **64 equation-driven quantitative figures**. The theorem frontier is P75."
    status_new = "The research currently contains **76 proposition-level results** and **64 equation-driven quantitative figures**. The theorem frontier is P76."
    text = replace_once(text, status_old, status_new, label="README plain status")

    p75_abstract = "P75 separates identifiability from target-model adequacy. Three binary views and one binary latent state have equal generic continuous dimension, so successful P73 recovery does not by itself provide an independent equality-based goodness-of-fit test. A fourth binary view creates six generic overidentifying degrees of freedom. P75 derives covariance tetrads, cross-triple latent-imbalance consistency, a fourth-centered-moment relation, and a full sixteen-cell reconstruction audit. These are conditional statistical model checks, not an experiential ontology."
    p76_abstract = """P76 adds finite-sample target-model rejection. From one IID sample of the sixteen-cell four-view law, a shared Hoeffding event controls the full empirical distribution and every binary raw moment simultaneously. The theorem propagates that event to covariance tetrads and to denominator-free polynomial forms of the P75 cross-triple and fourth-moment constraints. If any necessary-constraint interval excludes zero, the declared P75 target-measurement model is rejected with confidence at least $1-\\alpha$. Non-rejection remains inconclusive and is not model acceptance."""
    text = replace_once(text, p75_abstract, p75_abstract + "\n\n" + p76_abstract, label="README abstract P76")

    text = replace_once(
        text,
        "Likewise, a latent target symbol such as $E^\\star$ or $S$ is not a declaration of experiential ground truth. P71-P76 formalize separate requirements on target provenance, observation, channel identifiability, and finite-data recovery before such a target can carry bridge evidence.",
        "Likewise, a latent target symbol such as $E^\\star$ or $S$ is not a declaration of experiential ground truth. P71-P76 formalize separate requirements on target provenance, observation, channel identifiability, finite-data recovery, model adequacy, and finite-sample model rejection before such a target can carry bridge evidence.",
        label="README status discipline",
    )

    target_row = "| Target-model adequacy | four-view latent-model restrictions | Does the identified target-measurement model survive independent observable constraints? | Tetrad, cross-triple, fourth-moment, or full-law reconstruction failure, P75 |"
    finite_row = "| Finite target-model adequacy | simultaneous P75 constraint intervals | Is an apparent adequacy failure larger than finite-sample uncertainty? | Any necessary-constraint interval excludes zero, P76 |"
    text = replace_once(text, target_row, target_row + "\n" + finite_row, label="README core table P76")

    p75_reader = "| How is the target-measurement model itself tested? | [P75](docs/proposition_75_target_model_adequacy_overidentification.md) |"
    p76_reader = "| When can finite data actually reject that target model? | [P76](docs/proposition_76_finite_sample_target_model_adequacy.md) |"
    text = replace_once(text, p75_reader, p75_reader + "\n" + p76_reader, label="README reader row P76")

    text = replace_once(
        text,
        "| 3. Bridge sufficiency and target validity | **P19-P24, P71-P76** |",
        "| 3. Bridge sufficiency and target validity | **P19-P24, P71-P76** |",
        label="README glance P76",
    )
    text = replace_once(
        text,
        "Proposition numbers preserve development order, while the dependency map shows scientific order. P71-P76 return to the P19 target-sufficiency lineage; P61-P70 remains a separate downstream optimization branch.",
        "Proposition numbers preserve development order, while the dependency map shows scientific order. P71-P76 return to the P19 target-sufficiency lineage; P61-P70 remains a separate downstream optimization branch.",
        label="README map caption no-op guard",
    )

    text = replace_once(
        text,
        "| $S$ | binary latent target in P73-P76 | statistical latent variable whose semantic meaning requires independent justification |\n| $X_j$ | target view in P73-P76 | one of three declared binary observations used to identify and certify target-channel quantities under the model |",
        "| $S$ | binary latent target in P73-P76 | statistical latent variable whose semantic meaning requires independent justification |\n| $X_j$ | target view in P73-P76 | one of the declared binary observations used to identify, certify, and test target-channel models under explicit assumptions |",
        label="README symbol table",
    )

    p75_end = "Direct proof: [Proposition 75](docs/proposition_75_target_model_adequacy_overidentification.md). Equation and literature classification: [P75 provenance record](docs/p75_equation_provenance.md)."
    p76_section = r"""

## 1.10 P76: finite data must separate model failure from sampling noise

P75 gives population-level restrictions. P76 asks when a finite IID sample is already strong enough to reject the declared four-view target-measurement model.

For the empirical sixteen-cell law $\widehat P$, define

$$
\varepsilon_n(\alpha)=\sqrt{\frac{\log(32/\alpha)}{2n}},
\qquad
\boxed{\delta_n(\alpha)=\min\{2,16\varepsilon_n(\alpha)\}.}
$$

With probability at least $1-\alpha$, the same event controls every binary raw monomial moment. In particular, every pair covariance satisfies

$$
\boxed{|\widehat C_{ij}-C_{ij}|\le3\delta_n.}
$$

For either P75 tetrad residual $D$, P76 obtains

$$
\boxed{|\widehat D-D|\le12\delta_n.}
$$

Therefore

$$
\boxed{|\widehat D|>12\delta_n\quad\Longrightarrow\quad D\ne0}
$$

on the shared confidence event, which certifies incompatibility with the declared P75 model. P76 also rewrites the P75 cross-triple and fourth-moment consistency conditions as denominator-free polynomials and propagates the same empirical-law event through interval arithmetic. This avoids unstable division by uncertain covariance products.

![P76 finite-sample target-model adequacy rejection](docs/figures/p76_finite_sample_target_model_adequacy.svg)

**Figure 11. P76 finite-sample adequacy rejection.** One simultaneous sixteen-cell confidence event controls the raw moments and the P75 polynomial constraints. Excluding zero from any necessary-constraint interval certifies model incompatibility. If no interval excludes zero, the result remains inconclusive; it is not model acceptance and does not identify the latent state with consciousness.

Direct proof: [Proposition 76](docs/proposition_76_finite_sample_target_model_adequacy.md). Equation and literature classification: [P76 provenance record](docs/p76_equation_provenance.md).
"""
    text = replace_once(text, p75_end, p75_end + p76_section, label="README P76 theorem section")

    finite_old = "P72 applies the same philosophy on the target side. P73 establishes population identifiability for its declared three-view model, and P74 propagates finite empirical-law uncertainty through that nonlinear inversion. P75 then makes the conditional-independence model itself falsifiable at population level by adding a fourth view and overidentifying restrictions. The remaining adequacy gap is finite-sample uncertainty around those P75 residuals and reconstruction checks."
    finite_new = "P72 applies the same philosophy on the target side. P73 establishes population identifiability for its declared three-view model, and P74 propagates finite empirical-law uncertainty through that nonlinear inversion. P75 then makes the conditional-independence model itself falsifiable at population level by adding a fourth view and overidentifying restrictions. P76 adds a simultaneous finite-sample rejection certificate for the tracked P75 polynomial constraints. A stronger finite-data full-law membership test and higher-power alternatives remain open."
    text = replace_once(text, finite_old, finite_new, label="README finite experiment P76")

    text = replace_once(
        text,
        "This branch remains intentionally separate from P71-P76. Better optimization can make an experiment more efficient; it cannot rescue a circular target, an invalid target-measurement channel, a nonidentified reliability model, a finite-data recovery whose nondegeneracy gate has failed, or a target model rejected by independent adequacy constraints.",
        "This branch remains intentionally separate from P71-P76. Better optimization can make an experiment more efficient; it cannot rescue a circular target, an invalid target-measurement channel, a nonidentified reliability model, a finite-data recovery whose nondegeneracy gate has failed, or a target model rejected by finite-sample adequacy evidence.",
        label="README calibration boundary",
    )

    established_old = "17. P75 derives observable tetrad, cross-triple, and fourth-moment adequacy constraints and implements a full sixteen-cell reconstruction audit for the declared four-view model.\n18. The experiment-design branch provides scheduling, stopping, calibration, integer optimization, and primal-dual certification without promoting those results into consciousness ontology."
    established_new = "17. P75 derives observable tetrad, cross-triple, and fourth-moment adequacy constraints and implements a full sixteen-cell reconstruction audit for the declared four-view model.\n18. P76 turns the tracked P75 population constraints into simultaneous finite-sample rejection intervals from one sixteen-cell Hoeffding event, while keeping non-rejection explicitly inconclusive.\n19. The experiment-design branch provides scheduling, stopping, calibration, integer optimization, and primal-dual certification without promoting those results into consciousness ontology."
    text = replace_once(text, established_old, established_new, label="README established P76")

    text = replace_once(
        text,
        "- extend the P75 population adequacy restrictions into simultaneous finite-sample tests before treating conditional independence as empirically supported;",
        "- extend P76 beyond the tracked necessary polynomials to sharper finite-sample full-law and power-aware adequacy procedures;",
        label="README open bullet P76",
    )
    text = replace_once(
        text,
        "- quantify uncertainty strongly enough to rule out estimation artifacts in the P75 adequacy residuals and in broader dependent-view models;",
        "- sharpen finite-sample power and uncertainty control for broader dependent-view and learned target-measurement models;",
        label="README open power bullet",
    )
    open_old = "The most immediate target-side problem after P75 is **finite-sample certification of model adequacy**. P75 makes the P73-P74 conditional-independence model falsifiable at population level by adding a fourth view, but finite experiments still need simultaneous uncertainty bounds for the tetrad, cross-triple, fourth-moment, and full-law reconstruction discrepancies. Shared rater bias, correlated reports, contextual dependence, temporal drift, or hidden common causes remain important alternatives that a target-measurement protocol must be designed to expose."
    open_new = "The most immediate target-side problem after P76 is **stronger finite-sample model-adequacy characterization and power**. P76 supplies a simultaneous rejection certificate for tracked necessary P75 polynomial constraints, but it does not yet provide a complete finite-sample confidence test for the full sixteen-cell model image or an optimal-power procedure. Shared rater bias, correlated reports, contextual dependence, temporal drift, hidden common causes, and learned measurement pipelines remain important alternatives that a target-measurement protocol must be designed to expose."
    text = replace_once(text, open_old, open_new, label="README open frontier P76")

    adequacy_row = "| Target-measurement model is adequate | P75 tetrad, cross-triple, fourth-moment, or full-law reconstruction constraints fail | Successful three-view parameter recovery by itself |"
    finite_adequacy_row = "| Finite data reject the target model | A P76 simultaneous necessary-constraint interval excludes zero | Treating non-rejection as model acceptance |"
    text = replace_once(text, adequacy_row, adequacy_row + "\n" + finite_adequacy_row, label="README falsification P76")

    p75_prov = "| [P75 equation and provenance record](docs/p75_equation_provenance.md) | Just-identification, four-view overidentification, model-invariant context, moment consistency, and full-law reconstruction provenance |"
    p76_prov = "| [P76 equation and provenance record](docs/p76_equation_provenance.md) | Sixteen-cell concentration, denominator-free polynomial intervals, and finite-sample adequacy rejection provenance |"
    text = replace_once(text, p75_prov, p75_prov + "\n" + p76_prov, label="README provenance P76")

    text = replace_once(
        text,
        "**[Read the complete P1 to P75 detailed proposition record](docs/detailed_proposition_record.md).**",
        "**[Read the complete P1 to P76 detailed proposition record](docs/detailed_proposition_record.md).**",
        label="README detailed link no-op guard",
    )

    status_table_old = "| Public theorem frontier | **P75** |\n| Documented version | **v0.75.0** |\n| Proposition-level results | **75** |\n| Equation-driven quantitative figures | **63** |"
    status_table_new = "| Public theorem frontier | **P76** |\n| Documented version | **v0.76.0** |\n| Proposition-level results | **76** |\n| Equation-driven quantitative figures | **64** |"
    text = replace_once(text, status_table_old, status_table_new, label="README current status")
    p75_status = "| Target-model adequacy | **P75 proved at population level for the declared binary four-view extension, with six generic overidentifying degrees of freedom and full-law reconstruction** |"
    p76_status = "| Finite-sample target-model adequacy | **P76 proved under IID sampling as a simultaneous one-sided rejection certificate for tracked P75 necessary constraints** |"
    text = replace_once(text, p75_status, p75_status + "\n" + p76_status, label="README status row P76")
    text = replace_once(
        text,
        "The scientific target is precise: continue reducing ambiguity in the physical description, target provenance, target measurement, channel identifiability, finite-data recovery, target-model adequacy, admissible bridge class, and experiment",
        "The scientific target is precise: continue reducing ambiguity in the physical description, target provenance, target measurement, channel identifiability, finite-data recovery, target-model adequacy, finite-sample adequacy, admissible bridge class, and experiment",
        label="README scientific target",
    )

    nav_p75 = "| Inspect target-model adequacy and four-view overidentification | [P75](docs/proposition_75_target_model_adequacy_overidentification.md) |"
    nav_p76 = "| Inspect finite-sample target-model adequacy rejection | [P76](docs/proposition_76_finite_sample_target_model_adequacy.md) |"
    text = replace_once(text, nav_p75, nav_p75 + "\n" + nav_p76, label="README nav P76")
    audit_p75 = "| Audit P75 model-adequacy equations | [P75 equation and provenance record](docs/p75_equation_provenance.md) |"
    audit_p76 = "| Audit P76 finite-sample adequacy equations | [P76 equation and provenance record](docs/p76_equation_provenance.md) |"
    text = replace_once(text, audit_p75, audit_p75 + "\n" + audit_p76, label="README nav provenance P76")

    text = replace_all(text, "Version 0.75.0", "Version 0.76.0", minimum=1, label="README citation version")
    text = replace_all(text, "version      = {0.75.0}", "version      = {0.76.0}", minimum=1, label="README BibTeX version")
    text = replace_once(
        text,
        "note         = {Ongoing research program. Current documented theorem frontier: P75.}",
        "note         = {Ongoing research program. Current documented theorem frontier: P76.}",
        label="README BibTeX frontier",
    )
    save(path, text)


def patch_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = load(path)
    text = replace_once(
        text,
        "The current documented theorem frontier is **P75**. The proposition record runs from **P1 through P75 with explicit dependency branches**. P71-P75 return to the core P19 bridge-sufficiency lineage; they do not extend the P61-P70 calibration branch.",
        "The current documented theorem frontier is **P76**. The proposition record runs from **P1 through P76 with explicit dependency branches**. P71-P76 return to the core P19 bridge-sufficiency lineage; they do not extend the P61-P70 calibration branch.",
        label="roadmap intro",
    )
    chain_old = "&\\text{P75: the target-measurement model must face overidentifying adequacy tests}\n\\end{aligned}"
    chain_new = "&\\text{P75: the target-measurement model must face overidentifying adequacy tests}\\\\\n&\\Downarrow\\\\\n&\\text{P76: finite data must separate adequacy failure from sampling noise}\n\\end{aligned}"
    text = replace_once(text, chain_old, chain_new, label="roadmap chain P76")
    text = replace_once(
        text,
        "The proposition number records development order. It does not imply that P75 depends on P70. P75 depends scientifically on P19 and the P71-P74 target-side lineage, especially the P73 binary latent model whose adequacy it tests.",
        "The proposition number records development order. It does not imply that P76 depends on P70. P76 depends scientifically on P75, which in turn depends on P19 and the P71-P74 target-side lineage.",
        label="roadmap dependency wording",
    )
    p75_end = "Direct proof: [P75](proposition_75_target_model_adequacy_overidentification.md). Provenance: [P75 equation record](p75_equation_provenance.md). Implementation: [`target_model_adequacy.py`](../src/consciousness_bridge/target_model_adequacy.py). Tests: [`test_target_model_adequacy.py`](../tests/test_target_model_adequacy.py)."
    p76 = r"""

### P76: finite-sample target-model adequacy rejection

P75 is a population adequacy theorem. P76 places the empirical sixteen-cell four-view law inside one simultaneous finite-sample event. With

\[
\varepsilon_n(\alpha)=\sqrt{\frac{\log(32/\alpha)}{2n}},
\qquad
\delta_n(\alpha)=\min\{2,16\varepsilon_n(\alpha)\},
\]

all binary raw monomial moments are simultaneously controlled by \(\delta_n\) with probability at least \(1-\alpha\). This gives

\[
\boxed{|\widehat C_{ij}-C_{ij}|\le3\delta_n}
\]

and, for each displayed P75 tetrad residual \(D\),

\[
\boxed{|\widehat D-D|\le12\delta_n.}
\]

Therefore \(|\widehat D|>12\delta_n\) certifies a nonzero population tetrad and rejects the declared P75 model on the same confidence event. P76 also cross-multiplies the P75 equal-\(q\) and fourth-moment conditions into denominator-free polynomial equalities and propagates the shared empirical-law uncertainty through interval arithmetic.

The conclusion is one-sided. Exclusion of zero by any necessary-constraint interval certifies model incompatibility. Failure to exclude zero is inconclusive and is not model acceptance.

![P76 finite-sample target-model adequacy rejection](figures/p76_finite_sample_target_model_adequacy.svg)

Direct proof: [P76](proposition_76_finite_sample_target_model_adequacy.md). Provenance: [P76 equation record](p76_equation_provenance.md). Implementation: [`finite_sample_target_model_adequacy.py`](../src/consciousness_bridge/finite_sample_target_model_adequacy.py). Tests: [`test_finite_sample_target_model_adequacy.py`](../tests/test_finite_sample_target_model_adequacy.py).
"""
    text = replace_once(text, p75_end, p75_end + p76, label="roadmap P76 section")
    p75_index = "| [P75](proposition_75_target_model_adequacy_overidentification.md) | dimension count, tetrads, cross-triple moments, full-law reconstruction | target-model adequacy and four-view overidentification | proved conditional theorem |"
    p76_index = "| [P76](proposition_76_finite_sample_target_model_adequacy.md) | sixteen-cell concentration and polynomial interval propagation | finite-sample target-model adequacy rejection | proved conditional theorem |"
    text = replace_once(text, p75_index, p75_index + "\n" + p76_index, label="roadmap index P76")
    open_old_start = "After P75, the target side has five explicit requirements:"
    open_new_start = "After P76, the target side has six explicit requirements:"
    text = replace_once(text, open_old_start, open_new_start, label="roadmap open count")
    text = replace_once(
        text,
        "5. the target-measurement model itself must survive adequacy tests rather than being accepted because it can be fit.\n\nP75 closes the population-level fifth item for one binary four-view extension of the P73 model. It provides explicit observable restrictions and full-law reconstruction, but it does not yet attach finite-sample simultaneous uncertainty to those adequacy residuals. The next structural question is therefore **finite-sample model-adequacy certification**.",
        "5. the target-measurement model itself must survive adequacy tests rather than being accepted because it can be fit;\n6. finite data must separate a genuine adequacy violation from sampling uncertainty before model rejection is claimed.\n\nP76 closes the sixth item for a tracked family of necessary P75 polynomial constraints under IID sampling. It supplies simultaneous rejection intervals, but it does not yet give a complete finite-sample confidence characterization of the full sixteen-cell model image or an optimal-power test. The next structural question is therefore **stronger finite-sample full-law adequacy and power under dependent-view alternatives**.",
        label="roadmap open frontier",
    )
    text = replace_once(
        text,
        "- test target-model adequacy under finite data and residual dependence;",
        "- strengthen finite-sample target-model adequacy beyond the tracked necessary polynomials and characterize power under residual dependence;",
        label="roadmap future bullet",
    )
    save(path, text)


def patch_navigation() -> None:
    path = "docs/research_navigation.md"
    text = load(path)
    text = replace_once(
        text,
        "The current documented theorem frontier is **P75**. The complete proposition record runs from **P1 through P75**. P71-P75 form a target-side methodology branch descending from the P19 physical-sufficiency question. They are not extensions of the P61-P70 calibration branch.",
        "The current documented theorem frontier is **P76**. The complete proposition record runs from **P1 through P76**. P71-P76 form a target-side methodology branch descending from the P19 physical-sufficiency question. They are not extensions of the P61-P70 calibration branch.",
        label="navigation intro",
    )
    text = replace_once(text, "from P1 through P75.", "from P1 through P76.", label="navigation roadmap reader")

    lines = text.splitlines()
    in_order = False
    for i, line in enumerate(lines):
        if line == "## Recommended reading order":
            in_order = True
            continue
        if in_order and line.startswith("## "):
            break
        match = re.match(r"^(\d+)\. (.*)$", line)
        if in_order and match:
            number = int(match.group(1))
            if 12 <= number <= 22:
                lines[i] = f"{number + 1}. {match.group(2)}"
    text = "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    p75_reader = "11. [P75 target-model adequacy and four-view overidentification](proposition_75_target_model_adequacy_overidentification.md) for the distinction between target-channel identifiability and model adequacy, six generic four-view overidentifying degrees of freedom, observable moment constraints, and full-law reconstruction."
    p76_reader = "12. [P76 finite-sample target-model adequacy rejection](proposition_76_finite_sample_target_model_adequacy.md) for simultaneous sixteen-cell uncertainty, denominator-free polynomial adequacy intervals, and the distinction between certified rejection and inconclusive non-rejection."
    text = replace_once(text, p75_reader, p75_reader + "\n" + p76_reader, label="navigation reader P76")

    p75_branch = "| Target-model adequacy | P75 | Separates identifiability from adequacy and gives four-view overidentifying restrictions plus full-law model reconstruction | [P75](proposition_75_target_model_adequacy_overidentification.md) |"
    p76_branch = "| Finite-sample target-model adequacy | P76 | Turns tracked P75 population restrictions into simultaneous one-sided finite-data rejection certificates | [P76](proposition_76_finite_sample_target_model_adequacy.md) |"
    text = replace_once(text, p75_branch, p75_branch + "\n" + p76_branch, label="navigation branch P76")

    p75_line_match = re.search(r"^\| P75 \| .*\|$", text, flags=re.MULTILINE)
    if not p75_line_match:
        raise RuntimeError("navigation proposition index: P75 row not found")
    p75_line = p75_line_match.group(0)
    p76_line = "| P76 | [Finite-sample target-model adequacy rejection](proposition_76_finite_sample_target_model_adequacy.md) | sixteen-cell concentration and simultaneous polynomial adequacy rejection |"
    text = text.replace(p75_line, p75_line + "\n" + p76_line, 1)

    p75_core = "P75 adds the model-adequacy obligation. A three-view fit is generically just-identified and therefore should not be mistaken for generic validation of conditional independence. A fourth view creates six generic overidentifying degrees of freedom. P75 exposes covariance tetrads, cross-triple latent-imbalance consistency, a fourth-centered-moment relation, and full sixteen-cell reconstruction as population checks of the declared target-measurement model. Passing these checks means compatibility with that model, not proof that the model is uniquely true."
    p76_core = "P76 adds finite-data discipline to that adequacy check. One simultaneous sixteen-cell confidence event is propagated to the tracked P75 polynomial constraints. Excluding zero from any necessary-constraint interval certifies model incompatibility at the stated confidence level. If no interval excludes zero, P76 reports only non-rejection, never model acceptance."
    text = replace_once(text, p75_core, p75_core + "\n\n" + p76_core, label="navigation core P76")

    p75_figure = "| [P75 figure](figures/p75_target_model_adequacy_overidentification.svg) | three-view just-identification, four-view overidentification, observable adequacy restrictions, and full-law reconstruction |"
    p76_figure = "| [P76 figure](figures/p76_finite_sample_target_model_adequacy.svg) | shared finite-sample confidence event, polynomial adequacy intervals, certified rejection, and the non-rejection boundary |"
    text = replace_once(text, p75_figure, p75_figure + "\n" + p76_figure, label="navigation figure P76")

    text = replace_once(
        text,
        "Use the [P72 provenance record](p72_equation_provenance.md), [P73 provenance record](p73_equation_provenance.md), [P74 provenance record](p74_equation_provenance.md), and [P75 provenance record](p75_equation_provenance.md) for target-side equation classification.",
        "Use the [P72 provenance record](p72_equation_provenance.md), [P73 provenance record](p73_equation_provenance.md), [P74 provenance record](p74_equation_provenance.md), [P75 provenance record](p75_equation_provenance.md), and [P76 provenance record](p76_equation_provenance.md) for target-side equation classification.",
        label="navigation provenance P76",
    )
    text = replace_once(
        text,
        "The research remains an ongoing mathematical-physics program. The current theorem frontier is P75, but the physical-to-experiential bridge itself remains open.",
        "The research remains an ongoing mathematical-physics program. The current theorem frontier is P76, but the physical-to-experiential bridge itself remains open.",
        label="navigation closing frontier",
    )
    save(path, text)


def patch_detail() -> None:
    path = "docs/detailed_proposition_record.md"
    text = load(path)
    text = replace_once(text, "## Complete P1 to P75 chronology", "## Complete P1 to P76 chronology", label="detail heading")
    p75_end = "Direct P75 proof: [target-model adequacy and four-view overidentification](proposition_75_target_model_adequacy_overidentification.md). Equation classification: [P75 equation and provenance record](p75_equation_provenance.md). Implementation: [`target_model_adequacy.py`](../src/consciousness_bridge/target_model_adequacy.py)."
    p76 = r"""

**P76** converts the tracked P75 population adequacy restrictions into a finite-sample rejection certificate. From \(n\) IID four-view observations it places the entire sixteen-cell empirical law inside one simultaneous Hoeffding event. The induced \(L^1\) radius \(\delta_n\) controls every binary raw monomial moment simultaneously, which in turn gives conservative intervals for the centered moments used by P75.

For the two displayed covariance tetrads, P76 proves the explicit perturbation bound

\[
|\widehat D-D|\le12\delta_n.
\]

Thus \(|\widehat D|>12\delta_n\) certifies a nonzero population tetrad and rejects the declared four-view conditional-independence model with the shared confidence level. For the P75 cross-triple and fourth-moment conditions, P76 avoids unstable empirical ratios by cross-multiplying them into denominator-free polynomial equalities and propagating the same raw-moment confidence box through interval arithmetic. Any reported necessary-constraint interval that excludes zero is a valid rejection witness on the shared event.

The inference is deliberately asymmetric. A rejection is evidence that the declared P75 model is incompatible with the population under the stated IID sampling assumption. A failure to reject is not model acceptance: finite power may be inadequate, the violation may be small, or a misspecified law may satisfy the tracked necessary polynomials while failing the stronger P75 full-law membership audit.

Direct P76 proof: [finite-sample target-model adequacy rejection](proposition_76_finite_sample_target_model_adequacy.md). Equation classification: [P76 equation and provenance record](p76_equation_provenance.md). Implementation: [`finite_sample_target_model_adequacy.py`](../src/consciousness_bridge/finite_sample_target_model_adequacy.py).
"""
    text = replace_once(text, p75_end, p75_end + p76, label="detail P76")
    text = replace_once(
        text,
        "- P71-P75 return to the target side of the P19 bridge and formalize non-circular target provenance, noisy target measurement, population target-channel identification, finite-sample target-channel recovery, and target-model adequacy.",
        "- P71-P76 return to the target side of the P19 bridge and formalize non-circular target provenance, noisy target measurement, population target-channel identification, finite-sample target-channel recovery, target-model adequacy, and finite-sample model rejection.",
        label="detail branch summary",
    )
    old = "P75 does not make an experiential ontology claim. Passing its four-view restrictions establishes compatibility with the declared target-measurement model, not uniqueness or truth of that model. Failure identifies inadequacy of the declared conditional-independence model for the observed law; it does not prove that the latent target is nonphysical or that the physical-to-experiential bridge has been solved.\n\nThe next target-side problem is finite-sample adequacy certification: turn the P75 population tetrad, cross-triple, fourth-moment, and full-law reconstruction residuals into simultaneous uncertainty-aware tests."
    new = "P75 does not make an experiential ontology claim. Passing its four-view restrictions establishes compatibility with the declared target-measurement model, not uniqueness or truth of that model. Failure identifies inadequacy of the declared conditional-independence model for the observed law; it does not prove that the latent target is nonphysical or that the physical-to-experiential bridge has been solved.\n\nP76 adds a finite-sample rejection layer for a tracked family of necessary P75 polynomial constraints. Its non-rejection output is explicitly inconclusive. The next target-side problem is stronger finite-sample full-law adequacy characterization, sharper power, and robust alternatives for residually dependent or learned target-view systems."
    text = replace_once(text, old, new, label="detail frontier")
    save(path, text)


def patch_equation_map() -> None:
    path = "docs/equation_and_citation_map.md"
    text = load(path)
    if "# P76 finite-sample target-model adequacy rejection" in text:
        raise RuntimeError("equation map already contains P76 section")
    addition = r"""

---

# P76 finite-sample target-model adequacy rejection

P76 is the finite-data continuation of the P75 target-model adequacy theorem. It uses one shared finite-alphabet confidence event and deterministic polynomial interval propagation.

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\varepsilon_n(\alpha)=\sqrt{\log(32/\alpha)/(2n)}\) | simultaneous sixteen-cell empirical-frequency radius | standard Hoeffding inequality specialized by union bound | Hoeffding 1963; P76A |
| \(\delta_n(\alpha)=\min\{2,16\varepsilon_n(\alpha)\}\) | induced sixteen-cell \(L^1\) radius | repository bookkeeping consequence | P76A |
| \(|\widehat r_A-r_A|\le\delta_n\) | simultaneous raw binary-monomial transport | standard \(L^1\) expectation bound applied here | P76B |
| \(|\widehat C_{ij}-C_{ij}|\le3\delta_n\) | covariance perturbation radius | repository derivation | P76C |
| \(|\widehat D-D|\le12\delta_n\) | explicit tetrad residual radius | repository derivation from P75 tetrads | P76C |
| denominator-free \(G_1,G_2,G_3=0\) | cross-triple adequacy constraints without uncertain division | algebraic reformulation of P75 equal-\(q\) obligations | P75; P76D |
| denominator-free \(H\)-constraints | fourth-moment adequacy constraints without uncertain division | algebraic reformulation of P75 fourth-moment obligations | P75; P76E |
| zero excluded from any simultaneous necessary-constraint interval | finite-sample target-model rejection witness | repository theorem assembly | P76F |

Detailed classification and literature boundary: [P76 equation and provenance record](p76_equation_provenance.md).

P76 does not assert an ordinary chi-square null law from the P75 dimension count, does not treat non-rejection as model validation, and does not identify a latent state with consciousness. The physical-to-experiential bridge remains open.
"""
    text = text.rstrip() + addition + "\n"
    save(path, text)


def patch_changelog() -> None:
    path = "CHANGELOG.md"
    text = load(path)
    if text.startswith("# 0.76.0"):
        raise RuntimeError("changelog already contains 0.76.0")
    entry = """# 0.76.0 - 2026-09-10

- Added P76 finite-sample target-model adequacy rejection as the finite-data continuation of P75.
- Built one simultaneous sixteen-cell Hoeffding event and propagated it to all binary raw monomial moments used by the P75 adequacy system.
- Derived an explicit covariance-tetrad perturbation radius and a conservative sufficient sample-size bound for a known tetrad violation margin.
- Rewrote the P75 cross-triple and fourth-moment obligations as denominator-free polynomial constraints and added simultaneous interval propagation for finite-data rejection.
- Added a synthetic residual-dependence stress test, formal proof, implementation, regression tests, theorem visual, geometry guards, provenance record, v0.76.0 metadata, README integration, navigation/roadmap updates, and website integration.
- Kept the inference one-sided: rejection can certify incompatibility, while non-rejection is explicitly inconclusive and is not model acceptance or an experiential ontology claim.

"""
    save(path, entry + text)


def patch_website_index() -> None:
    path = "website/index.html"
    text = load(path)
    text = replace_all(text, "v0.75.0", "v0.76.0", minimum=1, label="site version")
    text = replace_once(text, "<strong>75</strong><span>proposition-level results</span>", "<strong>76</strong><span>proposition-level results</span>", label="site result count")
    text = replace_once(text, "See all 75 results grouped by scientific role", "See all 76 results grouped by scientific role", label="site all results")
    text = replace_all(text, "P71-P75", "P71-P76", minimum=1, label="site target range")
    text = replace_once(
        text,
        "The current target-side frontier formalizes non-circular target provenance, noisy target measurement, population target-channel identifiability, finite-sample certification of that recovery, and explicit model-adequacy tests.",
        "The current target-side frontier formalizes non-circular target provenance, noisy target measurement, population target-channel identifiability, finite-sample certification of that recovery, explicit model-adequacy tests, and finite-sample rejection of tracked adequacy violations.",
        label="site hero P76",
    )
    text = replace_once(
        text,
        "the physical descriptor, target-construction protocol, target-measurement model, identifiability assumptions, finite-sample recovery conditions, target-model adequacy, bridge class, and uncertainty model",
        "the physical descriptor, target-construction protocol, target-measurement model, identifiability assumptions, finite-sample recovery conditions, target-model adequacy, finite-sample adequacy certificate, bridge class, and uncertainty model",
        label="site boundary P76",
    )
    model_node = '<div class="flow-node"><span>07</span><h3>Model adequacy</h3><p>P75 separates successful parameter recovery from validation of the target-measurement model and adds four-view overidentifying checks.</p></div>\n        <div class="flow-node"><span>08</span><h3>Bridge test</h3><p>Test whether independently justified target distinctions are determined by the declared physical information.</p></div>'
    new_nodes = '<div class="flow-node"><span>07</span><h3>Model adequacy</h3><p>P75 separates successful parameter recovery from validation of the target-measurement model and adds four-view overidentifying checks.</p></div>\n        <div class="flow-node"><span>08</span><h3>Finite adequacy</h3><p>P76 asks whether an apparent P75 model violation remains separated from zero after finite-sample uncertainty is propagated.</p></div>\n        <div class="flow-node"><span>09</span><h3>Bridge test</h3><p>Test whether independently justified target distinctions are determined by the declared physical information.</p></div>'
    text = replace_once(text, model_node, new_nodes, label="site flow P76")
    text = replace_once(
        text,
        "\\text{model adequacy}\\to\\text{bridge test}",
        "\\text{model adequacy}\\to\\text{finite adequacy}\\to\\text{bridge test}",
        label="site equation flow",
    )
    results_intro = "P71 asks whether the target is non-circular. P72 asks whether noisy observation preserves its distinctions. P73 asks whether channel reliability can be identified rather than assumed. P74 asks whether finite data justify trusting that recovered channel. P75 asks whether the measurement model itself survives independent adequacy checks."
    results_new = results_intro + " P76 asks whether finite data are strong enough to reject a tracked adequacy violation after sampling uncertainty is included."
    text = replace_once(text, results_intro, results_new, label="site results intro P76")
    p75_card = '<article class="result"><span>P75</span><h3>Target-model adequacy</h3><p>Three binary views are generically just-identified. A fourth view creates six generic overidentifying degrees of freedom, observable moment constraints, and a full sixteen-cell reconstruction audit.</p></article>'
    p76_card = '<article class="result"><span>P76</span><h3>Finite-sample model rejection</h3><p>One simultaneous sixteen-cell confidence event is propagated to denominator-free P75 polynomial constraints. Excluding zero certifies incompatibility; non-rejection remains inconclusive.</p></article>'
    text = replace_once(text, p75_card, p75_card + "\n        " + p76_card, label="site P76 card")
    p75_figure = '<div class="figure-card"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p75_target_model_adequacy_overidentification.svg" alt="P75 target-model adequacy and four-view overidentification"/><div><h3>P75 theorem figure</h3><p>The figure separates three-view just-identification from four-view overidentification and shows the covariance-tetrad, cross-triple, fourth-moment, and full-law reconstruction obligations. Passing establishes compatibility with the declared model, not uniqueness or truth.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_75_target_model_adequacy_overidentification.md">Read Proposition 75 →</a></div></div>'
    p76_figure = '<div class="figure-card"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p76_finite_sample_target_model_adequacy.svg" alt="P76 finite-sample target-model adequacy rejection"/><div><h3>P76 theorem figure</h3><p>The figure shows one shared finite-sample confidence event feeding P75 polynomial adequacy intervals. A separated interval certifies rejection, while non-rejection is not model acceptance.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_76_finite_sample_target_model_adequacy.md">Read Proposition 76 →</a></div></div>'
    text = replace_once(text, p75_figure, p75_figure + "\n\n      " + p76_figure, label="site P76 figure")
    adequacy_fail = '<div><h3>Model-adequacy failure</h3><p>Reject the P73-P74 target model when a fourth view violates the P75 overidentifying constraints or full-law reconstruction.</p></div>'
    finite_fail = '<div><h3>Finite adequacy rejection</h3><p>Use P76 to reject only when a simultaneous necessary-constraint interval excludes zero. Do not convert non-rejection into model validation.</p></div>'
    text = replace_once(text, adequacy_fail, adequacy_fail + finite_fail, label="site falsification P76")
    p75_source = '<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p75_equation_provenance.md"><h3>P75 provenance</h3><p>Classifies just-identification, four-view overidentification, model invariants, moment consistency, and full-law reconstruction.</p></a>'
    p76_source = '<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p76_equation_provenance.md"><h3>P76 provenance</h3><p>Classifies sixteen-cell concentration, polynomial interval propagation, finite-sample rejection, and the non-rejection boundary.</p></a>'
    text = replace_once(text, p75_source, p75_source + "\n        " + p76_source, label="site provenance P76")
    text = replace_once(text, "Dependency-aware path through P1-P75.", "Dependency-aware path through P1-P76.", label="site roadmap range")
    text = replace_once(
        text,
        "finite-data certification where recovery is estimated, explicit target-model adequacy checks, transparent empirical interfaces",
        "finite-data certification where recovery is estimated, explicit target-model adequacy checks, finite-sample adequacy rejection with non-rejection kept inconclusive, transparent empirical interfaces",
        label="site closing P76",
    )
    save(path, text)


def patch_research_map() -> None:
    path = "website/research-map.html"
    text = load(path)
    text = replace_once(text, "through Proposition 75", "through Proposition 76", label="map meta")
    text = replace_once(text, "Seventy-five results", "Seventy-six results", label="map hero count")
    text = replace_once(text, "<strong>75</strong><span>proposition-level results</span>", "<strong>76</strong><span>proposition-level results</span>", label="map count")
    text = replace_all(text, "P71-P75", "P71-P76", minimum=1, label="map target range")
    text = replace_once(
        text,
        "P71 protects target provenance, P72 protects the target-observation interface, P73 identifies target channels under one explicit latent model, P74 asks when finite data are strong enough to certify that recovery, and P75 asks whether the measurement model itself survives independent adequacy checks.",
        "P71 protects target provenance, P72 protects the target-observation interface, P73 identifies target channels under one explicit latent model, P74 asks when finite data are strong enough to certify that recovery, P75 asks whether the measurement model itself survives independent adequacy checks, and P76 asks whether finite data can certify an adequacy violation beyond sampling noise.",
        label="map hero P76",
    )
    text = replace_once(text, "6 · P73-P75", "6 · P73-P76", label="map stage range")
    text = replace_once(
        text,
        "Identify the declared binary target channel, certify that recovery from finite data, then test whether a fourth view supports the model assumptions rather than merely fitting them.",
        "Identify the declared binary target channel, certify that recovery from finite data, test whether a fourth view supports the model assumptions, then ask whether finite data are strong enough to reject a tracked violation.",
        label="map stage wording",
    )
    text = replace_once(
        text,
        "P74-P75 continue that target-side branch with finite-data certification and model-adequacy testing. None of P71-P76 is a consciousness ontology.",
        "P74-P76 continue that target-side branch with finite-data recovery, model-adequacy testing, and finite-sample adequacy rejection. None of P71-P76 is a consciousness ontology.",
        label="map reading rule",
    )
    p75_section = '<section><div class="section-head"><p class="eyebrow">IV-E · Target-model adequacy</p><h2>P75: Does an identifiable target-channel model actually fit independent constraints?</h2></div><div class="result-grid"><article class="result"><span>P75A</span><h3>Just-identification boundary</h3><p>Three binary views provide seven observable degrees of freedom for a seven-parameter binary latent conditional-independence model. Recovery is not generic model validation.</p></article><article class="result"><span>P75B-P75D</span><h3>Four-view overidentification</h3><p>A fourth binary view creates six generic overidentifying degrees of freedom, including covariance tetrads, cross-triple latent-imbalance agreement, and fourth-moment consistency.</p></article><article class="result"><span>P75E-P75F</span><h3>Full-law falsification</h3><p>The executable audit reconstructs all 16 cells and rejects a synthetic residual-dependence perturbation that is not mediated by the declared latent state.</p></article></div><div class="figure-card"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p75_target_model_adequacy_overidentification.svg" alt="P75 target-model adequacy and four-view overidentification"/><div><h3>P75 target-model adequacy</h3><p>The fourth view turns the target model from a just-identified recovery problem into an overidentified model that can face independent population restrictions.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_75_target_model_adequacy_overidentification.md">Read Proposition 75 →</a></div></div></section>'
    p76_section = '<section><div class="section-head"><p class="eyebrow">IV-F · Finite target-model adequacy</p><h2>P76: When can finite data certify that the target model fails?</h2></div><div class="result-grid"><article class="result"><span>P76A-P76B</span><h3>One sixteen-cell confidence event</h3><p>A simultaneous Hoeffding event controls the empirical four-view law and every binary raw monomial used by the adequacy constraints.</p></article><article class="result"><span>P76C-P76E</span><h3>Denominator-free rejection intervals</h3><p>Tetrad, cross-triple, and fourth-moment obligations receive finite-sample intervals without dividing by uncertain covariance products.</p></article><article class="result"><span>P76F-P76G</span><h3>One-sided falsification</h3><p>If any necessary-constraint interval excludes zero, the declared P75 model is rejected. Non-rejection remains inconclusive.</p></article></div><div class="figure-card"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p76_finite_sample_target_model_adequacy.svg" alt="P76 finite-sample target-model adequacy rejection"/><div><h3>P76 finite-sample adequacy rejection</h3><p>The figure separates controlled finite-data rejection from the scientifically invalid inference that a non-rejected model has been validated.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_76_finite_sample_target_model_adequacy.md">Read Proposition 76 →</a></div></div></section>'
    text = replace_once(text, p75_section, p75_section + "\n\n" + p76_section, label="map P76 section")
    save(path, text)


def patch_visual_atlas() -> None:
    path = "website/visual-atlas.html"
    text = load(path)
    text = replace_once(
        text,
        "From physical sufficiency to non-circular targets, noisy observation, channel recovery, and target-model adequacy",
        "From physical sufficiency to non-circular targets, noisy observation, channel recovery, model adequacy, and finite-sample rejection",
        label="atlas heading P76",
    )
    p75_card = '<div class="figure-card"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p75_target_model_adequacy_overidentification.svg" alt="P75 target-model adequacy and four-view overidentification"/><div><h3>P75: target-model adequacy and four-view overidentification</h3><p>Three binary views are generically just-identified under the declared binary latent model. A fourth view creates six generic overidentifying degrees of freedom and exposes covariance-tetrad, cross-triple, fourth-moment, and full-law reconstruction checks. Passing means compatibility with the declared model, not proof that the model is uniquely true.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_75_target_model_adequacy_overidentification.md">Proof and assumptions →</a></div></div>'
    p76_card = '<div class="figure-card"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p76_finite_sample_target_model_adequacy.svg" alt="P76 finite-sample target-model adequacy rejection"/><div><h3>P76: finite-sample target-model adequacy rejection</h3><p>One shared sixteen-cell confidence event is propagated to denominator-free P75 polynomial constraints. Excluding zero certifies incompatibility; non-rejection remains inconclusive and is not model acceptance.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_76_finite_sample_target_model_adequacy.md">Proof and assumptions →</a></div></div>'
    text = replace_once(text, p75_card, p75_card + p76_card, label="atlas P76 card")
    save(path, text)


def patch_tests() -> None:
    path = "tests/test_readme_research_orientation.py"
    text = load(path)
    text = replace_once(
        text,
        '    p75 = text.index("## 1.9 P75: identifiability does not by itself validate the target model")\n    operational = text.index',
        '    p75 = text.index("## 1.9 P75: identifiability does not by itself validate the target model")\n    p76 = text.index("## 1.10 P76: finite data must separate model failure from sampling noise")\n    operational = text.index',
        label="readme test p76 index",
    )
    text = replace_once(
        text,
        "assert formulation < p71 < p72 < p73 < p74 < p75 < operational < scale < finite < fundamental",
        "assert formulation < p71 < p72 < p73 < p74 < p75 < p76 < operational < scale < finite < fundamental",
        label="readme test order",
    )
    text = replace_once(
        text,
        '        "A fourth binary view creates additional observable constraints",',
        '        "A fourth binary view creates additional observable constraints",\n        "P76 asks the next practical question",\n        "finite data are strong enough to demonstrate that one of those requirements has genuinely failed",',
        label="readme test plain P76",
    )
    text = replace_once(text, '"P19-P24, P71-P75",', '"P19-P24, P71-P76",', label="readme test glance")
    text = replace_all(text, "P1 to P75", "P1 to P76", minimum=2, label="readme test chronology")
    text = replace_once(
        text,
        '    assert "**P75** separates target-channel identifiability from target-model adequacy" in detail',
        '    assert "**P75** separates target-channel identifiability from target-model adequacy" in detail\n    assert "**P76** converts the tracked P75 population adequacy restrictions" in detail',
        label="readme test detail P76",
    )
    text = replace_once(text, '    assert "75 proposition-level results" in text\n    assert "**P75**" in text\n    assert "**63**" in text', '    assert "76 proposition-level results" in text\n    assert "**P76**" in text\n    assert "**64**" in text', label="readme test counts")
    save(path, text)

    path = "tests/test_main_page_visual_paper.py"
    text = load(path)
    text = replace_once(
        text,
        '    "p75_target_model_adequacy_overidentification.svg",\n    "observer_to_bridge_handoff.svg",',
        '    "p75_target_model_adequacy_overidentification.svg",\n    "p76_finite_sample_target_model_adequacy.svg",\n    "observer_to_bridge_handoff.svg",',
        label="visual test P76 figure",
    )
    text = replace_all(text, "P1 to P75", "P1 to P76", minimum=2, label="visual test chronology")
    text = replace_once(
        text,
        '    assert "**P75** separates target-channel identifiability from target-model adequacy" in detail',
        '    assert "**P75** separates target-channel identifiability from target-model adequacy" in detail\n    assert "**P76** converts the tracked P75 population adequacy restrictions" in detail',
        label="visual test detail P76",
    )
    text = replace_once(
        text,
        '        "Passing means compatibility with the declared model",',
        '        "Passing means compatibility with the declared model",\n        "non-rejection is not model acceptance",',
        label="visual test boundary P76",
    )
    save(path, text)

    path = "tests/test_website_research_orientation.py"
    text = load(path)
    text = replace_once(text, "Seventy-five results", "Seventy-six results", label="website test hero")
    text = replace_once(text, '        "P73-P75",', '        "P73-P76",', label="website test stage range")
    text = replace_once(
        text,
        '        "proposition_75_target_model_adequacy_overidentification.md",',
        '        "proposition_75_target_model_adequacy_overidentification.md",\n        "proposition_76_finite_sample_target_model_adequacy.md",',
        label="website test P76 path",
    )
    save(path, text)


def main() -> None:
    patch_source()
    patch_readme()
    patch_roadmap()
    patch_navigation()
    patch_detail()
    patch_equation_map()
    patch_changelog()
    patch_website_index()
    patch_research_map()
    patch_visual_atlas()
    patch_tests()


if __name__ == "__main__":
    main()
