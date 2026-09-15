"""Repair exact generated P94 test literals during the one-run publication migration.

Temporary helper for PR #156. Delete it after the promoted P94 publication head
is validated and before merge.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "tests" / "test_p94_reader_surface_coherence.py"


def main() -> None:
    text = PATH.read_text(encoding="utf-8")
    old = '    assert "-\\frac{2145}{281474976710656}" in proof\n'
    new = '    assert r"-\\frac{2145}{281474976710656}" in proof\n'
    if text.count(old) != 1:
        raise RuntimeError(
            "expected exactly one generated P94 determinant-product assertion"
        )
    PATH.write_text(text.replace(old, new, 1), encoding="utf-8")
    print("[P94] generated reader-contract escape repaired")


if __name__ == "__main__":
    main()
