"""Synchronize generated figure publication artifacts for the reader-first site.

The legacy synchronization module still owns deterministic publication artifacts
(`figures/current_frontier.svg`, `figures/manifest.json`, and `figures/index.md`).
Its old HTML injectors predate the curated reader-first website, so this adapter
keeps the current homepage and Visual Atlas intact while retaining the generated
artifact contract.
"""

from __future__ import annotations

import sync_figure_publication as sync


def _preserve_curated_html(text: str) -> str:
    return text


def main() -> None:
    sync._normalize_atlas = _preserve_curated_html
    sync._normalize_home = _preserve_curated_html
    sync.main()


if __name__ == "__main__":
    main()
