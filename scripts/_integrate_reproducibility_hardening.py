from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(path: str, old: str, new: str) -> None:
    text = read(path)
    if old not in text:
        raise RuntimeError(f"expected marker not found in {path}: {old[:90]!r}")
    if text.count(old) != 1:
        raise RuntimeError(f"marker is not unique in {path}: {old[:90]!r}")
    write(path, text.replace(old, new, 1))


def patch_generators() -> None:
    for path in (
        "scripts/generate_quantitative_atlas.py",
        "scripts/generate_quantum_foundations_atlas.py",
    ):
        replace_once(
            path,
            '        "svg.fonttype": "none",\n',
            '        "svg.fonttype": "none",\n'
            '        "svg.hashsalt": "mathematical-consciousness-bridge-v0.81.0",\n'
            '        "font.family": "DejaVu Sans",\n',
        )
        replace_once(
            path,
            "META = []\n",
            'SVG_METADATA = {\n'
            '    "Date": None,\n'
            '    "Creator": "Mathematical Consciousness Bridge v0.81.0",\n'
            '}\n\n'
            'META = []\n',
        )
        replace_once(
            path,
            '    fig.savefig(OUT / filename, format="svg", bbox_inches="tight")\n',
            '    fig.savefig(\n'
            '        OUT / filename,\n'
            '        format="svg",\n'
            '        bbox_inches="tight",\n'
            '        metadata=SVG_METADATA,\n'
            '    )\n',
        )


def patch_unified_figure_build() -> None:
    replace_once(
        "scripts/generate_all_figures.py",
        "GENERATORS = (\n"
        '    ROOT / "scripts" / "generate_quantitative_atlas.py",\n'
        '    ROOT / "scripts" / "generate_quantum_foundations_atlas.py",\n'
        ")\n",
        "GENERATORS = (\n"
        '    ROOT / "scripts" / "generate_quantitative_atlas.py",\n'
        '    ROOT / "scripts" / "generate_quantum_foundations_atlas.py",\n'
        ")\n"
        'ENRICHER = ROOT / "scripts" / "enrich_figure_documentation.py"\n',
    )
    replace_once(
        "scripts/generate_all_figures.py",
        "            _run_generator(generator)\n\n    validate_figures()\n",
        "            _run_generator(generator)\n"
        "        if not ENRICHER.is_file():\n"
        "            raise FileNotFoundError(\n"
        '                f"missing figure documentation enricher: {ENRICHER.relative_to(ROOT)}"\n'
        "            )\n"
        "        _run_generator(ENRICHER)\n\n"
        "    validate_figures()\n",
    )
    replace_once(
        "scripts/generate_all_figures.py",
        "This command regenerates the two computational atlases using their canonical\n"
        "scripts and then validates every SVG in the figure tree as parseable vector\n"
        "content. Source-authored theorem SVGs are validated rather than rewritten.\n",
        "This command regenerates the two computational atlases using their canonical\n"
        "scripts, reapplies the repository's embedded SVG title/description metadata,\n"
        "and then validates every SVG in the figure tree as parseable vector content.\n"
        "Source-authored theorem SVGs are validated and enriched from their maintained\n"
        "documentation records rather than being recreated by a plotting script.\n",
    )


