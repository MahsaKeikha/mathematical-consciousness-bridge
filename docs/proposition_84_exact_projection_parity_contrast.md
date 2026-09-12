# Proposition 84: Exact Joint Projection-Parity Contrast Certificate

## Status

**Proved conditional computational theorem.** P84 strengthens the complete P83 certificate for the same declared P75 four-view binary latent family and the same full-law $L_\infty$ distance.

P83 tests 22 projection-parity events separately. For each parity event it computes the exact probability range over a P75 parameter box. Separate interval compatibility does not imply that two observed parity probabilities are jointly attainable by one common P75 parameter assignment. P84 tests that missing shared-parameter compatibility directly.

P84 is a model-distance certification result. It does not establish that the P75 latent state is consciousness, does not validate the P75 model when rejection fails, and does not close the physical-to-experiential bridge.

---

## 1. Question left open by P83

For a selected view set $J$ and parity $b\in\{0,1\}$, define

\[
H(J,b)=\left\{x:\bigoplus_{j\in J}x_j=b\right\}.
\]

P83 computes an exact box interval for every standard event $H(J,b)$ with two, three, or four selected views.

Suppose two empirical parity probabilities each fall inside their own exact P75 box intervals. That establishes only separate compatibility. It does not prove that one common parameter vector inside the box can realize both values simultaneously.

For two parity events

\[
H_1=H(J_1,b_1),
\qquad
H_2=H(J_2,b_2),
\]

with different view sets, P84 therefore studies the coupled contrast

\[
\boxed{
C=P(H_1)-P(H_2).
}
\]

The key requirement is joint optimization over the shared physical response parameters. P84 does not subtract two independently optimized P83 intervals.

---

## 2. Exact branchwise contrast formula

Inside latent branch $s\in\{-,+\}$, conditional independence gives the P83 identity

\[
P_s(H(J,b))
=
\frac{1+(-1)^b\prod_{j\in J}(1-2q_{j,s})}{2}.
\]

Therefore

\[
\boxed{
C_s
=
\frac12
\left[
(-1)^{b_1}\prod_{j\in J_1}(1-2q_{j,s})
-
(-1)^{b_2}\prod_{j\in J_2}(1-2q_{j,s})
\right].
}
\]

Let

\[
U=J_1\cup J_2.
\]

Every response coordinate indexed by $U$ appears with degree at most one. Hence $C_s$ is multi-affine on the response-coordinate box. A multi-affine function on a rectangular box attains its extrema at endpoint vertices.

Since there are only four observed views,

\[
|U|\le4,
\]

so at most

\[
2^4=16
\]

endpoint assignments need to be checked per latent branch.

This gives the exact branch interval

\[
C_s\in[c_s^L,c_s^U].
\]

The phrase **common endpoint vertices** is essential: the two parity probabilities are optimized together through their shared response coordinates.

---

## 3. Exact latent-mixture interval

The minus-branch and plus-branch response coordinates are disjoint. Once their exact branch intervals are known, the full latent mixture is

\[
C(\pi)
=(1-\pi)C_-+\pi C_+.
\]

Prevalence $\pi$ is a separate coordinate and enters affinely. Therefore its exact extrema occur at the prevalence endpoints.

If

\[
\pi\in[\pi_L,\pi_U],
\]

then the exact P75 box interval is obtained from the branch extrema and the two prevalence endpoints. The result is an exact parameter-box image interval, not a conservative enclosure formed by subtracting separate P83 ranges.

---

## 4. Standard P84 contrast family

P83 has 22 parity events: both parity values for each of the 11 nontrivial view sets of sizes two, three, and four.

P84 considers unordered event pairs and retains the genuinely coupled contrasts whose view sets differ. Pairs that are algebraically redundant with a single P83 event or collapse to already-covered nested residual structure are excluded by the executable standard-family construction.

The resulting standard family contains exactly

\[
\boxed{220}
\]

genuinely coupled parity-event contrasts.

The implementation and regression suite verify this count exactly.

---

## 5. Transfer to full-law $L_\infty$ distance

For parity events $H_1$ and $H_2$, define

\[
c_x=1_{H_1}(x)-1_{H_2}(x).
\]

Then

\[
C(p)-C(q)
=
\sum_x c_x\bigl(p(x)-q(x)\bigr),
\]

and therefore

\[
|C(p)-C(q)|
\le
\left(\sum_x|c_x|\right)\|p-q\|_\infty.
\]

For the standard genuinely coupled contrasts used by P84, the signed coefficient support has eight observed cells. Thus

\[
\sum_x|c_x|=8.
\]

If an empirical contrast lies a distance $g$ outside its exact P75 box interval, then

\[
\boxed{
\|\widehat p-q\|_\infty\ge\frac{g}{8}.
}
\]

Let $L_{\mathrm{joint-parity}}(B)$ be the maximum of these exact lower bounds over the 220 standard contrasts on box $B$.

---

## 6. P84 theorem

For every admissible P78 parameter box $B$, define

\[
\boxed{
L_{84}(B)
=
\max\{L_{83}(B),L_{\mathrm{joint-parity}}(B)\}.
}
\]

Then:

1. $L_{84}(B)$ is a rigorous lower bound on the $L_\infty$ distance from the empirical law to every P75 law generated inside $B$;
2. $L_{84}(B)\ge L_{83}(B)\ge L_{82}(B)\ge L_{81}(B)\ge L_{80}(B)\ge L_{78}(B)$;
3. every retained branchwise P84 contrast interval is exact over the declared response-coordinate box;
4. every full latent-mixture contrast interval is exact over the complete P75 parameter box;
5. all interval endpoints and lower bounds remain exactly rational when the empirical law and parameter-box endpoints are rational;
6. for any finite partition $\mathcal B$ of the complete P75 parameter cube,

