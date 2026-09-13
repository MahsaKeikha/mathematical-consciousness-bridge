"""Synchronize canonical reader-facing P88 frontier wording and audit guides.

Historical P87 theorem material remains valid, but no reader-facing surface may
call P87 the current frontier once the canonical repository frontier is P88.
The canonical roadmap, navigation, and reproducibility guides are synchronized
here so the publication contract remains reproducible and idempotent.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEBSITE = ROOT / "website"
DOCS = ROOT / "docs"
STALE = "current P87 frontier"
CURRENT = "current P88 frontier"


def _replace_required(text: str, old: str, new: str, label: str) -> str:
    if old in text:
        return text.replace(old, new)
    if new in text:
        return text
    raise RuntimeError(f"{label}: expected source text is missing")


def _write_if_changed(path: Path, text: str, changed: list[str]) -> None:
    original = path.read_text(encoding="utf-8")
    if text != original:
        path.write_text(text, encoding="utf-8")
        changed.append(str(path.relative_to(ROOT)))


def _sync_website(changed: list[str]) -> None:
    offenders: list[str] = []
    for path in sorted(WEBSITE.glob("*.html")):
        text = path.read_text(encoding="utf-8")
        _write_if_changed(path, text.replace(STALE, CURRENT), changed)
        if STALE in path.read_text(encoding="utf-8"):
            offenders.append(path.name)
    if offenders:
        raise RuntimeError(f"stale P87 current-frontier wording remains: {offenders}")


def _sync_theorem_roadmap(changed: list[str]) -> None:
    path = DOCS / "theorem_roadmap.md"
    text = path.read_text(encoding="utf-8")

    text = _replace_required(
        text,
        "The current documented theorem frontier is **P87**. The proposition record runs from **P1 through P87 with explicit dependency branches**.",
        "The current documented theorem frontier is **P88**. The proposition record runs from **P1 through P88 with explicit dependency branches**.",
        "theorem roadmap frontier declaration",
    )

    p87_dependency = r"&\text{P87: bounded primitive four-event parity functionals complete the nonzero coefficient box with |c_i| <= 2}"
    p88_dependency_line = r"&\text{P88: radius-three bounded primitive four-event parity functionals extend the exact coefficient box to |c_i| <= 3}"
    if p88_dependency_line not in text:
        if p87_dependency not in text:
            raise RuntimeError("theorem roadmap P87 dependency line is missing")
        text = text.replace(
            p87_dependency,
            p87_dependency + r"\\" + "\n" + r"&\Downarrow\\" + "\n" + p88_dependency_line,
            1,
        )

    p87_row = "| [P87](proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md) | complete bounded primitive four-event parity functionals | same-order coefficient-family completion that strictly strengthens P86 | proved conditional computational theorem |"
    p88_row = "| [P88](proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md) | radius-three bounded primitive four-event parity functionals | exact coefficient-radius extension that strictly strengthens P87 on the declared witness | proved conditional computational theorem |"
    if p88_row not in text:
        if p87_row not in text:
            raise RuntimeError("theorem roadmap P87 index row is missing")
        text = text.replace(p87_row, p87_row + "\n" + p88_row, 1)

    if "## P88: exact radius-three bounded primitive four-event parity-functional separation" not in text:
        p87_boundary = (
            "P87 remains a conditional model-separation theorem for the declared P75 family. "
            "It does not identify the latent state with consciousness or close the physical-to-experiential bridge.\n\n"
            "## After P87\n\n"
            "The next frontier should not be inferred merely by increasing functional order. Any P88 claim must close a separately stated mathematical or scientific gap and must include a strict or otherwise informative certificate that is not already implied by P86."
        )
        p88_boundary = (
            "P87 remains a conditional model-separation theorem for the declared P75 family. "
            "It does not identify the latent state with consciousness or close the physical-to-experiential bridge.\n\n"
            "## P88: exact radius-three bounded primitive four-event parity-functional separation\n\n"
            "P88 extends P87 from the nonzero primitive coefficient box `|c_i| <= 2` to `|c_i| <= 3`. "
            "Across the eleven canonical P83 parity coordinates there are 632 sign-normalized primitive coefficient patterns per four-event subset and 208,560 exact functionals in total. "
            "Every functional retains the common-parameter, multi-affine P75 box structure, so the branchwise interval remains exact at endpoint vertices.\n\n"
            "For the strict P88 witness, the coefficient pattern `(1,-1,-3,2)` has empirical value `-11/8`, exact P75 interval `[-1,2]`, interval gap `3/8`, centering constant `-1`, and centered coefficient norm `24`. Therefore\n\n"
            "\\[\n"
            "\\boxed{L_{85}=0<L_{86}=1/192<L_{87}=1/96<L_{88}=1/64.}\n"
            "\\]\n\n"
            "- Proof: [P88](proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md)\n"
            "- Provenance: [p88_equation_provenance.md](p88_equation_provenance.md)\n"
            "- Figure: [P88 radius-three certificate](figures/p88_exact_radius_three_bounded_primitive_quad_projection_parity.svg)\n"
            "- Source: [`radius_three_bounded_primitive_quad_projection_parity_functional_separation.py`](../src/consciousness_bridge/radius_three_bounded_primitive_quad_projection_parity_functional_separation.py)\n"
            "- Tests: [`test_radius_three_bounded_primitive_quad_projection_parity_functional_separation.py`](../tests/test_radius_three_bounded_primitive_quad_projection_parity_functional_separation.py)\n\n"
            "P88 remains a conditional model-separation theorem for the declared P75 target-measurement family. It does not identify the latent state with consciousness, establish nonphysicality, validate an alternative model, or close the physical-to-experiential bridge.\n\n"
            "## After P88\n\n"
            "The next frontier should not be inferred merely by increasing functional order. Any P89 claim must close a separately stated mathematical or scientific gap and must include a strict or otherwise informative certificate that is not already implied by P88."
        )
        if p87_boundary not in text:
            raise RuntimeError("theorem roadmap P87 future-boundary block is missing")
        text = text.replace(p87_boundary, p88_boundary, 1)

    text = text.replace(
        "After P87, the target-side chain has a substantially clearer scientific burden:",
        "After P88, the target-side chain has a substantially clearer scientific burden:",
    )
    text = text.replace("continuation beyond P87", "continuation beyond P88")
    text = text.replace(
        "with a certificate not already implied by P86, or an observable-specific finite-sample rejection theorem that propagates uncertainty through a selected P86 score",
        "with a certificate not already implied by P88, or an observable-specific finite-sample rejection theorem that propagates uncertainty through a selected P88 score",
    )

    _write_if_changed(path, text, changed)


def _sync_research_navigation(changed: list[str]) -> None:
    path = DOCS / "research_navigation.md"
    text = path.read_text(encoding="utf-8")
    replacements = (
        ("**Results:** P75 through P87", "**Results:** P75 through P88"),
        (
            "**Current frontier:** [P87: Exact Bounded Primitive Four Event Projection Parity Functional Certificate](proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md)",
            "**Current frontier:** [P88: Exact Radius-Three Bounded Primitive Four Event Projection Parity Functional Certificate](proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md)",
        ),
        ("For P87:", "For P88:"),
        ("[P87 proposition](proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md)", "[P88 proposition](proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md)"),
        ("[P87 provenance](p87_equation_provenance.md)", "[P88 provenance](p88_equation_provenance.md)"),
        ("[`bounded_primitive_quad_projection_parity_functional_separation.py`](../src/consciousness_bridge/bounded_primitive_quad_projection_parity_functional_separation.py)", "[`radius_three_bounded_primitive_quad_projection_parity_functional_separation.py`](../src/consciousness_bridge/radius_three_bounded_primitive_quad_projection_parity_functional_separation.py)"),
        ("[`test_bounded_primitive_quad_projection_parity_functional_separation.py`](../tests/test_bounded_primitive_quad_projection_parity_functional_separation.py)", "[`test_radius_three_bounded_primitive_quad_projection_parity_functional_separation.py`](../tests/test_radius_three_bounded_primitive_quad_projection_parity_functional_separation.py)"),
        ("[P87 theorem figure](figures/p87_exact_bounded_primitive_quad_projection_parity.svg)", "[P88 theorem figure](figures/p88_exact_radius_three_bounded_primitive_quad_projection_parity.svg)"),
        (
            "P87 is a conditional model separation result for the declared P75 family. It does not identify the latent state with consciousness or close the final bridge from physical description to experience.",
            "P88 is a conditional model separation result for the declared P75 target-measurement family. It does not identify the latent state with consciousness, establish nonphysicality, or close the final bridge from physical description to experience.",
        ),
        ("P74 through P87", "P74 through P88"),
        ("P71 through P87", "P71 through P88"),
        ("the full 87 proposition index", "the full 88 proposition index"),
    )
    for old, new in replacements:
        text = _replace_required(text, old, new, f"research navigation replacement: {old[:40]}")
    _write_if_changed(path, text, changed)


def _sync_reproducibility(changed: list[str]) -> None:
    path = DOCS / "reproducibility.md"
    text = path.read_text(encoding="utf-8")
    text = _replace_required(
        text,
        "| Run only the current P87 theorem checks | focused P87 commands below |",
        "| Run only the current P88 theorem checks | focused P88 commands below |",
        "reproducibility route table",
    )

    section = """## 5. Focused audit of the current P88 frontier

