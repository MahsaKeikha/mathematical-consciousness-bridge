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
        raise RuntimeError(f"{label}: expected one anchor, found {count}: {old!r}")
    return text.replace(old, new, 1)


def replace_if_present(text: str, old: str, new: str) -> str:
    return text.replace(old, new)


def insert_before_once(text: str, anchor: str, block: str, label: str) -> str:
    count = text.count(anchor)
    if count != 1:
        raise RuntimeError(f"{label}: expected one anchor, found {count}: {anchor!r}")
    return text.replace(anchor, block + anchor, 1)


def insert_after_once(text: str, anchor: str, block: str, label: str) -> str:
    count = text.count(anchor)
    if count != 1:
        raise RuntimeError(f"{label}: expected one anchor, found {count}: {anchor!r}")
    return text.replace(anchor, anchor + block, 1)


def replace_section(text: str, start: str, end: str, replacement: str, label: str) -> str:
    start_count = text.count(start)
    end_count = text.count(end)
    if start_count != 1 or end_count != 1:
        raise RuntimeError(
            f"{label}: expected unique section anchors, got start={start_count}, end={end_count}"
        )
    i = text.index(start)
    j = text.index(end, i)
    return text[:i] + replacement + text[j:]


def patch_readme() -> None:
    path = "README.md"
    text = read(path)
    if "## 1.13 P79: joint statistical-computational power for full-law rejection" in text:
        raise RuntimeError("README already contains P79 section")

    text = replace_once(
        text,
        "version-0.78.0-2563eb",
        "version-0.79.0-2563eb",
        "README version badge",
    )

    plain_anchor = (
        "A small lower bound remains inconclusive; P78 does not turn failure to reject into model validation.\n\n"
        "Only after the physical description"
    )
    p79_plain = (
        "A small lower bound remains inconclusive; P78 does not turn failure to reject into model validation.\n\n"
        "P79 asks how much statistical evidence and computational precision are jointly enough to make that full-law rejection reliable before an experiment is run. It keeps three budgets separate: the rejection level, the desired power, and the remaining certified optimization error. A larger optimization error consumes part of the separation margin that would otherwise be available to absorb sampling uncertainty, so collecting more data and refining the certified computation are mathematically exchangeable only through an explicit bound. P79 also distinguishes three outcomes from a certified distance bracket: certified rejection, an explicit overlap witness when an admissible model lies inside the confidence region, and an unresolved case when the bracket still straddles the decision boundary. If the sufficient planning inequality fails, that does not mean the true power is zero; it means this conservative guarantee is not yet available. The population separation margin used for a prospective power claim must be prespecified or justified independently rather than chosen after seeing the same test result.\n\n"
        "Only after the physical description"
    )
    text = replace_once(text, plain_anchor, p79_plain, "README P79 plain-language insertion")

    narrative_anchor = (
        "P78 supplies a certified continuous-family lower-bound procedure for the specific P75 model by exploiting its multi-affine parameterization and exact-rational box refinement. Others"
    )
    narrative_replacement = (
        "P78 supplies a certified continuous-family lower-bound procedure for the specific P75 model by exploiting its multi-affine parameterization and exact-rational box refinement. P79 then budgets statistical uncertainty and certified optimization error together, separating rejection calibration from desired power and refusing to treat an unresolved computational bracket as either rejection or acceptance. Others"
    )
    text = replace_once(text, narrative_anchor, narrative_replacement, "README P79 narrative insertion")

    abstract_block = """
P79 adds a prospective joint statistical-computational power theorem to the P77-P78 full-law interface. If the population law has declared model-set separation at least $\Delta_0$, the P77 rejection radius is calibrated at level $\alpha$, the alternative-side empirical-law concentration radius is calibrated at $\beta$, and the P78 certified optimization gap is at most $\eta$, then

$$
\boxed{
\Delta_0
>
\varepsilon_{n,K}(\alpha)
+
\varepsilon_{n,K}(\beta)
+
\eta
}
$$

is sufficient for Type I error at most $\alpha$ and power at least $1-\beta$ against the declared separated alternative class. P79 also gives the equivalent sufficient sample-size inequality, a maximum certified optimization-tolerance budget, and a three-way reject/overlap/unresolved computational decision. Failure of this sufficient power condition is not an impossibility statement about actual power, and the population separation margin must have a defensible prospective provenance.

"""
    text = insert_before_once(
        text,
        "# Scientific status discipline",
        abstract_block,
        "README P79 abstract",
    )

    for old, new in (
        ("P71-P78", "P71-P79"),
        ("P1 through P78 with explicit dependency branches", "P1 through P79 with explicit dependency branches"),
        ("78 proposition-level results", "79 proposition-level results"),
        ("66 equation-driven quantitative figures", "67 equation-driven quantitative figures"),
        ("The theorem frontier is P78.", "The theorem frontier is P79."),
        ("| Public theorem frontier | **P78** |", "| Public theorem frontier | **P79** |"),
        ("| Documented version | **v0.78.0** |", "| Documented version | **v0.79.0** |"),
        ("| Proposition-level results | **78** |", "| Proposition-level results | **79** |"),
        ("| Equation-driven quantitative figures | **66** |", "| Equation-driven quantitative figures | **67** |"),
        ("Read the complete P1 to P78 detailed proposition record", "Read the complete P1 to P79 detailed proposition record"),
        ("Version 0.78.0", "Version 0.79.0"),
        ("Version **0.78.0**", "Version **0.79.0**"),
        ("theorem frontier **P78**", "theorem frontier **P79**"),
    ):
        text = replace_if_present(text, old, new)

    for number in range(27, 13, -1):
        old = f"**Figure {number}."
        new = f"**Figure {number + 1}."
        count = text.count(old)
        if count != 1:
            raise RuntimeError(
                f"README figure renumber: expected exactly one Figure {number}, found {count}"
            )
        text = text.replace(old, new, 1)

    p79_section = r"""
## 1.13 P79: joint statistical-computational power for full-law rejection

P77 controls finite-sample false rejection through a simultaneous confidence radius. P78 controls deterministic optimization error through a certified model-distance lower-bound gap. P79 asks how those two uncertainties jointly determine prospective power.

Let the true population law satisfy

$$
d_\infty(P,\mathcal M)\ge\Delta_0,
$$

and suppose the P78-style certified lower bound $L_n$ satisfies

$$
0\le d_\infty(\widehat P_n,\mathcal M)-L_n\le\eta.
$$

Using separate concentration levels for rejection and power gives the sufficient condition

$$
\boxed{
\Delta_0
>
\varepsilon_{n,K}(\alpha)
+
\varepsilon_{n,K}(\beta)
+
\eta.
}
$$

Under that condition, the P77 rejection rule retains Type I error at most $\alpha$ and has power at least $1-\beta$ over the declared alternative class. For the Hoeffding specialization, a sufficient prospective sample size is

$$
\boxed{
n>
\frac{\left(\sqrt{\log(2K/\alpha)}+\sqrt{\log(2K/\beta)}\right)^2}
{2(\Delta_0-\eta)^2}
}
$$

when $0\le\eta<\Delta_0$.

P79 also turns the empirical distance bracket into a three-way decision. If the certified lower bound exceeds the rejection radius, rejection is certified. If an explicit admissible candidate gives an upper bound inside the closed confidence ball, there is an explicit overlap witness. If the bracket straddles the radius, the computation remains unresolved. An overlap witness is not model acceptance, and a failed sufficient power certificate does not imply that actual power is zero.

The planning separation margin $\Delta_0$ must be prespecified or justified independently for the prospective guarantee stated here. The exact executable handoff uses rational certified bounds; the convenience logarithm and square-root calculation is a numerical planning helper rather than a formal interval proof.

![P79 joint statistical-computational power](docs/figures/p79_joint_statistical_computational_power.svg)

**Figure 14. P79 joint statistical-computational power.** The first panel separates certified rejection, explicit confidence-model overlap, and an unresolved optimization bracket. The second panel shows how the rejection radius, power radius, and P78 optimization gap consume one declared population-separation budget. The third panel shows the sample-size/computation tradeoff. The result is a prospective statistical-computational guarantee, not a consciousness ontology.

Direct proof: [Proposition 79](docs/proposition_79_joint_statistical_computational_power.md). Equation and literature classification: [P79 provenance record](docs/p79_equation_provenance.md). Implementation: [`joint_statistical_computational_power.py`](src/consciousness_bridge/joint_statistical_computational_power.py). Tests: [`test_joint_statistical_computational_power.py`](tests/test_joint_statistical_computational_power.py).

"""
    text = insert_before_once(
        text,
        "\n---\n\n# 2. From physical dynamics to operational structure",
        p79_section,
        "README P79 theorem section",
    )

    established_anchor = (
        "20. P78 supplies a certified global L-infinity lower bound for the continuous P75 family by exact-rational multi-affine box refinement, with an explicit mesh-gap guarantee and a direct P77 rejection handoff.\n"
        "21. The experiment-design branch provides scheduling, stopping, calibration, integer optimization, and primal-dual certification without promoting those results into consciousness ontology."
    )
    established_replacement = (
        "20. P78 supplies a certified global L-infinity lower bound for the continuous P75 family by exact-rational multi-affine box refinement, with an explicit mesh-gap guarantee and a direct P77 rejection handoff.\n"
        "21. P79 combines the P77 rejection radius, a separate alternative-side concentration radius, and the P78 deterministic optimization gap into a sufficient prospective power guarantee, with explicit sample-size and computational-tolerance budgets.\n"
        "22. The experiment-design branch provides scheduling, stopping, calibration, integer optimization, and primal-dual certification without promoting those results into consciousness ontology."
    )
    text = replace_once(
        text,
        established_anchor,
        established_replacement,
        "README established-results P79",
    )

    text = replace_once(
        text,
        "- extend P78's certified continuous-family computation with tighter pruning, sharper relaxations, and power-aware stopping criteria;",
        "- extend P78's certified continuous-family computation with tighter pruning and sharper global relaxations while using P79 to make the stopping tolerance scientifically power-aware;",
        "README open bullet",
    )

    old_open = (
        "The most immediate target-side problem after P78 is **tighter certified computation and power for full-law adequacy**. P78 supplies a rigorous exact-rational branch-and-bound lower bound for the continuous P75 family, but the nine-dimensional search can be expensive. The next methodological target is stronger certified pruning or relaxation, potentially using interval tightening or polynomial moment-SOS lower bounds, together with sharper power analysis and broader target-view dependence models."
    )
    new_open = (
        "The most immediate target-side problem after P79 is **tighter global certification and broader target-measurement models**. P79 closes the first explicit joint power budget for the P77-P78 Hoeffding setting, but the nine-dimensional P78 search can still be expensive and the concentration bound is deliberately conservative. The next methodological targets are stronger certified pruning or relaxation, sharper concentration and power analysis, and target-view models that allow residual dependence, shared bias, temporal drift, or learned measurement pipelines."
    )
    text = replace_once(text, old_open, new_open, "README open-frontier paragraph")

    p78_falsification = (
        "| Continuous P75 full-law separation is certified | A P78 global lower bound exceeds a valid P77 sampling-radius upper bound | Treating an incomplete parameter search or ordinary floating approximation as a formal certificate |"
    )
    p79_falsification = (
        p78_falsification
        + "\n| Joint power guarantee is certified | A prespecified or independently justified separation margin exceeds the rejection radius, alternative-side concentration radius, and certified optimization gap | Treating failure of the sufficient P79 margin as proof that actual power is zero |"
    )
    text = replace_once(text, p78_falsification, p79_falsification, "README P79 falsification row")

    p78_resource = (
        "| [P78 equation and provenance record](docs/p78_equation_provenance.md) | Multi-affine box enclosures, global branch-and-bound lower bounds, mesh-gap certification, and P77 handoff provenance |"
    )
    p79_resource = (
        p78_resource
        + "\n| [P79 equation and provenance record](docs/p79_equation_provenance.md) | Joint alpha-beta-optimization power budgeting, three-way certified decision logic, and sample-size/computation tradeoff provenance |"
    )
    text = replace_once(text, p78_resource, p79_resource, "README P79 provenance row")

    finite_old = (
        "P72 applies the same philosophy on the target side. P73 establishes population identifiability for its declared three-view model, and P74 propagates finite empirical-law uncertainty through that nonlinear inversion. P75 then makes the conditional-independence model itself falsifiable at population level by adding a fourth view and overidentifying restrictions. P76 adds a simultaneous finite-sample rejection certificate for the tracked P75 polynomial constraints. P77 upgrades the finite-data target to the complete declared observed-law model set through confidence-region separation. P78 then supplies an exact-rational branch-and-bound lower-bound certificate for the continuous P75 latent family. The remaining challenges are faster and tighter global certification, sharper power, and broader dependent-view alternatives."
    )
    finite_new = (
        "P72 applies the same philosophy on the target side. P73 establishes population identifiability for its declared three-view model, and P74 propagates finite empirical-law uncertainty through that nonlinear inversion. P75 then makes the conditional-independence model itself falsifiable at population level by adding a fourth view and overidentifying restrictions. P76 adds a simultaneous finite-sample rejection certificate for the tracked P75 polynomial constraints. P77 upgrades the finite-data target to the complete declared observed-law model set through confidence-region separation. P78 then supplies an exact-rational branch-and-bound lower-bound certificate for the continuous P75 latent family. P79 combines sampling uncertainty and certified optimization error into a prospective power budget. The remaining challenges are faster and tighter global certification, sharper concentration, and broader dependent-view alternatives."
    )
    text = replace_once(text, finite_old, finite_new, "README finite-experiment P79")

    if "0.78.0" in text:
        text = text.replace("0.78.0", "0.79.0")
    if "P71-P78" in text:
        text = text.replace("P71-P78", "P71-P79")

    write(path, text)


