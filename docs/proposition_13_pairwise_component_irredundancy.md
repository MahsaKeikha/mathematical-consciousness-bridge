# Proposition 13: pairwise causal-structure component insufficiency and irredundancy

## 1. Purpose

Proposition 12 proves that each major component of the intervention-resolved causal-structure candidate is individually insufficient to reconstruct the three-component physical fingerprint

\[
\boxed{
F_C(p)
=
(\mathcal G_p,\mathcal A_p,\mathcal K_p),
}
\]

where

\[
\mathcal G_p
\quad\text{is intervention-response geometry},
\]

\[
\mathcal A_p
\quad\text{is directed interventional influence},
\]

and

\[
\mathcal K_p
\quad\text{is the partition-irredundancy landscape}.
\]

Proposition 13 asks the stronger minimality question:

> Can any two of the three components reconstruct the third on a declared finite physical domain?

The answer is **no** for the explicit finite audit domain constructed below.

The theorem is a component-level minimality result for the labeled causal-structure fingerprint. It does not claim that the full raw physical object has been proved globally minimal among all possible mathematical representations, and it does not attach an experiential interpretation to the candidate.

---

# 2. General pairwise projection criterion

Let

\[
F_C:X\to
\mathcal Z_G\times\mathcal Z_A\times\mathcal Z_K
\]

be the three-component fingerprint.

Define the three pairwise projections

\[
H_{GA}(p)
=
(\mathcal G_p,\mathcal A_p),
\]

\[
H_{GK}(p)
=
(\mathcal G_p,\mathcal K_p),
\]

\[
H_{AK}(p)
=
(\mathcal A_p,\mathcal K_p).
\]

