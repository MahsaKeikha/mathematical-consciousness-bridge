# P86 Equation Provenance

This record identifies which equations in Proposition 86 are inherited, which are elementary derivations, and which are new proposition-level constructions. It is designed so that no mathematical step has to rely on an uncited appeal to authority: imported structure is linked to earlier repository results, while elementary facts used by P86 are derived locally below.

## Scope

P86 works inside the same declared P75 four-view binary latent measurement family used by P75-P85. It introduces no new ontological assumption. Its contribution is a stronger exact shared-parameter rejection certificate based on minimally non-uniform weighted four-event parity functionals.

Canonical dependencies:

- P75: declared four-view binary latent target-measurement family;
- P78: exact multi-affine parameter-box certification architecture;
- P83: exact projection-parity identity and single-event parity certification;
- P84: pairwise shared-parameter parity compatibility;
- P85: complete three-event shared-parameter parity-functional certificate;
- P86: minimally weighted four-event strict strengthening.

See [Proposition 86](proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md), the [Claim-to-Source Scientific Audit Matrix](claim_source_matrix.md), and the [Claim, Evidence, and Citation Standard](claim_evidence_standard.md).

## Inherited identities

### Binary parity identity

For latent branch $s$ and view set $J$,

\[
P_s(H_J)=\frac{1+\prod_{j\in J}(1-2q_{j,s})}{2}.
\]

This is the same exact parity identity used in P83-P85. Its role in P86 is inherited algebra inside the declared P75 conditional-independence model, not a new empirical assumption about consciousness.

### Latent mixture

For prevalence $\pi$,

\[
P(H_J)=(1-\pi)P_-(H_J)+\pi P_+(H_J).
\]

This is inherited from the P75 latent-mixture model.

### Mass-conservation centering

For probability laws $p$ and $q$,

\[
\sum_x[p(x)-q(x)]=0.
\]

Therefore a constant may be subtracted from any outcome coefficient vector without changing a linear functional difference. P85 already used this device for the exact centered transfer denominator.

## New P86 definitions

### Minimal non-uniform primitive weight family

P86 defines the standard magnitude multiset

\[
\{1,1,1,2\}.
\]

After all distinct magnitude placements and sign patterns are taken modulo one global sign, there are 32 coefficient patterns per four-event subset.

With eleven canonical parity coordinates,

\[
\binom{11}{4}\times32=10{,}560
\]

standard P86 functionals.

This 10,560-element family is a repository-original finite construction. It is not attributed to an external source.

### Weighted four-event functional

For four distinct canonical parity view sets,

\[
Q(p)=\sum_{i=1}^4c_iP_p(H_{J_i}),
\qquad
\{|c_i|\}=\{1,1,1,2\}.
\]

This is the new P86 test family.

### Exact box range

Substitution of the inherited parity identity gives

\[
Q_s=\frac12\sum_i c_i+
\frac12\sum_i c_i\prod_{j\in J_i}(1-2q_{j,s}).
\]

Every response coordinate appears with degree at most one. The function is therefore multi-affine in each branch, so exact extrema occur at response-box vertices. The final mixture is affine in prevalence, so prevalence endpoints suffice.

This is an elementary exact derivation from the declared P75 parametrization, not an imported theorem specific to consciousness.

### Why vertex evaluation is exact

The vertex claim can be proved directly without importing a separate optimization theorem. Hold every coordinate except one, say $z$, fixed. A multi-affine function then has the form

\[
f(z)=az+b
\]

on the allowed interval $[\ell,u]$. Therefore its minimum and maximum over that coordinate occur at $z=\ell$ or $z=u$. Fix whichever endpoint is extremal and repeat the same argument coordinate by coordinate. After finitely many reductions, an extremum is attained at a full box vertex.

The prevalence step is the one-dimensional version of the same argument because

\[
Q(\pi)=(1-\pi)Q_-+\pi Q_+
\]

is affine in $\pi$.

Thus exact endpoint enumeration is justified internally by the algebraic form of the P75 model.

### Centered coefficient denominator

Define

\[
g(x)=\sum_i c_i\mathbf1_{H_{J_i}}(x).
\]

