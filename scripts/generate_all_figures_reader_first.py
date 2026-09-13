"""Generate and validate figures using the reader-first publication adapters."""

from __future__ import annotations

from pathlib import Path

import generate_all_figures as legacy

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    legacy.ENRICHER = ROOT / "scripts" / "enrich_reader_first_figure_documentation.py"
    legacy.PUBLICATION_SYNCER = ROOT / "scripts" / "sync_reader_first_figure_publication.py"
    legacy.main()


if __name__ == "__main__":
    main()
