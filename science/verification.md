# Finite checks of the feedback reconstruction

The numerical checks test the local collocation map, deterministic nodal errors, and consistency of replaying a learned prefix. They use small classical state vectors. They do not execute a quantum circuit, test amplitude estimation, estimate a hardware crossover, or establish an asymptotic complexity result.

The reproducible script is [check_spectral_feedback.py](../verification/check_spectral_feedback.py), and its recorded output is [spectral_feedback_results.json](../results/spectral_feedback_results.json). The complete analytic and resource arguments are in [Spectral reconstruction](spectral-reconstruction.md) and [Complete cost](complete-cost.md).

A separate exact-rational certificate for the active-probe constants appears in Section 6. It certifies the numerical margins in the hardness construction, not the circuit reduction or dynamics.

## 1. Numerical method and error patterns

Each prescribed-field or nonlinear Schrödinger equation is integrated with SciPy's DOP853 implementation, using relative tolerance $`2\times10^{-12}`$ and absolute tolerance $`2\times10^{-14}`$. The recorded run used NumPy 2.3.5 and SciPy 1.17.0. The code records its actual library versions whenever it is rerun.

The panel lengths, Chebyshev degrees, number of fixed-point rounds, and nodal budgets follow the conservative choices of the analytic theorem with requested final tolerance $`\epsilon=0.1`$. A direct cosine transform constructs the interpolants. The numerical implementation uses floating-point coefficients; it does not emulate a finite-gate compiler or separately inject the coefficient-map rounding budget $`\beta`$. Those errors are bounded analytically in the complete-cost theorem.

The recorded run uses the certified bound $`L_q=2+(2/\pi)\log(q+1)`$, with a natural logarithm. This is a valid choice in the theorem, which permits any certified Lebesgue upper bound of logarithmic order. A more conservative default such as $`2+\log(q+1)`$ or an upward rational/integer bound can change the chosen iteration counts or widths without invalidating these recorded parameter choices.

Four representative cases use deterministic perturbations of the scalar node values before clipping to $`[-1,1]`$:

- Zero nodal error.
- Alternating errors of magnitude $`\delta`$, with sign changing across node index, iteration, and panel.
- Persistent positive error $`+\delta`$.
- Opposite signs across the panel's midpoint, with all signs reversed at the next iteration.

These patterns probe persistent bias and changing interpolation errors without relying on a favorable sampled random realization.

## 2. Models

### Exact hyperbolic-secant solution

The first model has
```math
H(t)=X+2z(t)Z,\qquad
z(t)=\langle Z\rangle_t,\qquad
|\psi(0)\rangle=|0\rangle,\qquad T=1.
```
Its exact Bloch coordinates are
```math
x(t)=\tanh^2(2t),\qquad
y(t)=-\mathrm{sech}(2t)\tanh(2t),\qquad
z(t)=\mathrm{sech}(2t).
```
They satisfy the Bloch equations and the conserved relation $`x+z^2=1`$. This checks the nonlinear reference solver against an analytic solution, rather than comparing two unconstrained numerical trajectories.

The conservative settings use 320 panels, degree 21, and 20 collocation rounds per panel. The nominal nodal count is 140,800; the scalar error budget is approximately $`4.51\times10^{-7}`$. The nonlinear reference agrees with the analytic $`z(t)`$ on the comparison grid to approximately $`8.92\times10^{-12}`$.

### Two-qubit noncommuting Hamiltonian

The second model uses
```math
\begin{split}
B={}&0.9X\otimes I+0.7Z\otimes Z+0.5I\otimes X\\
   &+0.4Y\otimes X+0.3I\otimes Z,
\end{split}
```
with $`A=Z\otimes I`$, $`\lambda=1.5`$, $`T=0.4`$, and initial state $`|00\rangle`$. The supplied base-norm bound is $`2.8`$, compared with an actual spectral norm approximately $`1.76734`$.

The settings use 149 panels, degree 17, and 15 rounds, giving 40,230 nominal nodal evaluations. The scalar error budget is approximately $`7.66\times10^{-6}`$. This example has noncommuting couplings and a nontrivial reduced-state evolution; no closed-form solution is used.

## 3. Recorded results

| Model and perturbation | Panels / degree / rounds | Largest observed collocation ratio | Analytic contraction upper bound | Terminal mean error | Terminal trace-norm state error |
|---|---:|---:|---:|---:|---:|
| Exact sech, zero error | 320 / 21 / 20 | $`3.63\times10^{-5}`$ or less | 0.04960 | $`1.56\times10^{-13}`$ or less | $`4.31\times10^{-13}`$ or less |
| Exact sech, alternating error | 320 / 21 / 20 | $`3.63\times10^{-5}`$ or less | 0.04960 | $`4.51\times10^{-7}`$ or less | $`3.51\times10^{-11}`$ or less |
| Two qubits, positive error | 149 / 17 / 15 | $`9.95\times10^{-6}`$ or less | 0.03093 | $`8.29\times10^{-6}`$ or less | $`3.29\times10^{-6}`$ or less |
| Two qubits, changing endpoint signs | 149 / 17 / 15 | $`9.95\times10^{-6}`$ or less | 0.03093 | $`7.66\times10^{-6}`$ or less | $`9.62\times10^{-9}`$ or less |

