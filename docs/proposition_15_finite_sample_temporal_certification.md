# Proposition 15: finite-sample certification of temporal continuation

## From estimated causal-structure trajectories to certified physical change

Proposition 14 defines a representation-independent temporal metric on the intervention-resolved causal-structure candidate. Proposition 15 addresses the next experimental question:

> If the causal-structure fingerprint at each time is estimated from finite data, when can an apparent temporal change be certified as physical rather than explained by estimation error?

The result is deliberately conditional. It assumes a valid simultaneous error radius for each estimated fingerprint. It then propagates those radii through the Proposition 14 quotient metric without adding a new consciousness criterion.

---

# 1. Setup

Let

\[
c_t=(g_t,a_t,k_t)
\]

be the true finite causal-structure fingerprint at physical time \(t\), and let

\[
\widehat c_t
\]

be its estimate.

Let \(D_w\) be the weighted component metric from Proposition 14 and let

\[
\overline D_w([c],[c'])
=\min_{h\in\mathcal H}D_w(c,hc')
\]

be the corresponding quotient metric over the declared finite relabeling group \(\mathcal H\).

Assume the simultaneous event

\[
\boxed{
D_w(c_t,\widehat c_t)\le \varepsilon_t
\quad\text{for every }t=0,\ldots,T
}
\]

holds. If this event is probabilistic, suppose it holds with probability at least \(1-\alpha\).

The radii \(\varepsilon_t\) may come from any scientifically justified estimator and concentration argument. Proposition 15 only concerns how those radii propagate through temporal comparison.

---

# 2. Proposition 15A - quotient-distance stability

Define

\[
d_{st}=\overline D_w([c_s],[c_t])
\]

and

\[
\widehat d_{st}
=\overline D_w([\widehat c_s],[\widehat c_t]).
\]

Then

\[
\boxed{
|\widehat d_{st}-d_{st}|
\le
\varepsilon_s+\varepsilon_t.
}
\]

Equivalently,

\[
\boxed{
\max\{0,\widehat d_{st}-\varepsilon_s-\varepsilon_t\}
\le d_{st}\le
\widehat d_{st}+\varepsilon_s+\varepsilon_t.
}
\]

## Proof

Because \(\overline D_w\) is a metric on the quotient space,

\[
d_{st}
\le
\overline D_w([c_s],[\widehat c_s])
+
\widehat d_{st}
+
\overline D_w([\widehat c_t],[c_t]).
\]

The quotient distance cannot exceed the raw distance obtained from the identity relabeling, so

\[
\overline D_w([c_s],[\widehat c_s])
\le D_w(c_s,\widehat c_s)
\le \varepsilon_s
\]

and similarly at time \(t\). Therefore

\[
d_{st}\le \widehat d_{st}+\varepsilon_s+\varepsilon_t.
\]

Exchanging true and estimated fingerprints gives

\[
\widehat d_{st}\le d_{st}+\varepsilon_s+\varepsilon_t.
\]

Combining the inequalities proves the result. \(\square\)

---

# 3. Certified temporal-change test

A nonzero lower confidence bound is

\[
\boxed{
L_{st}
=
\max\{0,\widehat d_{st}-\varepsilon_s-\varepsilon_t\}.
}
\]

Hence

\[
\boxed{
L_{st}>0
\Longrightarrow
d_{st}>0.
}
\]

So an observed change is certified as physically non-equivalent under the declared quotient whenever

\[
\boxed{
\widehat d_{st}>\varepsilon_s+\varepsilon_t.
}
\]

This is the exact deterministic separation threshold implied by the stated radii.

The converse is deliberately weaker: if

\[
\widehat d_{st}\le\varepsilon_s+\varepsilon_t,
\]

one cannot conclude that the true structures are equal. The data are simply insufficient to certify a nonzero separation at the declared error level.

---

# 4. Proposition 15B - cumulative path-variation bounds

For adjacent times, define

\[
d_t
=
\overline D_w([c_t],[c_{t+1}]),
\qquad
\widehat d_t
=
\overline D_w([\widehat c_t],[\widehat c_{t+1}]).
\]

Let

\[
V_{0:T}
=
\sum_{t=0}^{T-1}d_t,
\qquad
\widehat V_{0:T}
=
\sum_{t=0}^{T-1}\widehat d_t.
\]

Then

\[
\boxed{
|\widehat V_{0:T}-V_{0:T}|
\le
\varepsilon_0
+2\sum_{t=1}^{T-1}\varepsilon_t
+\varepsilon_T.
}
\]

Define

\[
E_V
=
\varepsilon_0
+2\sum_{t=1}^{T-1}\varepsilon_t
+\varepsilon_T.
\]

Then

\[
\boxed{
\max\{0,\widehat V_{0:T}-E_V\}
\le V_{0:T}\le
\widehat V_{0:T}+E_V.
}
\]

## Proof

Apply Proposition 15A to every adjacent pair:

\[
|\widehat d_t-d_t|
\le \varepsilon_t+\varepsilon_{t+1}.
\]

Summing and applying the triangle inequality gives

\[
|\widehat V-V|
\le
\sum_{t=0}^{T-1}(\varepsilon_t+\varepsilon_{t+1}),
\]

which equals \(E_V\). \(\square\)

---

# 5. Proposition 15C - maximum-step certification

Let

\[
J_{0:T}=\max_t d_t,
\qquad
\widehat J_{0:T}=\max_t \widehat d_t.
\]

Define

\[
E_J
=
\max_{0\le t<T}(\varepsilon_t+\varepsilon_{t+1}).
\]

Then

\[
\boxed{
|\widehat J_{0:T}-J_{0:T}|
\le E_J.
}
\]

Therefore

\[
\boxed{
\max\{0,\widehat J_{0:T}-E_J\}
\le J_{0:T}\le
\widehat J_{0:T}+E_J.
}
\]

This turns Proposition 14's descriptive maximum-jump statistic into a finite-error certificate.

---

# 6. Thresholded continuity and discontinuity certificates

Suppose a physical application declares a scientifically meaningful structural-change threshold \(\eta>0\).

For an adjacent step \(t\to t+1\):

## Certified change larger than \(\eta\)

If

\[
\boxed{
\widehat d_t-(\varepsilon_t+\varepsilon_{t+1})>\eta,
}
\]

then

\[
d_t>\eta.
\]

## Certified change no larger than \(\eta\)

If

\[
\boxed{
\widehat d_t+(\varepsilon_t+\varepsilon_{t+1})\le\eta,
}
\]

then

\[
d_t\le\eta.
\]

## Unresolved band

If neither condition holds, the data do not decide whether the true structural change crosses \(\eta\).

This three-way classification is preferable to forcing every finite-data comparison into a binary continuous/discontinuous label.

---

# 7. Finite-sample corollary for bounded fingerprint coordinates

A simple explicit corollary is available when every fingerprint coordinate is itself the expectation of a random variable in \([0,1]\), estimated by an IID sample mean.

Suppose there are \(M\) scalar coordinates per time point and \(T+1\) time points, each estimated from \(n\) IID repetitions. Hoeffding's inequality and a union bound give the simultaneous coordinate radius

\[
\boxed{
\delta_n(\alpha)
=
\sqrt{
\frac{1}{2n}
\log\left(
\frac{2M(T+1)}{\alpha}
\right)
}.
}
\]

For the weighted max metric,

\[
D_w(c_t,\widehat c_t)
\le
w_{\max}\,\delta_n(\alpha),
\qquad
w_{\max}=\max\{w_G,w_A,w_K\},
\]

simultaneously for all \(t\) with probability at least \(1-\alpha\).

Thus one may take

\[
\boxed{
\varepsilon_t
=
w_{\max}\delta_n(\alpha)
}
\]

for all times in this bounded-coordinate model and insert that radius directly into Propositions 15A-15C.

This corollary does **not** claim that every causal-structure coordinate in Proposition 11 is automatically a direct sample mean. More complicated estimators require their own concentration analysis.

---

# 8. What Proposition 15 establishes

Proposition 15 establishes, under declared simultaneous fingerprint-error radii:

1. an exact Lipschitz stability bound for quotient temporal distance;
2. a finite-error certificate for nonzero physical structural change;
3. lower and upper bounds for cumulative path variation;
4. lower and upper bounds for the maximum temporal jump;
5. thresholded continuity, discontinuity, and unresolved classifications;
6. a simple explicit IID bounded-coordinate sample-size corollary.

The result is representation aware because all temporal comparisons are made with the Proposition 14 quotient metric.

---

# 9. What Proposition 15 does not establish

It does not establish:

- that temporal smoothness is sufficient for consciousness;
- that a large causal-structure jump implies loss of consciousness;
- that the weighting \(w\) or threshold \(\eta\) is universal;
- that every Proposition 11 coordinate has the same estimator or concentration law;
- that temporal continuation implies experiential identity;
- that the physical-to-experiential bridge has been solved.

Those remain separate scientific questions.

---

# 10. Scientific role

P14 upgrades the physical candidate from a static object to a trajectory on a quotient space. P15 upgrades that trajectory from a descriptive construction to a finite-error experimental object.

The resulting chain is

\[
\boxed{
\text{controlled physical response}
\longrightarrow
\text{causal-structure fingerprint}
\longrightarrow
\text{quotient temporal trajectory}
\longrightarrow
\text{finite-data continuation certificate}.
}
\]

The next structural questions are composition, splitting, merging, controlled coupling, and the interface between a certified moving physical subsystem and the time-indexed causal structure carried by that subsystem.

---

## References used for this proposition

- Burago, D., Burago, Y., and Ivanov, S. *A Course in Metric Geometry*. American Mathematical Society, 2001. Used for metric and quotient-space background.
- Hoeffding, W. "Probability Inequalities for Sums of Bounded Random Variables." *Journal of the American Statistical Association* 58(301), 1963: 13-30. DOI: 10.1080/01621459.1963.10500830. Used only for the bounded-coordinate finite-sample corollary.
- Pearl, J. *Causality: Models, Reasoning, and Inference*, 2nd ed. Cambridge University Press, 2009. Used for intervention semantics inherited from Proposition 11.

These references support the mathematical tools and intervention language. They do not imply endorsement of the repository's consciousness-bridge program.