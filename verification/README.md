# Reproducing the finite checks

This directory contains two checks and an optional figure generator. They establish different kinds of evidence:

| Program | Method | What it checks |
|---|---|---|
| [check_active_probe.py](check_active_probe.py) | Exact rational arithmetic and Taylor remainder bounds; Python standard library only | The sign and active-feedback margins in the terminal-probe corollary |
| [check_spectral_feedback.py](check_spectral_feedback.py) | Small classical state vectors, DOP853 integration, and deterministic bounded nodal errors | Four representative cases of the panelwise interpolation and replay construction |
| [plot_probe.py](plot_probe.py) | Direct evaluation of two closed-form functions | An explanatory figure of the analytically solvable probe |

None of these programs executes quantum circuits or amplitude estimation. The [scientific verification account](../science/verification.md) explains the examples and their limits. The [reconstruction proof](../science/spectral-reconstruction.md), [complete resource theorem](../science/complete-cost.md), and [hardness argument](../science/hardness.md) establish the separate analytical claims.

## Environment

Run the commands below from the repository root. The current reproduction environment uses Python 3.12.14. [requirements.txt](requirements.txt) pins the direct numerical and plotting dependencies:

| Dependency | Version | Use |
|---|---:|---|
| NumPy | 2.3.5 | State vectors, interpolation data, and analytical plot samples |
| SciPy | 1.17.0 | DOP853 integration and discrete cosine transforms |
| Matplotlib | 3.10.8 | Optional analytical-probe figure |

The [recorded spectral results](../results/spectral_feedback_results.json) report the NumPy and SciPy versions actually used. Each rerun records its own installed versions. The rational certificate needs none of these third-party dependencies.

For an isolated environment on Linux or macOS:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r verification/requirements.txt
```

On Windows, use the corresponding virtual-environment interpreter at `.venv\Scripts\python.exe` in place of `.venv/bin/python`. Dependency pins support reproduction, but floating-point library and platform differences can change the final digits of the numerical diagnostics.

## 1. Exact active-probe certificate

This check can run directly with Python, without installing the numerical packages:

```bash
python3 verification/check_active_probe.py
```

It writes [results/active_probe_certificate.json](../results/active_probe_certificate.json). Expected summary:

```text
sign_margin: certified lower bound 0.630306765206872 > 5/8
active_probe_effect: certified lower bound 0.086711044268815 > 2/25
```

The final output line gives the certificate's absolute path in the current checkout.

All calculations use exact integer and rational arithmetic. A positive exponential Taylor series and a geometric remainder bound enclose the stability factor. An analogous even-power series encloses the hyperbolic cosine, whose reciprocal encloses the hyperbolic secant. Alternating-series bounds enclose the cosine. The JSON file retains rational interval endpoints and outward-rounded decimal summaries, so the strict inequalities are not inferred from rounded decimal output.

The certificate checks the constant arithmetic assuming the analytical solution and trace-stability inequality in the hardness proof. It does not simulate the hard family, verify a universal-circuit compiler, prove BQP hardness, or measure a physical feedback effect.

## 2. Spectral reconstruction diagnostics

After installing the pinned dependencies, run:

```bash
.venv/bin/python verification/check_spectral_feedback.py
```

The program prints one JSON summary for each case and writes [results/spectral_feedback_results.json](../results/spectral_feedback_results.json). A successful run reaches the final save message with all four case statuses equal to `passed`.

The recorded cases are:

| Case identifier | Nodal perturbation | Panels / degree / rounds | Recorded terminal mean error |
|---|---|---:|---:|
| `exact_sech` | `none` | 320 / 21 / 20 | About 1.55e-13 |
| `exact_sech` | `alternating` | 320 / 21 / 20 | About 4.51e-7 |
| `two_qubit_noncommuting` | `positive` | 149 / 17 / 15 | About 8.28e-6 |
| `two_qubit_noncommuting` | `endpoint` | 149 / 17 / 15 | About 7.66e-6 |

The first model has an exact hyperbolic-secant solution; the second has noncommuting two-qubit terms. Perturbations are deterministic and bounded before clipping, so no random seed is needed. The script records its actual parameter choices, error budgets, sampled maxima, trace-norm errors, and replay comparisons.

The check uses relative integration tolerance 2e-12 and absolute tolerance 2e-14. It samples proxy norms and local errors on a finite real grid, and excludes contraction ratios with very small denominators. Its assertions include explicit floating-point cushions. The recorded results are representative diagnostics, not interval certificates for every trajectory.

Cached panel-start states accelerate this small classical emulation. Selected interior times are also reconstructed by replaying the entire stored prefix from the original initial state, checking that the cached and replayed constructions agree. Both use the same numerical integrator, so this is a consistency check rather than an independent integration-error certificate.

Dense classical output supplies multiple nodal values from one ODE solve. The quantum resource theorem receives no such saving: it charges a separate acquisition, original-state preparation, and complete prefix replay for every requested mean. The code also does not emulate finite-gate synthesis, amplitude-estimation sampling, or a separately injected coefficient-rounding budget.

## 3. Optional analytical-probe figure

The figure is generated directly from `sech(u)` and `cos(u)` on a grid of 500 points, without an ODE solve:

```bash
.venv/bin/python verification/plot_probe.py
```

This writes [assets/feedback-probe.svg](../assets/feedback-probe.svg). To also generate a PNG preview:

```bash
.venv/bin/python verification/plot_probe.py --preview
```

The optional second output is `assets/feedback-probe-preview.png`. At dimensionless time 2, the two plotted means are approximately 0.26580223 and -0.41614684, giving the figure's rounded difference of 0.682.

“Analytical” describes the source formulas; their plotted samples are evaluated in floating-point arithmetic. Font rendering and SVG identifiers can vary between environments, so the figure is not a byte-for-byte reproducibility certificate. The probe is itself analytically tractable and supplies no evidence of computational hardness or hardware advantage.

## Generated files and interpretation

Each command replaces its own named output with the newly generated result. No network service, quantum backend, or external data is needed after the dependencies are installed.

Use the exact certificate to assess its two strict constant inequalities. Use the floating-point cases to assess the implemented interpolation, state evolution, and prefix bookkeeping on the stated small examples. Use the scientific proofs to assess the dimension-independent reconstruction theorem, asymptotic task cost, and conditional complexity separation.

The separate [hosted mathematics check](hosted_math/README.md) compares the formulas with their actual GitHub rendering at wide and narrow widths. Its screenshots support visual review; the display check does not establish the scientific claims.
