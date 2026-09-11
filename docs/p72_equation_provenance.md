# P72 equation and provenance record

This page classifies the main equations used in Proposition 72 so that standard mathematics, earlier repository results, new repository assembly, synthetic examples, and open empirical assumptions remain visibly distinct.

## Claim classification

| P72 object | Role | Status and provenance |
| --- | --- | --- |
| \(Y\perp\!\!\!\perp\Omega\mid(E^\star,T)\) | nondifferential target-measurement premise | declared model assumption, not inferred by P72 |
| \(I(Y;\Omega\mid T)\le I(E^\star;\Omega\mid T)\) | target-residual attenuation | standard conditional data-processing consequence assembled into the P19/P71 bridge setting by P72 |
| positive observed residual \(\Rightarrow\) positive latent residual | population witness transfer | repository P72 corollary under the declared measurement premise |
| erasure counterexample | shows null observed residual need not imply null latent residual | repository synthetic counterexample |
| \(\operatorname{TV}(Kp,Kq)\le\operatorname{TV}(p,q)\) | target-channel contraction | standard stochastic-kernel contraction, related to P17 |
| \(\gamma_t=\inf_{v\in\mathcal H\setminus\{0\}}\|K_tv\|_1/\|v\|_1\) | target-channel witness-stability coefficient | P72 definition |
| \(\gamma_t\operatorname{TV}(p,q)\le\operatorname{TV}(K_tp,K_tq)\) | lower witness-transfer bound | direct consequence of the P72 stability definition |
| \(\gamma_t>0\iff\ker K_t\cap\mathcal H=\{0\}\) | finite-dimensional non-erasure criterion | elementary finite-dimensional linear analysis applied to the P72 definition |
| \(\gamma=|1-2\eta|\) | binary symmetric target-channel stability | direct P72 derivation from the binary channel |
| coordinate Hoeffding radius | finite categorical target confidence control | standard Hoeffding inequality plus union bound |
| \(L_Y\) target-TV lower confidence bound | measurement-aware finite-data witness | P72 construction from standard concentration and TV triangle inequality |
| sufficient \(n\) scaling as \((\gamma_0\Delta_E)^{-2}\) | pre-data target-measurement design | P72 sufficient design corollary, conservative rather than minimax-optimal |

## Standard mathematical sources

### Conditional data processing

For fixed \(T=t\), the P72 measurement premise creates a Markov chain

\[
\Omega\to E^\star\to Y.
\]

The inequality

\[
I(Y;\Omega\mid T=t)
\le
I(E^\star;\Omega\mid T=t)
\]

is the ordinary data-processing inequality. Averaging over \(t\) gives the P72 conditional result.

Standard reference: T. M. Cover and J. A. Thomas, *Elements of Information Theory*, 2nd ed., Wiley, 2006. See the repository's [Foundational physics and mathematics bibliography](foundational_physics_mathematics_bibliography.md).

### Total-variation contraction

A stochastic kernel cannot increase total variation:

\[
\operatorname{TV}(KP,KQ)
\le
\operatorname{TV}(P,Q).
\]

This is standard probability/data-processing mathematics and is already used in the repository's physical coarse-graining branch, especially [P17](proposition_17_coarse_graining_and_refinement.md).

### Finite categorical concentration

P72D uses coordinate-wise Hoeffding bounds and a union bound over both samples and every predeclared observed-target category. The same conservative proof philosophy appears in [P20](proposition_20_finite_sample_residual_certification.md).

Standard source: W. Hoeffding, "Probability Inequalities for Sums of Bounded Random Variables," *Journal of the American Statistical Association* 58(301), 1963, 13-30.

## Repository-original role

P72 does not claim novelty for data processing, total-variation contraction, Hoeffding concentration, or elementary compactness arguments.

The repository-specific contribution is the explicit target-measurement theorem architecture:

\[
\boxed{
\text{P71 non-circular target provenance}
\to
\text{P72 declared target channel}
\to
\text{population residual transfer}
\to
\text{witness stability or erasure}
\to
\text{finite-data target certificate}.
}
\]

This architecture exposes a previously separate scientific obligation in the bridge program: an independently justified target can still fail to provide decisive evidence if the observation channel destroys or contaminates the target distinctions.

## External context on channel identifiability

P72 treats the target channel as declared or assumes a justified lower bound on its stability. It does not solve the separate problem of identifying an unknown noise transition matrix.

Relevant methodological context includes:

- Yang Liu, Hao Cheng, and Kun Zhang, "Identifiability of Label Noise Transition Matrix," *Proceedings of the 40th International Conference on Machine Learning*, PMLR 202, 2023, 21475-21496. The paper studies conditions under which noisy-label transition matrices are identifiable and emphasizes the difficulty of instance-dependent noise without extra information or assumptions.
- A. P. Dawid and A. M. Skene, "Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm," *Journal of the Royal Statistical Society: Series C*, 28(1), 1979, 20-28. The work provides a classical latent-response and observer-error model when the true response is unavailable.

These sources motivate the next identifiability problem. They are not required for the P72 data-processing proof.

## Scientific boundary

The notation \(E^\star\) is not an ontology claim. P72 does not prove that the latent target is consciousness or that any available report, behavioral measure, neural proxy, or clinical label is an exact observation of experience.

The theorem is conditional on a declared measurement process. If the measurement channel depends on \(\Omega\) beyond \((E^\star,T)\), the population no-false-positive transfer need not hold. If the channel is unknown or non-identifiable, its stability cannot simply be assumed.
