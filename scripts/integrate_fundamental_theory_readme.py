from pathlib import Path


README = Path(__file__).resolve().parents[1] / "README.md"
SENTINEL = "# 4.4 Fundamental theory / Theory-of-Everything interface"
ANCHOR = "---\n\n# 5. Probability, distinguishability, and information geometry"

SECTION = r'''---

# 4.4 Fundamental theory / Theory-of-Everything interface

![Fundamental Theory to Consciousness map](docs/figures/fundamental_theory_consciousness_map.svg)

There is currently **no experimentally established Theory of Everything** unifying quantum theory, the Standard Model, and gravity. This project therefore does not insert a preferred TOE as scientific fact. Instead it defines a common mathematical interface into which candidate fundamental theories can be placed and compared.

Let

\[
\boxed{\Omega\in\mathcal M}
\]

be a state of a declared candidate fundamental theory. From the same underlying state define

\[
\boxed{
G:\mathcal M\to\mathcal Q_G,
\qquad
Q:\mathcal M\to\mathcal Q_Q,
\qquad
C:\mathcal M\to\mathcal Q_C,
\qquad
E:\mathcal M\to\mathcal Q_E,
}
\]

where \(G\) is geometric/spacetime structure, \(Q\) is quantum-operational structure, \(C\) is intervention-resolved causal structure, and \(E\) is independently formalized experiential structure. The declared complete physical descriptor is

\[
\boxed{T(\Omega)=\bigl(G(\Omega),Q(\Omega),C(\Omega)\bigr).}
\]

The conservative physical-reduction hypothesis is the factorization

\[
\boxed{E=B_T\circ T.}
\]

The exact no-factorization witness is therefore

\[
\boxed{
T(\Omega)=T(\Omega')
\quad\text{but}\quad
E(\Omega)\ne E(\Omega')
\Longrightarrow
\nexists B_T\text{ consistent with both states}.
}
\]

This gives the project a rigorous way to investigate a very broad question without deciding the metaphysics in advance: **spacetime and experiential structure may be tested as different quotient structures of a deeper candidate state, while factorization determines whether the experiential quotient is already fixed by the complete physical quotient.**

For local smooth coordinates, define the transverse residual

\[
\boxed{
d_{\mathrm{TOE}}^{\perp}
=
\operatorname{rank}D(\Psi_T,\Psi_E)
-
\operatorname{rank}D\Psi_T.
}
\]

If \(\Psi_E=g\circ\Psi_T\), then necessarily \(d_{\mathrm{TOE}}^{\perp}=0\). A certified positive residual would rule out that local factorization relative to the declared physical representation. It would **not** by itself establish a fifth spatial dimension, nonphysical substance, simulation ontology, or failure of quantum mechanics.

## Scientific anchors

The fundamental-theory layer is motivated by peer-reviewed work showing that quantum information can constrain questions about gravity and emergent spacetime: Jacobson's entanglement-equilibrium derivation of the semiclassical Einstein equation, holographic quantum error-correcting-code models, recent information-theoretic quantum-gravity test programs, and holographic spacetime/entanglement relations. The experiential side is kept independent using mathematical consciousness frameworks and adversarial empirical theory testing.

## Where *My Big TOE* fits

Thomas W. Campbell's *My Big TOE* proposes that consciousness is fundamental and physical reality is virtual. Those broad claims are **not treated as established scientific facts here**. Campbell, Owhadi, Sauvageau, and Watkinson did publish a narrower simulation-theory experiment proposal based on explicit finite-resource assumptions and wave/particle tests. That work is included only as a **speculative, falsifiable antecedent**, not as a premise of the present framework.

The scientific rule is simple: an additional primitive must change a measurable prediction, improve out-of-sample explanatory power, resolve a proved factorization failure, or produce a new falsifiable invariant. Otherwise it is not an identifiable new component of reality.

[Read the full Fundamental Theory to Consciousness program](docs/fundamental_theory_consciousness_program.md).

'''


def main() -> None:
    text = README.read_text(encoding="utf-8")
    if SENTINEL in text:
        return
    if ANCHOR not in text:
        raise RuntimeError("README insertion anchor not found")

    text = text.replace(ANCHOR, SECTION + "# 5. Probability, distinguishability, and information geometry", 1)

    paper_row = (
        "| **4. Quantum completeness test** | What exact result would show failure of a quantum-only experiential reduction? |"
    )
    added_row = (
        paper_row
        + "\n| **4.4 Fundamental-theory interface** | Can spacetime, quantum, causal, and experiential structure be tested as quotients of one candidate fundamental state? |"
    )
    if paper_row in text and "**4.4 Fundamental-theory interface**" not in text:
        text = text.replace(paper_row, added_row, 1)

    record_row = "| quantum operational-completeness test | **formal open theorem target** |"
    added_record = (
        record_row
        + "\n| fundamental-theory factorization test | **formal open theorem + experiment target** |"
    )
    if record_row in text and "fundamental-theory factorization test" not in text:
        text = text.replace(record_row, added_record, 1)

    README.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
