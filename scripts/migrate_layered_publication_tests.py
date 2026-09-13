"""Migrate legacy publication tests to the layered P88 reader architecture.

This maintenance script keeps scientific and reproducibility assertions intact while
moving presentation-specific assertions away from the historical monolithic README.
It is intentionally deterministic and idempotent so CI can apply it on the staging
branch before running the complete repository matrix.
"""

from __future__ import annotations

import ast
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def write(relative: str, text: str) -> None:
    path = ROOT / relative
    normalized = text.rstrip() + "\n"
    if path.read_text(encoding="utf-8") != normalized:
        path.write_text(normalized, encoding="utf-8")


def replace_once(relative: str, old: str, new: str) -> None:
    text = read(relative)
    if new in text:
        return
    if old not in text:
        raise RuntimeError(f"expected migration anchor missing in {relative}: {old!r}")
    write(relative, text.replace(old, new, 1))


def migrate_readme() -> None:
    path = "README.md"
    text = read(path)
    anchor = (
        "The current public theorem frontier is **P88**. "
        "The formal release remains **v0.82.0**."
    )
    block = """

| Research status | Current public value |
| --- | --- |
| Public theorem frontier | **P88** |
| Proposition-level results | **88** |
| Formal release | **v0.82.0** |
| Physical-to-experiential bridge | **Open** |

The [Theorem Roadmap](docs/theorem_roadmap.md) covers **P1 through P88 with explicit dependency branches**. The detailed theorem ledger lives in the [Detailed Proposition Record](docs/detailed_proposition_record.md), while the specialized P61-P70 optimization sequence lives in the [Calibration and Optimization Frontier](docs/calibration_optimization_frontier_p61_p70.md).

### Audit routes

For readers auditing provenance rather than reading the narrative linearly:

- [Research Navigation](docs/research_navigation.md)
- [Complete Figure Catalog](docs/figure_catalog.md)
- [Figure Caption and Description Standard](docs/figure_caption_and_description_standard.md)
- [Equation and Citation Map](docs/equation_and_citation_map.md)
- [Foundational Physics and Mathematics Bibliography](docs/foundational_physics_mathematics_bibliography.md)
- [Literature Map](docs/literature_map.md)
- [Fundamental Theory Program](docs/fundamental_theory_consciousness_program.md)
- [Fundamental Theory References](docs/fundamental_theory_references.bib)
- [Reference Audit](docs/reference_audit.md)
- [Citation and Reference Policy](docs/citation_and_reference_policy.md)
""".rstrip()
    marker = "### Audit routes"
    if marker not in text:
        if anchor not in text:
            raise RuntimeError("README frontier anchor missing")
        text = text.replace(anchor, anchor + block, 1)

    citation_old = (
        "For scholarly citation, see **[CITATION.md](CITATION.md)** and "
        "**[CITATION.cff](CITATION.cff)**."
    )
    citation_new = (
        "For scholarly citation, see **[CITATION.md](CITATION.md)**, "
        "**[CITATION.cff](CITATION.cff)**, and **[CITATION.bib](CITATION.bib)**."
    )
    if citation_old in text:
        text = text.replace(citation_old, citation_new, 1)
    write(path, text)


def migrate_start_here() -> None:
    path = "START_HERE.md"
    text = read(path)
    sentence = (
        "> **Current public record:** 88 proposition-level results through **P88**, "
        "with formal release **v0.82.0**. Direct frontier proof: "
        "[P88](docs/proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md)."
    )
    if "88 proposition-level results" not in text:
        lines = text.splitlines()
        insert_at = 1
        while insert_at < len(lines) and not lines[insert_at].strip():
            insert_at += 1
        lines[insert_at:insert_at] = [sentence, ""]
        text = "\n".join(lines)
    if "docs/proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md" not in text:
        text += "\n\n" + sentence
    write(path, text)


def migrate_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    prefix = (
        "[Start Here](../START_HERE.md) is the shortest reader-oriented entry point. "
        "The current documented theorem frontier is **P88**.\n\n"
        "| Current frontier | Direct proof |\n"
        "| --- | --- |\n"
        "| P88 | [Exact radius-three bounded primitive quad projection-parity separation]"
        "(proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md) |\n"
    )
    if "current documented theorem frontier is **P88**" not in text:
        lines = text.splitlines()
        insert_at = 1
        while insert_at < len(lines) and not lines[insert_at].strip():
            insert_at += 1
        lines[insert_at:insert_at] = [prefix, ""]
        text = "\n".join(lines)
    elif "START_HERE.md" not in text:
        text = text.replace(
            "The current documented theorem frontier is **P88**.",
            "[Start Here](../START_HERE.md) is the shortest reader-oriented entry point. "
            "The current documented theorem frontier is **P88**.",
            1,
        )
    write(path, text)


