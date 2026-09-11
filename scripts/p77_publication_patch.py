from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one anchor, found {count}: {old!r}")
    return text.replace(old, new, 1)


def require(text: str, token: str, label: str) -> None:
    if token not in text:
        raise RuntimeError(f"{label}: missing required token {token!r}")


def patch_readme() -> None:
    path = "README.md"
    text = read(path)
    require(text, "## 1.10 P76: finite data must separate model failure from sampling noise", path)
    require(text, "docs/figures/p76_finite_sample_target_model_adequacy.svg", path)
    if "## 1.11 P77: full-law confidence regions can reject the complete declared model set" in text:
        raise RuntimeError("README already contains P77 publication section")

    text = text.replace("0.76.0", "0.77.0")
    text = text.replace("P1 through P76 with explicit dependency branches", "P1 through P77 with explicit dependency branches")
    text = text.replace("P1 through P76", "P1 through P77")
    text = text.replace("P71-P76", "P71-P77")
    text = text.replace("P71 through P76", "P71 through P77")
    text = text.replace("**76 proposition-level results**", "**77 proposition-level results**")
    text = text.replace("**64 equation-driven quantitative figures**", "**65 equation-driven quantitative figures**")
    text = text.replace("The theorem frontier is P76.", "The theorem frontier is P77.")
    text = text.replace("| Proposition-level results | **76** |", "| Proposition-level results | **77** |")
    text = text.replace("| Equation-driven quantitative figures | **64** |", "| Equation-driven quantitative figures | **65** |")
    text = text.replace("Current documented theorem frontier: P76", "Current documented theorem frontier: P77")

    p76_plain = (
        "P76 asks the next practical question: **if those model checks are applied to finite data, is an apparent failure large enough to distinguish from ordinary sampling noise?** It places the complete sixteen-cell observed table inside one shared confidence event and carries that uncertainty into the P75 adequacy constraints. If a required constraint is separated from zero even after uncertainty is included, the declared measurement model can be rejected with controlled confidence. If the data do not reject it, P76 deliberately does not call the model validated: non-rejection is not model acceptance. The sample may simply be too small, the violation may be too subtle, or the failure may lie outside the particular constraints being tested. In plain language, P75 explains what a valid four-view model must satisfy at the population level; P76 asks when finite data are strong enough to demonstrate that one of those requirements has genuinely failed.\n\n"
    )
    p77_plain = (
        "P77 closes the next logical gap. P76 can reject the measurement model when one of its tracked mathematical requirements fails, but a model can in principle pass those selected checks and still fail to reproduce the complete pattern of observed outcomes. P77 therefore asks a stronger question: **after finite-sample uncertainty is included, is there any distribution allowed by the entire declared measurement model that is still compatible with the data?** If the whole confidence region around the observed distribution is separated from the whole model family, the model can be rejected. If the regions still overlap, the result remains inconclusive. P77 also makes a computational safeguard explicit: finding one imperfect best-fitting model is not enough to prove separation from every model in the family. A rejection requires a mathematically certified lower bound on the distance to the model set, or an equivalent certified proof that no admissible model lies inside the confidence region. In plain language, P76 tests interpretable necessary requirements; P77 defines the stronger full-distribution standard that a complete finite-data adequacy test must satisfy.\n\n"
    )
    text = replace_once(text, p76_plain, p76_plain + p77_plain, "README plain-language P77 insertion")

    text = replace_once(
        text,
        "P76 adds the requirement that an apparent adequacy failure survive finite-sample uncertainty before it is called a model rejection. Others examine changes of physical scale, test quantum descriptions, design experiments, protect validity under adaptive sampling, or make experiments more efficient. Together they are intended to remove hidden assumptions one by one.",
        "P76 adds the requirement that an apparent adequacy failure survive finite-sample uncertainty before it is called a model rejection. P77 then asks the stronger full-law question: whether the complete finite-sample confidence region is separated from the entire declared target-measurement model, while refusing to treat an uncertified local best fit as proof of global incompatibility. Others examine changes of physical scale, test quantum descriptions, design experiments, protect validity under adaptive sampling, or make experiments more efficient. Together they are intended to remove hidden assumptions one by one.",
        "README synthesis paragraph",
    )

    p76_abstract = (
        "P76 adds finite-sample target-model rejection. From one IID sample of the sixteen-cell four-view law, a shared Hoeffding event controls the full empirical distribution and every binary raw moment simultaneously. The theorem propagates that event to covariance tetrads and to denominator-free polynomial forms of the P75 cross-triple and fourth-moment constraints. If any necessary-constraint interval excludes zero, the declared P75 target-measurement model is rejected with confidence at least $1-\\alpha$. Non-rejection remains inconclusive and is not model acceptance.\n\n"
    )
    p77_abstract = (
        "P77 strengthens that finite-data adequacy layer from selected necessary constraints to the complete declared observed-law model set. For a finite alphabet of size $K$, one simultaneous empirical-law event gives $\\|\\widehat P-P\\|_\\infty\\le\\varepsilon_{n,K}$ and $\\|\\widehat P-P\\|_1\\le\\delta_{n,K}$ with probability at least $1-\\alpha$. If the corresponding confidence region is disjoint from the declared model family $\\mathcal M$, equivalently if a sound lower bound on empirical distance to $\\mathcal M$ exceeds the sampling radius, the model is rejected at the same confidence level. A numerical candidate fit supplies only an upper bound on distance and cannot by itself certify rejection of a continuous model family.\n\n"
    )
    text = replace_once(text, p76_abstract, p76_abstract + p77_abstract, "README abstract P77 insertion")

    p76_end = (
        "Direct proof: [Proposition 76](docs/proposition_76_finite_sample_target_model_adequacy.md). Equation and literature classification: [P76 provenance record](docs/p76_equation_provenance.md).\n\n\n\n---\n\n# 2. From physical dynamics to operational structure"
    )
    p77_section = """Direct proof: [Proposition 76](docs/proposition_76_finite_sample_target_model_adequacy.md). Equation and literature classification: [P76 provenance record](docs/p76_equation_provenance.md).

## 1.11 P77: full-law confidence regions can reject the complete declared model set

P76 tests a transparent family of necessary P75 polynomial constraints. P77 asks the stronger finite-data question: does the complete confidence region for the observed law intersect the complete declared model family at all?

For a finite alphabet of size $K$, define

$$
\\boxed{\\varepsilon_{n,K}(\\alpha)=\\sqrt{\\frac{\\log(2K/\\alpha)}{2n}}}
$$

and

$$
\\boxed{\\delta_{n,K}(\\alpha)=\\min\\{2,K\\varepsilon_{n,K}(\\alpha)\\}.}
$$

With probability at least $1-\\alpha$,

$$
\\|\\widehat P-P\\|_\\infty\\le\\varepsilon_{n,K},
\\qquad
\\|\\widehat P-P\\|_1\\le\\delta_{n,K}.
$$

Let $\\mathcal M$ be the complete declared observed-law model set. P77 gives the full-law rejection rule

$$
\\boxed{\\mathcal C_n(\\widehat P)\\cap\\mathcal M=\\varnothing
\\quad\\Longrightarrow\\quad
P\\notin\\mathcal M.}
$$

Equivalently, if a mathematically certified lower bound on $d(\\widehat P,\\mathcal M)$ exceeds the sampling radius in the same norm, the model is rejected on the shared confidence event. Distance to a nonempty set is 1-Lipschitz, so the same event also transports empirical model distance into a confidence interval for population distance to the model family.

The optimization direction is scientifically important. A candidate best-fit model $Q^\\star\\in\\mathcal M$ gives $d(\\widehat P,\\mathcal M)\\le\\|\\widehat P-Q^\\star\\|$, which is an upper bound on the unknown minimum distance. It cannot by itself certify rejection. P77 requires a sound lower bound or an equivalent certified feasibility result before declaring a continuous model family incompatible.

![P77 finite-sample full-law model-set separation](docs/figures/p77_full_law_model_set_separation.svg)

**Figure 12. P77 full-law model-set separation.** P76 provides interpretable finite-sample rejection through selected necessary constraints. P77 defines the stronger full-law criterion: the entire confidence region must be separated from the entire declared model set. An ordinary best-fit candidate is not a rejection certificate because it gives an upper bound on model distance.

Direct proof: [Proposition 77](docs/proposition_77_full_law_model_set_separation.md). Equation and literature classification: [P77 provenance record](docs/p77_equation_provenance.md). Implementation: [`full_law_model_set_separation.py`](src/consciousness_bridge/full_law_model_set_separation.py). Tests: [`test_full_law_model_set_separation.py`](tests/test_full_law_model_set_separation.py).



---

# 2. From physical dynamics to operational structure"""
    text = replace_once(text, p76_end, p77_section, "README formal P77 section")

    # P77 occupies Figure 12. Shift all later curated figure numbers by one.
    for number in range(25, 11, -1):
        text = text.replace(f"**Figure {number}.", f"**Figure {number + 1}.")

    text = replace_once(
        text,
        "P72 applies the same philosophy on the target side. P73 establishes population identifiability for its declared three-view model, and P74 propagates finite empirical-law uncertainty through that nonlinear inversion. P75 then makes the conditional-independence model itself falsifiable at population level by adding a fourth view and overidentifying restrictions. P76 adds a simultaneous finite-sample rejection certificate for the tracked P75 polynomial constraints. A stronger finite-data full-law membership test and higher-power alternatives remain open.",
        "P72 applies the same philosophy on the target side. P73 establishes population identifiability for its declared three-view model, and P74 propagates finite empirical-law uncertainty through that nonlinear inversion. P75 then makes the conditional-independence model itself falsifiable at population level by adding a fourth view and overidentifying restrictions. P76 adds a simultaneous finite-sample rejection certificate for the tracked P75 polynomial constraints. P77 upgrades the finite-data target to the complete declared observed-law model set through confidence-region separation. The remaining challenge is computational certification of global distance or feasibility for the continuous P75 latent family, together with sharper power and broader dependent-view alternatives.",
        "README finite experiment summary",
    )

    text = text.replace("This branch remains intentionally separate from P71-P76.", "This branch remains intentionally separate from P71-P77.")

    text = replace_once(
        text,
        "18. P76 turns the tracked P75 population constraints into simultaneous finite-sample rejection intervals from one sixteen-cell Hoeffding event, while keeping non-rejection explicitly inconclusive.\n19. The experiment-design branch provides scheduling, stopping, calibration, integer optimization, and primal-dual certification without promoting those results into consciousness ontology.",
        "18. P76 turns the tracked P75 population constraints into simultaneous finite-sample rejection intervals from one sixteen-cell Hoeffding event, while keeping non-rejection explicitly inconclusive.\n19. P77 strengthens finite-sample adequacy to the complete declared observed-law model set: confidence-region/model-set separation certifies rejection, but only when model distance or infeasibility is lower-bounded soundly.\n20. The experiment-design branch provides scheduling, stopping, calibration, integer optimization, and primal-dual certification without promoting those results into consciousness ontology.",
        "README established-results list",
    )

    text = replace_once(
        text,
        "- extend P76 beyond the tracked necessary polynomials to sharper finite-sample full-law and power-aware adequacy procedures;",
        "- make the P77 full-law criterion computationally decisive for the continuous P75 latent family using certified global lower bounds or equivalent feasibility certificates;",
        "README open problem bullet",
    )

    text = replace_once(
        text,
        "The most immediate target-side problem after P76 is **stronger finite-sample model-adequacy characterization and power**. P76 supplies a simultaneous rejection certificate for tracked necessary P75 polynomial constraints, but it does not yet provide a complete finite-sample confidence test for the full sixteen-cell model image or an optimal-power procedure. Shared rater bias, correlated reports, contextual dependence, temporal drift, hidden common causes, and learned measurement pipelines remain important alternatives that a target-measurement protocol must be designed to expose.",
        "The most immediate target-side problem after P77 is **certified computation and power for full-law adequacy**. P77 defines the complete finite-sample model-set separation criterion, but for the continuous P75 latent family an ordinary local optimizer is not enough: the repository still needs a sound global lower-bounding or feasibility method that can certify separation from the entire model set. Sharper power, shared rater bias, correlated reports, contextual dependence, temporal drift, hidden common causes, and learned measurement pipelines remain important alternatives that a target-measurement protocol must be designed to expose.",
        "README immediate frontier",
    )

    p76_falsification = "| Finite data reject the target model | A P76 simultaneous necessary-constraint interval excludes zero | Treating non-rejection as model acceptance |"
    p77_falsification = "| Full-law finite data reject the target model | A P77 confidence region is certified disjoint from the complete declared model set | Treating a local best-fit optimizer value as a certified global distance lower bound |"
    text = replace_once(text, p76_falsification, p76_falsification + "\n" + p77_falsification, "README falsification table")

    p76_prov = "| [P76 equation and provenance record](docs/p76_equation_provenance.md) | Sixteen-cell concentration, denominator-free polynomial intervals, and finite-sample adequacy rejection provenance |"
    p77_prov = "| [P77 equation and provenance record](docs/p77_equation_provenance.md) | Full-law confidence-region inversion, model-set distance transport, and certified lower-bound rejection provenance |"
    text = replace_once(text, p76_prov, p76_prov + "\n" + p77_prov, "README provenance table")

    p76_status = "| Finite-sample target-model adequacy | **P76 proved under IID sampling as a simultaneous one-sided rejection certificate for tracked P75 necessary constraints** |"
    p77_status = "| Full-law finite-sample target-model adequacy | **P77 proved as a confidence-region/model-set separation theorem, conditional on a sound distance lower bound or equivalent certified feasibility result** |"
    text = replace_once(text, p76_status, p76_status + "\n" + p77_status, "README status table")

    p76_nav = "| Inspect finite-sample target-model adequacy rejection | [P76](docs/proposition_76_finite_sample_target_model_adequacy.md) |"
    p77_nav = "| Inspect finite-sample full-law model-set separation | [P77](docs/proposition_77_full_law_model_set_separation.md) |"
    text = replace_once(text, p76_nav, p76_nav + "\n" + p77_nav, "README navigation proof")

    p76_audit = "| Audit P76 finite-sample adequacy equations | [P76 equation and provenance record](docs/p76_equation_provenance.md) |"
    p77_audit = "| Audit P77 full-law separation equations | [P77 equation and provenance record](docs/p77_equation_provenance.md) |"
    text = replace_once(text, p76_audit, p76_audit + "\n" + p77_audit, "README navigation provenance")

    text = text.replace(
        "target-model adequacy, finite-sample adequacy, admissible bridge class",
        "target-model adequacy, finite-sample adequacy, full-law model-set separation, admissible bridge class",
    )

    write(path, text)


