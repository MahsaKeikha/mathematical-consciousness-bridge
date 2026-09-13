# P88 Equation Provenance

This record separates inherited mathematics, elementary derivations, standard external mathematics, repository-original constructions, exact computational evidence, and interpretation boundaries for Proposition 88.

## Scope

P88 uses the same declared P75 four-view binary latent target-measurement family as P75-P87. It introduces no new consciousness ontology and no new empirical assumption. Its contribution is to replace the finite parity-functional coefficient searches of P83-P87 with the complete real linear span of the eleven nontrivial parity coordinates, and to derive an exact primal-dual linear-program representation for the strongest certificate in that class.

Canonical dependencies:

- P75: declared four-view binary latent target-measurement family;
- P78: exact rational parameter-box architecture;
- P83: exact P75 parity probability identity;
- P85: mass-conservation centering for parity-functional transfer to full-law $L_\infty$ distance;
- P86-P87: increasingly complete finite parity-functional families;
- P88: complete parity-linear support optimization and exact dual certification.

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
\binom42+\binom43+\binom44=6+4+1=11
\]

such even-parity coordinates.

The eleven-dimensional feature vector $h(p)$ is inherited from P83-P87. P88's new step is to allow an arbitrary real coefficient vector $c\in\mathbb R^{11}$ rather than a predeclared finite integer family.

## 2. Incidence representation

Let $A\in\{0,1\}^{16\times11}$ satisfy

\[
A_{x,J}=\mathbf1_{H_J}(x).
\]

Then for

\[
Q_c(p)=c^\top h(p),
\]

the sixteen outcome coefficients are

\[
g_c=Ac.
\]

This is an elementary finite re-indexing of the parity-linear functional.

## 3. Centered transfer norm

Mass conservation gives

\[
\mathbf1^\top(p-q)=0.
\]

Hence for every scalar $a$,

\[
Q_c(p)-Q_c(q)
=
(Ac-a\mathbf1)^\top(p-q).
\]

By Hölder's $\ell_1$-$\ell_\infty$ inequality,

\[
|Q_c(p)-Q_c(q)|
\le
\|Ac-a\mathbf1\|_1\|p-q\|_\infty.
\]

Minimizing over $a$ yields

\[
\boxed{
D(c)=\min_a\|Ac-a\mathbf1\|_1.
}
\]

This is the same mass-conservation centering principle used in P85-P87, now written for the full eleven-dimensional parity coefficient vector.

For finitely many scalar entries of $Ac$, a median minimizes the sum of absolute deviations. The implementation evaluates the exact coefficient values and returns a deterministic minimizing center.

## 4. Why $D(c)$ is positive for nonzero $c$

For nonempty $J$, define the Walsh character

\[
\chi_J(x)=(-1)^{\sum_{j\in J}x_j}.
\]

Then

\[
\mathbf1_{H_J}(x)=\frac{1+\chi_J(x)}2.
\]

If $Ac$ is constant, then

\[
\sum_Jc_J\chi_J
\]

is constant. Distinct Walsh characters on $\{0,1\}^4$ are orthogonal under the uniform inner product, and every nonempty Walsh character is orthogonal to the constant character. Therefore every coefficient must vanish.

Thus

\[
D(c)=0\iff c=0.
\]

Walsh-character orthogonality is standard finite harmonic analysis on the Boolean cube. The application to the P88 centered transfer norm is a local derivation.

## 5. Exact P75 box support

Inside branch $s$,

\[
P_s(H_J)
=
\frac{1+\prod_{j\in J}(1-2q_{j,s})}{2}.
\]

This is inherited from P83.

For fixed $c$, the resulting $Q_c$ is multi-affine in prevalence and the eight branchwise binary response parameters. Repeated coordinatewise endpoint reduction therefore gives

\[
\max_{\theta\in B}Q_c(\theta)
=
\max_{v\in V(B)}Q_c(v),
\]

and the corresponding minimum identity.

This endpoint result is an elementary exact derivation from multi-affinity. It is not an appeal to numerical optimization.

## 6. P88 primal LP

Let $z_v=h(p_v)$ for P75 parameter-box vertices $v\in V(B)$ and let $\widehat h=h(\widehat p)$.

The complete parity-linear certificate is

\[
L_{88}^{\mathrm{par}}(B)
=
\sup_{D(c)\le1}
\left[c^\top\widehat h-\max_vc^\top z_v\right].
\]

Introducing $t$, a centering scalar $a$, and absolute-value variables $u_x$ gives the finite linear program