def patch_changelog() -> None:
    path = "CHANGELOG.md"
    text = read(path)
    if text.startswith("# 0.79.0"):
        raise RuntimeError("CHANGELOG already starts with 0.79.0")
    block = """# 0.79.0 - 2026-09-10

## Proposition 79: joint statistical-computational power

- combines the P77 finite-sample rejection radius with the P78 certified deterministic optimization gap in one prospective power theorem;
- separates the rejection level alpha from the desired Type II level beta rather than using one confidence parameter for both roles;
- proves the sufficient population-separation condition Delta_0 > epsilon_alpha + epsilon_beta + eta;
- derives the corresponding conservative sample-size inequality and maximum certified optimization-tolerance budget;
- adds a three-way certified decision: rejection, explicit confidence-model overlap witness, or unresolved optimization bracket;
- keeps an overlap witness distinct from model acceptance and keeps failure of the sufficient power inequality distinct from a zero-power claim;
- requires the prospective population-separation margin to be prespecified, independently justified, or treated as a sensitivity parameter;
- distinguishes the exact Fraction-based final certification interface from the floating-point planning helper;
- adds the P79 proof, provenance record, theorem figure, geometry guard, implementation, tests, and public research integration;
- keeps the physical-to-experiential bridge open.

"""
    write(path, block + text)