The current theorem frontier is **P88**.

Its direct technical record is:

```text
docs/proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md
docs/p88_equation_provenance.md
src/consciousness_bridge/radius_three_bounded_primitive_quad_projection_parity_functional_separation.py
tests/test_radius_three_bounded_primitive_quad_projection_parity_functional_separation.py
docs/figures/p88_exact_radius_three_bounded_primitive_quad_projection_parity.svg
figures/manifest.json
```

Run the focused theorem and figure publication checks with:

```bash
python -m pytest \\
  tests/test_radius_three_bounded_primitive_quad_projection_parity_functional_separation.py \\
  tests/test_figure_publication_sync.py \\
  tests/test_p88_reader_surface_coherence.py
```

P88 extends the sign-normalized primitive nonzero four-event coefficient family to coefficient magnitudes at most 3. The exact family contains 208,560 functionals across the 330 four-event subsets of the eleven canonical P83 parity coordinates.

For the published strict witness, the coefficient pattern is `(1,-1,-3,2)`. The empirical functional value is

\[
-\frac{11}{8},
\]

while the exact P75 box interval is

\[
[-1,2],
\]

giving an exact functional gap

\[
\frac{3}{8}.
\]

The centering constant is `-1` and the centered coefficient norm is 24, which yields the P88 empirical full-law lower bound

