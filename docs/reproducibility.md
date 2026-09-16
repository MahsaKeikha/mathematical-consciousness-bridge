# Reproducibility Guide

**Use this page when you want to rerun, verify, or audit the repository rather than only read it.**

You do not need every command at once. Choose the route that matches your goal.

## Choose your route

| I want to... | Use this |
| --- | --- |
| Reproduce the maintained repository as strictly as possible | `make reproduce` |
| Run the normal verification suite | `make check` |
| Run only the current P99 theorem checks | focused P99 commands below |
| Validate figures without rebuilding them | `make figures-check` |
| Regenerate the complete visual record | `make figures` |
| Inspect CI without installing locally | GitHub Actions |

The current public theorem frontier is **P100**. The formal release remains **v0.82.0**.

---

## 1. Supported environment

The repository supports:

- Python 3.10
- Python 3.11
- Python 3.12

The exact reference environment is **Python 3.12.14**, recorded in `.python-version`.

Primary tools:

- `pytest` for tests
- `ruff` for static checks
- `numpy` and `matplotlib` for numerical and visual work
- editable package installation from `pyproject.toml`

The compatibility matrix and the exact reproduction environment answer different questions. The compatibility matrix asks whether the software works across supported Python versions. The exact environment asks whether maintained computational and publication artifacts can be rebuilt identically.

---

## 2. Fresh clone setup

```bash
git clone https://github.com/MahsaKeikha/mathematical-consciousness-bridge.git
cd mathematical-consciousness-bridge
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m pip install -r requirements-reproducibility.txt
```

If your system uses `python3` rather than `python`, substitute `python3` in the commands below.

`requirements-reproducibility.txt` pins the exact environment used for strict reproduction. `requirements-figures.txt` contains the plotting stack for figure work.

---

## 3. Exact repository reproduction

Run:

```bash
make reproduce
```

or directly:

```bash
python scripts/reproducibility_audit.py
```

This is the strongest maintained repository check. It verifies a clean Git state, compiles source and scripts, imports package modules, runs tests and static checks, verifies repository structure, regenerates computational atlases, reapplies SVG metadata, synchronizes public figure surfaces, and checks that the rebuild matches the committed record.

A second generation pass is used to confirm that the maintained generated artifacts are stable.

### What success means

A successful exact reproduction means the repository can rebuild its maintained computational and publication surfaces under the declared reference environment.

It does **not** mean that every scientific assumption is empirically true or that the bridge from physical description to experience has been established.

---

## 4. Fast verification

Run:

```bash
make check
```

The corresponding direct commands are:

```bash
python -m pytest
python -m ruff check .
python scripts/generate_all_figures.py --validate-only
python scripts/sync_figure_publication.py --check
python scripts/verify_repository.py
```

Use this route when you want to verify the current committed state without regenerating every maintained artifact.

---

## 5. Focused audit of the current P100 frontier

The current theorem frontier is **P100**.

Its direct technical record is:

```text
docs/proposition_100_anytime_sequential_eprocess.md
docs/p100_equation_provenance.md
src/consciousness_bridge/anytime_sequential_eprocess.py
tests/test_anytime_sequential_eprocess.py
docs/figures/p100_anytime_sequential_eprocess.svg
figures/manifest.json
```

Run the focused theorem and publication checks with:

```bash
python -m pytest -q \
  tests/test_anytime_sequential_eprocess.py \
  tests/test_p100_reader_surface_coherence.py \
  tests/test_p99_reader_surface_coherence.py \
  tests/test_figure_publication_sync.py \
  tests/test_frontier_publication_consistency.py
python scripts/sync_figure_publication.py --check
python scripts/verify_repository.py
```

P100 composes fresh P99 round e-values with predictable reserve stakes. Under the declared sequential null, each current round remains conditionally valid given the past, the cumulative product is a nonnegative supermartingale, and Ville's inequality protects repeated inspection and adaptive stopping.

For the exact 95 percent checkpoint, a moderate round has `E_t = 25/2`, half stake gives `F_t = 27/4`, and two fresh rounds give `M_2 = 729/16 = 45.5625 > 20`. The inherited per-regime crossings are `3774 / 3792`; the two-round unique-data totals are `30192 / 30336`.

P100 does not make reused certification data fresh, permit current-round leakage, establish model acceptance, identify consciousness, establish nonphysicality, or complete the physical-to-experiential bridge.

---

## 6. Run the full tests

```bash
python -m pytest
```

Useful variants include:

```bash
python -m pytest -q
python -m pytest tests/test_radius_three_bounded_primitive_quad_projection_parity_functional_separation.py
python -m pytest tests/test_figure_publication_sync.py
python -m pytest -k strict_improvement
```

The test suite covers theorem implementations, exact witnesses, numerical certificates, finite data logic, figure guards, publication synchronization, reader experience contracts, and regression behavior.

A passing test suite confirms that the declared implementation and repository checks pass. It is not empirical evidence about consciousness.

---

## 7. Static checks

Run:

```bash
python -m ruff check .
```

or:

```bash
make lint
```

Ruff checks the maintained Python source, scripts, and tests according to `pyproject.toml`.

---

## 8. Generate the visual record

Run:

```bash
make figures
```