def patch_citation_guide() -> None:
    path = "CITATION.md"
    text = read(path)
    text = text.replace("0.76.0", "0.77.0")
    text = text.replace("current documented frontier, P76", "current documented frontier, P77")
    text = text.replace("Current documented theorem frontier: P76", "Current documented theorem frontier: P77")
    text = text.replace("theorem frontier **P76**", "theorem frontier **P77**")
    text = text.replace("P1 through P76 chronological theorem record", "P1 through P77 chronological theorem record")

    p76_specific = "Cite [Proposition 76](docs/proposition_76_finite_sample_target_model_adequacy.md) when relying on the sixteen-cell finite-sample adequacy rejection theorem, the explicit tetrad confidence radius, denominator-free polynomial adequacy intervals, or the one-sided rule separating certified model rejection from inconclusive non-rejection."
    p77_specific = "Cite [Proposition 77](docs/proposition_77_full_law_model_set_separation.md) when relying on finite-sample confidence-region separation from the complete declared model set, 1-Lipschitz transport of model distance, fixed-margin design bounds, or the requirement that rejection of a continuous family use a certified distance lower bound or equivalent feasibility proof rather than an ordinary best-fit upper bound."
    text = replace_once(text, p76_specific, p76_specific + " " + p77_specific, "CITATION specific proposition")

    p76_scope = "P76 adds finite-data model falsification to that adequacy layer. It places the sixteen-cell empirical law inside one simultaneous Hoeffding event, propagates that event to denominator-free P75 polynomial constraints, and permits model rejection when any necessary-constraint confidence interval excludes zero. P76 deliberately does not infer an ordinary chi-square null law from the P75 dimension count, and a failure to reject remains inconclusive rather than model acceptance.\n\n"
    p77_scope = "P77 then extends finite-data adequacy from selected necessary constraints to the complete declared observed-law model set. It inverts the simultaneous empirical-law confidence region against that model set and permits rejection only when the confidence region is certified disjoint from the model family. For continuous latent models, an ordinary candidate fit is only an upper bound on the minimum model distance, so P77 requires a sound lower bound or equivalent certified feasibility result before claiming full-law incompatibility.\n\n"
    text = replace_once(text, p76_scope, p76_scope + p77_scope, "CITATION P77 scope")

    p76_resource = "- [P76 equation and provenance record](docs/p76_equation_provenance.md): sixteen-cell concentration, denominator-free polynomial intervals, and finite-sample adequacy rejection provenance."
    p77_resource = "- [P77 equation and provenance record](docs/p77_equation_provenance.md): full-law confidence-region inversion, model-distance transport, and certified lower-bound rejection provenance."
    text = replace_once(text, p76_resource, p76_resource + "\n" + p77_resource, "CITATION provenance resource")
    write(path, text)


