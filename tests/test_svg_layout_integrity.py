import re
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURE_ROOT = ROOT / "docs" / "figures"
VISUAL_ATLAS = ROOT / "website" / "visual-atlas.html"
NS = {"svg": "http://www.w3.org/2000/svg"}


def _public_atlas_figures() -> list[Path]:
    text = VISUAL_ATLAS.read_text(encoding="utf-8")
    names = re.findall(r"/docs/figures/([^\"?#]+\.svg)", text)
    figures = [FIGURE_ROOT / name for name in dict.fromkeys(names)]
    assert figures, "Visual Atlas must expose at least one canonical SVG"
    missing = [str(path.relative_to(ROOT)) for path in figures if not path.is_file()]
    assert not missing, f"Visual Atlas references missing figures: {missing}"
    return figures


def _viewbox(root: ET.Element) -> tuple[float, float, float, float]:
    raw = root.attrib.get("viewBox")
    assert raw, "public SVGs must declare a viewBox"
    x, y, width, height = (float(value) for value in raw.split())
    return x, y, width, height


def _rectangles(root: ET.Element, view_width: float, view_height: float) -> list[tuple[float, float, float, float]]:
    rectangles = []
    for rect in root.findall(".//svg:rect", NS):
        x = float(rect.attrib.get("x", 0))
        y = float(rect.attrib.get("y", 0))
        width = float(rect.attrib.get("width", 0))
        height = float(rect.attrib.get("height", 0))
        if width <= 0 or height <= 0:
            continue
        if width >= 0.9 * view_width and height >= 0.9 * view_height:
            continue
        rectangles.append((x, y, width, height))
    return rectangles


def _font_sizes(root: ET.Element) -> dict[str, float]:
    sizes: dict[str, float] = {}
    style_text = "\n".join(style.text or "" for style in root.findall(".//svg:style", NS))
    for class_name, body in re.findall(r"\.([A-Za-z0-9_-]+)\s*\{([^}]*)\}", style_text):
        match = re.search(r"font-size\s*:\s*([0-9.]+)px", body)
        if match is None:
            match = re.search(r"font\s*:[^;]*?([0-9.]+)px", body)
        if match:
            sizes[class_name] = float(match.group(1))
    return sizes


def _font_size(text: ET.Element, class_sizes: dict[str, float]) -> float:
    style = text.attrib.get("style", "")
    match = re.search(r"font-size\s*:\s*([0-9.]+)px", style)
    if match is None:
        match = re.search(r"font\s*:[^;]*?([0-9.]+)px", style)
    if match:
        return float(match.group(1))
    for name in text.attrib.get("class", "").split():
        if name in class_sizes:
            return class_sizes[name]
    return 14.0


def _text_content(element: ET.Element) -> str:
    return " ".join("".join(element.itertext()).split())


def _smallest_containing_rect(
    x: float,
    y: float,
    rectangles: list[tuple[float, float, float, float]],
) -> tuple[float, float, float, float] | None:
    candidates = [
        rect
        for rect in rectangles
        if rect[0] <= x <= rect[0] + rect[2] and rect[1] <= y <= rect[1] + rect[3]
    ]
    return min(candidates, key=lambda rect: rect[2] * rect[3]) if candidates else None


def _path_endpoints(path_data: str) -> tuple[tuple[float, float], tuple[float, float]]:
    tokens = re.findall(r"[MLHVC]|-?(?:\d+(?:\.\d*)?|\.\d+)", path_data)
    index = 0
    command = None
    current = (0.0, 0.0)
    start = None
    while index < len(tokens):
        token = tokens[index]
        if token in {"M", "L", "H", "V", "C"}:
            command = token
            index += 1
            continue
        assert command is not None, f"unsupported SVG path: {path_data}"
        if command in {"M", "L"}:
            current = (float(tokens[index]), float(tokens[index + 1]))
            index += 2
            if start is None:
                start = current
            if command == "M":
                command = "L"
        elif command == "H":
            current = (float(tokens[index]), current[1])
            index += 1
        elif command == "V":
            current = (current[0], float(tokens[index]))
            index += 1
        elif command == "C":
            current = (float(tokens[index + 4]), float(tokens[index + 5]))
            index += 6
    assert start is not None
    return start, current


