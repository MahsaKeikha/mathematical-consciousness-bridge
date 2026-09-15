"""Repair residual reader and citation contracts during the one-run P94 promotion.

This helper is temporary. It is designed to run after
``promote_p94_public_frontier.py`` has created the formal P94 publication state.
Delete it together with the temporary promotion workflow after the exact P94
head is validated.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_required(text: str, old: str, new: str, *, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one {old!r}, found {count}")
    return text.replace(old, new, 1)


def repair_start_here() -> None:
    path = "START_HERE.md"
    text = read(path)
    replacements = (
        (
            "The public theorem frontier is **P93**. The formal release is **v0.82.0**.",
            "The public theorem frontier is **P94**. The formal release is **v0.82.0**.",
        ),
        (
            "You do not need to read 93 propositions to understand the project.",
            "You do not need to read 94 propositions to understand the project.",
        ),
        (
            "| Read the current frontier result | **[P93](docs/proposition_93_localized_sign_coherence_rejection.md)** |",
            "| Read the current frontier result | **[P94](docs/proposition_94_finite_range_dependent_sign_coherence.md)** |",
        ),
        (
            "### P93 localized finite-sample frontier",
            "### P93 historical IID finite-sample step",
        ),
        (
            "The current Research II frontier is [P93](docs/proposition_93_localized_sign_coherence_rejection.md).",
            "The historical IID finite-sample step is [P93](docs/proposition_93_localized_sign_coherence_rejection.md).",
        ),
    )
    for old, new in replacements:
        text = replace_required(text, old, new, label=path)

    if "### P94 finite-range dependent frontier" not in text:
        text = text.rstrip() + """

### P94 finite-range dependent frontier

The current Research II frontier is [P94](docs/proposition_94_finite_range_dependent_sign_coherence.md). P94 keeps the seven-cell P92/P93 nonlinear rejection witness but relaxes IID sampling to a declared finite-range dependent sequence with one common marginal four-view law. For dependence range `m`, the squared confidence radius is multiplied by `m+1`. At 95 percent confidence, the established witness crosses at 1623, 3246, and 4869 samples for `m=0,1,2` respectively. An exact temporal-pooling counterexample shows why arbitrary marginal drift is outside the theorem. Non-rejection remains inconclusive, and the physical-to-experiential bridge remains open.
"""
    write(path, text)


def repair_citation_markdown() -> None:
    path = "CITATION.md"
    text = read(path)
    replacements = (
        (
            "This is the preferred citation for the research program at the current documented frontier, P93.",
            "This is the preferred citation for the research program at the current documented frontier, P94.",
        ),
        (
            "note         = {Ongoing research program. Current documented theorem frontier: P93.}",
            "note         = {Ongoing research program. Current documented theorem frontier: P94.}",
        ),
        (
            "The current citation metadata identify Version **0.82.0** and theorem frontier **P93**.",
            "The current citation metadata identify Version **0.82.0** and theorem frontier **P94**.",
        ),
        (
            "[Detailed proposition record](docs/detailed_proposition_record.md): P1 through P93 chronological theorem record.",
            "[Detailed proposition record](docs/detailed_proposition_record.md): P1 through P94 chronological theorem record.",
        ),
    )
    for old, new in replacements:
        text = replace_required(text, old, new, label=path)

    pattern = re.compile(
        r"## Current theorem frontier: P94\n.*?(?=\n## Historical mixed-prevalence frontier: P91)",
        flags=re.DOTALL,
    )
    match = pattern.search(text)
    if match is None:
        raise RuntimeError("CITATION.md: promoted P94 current-frontier section missing")
    section = """## Current theorem frontier: P94

The current documented theorem frontier is **P94**. The formal package release remains **Version 0.82.0**. P94 extends the localized P92/P93 sign-coherence rejection witness from IID observations to a declared finite-range dependent sequence with one common marginal four-view law. With dependence range `m`, its seven-cell confidence radius is