def migrate_lineage_page() -> None:
    path = "website/research-lineage.html"
    text = read(path)
    old = "whether the target itself is non-circular and measurable"
    new = "whether an independently justified experiential target or bridge principle is non-circular and measurable"
    if new not in text:
        if old not in text:
            raise RuntimeError("research-lineage bridge-boundary anchor missing")
        text = text.replace(old, new, 1)
    write(path, text)


def fix_unicode_contract_source() -> None:
    path = "scripts/modernize_publication_contract.py"
    text = read(path)
    em = chr(0x2014)
    en = chr(0x2013)
    text = text.replace(
        f'        assert "{em}" not in text, path',
        "        assert chr(0x2014) not in text, path",
    )
    text = text.replace(
        f'        assert "{en}" not in text, path',
        "        assert chr(0x2013) not in text, path",
    )
    write(path, text)

    punctuation_test = '''from pathlib import Path

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
'''
    write("tests/test_public_reader_punctuation.py", punctuation_test)


def _remove_legacy_reader_assertions(relative: str) -> None:
    text = read(relative)
    tree = ast.parse(text)
    lines = text.splitlines(keepends=True)
    ranges: list[tuple[int, int]] = []
    for node in tree.body:
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if node.end_lineno is None:
            continue
        segment = "".join(lines[node.lineno - 1 : node.end_lineno])
        presentation_bound = (
            "README" in segment
            or "research_navigation.md" in segment
            or "| P" in segment and "navigation" in segment.lower()
        )
        if presentation_bound:
            start = node.lineno - 1
            while start > 0 and not lines[start - 1].strip():
                start -= 1
            ranges.append((start, node.end_lineno))

    if not ranges:
        return
    for start, end in reversed(ranges):
        del lines[start:end]
    write(relative, "".join(lines))


def _append_layered_publication_test(
    relative: str,
    number: int,
    proof: str,
    figure: str,
    source: str,
    algorithm_test: str,
    calibration: bool = False,
) -> None:
    _remove_legacy_reader_assertions(relative)
    text = read(relative)
    marker = f"test_p{number}_layered_publication_route"
    if marker in text:
        return
    if "from pathlib import Path" not in text:
        text = "from pathlib import Path\n\n" + text
    extra = ""
    if calibration:
        extra = f'''
    calibration = root / "docs" / "calibration_optimization_frontier_p61_p70.md"
    calibration_text = calibration.read_text(encoding="utf-8")
    assert proof.name in calibration_text
    assert figure.name in calibration_text
'''
    block = f'''


def {marker}() -> None:
    root = Path(__file__).resolve().parents[1]
    proof = root / "docs" / "{proof}"
    figure = root / "docs" / "figures" / "{figure}"
    source = root / "src" / "consciousness_bridge" / "{source}"
    algorithm_test = root / "tests" / "{algorithm_test}"
    record = (root / "docs" / "detailed_proposition_record.md").read_text(encoding="utf-8")
    catalog = (root / "docs" / "figure_catalog.md").read_text(encoding="utf-8")
    readme = (root / "README.md").read_text(encoding="utf-8")

    for artifact in (proof, figure, source, algorithm_test):
        assert artifact.is_file(), artifact
    assert proof.name in record
    assert figure.name in catalog
    assert "docs/detailed_proposition_record.md" in readme
    assert "docs/figure_catalog.md" in readme
{extra.rstrip()}
'''
    write(relative, text.rstrip() + block)


