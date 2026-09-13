"""Synchronize public figure surfaces with the canonical ``docs/figures`` tree.

There is one canonical SVG archive in this repository: ``docs/figures``.  This
command derives the GitHub-facing ``figures/`` gateway, its SHA-256 manifest,
the current-frontier documentation, and the placement of the current theorem
figure on the Visual Atlas.  CI can therefore detect figure-publication drift
instead of relying on folder timestamps or manual inspection.

Run from the repository root::

    python scripts/sync_figure_publication.py

Use ``--check`` in CI to fail on drift without rewriting files.
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
VISUAL_ATLAS = ROOT / "website" / "visual-atlas.html"
VERIFIER = ROOT / "scripts" / "verify_repository.py"

FRONTIER_RE = re.compile(r'^CURRENT_FRONTIER = "P(?P<number>\d+)"$', re.MULTILINE)
RAW_FIGURE_PREFIX = (
    "https://raw.githubusercontent.com/MahsaKeikha/"
    "mathematical-consciousness-bridge/main/docs/figures/"
)
BLOB_PREFIX = (
    "https://github.com/MahsaKeikha/"
    "mathematical-consciousness-bridge/blob/main/"
)


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
                "provenance": (
                    provenance.relative_to(ROOT).as_posix()
                    if provenance.is_file()
                    else ""
                ),
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


def _gateway_readme(frontier: int) -> str:
    current_figure = _one_match(f"p{frontier}_*.svg", root=DOC_FIGURES)
    current_prop = _one_match(f"proposition_{frontier}_*.md", root=ROOT / "docs")
    return f"""# Visual research gateway

This top-level `figures/` directory is the GitHub-facing entry point for the
visual record of the Mathematical Consciousness Bridge project. The canonical
SVG archive lives in [`docs/figures/`](../docs/figures/); this gateway is derived
from that archive by code so it cannot silently remain on an older proposition.

## Current theorem frontier: P{frontier}

![P{frontier} current theorem frontier](../{current_figure.relative_to(ROOT).as_posix()})

Canonical figure: [`{current_figure.name}`](../{current_figure.relative_to(ROOT).as_posix()})
Theorem: [`{current_prop.name}`](../{current_prop.relative_to(ROOT).as_posix()})
Equation provenance: [`p{frontier}_equation_provenance.md`](../docs/p{frontier}_equation_provenance.md)

For the full P71-P{frontier} visual progression, open
[`CURRENT_FRONTIER.md`](CURRENT_FRONTIER.md).

## Complete reproducible figure record

[`manifest.json`](manifest.json) is generated from **every SVG under
`docs/figures/`**. Each record contains its canonical path, SHA-256 digest, byte
size, category, SVG title, and description length. This makes figure drift
machine-auditable rather than relying on folder timestamps or manual inspection.

The curated human-readable index remains
[`docs/figure_catalog.md`](../docs/figure_catalog.md), and the browser-facing
atlas is [`website/visual-atlas.html`](../website/visual-atlas.html).

## Reproduce and validate

```bash
python scripts/generate_all_figures.py
python scripts/sync_figure_publication.py --check
python scripts/verify_repository.py
```

`generate_all_figures.py` regenerates the computational atlases and validates
the canonical SVG tree. The publication synchronizer keeps this gateway, its
manifest, and the Visual Atlas current-frontier ordering synchronized.

## Scientific boundary

Generated atlases, theorem diagrams, and architecture illustrations have
different evidential meanings. A figure is not empirical consciousness evidence
merely because it is visual. Its scientific status comes from the associated
theorem, assumptions, data provenance, tests, and declared evidence class.

The legacy file `p30_p37_operational_scale_map.svg` is retained for continuity;
new theorem figures are maintained canonically under `docs/figures/`.
"""


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
    if frontier == 86:
        lines.extend(
            [
                "### Exact P86 hierarchy witness",
                "",
                "The current exact rational witness preserves the complete P85 certificate at zero while the minimally weighted four-event family is strictly positive:",
                "",
                "```text",
                "L85 = 0 < L86 = 1/192",
                "10,560 standard P86 functionals",
                "primitive coefficient magnitudes {1,1,1,2}",
                "```",
                "",
                "This is a conditional model-separation result inside the declared P75 family. It is not an identification of a latent state with conscious experience.",
                "",
            ]
        )

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
            f"[equations](../{record['provenance']})" if record["provenance"] else "—"
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

The canonical generators are `scripts/generate_quantitative_atlas.py` and
`scripts/generate_quantum_foundations_atlas.py`. Their JSON manifests are
validated against the generated SVG sets.

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

The `.github/workflows/figures.yml` workflow regenerates the computational
atlases, validates byte-identical reproducibility, checks figure-publication
synchronization, runs repository verification, and uploads generated figure
artifacts.

For the curated reader-facing index, see [`docs/figure_catalog.md`](../figure_catalog.md).
For complete setup instructions, see [`docs/reproducibility.md`](../reproducibility.md).

## Scientific boundary

A successful figure workflow proves that the declared generation and validation
path reproduced successfully. It does not turn a theorem illustration, synthetic
benchmark, or model calculation into empirical evidence about consciousness.
"""


