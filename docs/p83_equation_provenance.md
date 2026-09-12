# P83 equation and provenance record

This page classifies the mathematical ingredients used in **Proposition 83: Exact Signed Cylinder-Contrast Certificate for Continuous P75 Separation** and makes explicit which parts are standard mathematics, which are inherited from earlier propositions, and which are the new P83 construction in this repository.

## Scientific status

P83 is a **conditional exact-rational computational-certification theorem** for the declared P75 four-view binary latent target-measurement family. It strengthens a model-distance lower bound. It does not identify the P75 latent state with consciousness, does not validate the model when rejection fails, and does not close the physical-to-experiential bridge.

---

## 1. Inherited P75 model

For observed pattern $x=(x_1,x_2,x_3,x_4)\in\{0,1\}^4$ and parameters

\[
\theta=(\pi,q_{1,-},q_{1,+},\ldots,q_{4,-},q_{4,+}),
\]

P75 defines

\[
q_x(\theta)
=(1-\pi)\prod_{j=1}^4 f(q_{j,-},x_j)
+\pi\prod_{j=1}^4 f(q_{j,+},x_j),
\]

with

\[
f(q,1)=q,\qquad f(q,0)=1-q.
\]

**Provenance:** inherited from P75 and the standard binary latent conditional-independence model declared there. P83 does not introduce a new latent model.

---

## 2. Inherited cylinder-event probability

For a nonempty coordinate set $J$ and binary assignment $a$,

\[
C(J,a)=\{x:x_j=a_j\text{ for all }j\in J\},
\]

and

\[
q_\theta(C(J,a))
=(1-\pi)\prod_{j\in J}f(q_{j,-},a_j)
+\pi\prod_{j\in J}f(q_{j,+},a_j).
\]

**Provenance:** inherited from P81. The count of 80 nonempty four-view cylinders is the elementary combinatorial identity

\[
\sum_{k=1}^4{4\choose k}2^k=3^4-1=80.
\]

---

## 3. P83 signed-cylinder observable

For two distinct cylinders $A$ and $B$, P83 defines

\[
\boxed{\phi_{A,B}=\mathbf1_A-\mathbf1_B.}
\]

The empirical contrast is

\[
\boxed{\widehat c_{A,B}=\widehat p(A)-\widehat p(B).}
\]

**Provenance:** repository-original P83 certificate construction in this theorem chain. Signed test functions themselves are standard linear-functional objects; the specific finite non-nested cylinder family and its use as an exact P75 box certificate are the P83 contribution.

---

## 4. Full-law $L_\infty$ transfer inequality

For arbitrary finite signed coefficients $\phi(x)$,

\[
\left|\sum_x\phi(x)(p_x-q_x)\right|
\le
\sum_x|\phi(x)|\,|p_x-q_x|
\le
\|\phi\|_1\|p-q\|_\infty.
\]

Therefore

\[
\boxed{
\|p-q\|_\infty
\ge
\frac{|E_p\phi-E_q\phi|}{\|\phi\|_1}.
}
\]

For $\phi_{A,B}=\mathbf1_A-\mathbf1_B$,

\[
\boxed{\|\phi_{A,B}\|_1=|A\triangle B|.}
\]

**Provenance:** the triangle inequality and the $\ell_1$-$\ell_\infty$ dual estimate are standard finite-dimensional analysis. The symmetric-difference identity is elementary set algebra. P81 used the one-indicator special case; P83 uses the two-indicator signed form to retain cross-event compatibility.

---

## 5. Branchwise multi-affine contrast

Inside latent branch $s$,

\[
P_s(C(J,a))=\prod_{j\in J}f(q_{j,s},a_j).
\]

Thus

\[
\boxed{
g_s(q_s)=P_s(A)-P_s(B)}
\]

is multi-affine in the union of response coordinates used by $A$ and $B$.

**Provenance:** the product form is inherited from P75/P81. Multi-affinity follows algebraically because each response coordinate appears with degree at most one. P78 already exploits multi-affinity of the complete P75 cell map; P83 applies the same endpoint principle to a new signed event functional.

---

## 6. Exact vertex extremization

A scalar multi-affine function on a hyperrectangle attains its minimum and maximum at hyperrectangle vertices. Therefore

\[
\boxed{
\ell_s=
\min_{v\in V_s}g_s(v),
\qquad
u_s=
\max_{v\in V_s}g_s(v).
}
\]

For four binary observed views, a signed cylinder pair uses at most four response coordinates per latent branch, so at most $2^4=16$ endpoint vertices are evaluated per branch.

**Provenance:** standard multi-affine endpoint extremization; used in related form by P78. The P83 specialization to signed non-nested cylinder pairs is repository-original in this theorem sequence.

---

## 7. Exact prevalence mixture interval

The complete P75 signed contrast is

\[
E_{q_\theta}\phi_{A,B}
=(1-\pi)g_-+\pi g_+.
\]

With exact branch intervals

\[
g_-\in[\ell_-,u_-],\qquad g_+\in[\ell_+,u_+],
\]

and prevalence $\pi\in[\pi_L,\pi_U]$, the exact global endpoints are