def patch_audit() -> None:
    path = "scripts/reproducibility_audit.py"
    text = read(path)
    text = text.replace(
        '    python -m pip install -r requirements-figures.txt\n',
        '    python -m pip install -r requirements-reproducibility.txt\n',
    )
    text = text.replace(
        'import importlib.metadata\n',
        'import importlib.metadata\nimport pkgutil\n',
    )
    text = text.replace(
        'PINNED_RUNTIME = {\n    "matplotlib": "3.11.2",\n    "numpy": "2.5.3",\n}\n',
        'REFERENCE_PYTHON = (3, 12, 14)\n'
        'PINNED_RUNTIME = {\n'
        '    "matplotlib": "3.11.2",\n'
        '    "numpy": "2.5.3",\n'
        '    "pytest": "9.1.1",\n'
        '    "ruff": "0.16.7",\n'
        '}\n',
    )
    text = text.replace(
        '            "`python -m pip install -r requirements-figures.txt`.\\n"\n',
        '            "`python -m pip install -r requirements-reproducibility.txt`.\\n"\n',
    )
    old_import = '''def _verify_package_import() -> None:\n    module = importlib.import_module("consciousness_bridge")\n    if module is None:\n        raise RuntimeError("failed to import consciousness_bridge")\n    print("[reproduce] package import verified")\n'''
    new_import = '''def _verify_package_imports() -> None:\n    package = importlib.import_module("consciousness_bridge")\n    imported = ["consciousness_bridge"]\n    for module_info in pkgutil.iter_modules(\n        package.__path__, prefix="consciousness_bridge."\n    ):\n        importlib.import_module(module_info.name)\n        imported.append(module_info.name)\n    print(f"[reproduce] imported {len(imported)} package modules successfully")\n'''
    if old_import not in text:
        raise RuntimeError("package import marker not found in reproducibility audit")
    text = text.replace(old_import, new_import, 1)
    text = text.replace(
        '    if sys.version_info < (3, 10):\n        raise RuntimeError("Python 3.10 or newer is required")\n\n',
        '    if tuple(sys.version_info[:3]) != REFERENCE_PYTHON:\n'
        '        actual = ".".join(str(part) for part in sys.version_info[:3])\n'
        '        expected = ".".join(str(part) for part in REFERENCE_PYTHON)\n'
        '        raise RuntimeError(\n'
        '            f"exact reference audit requires Python {expected}; found {actual}. "\n'
        '            "Compatibility tests still cover Python 3.10, 3.11, and 3.12."\n'
        '        )\n\n',
    )
    text = text.replace(
        '    _verify_package_import()\n',
        '    _verify_package_imports()\n',
    )
    text = text.replace(
        '    _run("scripts/normalize_typography.py")\n'
        '    _require_clean_tree("typography normalization")\n\n',
        '',
    )
    write(path, text)


def patch_makefile() -> None:
    replace_once(
        "Makefile",
        ".PHONY: install test lint figures figures-check verify check\n",
        ".PHONY: install test lint figures figures-check verify check reproduce\n",
    )
    text = read("Makefile")
    if "reproduce:\n" not in text:
        text += "\nreproduce:\n\t$(PYTHON) scripts/reproducibility_audit.py\n"
    write("Makefile", text)


def patch_verifier() -> None:
    path = "scripts/verify_repository.py"
    text = read(path)
    text = text.replace(
        '    "pyproject.toml",\n',
        '    "pyproject.toml",\n'
        '    ".python-version",\n'
        '    "requirements-figures.txt",\n'
        '    "requirements-reproducibility.txt",\n',
        1,
    )
    text = text.replace(
        '    "scripts/generate_quantum_foundations_atlas.py",\n',
        '    "scripts/generate_quantum_foundations_atlas.py",\n'
        '    "scripts/reproducibility_audit.py",\n',
        1,
    )
    marker = '''    if not (ROOT / ".github" / "workflows" / "figures.yml").is_file():\n        raise RuntimeError("missing GitHub Actions figure workflow")\n'''
    replacement = marker + '''    if not (ROOT / ".github" / "workflows" / "reproducibility.yml").is_file():\n        raise RuntimeError("missing GitHub Actions reproducibility workflow")\n'''
    if marker not in text:
        raise RuntimeError("workflow marker not found in repository verifier")
    text = text.replace(marker, replacement, 1)
    write(path, text)


