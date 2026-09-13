# P86 Equation Provenance

This record identifies which equations in Proposition 86 are inherited, which are elementary derivations, and which are new proposition-level constructions.

## Scope

P86 works inside the same declared P75 four-view binary latent measurement family used by P75-P85. It introduces no new ontological assumption. Its contribution is a stronger exact shared-parameter rejection certificate based on minimally non-uniform weighted four-event parity functionals.

## Inherited identities

### Binary parity identity

For latent branch $s$ and view set $J$,

\[
P_s(H_J)=\frac{1+\prod_{j\in J}(1-2q_{j,s})}{2}.
\]

This is the same exact parity identity used in P83-P85.

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

### Full-law lower-bound transfer

If

\[
\Delta_Q=\operatorname{dist}(Q(\widehat p),I_B(Q)),
\]

then

\[
\|\widehat p-q\|_\infty\ge\frac{\Delta_Q}{D(Q)}
\]

for every P75 law $q$ generated in the box. This follows directly from mass-conservation centering and the triangle inequality.

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

The regression suite verifies the complete P85 value is exactly zero and exhausts all 10,560 standard P86 functionals.

## Interpretation boundary

No equation in P86 identifies the latent P75 state with conscious experience. No P86 derivation establishes nonphysicality, selects a correct alternative ontology, or closes the physical-to-experiential bridge. The result is an exact conditional model-separation theorem inside the declared P75 family.