def patch_detailed_record() -> None:
    path = "docs/detailed_proposition_record.md"
    text = read(path)
    text = replace_once(
        text,
        "Complete P1 to P78 chronology",
        "Complete P1 to P79 chronology",
        "detailed record chronology",
    )
    text = replace_if_present(text, "P71-P78 return", "P71-P79 return")

    p79 = r"""
**P79** adds a prospective joint power budget to the P77-P78 full-law adequacy chain. P77 supplies the finite-sample rejection radius and P78 supplies a certified deterministic optimization-gap bound. P79 separates the rejection level $\alpha$ from the desired Type II level $\beta$ and proves the sufficient condition

\[
\Delta_0>
\varepsilon_{n,K}(\alpha)
+
\varepsilon_{n,K}(\beta)
+
\eta
\]

for power at least $1-\beta$ against population laws whose distance from the declared model set is at least $\Delta_0$, while preserving Type I error at most $\alpha$. It derives the corresponding sample-size and optimization-tolerance budgets and distinguishes certified rejection, explicit confidence-model overlap, and an unresolved optimization bracket. The planning margin must have prospective or independently justified provenance; failure of the sufficient condition is not an impossibility statement about actual power.

Direct P79 proof: [joint statistical-computational power](proposition_79_joint_statistical_computational_power.md). Equation classification: [P79 equation and provenance record](p79_equation_provenance.md). Implementation: [`joint_statistical_computational_power.py`](../src/consciousness_bridge/joint_statistical_computational_power.py).

"""
    text = insert_before_once(
        text,
        "\n---\n\n## Scientific interpretation of the chronology",
        p79,
        "detailed P79 insertion",
    )
    old = (
        "P76 adds a finite-sample rejection layer for a tracked family of necessary P75 polynomial constraints. Its non-rejection output is explicitly inconclusive. P77 then defines the stronger finite-sample full-law criterion by asking whether the complete confidence region is separated from the complete declared model family. P78 supplies the missing global lower-bound certificate for the continuous P75 latent family using exact-rational multi-affine box refinement. The next problems are computational efficiency, sharper power, and robust alternatives for residually dependent or learned target-view systems."
    )
    new = (
        "P76 adds a finite-sample rejection layer for a tracked family of necessary P75 polynomial constraints. Its non-rejection output is explicitly inconclusive. P77 then defines the stronger finite-sample full-law criterion by asking whether the complete confidence region is separated from the complete declared model family. P78 supplies the missing global lower-bound certificate for the continuous P75 latent family using exact-rational multi-affine box refinement. P79 adds the first explicit joint statistical-computational power budget for that rejection pipeline. The next problems are computational efficiency, sharper concentration, and robust alternatives for residually dependent or learned target-view systems."
    )
    text = replace_once(text, old, new, "detailed interpretation P79")
    write(path, text)


