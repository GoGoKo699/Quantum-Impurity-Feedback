#!/usr/bin/env python3
"""Certify the active-probe constants using exact rational arithmetic.

This checks only the quantitative inequalities in the active-probe corollary.
It does not simulate dynamics or verify the circuit/hardness reduction.
All transcendental bounds come from Taylor sums with proved remainder bounds.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


@dataclass(frozen=True)
class Interval:
    lower: Fraction
    upper: Fraction


def exp_interval(x: Fraction, order: int = 32) -> Interval:
    """Positive Taylor series, with its tail bounded by a geometric series."""
    if x < 0 or order < 0:
        raise ValueError("Require x >= 0 and order >= 0.")
    term = Fraction(1)
    total = term
    for k in range(1, order + 1):
        term *= x / k
        total += term
    first_omitted = term * x / (order + 1)
    ratio_bound = x / (order + 2)
    if ratio_bound >= 1:
        raise ValueError("Taylor order is too small for this tail bound.")
    return Interval(total, total + first_omitted / (1 - ratio_bound))


def cosh_interval(x: Fraction, order: int = 16) -> Interval:
    """Positive even-power series, again using a geometric tail bound."""
    if x < 0 or order < 0:
        raise ValueError("Require x >= 0 and order >= 0.")
    term = Fraction(1)
    total = term
    for k in range(1, order + 1):
        term *= x * x / ((2 * k - 1) * (2 * k))
        total += term
    first_omitted = term * x * x / ((2 * order + 1) * (2 * order + 2))
    ratio_bound = x * x / ((2 * order + 3) * (2 * order + 4))
    if ratio_bound >= 1:
        raise ValueError("Taylor order is too small for this tail bound.")
    return Interval(total, total + first_omitted / (1 - ratio_bound))


def cos_interval(x: Fraction, order: int = 16) -> Interval:
    """Alternating-series bounds; even order is an upper partial sum."""
    if not 0 <= x <= 1 or order < 0 or order % 2:
        raise ValueError("Require 0 <= x <= 1 and a nonnegative even order.")
    term = Fraction(1)
    total = term
    for k in range(1, order + 1):
        term *= -x * x / ((2 * k - 1) * (2 * k))
        total += term
    first_omitted = term * (-x * x) / ((2 * order + 1) * (2 * order + 2))
    return Interval(total + first_omitted, total)


def decimal_bound(x: Fraction, *, upward: bool, places: int = 15) -> str:
    """Outward decimal rounding, using integer arithmetic rather than floats."""
    scale = 10 ** places
    numerator = x.numerator * scale
    scaled, remainder = divmod(numerator, x.denominator)
    if upward and remainder:
        scaled += 1
    sign = "-" if scaled < 0 else ""
    whole, fractional = divmod(abs(scaled), scale)
    return f"{sign}{whole}.{fractional:0{places}d}"


def encoded_interval(value: Interval) -> dict:
    if value.lower > value.upper:
        raise ArithmeticError("Invalid interval.")
    return {
        "lower_rational": str(value.lower),
        "upper_rational": str(value.upper),
        "lower_decimal_outward": decimal_bound(value.lower, upward=False),
        "upper_decimal_outward": decimal_bound(value.upper, upward=True),
    }


def main() -> None:
    tc = Fraction(1, 2 ** 10)
    probe_time = 1 - tc
    amplification_error = Fraction(1, 2 ** 24)
    sqrt_amplification_error = Fraction(1, 2 ** 12)
    compilation_error = Fraction(1, 2 ** 16)
    d0 = 2 * tc + 2 * sqrt_amplification_error + 2 * compilation_error
    if sqrt_amplification_error ** 2 != amplification_error:
        raise ArithmeticError("The amplification square root is not exact.")
    if d0 != Fraction(81, 32768):
        raise ArithmeticError("The initial trace-distance budget is incorrect.")

    exp_factor = exp_interval(2 * probe_time)
    cosh_factor = cosh_interval(probe_time)
    sech_factor = Interval(1 / cosh_factor.upper, 1 / cosh_factor.lower)
    cos_factor = cos_interval(probe_time)
    nonlinear_error_upper = exp_factor.upper * d0
    sign_margin_lower = sech_factor.lower - nonlinear_error_upper
    active_effect_lower = (
        sech_factor.lower - cos_factor.upper - (exp_factor.upper + 1) * d0
    )

    claims = {
        "sign_margin": (sign_margin_lower, Fraction(5, 8)),
        "active_probe_effect": (active_effect_lower, Fraction(2, 25)),
    }
    for name, (lower, threshold) in claims.items():
        if lower <= threshold:
            raise ArithmeticError(f"{name} is not certified above {threshold}.")

    certificate = {
        "scope": (
            "Exact-rational certificate of the active-probe numerical constants. "
            "No dynamics simulation, circuit execution, or hardness-proof check."
        ),
        "method": {
            "exp": "Taylor degree 32; positive tail bounded geometrically.",
            "cosh": "Even-power Taylor index 16; positive tail bounded geometrically.",
            "cos": "Alternating Taylor index 16 and first omitted term.",
            "arithmetic": "fractions.Fraction and integer outward decimal rounding.",
        },
        "constants": {
            "computation_time": str(tc),
            "probe_time": str(probe_time),
            "amplification_error": str(amplification_error),
            "sqrt_amplification_error": str(sqrt_amplification_error),
            "bare_compilation_operator_error": str(compilation_error),
            "probe_initial_trace_distance_bound": str(d0),
        },
        "intervals": {
            "exp_twice_probe_time": encoded_interval(exp_factor),
            "sech_probe_time": encoded_interval(sech_factor),
            "cos_probe_time": encoded_interval(cos_factor),
        },
        "nonlinear_terminal_error_upper": {
            "rational": str(nonlinear_error_upper),
            "decimal_outward": decimal_bound(nonlinear_error_upper, upward=True),
        },
        "claims": {
            name: {
                "lower_bound_rational": str(lower),
                "lower_bound_decimal_outward": decimal_bound(lower, upward=False),
                "strict_threshold": str(threshold),
                "proved_by_exact_rational_comparison": True,
            }
            for name, (lower, threshold) in claims.items()
        },
    }
    destination = Path(__file__).resolve().parents[1] / "results"
    destination.mkdir(exist_ok=True)
    output = destination / "active_probe_certificate.json"
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    for name, (lower, threshold) in claims.items():
        print(
            f"{name}: certified lower bound "
            f"{decimal_bound(lower, upward=False)} > {threshold}"
        )
    print(f"Saved {output}")


if __name__ == "__main__":
    main()