def migrate_legacy_proposition_publication_tests() -> None:
    specs = {
        47: ("proposition_47_anytime_sequential_witness_graph.md", "p47_sequential_graph_refinement.svg", "sequential_witness_graph.py", "test_sequential_witness_graph.py", False),
        48: ("proposition_48_gap_dependent_stopping_complexity.md", "p48_gap_dependent_stopping_complexity.svg", "gap_stopping_complexity.py", "test_gap_stopping_complexity.py", False),
        49: ("proposition_49_dyadic_stopping_overhead.md", "p49_dyadic_stopping_overhead.svg", "dyadic_stopping_overhead.py", "test_dyadic_stopping_overhead.py", False),
        50: ("proposition_50_bounded_starvation_asynchronous_sampling.md", "p50_bounded_starvation_asynchronous_sampling.svg", "bounded_starvation_sampling.py", "test_bounded_starvation_sampling.py", False),
        51: ("proposition_51_heterogeneous_service_rate_stopping.md", "p51_heterogeneous_service_rate_stopping.svg", "heterogeneous_service_stopping.py", "test_heterogeneous_service_stopping.py", False),
        52: ("proposition_52_capacity_optimal_service_allocation.md", "p52_capacity_optimal_service_allocation.svg", "capacity_optimal_service_allocation.py", "test_capacity_optimal_service_allocation.py", False),
        53: ("proposition_53_residual_demand_reoptimization.md", "p53_residual_demand_reoptimization.svg", "residual_demand_reoptimization.py", "test_residual_demand_reoptimization.py", False),
        54: ("proposition_54_metric_switching_cost_residual_scheduling.md", "p54_metric_switching_cost_residual_scheduling.svg", "metric_switching_residual_schedule.py", "test_metric_switching_residual_schedule.py", False),
        55: ("proposition_55_pruning_aware_switching_monotonicity.md", "p55_pruning_aware_switching_monotonicity.svg", "pruning_aware_switching_monotonicity.py", "test_pruning_aware_switching_monotonicity.py", False),
        56: ("proposition_56_moving_start_metric_reoptimization_stability.md", "p56_moving_start_metric_reoptimization_stability.svg", "moving_start_metric_reoptimization.py", "test_moving_start_metric_reoptimization.py", False),
        57: ("proposition_57_switching_metric_perturbation.md", "p57_switching_metric_perturbation.svg", "switching_metric_perturbation.py", "test_switching_metric_perturbation.py", False),
        58: ("proposition_58_finite_data_metric_uncertainty.md", "p58_finite_data_metric_uncertainty.svg", "finite_data_metric_uncertainty.py", "test_finite_data_metric_uncertainty.py", False),
        59: ("proposition_59_optimal_transition_calibration.md", "p59_optimal_transition_calibration.svg", "optimal_transition_calibration.py", "test_optimal_transition_calibration.py", False),
        60: ("proposition_60_integer_transition_calibration.md", "p60_integer_transition_calibration.svg", "integer_transition_calibration.py", "test_integer_transition_calibration.py", False),
        61: ("proposition_61_exact_integer_transition_calibration.md", "p61_exact_integer_transition_calibration.svg", "exact_integer_transition_calibration.py", "test_exact_integer_transition_calibration.py", True),
        62: ("proposition_62_heterogeneous_cost_transition_calibration.md", "p62_heterogeneous_cost_transition_calibration.svg", "heterogeneous_cost_transition_calibration.py", "test_heterogeneous_cost_transition_calibration.py", True),
        63: ("proposition_63_exact_heterogeneous_integer_calibration.md", "p63_exact_heterogeneous_integer_calibration.svg", "exact_heterogeneous_integer_calibration.py", "test_exact_heterogeneous_integer_calibration.py", True),
        64: ("proposition_64_fast_heterogeneous_integer_approximation.md", "p64_fast_heterogeneous_integer_approximation.svg", "fast_heterogeneous_integer_approximation.py", "test_fast_heterogeneous_integer_approximation.py", True),
        65: ("proposition_65_lower_bounded_heterogeneous_calibration.md", "p65_lower_bounded_heterogeneous_calibration.svg", "lower_bounded_heterogeneous_calibration.py", "test_lower_bounded_heterogeneous_calibration.py", True),
        66: ("proposition_66_residual_exact_calibration_augmentation.md", "p66_residual_exact_calibration_augmentation.svg", "residual_exact_calibration_augmentation.py", "test_residual_exact_calibration_augmentation.py", True),
        67: ("proposition_67_global_integer_optimality_certificate.md", "p67_global_integer_optimality_certificate.svg", "global_integer_optimality_certificate.py", "test_global_integer_optimality_certificate.py", True),
        68: ("proposition_68_lagrangian_optimality_gap.md", "p68_lagrangian_optimality_gap.svg", "lagrangian_optimality_gap.py", "test_lagrangian_optimality_gap.py", True),
        69: ("proposition_69_dual_optimal_multiplier.md", "p69_dual_optimal_multiplier.svg", "dual_optimal_multiplier.py", "test_dual_optimal_multiplier.py", True),
        70: ("proposition_70_primal_dual_gap_decomposition.md", "p70_primal_dual_gap_decomposition.svg", "primal_dual_gap_decomposition.py", "test_primal_dual_gap_decomposition.py", True),
    }
    files = {
        47: ["tests/test_sequential_witness_graph_documentation.py"],
        48: ["tests/test_gap_stopping_complexity_documentation.py"],
        49: ["tests/test_dyadic_stopping_overhead_documentation.py"],
        50: ["tests/test_bounded_starvation_sampling_documentation.py"],
        51: ["tests/test_heterogeneous_service_stopping_documentation.py"],
        52: ["tests/test_capacity_optimal_service_allocation_documentation.py"],
        53: ["tests/test_residual_demand_reoptimization_documentation.py"],
        54: ["tests/test_metric_switching_residual_schedule_documentation.py", "tests/test_metric_switching_publication.py"],
        55: ["tests/test_pruning_aware_switching_monotonicity_documentation.py", "tests/test_pruning_aware_switching_publication.py"],
        56: ["tests/test_moving_start_metric_reoptimization_documentation.py", "tests/test_moving_start_metric_reoptimization_publication.py"],
        57: ["tests/test_switching_metric_perturbation_publication.py"],
        58: ["tests/test_finite_data_metric_uncertainty_publication.py"],
        59: ["tests/test_optimal_transition_calibration_publication.py"],
        60: ["tests/test_integer_transition_calibration_publication.py"],
        61: ["tests/test_exact_integer_transition_calibration_publication.py"],
        62: ["tests/test_heterogeneous_cost_transition_calibration_publication.py"],
        63: ["tests/test_exact_heterogeneous_integer_calibration_publication.py"],
        64: ["tests/test_fast_heterogeneous_integer_approximation_publication.py"],
        65: ["tests/test_p65_publication_integration.py"],
        66: ["tests/test_p66_publication_integration.py"],
        67: ["tests/test_p67_publication_integration.py"],
        68: ["tests/test_p68_publication_integration.py"],
        69: ["tests/test_p69_publication_integration.py"],
        70: ["tests/test_p70_publication_integration.py"],
    }
    for number, paths in files.items():
        spec = specs[number]
        for path in paths:
            _append_layered_publication_test(path, number, *spec)


