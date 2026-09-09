# Foundational Physics, Mathematics, and Spaceflight Bibliography

This bibliography complements the consciousness-theory [Literature Map](literature_map.md). It is organized by **scientific role**, because the repository draws from several different disciplines and those sources should not be treated as interchangeable evidence.

The categories are:

1. mathematical foundations;
2. physical dynamics and statistical mechanics;
3. information theory and information geometry;
4. causal inference and intervention;
5. complexity, integration, and neural dynamics;
6. empirical consciousness measurement;
7. consciousness-theory and adversarial-testing literature;
8. spaceflight and extreme-environment research.

A source in sections 1-5 supplies mathematics or physics. A source in section 6 supplies empirical consciousness evidence. A source in section 7 supplies consciousness-theory architecture or comparison. A source in section 8 supplies an application/test environment. None of those roles are equivalent.

---

# 1. Information theory

## Shannon 1948

Claude E. Shannon, "A Mathematical Theory of Communication," *Bell System Technical Journal* 27 (1948): 379-423, 623-656.

DOI Part I: [10.1002/j.1538-7305.1948.tb01338.x](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x).

**Role:** foundational definition of entropy and information in communication theory.

Core object:

\[
H(X)=-\sum_x p(x)\log p(x).
\]

Mutual information may be written

\[
I(X;Y)
=
D_{\mathrm{KL}}(P_{XY}\Vert P_XP_Y).
\]

**Repository use:** information-theoretic dependence, conditional information, and the mathematical language used by several consciousness theories and by the companion observer project.

## Cover and Thomas 2006

