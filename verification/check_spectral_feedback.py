#!/usr/bin/env python3
"""Finite scientific checks for panelwise noisy spectral Hartree feedback.

This emulates scalar expectation values by small classical state-vector solves.
It does not simulate a quantum algorithm or validate a hardware crossover.
Cached panel-start states accelerate the numerical emulation; selected nodes
are independently regenerated from the original initial state by full replay.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import scipy
from numpy.polynomial.chebyshev import chebval
from scipy.fft import dct
from scipy.integrate import solve_ivp

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
ID = np.eye(2, dtype=complex)


def coeffs(values: np.ndarray) -> np.ndarray:
    q = len(values) - 1
    ans = dct(np.asarray(values, float), type=1) / q
    ans[0] /= 2
    ans[-1] /= 2
    return ans


def expect(psi: np.ndarray, obs: np.ndarray) -> np.ndarray:
    return np.real(np.sum(psi.conj() * (obs @ psi), axis=0))


def linear_panel(H, A, lam, p, psi0, h, stop=None):
    endpoint = h if stop is None else stop
    if endpoint == 0:
        return None

    def rhs(t, psi):
        return -1j * ((H + lam * chebval(2 * t / h - 1, p) * A) @ psi)

    sol = solve_ivp(rhs, (0.0, endpoint), psi0, method="DOP853",
                    rtol=2e-12, atol=2e-14, dense_output=True)
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol


def nonlinear_panel(H, A, lam, psi0, h):
    def rhs(t, psi):
        m = float(np.real(np.vdot(psi, A @ psi)))
        return -1j * ((H + lam * m * A) @ psi)

    sol = solve_ivp(rhs, (0.0, h), psi0, method="DOP853",
                    rtol=2e-12, atol=2e-14, dense_output=True)
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol


def trace_distance(psi, phi):
    rho = np.outer(psi, psi.conj())
    sig = np.outer(phi, phi.conj())
    return float(np.sum(np.abs(np.linalg.eigvalsh(rho - sig))))


def run_case(name, H, A, lam, horizon, norm_bound, noise_mode,
             epsilon=0.1):
    dim = H.shape[0]
    initial = np.zeros(dim, complex)
    initial[0] = 1.0
    kappa = lam * horizon
    eta = epsilon * math.exp(-2 * kappa) / 16
    q = max(1, math.ceil(math.log2(128 / eta)))
    # Deliberately generous certified upper bound, not a sampled Lebesgue value.
    leb_bound = 2 + 2 / math.pi * math.log(q + 1)
    h_cap = min(1 / (64 * (norm_bound + 2 * lam)),
                1 / (4 * lam * leb_bound))
    panels = math.ceil(horizon / h_cap)
    h = horizon / panels
    rounds = math.ceil(math.log2(16 * leb_bound / eta))
    delta = eta / (64 * leb_bound)
    theta = 2 * lam * h * leb_bound
    nodes = np.cos(np.pi * np.arange(q + 1) / q)
    node_t = (nodes + 1) * h / 2
    inspect_x = np.linspace(-1, 1, 257)
    inspect_t = (inspect_x + 1) * h / 2
    initial_density = np.outer(initial, initial.conj())
    ref = nonlinear_panel(H, A, lam, initial, horizon)

    saved = []
    starts = []
    psi_start = initial.copy()
    max_p = 0.0
    max_coef = 0.0
    max_nodal_error = 0.0
    max_contraction_ratio = 0.0
    contraction_pairs = 0
    max_local_mean_error = 0.0
    max_norm_error = 0.0
    max_round_residual = 0.0
    max_state_error = 0.0
    max_global_mean_error = 0.0
    observed_local_errors = []

    for panel in range(panels):
        starts.append(psi_start.copy())
        p = np.zeros(q + 1)
        prev_p = None
        prev_exact_image = None
        last_image = None
        for iteration in range(rounds):
            prop = linear_panel(H, A, lam, p, psi_start, h)
            actual = expect(prop.sol(node_t), A)
            exact_image = coeffs(actual)
            if prev_p is not None:
                denominator = np.max(np.abs(chebval(inspect_x, p - prev_p)))
                if denominator > 1e-8:
                    numerator = np.max(np.abs(chebval(
                        inspect_x, exact_image - prev_exact_image)))
                    max_contraction_ratio = max(max_contraction_ratio,
                                                float(numerator / denominator))
                    contraction_pairs += 1
            if noise_mode == "none":
                noise = np.zeros(q + 1)
            elif noise_mode == "alternating":
                noise = delta * (-1.0) ** (np.arange(q + 1) + iteration + panel)
            elif noise_mode == "positive":
                noise = np.full(q + 1, delta)
            elif noise_mode == "endpoint":
                # Opposite signs across the panel; flips at each iteration.
                noise = delta * np.where(nodes >= 0, 1.0, -1.0) * (-1) ** iteration
            else:
                raise ValueError(noise_mode)
            reported = np.clip(actual + noise, -1, 1)
            max_nodal_error = max(max_nodal_error,
                                  float(np.max(np.abs(reported - actual))))
            prev_p = p.copy()
            prev_exact_image = exact_image.copy()
            p = coeffs(reported)
            last_image = exact_image
            max_p = max(max_p, float(np.max(np.abs(chebval(inspect_x, p)))))
            max_coef = max(max_coef, float(np.max(np.abs(p))))
        assert last_image is not None
        max_round_residual = max(max_round_residual,
                                  float(np.max(np.abs(chebval(inspect_x,
                                                              p - last_image)))))
        # The comparison nonlinear solution starts from the actual approximate
        # prefix state; this is the state required by the analytical theorem.
        local_truth = nonlinear_panel(H, A, lam, psi_start, h)
        local_mean = expect(local_truth.sol(inspect_t), A)
        local_error = float(np.max(np.abs(chebval(inspect_x, p) - local_mean)))
        observed_local_errors.append(local_error)
        max_local_mean_error = max(max_local_mean_error, local_error)

        learned_prop = linear_panel(H, A, lam, p, psi_start, h)
        actual_grid = learned_prop.sol(inspect_t)
        exact_grid = ref.sol(panel * h + inspect_t)
        max_norm_error = max(max_norm_error,
                             float(np.max(np.abs(np.sum(abs(actual_grid)**2,
                                                        axis=0) - 1))))
        max_global_mean_error = max(max_global_mean_error,
            float(np.max(abs(chebval(inspect_x, p) - expect(exact_grid, A)))))
        psi_start = learned_prop.y[:, -1]
        max_state_error = max(max_state_error,
                              trace_distance(psi_start, ref.sol((panel + 1) * h)))
        saved.append(p.copy())

    terminal_mean = float(chebval(1.0, saved[-1]))
    true_terminal_mean = float(expect(ref.sol(horizon), A))
    state_error = trace_distance(psi_start, ref.sol(horizon))
    mean_error = abs(terminal_mean - true_terminal_mean)
    global_state_bound = eta * math.expm1(2 * kappa)
    global_mean_bound = eta * math.exp(2 * kappa)

    # Fresh prefix replays at selected interior-node times. This check does not
    # use cached starts for the independently regenerated state.
    replay_errors = []
    chosen = sorted(set([0, panels // 3, 2 * panels // 3, panels - 1]))
    for index in chosen:
        fresh = initial.copy()
        for k in range(index):
            fresh = linear_panel(H, A, lam, saved[k], fresh, h).y[:, -1]
        tau = 0.37 * h
        fresh = linear_panel(H, A, lam, saved[index], fresh, h, stop=tau).y[:, -1]
        cached = linear_panel(H, A, lam, saved[index], starts[index], h,
                              stop=tau).y[:, -1]
        replay_errors.append(trace_distance(fresh, cached))

    exact_sech_error = None
    if name == "exact_sech":
        points = np.linspace(0, horizon, 1001)
        exact_sech_error = float(np.max(np.abs(expect(ref.sol(points), A)
                                              - 1 / np.cosh(2 * points))))

    # Assertions allow a small absolute floating-point cushion; results retain
    # the raw values and are numerical diagnostics, not interval certificates.
    assert np.linalg.norm(H, 2) <= norm_bound * (1 + 1e-12)
    assert theta <= 0.5
    assert max_p <= leb_bound + 1e-10
    assert max_coef <= 2 + 1e-10
    assert max_nodal_error <= delta + 1e-10
    assert max_contraction_ratio <= theta + 2e-5
    assert max_local_mean_error <= eta + 1e-9
    assert state_error <= global_state_bound + 1e-8
    assert mean_error <= global_mean_bound + 1e-8
    assert max(replay_errors) < 1e-9
    if exact_sech_error is not None:
        assert exact_sech_error < 1e-9
    return {
        "case": name, "noise": noise_mode, "dimension": dim,
        "lambda": lam, "T": horizon, "kappa": kappa,
        "base_norm_bound": norm_bound, "base_norm_actual": float(np.linalg.norm(H, 2)),
        "epsilon_budget": epsilon, "eta_local": eta,
        "degree": q, "panels": panels, "rounds_per_panel": rounds,
        "nominal_nodal_evaluations": panels * rounds * (q + 1),
        "h": h, "h_cap": h_cap, "lebesgue_bound": leb_bound,
        "node_error_budget": delta, "maximum_nodal_error": max_nodal_error,
        "contraction_bound": theta, "observed_max_contraction_ratio": max_contraction_ratio,
        "contraction_pairs_tested": contraction_pairs,
        "maximum_proxy_real_absolute": max_p, "maximum_Chebyshev_coefficient": max_coef,
        "maximum_local_mean_error_on_grid": max_local_mean_error,
        "maximum_final_round_nodal_noise_polynomial": max_round_residual,
        "terminal_mean": terminal_mean, "reference_terminal_mean": true_terminal_mean,
        "terminal_mean_error": mean_error, "terminal_mean_bound": global_mean_bound,
        "terminal_trace_norm_error": state_error, "terminal_trace_norm_bound": global_state_bound,
        "maximum_prefix_trace_norm_error": max_state_error,
        "maximum_global_mean_curve_error_on_grid": max_global_mean_error,
        "maximum_state_norm_drift": max_norm_error,
        "fresh_prefix_replay_errors": replay_errors,
        "exact_sech_reference_error": exact_sech_error,
        "status": "passed",
    }


def main():
    H2 = (0.9 * np.kron(X, ID) + 0.7 * np.kron(Z, Z)
          + 0.5 * np.kron(ID, X) + 0.4 * np.kron(Y, X)
          + 0.3 * np.kron(ID, Z))
    A2 = np.kron(Z, ID)
    cases = [
        ("exact_sech", X, Z, 2.0, 1.0, 1.0, "none"),
        ("exact_sech", X, Z, 2.0, 1.0, 1.0, "alternating"),
        ("two_qubit_noncommuting", H2, A2, 1.5, 0.4, 2.8, "positive"),
        ("two_qubit_noncommuting", H2, A2, 1.5, 0.4, 2.8, "endpoint"),
    ]
    results = []
    for spec in cases:
        result = run_case(*spec)
        results.append(result)
        print(json.dumps({k: result[k] for k in ["case", "noise", "degree", "panels",
                         "observed_max_contraction_ratio", "contraction_bound",
                         "terminal_mean_error", "terminal_trace_norm_error", "status"]}),
              flush=True)
    artifact = {
        "numpy_version": np.__version__, "scipy_version": scipy.__version__,
        "method": "Classical DOP853 state-vector emulation of finite spectral feedback reconstruction",
        "scope": "Small-state numerical diagnostic; no quantum circuit execution, QAE test, interval certificate, asymptotic proof, or practical crossover",
        "cases": results,
    }
    RESULTS.mkdir(exist_ok=True)
    out = RESULTS / "spectral_feedback_results.json"
    out.write_text(json.dumps(artifact, indent=2) + "\n")
    print(f"Saved {out}", flush=True)


if __name__ == "__main__":
    main()