def frontier_integration_test(number: int, proof: str, provenance: str, figure: str, source: str, algorithm_test: str) -> str:
    return f'''from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def test_p{number}_core_artifacts_exist() -> None:
    required = (
        DOCS / "{proof}",
        DOCS / "{provenance}",
        DOCS / "figures" / "{figure}",
        ROOT / "src" / "consciousness_bridge" / "{source}",
        ROOT / "tests" / "{algorithm_test}",
    )
    for path in required:
        assert path.is_file(), path


def test_p{number}_uses_layered_publication_surfaces() -> None:
    proof_path = DOCS / "{proof}"
    figure_path = DOCS / "figures" / "{figure}"
    roadmap = (DOCS / "theorem_roadmap.md").read_text(encoding="utf-8")
    record = (DOCS / "detailed_proposition_record.md").read_text(encoding="utf-8")
    catalog = (DOCS / "figure_catalog.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    assert proof_path.name in roadmap
    assert proof_path.name in record
    assert figure_path.name in catalog
    assert "docs/theorem_roadmap.md" in readme
    assert "docs/detailed_proposition_record.md" in readme
    assert "docs/figure_catalog.md" in readme


def test_p{number}_scientific_boundary_remains_explicit() -> None:
    proof = (DOCS / "{proof}").read_text(encoding="utf-8")
    provenance = (DOCS / "{provenance}").read_text(encoding="utf-8")
    source = (ROOT / "src" / "consciousness_bridge" / "{source}").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    combined = "\n".join((proof, provenance, source)).lower()

    assert "physical-to-experiential bridge" in combined
    assert "consciousness" in combined
    assert any(token in combined for token in ("does not", "remains open", "inconclusive"))
    assert "The bridge remains an open scientific problem." in readme


def test_p{number}_release_history_is_preserved() -> None:
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert "# 0.{number}.0" in changelog
    assert "Proposition {number}" in changelog
'''


