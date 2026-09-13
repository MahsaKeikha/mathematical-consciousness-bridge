# P88 Equation Provenance

This record separates inherited mathematics, elementary derivations, standard external mathematics, repository-original constructions, exact computational evidence, and interpretation boundaries for Proposition 88.

## Scope

P88 uses the same declared P75 four-view binary latent target-measurement family as P75-P87. It introduces no new consciousness ontology and no new empirical assumption.

Its new mathematical component is the complete real linear span of the eleven nontrivial parity coordinates, together with an exact primal-dual linear-program representation of the strongest lower bound in that class.

The **full** P88 hierarchy retains the recursive P87 certificate:

\[
\boxed{
L_{88}(B)=\max\{L_{87}(B),L_{88}^{\mathrm{par}}(B)\}.
}
\]

This is necessary because P87 inherits earlier non-parity P78-P82 lower bounds. P88 does not claim that its parity feature map subsumes those non-parity certificates.

Canonical dependencies:

- P75: declared four-view binary latent target-measurement family;
- P78-P82: earlier continuous-model and non-parity lower-bound layers retained recursively by P87;
- P83: exact P75 parity probability identity;
- P85: mass-conservation centering for parity-functional transfer to full-law $L_\infty$ distance;
- P86-P87: increasingly complete finite parity-functional families;
- P88: complete parity-linear optimization, exact dual certification, and the retained P87 baseline.

See [Proposition 88](proposition_88_complete_parity_linear_certificate.md), the [Claim-to-Source Scientific Audit Matrix](claim_source_matrix.md), and the [Claim, Evidence, and Citation Standard](claim_evidence_standard.md).

## 1. Parity feature coordinates

For each canonical view set $J$ of size two, three, or four,

\[
h_J(p)=P_p(H_J),
\qquad
H_J=\left\{x:\sum_{j\in J}x_j\equiv0\pmod2\right\}.
\]

There are

\[
\binom42+\binom43+\binom44=11
\]

such even-parity coordinates.

The eleven-dimensional feature vector $h(p)$ is inherited from P83-P87. P88's new step is to allow arbitrary $c\in\mathbb R^{11}$ rather than a predeclared finite integer family.

## 2. Incidence representation

Let $A\in\{0,1\}^{16\times11}$ satisfy

\[
A_{x,J}=\mathbf1_{H_J}(x).
\]

For

\[
Q_c(p)=c^\top h(p),
\]

the sixteen outcome coefficients are

\[
g_c=Ac.
\]

This is an elementary finite re-indexing.

## 3. Centered transfer norm

Mass conservation gives

\[
\mathbf1^\top(p-q)=0.
\]

Thus for every scalar $a$,

\[
Q_c(p)-Q_c(q)
=(Ac-a\mathbf1)^\top(p-q).
\]

By the $\ell_1$-$\ell_\infty$ inequality,

\[
|Q_c(p)-Q_c(q)|
\le
\|Ac-a\mathbf1\|_1\|p-q\|_\infty.
\]

Minimizing over $a$ yields

\[
\boxed{D(c)=\min_a\|Ac-a\mathbf1\|_1.}
\]

This is the P85-P87 centering principle generalized to the full eleven-dimensional coefficient vector.

For finitely many scalar entries of $Ac$, a median minimizes the absolute-deviation objective. The implementation evaluates the exact finite coefficient values.

## 4. Why $D$ is a norm

For nonempty $J$, define the Walsh character

\[
\chi_J(x)=(-1)^{\sum_{j\in J}x_j}.
\]

Then

\[
\mathbf1_{H_J}(x)=\frac{1+\chi_J(x)}2.
\]

If $Ac$ is constant, then $\sum_Jc_J\chi_J$ is constant. Distinct Walsh characters are orthogonal on the Boolean cube, and each nonempty character is orthogonal to the constant character. Therefore every coefficient must vanish.

Hence

\[
D(c)=0\iff c=0.
\]

Walsh-character orthogonality is standard finite harmonic analysis; its use here to prove positivity of the P88 centered transfer norm is a local derivation.

## 5. Exact P75 box support

Inside branch $s$,

\[
P_s(H_J)
=
\frac{1+\prod_{j\in J}(1-2q_{j,s})}{2}.
\]

This identity is inherited from P83.

For fixed $c$, $Q_c$ is multi-affine in the prevalence and eight branchwise response parameters. Therefore

\[
\max_{\theta\in B}Q_c(\theta)
=
\max_{v\in V(B)}Q_c(v),
\]

with the analogous minimum identity.

This is an elementary exact endpoint derivation, not a numerical optimization claim.

## 6. Complete parity-linear primal LP

Let $z_v=h(p_v)$ for parameter-box vertices $v\in V(B)$ and let $\widehat h=h(\widehat p)$.

P88 defines the new parity component

\[
\boxed{
L_{88}^{\mathrm{par}}(B)
=
\sup_{D(c)\le1}
\left[c^\top\widehat h-\max_vc^\top z_v\right].
}
\]

Introducing a support variable $t$, centering scalar $a$, and absolute-value variables $u_x$ gives

\[
\begin{aligned}
\max\;&t\\
\text{s.t. }&t\le c^\top(\widehat h-z_v),\quad v\in V(B),\\
&-u_x\le(Ac)_x-a\le u_x,\\
&u_x\ge0,\qquad\sum_xu_x\le1.
\end{aligned}
\]

The conversion is repository-local algebra.

## 7. Exact dual LP

Finite-dimensional linear-program duality gives the equivalent dual

\[
\min\mu
\]

subject to

