"""One-time publication helper for the researcher About section."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEBSITE = ROOT / "website"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


# Add a durable About link to website navigation wherever the Visual Atlas link exists.
for path in WEBSITE.glob("*.html"):
    text = read(path)
    if path.name != "about.html" and 'href="about.html"' not in text:
        visual = '<a href="visual-atlas.html">Visual Atlas</a>'
        if visual in text:
            text = text.replace(visual, visual + '<a href="about.html">About</a>', 1)
        else:
            sources = '<a href="sources.html">Sources'
            if sources in text:
                text = text.replace(sources, '<a href="about.html">About</a>' + sources, 1)
    write(path, text)

# Add About to the homepage action row and insert the concise researcher-origin section.
path = WEBSITE / "index.html"
text = read(path)
if '<a class="button" href="about.html">About the researcher</a>' not in text:
    marker = '<a class="button" href="research-lineage.html">Research lineage</a>'
    replacement = marker + '\n        <a class="button" href="about.html">About the researcher</a>'
    if marker not in text:
        raise RuntimeError("homepage hero action marker not found")
    text = text.replace(marker, replacement, 1)

if 'id="about-researcher"' not in text:
    marker = '    <section id="research-i-overview">'
    section = '''    <section id="about-researcher" class="two-col">
      <div>
        <p class="eyebrow">About the researcher · Where this question came from</p>
        <h2>A question I never stopped asking</h2>
        <p>My curiosity about consciousness began long before this repository. During my doctoral years, when I began research at <strong>TRIUMF</strong> and studied quantum mechanics, particle accelerators, measurement, and physical description more deeply, that curiosity became a scientific problem I could no longer treat only conceptually.</p>
        <p>I wrote and completed a book about consciousness, human experience, physics, and questions raised by quantum mechanics, but I never published it. It always felt unfinished. What was missing was not another chapter; it was a mathematical layer strong enough to separate intuition from hypothesis, measurement from interpretation, and an interesting idea from a falsifiable scientific claim.</p>
        <p>Years later, this research program is my return to some of those questions with formal definitions, identifiability conditions, sufficiency tests, measurement models, finite-data guarantees, counterexamples, and reproducible computation.</p>
        <p>Today, as founder and CEO of <strong>Connected Care</strong>, the same scientific thread continues through my work on human biomarkers, physiological and behavioral signals, multimodal sensing, aging, neuroscience, cognitive change, and dementia. At both scales, the question is similar: <strong>what can an observable signal legitimately tell us about an underlying human state?</strong></p>
        <p><a href="about.html">Read the full research story →</a></p>
      </div>
      <aside class="card">
        <h3>Mahsa Keikha, PhD</h3>
        <p><strong>Founder &amp; CEO, Connected Care</strong></p>
        <p>The personal history explains why I care about the question. The theorems still stand or fall on assumptions, proofs, computation, tests, sources, and empirical evaluation.</p>
        <p>Correspondence: <a href="mailto:mahsa@connectioncare.net">mahsa@connectioncare.net</a></p>
      </aside>
    </section>

'''
    if marker not in text:
        raise RuntimeError("homepage Research I marker not found")
    text = text.replace(marker, section + marker, 1)
write(path, text)