def migrate_p75_p79_integration_tests() -> None:
    specs = {
        75: ("proposition_75_target_model_adequacy_overidentification.md", "p75_equation_provenance.md", "p75_target_model_adequacy_overidentification.svg", "target_model_adequacy.py", "test_target_model_adequacy.py"),
        76: ("proposition_76_finite_sample_target_model_adequacy.md", "p76_equation_provenance.md", "p76_finite_sample_target_model_adequacy.svg", "finite_sample_target_model_adequacy.py", "test_finite_sample_target_model_adequacy.py"),
        77: ("proposition_77_full_law_model_set_separation.md", "p77_equation_provenance.md", "p77_full_law_model_set_separation.svg", "full_law_model_set_separation.py", "test_full_law_model_set_separation.py"),
        78: ("proposition_78_certified_continuous_model_separation.md", "p78_equation_provenance.md", "p78_certified_continuous_model_separation.svg", "certified_continuous_model_separation.py", "test_certified_continuous_model_separation.py"),
        79: ("proposition_79_certified_sampling_radius.md", "p79_equation_provenance.md", "p79_certified_sampling_radius.svg", "certified_sampling_radius.py", "test_certified_sampling_radius.py"),
    }
    for number, spec in specs.items():
        write(f"tests/test_p{number}_research_integration.py", frontier_integration_test(number, *spec))


def migrate_document_link_test() -> None:
    content = r'''import re
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
            destination = (
                ROOT / path_part.lstrip("/")
                if path_part.startswith("/")
                else (source.parent / path_part).resolve()
                if path_part
                else source.resolve()
            )
            try:
                destination.relative_to(ROOT.resolve())
            except ValueError:
                failures.append(f"{source.relative_to(ROOT)} -> {target}: target leaves repository")
                continue
            if not destination.exists():
                failures.append(f"{source.relative_to(ROOT)} -> {target}: file does not exist")
                continue
            if separator and fragment and destination.suffix.lower() == ".md":
                anchors = anchor_cache.setdefault(destination, _anchors(destination))
                if fragment not in anchors:
                    failures.append(f"{source.relative_to(ROOT)} -> {target}: anchor does not exist")
    assert not failures, "\n".join(failures)


def test_reader_navigation_routes_to_complete_archives():
    navigation = (ROOT / "docs/research_navigation.md").read_text(encoding="utf-8")
    record = (ROOT / "docs/detailed_proposition_record.md").read_text(encoding="utf-8")
    assert "detailed_proposition_record.md" in navigation
    assert "theorem_roadmap.md" in navigation
    for number in range(1, 89):
        assert f"proposition_{number}_" in record


def test_main_page_routes_to_reader_and_provenance_layers():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    required = (
        "START_HERE.md",
        "docs/research_map.md",
        "docs/research_navigation.md",
        "docs/theorem_roadmap.md",
        "docs/detailed_proposition_record.md",
        "docs/equation_and_citation_map.md",
        "docs/citation_and_reference_policy.md",
        "docs/reference_audit.md",
        "CITATION.md",
    )
    for path in required:
        assert path in text
'''
    write("tests/test_document_link_integrity.py", content)


def migrate_reader_guide_test() -> None:
    content = '''from pathlib import Path

README = Path(__file__).resolve().parents[1] / "README.md"


def test_reader_guide_routes_each_audience_to_the_correct_layer() -> None:
    text = README.read_text(encoding="utf-8")
    required = (
        "[Start here](START_HERE.md)",
        "[Research map](docs/research_map.md)",
        "[Visual atlas](docs/figure_catalog.md)",
        "[Technical record](docs/detailed_proposition_record.md)",
        "[Reproduce the work](docs/reproducibility.md)",
        "[Theorem Roadmap](docs/theorem_roadmap.md)",
        "[Equation and Citation Map](docs/equation_and_citation_map.md)",
        "[Research Navigation](docs/research_navigation.md)",
        "[Calibration and Optimization Frontier](docs/calibration_optimization_frontier_p61_p70.md)",
    )
    for link in required:
        assert link in text


def test_compact_homepage_does_not_duplicate_the_full_proposition_ledger() -> None:
    text = README.read_text(encoding="utf-8")
    assert "docs/detailed_proposition_record.md" in text
    assert text.count("proposition_88_exact_radius_three") == 1
    assert "The bridge remains an open scientific problem." in text
'''
    write("tests/test_reader_guide_links.py", content)


