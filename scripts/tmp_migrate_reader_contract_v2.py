from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if text.count(old) != 1:
        raise SystemExit(f"{label}: expected exactly one replacement target, found {text.count(old)}")
    return text.replace(old, new, 1)


def update_overview() -> None:
    path = ROOT / "website/index.html"
    text = path.read_text(encoding="utf-8")

    old_actions = '''      <div class="hero-actions">
        <a class="button primary" href="#plain-language">Explain it simply</a>
        <a class="button" href="start-here.html">Start here</a>
        <a class="button" href="research-map.html">Explore all 88 results</a>
        <a class="button" href="visual-atlas.html">Open the visual atlas</a>
        <a class="button" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge">GitHub repository</a>
      </div>'''
    new_actions = '''      <div class="hero-actions">
        <a class="button primary" href="#project-journey">Explore the full research program</a>
        <a class="button" href="#plain-language">Explain it simply</a>
        <a class="button" href="https://github.com/MahsaKeikha/spatiotemporal-observer-math">Research I</a>
        <a class="button" href="research-map.html">Research II · 88 results</a>
        <a class="button" href="measurement-science.html">Research III · measurement science</a>
        <a class="button" href="research-lineage.html">Research lineage</a>
      </div>'''
    text = replace_once(text, old_actions, new_actions, "website/index.html hero actions")

    old_status = '''      <div class="status-grid" aria-label="Current research status">
        <div><strong>88</strong><span>proposition-level results</span></div>
        <div><strong>P88</strong><span>current theorem frontier</span></div>
        <div><strong>v0.82.0</strong><span>current documented release</span></div>
        <div><strong>Open</strong><span>physical-to-experiential bridge</span></div>
      </div>'''
    new_status = '''      <div class="research-dashboard" aria-label="Three-part research program and open scientific boundary">
        <a class="research-program-card" href="https://github.com/MahsaKeikha/spatiotemporal-observer-math">
          <span class="research-program-kicker">Research I · Physical-system identification</span>
          <span class="research-program-metric"><strong>58</strong><span>proposition-level statements</span></span>
          <span class="research-program-meta">45 experiments · 33 figures · 223 claim-level tests</span>
          <span class="research-program-cta">Open Research I →</span>
        </a>
        <a class="research-program-card" href="research-map.html">
          <span class="research-program-kicker">Research II · Bridge sufficiency and falsification</span>
          <span class="research-program-metric"><strong>88</strong><span>proposition-level results</span></span>
          <span class="research-program-meta">P88 current theorem frontier · v0.82.0</span>
          <span class="research-program-cta">Explore all 88 results →</span>
        </a>
        <a class="research-program-card" href="measurement-science.html">
          <span class="research-program-kicker">Research III · Consciousness measurement science</span>
          <span class="research-program-metric"><strong>34</strong><span>tests in each CI job</span></span>
          <span class="research-program-meta">5 targets · 2 research arms · M0-M7 claim ladder</span>
          <span class="research-program-cta">Explore Research III →</span>
        </a>
        <a class="research-program-card open-problem-card" href="plain-language.html">
          <span class="research-program-kicker">Shared scientific boundary</span>
          <span class="research-program-metric"><strong>Open</strong><span>physical-to-experiential bridge</span></span>
          <span class="research-program-meta">The three programs constrain the problem without presupposing the answer.</span>
          <span class="research-program-cta">See what remains open →</span>
        </a>
      </div>'''
    text = replace_once(text, old_status, new_status, "website/index.html research dashboard")

    path.write_text(text, encoding="utf-8")


