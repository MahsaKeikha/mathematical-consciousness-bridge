from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".tex", ".bib", ".svg", ".txt"}


def _scientific_text_files():
    for path in (ROOT / "README.md", *sorted((ROOT / "docs").rglob("*"))):
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def test_scientific_text_has_no_form_feed_control_characters():
    for path in _scientific_text_files():
        text = path.read_text(encoding="utf-8")
        assert "\x0c" not in text, f"form-feed control character found in {path.relative_to(ROOT)}"


def test_proposition_sources_have_no_truncated_frac_command():
    for path in sorted((ROOT / "docs").glob("proposition_*.md")):
        text = path.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            stripped = line.lstrip()
            assert not stripped.startswith("rac{"), (
                f"possible corrupted LaTeX \\frac command in "
                f"{path.relative_to(ROOT)}:{line_number}"
            )
