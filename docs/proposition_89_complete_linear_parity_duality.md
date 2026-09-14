# Proposition 89: Complete Linear Parity-Functional Duality Certificate

## Status

**Proved conditional computational theorem.** P89 closes a different gap from P88. P88 exhausts a finite integer coefficient box supported on exactly four of the eleven canonical P83 parity observables. P89 removes both restrictions at once: it considers **every real linear functional of all eleven canonical parity coordinates**.

The theorem gives an exact finite-dimensional duality between the strongest possible normalized linear-parity mismatch and a signed full-law perturbation problem. On the established P86-P88 exact rational witness, matching rational lower and upper certificates prove that the complete linear-parity optimum is

\[
\boxed{\frac{5}{168}},
\]

strictly stronger than the P88 value

\[
\boxed{\frac1{64}}.
\]

P89 is still a model-separation theorem for the declared P75 four-view binary latent target-measurement family. It does not identify the P75 latent state with consciousness, establish nonphysicality, validate a replacement model, or close the physical-to-experiential bridge.

---

## 1. Eleven canonical parity coordinates

Let

\[
\mathcal J
=
\{J\subseteq\{0,1,2,3\}:|J|\ge2\}.
\]

There are

\[
\binom42+\binom43+\binom44=6+4+1=11
\]

canonical nontrivial even-parity events

\[
H_J=\left\{x:\bigoplus_{j\in J}x_j=0\right\}.
\]

Write the corresponding parity vector as

\[
y(p)=\bigl(P_p(H_J)\bigr)_{J\in\mathcal J}\in\mathbb R^{11}.
\]

The implementation uses the fixed coordinate order

\[
\begin{aligned}
&(01),(02),(03),(12),(13),(23),\\
&(012),(013),(023),(123),(0123).
\end{aligned}
\]

For one P75 parameter vector \(\theta\), with latent branch \(s\in\{-,+\}\), response coordinates

\[
a_{j,s}=1-2q_{j,s},
\]

and prevalence \(\pi=P(S=+)\),

\[
P_\theta(H_J)
=
(1-\pi)\frac{1+\prod_{j\in J}a_{j,-}}2
+
\pi\frac{1+\prod_{j\in J}a_{j,+}}2.
\]

Each coordinate is multi-affine in the nine P75 parameters. Therefore every scalar linear functional of the eleven-vector is also multi-affine.

---

## 2. Exact vertex support for every linear parity functional

Let \(B\subset[0,1]^9\) be a rational axis-aligned P75 parameter box and let

\[
V_B=\{y(F(\theta)): \theta\in\operatorname{Vert}(B)\}
\]

be the distinct eleven-dimensional parity vectors at its parameter vertices.

For an arbitrary real coefficient vector

\[
c\in\mathbb R^{11}\setminus\{0\},
\]

define

\[
Q_c(p)=c^\top y(p).
\]

Because \(Q_c(F(\theta))\) is multi-affine in \(\theta\),

\[
\boxed{
I_B(c)
=
\left[
\min_{v\in V_B}c^\top v,
\max_{v\in V_B}c^\top v
\right]
}
\]

is the **exact** P75-box interval for that functional.

This is more than a computational convenience. It means the convex hull

\[
\operatorname{conv}(V_B)
\]

has exactly the same support function as the nonlinear P75 box image for every linear parity direction. P89 therefore characterizes the entire linear-functional envelope of the eleven P83 parity observables without imposing a coefficient radius or a support-size cutoff.

---

## 3. Full-law transfer norm

Let

\[
A_{xJ}=\mathbf 1_{H_J}(x),
\qquad
A\in\{0,1\}^{16\times11}.
\]

For a coefficient vector \(c\), the outcome score is

\[
g_c(x)=(Ac)_x.
\]

Two probability laws have equal total mass, so for any scalar \(a\),

\[
Q_c(p)-Q_c(q)
=
\sum_x\bigl(g_c(x)-a\bigr)\bigl(p(x)-q(x)\bigr).
\]

Define the exact centered transfer norm

\[
\boxed{
D(c)=\min_{a\in\mathbb R}
\sum_x|g_c(x)-a|.
}
\]

Then

\[
\boxed{
|Q_c(p)-Q_c(q)|
\le
D(c)\,\|p-q\|_\infty.
}
\]

For the eleven distinct nonconstant Walsh-parity coordinates used here, \(D(c)>0\) for every nonzero \(c\).

Given an empirical law \(\widehat p\), define

\[
\Delta_B(c)
=
\operatorname{dist}\bigl(c^\top y(\widehat p),I_B(c)\bigr).
\]

Every direction gives a valid full-law lower bound

\[
\boxed{
\|\widehat p-q\|_\infty
\ge
\frac{\Delta_B(c)}{D(c)}
}
\]

for every P75 law \(q\) generated inside \(B\).

---

## 4. Complete linear-parity optimum

Define

\[
\boxed{
L_{\mathrm{lin}}(B)
=
\sup_{c\ne0}
\frac{\Delta_B(c)}{D(c)}.
}
\]

