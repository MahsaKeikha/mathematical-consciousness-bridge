from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SVG_ROOTS = (
    ROOT / "docs" / "figures",
    ROOT / "website",
    ROOT / "figures",
)
MARKER_BLOCK_RE = re.compile(r"<marker\b(?P<attrs>[^>]*)>(?P<body>.*?)</marker>", re.S)
ATTR_RE = re.compile(r"(?P<name>[A-Za-z_:][-A-Za-z0-9_:.]*)=(?P<quote>['\"])(?P<value>.*?)(?P=quote)")
MARKER_REF_RE = re.compile(r"marker-(?:start|mid|end)\s*[:=]\s*['\"]?url\(#(?P<id>[^)]+)\)")
MAX_MARKER_SIZE = 8.0


def _svg_paths() -> list[Path]:
    paths: set[Path] = set()
    for root in SVG_ROOTS:
        if root.is_dir():
            paths.update(root.rglob("*.svg"))
    return sorted(paths)


def _attrs_map(attrs: str) -> dict[str, str]:
    return {match.group("name"): match.group("value") for match in ATTR_RE.finditer(attrs)}


def test_no_reader_facing_svg_uses_stroke_scaled_markers() -> None:
    offenders = []
    for path in _svg_paths():
        text = path.read_text(encoding="utf-8")
        if 'markerUnits="strokeWidth"' in text or "markerUnits='strokeWidth'" in text:
            offenders.append(str(path.relative_to(ROOT)))
    assert not offenders, f"stroke-scaled SVG markers remain: {offenders}"


def test_every_referenced_marker_is_fixed_size_and_restrained() -> None:
    violations = []
    for path in _svg_paths():
        text = path.read_text(encoding="utf-8")
        referenced = {match.group("id") for match in MARKER_REF_RE.finditer(text)}
        if not referenced:
            continue

        markers = {}
        for match in MARKER_BLOCK_RE.finditer(text):
            attrs = _attrs_map(match.group("attrs"))
            marker_id = attrs.get("id")
            if marker_id:
                markers[marker_id] = attrs

        for marker_id in sorted(referenced):
            attrs = markers.get(marker_id)
            if attrs is None:
                violations.append(f"{path.relative_to(ROOT)}: missing marker #{marker_id}")
                continue
            if attrs.get("markerUnits") != "userSpaceOnUse":
                violations.append(
                    f"{path.relative_to(ROOT)}: marker #{marker_id} is not userSpaceOnUse"
                )
                continue
            try:
                width = float(attrs["markerWidth"])
                height = float(attrs["markerHeight"])
            except (KeyError, ValueError):
                violations.append(
                    f"{path.relative_to(ROOT)}: marker #{marker_id} lacks numeric dimensions"
                )
                continue
            if max(width, height) > MAX_MARKER_SIZE + 1e-9:
                violations.append(
                    f"{path.relative_to(ROOT)}: marker #{marker_id} is {width}x{height}"
                )

    assert not violations, "unrestrained reader-facing arrowheads remain: " + "; ".join(violations)


def test_figure_pipeline_enforces_arrowhead_normalization() -> None:
    pipeline = (ROOT / "scripts" / "generate_all_figures.py").read_text(encoding="utf-8")
    assert "normalize_svg_arrowheads.py" in pipeline
    assert '_run_script(ARROWHEAD_NORMALIZER, "--check")' in pipeline