def patch_equation_map() -> None:
    path = "docs/equation_and_citation_map.md"
    text = read(path)
    if "# P79 joint statistical-computational power" in text:
        raise RuntimeError("equation map already contains P79")
    block = r"""

---

# P79 joint statistical-computational power

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| $\varepsilon_{n,K}(q)=\sqrt{\log(2K/q)/(2n)}$ | simultaneous finite-alphabet $L^\infty$ empirical-law radius | standard Hoeffding plus union bound | [P77](proposition_77_full_law_model_set_separation.md), [P79](proposition_79_joint_statistical_computational_power.md) |
| $|d_\infty(R,\mathcal M)-d_\infty(S,\mathcal M)|\le\|R-S\|_\infty$ | transports empirical-law uncertainty to model-set distance | standard distance-to-set Lipschitz inequality | [P77](proposition_77_full_law_model_set_separation.md), [P79](proposition_79_joint_statistical_computational_power.md) |
| $L_n>r_n$ | certified rejection branch | repository decision protocol using valid lower bound | [P79](proposition_79_joint_statistical_computational_power.md) |
| $U_n\le r_n$ | explicit confidence-model overlap witness | repository decision protocol using admissible candidate upper bound; not model acceptance | [P79](proposition_79_joint_statistical_computational_power.md) |
| $L_n\le r_n<U_n$ | unresolved certified bracket | repository decision protocol | [P79](proposition_79_joint_statistical_computational_power.md) |
| $0\le d_\infty(\widehat P_n,\mathcal M)-L_n\le\eta$ | deterministic optimization error budget | imported P78-style certified gap | [P78](proposition_78_certified_continuous_model_separation.md), [P79](proposition_79_joint_statistical_computational_power.md) |
| $\Delta_0>\varepsilon_{n,K}(\alpha)+\varepsilon_{n,K}(\beta)+\eta$ | sufficient joint Type I, Type II, and computation margin | repository-specific composition of standard concentration with P77-P78 certificates | [P79](proposition_79_joint_statistical_computational_power.md) |
| $n>\big(\sqrt{\log(2K/\alpha)}+\sqrt{\log(2K/\beta)}\big)^2/[2(\Delta_0-\eta)^2]$ | conservative sufficient sample-size planning rule | direct algebraic consequence, not claimed minimax optimal | [P79](proposition_79_joint_statistical_computational_power.md) |
| $\eta_{\max}=\Delta_0-\varepsilon_{n,K}(\alpha)-\varepsilon_{n,K}(\beta)$ | certified optimization-tolerance budget | direct rearrangement of P79 power condition | [P79](proposition_79_joint_statistical_computational_power.md) |

P79 keeps the alternative margin $\Delta_0$ subject to an explicit prospective-provenance requirement. A failed sufficient power certificate does not prove zero actual power, and an overlap witness does not validate the declared target-measurement model. The physical-to-experiential bridge remains open.
"""
    write(path, text.rstrip() + block + "\n")