def migrate_citation_test() -> None:
    content = r'''import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
CFF = ROOT / "CITATION.cff"
BIB = ROOT / "CITATION.bib"
GUIDE = ROOT / "CITATION.md"
PYPROJECT = ROOT / "pyproject.toml"


def _project_version() -> str:
    text = PYPROJECT.read_text(encoding="utf-8")
    match = re.search(r'^version\s*=\s*"([^"]+)"', text, flags=re.MULTILINE)
    assert match is not None
    return match.group(1)


def _frontier() -> int:
    numbers = []
    for path in (ROOT / "docs").glob("proposition_*_*.md"):
        match = re.match(r"proposition_(\d+)_", path.name)
        if match:
            numbers.append(int(match.group(1)))
    assert numbers
    return max(numbers)


def test_main_page_routes_to_professional_citation_surfaces() -> None:
    text = README.read_text(encoding="utf-8")
    for path in ("CITATION.md", "CITATION.cff", "CITATION.bib"):
        assert path in text
    assert "## Citation and license" in text


def test_machine_readable_citation_metadata_has_preferred_research_citation() -> None:
    text = CFF.read_text(encoding="utf-8")
    version = _project_version()
    frontier = _frontier()
    assert "cff-version: 1.2.0" in text
    assert f"version: {version}" in text
    assert "license: MIT" in text
    assert "family-names: Keikha" in text
    assert "given-names: Mahsa" in text
    assert "preferred-citation:" in text
    assert "type: generic" in text
    assert "year: 2026" in text
    assert "Physical-to-Experiential Bridge Problem" in text
    assert "lower-bounded heterogeneous calibration" in text
    assert "primal-dual gap decomposition" in text
    assert f"Current documented theorem frontier: P{frontier}" in text
    assert 'url: "https://github.com/MahsaKeikha/mathematical-consciousness-bridge"' in text


def test_bibtex_and_citation_guide_are_present_and_version_aligned() -> None:
    bib = BIB.read_text(encoding="utf-8")
    guide = GUIDE.read_text(encoding="utf-8")
    version = _project_version()
    frontier = _frontier()
    assert "keikha2026mathematicalconsciousnessbridge" in bib
    assert f"version      = {{{version}}}" in bib
    assert "@misc" in bib
    assert "## Preferred scholarly citation" in guide
    assert "## Version-specific reproducibility" in guide
    assert "## DOI and archival status" in guide
    assert f"P{frontier}" in guide
'''
    write("tests/test_citation_surface.py", content)


def migrate_release_metadata_test() -> None:
    content = r'''import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _project_version() -> str:
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    match = re.search(r'^version = "([0-9]+\.[0-9]+\.[0-9]+)"$', pyproject, re.MULTILINE)
    assert match is not None
    return match.group(1)


def test_release_versions_are_synchronized():
    version = _project_version()
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    assert f"version-{version}-2563eb" in readme
    assert re.search(rf"^version: {re.escape(version)}$", citation, re.MULTILINE)


def test_historical_theorem_artifacts_live_on_authoritative_archive_layers():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    record = (ROOT / "docs/detailed_proposition_record.md").read_text(encoding="utf-8")
    calibration = (ROOT / "docs/calibration_optimization_frontier_p61_p70.md").read_text(encoding="utf-8")

    assert "docs/detailed_proposition_record.md" in readme
    assert "docs/calibration_optimization_frontier_p61_p70.md" in readme
    for proposition in range(39, 61):
        proofs = list((ROOT / "docs").glob(f"proposition_{proposition}_*.md"))
        figures = list((ROOT / "docs/figures").glob(f"p{proposition}_*.svg"))
        assert len(proofs) == 1
        assert figures
        assert proofs[0].name in record
    for proposition in range(61, 71):
        proofs = list((ROOT / "docs").glob(f"proposition_{proposition}_*.md"))
        figures = list((ROOT / "docs/figures").glob(f"p{proposition}_*.svg"))
        assert len(proofs) == 1
        assert figures
        assert proofs[0].name in calibration
        assert figures[0].name in calibration
'''
    write("tests/test_release_metadata_consistency.py", content)