def update_styles() -> None:
    path = ROOT / "website/styles.css"
    text = path.read_text(encoding="utf-8")
    if ".research-dashboard {" in text:
        raise SystemExit("website/styles.css: research dashboard styles already present")

    anchor = ".section-head {\n  max-width: var(--reading);\n"
    css = '''.research-dashboard {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 12px;
  margin-top: 46px;
}

.research-program-card {
  display: flex;
  min-width: 0;
  min-height: 238px;
  padding: 21px;
  flex-direction: column;
  border: 1px solid var(--line);
  border-radius: 15px;
  background: var(--paper);
  color: var(--ink);
  transition: transform 150ms ease, border-color 150ms ease, box-shadow 150ms ease;
}

.research-program-card:hover {
  transform: translateY(-2px);
  border-color: #aeb7ca;
  box-shadow: 0 10px 26px rgba(20, 26, 36, 0.07);
  text-decoration: none;
}

.research-program-kicker {
  min-height: 3.3em;
  color: var(--accent2);
  font-size: 0.7rem;
  font-weight: 760;
  line-height: 1.45;
  letter-spacing: 0.07em;
  text-transform: uppercase;
}

.research-program-metric {
  display: block;
  margin-top: 18px;
}

.research-program-metric strong {
  display: block;
  font-family: var(--font-display);
  font-size: 2.15rem;
  font-weight: 600;
  line-height: 1.05;
  letter-spacing: -0.025em;
}

.research-program-metric > span {
  display: block;
  margin-top: 5px;
  color: var(--muted);
  font-size: 0.82rem;
  line-height: 1.45;
}

.research-program-meta {
  display: block;
  margin-top: 15px;
  color: var(--muted);
  font-size: 0.78rem;
  line-height: 1.55;
}

.research-program-cta {
  display: block;
  margin-top: auto;
  padding-top: 18px;
  color: var(--accent);
  font-size: 0.79rem;
  font-weight: 700;
  line-height: 1.4;
}

.open-problem-card {
  background: var(--soft);
}

@media (max-width: 1000px) {
  .research-dashboard {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 680px) {
  .research-dashboard {
    grid-template-columns: 1fr;
    margin-top: 36px;
  }

  .research-program-card {
    min-height: 0;
  }

  .research-program-kicker {
    min-height: 0;
  }
}

'''
    text = replace_once(text, anchor, css + anchor, "website/styles.css insertion")
    path.write_text(text, encoding="utf-8")


def update_contract() -> None:
    path = ROOT / "tests/test_publication_contract_v2.py"
    text = path.read_text(encoding="utf-8")
    old = '''def test_overview_orients_to_all_three_research_programs_before_p88() -> None:
    overview = _read(WEBSITE / "index.html")
    journey = overview.index('id="project-journey"')
    p88 = overview.index('id="p88-frontier"')
    assert journey < p88
    for token in (
        "The whole research program in three stages",
        "Research I",
        "Research II",
        "Research III",
        "spatiotemporal-observer-math",
        "88 proposition-level results",
        "measurement-science.html",
        "None of these stages by itself establishes the final physical-to-experiential bridge.",
    ):
        assert token in overview
'''
    new = '''def test_overview_orients_to_all_three_research_programs_before_p88() -> None:
    overview = _read(WEBSITE / "index.html")
    dashboard = overview.index('class="research-dashboard"')
    journey = overview.index('id="project-journey"')
    p88 = overview.index('id="p88-frontier"')
    assert dashboard < journey < p88
    for token in (
        "The whole research program in three stages",
        "Research I · Physical-system identification",
        "58</strong><span>proposition-level statements",
        "45 experiments · 33 figures · 223 claim-level tests",
        "spatiotemporal-observer-math",
        "Research II · Bridge sufficiency and falsification",
        "88</strong><span>proposition-level results",
        "P88 current theorem frontier · v0.82.0",
        "research-map.html",
        "Research III · Consciousness measurement science",
        "34</strong><span>tests in each CI job",
        "5 targets · 2 research arms · M0-M7 claim ladder",
        "measurement-science.html",
        "Open</strong><span>physical-to-experiential bridge",
        "None of these stages by itself establishes the final physical-to-experiential bridge.",
    ):
        assert token in overview
'''
    text = replace_once(text, old, new, "tests/test_publication_contract_v2.py overview contract")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_overview()
    update_styles()
    update_contract()
    print("Staged full-program Overview dashboard with Research I, II, III, and open bridge boundary")


if __name__ == "__main__":
    main()