def patch_script_docs() -> None:
    readme = read("scripts/README.md")
    readme = readme.replace(
        "python scripts/verify_repository.py\n```\n",
        "python scripts/verify_repository.py\n"
        "python scripts/reproducibility_audit.py\n```\n",
        1,
    )
    readme = readme.replace(
        "These commands are also exposed through the root `Makefile` as `make figures`, `make figures-check`, and `make verify`.\n",
        "These commands are also exposed through the root `Makefile`. Use `make reproduce` for the strongest end-to-end audit from a clean checkout.\n",
        1,
    )
    marker = "## Figure generation\n"
    section = '''## End-to-end reproducibility\n\n### `reproducibility_audit.py`\n\nCanonical full audit for the reference environment. It imports every package module, runs pytest and Ruff, verifies repository structure, regenerates and enriches all computational figures twice, and fails unless both regeneration passes leave the Git working tree byte-for-byte clean.\n\nInstall the exact reference environment first with:\n\n```bash\npython -m pip install -e ".[dev]"\npython -m pip install -r requirements-reproducibility.txt\n```\n\nThen run:\n\n```bash\npython scripts/reproducibility_audit.py\n```\n\n'''
    if section not in readme:
        if marker not in readme:
            raise RuntimeError("scripts README figure marker not found")
        readme = readme.replace(marker, section + marker, 1)
    write("scripts/README.md", readme)

    quick = read("scripts/QUICKSTART.md")
    old = '''## Fastest complete validation\n\nFrom the repository root:\n\n```bash\npython -m pip install -e ".[dev]"\npython -m pytest\npython -m ruff check .\npython scripts/generate_all_figures.py --validate-only\npython scripts/verify_repository.py\n```\n\nThe same validation is available through:\n\n```bash\nmake check\n```\n'''
    new = '''## Strongest reproducibility audit\n\nFor the exact v0.81.0 reference environment, use Python 3.12.14 and run:\n\n```bash\npython -m pip install -e ".[dev]"\npython -m pip install -r requirements-reproducibility.txt\npython scripts/reproducibility_audit.py\n```\n\nOr, after installation:\n\n```bash\nmake reproduce\n```\n\nThis is stronger than a normal test run: it runs the test/static checks, imports the package modules, rebuilds the generated atlases, reapplies figure documentation metadata, and requires two consecutive rebuilds to leave a clean Git tree.\n\n## Fast compatibility validation\n\n```bash\nmake check\n```\n\nThe compatibility path is also exercised in CI on Python 3.10, 3.11, and 3.12.\n'''
    if old not in quick:
        raise RuntimeError("quickstart validation block not found")
    quick = quick.replace(old, new, 1)
    quick = quick.replace(
        "| `generate_all_figures.py` | Canonical figure entry point | Regenerates computational atlases and validates all SVG assets |\n",
        "| `reproducibility_audit.py` | Exact reference audit | Runs tests/static checks, imports modules, regenerates figures twice, and requires a byte-clean Git tree |\n"
        "| `generate_all_figures.py` | Canonical figure entry point | Regenerates computational atlases, reapplies SVG documentation metadata, and validates all SVG assets |\n",
        1,
    )
    write("scripts/QUICKSTART.md", quick)