def patch_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    text = text.replace("current documented theorem frontier is **P76**", "current documented theorem frontier is **P77**")
    text = text.replace("**P1 through P76 with explicit dependency branches**", "**P1 through P77 with explicit dependency branches**")
    text = text.replace("P71-P76", "P71-P77")
    text = text.replace("It does not imply that P76 depends on P70. P76 depends scientifically on P75, which in turn depends on P19 and the P71-P74 target-side lineage.", "It does not imply that P77 depends on P70. P77 depends scientifically on P76 and P75, which in turn descend from P19 and the P71-P74 target-side lineage.")
    text = replace_once(
        text,
        "&\\text{P76: finite data must separate adequacy failure from sampling noise}\n\\end{aligned}",
        "&\\text{P76: finite data must separate adequacy failure from sampling noise}\\\\\n&\\Downarrow\\\\\n&\\text{P77: full-law confidence regions must be separated from the complete declared model set}\n\\end{aligned}",
        "roadmap dependency map",
    )

    marker = "Direct proof: [P76](proposition_76_finite_sample_target_model_adequacy.md). Provenance: [P76 equation record](p76_equation_provenance.md). Implementation: [`finite_sample_target_model_adequacy.py`](../src/consciousness_bridge/finite_sample_target_model_adequacy.py). Tests: [`test_finite_sample_target_model_adequacy.py`](../tests/test_finite_sample_target_model_adequacy.py).\n\n\n## 3. Complete proposition index"
    section = """Direct proof: [P76](proposition_76_finite_sample_target_model_adequacy.md). Provenance: [P76 equation record](p76_equation_provenance.md). Implementation: [`finite_sample_target_model_adequacy.py`](../src/consciousness_bridge/finite_sample_target_model_adequacy.py). Tests: [`test_finite_sample_target_model_adequacy.py`](../tests/test_finite_sample_target_model_adequacy.py).

### P77: finite-sample full-law model-set separation

P76 provides finite-data rejection through selected necessary P75 polynomial constraints. P77 states the stronger confidence-set inversion criterion for the complete declared observed-law model family. For an alphabet of size \(K\),

\[
\\varepsilon_{n,K}(\\alpha)=\\sqrt{\\frac{\\log(2K/\\alpha)}{2n}},
\\qquad
\\delta_{n,K}(\\alpha)=\\min\\{2,K\\varepsilon_{n,K}(\\alpha)\\}.
\]

If \(\\mathcal C_n(\\widehat P)\) is the corresponding simultaneous empirical-law confidence region and \(\\mathcal M\) is the declared model set, then

\[
\\boxed{\\mathcal C_n(\\widehat P)\\cap\\mathcal M=\\varnothing
\\Longrightarrow P\\notin\\mathcal M}
\]

with confidence at least \(1-\\alpha\). Equivalently, a sound lower bound on distance from \(\\widehat P\) to \(\\mathcal M\) that exceeds the sampling radius certifies rejection. A numerical candidate model supplies an upper bound on the minimum distance and cannot by itself certify incompatibility of a continuous family.

![P77 full-law model-set separation](figures/p77_full_law_model_set_separation.svg)

Direct proof: [P77](proposition_77_full_law_model_set_separation.md). Provenance: [P77 equation record](p77_equation_provenance.md). Implementation: [`full_law_model_set_separation.py`](../src/consciousness_bridge/full_law_model_set_separation.py). Tests: [`test_full_law_model_set_separation.py`](../tests/test_full_law_model_set_separation.py).


## 3. Complete proposition index"""
    text = replace_once(text, marker, section, "roadmap P77 section")

    lines = text.splitlines()
    p76_index = next((i for i, line in enumerate(lines) if line.startswith("| [P76](") and "finite-sample" in line.lower()), None)
    if p76_index is None:
        raise RuntimeError("roadmap P76 index row missing")
    if any(line.startswith("| [P77](") for line in lines):
        raise RuntimeError("roadmap P77 index row already present")
    lines.insert(p76_index + 1, "| [P77](proposition_77_full_law_model_set_separation.md) | confidence-region/model-set separation | finite-sample full-law rejection with certified distance lower bounds | proved conditional theorem |")
    text = "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    write(path, text)


