# P87 Equation Provenance

This record separates inherited mathematics, elementary derivations, repository-original constructions, and interpretation boundaries for Proposition 87.

## Scope

P87 uses the same declared P75 four-view binary latent target-measurement family as P75-P86. It introduces no new consciousness ontology and no new empirical assumption. Its contribution is a complete bounded primitive four-event parity-functional audit for nonzero integer coefficients with magnitude at most two.

Canonical dependencies:

- P75: declared four-view binary latent target-measurement family;
- P78: certified exact parameter-box lower-bound architecture;
- P83: exact parity identity inside the P75 model;
- P85: centered functional transfer to full-law $L_\infty$ distance;
- P86: minimally weighted four-event parity-functional certificate;
- P87: complete primitive coefficient box $0<|c_i|\le2$ at four-event order.

See [Proposition 87](proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md), the [Claim-to-Source Scientific Audit Matrix](claim_source_matrix.md), and the [Claim, Evidence, and Citation Standard](claim_evidence_standard.md).

## 1. Inherited parity identity

For latent branch $s$ and canonical even-parity view set $J$,

\[
P_s(H_J)
=
\frac{1+\prod_{j\in J}(1-2q_{j,s})}{2}.
\]

This identity is inherited from P83-P86 and follows directly from conditional independence of the binary views inside the declared P75 model. It is model algebra, not an empirical claim about consciousness.

## 2. P87 bounded primitive coefficient family

P87 defines the coefficient alphabet

\[
\{-2,-1,1,2\}.
\]

All entries are nonzero. A vector is retained only when

\[
\gcd(|c_1|,|c_2|,|c_3|,|c_4|)=1.
\]

There are $4^4=256$ nonzero vectors in the alphabet. The only non-primitive vectors are those with every magnitude equal to two, of which there are $2^4=16$. Therefore there are

\[
256-16=240
\]

primitive vectors before global-sign normalization. Quotienting by $c\sim-c$ gives

\[
\boxed{120}
\]

standard coefficient patterns.

Across the eleven canonical parity coordinates,

\[
\binom{11}{4}\times120
=
330\times120
=
\boxed{39{,}600}.
\]

This 39,600-element family is a repository-original finite construction.

## 3. Weighted four-event functional

For four distinct canonical parity events,

\[
Q(p)=\sum_{i=1}^4c_iP_p(H_{J_i}),
\]

with primitive nonzero integer coefficients satisfying $|c_i|\le2$.

P87's novelty is not the use of a linear functional itself. The new object is the complete declared finite coefficient family and its exact model-separation certificate relative to P86.

## 4. Exact P75 box range

Inside branch $s$, write

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

Each response coordinate enters affinely when all others are fixed. Therefore repeated one-coordinate endpoint reduction proves that every branch extremum over an axis-aligned box occurs at a vertex.

The final mixture

\[
Q(\pi)=(1-\pi)Q_-+\pi Q_+
\]

is affine in prevalence, so its extrema occur at prevalence endpoints.

This is an elementary exact derivation from the P75 parameterization. No floating-point optimizer is used.

## 5. Centered transfer norm

Define the sixteen-cell coefficient function

\[
g(x)=\sum_i c_i\mathbf1_{H_{J_i}}(x).
\]

For probability laws $p,q$,

\[
\sum_x[p(x)-q(x)]=0.
\]

Thus for any scalar $a$,

\[
Q(p)-Q(q)
=
\sum_x[g(x)-a][p(x)-q(x)].
\]

The triangle inequality gives

\[
|Q(p)-Q(q)|
\le
\left(\sum_x|g(x)-a|\right)
\|p-q\|_\infty.
\]

P87 uses

\[
D(Q)=\min_a\sum_x|g(x)-a|.
\]

As documented for P86, a median minimizes the finite absolute-deviation objective. The implementation evaluates the finitely many exact coefficient values and returns a deterministic minimizing center.

## 6. P87 hierarchy definition

Let

\[
L_{\mathrm{bp4}}(B)
=
\max_{Q\in\mathcal Q_{87}}
\frac{\operatorname{dist}(Q(\widehat p),I_B(Q))}{D(Q)}.
\]

P87 defines

\[
\boxed{
L_{87}(B)=\max\{L_{86}(B),L_{\mathrm{bp4}}(B)\}.
}
\]

Hence pointwise dominance

\[
L_{87}(B)\ge L_{86}(B)
\]

is definitional once the validity of each bounded primitive functional lower bound has been established.

## 7. Exact strict witness

For the exact rational P86 witness box and empirical law, P87 exhaustively selects

\[
Q=
P(H_{\{0,2\}})
-P(H_{\{1,3\}})
-2P(H_{\{1,2,3\}})
+2P(H_{\{0,1,2,3\}}).
\]

The exact quantities are

\[
Q(\widehat p)=-\frac{17}{24},
\qquad
I_B(Q)=\left[-\frac12,2\right],
\]

\[
\Delta_Q=\frac5{24},
\qquad
D(Q)=20,
\qquad
a=0.
\]

Therefore

\[
L_{87}(B)
=
\frac{5/24}{20}
=
\boxed{\frac1{96}}.
\]

The complete P86 value on the same box is

\[
L_{86}(B)=\frac1{192},
\]

so

\[
\boxed{
L_{86}(B)=\frac1{192}<L_{87}(B)=\frac1{96}.
}
\]

The implementation and regression suite use exact `fractions.Fraction` arithmetic and exhaust all 39,600 standard P87 functionals.

## 8. Evidence classification

| P87 ingredient | Scientific role | Support |
| --- | --- | --- |
| P75 latent family | declared modeling assumption | P75 definition and implementation |
| parity probability identity | inherited exact model algebra | P83-P86 |
| 120 normalized primitive patterns | elementary finite counting plus repository convention | direct count above and implementation |
| 39,600-function family | repository-original finite construction | exact enumeration and tests |
| box-vertex extremization | elementary derivation | coordinatewise affine endpoint argument |
| centered transfer inequality | elementary probability-law derivation | mass conservation plus triangle inequality |
| median center | standard finite-dimensional fact with local P86 proof | P86 provenance and exact implementation |
| `L86 = 1/192 < L87 = 1/96` | repository-original exact strict witness | exact implementation and exhaustive regression tests |

## 9. Interpretation boundary

P87 is a conditional theorem about separation from the declared P75 model family. It does not identify the latent P75 state with experience, prove consciousness nonphysical, validate another ontology, establish that parity coordinates are phenomenological variables, or solve the physical-to-experiential bridge.
