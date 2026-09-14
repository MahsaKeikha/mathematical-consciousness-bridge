"""Synchronize public figure surfaces with the canonical ``docs/figures`` tree.

The canonical SVG archive lives in ``docs/figures``. This command derives the
GitHub-facing figure gateway, SHA-256 manifest, current-frontier documentation,
and stable current-frontier SVG from the repository verifier's declared
frontier. Reader-facing website promotion is delegated to the matching P88
publication script so one frontier declaration drives every public surface.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC_FIGURES = ROOT / "docs" / "figures"
GATEWAY = ROOT / "figures"
HOME = ROOT / "website" / "index.html"
VISUAL_ATLAS = ROOT / "website" / "visual-atlas.html"
VERIFIER = ROOT / "scripts" / "verify_repository.py"
PROMOTER = ROOT / "scripts" / "promote_p88_public_frontier.py"
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
                "provenance": provenance.relative_to(ROOT).as_posix() if provenance.is_file() else "",
            }
        )
    return records


def _svg_metadata(path: Path) -> tuple[str, str]:
    root = ET.parse(path).getroot()
    namespace = {"svg": "http://www.w3.org/2000/svg"}
    title = root.find("svg:title", namespace)
    description = root.find("svg:desc", namespace)
    title_text = "" if title is None or title.text is None else " ".join(title.text.split())
    description_text = "" if description is None or description.text is None else " ".join(description.text.split())
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


def _frontier_page(frontier: int) -> str:
    records = _frontier_records(71, frontier)
    current = records[-1]
    lines = [
        f"# Current visual frontier: P71-P{frontier}", "",
        "This page is generated from the canonical proposition and figure tree.",
        "It is the compact GitHub-facing visual route through the current target-side branch.", "",
        f"## Current theorem frontier: P{frontier}", "",
        f"![P{frontier} current theorem frontier](../{current['figure']})", "",
        f"[Read Proposition {frontier}](../{current['proposition']})", "",
        f"[Open P{frontier} equation provenance](../docs/p{frontier}_equation_provenance.md)", "",
    ]
    if frontier == 88:
        lines.extend([
            "### Exact P88 hierarchy witness", "",
            "P88 enlarges the complete primitive four-event coefficient box to nonzero integer coefficients satisfying `|c_i| <= 3` and strictly strengthens the complete P87 certificate on the same exact rational witness:", "",
            "```text",
            "L85 = 0 < L86 = 1/192 < L87 = 1/96 < L88 = 1/64",
            "632 primitive sign-normalized coefficient patterns per four-event subset",
            "208,560 standard P88 functionals",
            "```", "",
            "The strict P88 functional uses coefficients `(1, -1, -3, 2)`, has empirical value `-11/8`, exact P75 interval `[-1, 2]`, mismatch `3/8`, and centered transfer norm `24`.", "",
            "This is a conditional model-separation result inside the declared P75 family. It is not an identification of a latent state with conscious experience.", "",
        ])
    lines.extend([
        f"## P71-P{frontier} canonical theorem-figure index", "",
        "| Proposition | Canonical figure | Proof | Provenance |",
        "| --- | --- | --- | --- |",
    ])
    for record in records:
        provenance = f"[equations](../{record['provenance']})" if record["provenance"] else "N/A"
        lines.append(
            f"| P{record['number']} | [figure](../{record['figure']}) | "
            f"[proof](../{record['proposition']}) | {provenance} |"
        )
    lines.extend([
        "", "## Reproduce the visual record", "", "```bash",
        "python scripts/generate_all_figures.py",
        "python scripts/sync_figure_publication.py --check",
        "python scripts/verify_repository.py", "```", "",
        "The complete machine-readable SHA-256 inventory is in [`manifest.json`](manifest.json).", "",
        "## Interpretation boundary", "",
        f"P71-P{frontier} strengthens the methodology for testing a declared physical-to-target model. It does not derive consciousness from physics, prove nonphysicality, or close the physical-to-experiential bridge.", "",
    ])
    return "\n".join(lines)


def _docs_figure_readme(frontier: int) -> str:
    current = _one_match(f"p{frontier}_*.svg", root=DOC_FIGURES)
    recent = _frontier_records(max(71, frontier - 3), frontier)
    recent_lines = "\n".join(f"- `{Path(record['figure']).name}`" for record in recent)
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
    if frontier != 88:
        return
    home = HOME.read_text(encoding="utf-8")
    atlas = VISUAL_ATLAS.read_text(encoding="utf-8")
    required_home = (
        "Explore all 88 results",
        "Research I · Physical-system identification",
        "<strong>58</strong><span>proposition-level statements</span>",
        'id="research-i-overview"',
        "physics_pipeline.svg",
        "Research II · Bridge sufficiency and falsification",
        "<strong>88</strong><span>proposition-level results</span>",
        "P88 current theorem frontier · v0.82.0",
        'id="p88-frontier"',
        "Current theorem frontier · P88",
        "Research III · Consciousness measurement science",
        "<strong>34</strong><span>tests in each CI job</span>",
        'id="research-iii-overview"',
        "measurement_architecture.svg",
        "Two implemented fusion regimes",
        "Open</strong><span>physical-to-experiential bridge",
    )
    required_atlas = (
        'id="p88-frontier"',
        "Current theorem frontier · P88",
        "Previous theorem frontier · P87",
    )
    missing_home = [marker for marker in required_home if marker not in home]
    missing_atlas = [marker for marker in required_atlas if marker not in atlas]
    if missing_home:
        raise RuntimeError(
            f"homepage is not synchronized to P88 and the three-program dashboard: {missing_home}"
        )
    if missing_atlas:
        raise RuntimeError(f"Visual Atlas is not synchronized to P88: {missing_atlas}")
    research_i = home.index('id="research-i-overview"')
    p88_home = home.index('id="p88-frontier"')
    research_iii = home.index('id="research-iii-overview"')
    if home.index('class="research-dashboard"') > research_i:
        raise RuntimeError("homepage must orient readers to the full research program before stage details")
    if not (research_i < p88_home < research_iii):
        raise RuntimeError("homepage must balance Research I, Research II/P88, and Research III in stage order")
    for historical_id in ('id="p87-frontier"', 'id="p86-frontier"', 'id="p85-frontier"'):
        if historical_id in home:
            raise RuntimeError("historical Research II frontiers must remain off the Overview")
    if atlas.index('id="p88-frontier"') > atlas.index('id="p87-frontier"'):
        raise RuntimeError("Visual Atlas does not lead with P88")


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
    if frontier == 88:
        subprocess.run([sys.executable, str(PROMOTER)], cwd=ROOT, check=True)
    _check_reader_surfaces(frontier)
    print(f"[figures] synchronized complete visual publication record to P{frontier}")


if __name__ == "__main__":
    main()
