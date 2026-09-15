"""Synchronize public figure surfaces with the canonical docs/figures tree.

The synchronizer is frontier-generic. It reads the repository verifier's
CURRENT_FRONTIER declaration, derives the complete visual gateway from the
canonical SVG archive, and validates the balanced Research I, II, III reader
surfaces without running an older frontier promoter.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC_FIGURES = ROOT / "docs" / "figures"
GATEWAY = ROOT / "figures"
HOME = ROOT / "website" / "index.html"
VISUAL_ATLAS = ROOT / "website" / "visual-atlas.html"
VERIFIER = ROOT / "scripts" / "verify_repository.py"
FRONTIER_RE = re.compile(r'^CURRENT_FRONTIER = "P(?P<number>\d+)"$', re.MULTILINE)


def _current_frontier() -> int:
    match = FRONTIER_RE.search(VERIFIER.read_text(encoding="utf-8"))
    if match is None:
        raise RuntimeError("could not determine CURRENT_FRONTIER from verifier")
    return int(match.group("number"))


def _one_match(pattern: str, *, root: Path) -> Path:
    matches = sorted(root.glob(pattern))
    if len(matches) != 1:
        relative = root.relative_to(ROOT)
        raise RuntimeError(
            f"expected exactly one {relative}/{pattern} match, found "
            f"{[path.name for path in matches]}"
        )
    return matches[0]


def _frontier_records(start: int, stop: int) -> list[dict[str, str | int]]:
    records: list[dict[str, str | int]] = []
    for number in range(start, stop + 1):
        figure = _one_match(f"p{number}_*.svg", root=DOC_FIGURES)
        proposition = _one_match(f"proposition_{number}_*.md", root=ROOT / "docs")
        provenance = ROOT / "docs" / f"p{number}_equation_provenance.md"
        records.append(
            {
                "number": number,
                "figure": figure.relative_to(ROOT).as_posix(),
                "proposition": proposition.relative_to(ROOT).as_posix(),
                "provenance": provenance.relative_to(ROOT).as_posix()
                if provenance.is_file()
                else "",
            }
        )
    return records


def _svg_metadata(path: Path) -> tuple[str, str]:
    root = ET.parse(path).getroot()
    namespace = {"svg": "http://www.w3.org/2000/svg"}
    title = root.find("svg:title", namespace)
    description = root.find("svg:desc", namespace)
    title_text = "" if title is None or title.text is None else " ".join(title.text.split())
    description_text = (
        ""
        if description is None or description.text is None
        else " ".join(description.text.split())
    )
    return title_text, description_text


def _figure_manifest(frontier: int) -> str:
    records: list[dict[str, object]] = []
    for path in sorted(DOC_FIGURES.rglob("*.svg")):
        raw = path.read_bytes()
        title, description = _svg_metadata(path)
        relative = path.relative_to(ROOT).as_posix()
        if "/quantitative/" in relative:
            category = "quantitative"
        elif "/quantum/" in relative:
            category = "quantum"
        else:
            category = "theorem-or-architecture"
        records.append(
            {
                "path": relative,
                "sha256": hashlib.sha256(raw).hexdigest(),
                "bytes": len(raw),
                "category": category,
                "title": title,
                "description_chars": len(description),
            }
        )
    current = _one_match(f"p{frontier}_*.svg", root=DOC_FIGURES)
    return json.dumps(
        {
            "schema_version": 1,
            "canonical_root": "docs/figures",
            "current_frontier": f"P{frontier}",
            "current_frontier_figure": current.relative_to(ROOT).as_posix(),
            "figure_count": len(records),
            "hash_algorithm": "sha256",
            "figures": records,
        },
        indent=2,
    ) + "\n"


def _gateway_readme(frontier: int) -> str:
    figure = _one_match(f"p{frontier}_*.svg", root=DOC_FIGURES)
    proposition = _one_match(f"proposition_{frontier}_*.md", root=ROOT / "docs")
    return f"""# Visual research gateway

This top-level `figures/` directory is the GitHub-facing entry point for the
visual record of the Mathematical Consciousness Bridge project. The canonical
SVG archive lives in [`docs/figures/`](../docs/figures/); this gateway is derived
from that archive by code so it cannot silently remain on an older proposition.

## Current theorem frontier: P{frontier}

![P{frontier} current theorem frontier](../{figure.relative_to(ROOT).as_posix()})

Canonical figure: [`{figure.name}`](../{figure.relative_to(ROOT).as_posix()})
Theorem: [`{proposition.name}`](../{proposition.relative_to(ROOT).as_posix()})
Equation provenance: [`p{frontier}_equation_provenance.md`](../docs/p{frontier}_equation_provenance.md)

