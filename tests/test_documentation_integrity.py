import re
from pathlib import Path

_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def test_local_markdown_targets_exist():
    root = Path(__file__).resolve().parents[1]
    missing: list[str] = []

    for markdown in [root / "README.md", *sorted((root / "docs").glob("*.md"))]:
        text = markdown.read_text(encoding="utf-8")
        for raw_target in _LINK_RE.findall(text):
            target = raw_target.strip().split()[0]
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue

            path_part = target.split("#", 1)[0]
            if not path_part:
                continue

            resolved = (markdown.parent / path_part).resolve()
            if not resolved.exists():
                missing.append(
                    f"{markdown.relative_to(root)} -> {target}"
                )

    assert not missing, "Missing local Markdown targets:\n" + "\n".join(missing)