\[
\boxed{
\ell_{A,B}
=
\min_{\pi\in\{\pi_L,\pi_U\}}
[(1-\pi)\ell_-+\pi\ell_+],
}
\]

\[
\boxed{
u_{A,B}
=
\max_{\pi\in\{\pi_L,\pi_U\}}
[(1-\pi)u_-+\pi u_+].
}
\]

**Provenance:** affine endpoint extremization is elementary. Exact joint attainability follows from the P75 parameterization: minus-branch responses, plus-branch responses, and prevalence occupy disjoint coordinates of the axis-aligned parameter box. The resulting exact signed-cylinder box interval is the P83 construction.

---

## 8. P83 lower bound

For one signed pair,

\[
\boxed{
L_{A,B}(B_\theta)
=
\frac{
d(\widehat c_{A,B},[\ell_{A,B},u_{A,B}])
}{|A\triangle B|}.
}
\]

The standard signed-family bound is

\[
\boxed{
L_{\mathrm{signed}}(B_\theta)
=
\max_{(A,B)\in\mathcal S_{83}}L_{A,B}(B_\theta).
}
\]

P83 defines

\[
\boxed{
L_{83}(B_\theta)
=
\max\{L_{82}(B_\theta),L_{\mathrm{signed}}(B_\theta)\}.
}
\]

Hence

\[
\boxed{
L_{83}\ge L_{82}\ge L_{81}\ge L_{80}\ge L_{78}.
}
\]

**Provenance:** P78, P80, P81, and P82 provide the inherited lower-bound chain. The signed-family maximum and its combination with P82 are the P83 theorem construction.

---

## 9. Count of genuinely new P83 contrasts

There are

\[
{80\choose2}=3160
\]

unordered pairs of distinct nonempty cylinders.

Nested pairs are excluded because their signed difference is already represented by P81 or P82. The nested-pair count is

\[
48+192+224=464.
\]

Therefore

\[
\boxed{|\mathcal S_{83}|=3160-464=2696.}
\]

**Provenance:** elementary combinatorics specialized to the four-view cylinder family. The decision to use exactly the non-nested remainder as the predeclared P83 audit family is repository-original.

---

## 10. Strict witness

P83 uses the exact rational parameter box

\[
\pi\in[0,1],
\qquad
q_-=(1/4,1,0,1/2),
\qquad
q_+=(0,3/4,3/4,3/4),
\]

and empirical law

\[
\widehat p
=\frac1{64}
(0,0,0,5,18,19,1,10,0,0,0,0,8,3,0,0).
\]

The exact implementation audits all inherited P80/P81/P82 constraints and obtains

\[
\boxed{L_{80}=L_{81}=L_{82}=0.}
\]

For

\[
A=\{1100\},\qquad B=\{1101\},
\]

every model in the box satisfies

\[
q(A)-q(B)=0,
\]

while

\[
\widehat p(A)-\widehat p(B)=5/64,
\qquad
|A\triangle B|=2.
\]

Therefore

\[
\boxed{L_{83}=5/128.}
\]

**Provenance:** repository-original exact-rational P83 witness.

---

## 11. Tight upper witness

At the admissible prevalence

\[
\pi=5/16,
\]

the explicit P75 model law satisfies

\[
\boxed{
\|\widehat p-q_{5/16}\|_\infty=5/128.
}
\]

Together with the P83 lower bound this gives

\[
\boxed{
\inf_{\theta\in B_\theta}
\|\widehat p-q_\theta\|_\infty=5/128.
}
\]

**Provenance:** repository-original exact witness closure, verified in the P83 regression tests using exact `Fraction` arithmetic.

---

## 12. Inherited global and finite-sample handoffs

P83 uses its box lower bound inside the existing P78 branch-and-bound partition. It retains:

- explicit admissible P75 parameter points as valid global upper witnesses;
- the already-proved P78 mesh-width upper certificate;
- the P79 exact-rational upper certificate $\overline\varepsilon_{79}$ for the P77 sampling radius.

The rejection handoff is

\[
\boxed{
L_{83}(\mathcal B)>\overline\varepsilon_{79}
\Longrightarrow
\mathcal C_n(\widehat p)\cap\mathcal M_{4,2}=\varnothing.
}
\]

**Provenance:** inherited from P77-P79. P83 does not introduce or claim a new global convergence theorem or a new sampling theorem.

---

## 13. Executable sources

- theorem proof: [`proposition_83_signed_cylinder_contrast_separation.md`](proposition_83_signed_cylinder_contrast_separation.md)
- implementation: [`../src/consciousness_bridge/signed_cylinder_contrast_separation.py`](../src/consciousness_bridge/signed_cylinder_contrast_separation.py)
- regression tests: [`../tests/test_signed_cylinder_contrast_separation.py`](../tests/test_signed_cylinder_contrast_separation.py)
- theorem figure: [`figures/p83_signed_cylinder_contrast_separation.svg`](figures/p83_signed_cylinder_contrast_separation.svg)

---

## 14. Scientific boundary

P83 makes a declared model-distance certificate stronger by retaining shared-parameter compatibility across two observable events. It does not establish that the P75 family is a correct theory of experience, that its latent state is consciousness, or that consciousness has been derived from physics. The physical-to-experiential bridge remains an open scientific problem.