P86 uses

\[
D(Q)=\min_a\sum_x|g(x)-a|.
\]

For finitely many scalar coefficients, every median minimizes the sum of absolute deviations. The implementation evaluates the finitely many distinct integer coefficient values, keeping the calculation exact.

### Why a median minimizes the absolute-deviation sum

Let the finite coefficient values be sorted as

\[
y_1\le y_2\le\cdots\le y_n,
\]

and define

\[
F(a)=\sum_{k=1}^n|y_k-a|.
\]

Between consecutive data values, $F$ is affine. Increasing $a$ by a small amount decreases each term with $y_k>a$ and increases each term with $y_k<a$. Hence the slope on an interval containing no data value is

\[
\#\{k:y_k<a\}-\#\{k:y_k>a\}.
\]

Before the median region this slope is negative; after the median region it is positive. Therefore every median minimizes $F$. For the even sixteen-cell coefficient vector used here, any center between the two middle values is optimal; the implementation deterministically selects an exact integer minimizer when one is available.

This local derivation is sufficient for the P86 denominator calculation and avoids treating the median property as an unsupported imported claim.

### Full-law lower-bound transfer

If

\[
\Delta_Q=\operatorname{dist}(Q(\widehat p),I_B(Q)),
\]

then

\[
\|\widehat p-q\|_\infty\ge\frac{\Delta_Q}{D(Q)}
\]

for every P75 law $q$ generated in the box. This follows directly from mass-conservation centering and the triangle inequality:

\[
Q(\widehat p)-Q(q)=\sum_x[g(x)-a][\widehat p(x)-q(x)],
\]

so

\[
|Q(\widehat p)-Q(q)|
\le
\left(\sum_x|g(x)-a|\right)\|\widehat p-q\|_\infty.
\]

Minimizing the coefficient factor over $a$ gives $D(Q)$, and minimizing the left mismatch over all admissible $q$ inside the P75 box yields the stated lower bound.

### P86 hierarchy definition

\[
L_{86}(B)=\max\{L_{85}(B),L_{\mathrm{w4}}(B)\}.
\]

Pointwise dominance $L_{86}\ge L_{85}$ is therefore definitional once validity of the weighted-four-event lower bound has been proved.

## New exact strict witness

The repository contains an exact rational box and empirical sixteen-cell law for which

\[
L_{85}(B)=0.
\]

For

\[
Q=
P(H_{\{0,2\}})
-P(H_{\{1,3\}})
-2P(H_{\{1,2,3\}})
+P(H_{\{0,1,2,3\}}),
\]

the exact quantities are

\[
Q(\widehat p)=-\frac{13}{12},
\qquad
I_B(Q)=[-1,1],
\]

\[
\Delta_Q=\frac1{12},
\qquad
D(Q)=16,
\]

and hence

\[
L_{86}(B)=\frac1{192}>0.
\]

The regression suite verifies the complete P85 value is exactly zero and exhausts all 10,560 standard P86 functionals. The witness is synthetic and exact. It is not described as measured biological data.

## Evidence classification summary

| P86 ingredient | Scientific role | Support |
| --- | --- | --- |
| P75 latent family | declared model assumption | P75 definition and implementation |
| parity identity | inherited exact model algebra | P83-P85 and local P86 substitution |
| box-vertex extremization | elementary derivation | coordinatewise affine endpoint proof above |
| prevalence endpoints | elementary derivation | one-dimensional affine endpoint proof above |
| median absolute-deviation center | standard finite-dimensional fact with local proof | slope argument above |
| centered transfer inequality | elementary probability-law derivation | mass conservation plus triangle inequality above |
| 10,560 functional family | repository-original construction | exact combinatorial definition plus implementation |
| `L85 = 0 < L86 = 1/192` | repository-original exact strict witness | exact rational implementation and exhaustive regression tests |

## Interpretation boundary

No equation in P86 identifies the latent P75 state with conscious experience. No P86 derivation establishes nonphysicality, selects a correct alternative ontology, proves that consciousness is an additional dimension, or closes the physical-to-experiential bridge. The result is an exact conditional model-separation theorem inside the declared P75 family.