or:

```bash
python scripts/generate_all_figures.py
```

The unified figure path runs the canonical computational generators, reapplies SVG title and description metadata, synchronizes public figure surfaces, and validates the canonical SVG tree.

The repository contains two different kinds of visual assets.

### Generated computational figures

The quantitative and quantum atlases are produced by scripts from explicit equations, deterministic examples, or fixed seed simulations.

### Source controlled research figures

Theorem and architecture figures communicate mathematical structure, assumptions, dependencies, inequalities, and scientific boundaries. They are source assets, not simulated evidence.

A theorem diagram should not be mistaken for a simulation. A simulation should not be mistaken for a theorem.

The [Figure Catalog](figure_catalog.md) records those roles explicitly.

---

## 9. Validate figures without regenerating them

Run:

```bash
make figures-check
```

or:

```bash
python scripts/generate_all_figures.py --validate-only
python scripts/sync_figure_publication.py --check
```

The validation path checks the generated manifests, SVG parseability, canonical figure inventory, SHA 256 publication manifest, current frontier synchronization, and public visual ordering.

The current frontier figure is:

```text
docs/figures/p99_cross_fitted_evalue_aggregation.svg
```

---

## 10. Figure manifest and exact publication record

The top level file

```text
figures/manifest.json
```

is derived from every SVG under `docs/figures/`.

Each record stores:

- canonical repository path
- SHA 256 digest
- byte size
- figure category
- embedded SVG title
- embedded description length

The manifest also records the current theorem frontier and its canonical figure. This prevents the public figure gateway from silently remaining on an older proposition.

The Pages build copies canonical figures into the deployment artifact so the HTML and displayed SVGs come from the same checked out commit.

---

## 11. Repository consistency verification

Run:

```bash
make verify
```

or:

```bash
python scripts/verify_repository.py
```

This checks publication and reader facing consistency that is broader than an individual theorem unit test.

The repository verifier is designed to run without network access so it can be used in CI and in a fresh clone.

---

## 12. GitHub Actions

Three workflow families are especially useful to external reviewers.

### Tests

Runs the supported Python matrix and performs installation, pytest, Ruff, and repository consistency verification.

### Reproducibility

Runs the exact reference environment and executes the end to end reproducibility audit.

### Figures and website publication

Regenerates or validates the maintained visual surfaces, checks synchronization, builds the exact commit website figure artifact, and verifies that public figure references are consistent with the checked out commit.

These workflows let a reader inspect current verification results without installing the repository locally.

---

## 13. How to interpret a green run

A green run means the declared formal, computational, and publication checks completed successfully under the stated environment.

It does not mean:

- every modeling assumption is empirically true
- a latent target has been identified with consciousness
- a model that was not rejected has been validated as true
- a quantum description has been shown to be experiential
- the physical to experiential bridge has been solved

The repository deliberately keeps software reproducibility, mathematical proof, model adequacy, empirical evidence, and ontological interpretation separate.

---

## 14. Recommended reviewer path

For a result you want to inspect closely:

1. Read the proposition page.
2. Read its provenance record when available.
3. Inspect the corresponding implementation.
4. Inspect the regression tests.
5. Run the focused test file.
6. Run `make check`.
7. Inspect the theorem figure and the [Figure Catalog](figure_catalog.md).
8. Inspect `figures/manifest.json` for the canonical figure hash.
9. Confirm that the scientific boundary matches the conclusion you intend to draw.

For the conceptual path, begin with [Start Here](../START_HERE.md).

For terminology, use the [Glossary](glossary.md).

For the theorem dependency structure, use the [Theorem Roadmap](theorem_roadmap.md).

For every proposition in chronological order, use the [Detailed Proposition Record](detailed_proposition_record.md).

### P91 exact audit command

```bash
python -m pytest -q tests/test_exact_global_mixed_prevalence_distance.py
python scripts/sync_figure_publication.py --check
python scripts/verify_repository.py
```

The P91 lower certificate uses only exact `Fraction` arithmetic and checks all 512 vertices of the selected nonnegative determinant box.

### P92 exact audit command

```bash
python -m pytest -q tests/test_exact_global_mixed_prevalence_distance.py
python scripts/sync_figure_publication.py --check
python scripts/verify_repository.py
```

The P92 theorem uses exact `Fraction` arithmetic for all published determinant values, sign radii, factorization checks, and the matching `1/24` upper certificate.

### P93 focused audit

```bash
python -m pytest -q tests/test_localized_sign_coherence_rejection.py
python scripts/sync_figure_publication.py --check
python scripts/verify_repository.py
```

The P93 threshold audit uses P79 exact rational lower and upper sampling-radius envelopes and distinguishes the mathematical 1623 crossing from the first realizable exact 24-count replication at 1632.

P95 direct technical record:

```text
docs/proposition_95_drift_aware_stratified_sign_coherence.md
docs/p95_equation_provenance.md
docs/figures/p95_drift_aware_stratified_sign_coherence.svg
src/consciousness_bridge/drift_aware_stratified_sign_coherence.py
tests/test_drift_aware_stratified_sign_coherence.py
```

Focused check:

```bash
python -m pytest -q tests/test_drift_aware_stratified_sign_coherence.py
```