def patch_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    text = text.replace("current documented theorem frontier is **P76**", "current documented theorem frontier is **P77**")
    text = text.replace("**P1 through P76**", "**P1 through P77**")
    text = text.replace("P71-P76", "P71-P77")
    text = text.replace("from P1 through P76", "from P1 through P77")

    for number in range(23, 12, -1):
        text = text.replace(f"\n{number}. ", f"\n{number + 1}. ")
    p76_item = "12. [P76 finite-sample target-model adequacy rejection](proposition_76_finite_sample_target_model_adequacy.md) for simultaneous sixteen-cell uncertainty, denominator-free polynomial adequacy intervals, and the distinction between certified rejection and inconclusive non-rejection."
    p77_item = "13. [P77 finite-sample full-law model-set separation](proposition_77_full_law_model_set_separation.md) for confidence-region separation from the complete declared model family, model-distance transport, and the certified-lower-bound requirement for continuous-family rejection."
    text = replace_once(text, p76_item, p76_item + "\n" + p77_item, "navigation reading order")

    p76_branch = "| Finite-sample target-model adequacy | P76 | Turns tracked P75 population restrictions into simultaneous one-sided finite-data rejection certificates | [P76](proposition_76_finite_sample_target_model_adequacy.md) |"
    p77_branch = "| Full-law finite-sample target-model adequacy | P77 | Inverts the complete empirical-law confidence region against the declared model set and requires certified global separation for rejection | [P77](proposition_77_full_law_model_set_separation.md) |"
    text = replace_once(text, p76_branch, p76_branch + "\n" + p77_branch, "navigation branch map")

    lines = text.splitlines()
    p76_index = next((i for i, line in enumerate(lines) if line.startswith("| P76 |")), None)
    if p76_index is None:
        raise RuntimeError("navigation P76 proposition row missing")
    if any(line.startswith("| P77 |") for line in lines):
        raise RuntimeError("navigation P77 proposition row already present")
    lines.insert(p76_index + 1, "| P77 | [Full-law model-set separation](proposition_77_full_law_model_set_separation.md) | finite-sample confidence-region separation from the complete declared model family |")
    text = "\n".join(lines) + ("\n" if text.endswith("\n") else "")

    p76_prov = "[P76 equation and provenance record](p76_equation_provenance.md)"
    require(text, p76_prov, "navigation P76 provenance")
    if "[P77 equation and provenance record](p77_equation_provenance.md)" not in text:
        insert_at = text.find("[P76 equation and provenance record](p76_equation_provenance.md)")
        line_end = text.find("\n", insert_at)
        text = text[: line_end + 1] + "23. [P77 equation and provenance record](p77_equation_provenance.md) for full-law confidence-region inversion, model-distance transport, and certification-bound direction.\n" + text[line_end + 1 :]
    write(path, text)