def patch_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    text = replace_once(
        text,
        "The current documented theorem frontier is **P78**. The proposition record runs from **P1 through P78 with explicit dependency branches**. P71-P78 return to the core P19 bridge-sufficiency lineage; they do not extend the P61-P70 calibration branch.",
        "The current documented theorem frontier is **P79**. The proposition record runs from **P1 through P79 with explicit dependency branches**. P71-P79 return to the core P19 bridge-sufficiency lineage; they do not extend the P61-P70 calibration branch.",
        "roadmap opening",
    )
    p78_line = "&\\text{P78: continuous P75 model distance must be lower-bounded globally and certifiably}"
    p79_line = (
        p78_line
        + "\\\\\n&\\Downarrow\\\\\n"
        + "&\\text{P79: statistical power and certified optimization error must share one explicit margin budget}"
    )
    text = replace_once(text, p78_line, p79_line, "roadmap dependency P79")
    text = replace_once(
        text,
        "The proposition number records development order. It does not imply that P78 depends on P70. P78 depends scientifically on P77 and the P75 continuous target-model family, which descend from P19 and the P71-P76 target-side lineage.",
        "The proposition number records development order. It does not imply that P79 depends on P70. P79 depends scientifically on P77-P78 and the P75 continuous target-model family, which descend from P19 and the P71-P76 target-side lineage.",
        "roadmap dependency prose",
    )
    p79_section = r"""
### P79: joint statistical-computational power

P77 supplies the finite-sample rejection radius and P78 supplies a certified deterministic optimization-gap bound. P79 introduces a separate Type II target $\beta$ and asks when the two uncertainty sources jointly guarantee rejection power.

If

\[
d_\infty(P,\mathcal M)\ge\Delta_0
\]

and

\[
0\le d_\infty(\widehat P_n,\mathcal M)-L_n\le\eta,
\]

then the sufficient P79 condition is

\[
\boxed{
\Delta_0>
\varepsilon_{n,K}(\alpha)
+
\varepsilon_{n,K}(\beta)
+
\eta.
}
\]

Under this condition the P77 rejection rule has Type I error at most $\alpha$ and power at least $1-\beta$ over the declared separated alternative class. P79 also derives the corresponding sufficient sample size and certified optimization-tolerance budget, and separates rejection, explicit confidence-model overlap, and unresolved computation.

![P79 joint statistical-computational power](figures/p79_joint_statistical_computational_power.svg)

Direct proof: [P79](proposition_79_joint_statistical_computational_power.md). Provenance: [P79 equation record](p79_equation_provenance.md). Implementation: [`joint_statistical_computational_power.py`](../src/consciousness_bridge/joint_statistical_computational_power.py). Tests: [`test_joint_statistical_computational_power.py`](../tests/test_joint_statistical_computational_power.py).

"""
    text = insert_before_once(text, "\n## 3. Complete proposition index", p79_section, "roadmap P79 section")

    p78_row_pattern = re.compile(r"^(\| \[P78\]\([^\n]+)$", re.MULTILINE)
    matches = p78_row_pattern.findall(text)
    if len(matches) != 1:
        raise RuntimeError(f"roadmap P78 index row: expected one, found {len(matches)}")
    p79_row = "| [P79](proposition_79_joint_statistical_computational_power.md) | joint concentration and certified optimization margin | prospective full-law rejection power and computation budget | proved conditional sufficient theorem |"
    text = p78_row_pattern.sub(lambda m: m.group(1) + "\n" + p79_row, text, count=1)

    open_section = r"""## 5. Current open frontier

After P79, the target side has nine explicit requirements:

1. the target must have non-circular provenance relative to the tested physical descriptor;
2. its observation channel must be valid and sufficiently informative for the claimed witness;
3. channel reliability must be identified or externally calibrated under a defensible target-measurement model;
4. finite data must resolve the channel parameters far enough from the model singularity to support a confidence-certified reliability statement;
5. the target-measurement model itself must survive adequacy tests rather than being accepted because it can be fit;
6. finite data must separate a genuine adequacy violation from sampling uncertainty before model rejection is claimed;
7. complete full-law rejection must be defined against the whole declared model family, not only selected necessary constraints;
8. when the declared family is continuous, the required separation distance must be lower-bounded globally rather than inferred from a local best fit;
9. prospective power must account jointly for rejection calibration, alternative-side sampling fluctuation, and certified optimization error.

P78 closes the eighth item for the specific P75 four-view binary latent family in L-infinity distance. P79 closes the first explicit version of the ninth item for the same finite-alphabet Hoeffding and certified-gap setting. It gives a conservative sufficient power guarantee and an explicit sample-size/computation tradeoff; it does not claim an optimal power function.

The remaining computational problem is efficiency: stronger pruning, tighter relaxations, or moment-SOS lower bounds may reduce the number of P78 boxes required for a decisive certificate. The remaining statistical problems include sharper concentration and power, adaptive stopping rules that preserve the prospective guarantee, and target-view models that allow residual dependence, shared bias, temporal drift, or learned measurement pipelines.

None of these results identifies a latent variable with consciousness. The physical-to-experiential bridge remains open.
"""
    marker = "## 5. Current open frontier"
    if text.count(marker) != 1:
        raise RuntimeError("roadmap current-frontier heading not unique")
    i = text.index(marker)
    text = text[:i] + open_section
    write(path, text)


