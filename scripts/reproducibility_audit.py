"""Run the repository's strongest local reproducibility audit.

This command is intended for a fresh, clean clone after installing the development
and pinned figure dependencies. It checks syntax/importability, theorem tests,
static analysis, typography normalization, repository structure, deterministic
figure regeneration, and byte-level idempotence of the generated atlases.

Run from the repository root with::

    python -m pip install -e ".[dev]"
    python -m pip install -r requirements-figures.txt
    python scripts/reproducibility_audit.py

The command intentionally uses only local files after dependencies are installed.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib
import importlib.metadata
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERATED_DIRS = (
    ROOT / "docs" / "figures" / "quantitative",
    ROOT / "docs" / "figures" / "quantum",
)
PINNED_RUNTIME = {
    "matplotlib": "3.11.2",
    "numpy": "2.5.3",
}


def _run(*args: str) -> None:
    command = [sys.executable, *args]
    print("[reproduce]", " ".join(command))
    subprocess.run(command, cwd=ROOT, check=True)


def _run_external(*args: str) -> None:
    print("[reproduce]", " ".join(args))
    subprocess.run(args, cwd=ROOT, check=True)


def _git_status() -> str:
    result = subprocess.run(
        ["git", "status", "--porcelain", "--untracked-files=all"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def _require_clean_tree(label: str) -> None:
    status = _git_status()
    if status:
        print(f"[reproduce] working tree changed after {label}:")
        print(status)
        subprocess.run(["git", "diff", "--stat"], cwd=ROOT, check=False)
        subprocess.run(["git", "diff"], cwd=ROOT, check=False)
        raise RuntimeError(
            f"reproducibility failure: {label} did not preserve a clean checkout"
        )


def _hash_generated_tree() -> dict[str, str]:
    digests: dict[str, str] = {}
    for directory in GENERATED_DIRS:
        for path in sorted(directory.rglob("*")):
            if not path.is_file():
                continue
            relative = path.relative_to(ROOT).as_posix()
            digests[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
    return digests


def _verify_pinned_figure_environment() -> None:
    failures: list[str] = []
    for distribution, expected in PINNED_RUNTIME.items():
        try:
            actual = importlib.metadata.version(distribution)
        except importlib.metadata.PackageNotFoundError:
            failures.append(f"{distribution} is not installed")
            continue
        if actual != expected:
            failures.append(f"{distribution}=={actual}, expected {expected}")
    if failures:
        raise RuntimeError(
            "publication figure environment is not pinned correctly; run "
            "`python -m pip install -r requirements-figures.txt`.\n"
            + "\n".join(failures)
        )
    print("[reproduce] pinned publication figure environment verified")


def _verify_package_import() -> None:
    module = importlib.import_module("consciousness_bridge")
    if module is None:
        raise RuntimeError("failed to import consciousness_bridge")
    print("[reproduce] package import verified")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the end-to-end local reproducibility audit."
    )
    parser.add_argument(
        "--skip-tests",
        action="store_true",
        help="skip pytest and Ruff while retaining deterministic artifact checks",
    )
    args = parser.parse_args()

    if sys.version_info < (3, 10):
        raise RuntimeError("Python 3.10 or newer is required")

    _require_clean_tree("audit start")
    _verify_pinned_figure_environment()
    _run_external("git", "--version")
    _run("-m", "compileall", "-q", "src", "scripts")
    _verify_package_import()

    if not args.skip_tests:
        _run("-m", "pytest")
        _run("-m", "ruff", "check", ".")

    _run("scripts/normalize_typography.py")
    _require_clean_tree("typography normalization")

    _run("scripts/verify_repository.py")
    _run("scripts/generate_all_figures.py")
    _require_clean_tree("first complete figure regeneration")
    first = _hash_generated_tree()

    _run("scripts/generate_all_figures.py")
    _require_clean_tree("second complete figure regeneration")
    second = _hash_generated_tree()
    if first != second:
        changed = sorted(
            key for key in set(first) | set(second) if first.get(key) != second.get(key)
        )
        raise RuntimeError(
            "generated figure tree is not byte-idempotent: " + ", ".join(changed)
        )

    _run("scripts/verify_repository.py")
    print(
        "[reproduce] PASS: tests/static checks, repository verification, "
        "and deterministic generated artifacts are reproducible from a clean clone"
    )


if __name__ == "__main__":
    main()