def patch_detail() -> None:
    path = "docs/detailed_proposition_record.md"
    text = read(path)
    text = text.replace("## Complete P1 to P76 chronology", "## Complete P1 to P77 chronology")
    marker = "Direct P76 proof: [finite-sample target-model adequacy rejection](proposition_76_finite_sample_target_model_adequacy.md). Equation classification: [P76 equation and provenance record](p76_equation_provenance.md). Implementation: [`finite_sample_target_model_adequacy.py`](../src/consciousness_bridge/finite_sample_target_model_adequacy.py).\n\n\n---\n\n## Scientific interpretation of the chronology"
    section = """Direct P76 proof: [finite-sample target-model adequacy rejection](proposition_76_finite_sample_target_model_adequacy.md). Equation classification: [P76 equation and provenance record](p76_equation_provenance.md). Implementation: [`finite_sample_target_model_adequacy.py`](../src/consciousness_bridge/finite_sample_target_model_adequacy.py).

**P77** closes the finite-data full-law gap left explicit by P76. Let \(\\mathcal M\) be the complete declared observed-law model set and let \(\\mathcal C_n(\\widehat P)\) be a simultaneous confidence region for the population law. P77 proves that

\[
\\mathcal C_n(\\widehat P)\\cap\\mathcal M=\\varnothing
\]

is a valid finite-sample rejection certificate at the confidence level used to construct \(\\mathcal C_n\). For a finite alphabet of size \(K\), the same Hoeffding event used by P76 gives explicit \(L^\\infty\) and \(L^1\) radii. Distance to a nonempty set is 1-Lipschitz, so empirical model distance and population model distance differ by at most the corresponding sampling radius on that event.

P77 also makes the computational direction explicit. A candidate model found by numerical optimization provides an upper bound on the minimum distance to a continuous model family. It cannot be treated as a rejection lower bound. Full-law rejection therefore requires a sound global distance lower bound or an equivalent certified feasibility argument. Exhaustive comparison is exact only when the declared model family itself is finite.

Direct P77 proof: [finite-sample full-law model-set separation](proposition_77_full_law_model_set_separation.md). Equation classification: [P77 equation and provenance record](p77_equation_provenance.md). Implementation: [`full_law_model_set_separation.py`](../src/consciousness_bridge/full_law_model_set_separation.py).


---

## Scientific interpretation of the chronology"""
    text = replace_once(text, marker, section, "detail P77 chronology")
    text = text.replace("P71-P76 return to the target side", "P71-P77 return to the target side")
    text = replace_once(
        text,
        "P76 adds a finite-sample rejection layer for a tracked family of necessary P75 polynomial constraints. Its non-rejection output is explicitly inconclusive. The next target-side problem is stronger finite-sample full-law adequacy characterization, sharper power, and robust alternatives for residually dependent or learned target-view systems.",
        "P76 adds a finite-sample rejection layer for a tracked family of necessary P75 polynomial constraints. Its non-rejection output is explicitly inconclusive. P77 then defines the stronger finite-sample full-law criterion by asking whether the complete confidence region is separated from the complete declared model family. Its next computational problem is certified global lower-bounding or feasibility for the continuous P75 latent model, followed by sharper power and robust alternatives for residually dependent or learned target-view systems.",
        "detail frontier interpretation",
    )
    write(path, text)


