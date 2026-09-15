from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONNECTED_CARE_URL = 'https://www.connectioncare.org/'
LINKEDIN_URL = 'https://www.linkedin.com/in/mahsa-keikha-ph-d-p-eng-a9470b43/'


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_about_page_preserves_research_origin_and_current_affiliation() -> None:
    page = _read("website/about.html")
    lower = page.lower()
    assert "mahsa keikha" in lower
    assert "triumf" in lower
    assert "quantum mechanics" in lower
    assert "book" in lower and "never published" in lower
    assert "mathematical" in lower
    assert "connected care" in lower
    assert "mahsa@connectioncare.net" in lower
    assert "The question that kept drawing me deeper." in page
    assert "A question I never stopped asking" not in page
    assert '<a href="https://triumf.ca/">TRIUMF, Canada\'s Particle Accelerator Centre</a>' in page
    assert f'<a href="{CONNECTED_CARE_URL}">Connected Care</a>' in page
    assert f'<a href="{LINKEDIN_URL}">Mahsa Keikha, PhD</a>' in page


def test_about_page_connects_foundations_to_human_measurement_research() -> None:
    page = _read("website/about.html").lower()
    for term in (
        "human biomarkers",
        "physiological",
        "behavioral",
        "aging",
        "neuroscience",
        "dementia",
        "measurement channel",
        "identifiability",
        "falsifiable",
    ):
        assert term in page


def test_about_page_keeps_biography_separate_from_evidence() -> None:
    page = _read("website/about.html").lower()
    assert "personal history explains why i care about the question" in page
    assert "it is not evidence for any theorem" in page
    assert "physical-to-experiential" in page


def test_homepage_exposes_about_researcher_path() -> None:
    home = _read("website/index.html")
    assert 'href="about.html"' in home
    assert 'id="about-researcher"' in home
    assert "The question that kept drawing me deeper." in home
    assert "A question I never stopped asking" not in home
    assert '<a href="https://triumf.ca/">TRIUMF, Canada\'s Particle Accelerator Centre</a>' in home
    assert f'<a href="{CONNECTED_CARE_URL}">Connected Care</a>' in home
    assert f'<a href="{LINKEDIN_URL}">Mahsa Keikha, PhD</a>' in home
    assert "mahsa@connectioncare.net" in home