By the projection-collision theorem of Proposition 12, if for one retained pair \(H\) there exist systems \(p,p'\) with

\[
H(p)=H(p')
\qquad\text{but}\qquad
F_C(p)\ne F_C(p'),
\]

then no map \(g\) can satisfy

\[
F_C=g\circ H
\]

on that domain.

Therefore, to show that all three components are pairwise irredundant, it is enough to construct one collision for each omitted component.

---

# 3. Collision I - geometry plus influence do not determine partition irreducibility

We construct two two-block systems with two interventions \(u_0,u_1\), one delay \(\tau\), and four possible values per block.

Let the joint outcome space be

\[
\Omega
=
\{0,1,2,3\}\times\{0,1,2,3\}.
\]

Both systems use intervention-conditioned laws with **uniform one-block marginals**, so the declared matched intervention pair has zero directed marginal influence.

## 3.1 System \(p_{GA}^{(L)}\): two complementary degree-two regular supports

Define

\[
P_L^{u_0}(i,j)
=
\begin{cases}
\frac18,
&j-i\pmod 4\in\{0,1\},\\
0,&\text{otherwise},
\end{cases}
\]

and

\[
P_L^{u_1}(i,j)
=
\begin{cases}
\frac18,
&j-i\pmod 4\in\{2,3\},\\
0,&\text{otherwise}.
\end{cases}
\]

The supports are disjoint, hence

\[
\boxed{
d_L(u_0,u_1)=1.}
\]

Every row and every column contains two support points of mass \(1/8\), so both one-block marginals are uniform:

\[
P_{L,1}^{u_0}
=
P_{L,1}^{u_1}
=
P_{L,2}^{u_0}
=
P_{L,2}^{u_1}
=
\operatorname{Unif}\{0,1,2,3\}.
\]

Therefore the directed influence fingerprint for the matched pair is zero:

\[
\boxed{
\mathcal A_L=0.
}
\]

For the two-block partition

\[
\pi=\{\{1\},\{2\}\},
\]

the product of marginals is uniform on all 16 outcomes with mass \(1/16\). For either intervention, the response law has mass \(1/8\) on eight cells and zero on the other eight. Thus

\[
\boxed{
\kappa_L^\tau(\pi)=\frac12.
}
\]

## 3.2 System \(p_{GA}^{(H)}\): diagonal versus off-diagonal supports

Define

\[
P_H^{u_0}(i,j)
=
\begin{cases}
\frac14,&i=j,\\
0,&i\ne j,
\end{cases}
\]

and

\[
P_H^{u_1}(i,j)
=
\begin{cases}
0,&i=j,\\
\frac1{12},&i\ne j.
\end{cases}
\]

Again the supports are disjoint:

\[
\boxed{
d_H(u_0,u_1)=1.}
\]

Both distributions also have uniform one-block marginals, so

\[
\boxed{
\mathcal A_H=0.
}
\]

For \(u_0\), total variation from the uniform product distribution is

\[
\frac12
\left[
4\left|\frac14-\frac1{16}\right|
+
12\left|0-\frac1{16}\right|
\right]
=
\frac34.
\]

For \(u_1\), the corresponding value is \(1/4\). Since partition irreducibility takes the supremum over interventions,

\[
\boxed{
\kappa_H^\tau(\pi)=\frac34.
}
\]

Therefore

\[
\boxed{
\mathcal G_L=\mathcal G_H,
\qquad
\mathcal A_L=\mathcal A_H,
\qquad
\mathcal K_L\ne\mathcal K_H.
}
\]

Hence

\[
\boxed{
(\mathcal G,\mathcal A)
\text{ cannot reconstruct full }F_C.
}
\]

### Physical interpretation

Two systems can respond to perturbations with the same whole-system separation and the same marginal directed influence while differing substantially in how their joint response law factorizes across physical blocks.

---

# 4. Collision II - geometry plus partition irreducibility do not determine directed influence

Now use binary two-block outcomes.

## 4.1 System \(p_{GK}^{(0)}\): correlation swap

Let

\[
P_0^{u_0}
=
\frac12\delta_{00}
+
\frac12\delta_{11},
\]

\[
P_0^{u_1}
=
\frac12\delta_{01}
+
\frac12\delta_{10}.
\]

The supports are disjoint:

\[
\boxed{
d_0(u_0,u_1)=1.}
\]

Every single-block marginal is uniform under both interventions, so for the declared matched source pair

\[
\boxed{
\mathcal A_0=0.
}
\]

Each response law is at TV distance \(1/2\) from the product of its one-block marginals, hence

\[
\boxed{
\kappa_0^\tau(\pi)=\frac12.
}
\]

## 4.2 System \(p_{GK}^{(+)}\): correlated baseline plus deterministic response

Let

\[
P_+^{u_0}
=
\frac12\delta_{00}
+
\frac12\delta_{11},
\]

\[
P_+^{u_1}
=
\delta_{01}.
\]

The supports remain disjoint:

\[
\boxed{
d_+(u_0,u_1)=1.}
\]

The first intervention has partition irreducibility \(1/2\), while the deterministic second intervention factorizes exactly. Therefore

\[
\boxed{
\kappa_+^\tau(\pi)=\frac12.
}
\]

However, changing from \(u_0\) to \(u_1\) changes each one-block marginal from uniform to deterministic. The TV change is \(1/2\) at each target block. For the declared source-0 matched pair,

\[
\boxed{
A_{00}^{+}=A_{01}^{+}=\frac12,
}
\]

whereas the corresponding entries vanish in \(p_{GK}^{(0)}\).

Thus

\[
\boxed{
\mathcal G_0=\mathcal G_+,
\qquad
\mathcal K_0=\mathcal K_+,
\qquad
\mathcal A_0\ne\mathcal A_+.
}
\]

Hence

\[
\boxed{
(\mathcal G,\mathcal K)
\text{ cannot reconstruct full }F_C.
}
\]

### Physical interpretation

Whole-system response differentiation and partition dependence do not determine which physical block transmits the perturbational effect to which target block.

---

# 5. Collision III - influence plus partition irreducibility do not determine response geometry

Reuse the correlation-swap system

\[
P_D^{u_0}
=
\frac12\delta_{00}
+
\frac12\delta_{11},
\]

\[
P_D^{u_1}
=
\frac12\delta_{01}
+
\frac12\delta_{10}.
\]

and compare it with a system having identical correlated responses under both interventions:

\[
P_S^{u_0}
=
P_S^{u_1}
=
\frac12\delta_{00}
+
\frac12\delta_{11}.
\]

For both systems, all one-block marginals are uniform under both interventions. Therefore

\[
\boxed{
\mathcal A_D=\mathcal A_S=0.
}
\]

For both systems, the response law under at least one intervention lies at TV distance \(1/2\) from the product of its marginals, so

\[
\boxed{
\mathcal K_D=\mathcal K_S
=\left(\frac12\right).
}
\]

But

\[
\boxed{
d_D(u_0,u_1)=1,}
\]

whereas

\[
\boxed{
d_S(u_0,u_1)=0.}
\]

Thus

\[
\boxed{
\mathcal A_D=\mathcal A_S,
\qquad
\mathcal K_D=\mathcal K_S,
\qquad
\mathcal G_D\ne\mathcal G_S.
}
\]

Hence

\[
\boxed{
(\mathcal A,\mathcal K)
\text{ cannot reconstruct full }F_C.
}
\]

### Physical interpretation

Marginal influence and partition dependence can be identical even when one system strongly differentiates between interventions and another produces the same joint response every time.

---

# 6. Proposition 13 - pairwise component irredundancy theorem

Let \(D_{13}\) be the finite audit domain containing the systems constructed in Sections 3-5.

Then every two-component projection of

\[
F_C(p)
=
(\mathcal G_p,\mathcal A_p,\mathcal K_p)
\]

admits a projection collision on \(D_{13}\):

\[
\boxed{
H_{GA},
\quad
H_{GK},
\quad
H_{AK}
\text{ are all incomplete on }D_{13}.
}
\]

Equivalently, there do not exist maps

\[
g_{GA},g_{GK},g_{AK}
\]

such that

\[
F_C=g_{GA}\circ H_{GA},
\qquad
F_C=g_{GK}\circ H_{GK},
\qquad
F_C=g_{AK}\circ H_{AK}
\]

throughout \(D_{13}\).

Therefore each of the three major components is **irredundant relative to the other two** on this declared domain:

\[
\boxed{
\mathcal G
\not\preceq
(\mathcal A,\mathcal K),
\qquad
\mathcal A
\not\preceq
(\mathcal G,\mathcal K),
\qquad
\mathcal K
\not\preceq
(\mathcal G,\mathcal A),
}
\]

where \(X\preceq Y\) means that \(X\) is deterministically reconstructible from \(Y\) on the domain.

---

# 7. What this result establishes

**Proved on the declared finite audit domain:**

- response geometry cannot be omitted while retaining only directed influence and partition irreducibility;
- directed influence cannot be omitted while retaining only response geometry and partition irreducibility;
- partition irreducibility cannot be omitted while retaining only response geometry and directed influence;
- the three-component labeled causal-structure fingerprint is therefore pairwise irredundant on the domain.

**Not established by Proposition 13:**

- global minimality of the full raw causal-structure object over every possible physical domain;
- uniqueness of the particular \((\mathcal G,\mathcal A,\mathcal K)\) representation;
- that no alternative lower-dimensional sufficient representation exists after additional physical assumptions are imposed;
- bridge completeness with respect to experiential structure;
- an experiential interpretation of any component.

---

# 8. Why the result matters for the larger bridge program

P11 introduced a deliberately rich physical candidate. P12 showed that no single major component is enough. P13 now shows that **no pair is enough on the controlled domain either**.

This blocks three tempting reductions:

\[
\text{differentiation + recurrence/influence only},
\]

\[
\text{differentiation + irreducibility only},
\]

and

\[
\text{influence + irreducibility only}.
\]

A future reduced theory must therefore use additional assumptions strong enough to prove that the omitted component becomes reconstructible. Without such a theorem, dropping one component discards demonstrably independent physical information.

---

# 9. Next mathematical frontier

The next structural question is no longer whether the three components are pairwise redundant. They are not on \(D_{13}\).

The next frontier is **temporal continuation and composition**:

1. define time-indexed causal-structure states \(F_{\mathrm{causal}}(p_t)\);
2. determine what makes neighboring states part of one persistent physical process;
3. characterize how the causal structure behaves under independent composition and controlled coupling;
4. connect those temporal/compositional laws to the certified moving-subsystem machinery of Spatiotemporal Observer Mathematics;
5. test whether the resulting persistent causal structure improves cross-state and cross-substrate bridge discrimination.