def patch_equation_map() -> None:
    path = "docs/equation_and_citation_map.md"
    text = read(path)
    if "# P77 finite-sample full-law model-set separation" in text:
        raise RuntimeError("equation map already contains P77")
    text = text.rstrip() + """

# P77 finite-sample full-law model-set separation

P77 extends P76 from selected necessary polynomial restrictions to the complete declared observed-law model set.

- **Simultaneous cell radius:**
  \[
  \\varepsilon_{n,K}(\\alpha)=\\sqrt{\\frac{\\log(2K/\\alpha)}{2n}}.
  \]
  **Status:** standard Hoeffding plus union bound.

- **Induced full-law radius:**
  \[
  \\delta_{n,K}(\\alpha)=\\min\\{2,K\\varepsilon_{n,K}(\\alpha)\\}.
  \]
  **Status:** standard finite-dimensional norm inequality.

- **Full-law rejection gate:**
  \[
  \\mathcal C_n(\\widehat P)\\cap\\mathcal M=\\varnothing
  \\Longrightarrow P\\notin\\mathcal M.
  \]
  **Status:** standard confidence-region inversion, integrated here into the P71-P77 target-validity architecture.

- **Distance transport:**
  \[
  |d(\\widehat P,\\mathcal M)-d(P,\\mathcal M)|
  \\le\\|\\widehat P-P\\|.
  \]
  **Status:** standard 1-Lipschitz distance-to-set property.

- **Certified computational interface:** a sound lower bound \(L\\le d(\\widehat P,\\mathcal M)\) rejects when \(L\) exceeds the sampling radius. A candidate best-fit law gives an upper bound and cannot by itself certify rejection of a continuous family.
  **Status:** standard optimization-bound direction used as an explicit scientific safeguard.

Proof: [P77](proposition_77_full_law_model_set_separation.md). Dedicated provenance: [P77 equation and provenance record](p77_equation_provenance.md). Implementation: [`full_law_model_set_separation.py`](../src/consciousness_bridge/full_law_model_set_separation.py). Tests: [`test_full_law_model_set_separation.py`](../tests/test_full_law_model_set_separation.py).

The physical-to-experiential bridge remains open.
"""
    write(path, text)


