"""Run figure enrichment without mutating curated reader-first public pages.

The underlying enrichment module remains responsible for SVG metadata, captions,
and the generated figure catalog. The concise README and curated Visual Atlas are
publication surfaces with their own reader-first contract, so they are deliberately
left untouched by automated bulk insertion.
"""

from __future__ import annotations

import enrich_figure_documentation as enrich


def _leave_curated_surface_unchanged(*_args: object, **_kwargs: object) -> None:
    """Preserve hand-curated reader-facing pages during figure regeneration."""

    return None


def main() -> None:
    enrich._update_readme = _leave_curated_surface_unchanged
    enrich._update_visual_atlas = _leave_curated_surface_unchanged
    enrich.main()


if __name__ == "__main__":
    main()