def _p86_visual_section() -> str:
    return f'''<section id="p86-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head">
    <p class="eyebrow">Current theorem frontier · P86</p>
    <h2>Minimally weighted four-event shared-parameter parity certificate</h2>
    <p>P86 is the current exact continuous-model frontier. Its 10,560-function audit strictly separates an exact rational witness that leaves the complete P85 certificate at zero.</p>
  </div>
  <div class="theorem-figure-shell">
    <a href="{BLOB_PREFIX}docs/figures/p86_exact_minimally_weighted_quad_projection_parity.svg" aria-label="Open the full P86 theorem figure">
      <img loading="eager" decoding="async" src="{RAW_FIGURE_PREFIX}p86_exact_minimally_weighted_quad_projection_parity.svg" alt="P86 minimally weighted four-event parity certificate showing L85 equals zero and L86 equals one over 192" />
    </a>
  </div>
  <div class="frontier-summary-grid">
    <article class="frontier-summary-card"><h3>Exact family</h3><p>Four distinct canonical parity events with primitive coefficient magnitudes {{1,1,1,2}} yield 10,560 sign-normalized functionals.</p></article>
    <article class="frontier-summary-card"><h3>Strict hierarchy</h3><p>The exact witness has <strong>L85 = 0 &lt; L86 = 1/192</strong>.</p></article>
    <article class="frontier-summary-card"><h3>Reproducible record</h3><p>The theorem, equation provenance, implementation, exhaustive regression suite, SVG, and SHA-256 figure manifest are all source controlled.</p></article>
  </div>
  <div class="boundary"><p><strong>Scientific boundary:</strong> P86 is a conditional exact model-separation theorem for the declared P75 family. It does not identify consciousness, establish nonphysicality, or close the physical-to-experiential bridge.</p></div>
  <p><a href="{BLOB_PREFIX}docs/proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md">Open the P86 theorem</a> · <a href="{BLOB_PREFIX}docs/p86_equation_provenance.md">Equation provenance</a> · <a href="{BLOB_PREFIX}src/consciousness_bridge/weighted_quad_projection_parity_functional_separation.py">Implementation</a> · <a href="{BLOB_PREFIX}tests/test_weighted_quad_projection_parity_functional_separation.py">Exact tests</a></p>
</section>'''


def _normalize_visual_atlas(text: str) -> str:
    pattern = re.compile(r'<section id="p86-frontier".*?</section>', re.DOTALL)
    text, count = pattern.subn("", text, count=1)
    if count != 1:
        raise RuntimeError(f"expected exactly one P86 Visual Atlas section, found {count}")

    marker = "<!-- current-frontier-visual: P86 -->"
    text = re.sub(r"\s*" + re.escape(marker) + r"\s*", "", text)
    boundary = re.search(r'<section class="boundary">.*?</section>', text, re.DOTALL)
    if boundary is None:
        raise RuntimeError("could not locate Visual Atlas reading-boundary section")

    prefix = text[: boundary.end()].rstrip()
    suffix = text[boundary.end() :].lstrip()
    insertion = "\n\n" + marker + "\n" + _p86_visual_section() + "\n\n"
    result = prefix + insertion + suffix
    had_final_newline = result.endswith("\n")
    result = "\n".join(line.rstrip() for line in result.splitlines())
    return result + ("\n" if had_final_newline else "")


def _expected_outputs() -> dict[Path, str]:
    frontier = _current_frontier()
    visual_source = VISUAL_ATLAS.read_text(encoding="utf-8")
    return {
        GATEWAY / "README.md": _gateway_readme(frontier),
        GATEWAY / "CURRENT_FRONTIER.md": _frontier_page(frontier),
        GATEWAY / "manifest.json": _figure_manifest(frontier),
        DOC_FIGURES / "README.md": _docs_figure_readme(frontier),
        VISUAL_ATLAS: _normalize_visual_atlas(visual_source),
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
        description="Synchronize GitHub and website figure publication surfaces."
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
