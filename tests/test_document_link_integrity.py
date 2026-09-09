import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HTML_LINK = re.compile(r"(?:href|src)=[\"']([^\"']+)[\"']")
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)


def _without_fenced_code(text: str) -> str:
    lines = []
    in_fence = False
    fence = ""
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith(("```", "~~~")):
            token = stripped[:3]
            if not in_fence:
                in_fence = True
                fence = token
            elif token == fence:
                in_fence = False
                fence = ""
            continue
        if not in_fence:
            lines.append(line)
    return "\n".join(lines)


def _target_only(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and target.endswith(">"):
        return target[1:-1]
    if " \"" in target:
        target = target.split(" \"", 1)[0]
    if " '" in target:
        target = target.split(" '", 1)[0]
    return target


def _slug(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[`*_~]", "", text)
    text = text.strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text


def _anchors(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    for heading in HEADING.findall(text):
        base = _slug(heading)
        if not base:
            continue
        count = counts.get(base, 0)
        anchors.add(base if count == 0 else f"{base}-{count}")
        counts[base] = count + 1
    return anchors


def _markdown_files() -> list[Path]:
    return [ROOT / "README.md", *sorted((ROOT / "docs").rglob("*.md"))]


def _local_targets(path: Path):
    text = _without_fenced_code(path.read_text(encoding="utf-8"))
    for match in MARKDOWN_LINK.findall(text):
        yield _target_only(match)
    for match in HTML_LINK.findall(text):
        yield match.strip()


def test_all_local_markdown_links_resolve():
    failures = []
    anchor_cache: dict[Path, set[str]] = {}

    for source in _markdown_files():
        for target in _local_targets(source):
            if not target or target.startswith(("http://", "https://", "mailto:", "tel:")):
                continue

            path_part, separator, fragment = target.partition("#")
            path_part = unquote(path_part)
            fragment = unquote(fragment)

            if path_part:
                if path_part.startswith("/"):
                    destination = ROOT / path_part.lstrip("/")
                else:
                    destination = (source.parent / path_part).resolve()
            else:
                destination = source.resolve()

            try:
                destination.relative_to(ROOT.resolve())
            except ValueError:
                failures.append(
                    f"{source.relative_to(ROOT)} -> {target}: target leaves repository"
                )
                continue

            if not destination.exists():
                failures.append(
                    f"{source.relative_to(ROOT)} -> {target}: file does not exist"
                )
                continue

            if separator and fragment and destination.suffix.lower() == ".md":
                anchors = anchor_cache.setdefault(destination, _anchors(destination))
                if fragment not in anchors:
                    failures.append(
                        f"{source.relative_to(ROOT)} -> {target}: anchor does not exist"
                    )

    assert not failures, "\n".join(failures)


def test_reader_navigation_exposes_the_complete_theorem_chain():
    nav = (ROOT / "docs/research_navigation.md").read_text(encoding="utf-8")
    for number in range(1, 22):
        assert f"proposition_{number}_" in nav


def test_main_page_links_to_reader_navigation_and_provenance():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    required = [
        "docs/research_navigation.md",
        "docs/theorem_roadmap.md",
        "docs/equation_and_citation_map.md",
        "docs/citation_and_reference_policy.md",
        "docs/reference_audit.md",
    ]
    for path in required:
        assert path in text