def patch_changelog() -> None:
    path = "CHANGELOG.md"
    text = read(path)
    if text.startswith("# 0.77.0 - 2026-09-10"):
        raise RuntimeError("changelog already contains P77 release")
    entry = """# 0.77.0 - 2026-09-10

## Proposition 77: finite-sample full-law model-set separation

- adds a finite-alphabet confidence-region inversion theorem for the complete declared observed-law model set;
- proves equivalent rejection criteria using empirical distance to the model set in L-infinity or L1;
- uses the 1-Lipschitz property of distance to a nonempty set to transport empirical model distance into a finite-sample population-distance interval;
- adds conservative fixed-margin sample-size conditions;
- makes the optimization-bound direction explicit: a candidate best fit supplies an upper bound on model distance and cannot by itself certify rejection of a continuous family;
- adds an exact finite-family executable certificate while leaving certified global lower-bounding for the continuous P75 latent family as an open computational problem;
- adds the P77 proof, provenance record, theorem figure, geometry tests, implementation, regression tests, and public research integration;
- keeps non-rejection explicitly inconclusive and keeps the physical-to-experiential bridge open.

"""
    write(path, entry + text)


def patch_website_index() -> None:
    path = "website/index.html"
    text = read(path)
    text = text.replace("v0.76.0", "v0.77.0")
    text = text.replace("<strong>76</strong><span>proposition-level results</span>", "<strong>77</strong><span>proposition-level results</span>")
    text = text.replace("all 76 results", "all 77 results")
    text = text.replace("P71-P76", "P71-P77")
    text = text.replace("P1-P76", "P1-P77")
    text = text.replace("finite-sample rejection of tracked adequacy violations.", "finite-sample rejection of tracked adequacy violations, and full-law confidence-region separation from the complete declared model family.")
    text = text.replace("finite-sample adequacy certificate, bridge class", "finite-sample adequacy certificate, full-law model-set separation certificate, bridge class")
    text = text.replace("finite-sample adequacy, mathematical consequences", "finite-sample adequacy, full-law adequacy, mathematical consequences")

    p76_flow = '<div class="flow-node"><span>08</span><h3>Finite adequacy</h3><p>P76 asks whether an apparent P75 model violation remains separated from zero after finite-sample uncertainty is propagated.</p></div>\n        <div class="flow-node"><span>09</span><h3>Bridge test</h3><p>Test whether independently justified target distinctions are determined by the declared physical information.</p></div>'
    p77_flow = '<div class="flow-node"><span>08</span><h3>Finite adequacy</h3><p>P76 asks whether an apparent P75 model violation remains separated from zero after finite-sample uncertainty is propagated.</p></div>\n        <div class="flow-node"><span>09</span><h3>Full-law adequacy</h3><p>P77 asks whether the complete confidence region is separated from the complete declared model family, using only certified model-distance or feasibility evidence.</p></div>\n        <div class="flow-node"><span>10</span><h3>Bridge test</h3><p>Test whether independently justified target distinctions are determined by the declared physical information.</p></div>'
    text = replace_once(text, p76_flow, p77_flow, "website flow")
    text = text.replace("\\to\\text{finite adequacy}\\to\\text{bridge test}", "\\to\\text{finite adequacy}\\to\\text{full-law adequacy}\\to\\text{bridge test}")

    old_head = '<div class="section-head"><p class="eyebrow">Current theorem frontier</p><h2>P71-P77 strengthen the target side of the bridge test</h2><p>P71 asks whether the target is non-circular. P72 asks whether noisy observation preserves its distinctions. P73 asks whether channel reliability can be identified rather than assumed. P74 asks whether finite data justify trusting that recovered channel. P75 asks whether the measurement model itself survives independent adequacy checks. P76 asks whether finite data are strong enough to reject a tracked adequacy violation after sampling uncertainty is included.</p></div>'
    new_head = '<div class="section-head"><p class="eyebrow">Current theorem frontier</p><h2>P71-P77 strengthen the target side of the bridge test</h2><p>P71 asks whether the target is non-circular. P72 asks whether noisy observation preserves its distinctions. P73 asks whether channel reliability can be identified rather than assumed. P74 asks whether finite data justify trusting that recovered channel. P75 asks whether the measurement model itself survives independent adequacy checks. P76 asks whether finite data are strong enough to reject a tracked adequacy violation after sampling uncertainty is included. P77 asks whether the complete finite-sample confidence region is separated from the complete declared model family, while requiring certified global evidence rather than an ordinary best-fit value.</p></div>'
    text = replace_once(text, old_head, new_head, "website result heading")

    p76_result = '<article class="result"><span>P76</span><h3>Finite-sample model rejection</h3><p>One simultaneous sixteen-cell confidence event is propagated to denominator-free P75 polynomial constraints. Excluding zero certifies incompatibility; non-rejection remains inconclusive.</p></article>'
    p77_result = '<article class="result"><span>P77</span><h3>Full-law model-set separation</h3><p>The complete empirical-law confidence region is tested against the complete declared model family. Rejection requires certified separation; a local best-fit value alone is not enough.</p></article>'
    text = replace_once(text, p76_result, p76_result + "\n        " + p77_result, "website P77 result card")

    p76_figure = '<div class="figure-card"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p76_finite_sample_target_model_adequacy.svg" alt="P76 finite-sample target-model adequacy rejection"/><div><h3>P76 theorem figure</h3><p>The figure shows one shared finite-sample confidence event feeding P75 polynomial adequacy intervals. A separated interval certifies rejection, while non-rejection is not model acceptance.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_76_finite_sample_target_model_adequacy.md">Read Proposition 76 →</a></div></div>'
    p77_figure = '<div class="figure-card"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p77_full_law_model_set_separation.svg" alt="P77 finite-sample full-law model-set separation"/><div><h3>P77 theorem figure</h3><p>The figure contrasts P76 necessary-constraint rejection with P77 full-law model-set separation and highlights the critical distinction between certified distance lower bounds and ordinary best-fit upper bounds.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_77_full_law_model_set_separation.md">Read Proposition 77 →</a></div></div>'
    text = replace_once(text, p76_figure, p76_figure + "\n\n      " + p77_figure, "website P77 figure")

    p76_falsify = '<div><h3>Finite adequacy rejection</h3><p>Use P76 to reject only when a simultaneous necessary-constraint interval excludes zero. Do not convert non-rejection into model validation.</p></div>'
    p77_falsify = '<div><h3>Full-law adequacy rejection</h3><p>Use P77 only when the confidence region is certified disjoint from the complete model family. A local candidate fit is not a global separation certificate.</p></div>'
    text = replace_once(text, p76_falsify, p76_falsify + p77_falsify, "website P77 falsification")

    p76_source = '<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p76_equation_provenance.md"><h3>P76 provenance</h3><p>Classifies sixteen-cell concentration, polynomial interval propagation, finite-sample rejection, and the non-rejection boundary.</p></a>'
    p77_source = '<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p77_equation_provenance.md"><h3>P77 provenance</h3><p>Classifies full-law confidence-region inversion, model-distance transport, and the certified lower-bound requirement for continuous-family rejection.</p></a>'
    text = replace_once(text, p76_source, p76_source + "\n        " + p77_source, "website P77 provenance")
    write(path, text)


