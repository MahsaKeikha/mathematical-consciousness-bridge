"""Synchronize derived figure publication surfaces from ``docs/figures``.

The canonical figure archive lives under ``docs/figures``. This command derives
only the GitHub figure gateway, the byte exact current frontier mirror, and the
machine readable SHA 256 manifest. Public website HTML is intentionally not
rewritten here. Website structure is owned by the reader experience layer and is
validated separately by ``scripts/prepare_website.py``.
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
GATEWAY_CURRENT_FIGURE = GATEWAY / "current_frontier.svg"
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

    current_figure = _one_match(f"p{frontier}_*.svg", root=DOC_FIGURES)
    payload = {
        "schema_version": 1,
        "canonical_root": "docs/figures",
        "current_frontier": f"P{frontier}",
        "current_frontier_figure": current_figure.relative_to(ROOT).as_posix(),
        "figure_count": len(records),
        "hash_algorithm": "sha256",
        "figures": records,
    }
    return json.dumps(payload, indent=2) + "\n"


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
                "provenance": (
                    provenance.relative_to(ROOT).as_posix()
                    if provenance.is_file()
                    else ""
                ),
            }
        )
    return records


def _gateway_readme(frontier: int) -> str:
    current_figure = _one_match(f"p{frontier}_*.svg", root=DOC_FIGURES)
    current_prop = _one_match(f"proposition_{frontier}_*.md", root=ROOT / "docs")
    return f"""# Visual research gateway

This directory is the GitHub facing entry point for the visual record. The
canonical SVG archive lives in [`docs/figures/`](../docs/figures/).

## Current theorem frontier: P{frontier}

![P{frontier} current theorem frontier](../{current_figure.relative_to(ROOT).as_posix()})

Canonical figure: [`{current_figure.name}`](../{current_figure.relative_to(ROOT).as_posix()})  
Theorem: [`{current_prop.name}`](../{current_prop.relative_to(ROOT).as_posix()})  
Equation provenance: [`p{frontier}_equation_provenance.md`](../docs/p{frontier}_equation_provenance.md)

For the full P71 to P{frontier} progression, open
[`CURRENT_FRONTIER.md`](CURRENT_FRONTIER.md).

## Complete reproducible figure record

[`manifest.json`](manifest.json) is generated from every SVG under
`docs/figures/`. Each record stores its path, SHA 256 digest, byte size,
category, SVG title, and description length.

The curated reader index is [`docs/figure_catalog.md`](../docs/figure_catalog.md)
and the browser atlas is [`website/visual-atlas.html`](../website/visual-atlas.html).

## Scientific boundary

A figure is not evidence about consciousness merely because it is visual. Its
scientific status comes from the associated theorem, assumptions, data
provenance, tests, and declared evidence class.
"""


def _frontier_page(frontier: int) -> str:
    records = _frontier_records(71, frontier)
    current = records[-1]
    lines = [
        f"# Current visual frontier: P71 to P{frontier}",
        "",
        "This page is generated from the canonical proposition and figure tree.",
        "",
        f"## Current theorem frontier: P{frontier}",
        "",
        f"![P{frontier} current theorem frontier](../{current['figure']})",
        "",
        f"[Read Proposition {frontier}](../{current['proposition']})",
        "",
        f"[Open P{frontier} equation provenance](../docs/p{frontier}_equation_provenance.md)",
        "",
        f"## P71 to P{frontier} canonical theorem figure index",
        "",
        "| Proposition | Canonical figure | Proof | Provenance |",
        "| --- | --- | --- | --- |",
    ]
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
            "## Current scientific boundary",
            "",
            "P87 is a conditional model separation result for the declared P75 target measurement family. It does not identify a latent state with consciousness, prove that consciousness is nonphysical, or complete the physical to experiential bridge. The final bridge remains open.",
            "",
        ]
    )
    return "\n".join(lines)


def _docs_figure_readme(frontier: int) -> str:
    current = _one_match(f"p{frontier}_*.svg", root=DOC_FIGURES)
    return f"""# Figure provenance and regeneration

`docs/figures/` is the canonical visual archive for the Mathematical
Consciousness Bridge research program.

## Current frontier: P{frontier}

![P{frontier} current theorem frontier]({current.name})

Canonical current frontier figure: `{current.name}`

## Reproduce and validate

```bash
python scripts/generate_all_figures.py
python scripts/sync_figure_publication.py --check
```

Generated computational atlases live under `quantitative/` and `quantum/`.
Source authored theorem and architecture SVGs live directly in this directory.
The public Visual Atlas intentionally curates only a small subset of the full
record.

## Scientific boundary

Successful regeneration proves that the declared visual pipeline reproduced.
It does not turn a theorem diagram, synthetic benchmark, or model calculation
into empirical evidence about consciousness.
"""


def _expected_outputs() -> dict[Path, str]:
    frontier = _current_frontier()
    if frontier != 87:
        raise RuntimeError(f"P87 synchronizer expected frontier 87, found {frontier}")
    current_figure = _one_match(f"p{frontier}_*.svg", root=DOC_FIGURES)
    return {
        GATEWAY_CURRENT_FIGURE: current_figure.read_text(encoding="utf-8"),
        GATEWAY / "README.md": _gateway_readme(frontier),
        GATEWAY / "CURRENT_FRONTIER.md": _frontier_page(frontier),
        GATEWAY / "manifest.json": _figure_manifest(frontier),
        DOC_FIGURES / "README.md": _docs_figure_readme(frontier),
    }


def synchronize(*, check: bool) -> None:
    drift: list[str] = []
    for path, expected in _expected_outputs().items():
        current = path.read_text(encoding="utf-8") if path.is_file() else None
        if current == expected:
            continue
        relative = path.relative_to(ROOT).as_posix()
        if check:
            drift.append(relative)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(expected, encoding="utf-8")
            print(f"[figure-sync] updated {relative}")

    if drift:
        raise RuntimeError(
            "figure publication surfaces are out of sync: " + ", ".join(drift)
        )
    if check:
        print("[figure-sync] publication surfaces are synchronized")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Synchronize derived GitHub figure publication surfaces."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail on drift instead of rewriting synchronized publication files",
    )
    args = parser.parse_args()
    synchronize(check=args.check)


if __name__ == "__main__":
    main()
