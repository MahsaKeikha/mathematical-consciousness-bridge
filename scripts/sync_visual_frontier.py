"""Synchronize the current theorem-figure frontier across GitHub and website surfaces.

This script keeps the reader-facing ``figures/`` gateway and the website ordering
consistent with the canonical theorem figures under ``docs/figures``.  It does
not invent scientific content: it only publishes the already committed current
frontier and preserves older propositions as historical steps.

Run from the repository root with::

    python scripts/sync_visual_frontier.py

Use ``--check`` in CI to require that the committed publication surfaces are
already byte-for-byte synchronized.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "website" / "index.html"
VISUAL_ATLAS = ROOT / "website" / "visual-atlas.html"
GATEWAY_README = ROOT / "figures" / "README.md"
CURRENT_FRONTIER = ROOT / "figures" / "CURRENT_FRONTIER.md"
MANIFEST = ROOT / "figures" / "frontier_manifest.json"

CURRENT = "P86"
CURRENT_FIGURE = "p86_exact_minimally_weighted_quad_projection_parity.svg"
CURRENT_PROPOSITION = (
    "docs/proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md"
)
CURRENT_PROVENANCE = "docs/p86_equation_provenance.md"
CURRENT_IMPLEMENTATION = (
    "src/consciousness_bridge/minimally_weighted_quad_projection_parity_functional_separation.py"
)
CURRENT_TEST = "tests/test_minimally_weighted_quad_projection_parity_functional_separation.py"

FRONTIER_FIGURES = (
    (71, "p71_target_provenance_noncircularity.svg", "Target provenance and non-circularity"),
    (72, "p72_target_measurement_channel_robustness.svg", "Target-measurement channel robustness"),
    (73, "p73_target_channel_identifiability.svg", "Target-channel identifiability"),
    (74, "p74_finite_sample_target_channel_recovery.svg", "Finite-sample target-channel recovery"),
    (75, "p75_target_model_adequacy_overidentification.svg", "Target-model adequacy and overidentification"),
    (76, "p76_finite_sample_target_model_adequacy.svg", "Finite-sample target-model adequacy"),
    (77, "p77_full_law_model_set_separation.svg", "Full-law model-set separation"),
    (78, "p78_certified_continuous_model_separation.svg", "Certified continuous-family separation"),
    (79, "p79_certified_sampling_radius.svg", "Certified sampling-radius envelope"),
    (80, "p80_simplex_coupled_model_separation.svg", "Simplex-coupled separation"),
    (81, "p81_projection_event_model_separation.svg", "Projection-event separation"),
    (82, "p82_exact_nested_projection_contrast.svg", "Exact nested projection contrast"),
    (83, "p83_exact_projection_parity.svg", "Exact projection parity"),
    (84, "p84_exact_joint_projection_parity_contrast.svg", "Exact joint projection parity"),
    (85, "p85_exact_triple_projection_parity_functional.svg", "Exact three-event shared-parameter parity functional"),
    (86, CURRENT_FIGURE, "Minimally weighted four-event shared-parameter parity functional"),
)


def _extract_section(text: str, section_id: str) -> tuple[int, int, str]:
    marker = f'<section id="{section_id}"'
    start = text.find(marker)
    if start < 0:
        raise RuntimeError(f"missing section {section_id!r}")
    end = text.find("</section>", start)
    if end < 0:
        raise RuntimeError(f"unterminated section {section_id!r}")
    end += len("</section>")
    return start, end, text[start:end]


def _move_section_before(text: str, section_id: str, before_marker: str) -> str:
    start, end, block = _extract_section(text, section_id)
    remainder = text[:start] + text[end:]
    insertion = remainder.find(before_marker)
    if insertion < 0:
        raise RuntimeError(f"missing insertion marker {before_marker!r}")
    return remainder[:insertion] + block + "\n\n" + remainder[insertion:]


def _synchronized_index(text: str) -> str:
    # The current theorem must be the first substantive research figure a reader
    # encounters after the hero, not buried below historical P84/P85 material.
    return _move_section_before(
        text,
        "p86-frontier",
        '    <section id="plain-language">',
    )


def _synchronized_visual_atlas(text: str) -> str:
    # Keep P85 available as the previous frontier while making P86 visually first.
    return _move_section_before(
        text,
        "p86-frontier",
        '<section id="p85-frontier"',
    )


def _gateway_readme() -> str:
    return f"""# Visual research gateway

This top-level `figures/` directory is the reader-facing GitHub entry point for the visual record of the Mathematical Consciousness Bridge project. The canonical SVG archive lives in [`docs/figures/`](../docs/figures/); this gateway is synchronized from code so that it cannot silently lag behind the theorem frontier.

## Current theorem frontier · {CURRENT}

**{CURRENT}: Minimally weighted four-event shared-parameter parity-functional separation**

![{CURRENT} current theorem figure](../docs/figures/{CURRENT_FIGURE})

The strict exact-rational hierarchy witness is

```text
L85 = 0 < L86 = 1/192
```

The standard P86 audit contains **10,560** sign-normalized functionals built from four distinct canonical parity events with primitive coefficient magnitudes `{{1,1,1,2}}` under one shared P75 parameter assignment.

Audit records:

- [P86 theorem](../{CURRENT_PROPOSITION})
- [P86 equation provenance](../{CURRENT_PROVENANCE})
- [P86 implementation](../{CURRENT_IMPLEMENTATION})
- [P86 exact regression tests](../{CURRENT_TEST})
- [Complete canonical figure catalog](../docs/figure_catalog.md)
- [Public visual atlas](../website/visual-atlas.html)

P85 and P84 remain part of the historical dependency chain; they are not presented as the current frontier.

## Reproduce and validate the visual record

From the repository root:

```bash
python scripts/sync_visual_frontier.py --check
python scripts/generate_all_figures.py
python scripts/generate_all_figures.py --validate-only
python -m pytest tests/test_visual_frontier_sync.py tests/test_figure_documentation_integrity.py
python scripts/verify_repository.py
```

Generated computational atlases are recreated by code. Source-authored theorem SVGs are validated as parseable vector documents, checked for substantive accessible metadata, catalogued, and tied to theorem/provenance/test records. The website deployment bundles the exact validated `docs/figures/` tree from the deployed commit.

## Scientific boundary

A theorem diagram or generated visualization is not empirical evidence merely because it is visual. P86 is a conditional rejection certificate for the declared P75 model family. It does not identify a latent state with consciousness and does not solve the physical-to-experiential bridge.
"""


def _current_frontier() -> str:
    rows = [
        f"| P{number} | [{title}](../docs/figures/{filename}) |"
        for number, filename, title in FRONTIER_FIGURES
    ]
    table = "\n".join(rows)
    return f"""# Current visual frontier: P71-P86

This page is the compact GitHub visual index for the target-integrity and exact model-separation branch. It is generated by `scripts/sync_visual_frontier.py` and must remain synchronized with the website and the canonical archive under `docs/figures/`.

## Current frontier · P86

![P86 minimally weighted four-event shared-parameter parity certificate](../docs/figures/{CURRENT_FIGURE})

P86 tests the first non-uniform primitive four-event parity-functional family, with coefficient magnitudes `{{1,1,1,2}}`. The standard family has **10,560** sign-normalized functionals. On the exact strict witness, the complete P85 certificate remains zero while P86 certifies

```text
L85 = 0 < L86 = 1/192.
```

This makes P86 a strict strengthening of the current exact shared-parameter certification hierarchy for the declared P75 family.

## Frontier figure index

| Proposition | Canonical theorem figure |
| --- | --- |
{table}

## Immediate history

- **P84** couples two parity observables under one shared P75 parameter assignment.
- **P85** couples three parity observables with unit-magnitude signed coefficients.
- **P86** moves to four distinct parity observables and the minimal non-uniform primitive weighting `{{1,1,1,2}}`.

P84 and P85 remain scientifically important historical frontiers; they are not labeled current.

## Audit path for P86

- [Theorem](../{CURRENT_PROPOSITION})
- [Equation provenance](../{CURRENT_PROVENANCE})
- [Implementation](../{CURRENT_IMPLEMENTATION})
- [Regression tests](../{CURRENT_TEST})
- [Figure catalog](../docs/figure_catalog.md)
- [Website visual atlas](../website/visual-atlas.html)

## Reproduce and validate

```bash
python scripts/sync_visual_frontier.py --check
python scripts/generate_all_figures.py
python scripts/generate_all_figures.py --validate-only
python scripts/verify_repository.py
```

The project does not claim that P71-P86 derives consciousness from physics. These results strengthen the methodology required before a physical-to-experiential bridge claim could be treated as scientifically credible. The bridge itself remains open.
"""


def _manifest() -> str:
    payload = {
        "schema_version": 1,
        "current_frontier": CURRENT,
        "current_figure": f"docs/figures/{CURRENT_FIGURE}",
        "previous_frontiers": ["P85", "P84"],
        "canonical_figure_root": "docs/figures",
        "website_deployed_figure_root": "figures",
        "strict_hierarchy_witness": "L85 = 0 < L86 = 1/192",
        "standard_functional_count": 10560,
        "synchronizer": "scripts/sync_visual_frontier.py",
    }
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"


def _expected_outputs() -> dict[Path, str]:
    return {
        INDEX: _synchronized_index(INDEX.read_text(encoding="utf-8")),
        VISUAL_ATLAS: _synchronized_visual_atlas(
            VISUAL_ATLAS.read_text(encoding="utf-8")
        ),
        GATEWAY_README: _gateway_readme(),
        CURRENT_FRONTIER: _current_frontier(),
        MANIFEST: _manifest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if any committed visual-frontier surface differs from canonical output",
    )
    args = parser.parse_args()

    outputs = _expected_outputs()
    stale: list[str] = []
    for path, expected in outputs.items():
        actual = path.read_text(encoding="utf-8") if path.exists() else ""
        if actual == expected:
            continue
        stale.append(path.relative_to(ROOT).as_posix())
        if not args.check:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(expected, encoding="utf-8")

    if args.check and stale:
        raise SystemExit("stale visual-frontier surfaces: " + ", ".join(stale))
    if stale:
        print("synchronized visual-frontier surfaces: " + ", ".join(stale))
    else:
        print("visual-frontier surfaces already synchronized")


if __name__ == "__main__":
    main()