\[
\varepsilon^{(m)}_{n,7}(\alpha)
=
\sqrt{\frac{(m+1)\log(14/\alpha)}{2n}}.
\]

At 95 percent confidence, exact rational certification gives mathematical crossings 1623, 3246, and 4869 for `m=0,1,2`, with first exact denominator-24 replications 1632, 3264, and 4872. P94 also includes an exact temporal-pooling no-go construction: two individually valid interior P75 regimes can pool to determinants `(-65/65536, 11/65536, 3/65536)` with negative product. The theorem therefore does not claim robustness to arbitrary marginal drift.

- Proof: [`proposition_94_finite_range_dependent_sign_coherence.md`](docs/proposition_94_finite_range_dependent_sign_coherence.md)
- Equation provenance: [`p94_equation_provenance.md`](docs/p94_equation_provenance.md)
- Implementation: [`finite_range_dependent_sign_coherence.py`](src/consciousness_bridge/finite_range_dependent_sign_coherence.py)
- Exact thresholds: [`finite_range_dependent_sign_coherence_threshold.py`](src/consciousness_bridge/finite_range_dependent_sign_coherence_threshold.py)
- Exact tests: [`test_finite_range_dependent_sign_coherence.py`](tests/test_finite_range_dependent_sign_coherence.py)

P94 remains a conditional finite-sample model-rejection theorem. Non-rejection is inconclusive. It does not identify consciousness, establish nonphysicality, validate an alternative theory, or close the physical-to-experiential bridge.

## Historical IID finite-sample frontier: P93

P93 remains the IID localized seven-cell theorem that P94 extends. At 95 percent confidence, its exact mathematical crossing is 1623 and the first exact denominator-24 replication is 1632. P93 remains scientifically valid under its stated IID assumptions and is preserved as the immediate historical predecessor of P94.
"""
    text = text[: match.start()] + section + text[match.end() :]
    write(path, text)


def repair_citation_bib() -> None:
    path = "CITATION.bib"
    text = read(path)
    text = replace_required(
        text,
        "Current documented theorem frontier: P89.",
        "Current documented theorem frontier: P94.",
        label=path,
    )
    write(path, text)


def repair_glossary() -> None:
    path = "docs/glossary.md"
    text = read(path)
    text = replace_required(
        text,
        "The current public frontier is **P92**.",
        "The current public frontier is **P94**.",
        label=path,
    )
    text = replace_required(
        text,
        "## Current theorem frontier: P93",
        "## Historical IID theorem frontier: P93",
        label=path,
    )
    text = replace_required(
        text,
        "The current documented Research II theorem frontier is **P93**. P92 remains the exact population-distance theorem at `d_inf(P_emp, M75) = 1/24`; P93 adds the localized seven-cell finite-sample rejection handoff. This frontier status does not identify consciousness or close the physical-to-experiential bridge.",
        "P93 is the historical IID finite-sample predecessor of P94. P92 remains the exact population-distance theorem at `d_inf(P_emp, M75) = 1/24`; P93 adds the localized seven-cell IID rejection handoff. P94 then extends that handoff to declared finite-range temporal dependence under one common marginal law. None of these frontier labels identifies consciousness or closes the physical-to-experiential bridge.",
        label=path,
    )
    if text.count("## Current theorem frontier: P94") != 1:
        raise RuntimeError(
            "docs/glossary.md: expected exactly one promoted P94 current-frontier section"
        )
    write(path, text)


def repair_detailed_record() -> None:
    path = "docs/detailed_proposition_record.md"
    text = read(path)
    if text.count("Complete P1 to P93 chronology") < 1:
        raise RuntimeError("detailed proposition record lacks the P93 chronology heading")
    text = text.replace("Complete P1 to P93 chronology", "Complete P1 to P94 chronology")
    text = text.replace(
        "93 disconnected proposition-level results",
        "94 disconnected proposition-level results",
    )
    if "## Proposition 94: Finite-Range Dependent Sign-Coherence Rejection" not in text:
        raise RuntimeError("detailed proposition record lacks the promoted P94 entry")
    write(path, text)


def repair_research_map() -> None:
    path = "docs/research_map.md"
    text = read(path)
    pattern = re.compile(
        r"## Where the current work sits\n.*?(?=\n---\n\n## Choose a trail)",
        flags=re.DOTALL,
    )
    match = pattern.search(text)
    if match is None:
        raise RuntimeError("docs/research_map.md: current-work section missing")
    current = """## Where the current work sits