def patch_research_map() -> None:
    path = "website/research-map.html"
    text = read(path)
    text = text.replace("P71-P76", "P71-P77")
    text = text.replace("P1-P76", "P1-P77")
    text = text.replace("P1 through P76", "P1 through P77")
    text = text.replace("76 results", "77 results")
    if "P77" not in text:
        marker = "</main>"
        block = """
    <section class="boundary">
      <h2>P77: full-law model-set separation</h2>
      <p>P76 can reject through selected necessary polynomial constraints. P77 defines the stronger finite-sample criterion for the complete declared observed-law model family: the empirical-law confidence region must be certified disjoint from that entire family before full-law rejection is claimed.</p>
      <p>A numerical candidate fit supplies an upper bound on the minimum model distance. P77 therefore requires a sound lower bound or equivalent certified feasibility proof before rejecting a continuous family.</p>
      <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_77_full_law_model_set_separation.md">Read Proposition 77</a></p>
      <img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p77_full_law_model_set_separation.svg" alt="P77 finite-sample full-law model-set separation" />
    </section>

"""
        text = replace_once(text, marker, block + marker, "research map P77 block")
    write(path, text)


def patch_visual_atlas() -> None:
    path = "website/visual-atlas.html"
    text = read(path)
    if "p77_full_law_model_set_separation.svg" not in text:
        marker = "</main>"
        block = """
    <section class="figure-card">
      <img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p77_full_law_model_set_separation.svg" alt="P77 finite-sample full-law model-set separation" />
      <div>
        <p class="eyebrow">P77</p>
        <h2>Finite-Sample Full-Law Model-Set Separation</h2>
        <p>The figure shows the transition from P76 interpretable necessary-constraint tests to the stronger P77 requirement that the complete confidence region be separated from the complete declared model set. It also highlights why an ordinary best-fit candidate is an upper bound on model distance, not a rejection certificate.</p>
        <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_77_full_law_model_set_separation.md">Open the P77 proof</a>
      </div>
    </section>

"""
        text = replace_once(text, marker, block + marker, "visual atlas P77 block")
    write(path, text)


def main() -> None:
    patch_readme()
    patch_citation_guide()
    patch_roadmap()
    patch_navigation()
    patch_detail()
    patch_equation_map()
    patch_changelog()
    patch_website_index()
    patch_research_map()
    patch_visual_atlas()
    print("P77 publication patch: PASS")


if __name__ == "__main__":
    main()