def _touches_rect_boundary(
    point: tuple[float, float],
    rectangles: list[tuple[float, float, float, float]],
    tolerance: float = 1.5,
) -> bool:
    px, py = point
    for x, y, width, height in rectangles:
        horizontal = (
            x - tolerance <= px <= x + width + tolerance
            and (abs(py - y) <= tolerance or abs(py - (y + height)) <= tolerance)
        )
        vertical = (
            y - tolerance <= py <= y + height + tolerance
            and (abs(px - x) <= tolerance or abs(px - (x + width)) <= tolerance)
        )
        if horizontal or vertical:
            return True
    return False


def test_public_atlas_text_stays_inside_its_blocks() -> None:
    failures = []
    for path in _public_atlas_figures():
        root = ET.parse(path).getroot()
        _, _, view_width, view_height = _viewbox(root)
        rectangles = _rectangles(root, view_width, view_height)
        class_sizes = _font_sizes(root)

        for text in root.findall(".//svg:text", NS):
            if "x" not in text.attrib or "y" not in text.attrib:
                continue
            x = float(text.attrib["x"].split()[0])
            y = float(text.attrib["y"].split()[0])
            box = _smallest_containing_rect(x, y, rectangles)
            if box is None:
                continue

            content = _text_content(text)
            if not content:
                continue
            size = _font_size(text, class_sizes)
            estimated_width = len(content) * size * 0.48
            anchor = text.attrib.get("text-anchor", "start")
            if anchor == "middle":
                left = x - estimated_width / 2
                right = x + estimated_width / 2
            elif anchor == "end":
                left = x - estimated_width
                right = x
            else:
                left = x
                right = x + estimated_width

            bx, by, bw, bh = box
            if left < bx - 2 or right > bx + bw + 2:
                failures.append(
                    f"{path.name}: text may overflow block: {content!r} "
                    f"estimated [{left:.1f}, {right:.1f}] vs block [{bx:.1f}, {bx + bw:.1f}]"
                )
            if not by - 2 <= y <= by + bh + 2:
                failures.append(f"{path.name}: text baseline outside block: {content!r}")

    assert not failures, "\n".join(failures)


def test_public_atlas_arrow_paths_touch_source_and_target_blocks() -> None:
    failures = []
    arrow_count = 0
    for path in _public_atlas_figures():
        root = ET.parse(path).getroot()
        _, _, view_width, view_height = _viewbox(root)
        rectangles = _rectangles(root, view_width, view_height)
        for arrow in root.findall(".//svg:path", NS):
            classes = set(arrow.attrib.get("class", "").split())
            if "arrow" not in classes:
                continue
            arrow_count += 1
            start, end = _path_endpoints(arrow.attrib.get("d", ""))
            if not _touches_rect_boundary(start, rectangles):
                failures.append(f"{path.name}: arrow starts detached at {start}")
            if not _touches_rect_boundary(end, rectangles):
                failures.append(f"{path.name}: arrow ends detached at {end}")

    assert arrow_count > 0
    assert not failures, "\n".join(failures)


def test_public_atlas_figures_fit_their_declared_canvas() -> None:
    failures = []
    for path in _public_atlas_figures():
        root = ET.parse(path).getroot()
        vx, vy, width, height = _viewbox(root)
        for text in root.findall(".//svg:text", NS):
            if "x" not in text.attrib or "y" not in text.attrib:
                continue
            x = float(text.attrib["x"].split()[0])
            y = float(text.attrib["y"].split()[0])
            if not (vx <= x <= vx + width and vy <= y <= vy + height):
                failures.append(f"{path.name}: text anchor outside viewBox at {(x, y)}")
    assert not failures, "\n".join(failures)
