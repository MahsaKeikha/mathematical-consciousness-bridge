    p92_block = rf'''## P92: exact global mixed-prevalence distance

P92 closes the P91 bracket exactly. On the `X1 = 1` observable subtensor, every two-component P75 mixture has three conditional two-by-two determinants whose product is nonnegative. For the established empirical witness those determinants are `-1/48`, `1/64`, and `5/192`, with exact sign-stability radii `1/24`, `3/56`, and `5/72`.

Any law closer than `1/24` therefore keeps sign pattern `(-,+,+)` and has negative determinant product, which is impossible for P75. The P91 mixed rational point attains distance exactly `1/24`, so

\[
\\boxed{{d_\\infty(P_{{\\mathrm{{emp}}}},\\mathcal M_{{75}})=\\frac{{1}}{{24}}.}}
\]

- [P92]({PROOF})
- Provenance: [{PROVENANCE}]({PROVENANCE})
- Figure: [P92 exact global distance](figures/{FIGURE})
- Source: [`{SOURCE}`](../src/consciousness_bridge/{SOURCE})
- Tests: [`{TEST}`](../tests/{TEST})

P92 is a conditional model-separation theorem and does not identify consciousness or close the physical-to-experiential bridge.'''
    if "## P92: exact global mixed-prevalence distance" not in text:
        text = text.replace("\n## After P92", "\n" + p92_block + "\n\n## After P92", 1)
    text = text.replace(
        "Natural P92 directions include tightening the mixed-prevalence global distance bracket, combining several rank-two minors into a stronger exact certificate, or deriving a finite-sample rejection theorem specialized to the P91 algebraic witness.",
        "Natural P93 directions include finite-sample calibration of the P92 nonlinear sign certificate, stability under alternative observable slicings, or exact comparison with broader latent-class families.",
    )
    write(path, text)


def promote_records() -> None:
    path = "docs/detailed_proposition_record.md"
    text = replace_many(
        read(path),
        (
            ("## Complete P1 to P91 chronology", "## Complete P1 to P92 chronology"),
            ("P1 through P91", "P1 through P92"),
        ),