# Learning route

This route explains how an unknown scalar mean field can be reconstructed while charging every quantum operation used to learn it. It connects the complete algorithm to the classical regimes where the same task is already tractable and to the restricted growing families where a classical solver would have an unexpected complexity consequence.

The selected educational anchor is **Lin Lin, *Lecture Notes on Quantum Algorithms for Scientific Computation*, arXiv:2201.08309v1 (2022)**. Use this fixed version: [record](https://arxiv.org/abs/2201.08309v1), [full notes](https://arxiv.org/pdf/2201.08309v1). The arXiv submission is dated 20 January 2022; the PDF title page is dated 21 January. This is the single educational anchor for the project.

The [bridge](BRIDGE.md) explains the project-specific steps. The [30-milestone map](MILESTONES.md) records the common understanding targets and their dependencies. For a direct technical route, use the [scientific reading guide](../science/README.md).

## The project defines the route

The map has two phases, each moving from local objects to the complete scientific account:

| Phase | Milestones | Scientific purpose |
|---|---|---|
| Background and preliminaries | M01–M14 | Connect states, local charge, fermionic structure, preparation, estimation, finite access, error propagation, and mean-field closure into one fully specified task. |
| Narrative and contribution | M15–M30 | Assemble the reconstruction and its cost, challenge them with a classical algorithm, establish the qualified hard families, and interpret the combined result. |

The 14/16 allocation reflects the interfaces this project joins. Its quantum state, finite circuit, nonlinear field, and classical comparison all need a common language before the proof becomes meaningful. The second phase then integrates three distinct arguments: a quantum upper bound, a classical upper bound in an easy regime, and a conditional hardness result. The map is not a copy of the notes' contents and does not claim to cover every specialist detail.

## Selected sections from Lin's notes

The section names and printed page numbers below refer to the selected version. They provide foundations when the corresponding project idea is encountered; reading the entire notes is unnecessary.

| Lin section | Exact section name | Page | Project use |
|---|---|---:|---|
| 1.1 | Postulates of quantum mechanics | 7 | States, evolution, and measurement outcomes |
| 1.2 | Density operator | 11 | A local mean of a possibly correlated many-body state |
| 1.3 | Quantum circuit | 13 | Finite preparation and evolution procedures |
| 1.4 | Copy operation and no-cloning theorem | 15 | Why a measured intermediate state is not a reusable free resource |
| 1.5 | Measurement | 16 | A classical estimate and its sampling error |
| 1.6 | Linear error growth and Duhamel's principle | 19 | Comparing propagators and accumulating local errors |
| 1.7 | Universal gate sets and reversible computation | 20 | Explicit controlled circuits and inverse operations |
| 1.8 | Fixed point number representation and classical arithmetic operations | 23 | Finite coefficients, times, and arithmetic |
| 1.10 | Complexity of quantum algorithms | 24 | Resource counts and their input assumptions |
| 2.3 | Amplitude amplification | 33 | The reflection construction behind coherent estimation |
| 3.1 | Hadamard test | 39 | General expectation-readout context; the main task uses a direct local bit readout |
| 3.4 | Quantum phase estimation using quantum Fourier transform | 48 | The phase-estimation component of the chosen amplitude-estimation construction |
| 4.2 | Amplitude estimation | 57 | Estimating a marked probability using a preparation circuit and its inverse |
| 5.1 | Trotter splitting | 75 | A first connection between a Hamiltonian and an implementable evolution |
| 5.2 | Commutator type error bound | 76 | Structure and error in product approximations |
| 6.1 | Query model for matrix entries | 79 | What a matrix-access promise means |
| 6.2 | Block encoding | 80 | Normalization and the cost of representing a matrix within a unitary |
| 6.3 | Block encoding of s-sparse matrices | 84 | How sparsity and access affect implementation |
| 7.3 | Linear combination of unitaries | 99 | A simulation ingredient used by more accurate methods |
| 7.5 | Quantum eigenvalue transformation | 105 | A contrast: polynomial approximation of a matrix function differs from interpolation of a time-dependent mean |
| 7.7 | Application: Time-independent Hamiltonian simulation | 114 | Accurate simulation and its dependence on precision |

For the fermionic notation, **Example 4.2, “Fermionic system in second quantization,” on page 53** gives a useful optional connection to Pauli operators. Its surrounding ground-state application is different from this project's driven scalar-output task.

## Follow the bridge alongside the map

| Project thread | Map range | Bridge entry | Canonical scientific account |
|---|---|---|---|
| Define the state, measured charge, and access contract | M01–M14 | [Task and notation](BRIDGE.md#1-a-charge-measurement-with-an-unknown-field) | [Model](../science/model.md) |
| Build and price the acquired field | M15–M21 | [Scalar reconstruction](BRIDGE.md#4-reconstructing-one-scalar-curve), [physical prefix](BRIDGE.md#5-the-panel-start-state-is-a-complete-prefix), [cost](BRIDGE.md#6-from-a-response-circuit-to-the-full-cost) | [Reconstruction](../science/spectral-reconstruction.md), [complete cost](../science/complete-cost.md) |
| Identify the classical easy regimes | M22–M24 | [The two actions](BRIDGE.md#7-the-classical-boundary-uses-two-actions) | [Classical boundary](../science/classical-boundary.md) |
| Understand the qualified computational obstruction | M25–M28 | [Hardness and the active probe](BRIDGE.md#8-how-the-qualified-hardness-statements-fit) | [Hardness](../science/hardness.md), [exact example](../science/examples.md) |
| Integrate evidence, attribution, and the final conclusion | M29–M30 | [Complete conclusion](BRIDGE.md#9-reading-the-complete-conclusion) | [Prior work](../science/prior-work.md), [verification](../science/verification.md) |

The [complete two-mode example](BRIDGE.md#3-a-complete-two-mode-example) can be read near the beginning. It shows the preparation, mean, readout probability, and one field update without requiring the full many-body proof. Its exact analytic solution also demonstrates why a visible nonlinear effect is insufficient evidence of computational advantage.

## What this project supplies beyond the anchor

Lin's notes explain quantum algorithmic primitives and access models. The project supplies the additional mathematical and computational connections:

- A scalar expectation feeds back into its own Hamiltonian. The resulting nonlinear initial-value problem needs a new error argument around the prescribed-evolution primitives.
- A piecewise polynomial field is learned from noisy responses. Its local contraction and global stability are proved with physical operator and trace norms.
- Each response uses the original preparation and a complete replay of the recorded prefix. Finite arithmetic, time-dependent simulation, confidence amplification, and classical control are charged.
- Gaussian structure and bounded non-Gaussian action give explicit classical alternatives for the same output task.
- Interacting impurity controls yield qualified worst-case hardness statements, with their finite inputs, growing strengths, and reduction types stated explicitly.

These additions are explained in the bridge and proved in the science pages. Research-level dependencies, including time-dependent simulation, approximation bounds, Gaussian methods, and prior nonlinear algorithms, remain in the [bibliography](../references/REFERENCES.md). They support attribution and verification; they do not expand the selected educational anchor into a second prerequisite reading list.

## Keep the three conclusions distinct

The quantum result is a fully paid upper bound with inverse-linear precision dependence up to logarithms at fixed parameters. The classical result is an efficient regime under explicit action and input bounds. The hard-family result is a conditional growing-input obstruction under programmable control assumptions. Neither the small numerical examples nor the inverse-error exponent establishes a practical device advantage or a universal classical precision lower bound.

Continue with the [bridge](BRIDGE.md), the [milestone map](MILESTONES.md), or the [canonical science](../science/README.md).