The public theorem frontier is **P94** and the formal release remains **v0.82.0**.

P94 extends the P93 localized seven-cell rejection theorem from IID observations to a declared finite-range dependent sequence with one common marginal four-view law. The squared finite-sample radius carries the exact factor `m+1` for dependence range `m`, while the P92 determinant geometry is unchanged.

P94 also proves an exact temporal-pooling no-go: two individually valid interior P75 regimes can pool to a law with the negative determinant-product sign pattern used for rejection. Arbitrary marginal drift is therefore a separate problem and is not silently treated as finite-range dependence.

If you want the current result itself, open **[P94](proposition_94_finite_range_dependent_sign_coherence.md)**. For the IID predecessor, open **[P93](proposition_93_localized_sign_coherence_rejection.md)**. For the complete dependency chain, use the **[Theorem Roadmap](theorem_roadmap.md)**.
"""
    text = text[: match.start()] + current + text[match.end() :]

    text = replace_required(
        text,
        "### P93 localized finite-sample sign-coherence rejection",
        "### P93 historical IID finite-sample sign-coherence rejection",
        label=path,
    )
    text = replace_required(
        text,
        "P93 asks whether finite IID data preserve P92's impossible determinant sign pattern strongly enough to reject the complete P75 family. It uses only seven selected cells and exact P79 sampling-radius certification. [Read P93](proposition_93_localized_sign_coherence_rejection.md).",
        "P93 is the historical IID finite-sample handoff from P92. It uses only seven selected cells and exact P79 sampling-radius certification. [Read P93](proposition_93_localized_sign_coherence_rejection.md).",
        label=path,
    )
    if "### P94 finite-range dependent sign-coherence rejection" not in text:
        text = text.rstrip() + """

### P94 finite-range dependent sign-coherence rejection

P94 is the current Research II theorem frontier. It preserves the seven-cell P92/P93 nonlinear witness under a declared finite-range dependent sequence with one common marginal law, using exact rational certification of the dependence-adjusted confidence radius. Its exact pooling counterexample also marks the limit of that extension: arbitrary temporal drift remains outside the theorem. [Read P94](proposition_94_finite_range_dependent_sign_coherence.md).
"""
    write(path, text)


def verify_repair() -> None:
    checks = {
        "START_HERE.md": (
            "The public theorem frontier is **P94**.",
            "### P94 finite-range dependent frontier",
        ),
        "CITATION.md": (
            "current documented frontier, P94.",
            "## Current theorem frontier: P94",
            "## Historical IID finite-sample frontier: P93",
        ),
        "CITATION.bib": ("Current documented theorem frontier: P94.",),
        "docs/glossary.md": (
            "The current public frontier is **P94**.",
            "## Current theorem frontier: P94",
            "## Historical IID theorem frontier: P93",
        ),
        "docs/detailed_proposition_record.md": (
            "Complete P1 to P94 chronology",
            "## Proposition 94: Finite-Range Dependent Sign-Coherence Rejection",
        ),
        "docs/research_map.md": (
            "The public theorem frontier is **P94**",
            "### P94 finite-range dependent sign-coherence rejection",
        ),
    }
    for path, tokens in checks.items():
        text = read(path)
        for token in tokens:
            if token not in text:
                raise RuntimeError(f"{path}: repair verification missing {token!r}")


def main() -> None:
    repair_start_here()
    repair_citation_markdown()
    repair_citation_bib()
    repair_glossary()
    repair_detailed_record()
    repair_research_map()
    verify_repair()
    print("[P94] residual reader and citation contracts repaired")


if __name__ == "__main__":
    main()
