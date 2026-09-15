"""Audit the completed P92 publication migration.

The P91 to P92 reader-surface migration has already been applied on the P92
feature branch. This retained helper is intentionally read-only: permanent
publication workflows must never rewrite repository state.

Run with::

    python scripts/promote_p92_public_frontier.py

The command checks the canonical P92 frontier declarations and exits without
modifying any file.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def main() -> None:
    checks = {
        "README.md": (
            "current public theorem frontier is **P92**",
            "proposition_92_exact_global_mixed_prevalence_distance.md",
        ),
        "scripts/verify_repository.py": ('CURRENT_FRONTIER = "P92"',),
        "website/index.html": (
            'id="p92-frontier"',
            "P92 current theorem frontier",
        ),
        "website/plain-language.html": ("current frontier P92",),
        "website/start-here.html": ("current frontier P92",),
        "website/research-map.html": (
            'id="p92-research-map"',
            "d_inf(P_emp, M75) = 1/24",
        ),
        "figures/CURRENT_FRONTIER.md": (
            "Current theorem frontier: P92",
            "d_inf(P_emp, M_75) = 1/24",
        ),
    }

    failures: list[str] = []
    for path, required in checks.items():
        text = _read(path)
        for token in required:
            if token not in text:
                failures.append(f"{path}: missing {token!r}")

    if failures:
        raise RuntimeError(
            "P92 publication migration is incomplete:\n" + "\n".join(failures)
        )

    print("[P92] publication migration is present; no files were modified")


if __name__ == "__main__":
    main()