\[
\lambda_v\ge0,
\qquad
\sum_v\lambda_v=1,
\]

\[
\mathbf1^\top r=0,
\]

\[
A^\top r
=
\widehat h-\sum_v\lambda_vz_v,
\]

and

\[
|r_x|\le\mu.
\]

Finite-dimensional weak/strong LP duality is standard external mathematics. The particular P88 primal, the reduced zero-mass dual, and their parity-feature interpretation are repository-original applications.

The exact strict-witness claim does not require trusting a floating-point optimizer: the repository stores rational primal and dual certificates and verifies their feasibility exactly.

## 8. Geometric interpretation

The dual chooses a convex combination

\[
\bar z=\sum_v\lambda_vz_v
\]

of P75 box-vertex parity features and a zero-mass sixteen-cell perturbation $r$ such that

\[
A^\top r=\widehat h-\bar z.
\]

The objective minimizes $\|r\|_\infty$.

Thus $L_{88}^{\mathrm{par}}$ is a quotient distance from the empirical parity feature vector to the convex hull of the box-vertex parity features. This does **not** say that the convex hull equals the nonlinear P75 model family in full-law space.

## 9. Correct relationship to the P87 hierarchy

Every P83-P87 **parity functional** embeds into P88's eleven-dimensional parity coefficient space. Therefore $L_{88}^{\mathrm{par}}$ closes the linear parity-functional class generated by those propositions.

But P87 itself is recursively defined and retains non-parity predecessors. P86 retains P85, P85 retains P84, and the chain reaches P83, which retains P82. P82 and earlier certificates contain non-parity event/model-distance information.

Therefore feasible-set inclusion supports the statement

> P88's parity component contains all earlier parity-functional candidates,

but does not by itself support the stronger universal statement

\[
L_{88}^{\mathrm{par}}\ge L_{87}.
\]

The full P88 hierarchy is consequently

\[
\boxed{
L_{88}(B)=\max\{L_{87}(B),L_{88}^{\mathrm{par}}(B)\}.
}
\]

Pointwise dominance $L_{88}\ge L_{87}$ is then definitional after validity of the parity component has been proved.

## 10. Exact strict witness

For the same exact rational box and empirical law used by P86-P87, take

\[
c=(0,2,1,-1,-1,-1,2,1,3,-2,3)
\]

in canonical coordinate order

\[
(01,02,03,12,13,23,012,013,023,123,0123).
\]

The exact implementation verifies

\[
Q_c(\widehat p)=\frac{13}{6},
\]

\[
I_B(Q_c)=\left[3,\frac{51}{8}\right],
\]

\[
\Delta_c=\frac56,
\qquad
D(c)=28,
\qquad
a=3.
\]

Hence the primal value is

\[
\boxed{
\ell=\frac{5/6}{28}=\frac5{168}.
}
\]

A sparse rational dual certificate uses seven parameter-box vertices. The exact verifier checks

\[
\sum_v\lambda_v=1,
\qquad
\mathbf1^\top r=0,
\]

\[
A^\top r
=
\widehat h-\sum_v\lambda_vz_v,
\]

and

\[
\|r\|_\infty=\frac5{168}.
\]

Matching primal and dual values prove

\[
\boxed{L_{88}^{\mathrm{par}}(B)=\frac5{168}.}
\]

The recursive P87 value on the same witness is

\[
L_{87}(B)=\frac1{96},
\]

so

\[
\boxed{
L_{88}(B)=\max\left\{\frac1{96},\frac5{168}\right\}=\frac5{168}.
}
\]

Thus

\[
\boxed{L_{88}-L_{87}=\frac{13}{672}>0.}
\]

## 11. Evidence classification

| P88 ingredient | Scientific role | Support |
| --- | --- | --- |
| P75 latent family | declared modeling assumption | P75 definition and implementation |
| parity identity | inherited exact model algebra | P83-P87 |
| eleven-coordinate parity feature map | inherited finite construction | P83 and direct counting |
| centered transfer norm | inherited principle generalized to all eleven coordinates | P85-P87 plus direct derivation |
| positivity of $D(c)$ | local theorem using standard Walsh orthogonality | direct P88 proof |
| box-vertex support equality | elementary multi-affine endpoint theorem | direct derivation |
| primal LP | repository-original formulation | P88 derivation and implementation |
| finite LP duality | standard external mathematics | finite-dimensional LP duality |
| reduced zero-mass dual | repository-original specialization | P88 derivation |
| exact $5/168$ primal witness | repository-original exact construction | `Fraction` implementation/tests |
| exact $5/168$ dual witness | repository-original exact certificate | rational weights/residual/tests |
| full $L_{88}=\max(L_{87},L_{88}^{par})$ | hierarchy definition preserving non-parity predecessors | P88 definition |
| strict $L_{87}<L_{88}$ on common witness | repository-original exact result | P87 regression plus P88 primal-dual certificate |

## 12. Reproducibility

Implementation:

`src/consciousness_bridge/complete_parity_linear_certificate.py`

Tests:

`tests/test_complete_parity_linear_certificate.py`

Direct proposition:

`docs/proposition_88_complete_parity_linear_certificate.md`

Theorem figure:

`docs/figures/p88_complete_parity_linear_certificate.svg`

All strict-witness quantities are represented and checked with exact `fractions.Fraction` arithmetic.

## 13. Interpretation boundary

P88 is a conditional theorem about the declared P75 family and the complete linear span of eleven parity observables. It does not establish that those observables contain all physically or experientially relevant information, that the P75 latent variable is consciousness, that every physical description has been exhausted, that consciousness is nonphysical, or that the physical-to-experiential bridge has been solved.
