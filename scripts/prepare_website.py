"""Prepare the static research website for GitHub Pages deployment.

The build copies the canonical HTML source, injects the same shared design/navigation
assets into every page, bundles the exact-commit figure tree, localizes raw figure
URLs, and validates the public P1-P87 research state before deployment.
"""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL_WEBSITE = ROOT / "website"
CANONICAL_FIGURES = ROOT / "docs" / "figures"
RAW_FIGURE_PREFIX = (
    "https://raw.githubusercontent.com/MahsaKeikha/"
    "mathematical-consciousness-bridge/main/docs/figures/"
)
CURRENT_FRONTIER_FIGURE = "p87_exact_bounded_primitive_quad_projection_parity.svg"

ASSET_VERSION = "20260913-coherent-p87-r87"
SCRIPT_TAG = f'<script defer src="app.js?v={ASSET_VERSION}"></script>'
READER_LINKS_SCRIPT_TAG = '<script defer src="reader-links.js"></script>'
FOOTER_SCRIPT_TAG = '<script defer src="footer.js"></script>'
BASE_STYLE_TAG = f'<link rel="stylesheet" href="styles.css?v={ASSET_VERSION}" />'
NAVIGATION_STYLE_TAG = '<link rel="stylesheet" href="navigation.css" />'
NAVIGATION_V2_STYLE_TAG = (
    f'<link rel="stylesheet" href="navigation-v2.css?v={ASSET_VERSION}" />'
)
PUBLICATION_STYLE_TAG = '<link rel="stylesheet" href="publication.css" />'
PUBLICATION_V2_STYLE_TAG = '<link rel="stylesheet" href="publication-v2.css" />'
RESEARCH_GUIDE_STYLE_TAG = (
    f'<link rel="stylesheet" href="research-guide-v2.css?v={ASSET_VERSION}" />'
)
CONTRAST_STYLE_TAG = (
    f'<link rel="stylesheet" href="contrast-v2.css?v={ASSET_VERSION}" />'
)
READER_EXPERIENCE_STYLE_TAG = (
    f'<link rel="stylesheet" href="reader-experience-v2.css?v={ASSET_VERSION}" />'
)

APP_SCRIPT_PATTERN = re.compile(
    r'<script\s+defer\s+src="app\.js(?:\?v=[^"]+)?"></script>'
)
BASE_STYLE_PATTERN = re.compile(
    r'<link\s+rel="stylesheet"\s+href="styles\.css(?:\?v=[^"]+)?"\s*/?>'
)
NAVIGATION_V2_STYLE_PATTERN = re.compile(
    r'<link\s+rel="stylesheet"\s+href="navigation-v2\.css(?:\?v=[^"]+)?"\s*/?>'
)
RESEARCH_GUIDE_STYLE_PATTERN = re.compile(
    r'<link\s+rel="stylesheet"\s+href="research-guide-v2\.css(?:\?v=[^"]+)?"\s*/?>'
)
CONTRAST_STYLE_PATTERN = re.compile(
    r'<link\s+rel="stylesheet"\s+href="contrast-v2\.css(?:\?v=[^"]+)?"\s*/?>'
)
READER_EXPERIENCE_STYLE_PATTERN = re.compile(
    r'<link\s+rel="stylesheet"\s+href="reader-experience-v2\.css(?:\?v=[^"]+)?"\s*/?>'
)
TOPBAR_NAV_PATTERN = re.compile(
    r'(<header\s+class="topbar">.*?<nav(?:\s[^>]*)?>).*?(</nav>)',
    flags=re.DOTALL,
)

FALLBACK_NAV = (
    '<a href="index.html">Overview</a>'
    '<a href="plain-language.html">Plain Language</a>'
    '<a href="start-here.html">Start Here</a>'
    '<a href="research-map.html">Research Map</a>'
    '<a href="visual-atlas.html">Explore</a>'
    '<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge">GitHub</a>'
)

PUBLIC_BOUNDARY = (
    "P87 is a conditional model-separation result for the declared P75 "
    "target-measurement family. It does not identify a latent state with "
    "consciousness, prove that consciousness is nonphysical, or complete the "
    "physical-to-experiential bridge. The final bridge remains open."
)

CANONICAL_BRANCHES = (
    ("Foundations", "P1-P10"),
    ("Physical description", "P11-P18"),
    ("Candidate bridge class", "P19-P24"),
    ("Operational scale", "P25-P37"),
    ("Quantum interface", "P38-P44"),
    ("Adaptive evidence acquisition", "P45-P60"),
    ("Calibration and optimization", "P61-P70"),
    ("Target provenance", "P71"),
    ("Target measurement", "P72"),
    ("Channel recovery and model testing", "P73-P87"),
)

PUBLIC_PAGES = (
    "index.html",
    "plain-language.html",
    "start-here.html",
    "research-map.html",
    "research-navigation.html",
    "visual-atlas.html",
    "implementation.html",
)


def _normalize_navigation_assets(text: str) -> str:
    text = APP_SCRIPT_PATTERN.sub(SCRIPT_TAG, text)
    text = BASE_STYLE_PATTERN.sub(BASE_STYLE_TAG, text)
    text = NAVIGATION_V2_STYLE_PATTERN.sub(NAVIGATION_V2_STYLE_TAG, text)
    text = RESEARCH_GUIDE_STYLE_PATTERN.sub(RESEARCH_GUIDE_STYLE_TAG, text)
    text = CONTRAST_STYLE_PATTERN.sub(CONTRAST_STYLE_TAG, text)
    text = READER_EXPERIENCE_STYLE_PATTERN.sub(READER_EXPERIENCE_STYLE_TAG, text)
    return text


