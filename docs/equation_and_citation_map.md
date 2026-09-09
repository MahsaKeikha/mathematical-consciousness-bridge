# Equation and Citation Map

This page distinguishes repository definitions, standard mathematics, physical modeling assumptions, bridge hypotheses, theorem statements, theory-family translations, and empirical evidence.

The purpose is provenance: a reader should be able to see immediately whether an equation is defined here, inherited from standard mathematics, adapted from an external theory, or supported by experiment.

---

# 1. Physical and bridge objects

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(p=(\mathcal X,\mathcal D,\mathfrak I,\mathcal O)\) | declared physical-system object | repository definition | physical modeling framework |
| \(dX_t=f(X_t,u_t)dt+G(X_t,u_t)dW_t\) | example stochastic physical model | standard stochastic modeling form | stochastic dynamics |
| \(K_{\Delta t}(\cdot\mid X_t,u_t)\) | transition-kernel form | standard stochastic dynamics | probability/Markov modeling |
| \(\mathcal B\subseteq\mathcal P\times\mathcal E\) | general physical-to-experiential bridge relation | repository definition | consciousness-bridge formulation |
| \(p\sim_Pp'\) | physically irrelevant representation equivalence | repository definition, theory-dependent | quotient-space framework |
| \(e\sim_Ee'\) | experiential equivalence | repository definition, open formalization | mathematical-consciousness context including Kleiner 2019 |
| \(\mathcal Q_P=\mathcal P/{\sim_P}\) | physical quotient | repository construction using standard quotient mathematics | Proposition 1 |
| \(\mathcal Q_E=\mathcal E/{\sim_E}\) | experiential quotient | repository construction using standard quotient mathematics | Proposition 1 |
| \(\bar B:\mathcal Q_P\to\mathcal Q_E\) | quotient-level bridge | repository construction | Proposition 1 |
| \(B=\bar B\circ\pi_P\) | bridge factorization through physical quotient | proved | Proposition 1 + standard quotient logic |

---

# 2. Theory identifiability and experiment design

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(P_i^{\pi,q}\) | observable law predicted by complete bridge theory \(i\) under protocol \(\pi\) | repository notation | Proposition 2 |
| \(\|P-Q\|_{\mathrm{TV}}\) | statistical distance controlling binary distinguishability | standard probability/statistics | Le Cam-Yang; Tsybakov |
| \(\Delta_\Pi=\sup_{\pi\in\Pi}\|P_1^{\pi,q}-P_2^{\pi,q}\|_{\mathrm{TV}}\) | experiment-class bridge discriminability | repository construction | Proposition 2 |
| \(R_\pi^*=\tfrac12(1-\|P_1-P_2\|_{\mathrm{TV}})\) | optimal equal-prior one-shot error | standard testing identity applied to bridge theories | decision theory; Proposition 2 |
| \(\exp(-n\eta^2/2)\) | repeated-event discrimination error bound | standard concentration applied here | Hoeffding 1963; Proposition 2 |
| \(\Phi_{\Pi,q}(\mathfrak T)=(P_{\mathfrak T}^{\pi,q})_{\pi\in\Pi}\) | complete observable fingerprint of a theory | repository construction | Proposition 3 |
| \(\Theta/{\sim_{\Pi,q}}\cong\operatorname{Im}(\Phi_{\Pi,q})\) | observational theory-space quotient | proved | Proposition 3 + standard quotient logic |
| \(d_{ij}(\pi)=\|P_i^{\pi,q}-P_j^{\pi,q}\|_{\mathrm{TV}}\) | protocol-specific theory-pair separation | repository construction | Proposition 4 |
| \(U(S)=\min_{\{i,j\}\in\mathcal U}\max_{\pi\in S}d_{ij}(\pi)\) | worst-pair protocol-family separation | repository construction | Proposition 4 |
| \(U(S)>0\iff\bigcup_{\pi\in S}C_\pi=\mathcal U\) | complete-discrimination/set-cover equivalence | proved | Proposition 4 + finite set-cover structure |

---

# 3. Physical-feature sufficiency and completeness

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(F:\mathcal Q_P\to\mathcal Z\) | proposed representation-invariant physical feature | generic repository notation | Proposition 5 |
| \(\bar B=g\circ F\) | bridge factorization through physical feature | definition of bridge sufficiency | Proposition 5 + standard factorization logic |
| \(F(p)=F(p')\Rightarrow\bar B(p)=\bar B(p')\) | fiber-constancy criterion | proved equivalent to factorization | Proposition 5 |
| \(\sim_F\subseteq\sim_B\) | sufficient-feature partition refines bridge partition | proved equivalent characterization | Proposition 5 |
| \(p\sim_Bp'\iff\bar B(p)=\bar B(p')\) | bridge-induced physical equivalence | repository definition | Proposition 6 |
| \(\mathcal Q_B=\mathcal Q_P/{\sim_B}\) | canonical bridge quotient | repository construction | Proposition 6 |
| \(C_B(p)=[p]_{\sim_B}\) | canonical complete bridge signature | repository construction | Proposition 6 |
| \(C_B(p)=C_B(p')\iff\bar B(p)=\bar B(p')\) | canonical completeness | proved | Proposition 6 |
| \(\mathcal Q_B\cong\operatorname{Im}(\bar B)\) | canonical quotient/bridge-image equivalence | proved | Proposition 6 |
| \(C_B=h_F\circ F\) | every sufficient feature determines canonical bridge signature | proved | Proposition 6 |
| \(F(p)=F(p')\iff\bar B(p)=\bar B(p')\) | bridge-complete physical signature condition | repository definition + theorem target | Proposition 6 |

---

# 4. Experimental recovery of a complete signature

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\Psi_\Pi(p)=(P^{\pi,p})_{\pi\in\Pi}\) | complete experimental fingerprint of a physical realization | repository construction | Proposition 7 |
| \(F_*=D_F\circ\Psi_\Pi\) | experimental decoder for target signature | definition of recoverability | Proposition 7 |
| \(\Psi_\Pi(p)=\Psi_\Pi(p')\Rightarrow F_*(p)=F_*(p')\) | exact recoverability criterion | proved | Proposition 7 |
| equal observable fingerprint + different signature | exact experimental no-go counterexample | proved | Proposition 7 |
| \(d_S(p,p')=\max_{\pi\in S}\|P^{\pi,p}-P^{\pi,p'}\|_{\mathrm{TV}}\) | protocol-family distance between physical systems | repository construction | Proposition 8 |
| \(\omega_S\) | maximum within-signature experimental spread | repository definition | Proposition 8 |
| \(\delta_S\) | minimum between-signature experimental separation | repository definition | Proposition 8 |
| \(\gamma_S=\delta_S-\omega_S\) | robust signature gap | repository construction | Proposition 8 |
| \(|\widehat d_S-d_S|\le2\varepsilon\) | pair-distance perturbation bound | proved from TV triangle inequality | Proposition 8 |
| \(\gamma_S>4\varepsilon\) | sufficient deterministic exact-partition recovery condition | proved | Proposition 8 |

