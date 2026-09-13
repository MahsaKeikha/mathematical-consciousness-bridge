# Reproducibility Guide

This page is the practical entry point for reproducing the **Mathematical Consciousness Bridge** repository from a fresh clone. It covers installation, tests, linting, figure generation, figure-publication synchronization, repository-integrity checks, and GitHub Actions.

The goal is simple: a reader should not have to guess which commands were used to validate the mathematics, produce generated visual atlases, verify source-authored theorem figures, or publish the current visual frontier.

---

## 1. Supported environment

- **Compatibility:** Python 3.10, 3.11, or 3.12
- **Exact reference environment:** Python 3.12.14, recorded in `.python-version`
- **Primary test framework:** `pytest`
- **Static checks:** `ruff`
- **Numerical/figure dependencies:** `numpy`, `matplotlib`
- **Package installation:** editable install from `pyproject.toml`

The continuous-integration matrix runs the main test suite and Ruff on Python **3.10, 3.11, and 3.12**. Exact publication-artifact reproduction is additionally checked on Python **3.12.14** with the pinned versions in `requirements-reproducibility.txt`.

---

## 2. Fresh-clone setup

```bash
git clone https://github.com/MahsaKeikha/mathematical-consciousness-bridge.git
cd mathematical-consciousness-bridge
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m pip install -r requirements-reproducibility.txt
```

The `dev` extra contains the development tools. The pinned reproducibility file fixes the exact numerical and plotting versions used to reproduce publication artifacts. `requirements-figures.txt` contains the exact plotting stack and can be used separately when only the figures are needed.

If your system provides `python3` rather than `python`, substitute `python3` in the commands below.

---

## 3. Exact one-command reproduction

After installing the exact reference environment above, run:

```bash
python scripts/reproducibility_audit.py
```

Or:

```bash
make reproduce
```

This is the strongest repository-level check. It starts from a clean Git tree, compiles the source and scripts, imports every package module, runs pytest and Ruff, verifies repository structure, regenerates the computational atlases, reapplies embedded SVG descriptions, synchronizes the public figure surfaces, requires the rebuild to match the committed artifacts exactly, regenerates a second time, and requires the second build to be byte-identical to the first. Any changed tracked file is a reproducibility failure.

The exact reference environment is intentionally narrower than the compatibility matrix. This separates two questions cleanly: **does the software work on the supported Python versions?** and **can the published computational and figure-publication artifacts be rebuilt identically?**

---

## 4. Fast verification without regeneration

On systems with `make`:

```bash
make check
```

The canonical direct commands are:

```bash
python -m pytest
python -m ruff check .
python scripts/generate_all_figures.py --validate-only
python scripts/sync_figure_publication.py --check
python scripts/verify_repository.py
```

---

## 5. Run the full tests

```bash
python -m pytest
```

The test suite covers theorem implementations, exact witnesses, numerical certificates, dominance relations, finite-sample logic, figure geometry/content guards, figure-publication synchronization, publication integration, and regression behavior.

Useful pytest variants:

```bash
python -m pytest -q
python -m pytest tests/test_weighted_quad_projection_parity_functional_separation.py
python -m pytest tests/test_figure_publication_sync.py
python -m pytest -k strict_improvement
```

A passing test suite confirms that the declared implementation and regression checks pass. It is **not empirical evidence** that the physical-to-experiential bridge has been established.

---

## 6. Run static checks

```bash
python -m ruff check .
```

Or:

```bash
make lint
```

Ruff checks the Python source, scripts, and tests according to the repository configuration in `pyproject.toml`.

---

## 7. Generate and synchronize the complete visual record

Use the unified command:

```bash
python scripts/generate_all_figures.py
```

Or:

```bash
make figures
```

The command first runs the two canonical computational generators:

```text
scripts/generate_quantitative_atlas.py
    -> docs/figures/quantitative/

scripts/generate_quantum_foundations_atlas.py
    -> docs/figures/quantum/
```

It then reapplies embedded SVG title/description metadata, synchronizes the GitHub-facing `figures/` gateway and the website's current-frontier visual ordering, validates the complete canonical SVG tree, and requires the synchronized publication state to be stable.

### Figure provenance matters

The repository intentionally contains **two kinds of visual assets**:

1. **Generated computational figures.** The quantitative and quantum atlases are produced by numerical scripts from explicit equations, deterministic examples, or fixed-seed simulations. Their manifests live beside the generated SVGs.
2. **Source-controlled theorem and architecture figures.** These are publication diagrams used to communicate theorem structure, assumptions, inequalities, dependencies, and scientific boundaries. They are vector source assets stored directly in `docs/figures/`. They are validated, metadata-enriched, cataloged, and hash-audited rather than falsely described as plotting-script output.

A theorem diagram should not be mistaken for simulated evidence, and a simulation should not be mistaken for a theorem. The [Figure Catalog](figure_catalog.md) and figure captions preserve that distinction.

### Machine-auditable complete figure manifest

The top-level [`figures/manifest.json`](../figures/manifest.json) is derived from **every SVG under `docs/figures/`**. Each record stores:

- canonical repository path;
- SHA-256 digest;
- byte size;
- figure category;
- embedded SVG title;
- embedded description length.

The manifest also records the current theorem frontier and its canonical figure. This prevents the public GitHub `figures/` gateway from silently remaining at an older proposition while the theorem tree advances.

---

