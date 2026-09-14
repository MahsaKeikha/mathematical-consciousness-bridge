import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DOCS = ROOT / "docs"
WEBSITE = ROOT / "website"


def _plain_language_section(text: str) -> str:
    start = text.index("# What this project is trying to achieve, in plain language")
    end = text.index("# Abstract", start)
    return text[start:end]


def _frontier() -> int:
    numbers: list[int] = []
    for path in DOCS.glob("proposition_*_*.md"):
        match = re.match(r"proposition_(\d+)_", path.name)
        if match:
            numbers.append(int(match.group(1)))
    assert numbers
    return max(numbers)


def _project_version() -> str:
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    match = re.search(r'^version\s*=\s*"([^"]+)"', pyproject, flags=re.MULTILINE)
    assert match is not None
    return match.group(1)


def test_p79_core_artifacts_exist() -> None:
    required = (
        DOCS / "proposition_79_certified_sampling_radius.md",
        DOCS / "p79_equation_provenance.md",
        DOCS / "figures" / "p79_certified_sampling_radius.svg",
        ROOT / "src" / "consciousness_bridge" / "certified_sampling_radius.py",
        ROOT / "tests" / "test_certified_sampling_radius.py",
        ROOT / "tests" / "test_p79_figure_geometry.py",
    )
    for path in required:
        assert path.exists(), path












def test_p79_publication_contains_only_permanent_artifacts() -> None:
    assert not (ROOT / ".github" / "workflows" / "p79-publication-patch.yml").exists()
    assert not (ROOT / "scripts" / "p79_publication_patch.py").exists()