---

# 5. Finite categorical sample complexity

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\Pr(|\widehat p_j-p_j|>a)\le2e^{-2na^2}\) | one-category empirical-frequency concentration | standard inequality | Hoeffding 1963 |
| \(\|\widehat P-P\|_{\mathrm{TV}}=\tfrac12\sum_j|\widehat p_j-p_j|\) | categorical total-variation identity | standard probability |
| \(2MK\exp(-8n\varepsilon^2/K^2)\) | uniform failure bound over \(M\) system/protocol cells and at most \(K\) outcomes | proved by Hoeffding + union bounds | Proposition 9 |
| \(n\ge\frac{K^2}{8\varepsilon^2}\log\frac{2MK}{\alpha}\) | sufficient trials per cell for uniform TV radius \(\varepsilon\) | proved | Proposition 9A |
| \(\varepsilon=\gamma_S/8\) | conservative error target with recovery slack | repository design choice | Proposition 9B |
| \(n\ge\frac{8K^2}{\gamma_S^2}\log\frac{2N_PN_\pi K}{\alpha}\) | sufficient categorical trials per cell for exact signature-partition recovery | proved | Proposition 9B |
| \(\tau_*=(\omega_S+\delta_S)/2\) | midpoint recovery threshold | repository construction | Proposition 9B |

