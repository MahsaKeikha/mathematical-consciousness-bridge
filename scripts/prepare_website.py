"""Prepare the static research website for GitHub Pages deployment.

The repository keeps page content as plain HTML files. This build step copies the
website into a deployment directory and guarantees that every page loads the
shared navigation behavior, navigation styles, and final publication typography.
Keeping cross-page behavior centralized prevents page-to-page drift while
preserving a fully auditable static-site build.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

SCRIPT_TAG = '<script defer src="app.js"></script>'
NAVIGATION_STYLE_TAG = '<link rel="stylesheet" href="navigation.css" />'
PUBLICATION_STYLE_TAG = '<link rel="stylesheet" href="publication.css" />'


def prepare_website(source: Path, output: Path) -> None:
    """Copy ``source`` to ``output`` and inject shared publication assets."""

    if not source.is_dir():
        raise FileNotFoundError(f"website source directory not found: {source}")

    if output.exists():
        shutil.rmtree(output)
    shutil.copytree(source, output)

    html_files = sorted(output.glob("*.html"))
    if not html_files:
        raise RuntimeError("website build contains no HTML pages")

    for path in html_files:
        text = path.read_text(encoding="utf-8")
        if "</head>" not in text:
            raise RuntimeError(f"missing </head> in {path}")

        additions: list[str] = []
        if NAVIGATION_STYLE_TAG not in text:
            additions.append(NAVIGATION_STYLE_TAG)
        if PUBLICATION_STYLE_TAG not in text:
            additions.append(PUBLICATION_STYLE_TAG)
        if SCRIPT_TAG not in text:
            additions.append(SCRIPT_TAG)
        if additions:
            text = text.replace("</head>", "".join(additions) + "</head>", 1)
            path.write_text(text, encoding="utf-8")

    required_assets = ("app.js", "styles.css", "navigation.css", "publication.css")
    for asset in required_assets:
        if not (output / asset).is_file():
            raise RuntimeError(f"website build is missing {asset}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=Path("website"))
    parser.add_argument("--output", type=Path, default=Path("_site"))
    args = parser.parse_args()
    prepare_website(args.source, args.output)
    print(f"prepared website: {args.output}")


if __name__ == "__main__":
    main()