def patch_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    text = replace_once(
        text,
        "The current documented theorem frontier is **P78**. The complete proposition record runs from **P1 through P78**. P71-P78 form a target-side methodology branch descending from the P19 physical-sufficiency question. They are not extensions of the P61-P70 calibration branch.",
        "The current documented theorem frontier is **P79**. The complete proposition record runs from **P1 through P79**. P71-P79 form a target-side methodology branch descending from the P19 physical-sufficiency question. They are not extensions of the P61-P70 calibration branch.",
        "navigation opening",
    )

    reading = """## Recommended reading order

1. [Main research study](../README.md) for the complete scientific narrative and curated figures.
2. [Bridge problem](bridge_problem.md) for the formal physical-to-experiential question.
3. [Scientific status discipline](../README.md#scientific-status-discipline) for the distinction among definitions, proved results, implementations, numerical checks, empirical inputs, hypotheses, and open bridge claims.
4. [Theorem roadmap](theorem_roadmap.md) for the dependency structure from P1 through P79.
5. [P19 fundamental physical sufficiency](proposition_19_fundamental_physical_sufficiency.md) for the exact, stochastic, and differential bridge criteria.
6. [P20-P24 finite and adaptive residual certification](theorem_roadmap.md) for finite-data and repeated-look validity.
7. [P71 target-provenance non-circularity](proposition_71_target_provenance_noncircularity.md) for the theorem showing when a target construction makes a bridge test vacuous by design.
8. [P72 target-measurement channel robustness](proposition_72_target_measurement_channel_robustness.md) for noisy-target residual transfer, witness erasure, target-channel stability, and the finite-sample target-separation certificate.
9. [P73 three-view target-channel identifiability](proposition_73_target_channel_identifiability.md) for population recovery of binary target channels and P72 stability coefficients under a declared three-view latent model, together with the two-view non-identifiability boundary.
10. [P74 finite-sample target-channel recovery](proposition_74_finite_sample_target_channel_recovery.md) for simultaneous confidence bounds, the covariance nondegeneracy gate, full binary-channel confidence orbits, and finite-data certification of P72/P73 target-channel quantities.
11. [P75 target-model adequacy and four-view overidentification](proposition_75_target_model_adequacy_overidentification.md) for the distinction between target-channel identifiability and model adequacy, six generic four-view overidentifying degrees of freedom, observable moment constraints, and full-law reconstruction.
12. [P76 finite-sample target-model adequacy rejection](proposition_76_finite_sample_target_model_adequacy.md) for simultaneous sixteen-cell uncertainty, denominator-free polynomial adequacy intervals, and the distinction between certified rejection and inconclusive non-rejection.
13. [P77 finite-sample full-law model-set separation](proposition_77_full_law_model_set_separation.md) for confidence-region separation from the complete declared model family, model-distance transport, and the certified-lower-bound requirement for continuous-family rejection.
14. [P78 certified continuous P75 model separation](proposition_78_certified_continuous_model_separation.md) for exact multi-affine box enclosures, global L-infinity distance lower bounds, mesh-gap convergence, and the strict P77 rejection handoff.
15. [P79 joint statistical-computational power](proposition_79_joint_statistical_computational_power.md) for the separate alpha and beta concentration budgets, the P78 optimization-gap term, the three-way certified decision, and the sample-size/computation tradeoff.
16. [P11-P18 and P25-P37 operational physical structure](theorem_roadmap.md) for intervention, temporal, compositional, and multiscale requirements.
17. [P38-P44 quantum foundations and bridge tests](quantum_foundations_and_bridge_test.md) for quantum operational sufficiency under explicit bridge classes.
18. [P45-P60 adaptive experiment design and scheduling](theorem_roadmap.md) for valid evidence collection and transition-calibration setup.
19. [P61-P70 Calibration and Optimization Frontier](calibration_optimization_frontier_p61_p70.md) for downstream integer resource-allocation mathematics.
20. [Equation and citation map](equation_and_citation_map.md) for equation-level provenance and theorem lineage.
21. [P72 equation and provenance record](p72_equation_provenance.md) for the standard-versus-repository classification of the noisy-target theorem.
22. [P73 equation and provenance record](p73_equation_provenance.md) for latent-class context, moment inversion, and the P72 stability connection.
23. [P74 equation and provenance record](p74_equation_provenance.md) for finite-sample concentration, nonlinear interval propagation, and full-channel recovery.
24. [P75 equation and provenance record](p75_equation_provenance.md) for just-identification, overidentification, algebraic adequacy constraints, and full-law reconstruction provenance.
25. [P76 equation and provenance record](p76_equation_provenance.md) for finite-sample adequacy rejection provenance.
26. [P77 equation and provenance record](p77_equation_provenance.md) for full-law confidence-region inversion and global lower-bound direction.
27. [P78 equation and provenance record](p78_equation_provenance.md) for multi-affine box bounds, global distance certification, and the P77 handoff.
28. [P79 equation and provenance record](p79_equation_provenance.md) for joint statistical-computational power budgeting and the prospective margin-provenance rule.
29. [Falsification program](falsification_program.md) for the empirical burden required before any bridge claim can be accepted.
30. [Citation guide](../CITATION.md) for citing the whole research program or a specific proposition, figure, algorithm, or implementation.

"""
    text = replace_section(
        text,
        "## Recommended reading order",
        "## Scientific branch map",
        reading,
        "navigation reading order",
    )

    p78_row = "| Certified continuous target-model separation | P78 | Supplies exact-rational global lower bounds for distance to the continuous P75 model family and a convergent mesh certificate | [P78](proposition_78_certified_continuous_model_separation.md) |"
    p79_row = "| Joint statistical-computational power | P79 | Budgets rejection calibration, desired power, and certified optimization error in one prospective full-law separation theorem | [P79](proposition_79_joint_statistical_computational_power.md) |"
    text = replace_once(text, p78_row, p78_row + "\n" + p79_row, "navigation branch map P79")

    p78_index_pattern = re.compile(r"^(\| P78 \| \[[^\n]+)$", re.MULTILINE)
    matches = p78_index_pattern.findall(text)
    if len(matches) != 1:
        raise RuntimeError(f"navigation P78 index row: expected one, found {len(matches)}")
    p79_index = "| P79 | [Joint statistical-computational power](proposition_79_joint_statistical_computational_power.md) | prospective Type I, power, and certified optimization-error budgeting for full-law rejection |"
    text = p78_index_pattern.sub(lambda m: m.group(1) + "\n" + p79_index, text, count=1)

    text = replace_if_present(text, "P71-P78", "P71-P79")
    text = replace_if_present(text, "P1 through P78", "P1 through P79")
    write(path, text)


