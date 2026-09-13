"""One-time P87 reader/publication consistency cleanup.

This script repairs the small set of stale P86 reader/citation strings exposed by
the full P87 publication test run. It is intentionally deterministic and is
removed by the guarded cleanup workflow after validation succeeds.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace(path: str, replacements: tuple[tuple[str, str], ...]) -> None:
    text = read(path)
    for old, new in replacements:
        text = text.replace(old, new)
    write(path, text)


def update_citations() -> None:
    replace(
        "CITATION.cff",
        (("Current documented theorem frontier: P86.", "Current documented theorem frontier: P87."),),
    )

    citation = read("CITATION.md")
    if "Current documented theorem frontier: **P87**" not in citation:
        citation += """

## Current theorem frontier

The current documented theorem frontier is **P87**. Proposition 87 completes the sign-normalized primitive nonzero four-event coefficient box with `0 < |c_i| <= 2`, auditing 39,600 exact functionals. On the stored exact rational witness, the complete P86 certificate is `1/192` and P87 certifies `1/96`. This is a conditional model-separation result for the declared P75 family, not an identification or definition of consciousness.
"""
    write("CITATION.md", citation)


def update_reader_surfaces() -> None:
    replace(
        "README.md",
        (
            ("P1 through P86 with explicit dependency branches", "P1 through P87 with explicit dependency branches"),
            ("P19-P24, P71-P86", "P19-P24, P71-P87"),
            ("Later P61-P70 and P71-P86 are separate continuations", "Later P61-P70 and P71-P87 are separate continuations"),
        ),
    )

    start_here = read("START_HERE.md")
    if "docs/proposition_87_" not in start_here:
        start_here += """

## Current frontier: P87

P87 is the current exact theorem frontier. It exhausts every sign-normalized primitive nonzero four-event integer coefficient pattern with `0 < |c_i| <= 2` across the eleven canonical even-parity observables. The complete family contains 39,600 exact functionals and gives the exact strict hierarchy witness `L86 = 1/192 < L87 = 1/96` on the stored rational example.

- [P87 proof](docs/proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md)
- [P87 equation provenance](docs/p87_equation_provenance.md)
- [P87 implementation](src/consciousness_bridge/bounded_primitive_quad_projection_parity_functional_separation.py)
- [P87 tests](tests/test_bounded_primitive_quad_projection_parity_functional_separation.py)
- [P87 figure](docs/figures/p87_exact_bounded_primitive_quad_projection_parity.svg)

The result remains conditional on the declared P75 target-measurement family. It does not identify the latent state with consciousness, validate an alternative ontology, or close the physical-to-experiential bridge.
"""
    write("START_HERE.md", start_here)

    replace(
        "docs/detailed_proposition_record.md",
        (("## Complete P1 to P86 chronology", "## Complete P1 to P87 chronology"),),
    )

    replace(
        "website/index.html",
        (
            ("Explore all 86 results", "Explore all 87 results"),
            ("<strong>86</strong><span>proposition-level results</span>", "<strong>87</strong><span>proposition-level results</span>"),
            ("The 86-result program", "The 87-result program"),
            ("The 86 results form several dependency branches.", "The 87 results form several dependency branches."),
            ("all 86 propositions", "all 87 propositions"),
            ("P71-P86", "P71-P87"),
            ("P75-P86", "P75-P87"),
        ),
    )

    replace(
        "website/start-here.html",
        (
            ("Explore all 86 results", "Explore all 87 results"),
            ("P71-P86", "P71-P87"),
            ("P75-P86", "P75-P87"),
        ),
    )

    implementation_sentence = (
        "P73-P87 build a continuous chain from channel recovery to certified model-family separation."
    )
    implementation_text = read("website/implementation.html")
    if "P77-P87" not in implementation_text:
        implementation_text = implementation_text.replace(
            implementation_sentence,
            implementation_sentence
            + " The certified full-law separation subchain P77-P87 progressively strengthens exact rejection certificates while preserving the same declared target-measurement family.",
            1,
        )
    write("website/implementation.html", implementation_text)


def update_legacy_test_contract() -> None:
    path = "tests/test_p84_reader_presentation.py"
    text = read(path)
    old = '''    assert "Stage 06 · P73-P86" in implementation
    assert implementation.count(
        "P73-P86 build a continuous chain from channel recovery to certified model-family separation."
    ) == 1
'''
    new = '''    frontier = max(
        int(path.name.split("_")[1])
        for path in (ROOT / "docs").glob("proposition_*.md")
    )
    target_range = f"P73-P{frontier}"
    assert f"Stage 06 · {target_range}" in implementation
    assert implementation.count(
        f"{target_range} build a continuous chain from channel recovery to certified model-family separation."
    ) == 1
'''
    if old in text:
        text = text.replace(old, new, 1)
    elif "target_range = f\"P73-P{frontier}\"" not in text:
        raise RuntimeError("could not locate the P84 stage-range contract")
    write(path, text)


def main() -> None:
    update_citations()
    update_reader_surfaces()
    update_legacy_test_contract()
    print("[p87-consistency] repaired stale P86 reader/citation contracts")


if __name__ == "__main__":
    main()
