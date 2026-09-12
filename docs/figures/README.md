# Figure provenance and regeneration

This directory contains the visual record for the Mathematical Consciousness Bridge research program.

The repository intentionally distinguishes **generated computational atlases** from **source-controlled theorem and architecture diagrams**. They have different scientific meanings and should not be presented as the same kind of evidence.

## 1. Generated computational atlases

These directories are produced by executable Python scripts:

```text
docs/figures/quantitative/
docs/figures/quantum/
```

Regenerate both with:

```bash
python scripts/generate_all_figures.py
```

The canonical underlying generators are:

```text
scripts/generate_quantitative_atlas.py
scripts/generate_quantum_foundations_atlas.py
```

Each generated atlas has a JSON manifest stored beside its SVG outputs. The unified generator checks that the manifest and generated SVG set agree.

## 2. Source-controlled theorem and architecture figures

SVG files stored directly in `docs/figures/` include theorem diagrams, dependency maps, structural illustrations, and explanatory publication graphics. Current examples include:

```text
p75_target_model_adequacy_overidentification.svg
p76_finite_sample_target_model_adequacy.svg
p77_full_law_model_set_separation.svg
p78_certified_continuous_model_separation.svg
p79_certified_sampling_radius.svg
p80_simplex_coupled_model_separation.svg
p81_projection_event_model_separation.svg
p82_exact_nested_projection_contrast.svg
p83_exact_projection_parity.svg
p84_exact_pairwise_walsh_contrast.svg
```

These figures communicate mathematical structure, assumptions, inequalities, or proof logic. They are not claimed to be simulation results merely because they are SVG files.

The unified figure validator parses every SVG under this directory and fails if the figure tree contains invalid vector documents or generated-manifest mismatches.

## 3. Current frontier figure

The current theorem frontier is **P84**:

```text
docs/figures/p84_exact_pairwise_walsh_contrast.svg
```

Its corresponding records are:

```text
docs/proposition_84_exact_pairwise_walsh_contrast.md
docs/p84_equation_provenance.md
src/consciousness_bridge/walsh_contrast_model_separation.py
tests/test_walsh_contrast_model_separation.py
tests/test_p84_figure_geometry.py
```

P84 is a conditional exact-rational model-distance theorem. Its visual does not identify a latent state with consciousness, and the physical-to-experiential bridge remains open.

## 4. Validate without regenerating

```bash
python scripts/generate_all_figures.py --validate-only
```

or:

```bash
make figures-check
```

## 5. Reproduce through GitHub Actions

The `figures` workflow regenerates and validates the computational atlases in the pinned figure environment. The `reproducibility` workflow runs the complete publication audit, including tests, Ruff, repository verification, two full deterministic atlas generations, and a clean-tree check.
