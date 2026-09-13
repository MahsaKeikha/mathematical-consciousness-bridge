"""Promote the proved P88 result across research publication surfaces only.

This one-shot migration deliberately does not edit anything under ``website/``.
It is safe to re-run: every insertion is guarded and every replacement checks
its source marker before writing.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    target = ROOT / path
    target.write_text(text, encoding="utf-8")
    print(f"[p88-promote] updated {path}")


def replace_once(text: str, old: str, new: str, *, label: str) -> str:
    if new in text:
        return text
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one source marker, found {count}")
    return text.replace(old, new, 1)


def promote_verifier() -> None:
    path = "scripts/verify_repository.py"
    text = read(path)
    text = replace_once(
        text,
        'CURRENT_FRONTIER = "P87"',
        'CURRENT_FRONTIER = "P88"',
        label="verifier frontier",
    )
    if '"docs/figures/p88_exact_radius3_bounded_primitive_quad_projection_parity.svg"' not in text:
        marker = '    "docs/figures/p87_exact_bounded_primitive_quad_projection_parity.svg",\n'
        insertion = marker + '    "docs/figures/p88_exact_radius3_bounded_primitive_quad_projection_parity.svg",\n'
        text = replace_once(text, marker, insertion, label="verifier P88 figure")
    if '"docs/proposition_88_exact_radius3_bounded_primitive_quad_projection_parity_functional.md"' not in text:
        marker = '    "docs/p87_equation_provenance.md",\n'
        insertion = (
            marker
            + '    "docs/proposition_88_exact_radius3_bounded_primitive_quad_projection_parity_functional.md",\n'
            + '    "docs/p88_equation_provenance.md",\n'
        )
        text = replace_once(text, marker, insertion, label="verifier P88 docs")
    write(path, text)


def promote_figure_catalog() -> None:
    path = "docs/figure_catalog.md"
    text = read(path)
    text = text.replace(
        "**Current catalog:** 145 SVG figures: 17 architecture/conceptual visuals, 18 foundational quantum-physics visuals, 70 proposition/theorem visuals, and 40 quantitative figures.",
        "**Current catalog:** 146 SVG figures: 17 architecture/conceptual visuals, 18 foundational quantum-physics visuals, 71 proposition/theorem visuals, and 40 quantitative figures.",
    )
    if "P88 Radius-3 Bounded Primitive Four-Event Parity Certificate" not in text:
        marker = "\n## Quantitative physics and mathematics figures"
        row = (
            "\n| [P88 Radius-3 Bounded Primitive Four-Event Parity Certificate]"
            "(figures/p88_exact_radius3_bounded_primitive_quad_projection_parity.svg) | "
            "What this figure shows: Proposition 88 completes the next primitive four-event coefficient box with nonzero integer coefficients of absolute value at most three. "
            "How to read it: P87's 120 radius-two patterns expand to 632 sign-normalized primitive radius-three patterns per four-event subset, for 208,560 exact functionals total. "
            "Main takeaway: on the shared rational witness the strongest P88 functional has empirical value -11/8, exact P75 interval [-1,2], gap 3/8, centered coefficient norm 24, and certified full-law L-infinity lower bound 1/64, giving L85=0 < L86=1/192 < L87=1/96 < L88=1/64. | "
            "this is a conditional exact model-separation theorem for the declared P75 family. It does not identify a latent variable with consciousness, establish nonphysicality, validate another ontology, or solve the physical-to-experiential bridge. | "
            "[Proposition 88](proposition_88_exact_radius3_bounded_primitive_quad_projection_parity_functional.md) |\n"
        )
        if marker not in text:
            raise RuntimeError("figure catalog quantitative-section marker missing")
        text = text.replace(marker, row + marker, 1)
    write(path, text)


def promote_theorem_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    text = replace_once(
        text,
        "The current documented theorem frontier is **P87**. The proposition record runs from **P1 through P87 with explicit dependency branches**. P71-P87 return to the core P19 bridge-sufficiency lineage; they do not extend the P61-P70 calibration branch.",
        "The current documented theorem frontier is **P88**. The proposition record runs from **P1 through P88 with explicit dependency branches**. P71-P88 return to the core P19 bridge-sufficiency lineage; they do not extend the P61-P70 calibration branch.",
        label="roadmap opening",
    )
    p87_map = r"&\text{P87: bounded primitive four-event parity functionals complete the nonzero coefficient box with |c_i| <= 2}"
    if r"P88: radius-3 bounded primitive" not in text:
        replacement = (
            p87_map
            + r"\\"
            + "\n&\\Downarrow\\\\\n"
            + r"&\text{P88: radius-3 bounded primitive four-event parity functionals complete the nonzero coefficient box with |c_i| <= 3}"
        )
        text = replace_once(text, p87_map, replacement, label="roadmap dependency P88")

    if "## P88: radius-3 bounded primitive four-event parity-functional separation" not in text:
        marker = "\n## After P87\n"
        section = r'''
## P88: radius-3 bounded primitive four-event parity-functional separation

P88 asks whether P87's complete primitive radius-two coefficient box already exhausts the useful same-order four-event parity directions. It keeps the event order fixed and enlarges the coefficient alphabet to `{-3,-2,-1,1,2,3}`, retaining only primitive nonzero vectors and quotienting one global sign.

There are

\[
\frac{6^4-2^4-2^4}{2}=632
\]

sign-normalized primitive coefficient patterns per four-event subset. Across the 330 unordered four-event subsets of the eleven canonical P83 parity coordinates, P88 therefore exhausts

\[
330\times632=208{,}560
\]

exact functionals. The same multi-affine endpoint argument used in P87 gives exact rational P75 box intervals, and the same mass-conservation centering transfers a functional mismatch to a sound full-law \(L_\infty\) lower bound.

On the shared exact rational P86/P87 witness, exhaustive P88 enumeration selects

\[
Q=P(H_{\{0,2\}})-P(H_{\{1,3\}})-3P(H_{\{1,2,3\}})+2P(H_{\{0,1,2,3\}}),
\]

with

\[
Q(\widehat p)=-\frac{11}{8},\qquad I_B(Q)=[-1,2],\qquad \Delta_Q=\frac38,\qquad D(Q)=24.
\]

Hence

\[
\boxed{L_{85}=0<L_{86}=\frac1{192}<L_{87}=\frac1{96}<L_{88}=\frac1{64}.}
\]

- Proof: [P88](proposition_88_exact_radius3_bounded_primitive_quad_projection_parity_functional.md)
- Provenance: [p88_equation_provenance.md](p88_equation_provenance.md)
- Figure: [P88 radius-3 bounded primitive certificate](figures/p88_exact_radius3_bounded_primitive_quad_projection_parity.svg)
- Source: [`bounded_primitive_radius3_quad_projection_parity_functional_separation.py`](../src/consciousness_bridge/bounded_primitive_radius3_quad_projection_parity_functional_separation.py)
- Tests: [`test_bounded_primitive_radius3_quad_projection_parity_functional_separation.py`](../tests/test_bounded_primitive_radius3_quad_projection_parity_functional_separation.py)

P88 remains a conditional exact model-separation theorem for the declared P75 family. It does not identify the latent state with consciousness, establish nonphysicality, validate an alternative ontology, or close the physical-to-experiential bridge.
'''
        if marker not in text:
            raise RuntimeError("roadmap After P87 marker missing")
        text = text.replace(marker, "\n" + section.strip() + "\n\n## After P88\n", 1)
        text = text.replace(
            "The next frontier should not be inferred merely by increasing functional order. Any P88 claim must close a separately stated mathematical or scientific gap and must include a strict or otherwise informative certificate that is not already implied by P86.",
            "The next frontier should not be inferred merely by increasing coefficient radius or functional order. Any P89 claim must close a separately stated mathematical or scientific gap and must include a strict or otherwise informative certificate that is not already implied by P88.",
            1,
        )
    write(path, text)


def promote_detailed_record() -> None:
    path = "docs/detailed_proposition_record.md"
    text = read(path)
    text = text.replace("## Complete P1 to P87 chronology", "## Complete P1 to P88 chronology")
    text = text.replace("# Detailed proposition record\n\n## Complete P1 to P87 chronology", "# Detailed proposition record\n\n## Complete P1 to P88 chronology")
    if "**P88**" not in text:
        block = r'''

**P88** keeps the P87 four-event parity order fixed but enlarges the complete primitive integer coefficient box from `0 < |c_i| <= 2` to `0 < |c_i| <= 3`. The six-symbol coefficient alphabet contains 1,296 nonzero four-vectors. The only nonprimitive vectors are the 16 all-even `±2` vectors and the 16 all-`±3` vectors; after removing those and quotienting one global sign, 632 standard primitive coefficient patterns remain per four-event subset. Across the 330 unordered four-event subsets of the eleven canonical parity coordinates, the complete P88 family therefore contains 208,560 exact functionals.

The exact P75 interval calculation remains multi-affine and is certified at common parameter-box vertices. On the shared rational P86/P87 witness, exhaustive P88 search selects coefficients `(1,-1,-3,2)` on `(H02,H13,H123,H0123)`, with empirical value `-11/8`, exact model interval `[-1,2]`, gap `3/8`, centered transfer norm `24`, and lower bound `1/64`. Thus the shared witness gives

\[
L_{85}=0<L_{86}=\frac1{192}<L_{87}=\frac1{96}<L_{88}=\frac1{64}.
\]

Direct P88 proof: [radius-3 bounded primitive four-event parity-functional separation](proposition_88_exact_radius3_bounded_primitive_quad_projection_parity_functional.md). Equation classification: [P88 equation and provenance record](p88_equation_provenance.md). Implementation: [`bounded_primitive_radius3_quad_projection_parity_functional_separation.py`](../src/consciousness_bridge/bounded_primitive_radius3_quad_projection_parity_functional_separation.py). Tests: [`test_bounded_primitive_radius3_quad_projection_parity_functional_separation.py`](../tests/test_bounded_primitive_radius3_quad_projection_parity_functional_separation.py).

P88 is a conditional model-separation theorem for the declared P75 family. It does not identify a latent state with consciousness or close the physical-to-experiential bridge.
'''
        text = text.rstrip() + block + "\n"
    write(path, text)


def promote_equation_map() -> None:
    path = "docs/equation_and_citation_map.md"
    text = read(path)
    if "## P88" not in text:
        block = r'''

## P88: radius-3 bounded primitive four-event parity certificate

P88 inherits the P75 conditional-independence parity identity and P87 exact multi-affine endpoint argument, but enlarges the complete primitive coefficient box to `0 < |c_i| <= 3` at fixed four-event order. The finite family has 632 sign-normalized primitive patterns per subset and 208,560 exact functionals total.

The repository-original exact strict witness is

\[
Q=P(H_{02})-P(H_{13})-3P(H_{123})+2P(H_{0123}),
\]

with

\[
Q(\widehat p)=-\frac{11}{8},\quad I_B(Q)=[-1,2],\quad \Delta_Q=\frac38,\quad D(Q)=24,
\]

and therefore

\[
L_{88}=\frac1{64}>L_{87}=\frac1{96}.
\]

- Direct proof: [P88](proposition_88_exact_radius3_bounded_primitive_quad_projection_parity_functional.md)
- Equation provenance: [P88 provenance](p88_equation_provenance.md)
- Implementation: [`bounded_primitive_radius3_quad_projection_parity_functional_separation.py`](../src/consciousness_bridge/bounded_primitive_radius3_quad_projection_parity_functional_separation.py)
- Regression tests: [`test_bounded_primitive_radius3_quad_projection_parity_functional_separation.py`](../tests/test_bounded_primitive_radius3_quad_projection_parity_functional_separation.py)
'''
        text = text.rstrip() + block + "\n"
    write(path, text)


def promote_citations() -> None:
    for path in ("CITATION.cff", "CITATION.md"):
        text = read(path)
        text = re.sub(r"(?i)(current(?: documented)? theorem frontier(?: is|:)\s*\*{0,2})P87", r"\1P88", text)
        text = re.sub(r"(?i)(theorem frontier(?: is|:)\s*\*{0,2})P87", r"\1P88", text)
        if "P88" not in text:
            text = text.rstrip() + "\n\nCurrent documented theorem frontier: P88. The formal release remains v0.82.0.\n"
        write(path, text)


def promote_reproducibility() -> None:
    path = "docs/reproducibility.md"
    text = read(path)
    text = text.replace("The current theorem frontier is **P87**.", "The current theorem frontier is **P88**.")
    text = text.replace("## 12. Reproduce the current P87 implementation checks directly", "## 12. Reproduce the current P88 implementation checks directly")
    if "test_bounded_primitive_radius3_quad_projection_parity_functional_separation.py" not in text:
        block = """

### P88 exact frontier check

```bash
pytest -q tests/test_bounded_primitive_radius3_quad_projection_parity_functional_separation.py
python scripts/sync_figure_publication.py --check
```

The P88 test exhausts the declared radius-three primitive family and verifies the exact shared-witness value `L88 = 1/64`. The figure synchronization check validates the canonical theorem figure, gateway, and SHA-256 manifest without editing the website.
"""
        text = text.rstrip() + block + "\n"
    write(path, text)


def main() -> None:
    promote_verifier()
    promote_figure_catalog()
    promote_theorem_roadmap()
    promote_detailed_record()
    promote_equation_map()
    promote_citations()
    promote_reproducibility()
    subprocess.run(
        [sys.executable, "scripts/sync_figure_publication.py"],
        cwd=ROOT,
        check=True,
    )
    print("[p88-promote] research surfaces promoted; website untouched")


if __name__ == "__main__":
    main()
