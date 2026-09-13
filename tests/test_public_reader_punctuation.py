from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = (
    ROOT / "README.md",
    ROOT / "START_HERE.md",
    ROOT / "website/index.html",
    ROOT / "website/plain-language.html",
    ROOT / "website/start-here.html",
    ROOT / "website/research-map.html",
    ROOT / "website/measurement-science.html",
    ROOT / "website/research-lineage.html",
    ROOT / "website/sources.html",
)


def test_published_reader_surfaces_use_ascii_punctuation():
    for path in PUBLIC:
        text = path.read_text(encoding="utf-8")
        assert chr(0x2014) not in text, path
        assert chr(0x2013) not in text, path


def test_ascii_hyphenated_scientific_compounds_are_allowed():
    text = (ROOT / "website/measurement-science.html").read_text(encoding="utf-8")
    assert "machine-readable" in text
    assert "third-person" in text
    assert "measurement-science" in text