def patch_reproducibility_guide() -> None:
    path = "docs/reproducibility.md"
    text = read(path)
    text = text.replace(
        "- **Python:** 3.10, 3.11, or 3.12\n",
        "- **Compatibility:** Python 3.10, 3.11, or 3.12\n"
        "- **Exact reference environment:** Python 3.12.14, recorded in `.python-version`\n",
        1,
    )
    text = text.replace(
        "The continuous-integration matrix runs the main test suite and Ruff on Python **3.10, 3.11, and 3.12**.\n",
        "The continuous-integration matrix runs the main test suite and Ruff on Python **3.10, 3.11, and 3.12**. Exact publication-artifact reproduction is additionally checked on Python **3.12.14** with the pinned versions in `requirements-reproducibility.txt`.\n",
        1,
    )
    old_setup = '''python -m pip install --upgrade pip\npython -m pip install -e ".[dev]"\n```\n\nThe `dev` extra contains the dependencies needed for tests, linting, and the generated figure atlases.\n'''
    new_setup = '''python -m pip install --upgrade pip\npython -m pip install -e ".[dev]"\npython -m pip install -r requirements-reproducibility.txt\n```\n\nThe `dev` extra contains the development tools. The pinned reproducibility file fixes the exact numerical and plotting versions used to reproduce the publication artifacts. `requirements-figures.txt` contains the exact plotting stack and can be used separately when only the figures are needed.\n'''
    if old_setup not in text:
        raise RuntimeError("reproducibility setup block not found")
    text = text.replace(old_setup, new_setup, 1)
    marker = "## 3. One-command verification\n"
    stronger = '''## 3. Exact one-command reproduction\n\nAfter installing the exact reference environment above, run:\n\n```bash\npython scripts/reproducibility_audit.py\n```\n\nOr:\n\n```bash\nmake reproduce\n```\n\nThis is the strongest repository-level check. It starts from a clean Git tree, compiles the source and scripts, imports every package module, runs pytest and Ruff, verifies repository structure, regenerates both computational atlases, reapplies embedded SVG descriptions, requires the rebuild to match the committed artifacts exactly, regenerates a second time, and requires the second build to be byte-identical to the first. Any changed tracked file is a reproducibility failure.\n\nThe exact reference environment is intentionally narrower than the compatibility matrix. This separates two questions cleanly: **does the software work on the supported Python versions?** and **can the published computational artifacts be rebuilt identically?**\n\n---\n\n## 4. Fast verification without regeneration\n'''
    if marker not in text:
        raise RuntimeError("one-command verification marker not found")
    text = text.replace(marker, stronger, 1)
    text = text.replace("## 4. Run the full tests", "## 5. Run the full tests", 1)
    text = text.replace("## 5. Run static checks", "## 6. Run static checks", 1)
    text = text.replace("## 6. Generate the reproducible figure atlases", "## 7. Generate the reproducible figure atlases", 1)
    text = text.replace("## 7. Validate figures without regenerating them", "## 8. Validate figures without regenerating them", 1)
    text = text.replace("## 8. Verify repository publication consistency", "## 9. Verify repository publication consistency", 1)
    text = text.replace("## 9. GitHub Actions: see the results without installing locally", "## 10. GitHub Actions: see the results without installing locally", 1)
    text = text.replace("## 10. Reproduce the current P81 implementation checks directly", "## 11. Reproduce the current P81 implementation checks directly", 1)
    text = text.replace("## 11. Interpreting a successful run", "## 12. Interpreting a successful run", 1)
    text = text.replace("## 12. Recommended audit sequence for external reviewers", "## 13. Recommended audit sequence for external reviewers", 1)
    text = text.replace(
        "It then validates the complete SVG figure tree.\n",
        "It then reapplies embedded SVG title/description metadata and validates the complete SVG figure tree. In the exact reference environment, regeneration must leave `git status --porcelain` empty.\n",
        1,
    )
    actions_marker = "### `figures`\n"
    repro_actions = '''### `reproducibility`\n\nRuns the exact reference environment on Python 3.12.14 and executes `python scripts/reproducibility_audit.py`. This is the release-level proof that the maintained code, tests, repository checks, and generated computational artifacts can be reproduced from the committed record.\n\n'''
    if repro_actions not in text:
        if actions_marker not in text:
            raise RuntimeError("actions figure marker not found")
        text = text.replace(actions_marker, repro_actions + actions_marker, 1)
    write(path, text)


def patch_root_readme() -> None:
    path = "README.md"
    text = read(path)
    badge = "[![tests](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/test.yml/badge.svg)](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/test.yml)\n"
    added_badge = badge + "[![reproducibility](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/reproducibility.yml/badge.svg)](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/reproducibility.yml)\n[![figures](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/figures.yml/badge.svg)](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/figures.yml)\n"
    if "actions/workflows/reproducibility.yml/badge.svg" not in text:
        if badge not in text:
            raise RuntimeError("README tests badge marker not found")
        text = text.replace(badge, added_badge, 1)
    tip_end = "and use the **[Reproducibility Guide](docs/reproducibility.md)** when you want to run the tests or regenerate the computational figure atlases.\n"
    reproducible = '''\n> [!NOTE]\n> **Reproduce the complete computational record:** use Python 3.12.14, install `requirements-reproducibility.txt`, and run `python scripts/reproducibility_audit.py` (or `make reproduce`). The audit fails unless tests/static checks pass and two full generated-figure rebuilds leave the Git tree byte-for-byte clean.\n'''
    if reproducible.strip() not in text:
        if tip_end not in text:
            raise RuntimeError("README reproducibility tip marker not found")
        text = text.replace(tip_end, tip_end + reproducible, 1)
    write(path, text)