Thomas M. Cover and Joy A. Thomas, *Elements of Information Theory*, 2nd ed., Wiley, 2006. DOI: [10.1002/047174882X](https://doi.org/10.1002/047174882X).

**Role:** standard modern reference for entropy, mutual information, conditional information, data processing, and information-theoretic inequalities.

---

# 2. Information geometry

## Amari 2016

Shun-ichi Amari, *Information Geometry and Its Applications*. Applied Mathematical Sciences 194, Springer, 2016. DOI: [10.1007/978-4-431-55978-8](https://doi.org/10.1007/978-4-431-55978-8).

**Role:** foundational modern reference for differential-geometric structure on statistical manifolds.

For a parameterized probability family \(p(x\mid\theta)\), the Fisher metric is

\[
\boxed{
g_{ij}(\theta)
=
\mathbb E_\theta
\left[
\partial_i\log p(X\mid\theta)
\partial_j\log p(X\mid\theta)
\right].
}
\]

**Repository use:** candidate future geometry for comparing families of intervention-conditioned distributions beyond one total-variation summary.

## Ay, Jost, Le, and Schwachhofer 2017

Nihat Ay, Jurgen Jost, Hong Van Le, and Lorenz Schwachhofer, *Information Geometry*. Ergebnisse der Mathematik und ihrer Grenzgebiete 64, Springer, 2017. DOI: [10.1007/978-3-319-56478-4](https://doi.org/10.1007/978-3-319-56478-4).

**Role:** rigorous mathematical foundations for statistical manifolds, Fisher metric, Amari-Chentsov tensor, sufficient statistics, and geometric inference.

---

# 3. Thermodynamics and physics of information

## Landauer 1961

Rolf Landauer, "Irreversibility and Heat Generation in the Computing Process," *IBM Journal of Research and Development* 5(3) (1961): 183-191. DOI: [10.1147/rd.53.0183](https://doi.org/10.1147/rd.53.0183).

**Role:** foundational link between logically irreversible information processing and physical dissipation.

For erasure of one classical bit at temperature \(T\), the standard Landauer bound is

\[
\boxed{
W_{\mathrm{erase}}
\ge
k_B T\ln 2.
}
\]

**Repository use:** establishes that information processing is physically embodied. It is not used as a consciousness criterion.

## Seifert 2012

Udo Seifert, "Stochastic thermodynamics, fluctuation theorems and molecular machines," *Reports on Progress in Physics* 75(12) (2012): 126001. DOI: [10.1088/0034-4885/75/12/126001](https://doi.org/10.1088/0034-4885/75/12/126001).

**Role:** modern framework for work, heat, entropy production, and fluctuation relations along stochastic nonequilibrium trajectories.

A representative entropy-production decomposition is written schematically as

\[
\Delta s_{\mathrm{tot}}
=
\Delta s_{\mathrm{sys}}
+
\Delta s_{\mathrm{med}}.
\]

**Repository use:** future thermodynamic layer for testing whether candidate causal structures obey measurable energetic and nonequilibrium constraints.

---

# 4. Stochastic dynamics and dynamical systems

## Uhlenbeck and Ornstein 1930

George E. Uhlenbeck and Leonard S. Ornstein, "On the Theory of the Brownian Motion," *Physical Review* 36 (1930): 823-841. DOI: [10.1103/PhysRev.36.823](https://doi.org/10.1103/PhysRev.36.823).

**Role:** classical stochastic relaxation model and physical lineage for continuous-time temporal correlation.

## Doob 1942

Joseph L. Doob, "The Brownian Movement and Stochastic Equations," *Annals of Mathematics* 43(2) (1942): 351-369. DOI: [10.2307/1968873](https://doi.org/10.2307/1968873).

**Role:** Gaussian Markov-process context.

## Peters, Bauer, and Pfister 2020

Jonas Peters, Stefan Bauer, and Niklas Pfister, "Causal Models for Dynamical Systems," arXiv:2001.06208.

**Role:** modern causal-model language for dynamical systems.

---

# 5. Causal inference and intervention

## Pearl 2009

Judea Pearl, *Causality: Models, Reasoning, and Inference*, 2nd ed., Cambridge University Press, 2009.

**Role:** standard intervention and structural-causal-model foundation.

The notation

\[
P(Y\mid do(u))
\]

represents a distribution under controlled intervention rather than ordinary observational conditioning.

**Repository use:** intervention-conditioned causal-response laws in Proposition 11 and subsequent composition/temporal results.

---

# 6. Complexity, integration, and neural organization

## Tononi, Sporns, and Edelman 1994

Giulio Tononi, Olaf Sporns, and Gerald M. Edelman, "A measure for brain complexity: relating functional segregation and integration in the nervous system," *Proceedings of the National Academy of Sciences* 91(11) (1994): 5033-5037.

**Role:** early mathematical treatment of the balance between functional segregation and integration in neural systems.

**Repository use:** historical context for structured rather than purely scalar descriptions of neural organization.

## Tononi 2004

Giulio Tononi, "An Information Integration Theory of Consciousness," *BMC Neuroscience* 5 (2004): 42. DOI: [10.1186/1471-2202-5-42](https://doi.org/10.1186/1471-2202-5-42).

**Role:** foundational integrated-information consciousness-theory paper.

## Albantakis et al. 2023

Larissa Albantakis et al., "Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms," *PLOS Computational Biology* 19(10) (2023): e1011465. DOI: [10.1371/journal.pcbi.1011465](https://doi.org/10.1371/journal.pcbi.1011465).

**Role:** current formal IIT architecture linking phenomenal axioms to physical postulates and intrinsic cause-effect structure.

---

# 7. Empirical consciousness measurement

## Casali et al. 2013

Adenauer G. Casali et al., "A theoretically based index of consciousness independent of sensory processing and behavior," *Science Translational Medicine* 5(198) (2013): 198ra105. DOI: [10.1126/scitranslmed.3006294](https://doi.org/10.1126/scitranslmed.3006294).

**Role:** perturbational-complexity work combining direct cortical perturbation with distributed neural response.

**Repository use:** motivates direct perturbation-response measurement rather than passive correlational structure alone.

## Maschke et al. 2024

Charlotte Maschke et al., "Critical dynamics in spontaneous EEG predict anesthetic-induced loss of consciousness and perturbational complexity," *Communications Biology* 7 (2024): 946. DOI: [10.1038/s42003-024-06613-8](https://doi.org/10.1038/s42003-024-06613-8).

**Role:** empirical relation among spontaneous critical dynamics, anesthesia-induced loss of consciousness, and perturbational complexity.

## Luppi et al. 2024

Andrea I. Luppi et al., "A synergistic workspace for human consciousness revealed by Integrated Information Decomposition," *eLife* 12 (2024): RP88173. DOI: [10.7554/eLife.88173](https://doi.org/10.7554/eLife.88173).

**Role:** empirical information-decomposition study connecting synergistic information integration with conscious state.

## Luppi et al. 2026

Andrea I. Luppi et al., "Convergent transcriptomic and connectomic controllers of information integration and its anaesthetic breakdown across mammalian brains," *Nature Human Behaviour* 10 (2026): 777-802. DOI: [10.1038/s41562-025-02381-5](https://doi.org/10.1038/s41562-025-02381-5).

**Role:** cross-species work relating information integration, dynamical control, biological organization, and anesthesia.

---

# 8. Mathematical consciousness and theory comparison

## Tegmark 2015

Max Tegmark, "Consciousness as a State of Matter," *Chaos, Solitons & Fractals* 76 (2015): 238-270. DOI: [10.1016/j.chaos.2015.03.014](https://doi.org/10.1016/j.chaos.2015.03.014).

**Role:** physics/factorization lineage and conceptual background for observer-like physical organization.

## Kleiner 2019

Johannes Kleiner, "Mathematical Models of Consciousness," arXiv:1907.03223.

**Role:** mathematical formalization of consciousness models and experiential spaces.

## Kleiner and Tull 2020

Johannes Kleiner and Sean Tull, "The Mathematical Structure of Integrated Information Theory," arXiv:2002.07655.

**Role:** axiomatic mathematical formalization of IIT structure.

## Seth and Bayne 2022

Anil K. Seth and Tim Bayne, "Theories of consciousness," *Nature Reviews Neuroscience* 23 (2022): 439-452. DOI: [10.1038/s41583-022-00587-4](https://doi.org/10.1038/s41583-022-00587-4).

**Role:** major comparative review of leading consciousness theories.

## Cogitate Consortium et al. 2025

Cogitate Consortium et al., "Adversarial testing of global neuronal workspace and integrated information theories of consciousness," *Nature* 642 (2025): 133-142. DOI: [10.1038/s41586-025-08888-1](https://doi.org/10.1038/s41586-025-08888-1).

**Role:** preregistered adversarial test of major theory predictions using fMRI, MEG, and intracranial EEG.

---

# 9. Spaceflight and extreme-environment research

The spaceflight literature is used as an **application and robustness-testing domain**, not as evidence for a physical-to-experiential bridge.

## NASA Human Research Program

NASA, **Human Research Program (HRP)**.

Official resource: `https://www.nasa.gov/hrp/`

**Role:** umbrella program studying health and performance risks associated with human spaceflight, including behavioral performance, human factors, radiation, and physiological countermeasures.

## NASA Human Factors and Behavioral Performance

NASA, **Human Factors and Behavioral Performance (HFBP)**.

Official resource: `https://www.nasa.gov/reference/about-human-factors-and-behavioral-performance/`

NASA describes HFBP research as addressing behavioral health and performance risks relevant to Moon, Mars, and deep-space missions, including sleep, cognitive function, team performance, human-robotic interaction, isolation/confinement, radiation, and altered gravity.

**Repository role:** authoritative application context for robustness of temporal state estimation, cognitive/neural measurement, and human-system monitoring under combined environmental stressors.

## NASA HFBP risks

NASA, **Human Factors and Behavioral Performance - Spaceflight Risks**.

Official resource: `https://www.nasa.gov/hrp/human-factors-and-behavioral-performance/hfbp-risks/`

Relevant risk areas include behavioral/psychiatric change, inadequate sleep and irregular schedules, teamwork, and systems-operations support.

## NASA sleep/circadian/workload risk

NASA, **Risk of Performance Decrements and Adverse Health Outcomes Resulting from Sleep Loss, Circadian Desynchronization, and Work Overload**.

Official resource: `https://www.nasa.gov/directorates/esdmd/hhp/risk-of-performance-decrements-and-adverse-health-outcomes-resulting-from-sleep-loss-circadian-desynchronization-and-work-overload/`

**Role:** authoritative evidence synthesis connecting sleep quantity/quality, circadian disturbance, fatigue, and cognitive/operational performance in spaceflight.

## NASA ARCHeR

NASA, **Artemis Research for Crew Health & Readiness (ARCHeR)**.

Official resource: `https://www.nasa.gov/reference/archer/`

ARCHeR measures astronaut well-being, activity, sleep patterns, interactions, and behavioral performance around Artemis deep-space missions.

**Repository role:** example of prospective longitudinal human-performance measurement under a combined extreme-environment exposure regime.

---

# 10. How these sources connect to the bridge program

The repository's multidisciplinary source logic is

\[
\boxed{
\begin{array}{c}
\text{physics and dynamical systems}\\
\downarrow\\
\text{probability, information, geometry, causality}\\
\downarrow\\
\text{measurable neural / biological organization}\\
\downarrow\\
\text{controlled perturbation and empirical state comparisons}\\
\downarrow\\
\text{candidate physical equivalence classes}\\
\downarrow\\
\text{bridge identifiability and falsification}\\
\downarrow\\
\text{formal experiential structure}
\end{array}
}
\]

The purpose of the bibliography is to make the provenance of each arrow explicit.

A physics source does not establish a consciousness bridge. An empirical neural correlate does not by itself establish sufficiency. A mathematical consciousness formalism does not by itself establish empirical truth. The research program is designed to test where these layers can legitimately be connected.