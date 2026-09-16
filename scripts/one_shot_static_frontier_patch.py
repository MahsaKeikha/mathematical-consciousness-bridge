from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_exact(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"Expected exactly one {label}, found {count}")
    return text.replace(old, new, 1)


def patch_start_here() -> None:
    path = ROOT / "START_HERE.md"
    text = path.read_text(encoding="utf-8")
    replacements = (
        (
            "The public theorem frontier is **P99**. The formal release is **v0.82.0**.",
            "The public theorem frontier is **P100**. The formal release is **v0.82.0**.",
            "Start Here public frontier",
        ),
        (
            "You do not need to read 99 propositions to understand the project.",
            "You do not need to read 100 propositions to understand the project.",
            "Start Here proposition count",
        ),
        (
            "| Read the current frontier result | **[P99](docs/proposition_99_cross_fitted_evalue_aggregation.md)** |",
            "| Read the current frontier result | **[P100](docs/proposition_100_anytime_sequential_eprocess.md)** |",
            "Start Here current-frontier link",
        ),
    )
    for old, new, label in replacements:
        text = replace_exact(text, old, new, label)
    path.write_text(text, encoding="utf-8")


def patch_reproducibility() -> None:
    path = ROOT / "docs" / "reproducibility.md"
    text = path.read_text(encoding="utf-8")
    text = replace_exact(
        text,
        "| Run only the current P99 theorem checks | focused P99 commands below |",
        "| Run only the current P100 theorem checks | focused P100 commands below |",
        "reproducibility current-frontier route",
    )
    path.write_text(text, encoding="utf-8")


def patch_citation() -> None:
    path = ROOT / "CITATION.md"
    text = path.read_text(encoding="utf-8")

    replacements = (
        (
            "This is the preferred citation for the research program at the current documented frontier, P99.",
            "This is the preferred citation for the research program at the current documented frontier, P100.",
            "preferred citation frontier",
        ),
        (
            "note         = {Ongoing research program. Current documented theorem frontier: P99.}",
            "note         = {Ongoing research program. Current documented theorem frontier: P100.}",
            "BibTeX frontier note",
        ),
        (
            "The current citation metadata identify Version **0.82.0** and theorem frontier **P99**.",
            "The current citation metadata identify Version **0.82.0** and theorem frontier **P100**.",
            "citation metadata frontier",
        ),
        (
            "## Previous theorem frontier: P97\n\nThe current documented theorem frontier is **P97**.",
            "## Earlier theorem frontier: P97\n\nAt that stage, the documented theorem frontier was **P97**.",
            "historical P97 frontier label",
        ),
        (
            "## Immediate predecessor theorem frontier: P98\n\nThe current documented theorem frontier is **P98**.",
            "## Earlier theorem frontier: P98\n\nAt that stage, the documented theorem frontier was **P98**.",
            "historical P98 frontier label",
        ),
    )
    for old, new, label in replacements:
        text = replace_exact(text, old, new, label)

    start = text.index("## Current theorem frontier: P100")
    end = text.index("## Earlier theorem frontier: P98", start)
    current_and_p99 = '''## Current theorem frontier: P100

The current documented theorem frontier is **P100**. P100 composes genuinely fresh P99 certification rounds into an anytime-valid sequential evidence process. For each round, the P99 e-value must remain conditionally valid given the accumulated past, and the reserve stake must be chosen predictably before that round's certification data are inspected. Under those conditions, the reserve-stake product is a nonnegative supermartingale and Ville's inequality controls threshold crossing under repeated inspection and adaptive stopping.

At the exact 95 percent checkpoint, one moderate P99 round has `E_t = 25/2` and a half stake gives `F_t = 27/4`. Two fresh rounds give `M_2 = 729/16 = 45.5625 > 20`, with declared two-round unique-data totals `30192 / 30336`.

P100 is a conditional sequential-inference theorem. It does not make reused certification data fresh, permit current-round leakage, establish model acceptance, identify consciousness, establish nonphysicality, or complete the physical-to-experiential bridge.

## Immediate predecessor theorem frontier: P99

At the preceding stage, the documented theorem frontier was **P99**. P99 turns selection-valid P96/P98 fold rejection indicators into exact e-values, permits a finite calibration mixture fixed before own-fold evaluation, and combines the resulting cross-fitted fold evidence by a fixed convex average. The aggregate remains a valid e-value without assuming the final fold certificates are independent, and a global level-alpha rejection is obtained at aggregate e-value at least `1/alpha`.

For the declared two-fold, two-regime, one-step-dependent distributed-evidence checkpoint at 95 percent confidence, the per-regime crossing is **3774** and the first denominator-24 exact replication is **3792**, with unique totals **15096 / 15168**. This is a configuration-specific gain over the matched equal-split P98 checkpoint, not a uniform dominance claim.

P99 is a conditional model-rejection theorem. It does not justify own-fold leakage, post-hoc calibration search, naive dependent-stream splitting, model acceptance after non-rejection, consciousness identification, nonphysicality, or completion of the physical-to-experiential bridge.

'''
    text = text[:start] + current_and_p99 + text[end:]
    path.write_text(text, encoding="utf-8")


def write_test() -> None:
    path = ROOT / "tests" / "test_static_p100_frontier_docs.py"
    path.write_text(
        '''from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_start_here_points_to_p100_frontier() -> None:
    text = (ROOT / "START_HERE.md").read_text(encoding="utf-8")
    assert "The public theorem frontier is **P100**." in text
    assert "You do not need to read 100 propositions" in text
    assert "[P100](docs/proposition_100_anytime_sequential_eprocess.md)" in text
    assert "The public theorem frontier is **P99**." not in text


def test_reproducibility_route_names_p100_as_current() -> None:
    text = (ROOT / "docs" / "reproducibility.md").read_text(encoding="utf-8")
    assert "Run only the current P100 theorem checks" in text
    assert "focused P100 commands below" in text
    assert "Run only the current P99 theorem checks" not in text


def test_citation_guide_has_one_current_p100_frontier() -> None:
    text = (ROOT / "CITATION.md").read_text(encoding="utf-8")
    assert "current documented frontier, P100" in text
    assert "Current documented theorem frontier: P100" in text
    assert "theorem frontier **P100**" in text
    assert "## Current theorem frontier: P100" in text
    assert "## Immediate predecessor theorem frontier: P99" in text
    assert "At the preceding stage, the documented theorem frontier was **P99**." in text
    assert "## Earlier theorem frontier: P98" in text
    assert "At that stage, the documented theorem frontier was **P98**." in text
    assert "## Earlier theorem frontier: P97" in text
    assert "At that stage, the documented theorem frontier was **P97**." in text
    assert "current documented frontier, P99" not in text
    assert "theorem frontier **P99**" not in text
''',
        encoding="utf-8",
    )


if __name__ == "__main__":
    patch_start_here()
    patch_reproducibility()
    patch_citation()
    write_test()