The stated terminal mean bound is $`0.00625`$ in every case; the associated trace-norm bounds are approximately $`0.00614`$ and $`0.00437`$ for the first and second models. All recorded errors are below these conservative budgets.

The largest observed polynomial proxy magnitude is approximately $`1.000001582`$. This is slightly above $`1`$, as an interpolant of clipped nodal values can be. It remains safely below the Lebesgue bound used in the proof. Treating every interpolating proxy as automatically confined to $`[-1,1]`$ would be an incorrect implementation assumption.

The script checks the supplied Hamiltonian norm bound, certified panel contraction threshold, nodal error budget, real proxy and coefficient bounds, local field error, final state and mean error, state-norm drift, and consistency of replaying stored prefixes. The recorded cases passed these checks.

## 4. Replay semantics

For numerical efficiency, this small classical emulation caches the exact numerical state at each panel's start. The implemented quantum algorithm cannot obtain such intermediate states for free: every nodal estimate starts from the original known state and replays the whole stored prefix.

At four representative interior times in each numerical case, the script therefore also reconstructs the complete prefix from the original initial state and compares it with the cached-panel construction. Both paths use the same integration method and the same stored coefficients. Their recorded difference is zero at floating-point resolution, confirming consistent concatenation and node timing in this implementation. This is not an independent integrator accuracy certificate.

The nominal nodal counts above describe the algorithm's scalar acquisitions, not the number of ODE solves needed by this classical emulation. Dense numerical output supplies many node values in one solve, which is a convenience of the small classical test and is not credited to the quantum resource theorem.

## 5. Reproduction and limits

From the repository root, run:

    python verification/check_spectral_feedback.py

The script requires Python, NumPy, and SciPy. It prints each case's summary and writes the JSON output under the repository's results directory. The stored file contains every numerical parameter, the analytic budgets, maximum observed errors, library versions, and pass status.

Interpolation norms, contraction ratios, and local errors are sampled on a 257-point real grid. Ratios whose denominators are below $`10^{-8}`$ are excluded to avoid dividing integration noise. The exact-sech comparison uses 1,001 points. Assertions include small explicit floating-point cushions; these spectral simulations are not interval certificates.

The finite checks support implementation consistency in representative smooth cases. Dimension-independent analyticity, contraction under every admissible bounded nodal perturbation, full prefix-error accumulation, finite-bit compilation, and asymptotic gate complexity are mathematical claims proved separately. The cases do not test classical hardness, demonstrate typical-instance difficulty, or establish practical speedup.

## 6. Exact certificate for the active-probe margins

[check_active_probe.py](../verification/check_active_probe.py) uses only the Python standard library, with exact rational arithmetic throughout. Run it from the repository root:

    python verification/check_active_probe.py

The recorded certificate is [active_probe_certificate.json](../results/active_probe_certificate.json). It retains exact rational interval endpoints and outward-rounded decimal summaries.

The constants are
```math
t_c=\frac1{1024},\qquad
\tau_p=\frac{1023}{1024},\qquad
a_0=2^{-24},\qquad
\sqrt{a_0}=2^{-12},\qquad
\zeta=2^{-16},\qquad
d_0=2t_c+2\sqrt{a_0}+2\zeta=\frac{81}{32768}.
```
The script encloses $`e^{2\tau_p}`$ by a positive Taylor sum through degree 32 and a geometric bound on its remaining tail. It encloses $`\cosh(\tau_p)`$ using the corresponding positive even-power series, then inverts that positive interval to enclose $`\mathrm{sech}(\tau_p)`$. For $`\cos(\tau_p)`$, the alternating series and its first omitted term give upper and lower rational bounds. No floating-point exponential, trigonometric evaluation, or square root is used.

If $`E_+`$, $`S_-`$, and $`C_+`$ denote the resulting upper bound on $`e^{2\tau_p}`$, lower bound on $`\mathrm{sech}(\tau_p)`$, and upper bound on $`\cos(\tau_p)`$, the exact rational comparisons certify
```math
S_--E_+d_0>\frac58,
\qquad
S_--C_+-(E_++1)d_0>\frac{2}{25}=0.08.
```
Their outward-rounded lower bounds are approximately $`0.630306765206872`$ and $`0.086711044268815`$, respectively. The nonlinear terminal-error upper bound is below $`0.018229544466519`$.

This check validates the constant arithmetic used in [the direct active-probe corollary](hardness.md#6-a-direct-source-free-hardness-corollary-with-an-active-probe). It is not a simulation of a hard instance, a test of the universal-circuit compiler, a proof of the trace-stability inequality, or a measurement of a quantum device. Those mathematical premises remain explicit parts of the hardness proof.
