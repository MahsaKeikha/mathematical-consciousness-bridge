"""Remove final stale P90 reader-facing publication residuals before merge."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD_PROVENANCE = "proposition_90_equation_provenance.md"
NEW_PROVENANCE = "p90_equation_provenance.md"
OLD_CURRENT_FIGURE = "docs/figures/p89_complete_linear_parity_duality.svg"
NEW_CURRENT_FIGURE = "docs/figures/p90_exact_nonlinear_rank_one_separation.svg"
AUDIT_HEADING = "## Focused audit of the current P90 frontier"
OLD_CATALOG_COUNT = (
    "**Current catalog:** 147 SVG figures: 17 architecture/conceptual visuals, "
    "18 foundational quantum-physics visuals, 72 proposition/theorem visuals, "
    "and 40 quantitative figures."
)
NEW_CATALOG_COUNT = (
    "**Current catalog:** 148 SVG figures: 17 architecture/conceptual visuals, "
    "18 foundational quantum-physics visuals, 73 proposition/theorem visuals, "
    "and 40 quantitative figures."
)


def clean_reproducibility() -> None:
    path = ROOT / "docs" / "reproducibility.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace(OLD_PROVENANCE, NEW_PROVENANCE)
    text = text.replace(OLD_CURRENT_FIGURE, NEW_CURRENT_FIGURE)

    first = text.find(AUDIT_HEADING)
    if first == -1:
        raise RuntimeError("P90 focused audit heading is missing")
    second = text.find(AUDIT_HEADING, first + len(AUDIT_HEADING))
    if second != -1:
        text = text[:second].rstrip() + "\n"

    if text.count(AUDIT_HEADING) != 1:
        raise RuntimeError("P90 focused audit is not unique")
    if OLD_CURRENT_FIGURE in text:
        raise RuntimeError("stale P89 current-figure path remains in reproducibility guide")
    path.write_text(text, encoding="utf-8")


def clean_sources() -> None:
    path = ROOT / "website" / "sources.html"
    text = path.read_text(encoding="utf-8").replace(OLD_PROVENANCE, NEW_PROVENANCE)
    if OLD_PROVENANCE in text:
        raise RuntimeError("stale P90 provenance link remains in website sources")
    path.write_text(text, encoding="utf-8")


def clean_figure_catalog() -> None:
    path = ROOT / "docs" / "figure_catalog.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace(OLD_CATALOG_COUNT, NEW_CATALOG_COUNT)
    if NEW_CATALOG_COUNT not in text:
        raise RuntimeError("canonical P90 figure catalog count is missing")
    if "figures/p90_exact_nonlinear_rank_one_separation.svg" not in text:
        raise RuntimeError("P90 theorem figure is missing from the figure catalog")
    path.write_text(text, encoding="utf-8")


def verify_reader_surfaces() -> None:
    candidates = [ROOT / "README.md", ROOT / "START_HERE.md"]
    candidates.extend((ROOT / "docs").rglob("*.md"))
    candidates.extend((ROOT / "website").rglob("*.html"))
    stale: list[str] = []
    for path in candidates:
        if OLD_PROVENANCE in path.read_text(encoding="utf-8"):
            stale.append(str(path.relative_to(ROOT)))
    if stale:
        raise RuntimeError(f"stale P90 provenance filename remains in reader surfaces: {stale}")


def main() -> None:
    clean_reproducibility()
    clean_sources()
    clean_figure_catalog()
    verify_reader_surfaces()
    print("P90 reader residuals cleaned and guarded")


if __name__ == "__main__":
    main()
