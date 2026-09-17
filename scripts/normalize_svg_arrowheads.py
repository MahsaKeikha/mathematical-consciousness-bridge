"""Normalize reader-facing SVG arrowheads to restrained fixed-size geometry.

SVG markers default to ``markerUnits=\"strokeWidth\"``. That default makes an
otherwise reasonable 8-10 unit triangle scale with the connector stroke and can
produce visually dominant arrowheads in theorem diagrams. Reader-facing figures
should use a marker viewport measured in user-space units instead.

This normalizer is deliberately narrow: it changes only marker elements that
are actually referenced by ``marker-start``, ``marker-mid``, or ``marker-end``.
The marker's internal coordinate system and refX/refY are preserved. If the
marker has no viewBox, one is inferred from its pre-normalization markerWidth
and markerHeight so changing marker units does not clip the existing path.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SVG_ROOTS = (
    ROOT / "docs" / "figures",
    ROOT / "website",
    ROOT / "figures",
)
MAX_MARKER_SIZE = 8.0

MARKER_BLOCK_RE = re.compile(r"<marker\b(?P<attrs>[^>]*)>(?P<body>.*?)</marker>", re.S)
ATTR_RE = re.compile(r"(?P<name>[A-Za-z_:][-A-Za-z0-9_:.]*)=(?P<quote>['\"])(?P<value>.*?)(?P=quote)")
MARKER_REF_RE = re.compile(r"marker-(?:start|mid|end)\s*[:=]\s*['\"]?url\(#(?P<id>[^)]+)\)")


def _fmt(value: float) -> str:
    rounded = round(value, 4)
    if rounded.is_integer():
        return str(int(rounded))
    return f"{rounded:g}"


def _attrs_map(attrs: str) -> dict[str, str]:
    return {match.group("name"): match.group("value") for match in ATTR_RE.finditer(attrs)}


def _replace_attr(attrs: str, name: str, value: str) -> str:
    pattern = re.compile(rf"\b{re.escape(name)}=(['\"]).*?\1")
    replacement = f'{name}="{value}"'
    if pattern.search(attrs):
        return pattern.sub(replacement, attrs, count=1)
    suffix = "" if attrs.endswith(" ") or not attrs else " "
    return f"{attrs}{suffix}{replacement}"


def _referenced_marker_ids(text: str) -> set[str]:
    return {match.group("id") for match in MARKER_REF_RE.finditer(text)}


def _normalize_marker_block(match: re.Match[str], referenced: set[str]) -> str:
    attrs = match.group("attrs")
    body = match.group("body")
    values = _attrs_map(attrs)
    marker_id = values.get("id")
    if not marker_id or marker_id not in referenced:
        return match.group(0)

    try:
        old_width = float(values.get("markerWidth", str(MAX_MARKER_SIZE)))
        old_height = float(values.get("markerHeight", str(MAX_MARKER_SIZE)))
    except ValueError:
        old_width = old_height = MAX_MARKER_SIZE

    if old_width <= 0 or old_height <= 0:
        old_width = old_height = MAX_MARKER_SIZE

    largest = max(old_width, old_height)
    scale = min(1.0, MAX_MARKER_SIZE / largest)
    new_width = old_width * scale
    new_height = old_height * scale

    normalized = attrs
    if "viewBox" not in values:
        normalized = _replace_attr(
            normalized,
            "viewBox",
            f"0 0 {_fmt(old_width)} {_fmt(old_height)}",
        )
    normalized = _replace_attr(normalized, "markerUnits", "userSpaceOnUse")
    normalized = _replace_attr(normalized, "markerWidth", _fmt(new_width))
    normalized = _replace_attr(normalized, "markerHeight", _fmt(new_height))
    return f"<marker{normalized}>{body}</marker>"


def normalize_text(text: str) -> str:
    referenced = _referenced_marker_ids(text)
    if not referenced:
        return text
    return MARKER_BLOCK_RE.sub(lambda match: _normalize_marker_block(match, referenced), text)


def svg_paths() -> list[Path]:
    paths: set[Path] = set()
    for root in SVG_ROOTS:
        if root.is_file() and root.suffix.lower() == ".svg":
            paths.add(root)
        elif root.is_dir():
            paths.update(root.rglob("*.svg"))
    return sorted(paths)


def run(*, check: bool) -> int:
    changed: list[Path] = []
    for path in svg_paths():
        original = path.read_text(encoding="utf-8")
        normalized = normalize_text(original)
        if normalized == original:
            continue
        changed.append(path)
        if not check:
            path.write_text(normalized, encoding="utf-8")

    if changed:
        relative = ", ".join(str(path.relative_to(ROOT)) for path in changed)
        if check:
            raise SystemExit(f"arrowhead normalization required: {relative}")
        print(f"[arrowheads] normalized {len(changed)} SVG files")
        for path in changed:
            print(f"[arrowheads] {path.relative_to(ROOT)}")
    else:
        print("[arrowheads] all reader-facing SVG marker geometry is normalized")
    return len(changed)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if any reader-facing SVG would be changed",
    )
    args = parser.parse_args()
    run(check=args.check)


if __name__ == "__main__":
    main()