def migrate_fundamental_theory_test() -> None:
    content = r'''import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
PROGRAM = ROOT / "docs" / "fundamental_theory_consciousness_program.md"
STOCHASTIC = ROOT / "docs" / "stochastic_fundamental_bridge.md"
MAP = ROOT / "docs" / "figures" / "fundamental_theory_consciousness_map.svg"
NS = {"svg": "http://www.w3.org/2000/svg"}


def test_main_page_routes_to_fundamental_theory_interface():
    readme = README.read_text(encoding="utf-8")
    program = PROGRAM.read_text(encoding="utf-8")
    assert "docs/fundamental_theory_consciousness_program.md" in readme
    for phrase in (
        "There is currently no experimentally established Theory of Everything",
        "T(\\Omega)=\\bigl(G(\\Omega),Q(\\Omega),C(\\Omega)\\bigr)",
        "fundamental_theory_consciousness_map.svg",
    ):
        assert phrase in program


def test_speculative_antecedents_are_not_presented_as_scientific_fact():
    program = PROGRAM.read_text(encoding="utf-8")
    assert "Thomas W. Campbell" in program
    assert "not established scientific facts" in program
    assert "speculative falsifiable proposal" in program


def test_program_defines_exact_factorization_failure_and_controls():
    text = PROGRAM.read_text(encoding="utf-8")
    assert "E=B_T\\circ T" in text
    assert "\\Omega\\sim_T\\Omega'" in text
    assert "d_{\\mathrm{TOE}}^{\\perp}" in text
    assert "R_{E|T}" in text
    assert "No-free-metaphysics rule" in text
    assert "The last possibility matters" in text


def test_stochastic_bridge_defines_conditional_information_residual():
    text = STOCHASTIC.read_text(encoding="utf-8")
    assert "Markov kernel" in text
    assert "E\\perp\\!\\!\\!\\perp\\Omega\\mid T" in text
    assert "I(E;\\Omega\\mid T)=0" in text
    assert "\\mathcal I_{\\perp}^{\\mathrm{fund}}" in text
    assert "I(E;Z\\mid T)" in text
    assert "omitted physical variable" in text
    assert "would automatically prove" in text


def test_fundamental_theory_map_is_valid_svg_with_scientific_boundary():
    text = MAP.read_text(encoding="utf-8")
    assert "<svg" in text
    assert "Fundamental Theory to Consciousness" in text
    assert "Complete declared physical map" in text
    assert "Bridge factorization / residual test" in text
    assert "would not by itself prove" in text


def test_fundamental_theory_map_has_complete_attached_arrow_architecture():
    root = ET.parse(MAP).getroot()
    arrows = {
        path.attrib["id"]: path
        for path in root.findall("svg:path", NS)
        if path.attrib.get("id", "").startswith("arrow-")
    }
    expected_routes = {
        "arrow-fundamental-geometry": "M900 305 V360 H260 V405",
        "arrow-fundamental-quantum": "M900 305 V360 H690 V405",
        "arrow-fundamental-causal": "M900 305 V360 H1110 V405",
        "arrow-fundamental-experiential": "M900 305 V360 H1540 V405",
        "arrow-geometry-physical": "M260 625 V655 H760 V690",
        "arrow-quantum-physical": "M690 625 V690",
        "arrow-causal-physical": "M1110 625 V690",
        "arrow-physical-bridge": "M900 855 V930",
        "arrow-experiential-bridge": "M1540 625 V1032 H1380",
    }
    assert set(arrows) == set(expected_routes)
    for arrow_id, route in expected_routes.items():
        arrow = arrows[arrow_id]
        assert arrow.attrib["d"] == route
        assert arrow.attrib.get("marker-end") is None
        assert "marker-end:url(#arrow)" not in arrow.attrib.get("style", "")
        assert arrow.attrib["data-source"]
        assert arrow.attrib["data-target"]
    style_text = "".join(root.find("svg:defs/svg:style", NS).itertext())
    assert ".arrow{stroke:#64748b;stroke-width:2.4;fill:none;marker-end:url(#arrow)}" in style_text
    assert ".dash{stroke:#94a3b8;stroke-width:2.2;stroke-dasharray:9 8;fill:none;marker-end:url(#arrow)}" in style_text
    assert arrows["arrow-geometry-physical"].attrib["data-target"] == "physical-map"
    assert arrows["arrow-quantum-physical"].attrib["data-target"] == "physical-map"
    assert arrows["arrow-causal-physical"].attrib["data-target"] == "physical-map"
    assert arrows["arrow-experiential-bridge"].attrib["data-target"] == "bridge-test"
    assert arrows["arrow-experiential-bridge"].attrib["data-source"] == "experiential"
    assert arrows["arrow-physical-bridge"].attrib["data-target"] == "bridge-test"
'''
    write("tests/test_fundamental_theory_program.py", content)