This supremum ranges over **all real eleven-coordinate coefficient vectors**. It contains every single-event, pairwise, triple, P86 four-event, P87 bounded primitive, and P88 radius-three parity-functional direction as special cases. It does not, by itself, subsume the separate non-parity P82 branch, so the full P89 inherited certificate is

\[
\boxed{
L_{89}(B)=\max\{L_{88}(B),L_{\mathrm{lin}}(B)\}.
}
\]

Hence

\[
\boxed{L_{89}(B)\ge L_{88}(B)}
\]

pointwise.

---

## 5. Exact finite duality

P89 converts the unrestricted coefficient supremum into a finite exact upper-certificate problem.

Let the distinct box-vertex parity vectors be

\[
V_B=\{v^{(1)},\ldots,v^{(R)}\}.
\]

Define

\[
\boxed{
R_B(\widehat y)
=
\min_{\lambda,\delta}
\|\delta\|_\infty
}
\]

subject to

\[
\lambda_r\ge0,
\qquad
\sum_{r=1}^R\lambda_r=1,
\]

\[
\mathbf1^\top\delta=0,
\]

and

\[
\boxed{
\widehat y
=
\sum_{r=1}^R\lambda_rv^{(r)}+A^\top\delta.
}
\]

Here \(\delta\in\mathbb R^{16}\) is an algebraic signed full-law perturbation. It is **not** required to be a probability distribution.

### Proposition 89A: weak dual bound

For every feasible \((\lambda,\delta)\) and every nonzero \(c\),

\[
\frac{\Delta_B(c)}{D(c)}
\le
\|\delta\|_\infty.
\]

**Proof.** Let

\[
\bar v=\sum_r\lambda_rv^{(r)}.
\]

Because \(c^\top\bar v\) is a convex combination of vertex functional values,

\[
c^\top\bar v\in I_B(c).
\]

Therefore

\[
\Delta_B(c)
\le
|c^\top(\widehat y-\bar v)|
=
|(Ac)^\top\delta|.
\]

Since \(\mathbf1^\top\delta=0\), for any \(a\),

\[
(Ac)^\top\delta
=(Ac-a\mathbf1)^\top\delta.
\]

Thus

\[
|(Ac)^\top\delta|
\le
\|Ac-a\mathbf1\|_1\|\delta\|_\infty.
\]

Minimizing over \(a\) gives

\[
\Delta_B(c)
\le
D(c)\|\delta\|_\infty.
\]

Taking the supremum over \(c\) yields

\[
L_{\mathrm{lin}}(B)\le R_B(\widehat y).
\]

### Proposition 89B: equality by finite LP duality

The optimization defining \(R_B\) is a finite linear program after introducing one radius variable \(r\) and constraints

\[
-r\le\delta_x\le r.
\]

Its dual is the normalized complete linear-functional problem

\[
\max_{c}
\left[
 c^\top\widehat y-\max_{v\in V_B}c^\top v
\right]
\quad\text{subject to}\quad
D(c)\le1.
\]

Because \(c\) ranges over both signs, the dual objective is exactly the two-sided interval distance used in \(L_{\mathrm{lin}}\). Finite-dimensional LP strong duality therefore gives

\[
\boxed{
L_{\mathrm{lin}}(B)=R_B(\widehat y).
}
\]

When the box and empirical law are rational, the LP data are rational. Matching rational primal and dual certificates therefore prove an exact optimum without relying on floating-point rounding direction.

---

## 6. Proposition 89

For every rational empirical sixteen-cell law \(\widehat p\) and rational P75 parameter box \(B\):

1. every real linear functional of the eleven canonical parity coordinates has an exact P75-box interval determined by the finite vertex set \(V_B\);
2. every interval mismatch transfers to a valid full-law \(L_\infty\) lower bound through the exact centered norm \(D(c)\);
3. the strongest possible normalized linear-parity certificate satisfies
   \[
   L_{\mathrm{lin}}(B)=R_B(y(\widehat p));
   \]
4. a rational functional witness and a rational feasible perturbation certificate with equal objective values prove the exact unrestricted linear-parity optimum;
5. \(L_{89}(B)=\max\{L_{88}(B),L_{\mathrm{lin}}(B)\}\) is a valid lower bound on distance from \(\widehat p\) to every P75 law generated in \(B\), and \(L_{89}(B)\ge L_{88}(B)\) pointwise;
6. there exist exact rational boxes and empirical laws for which \(L_{\mathrm{lin}}(B)>L_{88}(B)\).

---

## 7. Exact strict witness

Use the same rational parameter box and sixteen-cell empirical law used in P86-P88. In the canonical P89 coordinate order, the empirical parity vector is

\[
\widehat y=
\left(
\frac38,
\frac{11}{24},
\frac{13}{24},
\frac12,
\frac7{12},
\frac23,
\frac{13}{24},
\frac{11}{24},
\frac38,
\frac23,
\frac38
\right).
\]

P88 gives

\[
\boxed{L_{88}(B)=\frac1{64}}.
\]

### 7.1 Exact lower certificate

