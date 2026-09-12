"""Prepare the static research website for GitHub Pages deployment.

The repository keeps page content as plain HTML files. This build step copies the
website into a deployment directory and guarantees that every page loads the
shared navigation script. Keeping the navigation behavior centralized prevents
page-to-page drift while preserving a fully auditable static-site build.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

SCRIPT_TAG = '<script defer src="app.js"></script>'


def prepare_website(source: Path, output: Path) -> None:
    """Copy ``source`` to ``output`` and inject the shared app script as needed."""

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
        if SCRIPT_TAG not in text:
            if "</head>" not in text:
                raise RuntimeError(f"missing </head> in {path}")
            text = text.replace("</head>", f"{SCRIPT_TAG}</head>", 1)
            path.write_text(text, encoding="utf-8")

    if not (output / "app.js").is_file():
        raise RuntimeError("website build is missing app.js")
    if not (output / "styles.css").is_file():
        raise RuntimeError("website build is missing styles.css")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=Path("website"))
    parser.add_argument("--output", type=Path, default=Path("_site"))
    args = parser.parse_args()
    prepare_website(args.source, args.output)
    print(f"prepared website: {args.output}")


if __name__ == "__main__":
    main()
