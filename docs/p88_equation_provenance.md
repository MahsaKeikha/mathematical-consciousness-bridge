# P88 Equation Provenance

This record separates inherited mathematics, elementary derivations, repository-original constructions, and interpretation boundaries for Proposition 88.

## Scope

P88 uses the same declared P75 four-view binary latent target-measurement family as P75-P87. It introduces no new consciousness ontology and no new empirical assumption. Its contribution is the complete nonzero primitive four-event coefficient box with integer radius three.

Canonical dependencies:

- P75: declared four-view binary latent target-measurement family;
- P78: certified parameter-box lower-bound architecture;
- P83: exact parity identity inside the P75 family;
- P85: centered functional transfer to full-law $L_\infty$ distance;
- P86: minimally weighted four-event parity certificate;
- P87: complete primitive radius-2 four-event coefficient box;
- P88: complete primitive radius-3 four-event coefficient box.

See [Proposition 88](proposition_88_exact_radius3_bounded_primitive_quad_projection_parity_functional.md), the [Claim-to-Source Scientific Audit Matrix](claim_source_matrix.md), and the [Claim, Evidence, and Citation Standard](claim_evidence_standard.md).

## 1. Inherited parity identity

For latent branch $s$ and canonical even-parity view set $J$,

\[
P_s(H_J)=\frac{1+\prod_{j\in J}(1-2q_{j,s})}{2}.
\]

This is inherited exact P75 model algebra from P83-P87. It follows from conditional independence of the binary views inside the declared model. It is not an empirical claim about consciousness.

## 2. Radius-3 primitive coefficient family

P88 uses

\[
\{-3,-2,-1,1,2,3\}
\]

for each nonzero coefficient and keeps only vectors satisfying

\[
\gcd(|c_1|,|c_2|,|c_3|,|c_4|)=1.
\]

There are $6^4=1296$ nonzero vectors in the full radius-3 alphabet.

Because the allowed positive magnitudes are only $1,2,3$, a nonprimitive vector must have common divisor $2$ or $3$. The divisor-2 vectors are precisely the $2^4=16$ sign choices with all magnitudes equal to two. The divisor-3 vectors are precisely the $2^4=16$ sign choices with all magnitudes equal to three. The two sets are disjoint. Therefore

\[
1296-16-16=1264
\]

primitive vectors remain before global-sign normalization. Quotienting by $c\sim-c$ gives

\[
\boxed{632}
\]

standard coefficient patterns.

Across the eleven canonical P83 parity coordinates,

\[
\binom{11}{4}\times632
=330\times632
=\boxed{208{,}560}.
\]

This finite family is a repository-original construction.

## 3. Four-event functional

For four distinct canonical parity events,

\[
Q(p)=\sum_{i=1}^4c_iP_p(H_{J_i}),
\]

where $c$ is nonzero, primitive, integer-valued, and satisfies $|c_i|\le3$.

The use of a linear functional is inherited from P84-P87. P88's new object is the complete declared radius-3 coefficient family at fixed event order.

## 4. Exact P75 box range

Inside branch $s$, set

\[
a_{j,s}=1-2q_{j,s}.
\]

Then

\[
Q_s
=
\frac12\sum_i c_i
+
\frac12\sum_i c_i\prod_{j\in J_i}a_{j,s}.
\]

Every response coordinate occurs with degree at most one, so $Q_s$ is multi-affine. Repeated coordinatewise endpoint reduction proves that every branch extremum over an axis-aligned box occurs at a vertex.

The final latent mixture

\[
Q(\pi)=(1-\pi)Q_-+\pi Q_+
\]

is affine in prevalence. Hence prevalence endpoints suffice as well.

This is an elementary exact derivation. The implementation does not use floating-point optimization.

## 5. Centered transfer norm

Define

\[
g(x)=\sum_i c_i\mathbf1_{H_{J_i}}(x).
\]

For probability laws $p,q$,

\[
\sum_x[p(x)-q(x)]=0.
\]

Therefore, for any scalar $a$,

\[
Q(p)-Q(q)
=
\sum_x[g(x)-a][p(x)-q(x)].
\]

The triangle inequality gives

\[
|Q(p)-Q(q)|
\le
\left(\sum_x|g(x)-a|\right)\|p-q\|_\infty.
\]

P88 uses

\[
D(Q)=\min_a\sum_x|g(x)-a|.
\]

As in P85-P87, any median of the sixteen exact outcome coefficients minimizes this finite absolute-deviation objective.

## 6. P88 hierarchy definition

Let

\[
L_{\mathrm{bp4},3}(B)
=
\max_{Q\in\mathcal Q_{88}}
\frac{\operatorname{dist}(Q(\widehat p),I_B(Q))}{D(Q)}.
\]

P88 defines

\[
\boxed{L_{88}(B)=\max\{L_{87}(B),L_{\mathrm{bp4},3}(B)\}.}
\]

Since the radius-2 P87 coefficient family is a subset of the radius-3 family,

\[
L_{88}(B)\ge L_{87}(B)
\]

pointwise.

## 7. Exact strict witness

For the exact rational witness already used by P86-P87, exhaustive P88 search selects

\[
Q=
P(H_{\{0,2\}})
-P(H_{\{1,3\}})
-3P(H_{\{1,2,3\}})
+2P(H_{\{0,1,2,3\}}).
\]

The exact quantities are

\[
Q(\widehat p)=-\frac{11}{8},
\qquad
I_B(Q)=[-1,2],
\]

\[
\Delta_Q=\frac38,
\qquad
D(Q)=24,
\qquad
a=-1.
\]

Hence

\[
L_{88}(B)
=\frac{3/8}{24}
=\boxed{\frac1{64}}.
\]

On the same exact box and empirical law,

\[
L_{86}(B)=\frac1{192},
\qquad
L_{87}(B)=\frac1{96},
\]

so

\[
\boxed{
0=L_{85}(B)
<\frac1{192}=L_{86}(B)
<\frac1{96}=L_{87}(B)
<\frac1{64}=L_{88}(B).
}
\]

The strict witness is repository-original and is reproduced by exact exhaustive computation over all 208,560 standard P88 functionals.

## 8. Evidence classification

| P88 ingredient | Scientific role | Support |
| --- | --- | --- |
| P75 latent family | declared modeling assumption | P75 definition and implementation |
| parity probability identity | inherited exact model algebra | P83-P87 |
| 632 normalized primitive patterns | elementary finite counting plus repository convention | direct count above and implementation |
| 208,560-function family | repository-original finite construction | exact enumeration and tests |
| box-vertex extremization | elementary derivation | coordinatewise affine endpoint argument |
| centered transfer inequality | elementary probability-law derivation | mass conservation plus triangle inequality |
| median center | standard finite-dimensional fact with prior local proofs | P85-P87 provenance and exact implementation |
| `L87 = 1/96 < L88 = 1/64` | repository-original exact strict witness | exact implementation and exhaustive regression tests |

## 9. Interpretation boundary

P88 is a conditional theorem about separation from the declared P75 model family. It does not identify the latent P75 state with experience, prove consciousness nonphysical, validate another ontology, establish that parity coordinates are phenomenological variables, or solve the physical-to-experiential bridge.