---

# 6. Candidate consciousness-theory feature families

The following are source-grounded translations into the generic feature notation. They are not claims that each named theory reduces to one scalar or one universally agreed implementation.

| Theory family | Generic feature notation in this repository | Primary source role |
| --- | --- | --- |
| IIT 4.0 | \(\mathcal F_{\mathrm{IIT}}(p)=\) intrinsic cause-effect structure and associated maximal-substrate organization | Albantakis et al. 2023 |
| GNWT | \(\mathcal F_{\mathrm{GNW}}(p)=\) multilevel workspace organization, ignition, and global availability | Dehaene-Changeux 2011; Changeux-Farisco 2026 |
| RPT | \(\mathcal F_{\mathrm{RPT}}(p)=\) relevant recurrent-processing structure/dynamics | Lamme 2006 |
| HOT | \(\mathcal F_{\mathrm{HOT}}(p)=\) theory-specific higher-order representational relation | Brown-Lau-LeDoux 2019 |
| predictive/NR/active-inference families | \(\mathcal F_{\mathrm{PP}}(p)=\) theory-specific predictive, inferential, and representational structure | Seth-Hohwy 2021; Pennartz 2022; Corcoran et al. 2026 |

Detailed caveats and source roles are maintained in [Candidate Theory Families](candidate_theory_families.md) and the [Literature Map](literature_map.md).

---

# 7. External conceptual and empirical landmarks

| Item | Role in this repository | Source |
| --- | --- | --- |
| observer/factorization question | physical-subsystem conceptual background | Tegmark 2015 |
| phenomenal axioms to physical postulates | example of explicit bridge architecture | IIT 4.0 |
| mathematical representation of experience | formal consciousness-modeling context | Kleiner 2019; Kleiner-Tull |
| unfolding-equivalence challenge | identifiability/no-go motivation | Doerig et al. 2019 |
| preregistered IIT/GNWT adversarial predictions | contemporary cross-theory empirical benchmark | Cogitate Consortium et al. 2025 |
| IIT/NR/active-inference adversarial comparison framework | current cross-theory prediction-design context | Corcoran et al. 2026 |
| certified moving subsystem/world-tube | candidate physical-domain interface | Spatiotemporal Observer Mathematics |

---

# 8. Proposition-to-source map

| Repository result | Standard mathematical/statistical source role | Consciousness-science source role |
| --- | --- | --- |
| P1 representation invariance | quotient-set logic | Tegmark/Kleiner representation context |
| P2 identifiability | total variation; binary decision theory; Hoeffding | unfolding challenge; adversarial theory testing |
| P3 theory quotient | equivalence relations and quotient sets | multiple competing theory families |
| P4 experiment design | finite optimization and set cover | adversarial experiment design |
| P5 feature sufficiency | factorization through fibers | theory-specific physical feature claims |
| P6 canonical complete signature | quotient/factorization mathematics | universal physical-signature target |
| P7 experimental recoverability | factorization of observable fingerprints | empirical accessibility of bridge claims |
| P8 robust recovery | metric triangle inequality and deterministic perturbation | finite measurement uncertainty |
| P9 sample complexity | Hoeffding + union bounds | explicit trial requirements for signature recovery |

---

# 9. Citation discipline

A theorem in this repository is cited as a repository result when the bridge-specific statement or construction is introduced here.

External literature is cited only for the conceptual, mathematical, statistical, physical, or empirical role it actually supplies.

The project maintains the distinction

\[
\boxed{
\text{definition}
\neq
\text{bridge axiom}
\neq
\text{physical model}
\neq
\text{theorem}
\neq
\text{empirical evidence}.
}
\]

This distinction is central to the final proof target: mathematics can establish what follows from bridge premises, while the physical-to-experiential premises themselves must be justified by independently discriminating evidence.
