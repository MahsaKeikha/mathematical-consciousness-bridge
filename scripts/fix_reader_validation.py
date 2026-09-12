from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fix_start_here_typography() -> None:
    path = ROOT / "START_HERE.md"
    text = path.read_text(encoding="utf-8")
    en_dash = chr(0x2013)
    em_dash = chr(0x2014)
    text = text.replace(f" {em_dash} ", ": ")
    text = text.replace(en_dash, "-")
    text = text.replace(em_dash, "-")
    path.write_text(text, encoding="utf-8")


def fix_website_contract() -> None:
    path = ROOT / "website" / "index.html"
    text = path.read_text(encoding="utf-8")

    old_boundary = (
        "<p><strong>The repository does not claim that consciousness has already been "
        "derived from physics.</strong>"
    )
    new_boundary = (
        "<p>The repository does <strong>not</strong> claim that consciousness has "
        "already been derived from physics."
    )
    if old_boundary in text:
        text = text.replace(old_boundary, new_boundary, 1)

    figure_marker = (
        "      <div class=\"figure-card\">\n"
        "        <img src=\"https://raw.githubusercontent.com/MahsaKeikha/"
        "mathematical-consciousness-bridge/main/docs/figures/"
        "p78_certified_continuous_model_separation.svg\""
    )
    if "p75_target_model_adequacy_overidentification.svg" not in text:
        figure_block = """      <div class="figure-card">
        <img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p75_target_model_adequacy_overidentification.svg" alt="P75 target model adequacy and overidentification" />
        <div><h3>P75 · Target-model adequacy</h3><p>A fourth observed target view creates overidentifying constraints and a full-law reconstruction audit. Parameter recovery is kept separate from model adequacy.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_75_target_model_adequacy_overidentification.md">Read P75 →</a></div>
      </div>

      <div class="figure-card">
        <img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p76_finite_sample_target_model_adequacy.svg" alt="P76 finite sample target model adequacy rejection" />
        <div><h3>P76 · Finite-sample adequacy rejection</h3><p>Population adequacy restrictions become finite-data rejection certificates only when the observed violation remains separated from zero after simultaneous uncertainty is propagated.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_76_finite_sample_target_model_adequacy.md">Read P76 →</a></div>
      </div>

      <div class="figure-card">
        <img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p77_full_law_model_set_separation.svg" alt="P77 full law model set separation" />
        <div><h3>P77 · Full-law model-set separation</h3><p>The complete empirical confidence region is compared with the complete declared model family. A local best fit is an upper bound on minimum distance, not a rejection lower bound.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_77_full_law_model_set_separation.md">Read P77 →</a></div>
      </div>

"""
        if figure_marker not in text:
            raise RuntimeError("could not locate P78 figure block insertion point")
        text = text.replace(figure_marker, figure_block + figure_marker, 1)

    provenance_marker = "    <section id=\"reproduce\" class=\"two-col\">"
    if "Repository-original theorem or computation" not in text:
        provenance = """    <section id="provenance">
      <div class="section-head">
        <p class="eyebrow">Provenance and audit</p>
        <h2>Every claim should expose where it came from and how to challenge it</h2>
      </div>
      <div class="result-grid">
        <article class="result"><h3>Equation and citation map</h3><p>Trace standard mathematics, prior repository results, external sources, and theorem-specific derivations.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/equation_and_citation_map.md">Open the equation and citation map →</a></article>
        <article class="result"><h3>Citation policy</h3><p>Separate established external results from repository-original claims and from open research targets.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/citation_and_reference_policy.md">Read the citation policy →</a></article>
        <article class="result"><h3>Reference audit</h3><p>Review the repository-wide reference audit and source-quality checks.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/reference_audit.md">Open the reference audit →</a></article>
        <article class="result"><h3>Theorem roadmap</h3><p>Follow logical dependencies rather than assuming proposition number alone determines scientific dependence.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/theorem_roadmap.md">Open the theorem roadmap →</a></article>
        <article class="result"><h3>Falsification and evidence</h3><p>See which observations would challenge a declared descriptor, target channel, target model, or bridge claim.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/falsification_program.md">Open falsification and evidence →</a></article>
      </div>
      <p><strong>Repository-original theorem or computation</strong> and <strong>Open hypothesis or theorem target</strong> are deliberately different claim classes. The publication architecture keeps them separate so a proved conditional result is not confused with an unresolved physical or experiential hypothesis.</p>
    </section>

"""
        if provenance_marker not in text:
            raise RuntimeError("could not locate reproducibility section insertion point")
        text = text.replace(provenance_marker, provenance + provenance_marker, 1)

    path.write_text(text, encoding="utf-8")


def main() -> None:
    fix_start_here_typography()
    fix_website_contract()
    print("reader validation fixes applied")


if __name__ == "__main__":
    main()