## 8. Validate figures without regenerating them

```bash
python scripts/generate_all_figures.py --validate-only
python scripts/sync_figure_publication.py --check
```

Or:

```bash
make figures-check
```

The validation path checks that:

- the quantitative manifest matches the quantitative SVG set;
- the quantum manifest matches the quantum SVG set;
- all SVG files under `docs/figures/` are valid parseable vector documents;
- no generated manifest silently points to a missing figure;
- the complete SHA-256 publication manifest matches the canonical SVG tree;
- the top-level GitHub figure gateway advertises P86;
- the Visual Atlas presents P86 before historical P84/P85 frontiers;
- the publication synchronizer reports zero drift.

---

## 9. Exact-commit GitHub Pages figures

The Pages builder copies the canonical `docs/figures/` tree into the deployment artifact as `_site/figures/`. During the build, image `src` values that previously referenced mutable raw-GitHub `main` URLs are rewritten to the bundled local copies.

Therefore the deployed HTML and the SVGs a reader sees come from the **same checked-out commit**. For P86 the deployed artifact must contain:

```text
_site/figures/p86_exact_minimally_weighted_quad_projection_parity.svg
```

and `visual-atlas.html` must load it as:

```html
src="figures/p86_exact_minimally_weighted_quad_projection_parity.svg"
```

The GitHub link around a figure may still point to the source file for inspection; the displayed image itself is commit-consistent with the Pages artifact.

---

## 10. Verify repository publication consistency

```bash
python scripts/verify_repository.py
```

Or:

```bash
make verify
```

This checks reader-facing and publication-level consistency that is broader than an individual theorem unit test. The current repository frontier is **P86**, and the proof sequence is expected through Proposition 86. The figure-specific synchronization contract is additionally enforced by `scripts/sync_figure_publication.py --check` and `tests/test_figure_publication_sync.py`.

The verifier is deliberately network-free so it can run in CI and in a fresh clone.

---

## 11. GitHub Actions: see the results without installing locally

### `tests`

Runs on pushes and pull requests using Python 3.10, 3.11, and 3.12:

```text
install package + dev dependencies
-> pytest
-> ruff
-> repository consistency verification
```

### `reproducibility`

Runs the exact reference environment on Python 3.12.14 and executes `python scripts/reproducibility_audit.py`. This is the release-level proof that the maintained code, tests, repository checks, generated computational artifacts, and publication surfaces can be reproduced from the committed record.

### `figures`

The figure workflow is triggered by canonical figure code, figure assets, the figure gateway, figure synchronization code, or the Visual Atlas. It performs:

```text
install exact figure environment
-> regenerate both computational atlases
-> synchronize all public figure surfaces
-> require a clean Git tree after regeneration
-> run figure publication and documentation tests
-> build the exact-commit website figure artifact
-> run repository verification
-> upload the complete reproduced visual record
```

The uploaded artifact includes the generated atlases, the current P86 theorem figure, the SHA-256 manifest, GitHub figure gateway records, and the P86 SVG as bundled into the Pages build.

### `deploy-research-website`

Pages deployment is also triggered by canonical figure changes. Before deployment it requires zero figure-publication drift, copies the canonical SVG tree into the site artifact, and verifies that the Visual Atlas loads P86 from the local exact-commit figure bundle rather than mutable raw-GitHub `main`.

---

## 12. Reproduce the current P86 implementation checks directly

The current theorem frontier is **P86**. Its primary records are:

```text
docs/proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md
docs/p86_equation_provenance.md
src/consciousness_bridge/weighted_quad_projection_parity_functional_separation.py
tests/test_weighted_quad_projection_parity_functional_separation.py
docs/figures/p86_exact_minimally_weighted_quad_projection_parity.svg
figures/manifest.json
```

Run the focused theorem and figure-publication checks with:

```bash
python -m pytest \
  tests/test_weighted_quad_projection_parity_functional_separation.py \
  tests/test_figure_publication_sync.py
```

The P86 exact hierarchy witness is:

```text
L85 = 0 < L86 = 1/192
```

The focused suite is useful for auditing P86, but the full test matrix remains the release-level standard because earlier propositions and publication surfaces are dependencies of the current repository state.

---

## 13. Interpreting a successful run

A green test or figure-generation run means the **repository's formal, computational, and publication-synchronization checks completed successfully** under the declared environment. It does not mean:

- every modeling assumption is empirically true;
- a latent target has been identified with consciousness;
- a non-rejected model has been validated;
- a quantum description has been shown to be experiential;
- the physical-to-experiential bridge has been solved.

The repository deliberately keeps **software reproducibility**, **mathematical proof**, **model adequacy**, **empirical evidence**, and **ontological interpretation** separate.

---

## 14. Recommended audit sequence for external reviewers

For a result you want to scrutinize closely:

1. read the proposition file;
2. read its equation/provenance record when available;
3. inspect the implementation in `src/consciousness_bridge/`;
4. inspect the corresponding tests;
5. run the focused test file;
6. run `make check` or the direct equivalent;
7. inspect the theorem figure and the [Figure Catalog](figure_catalog.md);
8. inspect [`figures/manifest.json`](../figures/manifest.json) for the canonical figure hash;
9. verify that the proposition's scientific-boundary statement matches the conclusion you intend to draw.

For navigation by audience and background, begin with [Start Here](../START_HERE.md). For terminology, use the [Glossary](glossary.md).