\[
\begin{aligned}
\max\;&t\\
\text{s.t. }&t\le c^\top(\widehat h-z_v),\quad v\in V(B),\\
&-u_x\le(Ac)_x-a\le u_x,\\
&u_x\ge0,\qquad\sum_xu_x\le1.
\end{aligned}
\]

The conversion from the support expression to this LP is repository-local algebra.

## 7. Dual LP

Associate nonnegative dual variables $\lambda_v$ with the vertex-support constraints, nonnegative variables with the two absolute-value inequalities, and a nonnegative multiplier with $\sum_xu_x\le1$.

Eliminating the paired absolute-value multipliers yields the equivalent dual

\[
\min\mu
\]

subject to

\[
\lambda\in\Delta(V(B)),
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

Finite-dimensional linear-program weak duality and strong duality are standard optimization results. P88's particular primal, its reduced dual form, and the parity-feature interpretation are repository-original applications.

The exact theorem claims do not depend on trusting a floating-point LP solution. The repository stores rational primal and dual certificates and checks all feasibility equalities and inequalities exactly.

## 8. Geometric interpretation

The dual asks for a convex combination

\[
\bar z=\sum_v\lambda_vz_v
\]

of P75 vertex parity-feature vectors and a zero-mass sixteen-cell vector $r$ satisfying

\[
A^\top r=\widehat h-\bar z.
\]

The objective minimizes

\[
\|r\|_\infty.
\]

Thus P88 computes a quotient distance from the empirical parity-feature vector to the convex hull of model-box parity features under the linear map induced by $A^\top$ and the zero-mass constraint.

This interpretation follows directly from the dual constraints. It is not a claim that the convex hull itself equals the nonlinear P75 model family in full-law space.

## 9. Pointwise dominance over P87

Every P87 functional embeds into the P88 coefficient space by placing its four primitive coefficients in the corresponding parity coordinates and zeros elsewhere.

Therefore

\[
L_{88}^{\mathrm{par}}(B)\ge L_{87}(B)
\]

for every empirical law and every admissible P75 box.

This dominance is a direct feasible-set inclusion. No empirical or asymptotic assumption is added.

## 10. Exact strict witness

For the same exact rational box and empirical law used by P86-P87, P88 uses coefficient vector

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
a=3,
\]

so the primal value is

\[
\boxed{
\ell=\frac{5/6}{28}=\frac5{168}.
}
\]

A rational dual certificate with seven nonzero vertex weights and a sixteen-entry zero-mass residual is stored in the implementation. The regression suite verifies

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

Matching exact primal and dual values prove

\[
\boxed{
L_{88}^{\mathrm{par}}(B)=\frac5{168}.
}
\]

The same witness has

\[
L_{87}(B)=\frac1{96},
\]

hence

\[
\boxed{
L_{88}^{\mathrm{par}}(B)-L_{87}(B)=\frac{13}{672}>0.
}
\]

## 11. Evidence classification

| P88 ingredient | Scientific role | Support |
| --- | --- | --- |
| P75 latent family | declared modeling assumption | P75 definition and implementation |
| parity probability identity | inherited exact model algebra | P83-P87 |
| 11-coordinate parity feature map | inherited finite construction | P83 and direct counting |
| centered transfer norm | inherited principle generalized to all 11 coordinates | P85-P87 plus direct derivation |
| positivity of $D(c)$ | local theorem using standard Walsh orthogonality | direct proof in P88 |
| box-vertex support equality | elementary multi-affine endpoint theorem | direct derivation |
| primal LP | repository-original formulation | P88 derivation and implementation |
| finite LP duality | standard external mathematics | finite-dimensional linear-program duality |
| reduced zero-mass dual | repository-original dual specialization | P88 derivation |
| exact $5/168$ primal witness | repository-original exact construction | `Fraction` implementation and tests |
| exact $5/168$ dual certificate | repository-original exact certificate | rational weights/residual and tests |
| strict $L_{87}<L_{88}^{par}$ | repository-original exact result | matching primal-dual proof and P87 regression |

## 12. Reproducibility

Implementation:

`src/consciousness_bridge/complete_parity_linear_certificate.py`

Tests:

`tests/test_complete_parity_linear_certificate.py`

Direct proposition:

`docs/proposition_88_complete_parity_linear_certificate.md`

All reported strict-witness quantities are represented by `fractions.Fraction` and verified exactly.

## 13. Interpretation boundary

P88 is a conditional theorem about the declared P75 model family and the complete **linear span of eleven parity observables**. It does not establish that those observables contain all physically or experientially relevant information, that the P75 latent variable is consciousness, that consciousness is nonphysical, that quantum mechanics is incomplete, or that the physical-to-experiential bridge has been solved.
