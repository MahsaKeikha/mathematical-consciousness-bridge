"""Repair changelog and temporary P94 migration-source contracts for PR #156.

This is a temporary migration helper. The pre phase reconstructs the missing
P85 through P93 changelog history before P94 promotion. The post phase demotes
the former P93 current heading after P94 has been prepended, leaves exactly one
current frontier heading at the top of CHANGELOG.md, and converts two LaTeX
Markdown literals in the temporary migration scripts to raw Python strings.

Delete this helper together with the one-run P94 promotion workflow after the
exact promoted head is validated.
"""

from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHANGELOG = ROOT / "CHANGELOG.md"
P93_TOP = "# Unreleased research frontier - P93\n"
P94_TOP = "# Unreleased research frontier - P94\n"
P84_TOP = "# Unreleased research frontier - P84\n"

P85_TO_P93 = """# Unreleased research frontier - P93

- Added Proposition 93, Localized Finite-Sample Sign-Coherence Rejection.
- Localized the P92 nonlinear sign-coherence witness to the seven observable cells entering its three determinants.
- Combined a simultaneous seven-cell Hoeffding event with the exact P92 sign-stability radii and P79 rational certification.
- Certified the 95 percent mathematical crossing at n = 1623 and the first exact denominator-24 replication at n = 1632.
- Kept non-rejection explicitly inconclusive and preserved the open physical-to-experiential bridge boundary.
- Kept formal release v0.82.0 separate from the advancing theorem frontier.

### P92 predecessor frontier

- Added Proposition 92, Exact Global Mixed-Prevalence Distance.
- Proved the three-determinant sign-coherence obstruction for the full P75 family and closed the established witness at exact L-infinity distance 1/24.

### P91 predecessor frontier

- Added Proposition 91, Mixed-Prevalence Rank-Two Flattening Separation.
- Extended nonlinear separation beyond the P90 prevalence restriction and certified 1/42 < d_inf(P_emp, M75) <= 1/24 on the established witness.

### P90 predecessor frontier

- Added Proposition 90, Exact Nonlinear Rank-One Slice Separation.
- Moved beyond the complete P89 linear envelope with an exact nonlinear slice determinant certificate attaining L90 = 5/72 on the strict P75 witness.

### P89 predecessor frontier

- Added Proposition 89, Complete Linear Parity-Functional Duality Certificate.
- Removed finite coefficient-radius and support restrictions for the declared eleven-coordinate linear parity-functional class and matched lower and upper certificates at 5/168.

### P88 predecessor frontier

- Added Proposition 88, Exact Radius-Three Bounded Primitive Four-Event Projection-Parity Functional Certificate.
- Expanded the P87 coefficient radius to three and strengthened the established exact witness from 1/96 to 1/64.

### P87 predecessor frontier

- Added Proposition 87, Exact Bounded Primitive Four-Event Projection-Parity Functional Certificate.
- Exhausted primitive four-event coefficient vectors with absolute coefficients at most two and strengthened the established witness to 1/96.

### P86 predecessor frontier

- Added Proposition 86, Exact Minimally Weighted Four-Event Projection-Parity Functional Certificate.
- Added the primitive coefficient-magnitude family {1,1,1,2} and obtained the strict exact witness L85 = 0 < L86 = 1/192.

### P85 predecessor frontier

- Added Proposition 85, Exact Three-Event Projection-Parity Functional Certificate.
- Added 660 sign-normalized three-event functionals and an exact strict witness with L84 = 0 < L85 = 1/32.

"""


def read() -> str:
    return CHANGELOG.read_text(encoding="utf-8")


def write(text: str) -> None:
    CHANGELOG.write_text(text, encoding="utf-8")


def replace_once_in_file(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if new in text:
        return
    if text.count(old) != 1:
        raise RuntimeError(f"{path.relative_to(ROOT)}: expected one {old!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def repair_python_latex_literals() -> None:
    replace_once_in_file(
        ROOT / "scripts" / "promote_p94_public_frontier.py",
        "after = '''## P94: finite-range dependent sign-coherence rejection",
        "after = r'''## P94: finite-range dependent sign-coherence rejection",
    )
    replace_once_in_file(
        ROOT / "scripts" / "repair_p94_reader_contracts.py",
        'section = """## Current theorem frontier: P94',
        'section = r"""## Current theorem frontier: P94',
    )
    print("[P94] temporary LaTeX migration literals are raw and lint-safe")


def repair_pre() -> None:
    text = read()
    if text.startswith(P93_TOP):
        print("[P94] changelog baseline already synchronized to P93")
        return
    if not text.startswith(P84_TOP):
        raise RuntimeError("CHANGELOG.md is neither the expected P84 legacy baseline nor synchronized P93")

    historical = text.replace(P84_TOP, "### P84 predecessor frontier\n", 1)
    write(P85_TO_P93 + historical)

    repaired = read()
    if not repaired.startswith(P93_TOP):
        raise RuntimeError("CHANGELOG.md did not advance to the P93 baseline")
    for number in range(85, 94):
        if f"P{number}" not in repaired:
            raise RuntimeError(f"CHANGELOG.md is missing reconstructed P{number} history")
    print("[P94] changelog baseline reconstructed through P93")


def repair_post() -> None:
    text = read()
    if not text.startswith(P94_TOP):
        raise RuntimeError("CHANGELOG.md is not promoted to P94")

    if P93_TOP in text:
        if text.count(P93_TOP) != 1:
            raise RuntimeError("CHANGELOG.md contains duplicate P93 current headings")
        text = text.replace(P93_TOP, "### P93 predecessor frontier\n", 1)
        write(text)

    final = read()
    if not final.startswith(P94_TOP):
        raise RuntimeError("CHANGELOG.md lost the P94 current heading")
    if P93_TOP in final:
        raise RuntimeError("CHANGELOG.md still contains a second current P93 heading")
    if final.count("# Unreleased research frontier - P94") != 1:
        raise RuntimeError("CHANGELOG.md must contain exactly one P94 current heading")

    repair_python_latex_literals()
    print("[P94] changelog promotion contract normalized")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("phase", choices=("pre", "post"))
    args = parser.parse_args()
    if args.phase == "pre":
        repair_pre()
    else:
        repair_post()


if __name__ == "__main__":
    main()
