# Proposition 8: robust recovery of bridge-signature classes under distribution error

## Physical question

Proposition 7 is an exact population statement. Real experiments provide estimated probability laws rather than exact laws.

The next question is therefore:

> If experimental outcome distributions are estimated with finite error, when is the partition induced by a proposed complete bridge signature still recovered exactly?

Proposition 8 gives a deterministic perturbation theorem. A later concentration theorem can supply the probability that its uniform estimation event holds.

---

# 1. Finite experimental domain

Let

\[
\mathcal Q_0
\subseteq
\mathcal Q_P
\]

be a finite declared family of physical realizations and let

\[
S\subseteq\Pi
\]

be a finite protocol family.

Let

\[
F_*:\mathcal Q_0\to\mathcal Z_*
\]

be a proposed bridge-complete signature on this domain.

For each

\[
p\in\mathcal Q_0,
\qquad
\pi\in S,
\]

let

\[
P^{\pi,p}
\]

be the true observable probability law and let

\[
\widehat P^{\pi,p}
\]

be its estimate from data.

---

# 2. Pairwise experimental distance

For two physical realizations define

\[
\boxed{
d_S(p,p')
=
\max_{\pi\in S}
\left\|
P^{\pi,p}-P^{\pi,p'}
\right\|_{\mathrm{TV}}.
}
\]

The estimated counterpart is

\[
\boxed{
\widehat d_S(p,p')
=
\max_{\pi\in S}
\left\|
\widehat P^{\pi,p}-\widehat P^{\pi,p'}
\right\|_{\mathrm{TV}}.
}
\]

Define the maximum within-signature spread

\[
\boxed{
\omega_S
=
\max_{F_*(p)=F_*(p')}
d_S(p,p')
}
\]

and the minimum between-signature separation

\[
\boxed{
\delta_S
=
\min_{F_*(p)\ne F_*(p')}
d_S(p,p').
}
\]

If there are no distinct within-signature pairs, set \(\omega_S=0\). The theorem assumes at least two signature classes so \(\delta_S\) is defined.

The population signature gap is

\[
\boxed{
\gamma_S
=
\delta_S-\omega_S.
}
\]

---

# 3. Uniform distribution-estimation event

Assume

\[
\boxed{
\sup_{p\in\mathcal Q_0}
\sup_{\pi\in S}
\left\|
\widehat P^{\pi,p}-P^{\pi,p}
\right\|_{\mathrm{TV}}
\le
\varepsilon.
}
\]

This proposition is deterministic conditional on that event.

---

# 4. Proposition

## Proposition 8

Under the uniform estimation event above, for every pair \(p,p'\),

\[
\boxed{
\left|
\widehat d_S(p,p')-d_S(p,p')
\right|
\le
2\varepsilon.
}
\]

Consequently, if

\[
\boxed{
\gamma_S
=
\delta_S-\omega_S
>
4\varepsilon,
}
\]

then the interval

\[
\boxed{
(\omega_S+2\varepsilon,
\delta_S-2\varepsilon)
}
\]

is nonempty.

For any threshold \(\tau\) in that interval,

\[
\boxed{
F_*(p)=F_*(p')
\iff
\widehat d_S(p,p')<\tau.
}
\]

Therefore the complete signature partition on \(\mathcal Q_0\) is recovered exactly from the estimated experimental laws.

If the uniform estimation event holds with probability at least \(1-\alpha\), then the same partition-recovery conclusion holds with probability at least \(1-\alpha\).

---

# 5. Proof

For one protocol \(\pi\), the reverse triangle inequality for a metric gives

\[
\begin{aligned}
&\left|
\|\widehat P^{\pi,p}-\widehat P^{\pi,p'}\|_{\mathrm{TV}}
-
\|P^{\pi,p}-P^{\pi,p'}\|_{\mathrm{TV}}
\right|\\
&\qquad\le
\|\widehat P^{\pi,p}-P^{\pi,p}\|_{\mathrm{TV}}
+
\|\widehat P^{\pi,p'}-P^{\pi,p'}\|_{\mathrm{TV}}\\
&\qquad\le2\varepsilon.
\end{aligned}
\]

Thus every protocol-specific pair distance changes by at most \(2\varepsilon\).

For real families \(a_\pi,b_\pi\),

\[
\left|
\max_\pi a_\pi-
\max_\pi b_\pi
\right|
\le
\max_\pi|a_\pi-b_\pi|.
\]

Therefore

\[
\boxed{
|\widehat d_S(p,p')-d_S(p,p')|
\le2\varepsilon.
}
\]

Now suppose

\[
F_*(p)=F_*(p').
\]

Then by definition

\[
d_S(p,p')\le\omega_S,
\]

so

\[
\widehat d_S(p,p')
\le
\omega_S+2\varepsilon
<
\tau.
\]

Conversely, if

\[
F_*(p)\ne F_*(p'),
\]

then

\[
d_S(p,p')\ge\delta_S,
\]

and hence

\[
\widehat d_S(p,p')
\ge
\delta_S-2\varepsilon
>
\tau.
\]

Thus thresholding \(\widehat d_S\) recovers the true pairwise signature-equivalence relation exactly.

Since an equivalence relation is determined by all of its pairwise same-class decisions, the signature partition is recovered exactly.

If the uniform estimation event has probability at least \(1-\alpha\), all preceding deterministic conclusions hold on that event, giving the same probability lower bound for exact partition recovery.

\[
\boxed{\text{QED}}
\]

---

# 6. Physical interpretation

The key quantity is not merely whether different signature classes have different mean signals.

The experiment family must create a separation gap

\[
\gamma_S
=
\delta_S-\omega_S
\]

between:

- the largest experimentally visible difference among systems that should belong to the **same** signature class;
- the smallest experimentally visible difference among systems that should belong to **different** signature classes.

Finite measurement error consumes this gap at twice the error radius on each side, producing the requirement

\[
\boxed{
\gamma_S>4\varepsilon.
}
\]

This is the first finite-error bridge-signature recovery criterion in the repository.

---

# 7. Why within-class spread matters

Two physical systems may receive the same complete-signature value while differing in other measurable physical properties.

Therefore the correct recovery problem is not generally

\[
\text{same signature}\iff d_S=0.
\]

Instead the theorem allows

\[
\omega_S>0.
\]

The experiments may retain irrelevant substrate detail, provided the within-class spread stays sufficiently below the between-class separation.

This distinction is important for substrate-general theories of consciousness.

---

# 8. Connection to experiment design

Proposition 4 optimized protocols for separating theory pairs.

For signature recovery, the natural robust design objective becomes

\[
\boxed{
\Gamma(S)
=
\delta_S-\omega_S.
}
\]

A good experiment family should simultaneously:

1. increase separation between different candidate consciousness-signature classes;
2. suppress or factor out irrelevant variation within one signature class.

Thus the experiment-design target is not simply maximal neural difference. It is maximal **between-class minus within-class** discriminability.

This will motivate a later robust experiment-design proposition.

---

# 9. Connection to finite sample size

Proposition 8 is conditional on

\[
\sup_{p,\pi}
\|\widehat P^{\pi,p}-P^{\pi,p}\|_{\mathrm{TV}}
\le\varepsilon.
\]

The next statistical layer will derive a sufficient sample size for this event when outcomes are discrete and empirical frequencies are used.

That theorem will turn

\[
\gamma_S>4\varepsilon
\]

into an explicit relation among:

- number of physical systems;
- number of protocols;
- outcome alphabet size;
- desired confidence;
- number of repeated trials;
- signature separation gap.

---

# 10. Status

| Item | Status |
| --- | --- |
| within-signature spread \(\omega_S\) | defined |
| between-signature separation \(\delta_S\) | defined |
| signature gap \(\gamma_S\) | defined |
| pair-distance perturbation bound | proved |
| exact threshold recovery under \(\gamma_S>4\varepsilon\) | proved |
| probability transfer from uniform estimation event | proved |
| sample-size guarantee for the uniform event | next theorem |

The next result is Proposition 9: finite categorical sample complexity for exact signature-partition recovery.