Take

\[
\boxed{
c=(0,-2,-1,1,1,1,-2,-1,-3,2,-3).
}
\]

The exact empirical functional value is

\[
Q_c(\widehat p)=-\frac{13}{6}.
\]

Exact vertex evaluation gives

\[
I_B(c)=\left[-\frac{51}{8},-3\right].
\]

Therefore

\[
\Delta_B(c)
=-\frac{13}{6}-(-3)
=\frac56.
\]

The exact outcome coefficients are centered optimally at

\[
a=-3,
\]

with

\[
D(c)=28.
\]

Hence

\[
\boxed{
\frac{\Delta_B(c)}{D(c)}
=
\frac{5/6}{28}
=
\frac5{168}.
}
\]

### 7.2 Exact universal upper certificate

For this box, \(\pi=0\), so only the minus-branch response endpoint vector

\[
a_-=(a_{0,-},a_{1,-},a_{2,-},a_{3,-})
\]

matters. A convex combination of eight box-vertex parity vectors is sufficient. The nonzero weights are

| minus-branch response vertex | weight |
| --- | ---: |
| \((1/2,1/2,-1,1/2)\) | \(4/189\) |
| \((1/2,1/2,-1,-1)\) | \(4/21\) |
| \((1/2,-1,-1,1/2)\) | \(16/189\) |
| \((1/2,-1,-1,-1)\) | \(10/189\) |
| \((-1,1/2,0,1/2)\) | \(22/63\) |
| \((-1,1/2,-1,-1)\) | \(5/27\) |
| \((-1,-1,0,-1)\) | \(23/252\) |
| \((-1,-1,-1,1/2)\) | \(19/756\) |

These weights sum exactly to one.

The corresponding convex-combination parity vector is

\[
\bar v=
\left(
\frac5{12},
\frac{29}{56},
\frac{167}{336},
\frac{27}{56},
\frac{167}{336},
\frac{229}{336},
\frac{13}{24},
\frac{149}{336},
\frac{155}{336},
\frac{199}{336},
\frac{157}{336}
\right).
\]

Use the exact signed outcome perturbation, in lexicographic outcome order \(0000,0001,\ldots,1111\),

\[
\delta=
\left(
-\frac5{168},
-\frac5{168},
\frac5{168},
-\frac5{168},
-\frac5{168},
\frac1{84},
\frac5{168},
\frac5{168},
\frac5{168},
-\frac5{168},
-\frac5{168},
\frac5{168},
-\frac5{168},
\frac5{168},
\frac1{336},
\frac5{336}
\right).
\]

It satisfies

\[
\mathbf1^\top\delta=0,
\qquad
\|\delta\|_\infty=\frac5{168},
\]

and exact rational multiplication gives

\[
\boxed{
\widehat y=\bar v+A^\top\delta.
}
\]

Therefore Proposition 89A gives

\[
L_{\mathrm{lin}}(B)\le\frac5{168}.
\]

The functional lower certificate gives the reverse inequality, so

\[
\boxed{
L_{\mathrm{lin}}(B)=\frac5{168}.
}
\]

Finally,

\[
\boxed{
L_{88}(B)=\frac1{64}
<
L_{89}(B)=\frac5{168}.
}
\]

The difference is exact:

\[
\frac5{168}-\frac1{64}=\frac{19}{1344}>0.
\]

This proves that P88 did not saturate the complete linear parity-functional family and that P89 closes the entire remaining **linear** parity direction space for this witness.

---

## 8. What P89 closes, and what it does not

P89 closes the following gap:

> For the eleven canonical P83 parity observables, how strong can **any real linear functional** possibly be on a fixed rational P75 parameter box?

On the strict witness, the answer is now exact: \(5/168\). No larger coefficient radius, no denser support, and no other real linear combination of the same eleven parity coordinates can improve that number.

P89 does **not** prove that no stronger P75 separation exists. Future improvements can still come from, for example:

- nonlinear joint constraints among the parity coordinates;
- additional observables outside the current eleven-event family;
- tighter relaxations that use more of the nonlinear P75 image than its linear support function;
- direct full-law structure not expressible through these parity coordinates.

This distinction is essential. P89 is complete for the declared **linear parity-functional class**, not complete for all possible model-separation arguments.

---

## 9. Reproducibility

Implementation:

`src/consciousness_bridge/complete_linear_parity_duality.py`

Regression tests:

`tests/test_complete_linear_parity_duality.py`

Equation provenance:

`docs/p89_equation_provenance.md`

All witness quantities, convex weights, perturbations, interval endpoints, norms, and equality checks are represented with exact `fractions.Fraction` arithmetic. The implementation verifies both sides of the matching rational certificate.

---

## 10. Scientific interpretation boundary

P89 strengthens exact rejection of the declared P75 latent target-measurement family under the stated parameter-box assumptions. It does not establish that consciousness is nonphysical, identify a latent variable with experience, privilege parity observables as uniquely experiential, validate any alternative consciousness theory, imply an additional dimension of consciousness, or solve the physical-to-experiential bridge.