def migrate_theorem_roadmap_caption_test() -> None:
    content = r'''import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
FIGURE = ROOT / "docs" / "figures" / "theorem_roadmap.svg"
CATALOG = ROOT / "docs" / "figure_catalog.md"


def _frontier() -> int:
    numbers = []
    for path in (ROOT / "docs").glob("proposition_*_*.md"):
        match = re.match(r"proposition_(\d+)_", path.name)
        if match:
            numbers.append(int(match.group(1)))
    assert numbers
    return max(numbers)


def test_readme_routes_the_complete_theorem_scope_to_the_roadmap():
    text = README.read_text(encoding="utf-8")
    frontier = _frontier()
    assert f"P1 through P{frontier} with explicit dependency branches" in text
    assert "docs/theorem_roadmap.md" in text
    assert "docs/detailed_proposition_record.md" in text


def test_theorem_roadmap_embedded_description_explains_arrow_semantics():
    text = FIGURE.read_text(encoding="utf-8")
    assert "the theorem roadmap for Propositions 1 through 31" in text
    assert "follow the arrows, not just the page order" in text
    assert "An absent arrow means that the figure is not asserting a prerequisite." in text
    assert "separate continuations" in text


def test_figure_catalog_preserves_specific_roadmap_description():
    text = CATALOG.read_text(encoding="utf-8")
    assert "Theorem dependency map for P1-P31" in text
    assert "the arrow topology records dependency structure" in text
'''
    write("tests/test_theorem_roadmap_caption.py", content)


def migrate_website_build_test() -> None:
    path = "tests/test_website_build.py"
    text = read(path)
    old = '''    assert '>Research Lineage</a>' not in built
    assert '>Research Map</a>' not in built
    assert '>Physics &amp; Math</a>' not in built
    assert '>Visual Atlas</a>' not in built
    assert '>Research</a>' in built
    assert '>Explore</a>' in built
'''
    new = '''    assert '>Research Lineage</a>' not in built
    assert '>Research Map</a>' not in built
    assert '>Physics &amp; Math</a>' not in built
    assert '>Visual Atlas</a>' not in built
    assert '>Research II</a>' in built
    assert '>Research III</a>' in built
    assert '>Explore</a>' in built
'''
    if new not in text:
        if old not in text:
            raise RuntimeError("website build fallback-navigation assertion block missing")
        text = text.replace(old, new, 1)
    write(path, text)


def migrate_website_lineage_test() -> None:
    content = '''from pathlib import Path


def test_research_lineage_connects_all_public_repositories() -> None:
    page = Path("website/research-lineage.html").read_text(encoding="utf-8")
    required = (
        "Spatiotemporal Observer Mathematics",
        "Mathematical Consciousness Bridge",
        "Consciousness Measurement Science",
        "https://github.com/MahsaKeikha/spatiotemporal-observer-math",
        "https://github.com/MahsaKeikha/mathematical-consciousness-bridge",
        "https://github.com/MahsaKeikha/consciousness-measurement-science",
        "Research I repository",
        "Research II",
        "Research III",
        "physical subsystem identification",
        "physical-to-experiential bridge",
    )
    for token in required:
        assert token in page


def test_lineage_preserves_scientific_boundary_between_projects() -> None:
    page = Path("website/research-lineage.html").read_text(encoding="utf-8")
    required = (
        "A recovered subsystem is not automatically a conscious subject",
        "Bridge remains an independently testable open problem",
        "not a proof chain to consciousness",
        "independently justified experiential target or bridge principle",
    )
    for token in required:
        assert token in page


def test_lineage_exposes_auditable_research_one_entry_points() -> None:
    page = Path("website/research-lineage.html").read_text(encoding="utf-8")
    required_paths = (
        "docs/visual_research_guide.md",
        "docs/research_overview.md",
        "docs/research_index.md",
        "docs/physics_guide.md",
        "docs/assumption_ledger.md",
    )
    for path in required_paths:
        assert path in page


def test_global_website_navigation_includes_current_research_lineage() -> None:
    script = Path("website/app.js").read_text(encoding="utf-8")
    assert "research-lineage.html" in script
    assert "Research Lineage" in script
    assert "spatiotemporal-observer-math" in script
    assert "Research II" in script
    assert "Research III" in script
'''
    write("tests/test_website_research_lineage.py", content)


def main() -> None:
    migrate_readme()
    migrate_start_here()
    migrate_navigation()
    migrate_lineage_page()
    fix_unicode_contract_source()
    migrate_legacy_proposition_publication_tests()
    migrate_p75_p79_integration_tests()
    migrate_document_link_test()
    migrate_reader_guide_test()
    migrate_citation_test()
    migrate_release_metadata_test()
    migrate_fundamental_theory_test()
    migrate_theorem_roadmap_caption_test()
    migrate_website_build_test()
    migrate_website_lineage_test()


if __name__ == "__main__":
    main()