def patch_website_index() -> None:
    path = "website/index.html"
    text = read(path)
    text = replace_once(text, "<strong>78</strong><span>proposition-level results</span>", "<strong>79</strong><span>proposition-level results</span>", "website count")
    text = replace_once(text, "<strong>v0.78.0</strong><span>current documented version</span>", "<strong>v0.79.0</strong><span>current documented version</span>", "website version")
    text = replace_if_present(text, "P71-P78", "P71-P79")
    text = replace_if_present(text, "See all 78 results", "See all 79 results")

    text = replace_once(
        text,
        "full-law confidence-region separation from the complete declared model family.</p>",
        "full-law confidence-region separation from the complete declared model family, certified continuous-family distance lower bounds, and joint statistical-computational power budgeting.</p>",
        "website hero P79",
    )
    text = replace_once(
        text,
        "full-law model-set separation certificate, bridge class, and uncertainty model must each be declared rather than hidden inside one score.",
        "full-law model-set separation certificate, certified optimization error, prospective power margin, bridge class, and uncertainty model must each be declared rather than hidden inside one score.",
        "website boundary P79",
    )
    text = replace_once(
        text,
        "<div class=\"flow-node\"><span>10</span><h3>Bridge test</h3><p>Test whether independently justified target distinctions are determined by the declared physical information.</p></div>",
        "<div class=\"flow-node\"><span>10</span><h3>Certified computation</h3><p>P78 lower-bounds distance to the continuous P75 family with an auditable global optimization certificate.</p></div>\n        <div class=\"flow-node\"><span>11</span><h3>Power and bridge test</h3><p>P79 budgets statistical and computational uncertainty before returning to the still-open physical-to-experiential bridge question.</p></div>",
        "website flow P79",
    )
    text = replace_once(
        text,
        "\\to\\text{full-law adequacy}\\to\\text{bridge test}",
        "\\to\\text{full-law adequacy}\\to\\text{certified computation}\\to\\text{power planning}\\to\\text{bridge test}",
        "website equation chain P79",
    )
    old_results = (
        "P71 asks whether the target is non-circular. P72 asks whether noisy observation preserves its distinctions. P73 asks whether channel reliability can be identified rather than assumed. P74 asks whether finite data justify trusting that recovered channel. P75 asks whether the measurement model itself survives independent adequacy checks. P76 asks whether finite data are strong enough to reject a tracked adequacy violation after sampling uncertainty is included. P77 asks whether the complete finite-sample confidence region is separated from the complete declared model family, while requiring certified global evidence rather than an ordinary best-fit value."
    )
    new_results = (
        "P71 asks whether the target is non-circular. P72 asks whether noisy observation preserves its distinctions. P73 asks whether channel reliability can be identified rather than assumed. P74 asks whether finite data justify trusting that recovered channel. P75 asks whether the measurement model itself survives independent adequacy checks. P76 asks whether finite data are strong enough to reject a tracked adequacy violation after sampling uncertainty is included. P77 asks whether the complete finite-sample confidence region is separated from the complete declared model family. P78 supplies a certified global lower bound for the continuous P75 family. P79 asks how rejection calibration, desired power, and certified optimization error share one prospective separation budget."
    )
    text = replace_once(text, old_results, new_results, "website results intro")

    p77_card = "<article class=\"result\"><span>P77</span><h3>Full-law model-set separation</h3><p>The complete empirical-law confidence region is tested against the complete declared model family. Rejection requires certified separation; a local best-fit value alone is not enough.</p></article>"
    added_cards = p77_card + "\n        <article class=\"result\"><span>P78</span><h3>Certified continuous separation</h3><p>Exact-rational multi-affine box refinement supplies a global lower bound and mesh-gap certificate for the continuous P75 family.</p></article>\n        <article class=\"result\"><span>P79</span><h3>Joint statistical-computational power</h3><p>A separate alpha rejection radius, beta power radius, and certified optimization gap share one prospective separation margin.</p></article>"
    text = replace_once(text, p77_card, added_cards, "website result cards P78-P79")

    p78_section_end = """    <section class=\"section\">
      <div class=\"section-head\"><p class=\"eyebrow\">P78 computational frontier</p><h2>Certified continuous P75 model separation</h2><p>P77 requires a sound global lower bound before a continuous model family can be rejected. P78 supplies one for the P75 four-view binary latent family using exact-rational multi-affine box refinement. Explicit model points remain upper bounds; only the certified lower side can trigger the P77 rejection gate.</p></div>
      <div class=\"figure-card\"><img src=\"https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p78_certified_continuous_model_separation.svg\" alt=\"P78 certified continuous model separation\"/><div><h3>P78 theorem figure</h3><p>Adaptive parameter boxes cover the full nine-dimensional P75 cube. Exact cell enclosures yield boxwise lower bounds, their minimum is globally valid, and the mesh width controls the remaining optimization gap.</p><a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_78_certified_continuous_model_separation.md\">Read Proposition 78 →</a></div></div>
    </section>
"""
    p79_section = """
    <section class=\"section\">
      <div class=\"section-head\"><p class=\"eyebrow\">P79 power frontier</p><h2>Joint statistical-computational power</h2><p>P79 combines the P77 rejection radius, a separate beta-level alternative concentration radius, and the P78 certified optimization gap. The resulting sufficient margin gives a prospective power guarantee without turning non-rejection or an unresolved bracket into model acceptance.</p></div>
      <div class=\"figure-card\"><img src=\"https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p79_joint_statistical_computational_power.svg\" alt=\"P79 joint statistical-computational power\"/><div><h3>P79 theorem figure</h3><p>The figure separates reject, overlap-witness, and unresolved decisions and shows how alpha, beta, and certified optimization error consume one declared population-separation budget.</p><a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_79_joint_statistical_computational_power.md\">Read Proposition 79 →</a></div></div>
    </section>
"""
    text = replace_once(text, p78_section_end, p78_section_end + p79_section, "website P79 section")
    write(path, text)