For the full P71-P{frontier} visual progression, open
[`CURRENT_FRONTIER.md`](CURRENT_FRONTIER.md).

## Complete reproducible figure record

[`manifest.json`](manifest.json) is generated from **every SVG under
`docs/figures/`**. Each record contains its canonical path, SHA-256 digest, byte
size, category, SVG title, and description length.

The curated human-readable index remains
[`docs/figure_catalog.md`](../docs/figure_catalog.md), and the browser-facing
atlas is [`website/visual-atlas.html`](../website/visual-atlas.html).

## Reproduce and validate

```bash
python scripts/generate_all_figures.py
python scripts/sync_figure_publication.py --check
python scripts/verify_repository.py
```

## Scientific boundary

Generated atlases, theorem diagrams, and architecture illustrations have
different evidential meanings. A figure is not empirical consciousness evidence
merely because it is visual. Its scientific status comes from the associated
theorem, assumptions, data provenance, tests, and declared evidence class.
"""


def _frontier_summary(frontier: int) -> list[str]:
    if frontier == 89:
        return [
            "### Exact P89 complete-linear witness",
            "",
            "P89 closes every real linear functional of the eleven canonical parity coordinates on the declared strict box.",
            "",
            "```text",
            "L88 = 1/64 < L89 = 5/168",
            "```",
            "",
        ]
    if frontier == 90:
        return [
            "### Exact P90 nonlinear rank-one witness",
            "",
            "P90 moves beyond the complete P89 linear envelope. On the strict box, prevalence is fixed at zero, so the selected two-by-two product-law slice must satisfy ad = bc. Matching exact rational lower and upper certificates prove:",
            "",
            "```text",
            "L89 = 5/168 < L90 = 5/72",
            "L90 / L89 = 7/3",
            "empirical determinant residual = 5/192",
            "```",
            "",
            "The theorem is exact only for the declared strict single-component P75 box. It does not identify consciousness, establish nonphysicality, or close the physical-to-experiential bridge.",
            "",
        ]
    if frontier == 91:
        return [
            "### Exact P91 mixed-prevalence rank-two witness",
            "",
            "P91 removes the extreme-prevalence restriction. The full two-component P75 family obeys a rank-at-most-two bipartite flattening constraint.",
            "",
            "```text",
            "empirical selected determinant = 1/512",
            "closed radius 1/42: minimum determinant = 23/677376 > 0",
            "explicit mixed P75 point: distance = 1/24",
            "1/42 < d_inf(P_emp, M_75) <= 1/24",
            "```",
            "",
            "The upper endpoint is not claimed to be the exact global optimum. P91 does not identify consciousness or close the physical-to-experiential bridge.",
            "",
        ]
    if frontier == 92:
        return [
            "### Exact P92 full-cube mixed-prevalence distance",
            "",
            "P92 closes the P91 bracket through a nonlinear three-minor sign-coherence invariant on the X1=1 subtensor.",
            "",
            "```text",
            "empirical determinants = (-1/48, 1/64, 5/192)",
            "sign-stability radii = (1/24, 3/56, 5/72)",
            "universal P75 determinant product >= 0",
            "d_inf(P_emp, M_75) = 1/24",
            "```",
            "",
            "P92 is a conditional model-separation theorem and does not identify consciousness or close the physical-to-experiential bridge.",
            "",
        ]
    if frontier == 93:
        return [
            "### Exact P93 localized finite-sample sign-coherence rejection",
            "",
            "P93 carries the P92 nonlinear sign-coherence obstruction into finite IID data using only seven selected observable cells.",
            "",
            "```text",
            "empirical determinants = (-1/48, 1/64, 5/192)",
            "empirical determinant signs = (-,+,+)",
            "d_inf(P_emp, M_75) = 1/24",
            "sign-stability radii = (1/24, 3/56, 5/72)",
            "95% mathematical crossing = 1622 / 1623",
            "first exact 24-count replication that clears = 1632",
            "generic P77 fixed-margin comparison = 7444",
            "```",
            "",
            "The P77 comparison is a different guarantee. P93 is localized to the observed P92 sign witness, does not claim universal or minimax sample complexity, and does not identify consciousness.",
            "",
        ]
    if frontier == 94:
        return [
            "### Exact P94 finite-range dependent sign-coherence rejection",
            "",
            "P94 preserves the P92/P93 nonlinear rejection witness under a declared finite-range dependent stream with one common marginal law.",
            "",
            "```text",
            "eps_m^2 = (m+1) log(14/alpha) / (2n)",
            "m=0: crossing 1623; exact replication 1632",
            "m=1: crossing 3246; exact replication 3264",
            "m=2: crossing 4869; exact replication 4872",
            "pooled-drift no-go determinants = (-65/65536, 11/65536, 3/65536)",
            "pooled determinant product = -2145/281474976710656",
            "```",
            "",
            "P94 is conditional on the declared dependence range and common marginal law. It does not establish arbitrary drift robustness or identify consciousness.",
            "",
        ]
    if frontier == 95:
        return [
            "### Exact P95 drift-aware stratified sign-coherence rejection",
            "",
            "P95 responds to the P94 temporal-pooling no-go by testing predeclared regimes separately and controlling the complete family with one explicit error budget.",
            "",
            "```text",
            "local radius: eps_b^2 = (m_b+1) log(14/alpha_b) / (2 n_b)",
            "familywise condition: sum_b alpha_b <= alpha",
            "joint null: P_b belongs to M_75 for every declared regime b",
            "B=2, m=1, 95% familywise crossing = 3645 per regime",
            "first exact denominator-24 replication = 3648 per regime",
            "```",
            "",
            "P95 permits arbitrary marginal changes between predeclared regimes and requires only local common-marginal finite-range assumptions. It does not validate data-dependent segmentation, unrestricted gradual drift, model acceptance, or any consciousness ontology.",
            "",
        ]
    if frontier == 96:
        return [
            "### Exact P96 selection-valid holdout stratification",
            "",
            "P96 closes one precise adaptive-regime gap left open by P95: pilot information may choose the regime plan, but the plan is frozen before an independent certification sample is inspected.",
            "",
            "```text",
            "pilot selects: B, regime definitions, m_b, alpha_b",
            "holdout requirement: C independent of S",
            "familywise condition: sum_b alpha_b <= alpha",
            "extra alpha penalty for pilot-selection complexity = 0",
            "B=2, m=1, 95% holdout crossing = 3645 per regime",
            "first exact denominator-24 holdout replication = 3648 per regime",
            "```",
            "",
            "The zero extra selection penalty is conditional on a genuinely independent holdout design and a plan frozen before holdout evaluation. Same-data redesign, naive splitting of a dependent stream, within-regime drift, model acceptance, consciousness identification, and bridge completion are not established.",
            "",
        ]
    if frontier == 97:
        return [
            "### Exact P97 simultaneous finite candidate-family selection",
            "",
            "P97 complements P96 by permitting same-data post-inspection selection within a finite candidate family fixed before certification statistics are inspected.",
            "",
            "```text",
            "candidate budgets: sum_k alpha_k <= alpha",
            "inside candidate k: sum_b alpha_kb <= alpha_k",
            "K=2, B=2, m=1: local alpha = 1/80",
            "95% mathematical crossing = 4045 per regime",
            "first exact denominator-24 replication = 4056 per regime",
            "balanced unique-observation totals = 8090 / 8112",
            "```",
            "",
            "P97 pays for same-data search through multiplicity. The candidate family must be fixed before inspection. New post-inspection candidates, unrestricted within-regime drift, model acceptance, consciousness identification, nonphysicality, and bridge completion are not established.",
            "",
        ]
    if frontier == 98:
        return [
            "### Exact P98 cross-fitted selection-valid certification",
            "",
            "P98 rotates the P96 independent-holdout principle across mutually independent certification blocks while preserving own-fold exclusion from plan selection.",
            "",
            "```text",
            "fold budgets: sum_k beta_k <= alpha",
            "inside fold k: sum_b alpha_kb <= beta_k",
            "K=2 folds, B=2 regimes, m=1: local alpha = 1/80",
            "95% mathematical crossing = 4045 per regime",
            "first exact denominator-24 replication = 4056 per regime",
            "per-fold totals = 8090 / 8112",
            "cross-fitted unique totals = 16180 / 16224",
            "```",
            "",
            "P98 requires genuinely independent certification blocks and no own-fold leakage. The final fold certificates may be dependent; validity is combined by an outer union bound. Dependent-stream pseudo-folds, unbudgeted scheme search, model acceptance, consciousness identification, nonphysicality, and bridge completion are not established.",
            "",
        ]
    if frontier == 99:
        return [
            "### Exact P99 cross-fitted e-value aggregation",
            "",
            "P99 converts selection-valid P96/P98 fold rejection indicators into exact e-values and accumulates distributed evidence without assuming the final fold certificates are independent.",
            "",
            "```text",
            "fold test level tau = 1/25",
            "local regime alpha = 1/50",
            "K=2 folds, B=2 regimes, m=1",
            "95% mathematical crossing = 3774 per regime",
            "first exact denominator-24 replication = 3792 per regime",
            "cross-fitted unique totals = 15096 / 15168",
            "matched P98 crossing = 4045 / 4056 per regime",
            "```",
            "",
            "P99 uses fixed finite calibration and exact convex e-value averaging. It does not uniformly dominate P98 and does not validate own-fold leakage, post-hoc calibration search, dependent-stream pseudo-folds, model acceptance, consciousness identification, nonphysicality, or bridge completion.",
            "",
        ]
    return []


def _frontier_page(frontier: int) -> str:
    records = _frontier_records(71, frontier)
    current = records[-1]
    lines = [
        f"# Current visual frontier: P71-P{frontier}",
        "",
        "This page is generated from the canonical proposition and figure tree.",
        "It is the compact GitHub-facing visual route through the current target-side branch.",
        "",
        f"## Current theorem frontier: P{frontier}",
        "",
        f"![P{frontier} current theorem frontier](../{current['figure']})",
        "",
        f"[Read Proposition {frontier}](../{current['proposition']})",
        "",
        f"[Open P{frontier} equation provenance](../docs/p{frontier}_equation_provenance.md)",
        "",
    ]
    lines.extend(_frontier_summary(frontier))
    lines.extend(
        [
            f"## P71-P{frontier} canonical theorem-figure index",
            "",
            "| Proposition | Canonical figure | Proof | Provenance |",
            "| --- | --- | --- | --- |",
        ]
    )
    for record in records:
        provenance = (
            f"[equations](../{record['provenance']})" if record["provenance"] else "N/A"
        )
        lines.append(
            f"| P{record['number']} | [figure](../{record['figure']}) | "
            f"[proof](../{record['proposition']}) | {provenance} |"
        )
    lines.extend(
        [
            "",
            "## Reproduce the visual record",
            "",
            "```bash",
            "python scripts/generate_all_figures.py",
            "python scripts/sync_figure_publication.py --check",
            "python scripts/verify_repository.py",
            "```",
            "",
            "The complete machine-readable SHA-256 inventory is in [`manifest.json`](manifest.json).",
            "",
            "## Interpretation boundary",
            "",
            f"P71-P{frontier} strengthens the methodology for testing a declared physical-to-target model. It does not derive consciousness from physics, prove nonphysicality, or close the physical-to-experiential bridge.",
            "",
        ]
    )
    return "\n".join(lines)


def _docs_figure_readme(frontier: int) -> str:
    current = _one_match(f"p{frontier}_*.svg", root=DOC_FIGURES)
    recent = _frontier_records(max(71, frontier - 3), frontier)
    recent_lines = "\n".join(
        f"- `{Path(record['figure']).name}`" for record in recent
    )
    return f"""# Figure provenance and regeneration