def _normalize_topbar_fallback(text: str) -> str:
    return TOPBAR_NAV_PATTERN.sub(
        lambda match: f"{match.group(1)}{FALLBACK_NAV}{match.group(2)}",
        text,
        count=1,
    )


def _localize_figure_sources(text: str) -> str:
    return text.replace(f'src="{RAW_FIGURE_PREFIX}', 'src="figures/')


def _copy_canonical_figures(output: Path) -> None:
    if not CANONICAL_FIGURES.is_dir():
        raise FileNotFoundError(
            f"canonical figure directory not found: {CANONICAL_FIGURES}"
        )
    shutil.copytree(CANONICAL_FIGURES, output / "figures", dirs_exist_ok=True)


def _assert_order(text: str, labels: tuple[str, ...], page: str) -> None:
    cursor = -1
    for label in labels:
        position = text.find(label)
        if position < 0:
            raise RuntimeError(f"{page} is missing canonical label: {label}")
        if position <= cursor:
            raise RuntimeError(f"{page} has branch labels out of canonical order")
        cursor = position


def _validate_public_state(output: Path) -> None:
    frontier_figure = output / "figures" / CURRENT_FRONTIER_FIGURE
    if not frontier_figure.is_file():
        raise RuntimeError(f"missing current P87 theorem figure: {frontier_figure}")

    stale_tokens = (
        "Explore all 86 results",
        "86 proposition-level results",
        "all 86 propositions",
        "Current theorem frontier · P86",
        "Current frontier · P86",
        "current theorem frontier is P86",
    )

    for name in PUBLIC_PAGES:
        path = output / name
        if not path.is_file():
            raise RuntimeError(f"website build is missing required public page: {name}")
        text = path.read_text(encoding="utf-8")
        if "P87" not in text:
            raise RuntimeError(f"{name} does not expose current theorem frontier P87")
        if "87" not in text:
            raise RuntimeError(f"{name} does not expose the 87-result public state")
        if PUBLIC_BOUNDARY not in text:
            raise RuntimeError(f"{name} does not use the canonical public scientific boundary")
        stale = [token for token in stale_tokens if token in text]
        if stale:
            raise RuntimeError(f"{name} contains stale pre-P87 reader text: {stale}")

    homepage = (output / "index.html").read_text(encoding="utf-8")
    if "Explore all 87 results" not in homepage:
        raise RuntimeError("homepage must expose the exact 'Explore all 87 results' action")

    branch_labels = tuple(label for label, _ in CANONICAL_BRANCHES)
    branch_ranges = tuple(result_range for _, result_range in CANONICAL_BRANCHES)
    for name in ("research-map.html", "research-navigation.html"):
        text = (output / name).read_text(encoding="utf-8")
        _assert_order(text, branch_labels, name)
        _assert_order(text, branch_ranges, name)

    research_map = (output / "research-map.html").read_text(encoding="utf-8")
    if "Chapter 1" in research_map or "Chapter 2" in research_map:
        raise RuntimeError("Research Map must not mix conceptual card numbers with proposition ranges")

    local_frontier_src = f'src="figures/{CURRENT_FRONTIER_FIGURE}"'
    for name in ("index.html", "visual-atlas.html"):
        text = (output / name).read_text(encoding="utf-8")
        if local_frontier_src not in text:
            raise RuntimeError(f"{name} does not use the exact-commit P87 theorem figure")
        if f'src="{RAW_FIGURE_PREFIX}' in text:
            raise RuntimeError(f"{name} still depends on mutable raw-GitHub main figures")


def prepare_website(source: Path, output: Path) -> None:
    if not source.is_dir():
        raise FileNotFoundError(f"website source directory not found: {source}")

    canonical_build = source.resolve() == CANONICAL_WEBSITE.resolve()

    if output.exists():
        shutil.rmtree(output)
    shutil.copytree(source, output)
    _copy_canonical_figures(output)

    html_files = sorted(output.glob("*.html"))
    if not html_files:
        raise RuntimeError("website build contains no HTML pages")

    for path in html_files:
        text = path.read_text(encoding="utf-8")
        if "</head>" not in text:
            raise RuntimeError(f"missing </head> in {path}")

        text = _normalize_navigation_assets(text)
        text = _normalize_topbar_fallback(text)
        text = _localize_figure_sources(text)

        additions: list[str] = []
        for tag in (
            BASE_STYLE_TAG,
            NAVIGATION_STYLE_TAG,
            NAVIGATION_V2_STYLE_TAG,
            PUBLICATION_STYLE_TAG,
            PUBLICATION_V2_STYLE_TAG,
            RESEARCH_GUIDE_STYLE_TAG,
            CONTRAST_STYLE_TAG,
            READER_EXPERIENCE_STYLE_TAG,
            SCRIPT_TAG,
            READER_LINKS_SCRIPT_TAG,
            FOOTER_SCRIPT_TAG,
        ):
            if tag not in text:
                additions.append(tag)
        if additions:
            text = text.replace("</head>", "".join(additions) + "</head>", 1)
        path.write_text(text, encoding="utf-8")

    required_assets = (
        "app.js",
        "reader-links.js",
        "footer.js",
        "styles.css",
        "navigation.css",
        "navigation-v2.css",
        "publication.css",
        "publication-v2.css",
        "research-guide-v2.css",
        "contrast-v2.css",
        "reader-experience-v2.css",
    )
    for asset in required_assets:
        if not (output / asset).is_file():
            raise RuntimeError(f"website build is missing {asset}")

    if canonical_build:
        _validate_public_state(output)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=Path("website"))
    parser.add_argument("--output", type=Path, default=Path("_site"))
    args = parser.parse_args()
    prepare_website(args.source, args.output)
    print(f"prepared coherent P1-P87 website: {args.output}")


if __name__ == "__main__":
    main()