def patch_research_map() -> None:
    path = "website/research-map.html"
    text = read(path)
    text = replace_once(
        text,
        "Scientific dependency map of the Mathematical Consciousness Bridge through Proposition 76.",
        "Scientific dependency map of the Mathematical Consciousness Bridge through Proposition 79.",
        "research map metadata",
    )
    text = replace_once(text, "Seventy-six results, one dependency-aware scientific program", "Seventy-nine results, one dependency-aware scientific program", "research map hero count")
    text = replace_once(text, "<strong>76</strong><span>proposition-level results</span>", "<strong>79</strong><span>proposition-level results</span>", "research map status count")
    old_lede = "Proposition numbers record development order, not conceptual depth. P71-P78 return to the P19 bridge-sufficiency lineage after the P61-P70 calibration branch: P71 protects target provenance, P72 protects the target-observation interface, P73 identifies target channels under one explicit latent model, P74 asks when finite data are strong enough to certify that recovery, P75 asks whether the measurement model itself survives independent adequacy checks, and P76 asks whether finite data can certify an adequacy violation beyond sampling noise."
    new_lede = "Proposition numbers record development order, not conceptual depth. P71-P79 return to the P19 bridge-sufficiency lineage after the P61-P70 calibration branch: P71 protects target provenance, P72 protects target observation, P73-P74 identify and certify target channels under one explicit latent model, P75-P76 test model adequacy, P77 defines full-law confidence-region separation, P78 certifies continuous-family model distance, and P79 budgets statistical power together with certified optimization error."
    text = replace_once(text, old_lede, new_lede, "research map lede")
    text = replace_once(text, "<article class=\"result\"><span>6 · P73-P76</span><h3>Channel recovery and model adequacy</h3><p>Identify the declared binary target channel, certify that recovery from finite data, test whether a fourth view supports the model assumptions, then ask whether finite data are strong enough to reject a tracked violation.</p></article>", "<article class=\"result\"><span>6 · P73-P79</span><h3>Channel recovery, adequacy, and power</h3><p>Identify and certify the target channel, test the model, reject it through full-law evidence when warranted, certify the continuous optimization, and budget statistical power together with computation error.</p></article>", "research map stage six")
    text = replace_once(
        text,
        "P74-P76 continue that target-side branch with finite-data recovery, model-adequacy testing, and finite-sample adequacy rejection. None of P71-P78 is a consciousness ontology.",
        "P74-P79 continue that target-side branch with finite-data recovery, model-adequacy testing, full-law rejection, certified continuous optimization, and joint power budgeting. None of P71-P79 is a consciousness ontology.",
        "research map reading rule",
    )
    p78 = """    <section class=\"boundary\">
      <h2>P78: Certified continuous P75 model separation</h2>
      <p>P77 defines the full-law rejection criterion. P78 makes that criterion computationally certifiable for the continuous P75 four-view binary latent family by covering the complete nine-parameter cube with boxes whose exact multi-affine cell ranges give rigorous global L-infinity distance lower bounds.</p>
      <p>Candidate models still provide only upper bounds. A P77 rejection is triggered only when the P78 global lower bound exceeds a separately valid sampling-radius upper bound.</p>
      <p><a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_78_certified_continuous_model_separation.md\">Read Proposition 78</a></p>
      <img src=\"https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p78_certified_continuous_model_separation.svg\" alt=\"P78 certified continuous model separation\" />
    </section>"""
    p79 = """

    <section class=\"boundary\">
      <h2>P79: Joint statistical-computational power</h2>
      <p>P79 combines P77 finite-sample calibration and the P78 certified optimization gap in one prospective power theorem. A declared population separation must exceed the alpha-level rejection radius, the beta-level alternative concentration radius, and the certified optimization error.</p>
      <p>The theorem also distinguishes certified rejection, an explicit model-confidence-ball overlap witness, and an unresolved bracket. Failure of the sufficient power condition is not a zero-power result.</p>
      <p><a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_79_joint_statistical_computational_power.md\">Read Proposition 79</a></p>
      <img src=\"https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p79_joint_statistical_computational_power.svg\" alt=\"P79 joint statistical-computational power\" />
    </section>"""
    text = replace_once(text, p78, p78 + p79, "research map P79 section")
    write(path, text)


def patch_visual_atlas() -> None:
    path = "website/visual-atlas.html"
    text = read(path)
    text = replace_once(
        text,
        "From physical sufficiency to non-circular targets, noisy observation, channel recovery, model adequacy, and finite-sample rejection",
        "From physical sufficiency to non-circular targets, noisy observation, channel recovery, model adequacy, certified full-law separation, and power",
        "visual atlas heading",
    )
    p78 = """    <section class=\"figure-card\">
      <img src=\"https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p78_certified_continuous_model_separation.svg\" alt=\"P78 certified continuous model separation\" />
      <div>
        <p class=\"eyebrow\">P78</p>
        <h2>Certified Continuous P75 Model Separation</h2>
        <p>The figure shows the exact-rational branch-and-bound bridge between P77's statistical rejection theorem and the continuous P75 latent family. Boxwise multi-affine enclosures give the lower side of the model-distance bracket; explicit model points give the upper side.</p>
        <a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_78_certified_continuous_model_separation.md\">Open the P78 proof</a>
      </div>
    </section>"""
    p79 = """

    <section class=\"figure-card\">
      <img src=\"https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p79_joint_statistical_computational_power.svg\" alt=\"P79 joint statistical-computational power\" />
      <div>
        <p class=\"eyebrow\">P79</p>
        <h2>Joint Statistical-Computational Power</h2>
        <p>The figure shows the P77-P78 decision bracket, the separate alpha and beta concentration budgets, and the certified optimization gap. The sufficient power condition is prospective and does not convert non-rejection into model acceptance.</p>
        <a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_79_joint_statistical_computational_power.md\">Open the P79 proof</a>
      </div>
    </section>"""
    text = replace_once(text, p78, p78 + p79, "visual atlas P79")
    write(path, text)


def main() -> None:
    patch_readme()
    patch_changelog()
    patch_detailed_record()
    patch_equation_map()
    patch_roadmap()
    patch_navigation()
    patch_website_index()
    patch_research_map()
    patch_visual_atlas()
    print("P79 publication patch: PASS")


if __name__ == "__main__":
    main()