def write_workflows() -> None:
    figures = '''name: figures\n\non:\n  workflow_dispatch:\n  push:\n    branches:\n      - main\n    paths:\n      - "scripts/generate_all_figures.py"\n      - "scripts/generate_quantitative_atlas.py"\n      - "scripts/generate_quantum_foundations_atlas.py"\n      - "scripts/enrich_figure_documentation.py"\n      - "requirements-figures.txt"\n      - "requirements-reproducibility.txt"\n      - "docs/figures/**"\n      - "docs/reproducibility.md"\n      - "pyproject.toml"\n      - ".github/workflows/figures.yml"\n  pull_request:\n    paths:\n      - "scripts/generate_all_figures.py"\n      - "scripts/generate_quantitative_atlas.py"\n      - "scripts/generate_quantum_foundations_atlas.py"\n      - "scripts/enrich_figure_documentation.py"\n      - "requirements-figures.txt"\n      - "requirements-reproducibility.txt"\n      - "docs/figures/**"\n      - "docs/reproducibility.md"\n      - "pyproject.toml"\n      - ".github/workflows/figures.yml"\n\njobs:\n  generate-and-validate:\n    runs-on: ubuntu-24.04\n    steps:\n      - uses: actions/checkout@v4\n      - uses: actions/setup-python@v5\n        with:\n          python-version: "3.12.14"\n      - name: Install repository and exact figure environment\n        run: |\n          python -m pip install --upgrade pip\n          python -m pip install -e ".[dev]"\n          python -m pip install -r requirements-figures.txt\n      - name: Regenerate and enrich computational figure atlases\n        run: python scripts/generate_all_figures.py\n      - name: Require byte-identical regeneration\n        run: |\n          if [ -n "$(git status --porcelain)" ]; then\n            echo "Generated artifacts differ from the committed publication record."\n            git status --short\n            git diff --stat\n            git diff\n            exit 1\n          fi\n      - name: Verify repository publication surfaces\n        run: python scripts/verify_repository.py\n      - name: Upload generated figure atlases\n        uses: actions/upload-artifact@v4\n        with:\n          name: generated-figure-atlases-python-3.12.14\n          path: |\n            docs/figures/quantitative\n            docs/figures/quantum\n          if-no-files-found: error\n'''
    write(".github/workflows/figures.yml", figures)

    reproducibility = '''name: reproducibility\n\non:\n  workflow_dispatch:\n  push:\n    branches:\n      - main\n  pull_request:\n\njobs:\n  reproduce:\n    runs-on: ubuntu-24.04\n    steps:\n      - uses: actions/checkout@v4\n      - uses: actions/setup-python@v5\n        with:\n          python-version: "3.12.14"\n      - name: Install exact reference environment\n        run: |\n          python -m pip install --upgrade pip\n          python -m pip install -e ".[dev]"\n          python -m pip install -r requirements-reproducibility.txt\n      - name: Run end-to-end reproducibility audit\n        run: python scripts/reproducibility_audit.py\n      - name: Upload reproduced computational atlases\n        uses: actions/upload-artifact@v4\n        with:\n          name: reproduced-computational-atlases-v0.81.0\n          path: |\n            docs/figures/quantitative\n            docs/figures/quantum\n          if-no-files-found: error\n'''
    write(".github/workflows/reproducibility.yml", reproducibility)

    test = read(".github/workflows/test.yml")
    marker = '      - name: Run pytest suite\n        run: python -m pytest\n'
    replacement = '      - name: Compile package and maintained scripts\n        run: python -m compileall -q src scripts\n' + marker
    if "Compile package and maintained scripts" not in test:
        if marker not in test:
            raise RuntimeError("test workflow pytest marker not found")
        test = test.replace(marker, replacement, 1)
    write(".github/workflows/test.yml", test)


def main() -> None:
    patch_generators()
    patch_unified_figure_build()
    patch_audit()
    patch_makefile()
    patch_verifier()
    patch_script_docs()
    patch_reproducibility_guide()
    patch_root_readme()
    write_workflows()
    print("reproducibility hardening integrated")


if __name__ == "__main__":
    main()