\[
\boxed{
L_{84}(\mathcal B)
:=
\min_{B\in\mathcal B}L_{84}(B)
\le
d_\infty(\widehat p,\mathcal M_{4,2});
}
\]

7. on the same partition, $L_{84}(\mathcal B)\ge L_{83}(\mathcal B)$;
8. explicit P75 parameter vectors remain valid global upper-bound witnesses;
9. the previously proved P78 mesh-width upper certificate remains valid and is retained unchanged. P84 does not claim a new convergence-rate theorem.

---

## 7. Proof

### 7.1 Exact branch interval

Each parity-event probability is affine in each branch response coordinate separately. Their difference is therefore multi-affine in the union of the two view sets. Multi-affine extrema over a rectangular box occur at vertices, so evaluating all common endpoint assignments gives the exact branch interval.

### 7.2 Exact mixture interval

Minus-branch and plus-branch response coordinates are disjoint. Their branch extrema can be attained independently and simultaneously. Prevalence is also a separate coordinate and enters affinely, so evaluating its two endpoints gives the exact full-box mixture interval.

### 7.3 Soundness of the $L_\infty$ lower bound

The event-difference functional has eight nonzero coefficients of magnitude one in every retained standard contrast. Hence

\[
|C_{\widehat p}-C_q|
\le
8\|\widehat p-q\|_\infty.
\]

Every P75 law inside $B$ has its contrast inside the exact model interval. Therefore distance of the empirical contrast to that interval divided by eight is a valid full-law lower bound. Maximizing over the 220 retained contrasts preserves soundness.

### 7.4 Dominance

By construction,

\[
L_{84}(B)
=
\max\{L_{83}(B),L_{\mathrm{joint-parity}}(B)\},
\]

so P84 is never weaker than P83 on the same box. Taking minima over a common complete partition preserves partition-level dominance.

---

## 8. Strict exact-rational witness

The regression suite contains an exact rational parameter box and empirical sixteen-cell law for which the complete P83 audit is compatible:

\[
\boxed{L_{83}(B)=0.}
\]

The strongest P84 witness compares the standard parity events

\[
H_1=H(\{1,3\},0),
\qquad
H_2=H(\{1,2,3\},1),
\]

using zero-based implementation indices. The declared P75 box allows the exact joint contrast range

\[
\boxed{C(B)\in[0,1/2].}
\]

The empirical law instead gives

\[
\boxed{\widehat C=-1/4.}
\]

so the exact contrast gap is

\[
\boxed{g=1/4.}
\]

The signed coefficient support has eight cells. Therefore

\[
L_{\mathrm{joint-parity}}(B)
=
\frac{1/4}{8}
=
\boxed{\frac1{32}}.
\]

Thus

\[
\boxed{
L_{84}(B)=\frac1{32}>0=L_{83}(B).
}
\]

This establishes a strict exact-rational strengthening: every individual P83 parity interval can be compatible while their shared-parameter joint contrast is impossible.

---

## 9. Global branch-and-bound handoff

The P84 lower bound replaces the P83 box lower bound inside the existing exact-rational branch-and-bound architecture.

For a partition $\mathcal B$ of the complete parameter cube,

\[
L_{84}(\mathcal B)
=
\min_{B\in\mathcal B}L_{84}(B)
\]

is a valid global lower certificate. Explicit P75 parameter vectors remain valid global upper-bound witnesses. The previously proved P78 mesh-width upper certificate remains valid because the underlying model-distance problem is unchanged.

No new convergence-rate theorem is claimed by P84.

---

## 10. Finite-data handoff

Let $\overline\varepsilon_{79}$ be the P79 certified rational upper bound on the P77 cellwise sampling radius. The same strict finite-data rejection gate applies:

\[
\boxed{
L_{84}(\mathcal B)>\overline\varepsilon_{79}
\Longrightarrow
\text{reject the declared P75 family under the stated finite-data guarantee.}
}
\]

If the strict inequality fails, the result is inconclusive. Failure to reject is not model validation.

---

## 11. Executable record

### Source implementation

- [`src/consciousness_bridge/joint_projection_parity_contrast_separation.py`](../src/consciousness_bridge/joint_projection_parity_contrast_separation.py)

### Regression tests

- [`tests/test_joint_projection_parity_contrast_separation.py`](../tests/test_joint_projection_parity_contrast_separation.py)

The tests verify:

1. exactly 220 standard genuinely coupled contrasts;
2. exact agreement between the analytic box interval and exhaustive parameter-box vertex evaluation on a nontrivial rational box;
3. strict improvement from $L_{83}=0$ to $L_{84}=1/32$ on the exact witness;
4. eight-cell signed coefficient support for the named strict witness;
5. boxwise dominance $L_{84}\ge L_{83}$;
6. exact-rational global branch-and-bound behavior;
7. explicit scientific-boundary language in the implementation.

---

## 12. Scientific interpretation boundary

P84 establishes a stronger conditional separation certificate for one declared latent-variable target-measurement model family. It does **not** establish any of the following:

- that the P75 model is true when the certificate is small;
- that the model's latent state is consciousness;
- that parity is a consciousness measure;
- that consciousness is nonphysical;
- that failure of the P75 model falsifies every physical theory;
- that the physical-to-experiential bridge has been solved.

The result is deliberately narrower and stronger: separate compatibility of exact parity events does not imply their joint compatibility with one underlying parameter assignment. P84 adds an exact family of shared-parameter constraints and proves, through a rational strict witness, that those constraints can matter.

The bridge remains open.
