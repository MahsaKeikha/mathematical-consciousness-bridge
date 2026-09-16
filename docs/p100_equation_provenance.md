# P100 Equation and Novelty Provenance

## Scope

P100 extends the repository's fixed-round P99 evidence certificate into a sequential, anytime-valid process. The novelty claim is deliberately narrow.

P100 does not claim to invent supermartingales, predictable betting, e-processes, Ville's inequality, optional stopping, or time-uniform sequential testing. Those are standard mathematical and statistical tools.

The repository-specific contribution is the exact integration of those standard tools with the P92-P99 certification chain: each new round is itself a selection-valid P99 e-value certificate; the current plan, calibration, and stake must be frozen from past information; the current certification data must remain conditionally fresh given that past; exact rational betting factors are accumulated; and the public checkpoint shows that two individually non-decisive P99 rounds can cross the 95 percent threshold anytime-validly.

## Standard ingredients

The following ingredients are standard and are not claimed as repository-original:

1. **Conditional e-value validity.** A nonnegative random variable `E_t` satisfying
   \[
   \mathbb E[E_t\mid\mathcal F_{t-1}]\le1
   \]
   may be used as one step in a sequential evidence process.
2. **Predictable convex reserve factor.** If `eta_t` is `F_{t-1}`-measurable and lies in `[0,1]`, then
   \[
   F_t=(1-\eta_t)+\eta_tE_t
   \]
   has conditional expectation at most one.
3. **Nonnegative supermartingale product.** If `M_0=1` and
   \[
   M_t=M_{t-1}F_t,
   \]
   then the conditional factor bound implies
   \[
   \mathbb E[M_t\mid\mathcal F_{t-1}]\le M_{t-1}.
   \]
4. **Ville's inequality.** For a nonnegative supermartingale starting at one,
   \[
   \Pr\left(\sup_tM_t\ge1/\alpha\right)\le\alpha.
   \]
5. **Anytime-valid threshold monitoring.** The process may be inspected after each step and rejection may occur at the first threshold crossing without an additional multiplicity penalty for the number of inspection times.
6. **Optional stopping for the declared rule.** A stopping time adapted to the filtration may determine when the process is inspected for the declared crossing event, provided the supermartingale construction itself has not been invalidated.

Standard references used for this layer include:

Ville, J. (1939). *Etude critique de la notion de collectif*. Paris: Gauthier-Villars.

Howard, S. R., Ramdas, A., McAuliffe, J., and Sekhon, J. (2021). *Time-uniform, nonparametric, nonasymptotic confidence sequences*. The Annals of Statistics 49(2), 1055-1080. DOI: 10.1214/20-AOS1991.

Vovk, V. and Wang, R. (2021). *E-values: Calibration, combination, and applications*. The Annals of Statistics 49(3), 1736-1754. DOI: 10.1214/20-AOS2020.

## Repository-specific dependency chain

P100 depends on the following established repository results:

- **P92:** exact three-minor sign-coherence obstruction for the declared mixed-prevalence P75 family at witness radius `1/24`.
- **P94:** exact finite-sample localized rejection under a declared finite dependence range.
- **P95:** predeclared drift regimes with familywise error control.
- **P96:** selection-valid holdout certification when pilot selection is separated from fresh certification data.
- **P97:** simultaneous protection for a finite same-data candidate family through explicit multiplicity accounting.
- **P98:** cross-fitted selection-valid certification across mutually independent certification blocks with own-fold exclusion.
- **P99:** exact conversion of valid fold rejections into e-values, finite exact-rational threshold mixtures, convex fold aggregation under arbitrary final-fold dependence, and global rejection by the threshold `1/alpha`.

P100 does not weaken any of these prerequisites. It adds a new outer sequential layer.

## Sequential filtration

Let

\[
\mathcal F_0\subseteq\mathcal F_1\subseteq\cdots
\]

record all information revealed through completed certification rounds.

Before round `t`, all design choices used by that round are required to be measurable with respect to `F_{t-1}`. The code records this requirement through

`choices_predictable_from_past_only=True`.

The current certification data must also satisfy the stronger sequential freshness declaration

`certification_data_conditionally_fresh_given_past=True`.

The resulting P99 round e-value must obey

\[
\boxed{
\mathbb E[E_t\mid\mathcal F_{t-1}]\le1.
}
\]

This conditional inequality is the critical bridge from P99 fixed-round validity to P100 sequential validity.

## Predictable reserve factor

Choose an exact-rational stake

\[
\eta_t\in[0,1]
\]

using past information only. Define

\[
\boxed{
F_t=(1-\eta_t)+\eta_tE_t.
}
\]

Then

\[
\begin{aligned}
\mathbb E[F_t\mid\mathcal F_{t-1}]
&=(1-\eta_t)+\eta_t\mathbb E[E_t\mid\mathcal F_{t-1}]\\
&\le1.
\end{aligned}
\]

No independence between `E_t` and the past is asserted. The required statement is the conditional e-value bound under the current round's declared data-generating contract.

## Sequential e-process

Set

\[
M_0=1
\]

and