\[
\frac{1}{64}.
\]

On this strict witness the certified hierarchy is

\[
L_{85}=0<L_{86}=\frac{1}{192}<L_{87}=\frac{1}{96}<L_{88}=\frac{1}{64}.
\]

These are conditional model-separation results for the declared P75 target-measurement family. They do not identify the latent state with consciousness, establish nonphysicality, or complete the physical-to-experiential bridge.
"""
    pattern = re.compile(
        r"## 5\. Focused audit of the current P87 frontier\n.*?\n---\n\n## 6\.",
        re.DOTALL,
    )
    if pattern.search(text):
        text = pattern.sub(section + "\n---\n\n## 6.", text, count=1)
    elif "## 5. Focused audit of the current P88 frontier" not in text:
        raise RuntimeError("reproducibility focused-audit section is missing")

    text = text.replace(
        "python -m pytest tests/test_bounded_primitive_quad_projection_parity_functional_separation.py",
        "python -m pytest tests/test_radius_three_bounded_primitive_quad_projection_parity_functional_separation.py",
    )
    text = text.replace(
        "docs/figures/p87_exact_bounded_primitive_quad_projection_parity_functional.svg",
        "docs/figures/p88_exact_radius_three_bounded_primitive_quad_projection_parity.svg",
    )
    _write_if_changed(path, text, changed)


def _assert_canonical_state() -> None:
    roadmap = (DOCS / "theorem_roadmap.md").read_text(encoding="utf-8")
    navigation = (DOCS / "research_navigation.md").read_text(encoding="utf-8")
    reproducibility = (DOCS / "reproducibility.md").read_text(encoding="utf-8")

    required = {
        "theorem roadmap": (
            "The current documented theorem frontier is **P88**.",
            r"\text{P88:",
            "## P88:",
            "## After P88",
        ),
        "research navigation": (
            "The public theorem frontier is **P88**.",
            "**Results:** P75 through P88",
            "For P88:",
            "the full 88 proposition index",
        ),
        "reproducibility": (
            "The current public theorem frontier is **P88**.",
            "## 5. Focused audit of the current P88 frontier",
            "The current theorem frontier is **P88**.",
            "208,560 functionals",
        ),
    }
    texts = {
        "theorem roadmap": roadmap,
        "research navigation": navigation,
        "reproducibility": reproducibility,
    }
    for label, markers in required.items():
        for marker in markers:
            if marker not in texts[label]:
                raise RuntimeError(f"{label}: missing canonical P88 marker {marker!r}")

    stale_markers = (
        "The current documented theorem frontier is **P87**.",
        "**Current frontier:** [P87:",
        "For P87:",
        "The current theorem frontier is **P87**.",
        "## After P87",
    )
    combined = roadmap + "\n" + navigation + "\n" + reproducibility
    for marker in stale_markers:
        if marker in combined:
            raise RuntimeError(f"stale canonical frontier marker remains: {marker}")


def main() -> None:
    changed: list[str] = []
    _sync_website(changed)
    _sync_theorem_roadmap(changed)
    _sync_research_navigation(changed)
    _sync_reproducibility(changed)
    _assert_canonical_state()
    print(
        "[reader-frontier] synchronized canonical P88 publication surfaces: "
        + (", ".join(changed) if changed else "no files")
    )


if __name__ == "__main__":
    main()
