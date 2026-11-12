# References

Primary sources and exact versions used in the scientific comparison. Bibliographic metadata and theorem locations were checked on 12 November 2026. The descriptions identify each source's role; the project's own guarantees are established in its science pages rather than attributed to those antecedents.

## andress2025

Joseph Andress, Alexander Engel, Yuan Shi, and Scott Parker. **Quantum simulation of nonlinear dynamical systems using repeated measurement.** *Journal of Plasma Physics* **91**(2), E55 (2025).

[Published article](https://doi.org/10.1017/S0022377825000091) · [arXiv:2410.03838v1](https://arxiv.org/abs/2410.03838v1)

Relevant locations: published Sections 2.2 and 2.10; preprint Section 2.8. The published scaling discussion and the preprint's more explicit amplitude-estimation discussion should not be silently conflated.

## baer2000

Roi Baer. **Accurate and efficient evolution of nonlinear Schrödinger equations.** *Physical Review A* **62**, 063810 (2000).

[Publisher](https://doi.org/10.1103/PhysRevA.62.063810) · [Author-hosted paper](https://openscholar.huji.ac.il/sites/default/files/roibaer/files/baer2000accurate.pdf)

Relevant location: Section II, especially equations (20)–(22), for iterative selfconsistent propagation on Chebyshev time nodes.

## tal-ezer2012

Hillel Tal-Ezer, Ronnie Kosloff, and Ido Schaefer. **New, Highly Accurate Propagator for the Linear and Nonlinear Schrödinger Equation.** *Journal of Scientific Computing* **53**, 211–221 (2012).

[Publisher](https://doi.org/10.1007/s10915-012-9583-x) · [Author-hosted paper](https://openscholar.huji.ac.il/sites/default/files/ronniekosloff/files/hillel.pdf)

Relevant locations: iterative treatment of time-dependent generators and Section 4's nonlinear extension.

## schaefer2017

Ido Schaefer, Hillel Tal-Ezer, and Ronnie Kosloff. **Semi-global approach for propagation of the time-dependent Schrödinger equation for time-dependent and nonlinear problems.** *Journal of Computational Physics* **343**, 368–413 (2017).

[Publisher](https://doi.org/10.1016/j.jcp.2017.04.017) · [arXiv:1611.06707v3](https://arxiv.org/abs/1611.06707v3)

Relevant locations: Sections 2.4 and 3; Section 3.3, equations (92)–(95), for few state-dependent coefficients; Appendix D for numerical error sources and their control.

## ko2023

Taehee Ko, Xiantao Li, and Chunhao Wang. **Implementation of the Density-functional Theory on Quantum Computers with Linear Scaling with respect to the Number of Atoms.** arXiv:2307.07067v1 (2023).

[Version used](https://arxiv.org/abs/2307.07067v1) · [Full text](https://arxiv.org/html/2307.07067v1)

Relevant locations: Section III.4; Theorems 16–17 and 21. This is prior work on noisy quantum selfconsistent iteration and its total Hamiltonian-query complexity under local convergence assumptions.

## brustle2025

Noah Brüstle and Nathan Wiebe. **Quantum and classical algorithms for nonlinear unitary dynamics.** *Quantum* **9**, 1741 (2025).

[Published article](https://doi.org/10.22331/q-2025-05-13-1741) · [arXiv:2407.07685v2](https://arxiv.org/abs/2407.07685v2)

Relevant locations: Theorem 2, Lemma 7, and Corollary 13. The comparison must retain the coefficient norms, sparsities, oracle access, and output-extraction cost.

## jennings2026

David Jennings, Kamil Korzekwa, Matteo Lostaglio, Andrew T. Sornborger, Yiğit Subaşı, and Guoming Wang. **Quantum algorithms for general nonlinear dynamics based on the Carleman embedding.** *Quantum* **10**, 2233 (2026).

[Published article](https://doi.org/10.22331/q-2026-10-08-2233) · [arXiv:2509.07155v3](https://arxiv.org/abs/2509.07155v3)

Relevant locations: Theorem 3.6; Section 4's conservation and oscillation conditions; Theorems 6.1–6.4; nonlinear Schrödinger complexity results. Version 3, dated 29 October 2026, was used.

## lloyd2020

Seth Lloyd, Giacomo De Palma, Can Gokler, Bobak Kiani, Zi-Wen Liu, Milad Marvian, Felix Tennie, and Tim Palmer. **Quantum algorithm for nonlinear differential equations.** arXiv:2011.06571v2 (2020).

[Version used](https://arxiv.org/abs/2011.06571v2) · [Full text](https://arxiv.org/html/2011.06571v2)

Relevant material: nonlinear Schrödinger evolution as a many-copy mean-field limit, including finite-copy and discretization considerations.

## liu2024

Jin-Peng Liu and Lin Lin. **Dense outputs from quantum simulations.** *Journal of Computational Physics* **514**, 113213 (2024).

[Published article](https://doi.org/10.1016/j.jcp.2024.113213) · [arXiv:2307.14441v2](https://arxiv.org/abs/2307.14441v2)

Relevant material: complexity of time-accumulated observable output for prescribed dynamics. It supplies output-cost precedent without closing the unknown scalar feedback studied here.

## bauer2016

Bela Bauer, Dave Wecker, Andrew J. Millis, Matthew B. Hastings, and Matthias Troyer. **Hybrid Quantum-Classical Approach to Correlated Materials.** *Physical Review X* **6**, 031045 (2016).

[Published article](https://doi.org/10.1103/PhysRevX.6.031045)

Relevant material: quantum impurity solvers used within classical correlated-material calculations and selfconsistency.

## kreula2016

J. M. Kreula, S. R. Clark, and D. Jaksch. **Non-linear quantum-classical scheme to simulate non-equilibrium strongly correlated fermionic many-body dynamics.** *Scientific Reports* **6**, 32940 (2016).

[Published article](https://doi.org/10.1038/srep32940) · [arXiv:1510.05703](https://arxiv.org/abs/1510.05703)

Relevant material: nonequilibrium dynamical mean-field theory with a digital quantum impurity solver and a classical selfconsistency loop.

## jiang2026

Jiaqing Jiang, Nathan Ju, Ojas Parekh, Chaithanya Rayudu, and Andrew Zhao. **Polynomial-time classical and quantum simulation of quantum impurity models.** arXiv:2610.02167v2 (2026).

[Version used](https://arxiv.org/abs/2610.02167v2)

Relevant locations: static classical algorithms and Section 7's dynamical complexity results, especially Theorem 7.10. The explicit input encoding, allowed impurity controls, initial state, and measured output must be checked for each reduction using this result.

## brassard2002

Gilles Brassard, Peter Høyer, Michele Mosca, and Alain Tapp. **Quantum Amplitude Amplification and Estimation.** In *Quantum Computation and Quantum Information*, edited by Samuel J. Lomonaco Jr., *Contemporary Mathematics* **305**, 53–74 (2002).

[Publisher](https://doi.org/10.1090/conm/305/05215) · [arXiv:quant-ph/0005055](https://arxiv.org/abs/quant-ph/0005055)

Relevant material: amplitude estimation with preparation and inverse-preparation access. In this project those operations are compiled circuits whose complete costs are charged.

## bravyi2002

Sergey Bravyi and Alexei Kitaev. **Fermionic quantum computation.** *Annals of Physics* **298**(1), 210–226 (2002).

[Publisher](https://doi.org/10.1006/aphy.2002.6254) · [arXiv:quant-ph/0003137v2](https://arxiv.org/abs/quant-ph/0003137v2)

Relevant material: universal fermionic gates and encodings. The hardness page supplies its own dual-rail routing, finite-control, initial-state, and local-readout construction.

## dawson2006

Christopher M. Dawson and Michael A. Nielsen. **The Solovay–Kitaev algorithm.** *Quantum Information and Computation* **6**(1), 81–95 (2006).

[Publisher](https://www.rintonpress.com/journals/doi/QIC6.1-6.html) · [arXiv:quant-ph/0505030v2](https://arxiv.org/abs/quant-ph/0505030v2)

Relevant material: a constructive compiler for a fixed finite universal gate set, with logarithmic-power precision overhead. The conservative complete-cost theorem uses this route instead of assuming exact arbitrary rotations.

## terhal2002

Barbara M. Terhal and David P. DiVincenzo. **Classical simulation of noninteracting-fermion quantum circuits.** *Physical Review A* **65**, 032325 (2002).

[Publisher](https://doi.org/10.1103/PhysRevA.65.032325) · [arXiv:quant-ph/0108010v2](https://arxiv.org/abs/quant-ph/0108010v2)

Relevant locations: Sections III–V, for Gaussian transformations and Wick/Pfaffian evaluation. These are inherited primitives in the classical comparator.

## werner2009

Philipp Werner, Takashi Oka, and Andrew J. Millis. **Diagrammatic Monte Carlo simulation of nonequilibrium systems.** *Physical Review B* **79**, 035320 (2009).

[Publisher](https://doi.org/10.1103/PhysRevB.79.035320) · [arXiv:0810.2345v2](https://arxiv.org/abs/0810.2345v2)

Relevant material: real-time impurity expansions on forward and backward branches. The independent Poisson-word estimator and the conservative finite-cost bound in this project are derived explicitly.

## cohen2015

Guy Cohen, Emanuel Gull, David R. Reichman, and Andrew J. Millis. **Taming the dynamical sign problem in real-time evolution of quantum many-body problems.** *Physical Review Letters* **115**, 266802 (2015).

[Publisher](https://doi.org/10.1103/PhysRevLett.115.266802) · [arXiv:1510.03534v1](https://arxiv.org/abs/1510.03534v1)

Relevant material: inchworm reuse improves real-time impurity calculations in studied regimes. It is a reason to treat this project's exponential-in-action classical upper bound as one comparator rather than an optimality result.

## kieferova2019

Mária Kieferová, Artur Scherer, and Dominic W. Berry. **Simulating the dynamics of time-dependent Hamiltonians with a truncated Dyson series.** *Physical Review A* **99**, 042314 (2019).

[Publisher](https://doi.org/10.1103/PhysRevA.99.042314) · [arXiv:1805.00582](https://arxiv.org/abs/1805.00582)

Relevant location: Section II, including equations (2)–(3), for time-dependent simulation queries and elementary-gate overhead. The field-evaluation and sparse-matrix oracles are explicitly implemented in the project instead of treated as free.

## trefethen2019

Lloyd N. Trefethen. **Approximation Theory and Approximation Practice, Extended Edition.** SIAM (2019).

[Publisher](https://doi.org/10.1137/1.9781611975949) · [Author's book page](https://people.maths.ox.ac.uk/trefethen/ATAP/) · [Publisher's contents](https://epubs.siam.org/doi/pdf/10.1137/1.9781611975949.fm)

Relevant chapters: 2–5 for polynomial interpolation and representations, 8 for analytic approximation, 15 for interpolation stability, and 21 for differential-equation applications.

## lin2022

Lin Lin. **Lecture Notes on Quantum Algorithms for Scientific Computation.** arXiv:2201.08309v1 (2022).

[Version used](https://arxiv.org/abs/2201.08309v1) · [Notes](https://arxiv.org/pdf/2201.08309v1)

Relevant route: Sections 1.2 and 1.4–1.8; Section 1.10; Sections 2.3 and 4.2; Chapters 5–7. These cover states, measurement, perturbation bounds, reversible arithmetic, resource accounting, estimation, and simulation.

## nielsen2010

Michael A. Nielsen and Isaac L. Chuang. **Quantum Computation and Quantum Information, 10th Anniversary Edition.** Cambridge University Press (2010). ISBN 9781107002173.

[Publisher's book page](https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE) · [Publisher's front matter and contents](https://assets.cambridge.org/97811070/02173/frontmatter/9781107002173_frontmatter.pdf)

Relevant route: Sections 2.4–2.5, 3.2, 4.3–4.7, 5.2, 6.3, and 9.2 for the quantum-information and complexity foundations.
