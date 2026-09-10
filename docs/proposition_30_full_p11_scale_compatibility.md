# Proposition 30: Full declared P11 scale compatibility

## Status

**Proved assembly theorem for the declared physical signature.** P30 combines the independently established scale results for the P11 response geometry, directed influence, and partition irreducibility. It does not identify consciousness, prove physical completeness, establish genuine physical fusion, or solve intervention/time aggregation.

## 1. Problem

P11 defines an intervention-resolved physical candidate schematically as

\[
\mathfrak C
=
(V,\mathcal U,\mathcal T,\mathcal G,\mathcal A,\mathcal K).
\]

P27, P28, and P29 solve different parts of its changing-node scale problem:

- P27 transports the partition semantics and \(\mathcal K\) through a surjective node quotient.
- P28 transports matched source-intervention semantics and \(\mathcal A\).
- P29 transports the complete response geometry \(\mathcal G\) on a fixed intervention-delay grid.

Those results cannot simply be concatenated. A valid full-signature scale claim requires them to refer to one common scale declaration.

## 2. Shared scale declaration

Let

\[
a:V_f\twoheadrightarrow V_c
\]

be one declared surjective node quotient. Let \(C_a\) be one declared aggregation-compatible state map and let \(R\) denote the reconstruction family used to audit lost information.

For the P30 theorem, the intervention and delay label sets are retained:

\[
\mathcal U_c=\mathcal U_f=\mathcal U,
\qquad
\mathcal T_c=\mathcal T_f=\mathcal T.
\]

This assumption is deliberate. P30 does not infer an intervention quotient or a time quotient.

The assembly is admissible only if all of the following hold.

### C1. Partition compatibility

The fine partitions used in the comparison are saturated by the fibers of \(a\), so P27 lift/descent applies.

### C2. Source-pair compatibility

For every matched intervention pair \(e\), P28 source incidence satisfies

\[
|\{a(i): i\in S_f(e)\}|\le1.
\]

### C3. Response-grid compatibility

P29 is evaluated on one common intervention-delay grid \(\mathcal U\times\mathcal T\).

### C4. Common state map

The coarse response laws used by \(\mathcal G\), \(\mathcal A\), and \(\mathcal K\) are induced by the same declared physical state map \(C_a\), with component marginals or partition products taken only where the earlier propositions justify them.

### C5. Common reconstruction declaration

The reconstruction defects used in the three component bounds refer to one declared reconstruction family or to explicitly compatible restrictions of that family.

These conditions prevent a mathematically invalid assembly in which each component is certified under a different quotient, experiment grid, or coarse state representation.

## 3. Component distortions

Define

\[
D_G
=
\|\mathcal G_f-\mathcal G_c\|_\infty,
\]

\[
D_A
=
\|\mathcal A_f-\mathcal A_c\|_\infty,
\]

where the supremum is taken only over source-target-delay entries whose source semantics satisfy P28, and

\[
D_K
=
\sup_{\pi_c}
\left|
\kappa_f(L_a\pi_c)-\kappa_c(\pi_c)
\right|,
\]

where \(L_a\pi_c\) is the P27 saturated lift.

The full declared P11 distortion vector is

\[
\boxed{
\mathbf D_{P11}(a)
=
(D_G,D_A,D_K).
}
\]

## 4. Component reconstruction budgets

Let \(\rho_G^*\) be the uniform P29 response-family reconstruction defect relevant to the geometry grid. Let \(\rho_A^*\) be the uniform P28/P25 target-fiber reconstruction defect relevant to directed influence. Let \(\rho_P^*\) and \(\rho_{\Pi}^*\) bound reconstruction error for actual response laws and their partition-product references in the P27/P26 branch.

The earlier propositions give

\[
D_G\le2\rho_G^*,
\]

\[
D_A\le2\rho_A^*,
\]

and

\[
D_K\le\rho_P^*+\rho_{\Pi}^*.
\]

Define the uniform P11 scale budget