`docs/figures/` is the canonical visual archive for the Mathematical
Consciousness Bridge research program. The repository distinguishes generated
computational atlases from source-controlled theorem and architecture diagrams
because they have different scientific meanings.

## Generated computational atlases

```text
docs/figures/quantitative/
docs/figures/quantum/
```

Regenerate and validate them with:

```bash
python scripts/generate_all_figures.py
```

## Source-controlled theorem and architecture figures

SVGs stored directly in this directory communicate theorem structure,
assumptions, inequalities, dependencies, or scientific boundaries. They are
validated as SVG documents and enriched with accessible `<title>` and `<desc>`
metadata. They are not reclassified as empirical evidence simply because they
are visual.

## Current frontier: P{frontier}

![P{frontier} current theorem frontier]({current.name})

Canonical current-frontier figure: `{current.name}`

Recent exact frontier figures:

{recent_lines}

The GitHub-facing [`figures/`](../../figures/) gateway and its SHA-256
[`manifest.json`](../../figures/manifest.json) are deterministically synchronized
from this canonical tree by `scripts/sync_figure_publication.py`.

## Validation without regeneration

```bash
python scripts/generate_all_figures.py --validate-only
python scripts/sync_figure_publication.py --check
```

For the curated reader-facing index, see [`docs/figure_catalog.md`](../figure_catalog.md).
For complete setup instructions, see [`docs/reproducibility.md`](../reproducibility.md).

