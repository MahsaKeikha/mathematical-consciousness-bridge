"""Repair narrow P92 migration contracts before canonical synchronization.

This helper exists only for the P92 branch migration. Delete it together with
the branch-only write workflow before merging P92 to main.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def patch_homepage() -> None:
    path = "website/index.html"
    text = read(path)
    replacements = (
        (
            "<strong>91</strong><span>proposition-level results</span>",
            "<strong>92</strong><span>proposition-level results</span>",
        ),
        (
            "P91 current theorem frontier · v0.82.0",
            "P92 current theorem frontier · v0.82.0",
        ),
        ("Explore all 91 results", "Explore all 92 results"),
        (
            "Current record:</strong> 91 proposition-level results through P91",
            "Current record:</strong> 92 proposition-level results through P92",
        ),
        ("The 91-result program", "The 92-result program"),
        ("all 91 propositions", "all 92 propositions"),
    )
    for old, new in replacements:
        text = text.replace(old, new)
    write(path, text)


def patch_visual_atlas() -> None:
    path = "website/visual-atlas.html"
    text = read(path)
    text = text.replace(
        "Historical mixed-prevalence frontier · P91",
        "Previous theorem frontier · P91",
    )
    text = text.replace(
        "Current theorem frontier · P91",
        "Previous theorem frontier · P91",
    )
    write(path, text)


def patch_svg_accessibility() -> None:
    path = "docs/figures/p92_exact_global_mixed_prevalence_distance.svg"
    text = read(path)
    old = (
        '<desc id="desc">Exact nonlinear sign-coherence certificate proving the '
        'full P75 L-infinity distance is one over twenty-four.</desc>'
    )
    new = (
        '<desc id="desc">This theorem figure compares three exact empirical '
        'conditional determinants with their sign-stability radii, states the '
        'universal nonnegative determinant-product constraint for the full P75 '
        'mixture family, and shows the matching exact distance boundary at one '
        'over twenty-four. Scientific status: conditional model-separation '
        'theorem only; it does not identify consciousness or establish a '
        'replacement ontology.</desc>'
    )
    if old not in text and new not in text:
        raise RuntimeError("P92 SVG description anchor changed unexpectedly")
    text = text.replace(old, new)
    write(path, text)


def patch_machine_citation() -> None:
    for path in ("CITATION.cff", "CITATION.bib", "CITATION.md"):
        text = read(path)
        text = text.replace(
            "Current documented theorem frontier: P91",
            "Current documented theorem frontier: P92",
        )
        text = text.replace(
            "current documented frontier, P91",
            "current documented frontier, P92",
        )
        write(path, text)


def patch_implementation_range() -> None:
    path = "website/implementation.html"
    text = read(path).replace("P73-P91", "P73-P92")
    write(path, text)


def main() -> None:
    patch_homepage()
    patch_visual_atlas()
    patch_svg_accessibility()
    patch_machine_citation()
    patch_implementation_range()
    print("[P92] branch migration contracts repaired")


if __name__ == "__main__":
    main()
