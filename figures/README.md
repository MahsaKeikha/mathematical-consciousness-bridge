# Visual research gateway

This top-level `figures/` directory is the GitHub-facing entry point for the
visual record of the Mathematical Consciousness Bridge project. The canonical
SVG archive lives in [`docs/figures/`](../docs/figures/); this gateway is derived
from that archive by code so it cannot silently remain on an older proposition.

## Current theorem frontier: P86

![P86 current theorem frontier](../docs/figures/p86_exact_minimally_weighted_quad_projection_parity.svg)

Canonical figure: [`p86_exact_minimally_weighted_quad_projection_parity.svg`](../docs/figures/p86_exact_minimally_weighted_quad_projection_parity.svg)
Theorem: [`proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md`](../docs/proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md)
Equation provenance: [`p86_equation_provenance.md`](../docs/p86_equation_provenance.md)

For the full P71-P86 visual progression, open
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