\[
\boxed{
\varepsilon_{P11}
=
\max\left\{
2\rho_G^*,
2\rho_A^*,
\rho_P^*+\rho_{\Pi}^*
\right\}.
}
\]

## 5. Proposition

**Proposition 30.** Suppose C1-C5 hold for one shared scale declaration \((a,C_a,R,\mathcal U,\mathcal T)\), and suppose the P27/P26, P28/P25, and P29 component hypotheses hold on their corresponding domains. Then

\[
\boxed{
\|\mathbf D_{P11}(a)\|_\infty
\le
\varepsilon_{P11}.
}
\]

Equivalently,

\[
\boxed{
\max\{D_G,D_A,D_K\}
\le
\max\left\{
2\rho_G^*,
2\rho_A^*,
\rho_P^*+\rho_{\Pi}^*
\right\}.
}
\]

### Proof

P29 gives \(D_G\le2\rho_G^*\) on the complete retained intervention-delay geometry. P28, using P25 after valid source-pair descent, gives \(D_A\le2\rho_A^*\) on the compatible aggregate-source/target-delay grid. P27, using P26 and P18 on every descendable partition, gives \(D_K\le\rho_P^*+\rho_{\Pi}^*\). Conditions C1-C5 ensure these inequalities refer to the same declared node quotient and compatible coarse physical representation rather than three unrelated scale changes. Taking the maximum of the three inequalities proves the result. \(\square\)

## 6. Exact simultaneous preservation

If all relevant reconstruction defects vanish,

\[
\rho_G^*=\rho_A^*=\rho_P^*=\rho_{\Pi}^*=0,
\]

then

\[
\boxed{
D_G=D_A=D_K=0.
}
\]

Thus, under C1-C5, the declared P11 physical signature is exactly preserved across the node quotient on the retained intervention and delay semantics.

This is stronger than exact preservation of any one component. It is still conditional on the declared experimental and state-space representation.

## 7. No semantic compensation theorem

A small numerical distortion cannot compensate for a failed semantic condition. In particular,

\[
\boxed{
D_G=D_A=D_K=0
\not\Rightarrow
\text{valid P11 scale transport}
}
\]

if, for example, a matched intervention pair has ambiguous coarse source identity, a required partition does not descend, or the compared objects were computed on different intervention-delay grids.

This matters because equal numbers can arise from mathematically incomparable constructions.

## 8. Interpretation boundary

P30 certifies simultaneous transport of a **declared physical candidate signature**. It does not prove that the signature is consciousness or that it is physically complete.

The result also does not imply

\[
\text{node quotient}
=
\text{physical fusion},
\]

nor does it imply

\[
\mathcal U_f\to\mathcal U_c
\quad\text{or}\quad
\mathcal T_f\to\mathcal T_c
\]

when intervention or time labels themselves are changed. Those require separate compatibility theorems.

The correct conclusion is narrower:

\[
\boxed{
\text{under one compatible scale declaration,}
\quad
\mathcal G,\mathcal A,\mathcal K
\text{ are simultaneously reconstruction-controlled.}
}
\]

## 9. Why P30 matters for the larger bridge program

Before a physical structure can be compared with an independently defined experiential structure, the physical object itself must be stable enough under legitimate changes of representation and scale to be scientifically interpretable. P30 closes one specific internal consistency gap: it shows how the three main P11 components can be certified together instead of under unrelated scale conventions.

It does not close the physical-to-experiential bridge. It strengthens the physical side of that bridge by making a full-signature scale claim conditional, auditable, and falsifiable.

## 10. Reproducibility

Implementation: [`full_p11_scale_compatibility.py`](../src/consciousness_bridge/full_p11_scale_compatibility.py)

Tests: [`test_full_p11_scale_compatibility.py`](../tests/test_full_p11_scale_compatibility.py)

The implementation intentionally acts as an assembly certificate rather than silently recomputing P27-P29. This makes the theorem dependencies explicit and keeps component-level proof obligations separately testable.
