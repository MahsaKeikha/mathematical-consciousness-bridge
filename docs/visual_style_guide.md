# Main-Page Visual Style Standard

This repository treats visual presentation as part of the scientific audit trail. Figures embedded in the main research page should remain readable without dominating the page or obscuring the surrounding mathematical argument.

## Quantitative figures

The reproducible quantitative and quantum atlases use the common Matplotlib baseline

- figure size: `7.6 × 4.7 in`,
- base font size: `9.5 pt`,
- axes title size: `13 pt`,
- axes label size: `9.5 pt`,
- vector SVG output with live text.

The generators are the source of truth:

- `scripts/generate_quantitative_atlas.py`,
- `scripts/generate_quantum_foundations_atlas.py`.

Do not manually enlarge individual generated SVG files on the main page unless a scientifically necessary detail becomes unreadable.

## Canonical architecture figures

Canonical research maps should use publication-style whitespace, short text lines, non-overlapping labels, and explicit interpretation boundaries. Dense decorative trajectories or repeated spiral paths should not be used when they compete with equations or labels.

The state-space map is the reference pattern: empirical regimes are represented schematically, transitions are sparse and explicit, and measurement/inference layers are separated from bridge-level interpretation.

## Scientific boundary

Visual proximity does not establish theoretical identity. In particular, colored regions, arrows, manifolds, basins, and geometric embeddings are illustrations of mathematical or empirical structure unless a theorem explicitly assigns them a stronger meaning.
