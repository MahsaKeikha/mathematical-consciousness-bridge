# Reproducibility Guide

**Use this page when you want to rerun, verify, or audit the repository rather than only read it.**

You do not need every command at once. Choose the route that matches your goal.

## Choose your route

| I want to... | Use this |
| --- | --- |
| Reproduce the maintained repository as strictly as possible | `make reproduce` |
| Run the normal verification suite | `make check` |
| Run only the current P89 theorem checks | focused P89 commands below |
| Validate figures without rebuilding them | `make figures-check` |
| Regenerate the complete visual record | `make figures` |
| Inspect CI without installing locally | GitHub Actions |

The current public theorem frontier is **P89**. The formal release remains **v0.82.0**.

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

## 5. Focused audit of the current P89 frontier

The current theorem frontier is **P89**.

Its direct technical record is:

```text
docs/proposition_89_complete_linear_parity_duality.md
docs/p89_equation_provenance.md
src/consciousness_bridge/complete_linear_parity_duality.py
tests/test_complete_linear_parity_duality.py
docs/figures/p89_complete_linear_parity_duality.svg
figures/manifest.json
```

Run the focused theorem and figure-publication checks with:

```bash
python -m pytest \
  tests/test_complete_linear_parity_duality.py \
  tests/test_figure_publication_sync.py \
  tests/test_p89_reader_surface_coherence.py
```

P89 considers every real linear functional of the eleven canonical P83 parity coordinates. On the published strict witness, the exact functional coefficient vector is

```text
(0, -2, -1, 1, 1, 1, -2, -1, -3, 2, -3)
```

with empirical value `-13/6`, exact P75 interval `[-51/8,-3]`, interval gap `5/6`, centering constant `-3`, and centered transfer norm `28`. The normalized lower certificate is therefore

\[
rac5{168}.
\]

A matching rational convex-vertex plus zero-mass perturbation certificate has exact infinity radius `5/168`. The equality of the lower and upper certificates proves that `5/168` is the exact optimum over the complete real linear parity-functional class on the stated box. Thus

\[
L_{88}=rac1{64}<L_{89}=rac5{168}.
\]

This completeness statement is limited to the declared linear parity-functional class. It does not exhaust nonlinear P75 constraints or close the physical-to-experiential bridge.

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
docs/figures/p88_exact_radius_three_bounded_primitive_quad_projection_parity.svg
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
