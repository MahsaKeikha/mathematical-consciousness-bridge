"""Keep P90 equation provenance on the repository-wide frontier naming contract."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD = "proposition_90_equation_provenance.md"
NEW = "p90_equation_provenance.md"


def patch(path: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    if OLD in text:
        text = text.replace(OLD, NEW)
        target.write_text(text, encoding="utf-8")
    if OLD in target.read_text(encoding="utf-8"):
        raise RuntimeError(f"noncanonical P90 provenance path remains in {path}")


def main() -> None:
    patch("scripts/promote_p90_public_frontier.py")
    patch("scripts/advance_p90_publication_contracts.py")
    print("P90 provenance paths aligned with frontier contract")


if __name__ == "__main__":
    main()
