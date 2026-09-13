"""Normalize stale current-frontier wording after the P88 reader promotion.

Historical P87 theorem material remains valid, but no reader-facing page may call
P87 the current frontier once the canonical repository frontier is P88.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEBSITE = ROOT / "website"
STALE = "current P87 frontier"
CURRENT = "current P88 frontier"


def main() -> None:
    changed: list[str] = []
    offenders: list[str] = []

    for path in sorted(WEBSITE.glob("*.html")):
        text = path.read_text(encoding="utf-8")
        if STALE in text:
            text = text.replace(STALE, CURRENT)
            path.write_text(text, encoding="utf-8")
            changed.append(path.name)
        if STALE in path.read_text(encoding="utf-8"):
            offenders.append(path.name)

    if offenders:
        raise RuntimeError(f"stale P87 current-frontier wording remains: {offenders}")

    print(
        "[reader-frontier] normalized stale current-P87 wording to P88 in: "
        + (", ".join(changed) if changed else "no files")
    )


if __name__ == "__main__":
    main()