\[
\boxed{
M_t
=\prod_{s=1}^{t}F_s
=\prod_{s=1}^{t}\bigl((1-\eta_s)+\eta_sE_s\bigr).
}
\]

Because `M_{t-1}` is nonnegative and measurable with respect to `F_{t-1}`,

\[
\begin{aligned}
\mathbb E[M_t\mid\mathcal F_{t-1}]
&=M_{t-1}\mathbb E[F_t\mid\mathcal F_{t-1}]\\
&\le M_{t-1}.
\end{aligned}
\]

Therefore

\[
\boxed{
(M_t)_{t\ge0}\text{ is a nonnegative supermartingale.}
}
\]

## Anytime-valid crossing rule

Ville's inequality gives

\[
\boxed{
\Pr\left(\sup_{t\ge0}M_t\ge\frac1\alpha\right)\le\alpha.
}
\]

For

\[
T_\alpha=\inf\{t\ge1:M_t\ge1/\alpha\},
\]

this implies

\[
\boxed{
\Pr(T_\alpha<\infty)\le\alpha.
}
\]

P100 therefore controls the probability of ever crossing the declared rejection threshold under the sequential global null. The statement is time-uniform and is not a fixed-horizon union bound over rounds.

## Exact moderate-evidence checkpoint

P99's balanced `K=2`, `B=2`, `m=1` design at fold level

\[
\tau=\frac1{25}
\]

has one-fold-rejection aggregate value

\[
\boxed{
E_t=\frac12\cdot25=\frac{25}{2}.
}
\]

At global 95 percent confidence,

\[
\frac1\alpha=20,
\]

so

\[
\frac{25}{2}<20.
\]

One such P99 round is not itself decisive.

With the predictable half stake

\[
\eta_t=\frac12,
\]

the P100 factor is

\[
\boxed{
F_t
=\frac12+\frac12\cdot\frac{25}{2}
=\frac{27}{4}.
}
\]

After two fresh rounds with that realized evidence,

\[
\boxed{
M_2
=\left(\frac{27}{4}\right)^2
=\frac{729}{16}
=45.5625
>20.
}
\]

Thus the declared P100 checkpoint first rejects at round two.

## Exact sample accounting

The inherited P99 round has:

\[
\boxed{3774}
\]

observations per regime at the mathematical crossing and

\[
\boxed{3792}
\]

at the first exact denominator-24 replication.

With two regimes per fold and two genuinely different folds per round, one P99 round uses

\[
\boxed{15096}
\]

or

\[
\boxed{15168}
\]

unique observations.

The two-round P100 checkpoint therefore uses

\[
\boxed{30192}
\]

or

\[
\boxed{30336}
\]

unique observations.

These are exact checkpoint totals, not universal lower bounds and not claims of optimal sample complexity.

## Reserve property

At the default half stake, a zero round e-value gives

\[
\boxed{
F_t=\frac12.
}
\]

Hence

\[
M_t=\frac12M_{t-1}.
\]

The process is reduced but not annihilated. This property is operationally useful because a later fresh round can still contribute evidence.

The half stake is a transparent checkpoint choice. P100 does not claim it is uniquely optimal.

## Exact implementation contract

The P100 implementation uses exact rational arithmetic and enforces the following guards:

- the round list must be nonempty;
- global alpha must be an exact `Fraction` strictly between zero and one;
- every round must have a nonempty unique identity;
- every stake must be an exact `Fraction` in `[0,1]`;
- current-round choices must be declared predictable from past information only;
- current certification data must be declared conditionally fresh given the past;
- P99 certification blocks inside each round must satisfy the established within-round independence contract;
- each P99 fold must exclude its own certification block from selection;
- nested P99 validity is recomputed rather than accepted from an unaudited supplied scalar.

The regression suite also verifies the exact `25/2`, `27/4`, and `729/16` arithmetic and the `30192/30336` sample totals.

## Novelty boundary

The strongest defensible novelty statement is:

> P100 supplies a repository-specific anytime-valid outer certification layer for the P92-P99 exact finite-data chain. It composes fresh P99 e-value rounds with predictable reserve stakes into an exact-rational nonnegative supermartingale, protects adaptive inspection and stopping by Ville's inequality, and gives a reproducible two-round checkpoint in which individually non-decisive P99 evidence accumulates to rejection.

The following are not claimed as original:

- e-values;
- e-processes;
- test martingales;
- supermartingales;
- Ville's inequality;
- predictable betting;
- optional stopping theory;
- general sequential hypothesis testing.

## Scientific boundary

P100's guarantee is conditional on the declared null and data-separation assumptions. It does not make invalid data fresh by declaration. In particular, it does not validate:

- a current stake chosen after observing the current e-value;
- a current calibration chosen after observing current certification outcomes;
- reuse of the same certification observations across rounds;
- hidden dependence between current certification data and past history that destroys the conditional expectation bound;
- pseudo-independent segmentation of one dependent stream without a valid argument;
- misspecified finite dependence ranges;
- unrestricted drift;
- model acceptance from non-rejection;
- identification of the latent state with consciousness;
- nonphysicality of consciousness;
- completion of the physical-to-experiential bridge.

P100 changes the temporal evidence calculus. It does not change the ontology or the scientific interpretation boundary of the research program.