## Scientific boundary

A successful figure workflow proves that the declared generation and validation
path reproduced successfully. It does not turn a theorem illustration, synthetic
benchmark, or model calculation into empirical evidence about consciousness.
"""


def _expected(frontier: int) -> dict[Path, str | bytes]:
    current = _one_match(f"p{frontier}_*.svg", root=DOC_FIGURES)
    return {
        GATEWAY / "manifest.json": _figure_manifest(frontier),
        GATEWAY / "README.md": _gateway_readme(frontier),
        GATEWAY / "CURRENT_FRONTIER.md": _frontier_page(frontier),
        GATEWAY / "current_frontier.svg": current.read_bytes(),
        DOC_FIGURES / "README.md": _docs_figure_readme(frontier),
    }


def _write_expected(expected: dict[Path, str | bytes]) -> None:
    for path, value in expected.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(value, bytes):
            path.write_bytes(value)
        else:
            path.write_text(value, encoding="utf-8")


def _check_expected(expected: dict[Path, str | bytes]) -> None:
    drift: list[str] = []
    for path, value in expected.items():
        if not path.is_file():
            actual: str | bytes | None = None
        elif isinstance(value, bytes):
            actual = path.read_bytes()
        else:
            actual = path.read_text(encoding="utf-8")
        if actual != value:
            drift.append(path.relative_to(ROOT).as_posix())
    if drift:
        raise RuntimeError(f"figure publication drift detected: {drift}")


def _check_reader_surfaces(frontier: int) -> None:
    home = HOME.read_text(encoding="utf-8")
    atlas = VISUAL_ATLAS.read_text(encoding="utf-8")
    plain = (ROOT / "website" / "plain-language.html").read_text(encoding="utf-8")
    start = (ROOT / "website" / "start-here.html").read_text(encoding="utf-8")
    previous = frontier - 1
    required_home = (
        f"Explore all {frontier} results",
        "Research I · Physical-system identification",
        'id="research-i-overview"',
        "physics_pipeline.svg",
        "Research II · Bridge sufficiency and falsification",
        f"P{frontier} current theorem frontier · v0.82.0",
        f'id="p{frontier}-frontier"',
        f"Current theorem frontier · P{frontier}",
        "Research III · Consciousness measurement science",
        'id="research-iii-overview"',
        "measurement_architecture.svg",
        "Open</strong><span>physical-to-experiential bridge",
    )
    required_atlas = (
        f'id="p{frontier}-frontier"',
        f"Current theorem frontier · P{frontier}",
        f"Previous theorem frontier · P{previous}",
    )
    required_plain = (
        '<strong>Research I</strong><span>physical-system identification</span>',
        f'<strong>Research II</strong><span>{frontier} results · current frontier P{frontier}</span>',
        '<strong>Research III</strong><span>measurement science under uncertainty</span>',
        'id="three-stage-progress"',
    )
    required_start = (
        '<strong>Research I</strong><span>physical-system identification</span>',
        f'<strong>Research II</strong><span>{frontier} results · current frontier P{frontier}</span>',
        '<strong>Research III</strong><span>measurement science under uncertainty</span>',
        'id="program-stages"',
        f"The {frontier} Research II propositions by scientific role",
    )
    for label, source, markers in (
        ("homepage", home, required_home),
        ("Visual Atlas", atlas, required_atlas),
        ("Plain Language", plain, required_plain),
        ("Start Here", start, required_start),
    ):
        missing = [marker for marker in markers if marker not in source]
        if missing:
            raise RuntimeError(
                f"{label} is not synchronized to P{frontier} balanced publication state: {missing}"
            )
    research_i = home.index('id="research-i-overview"')
    current_home = home.index(f'id="p{frontier}-frontier"')
    research_iii = home.index('id="research-iii-overview"')
    if home.index('class="research-dashboard"') > research_i:
        raise RuntimeError(
            "homepage must orient readers to the full research program before stage details"
        )
    if not (research_i < current_home < research_iii):
        raise RuntimeError(
            f"homepage must balance Research I, Research II/P{frontier}, and Research III in stage order"
        )
    for number in range(previous, max(70, frontier - 5), -1):
        if f'id="p{number}-frontier"' in home:
            raise RuntimeError("historical Research II frontiers must remain off the Overview")
    if atlas.index(f'id="p{frontier}-frontier"') > atlas.index(
        f'id="p{previous}-frontier"'
    ):
        raise RuntimeError(f"Visual Atlas does not lead with P{frontier}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    frontier = _current_frontier()
    expected = _expected(frontier)
    if args.check:
        _check_expected(expected)
        _check_reader_surfaces(frontier)
        print(f"[figures] publication surfaces are synchronized to P{frontier}")
        return
    _write_expected(expected)
    _check_reader_surfaces(frontier)
    print(f"[figures] synchronized complete visual publication record to P{frontier}")


if __name__ == "__main__":
    main()
