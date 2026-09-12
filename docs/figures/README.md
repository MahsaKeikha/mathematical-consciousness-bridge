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

SVG files stored directly in `docs/figures/` include theorem diagrams, dependency maps, structural illustrations, and explanatory publication graphics. Examples include:

```text
p75_target_model_adequacy_overidentification.svg
p76_finite_sample_target_model_adequacy.svg
p77_full_law_model_set_separation.svg
p78_certified_continuous_model_separation.svg
p79_certified_sampling_radius.svg
p80_simplex_coupled_model_separation.svg
p81_projection_event_model_separation.svg
```

These figures communicate mathematical structure, assumptions, inequalities, or proof logic. They are not claimed to be simulation results merely because they are SVG files.

The unified figure validator parses every SVG under this directory and fails if the figure tree contains invalid vector documents or generated-manifest mismatches.

## 3. Current frontier figure

The current theorem frontier is **P81**:

```text
docs/figures/p81_projection_event_model_separation.svg
```

Its corresponding records are:

```text
docs/proposition_81_projection_event_model_separation.md
docs/p81_equation_provenance.md
src/consciousness_bridge/projection_event_model_separation.py
tests/test_projection_event_model_separation.py
tests/test_p81_figure_geometry.py
```

## 4. Validate without regenerating

```bash
python scripts/generate_all_figures.py --validate-only
```

or:

```bash
make figures-check
```

## 5. Reproduce through GitHub Actions

The `.github/workflows/figures.yml` workflow regenerates both computational atlases, validates the complete figure tree, runs repository verification, and uploads the generated atlas directories as a workflow artifact.

A successful figure workflow means the repository's declared generation and validation path executed successfully. It does not convert a theorem illustration, synthetic benchmark, or model calculation into empirical evidence about consciousness.

For the curated reader-facing index, see [`docs/figure_catalog.md`](../figure_catalog.md). For full setup instructions, see [`docs/reproducibility.md`](../reproducibility.md).
