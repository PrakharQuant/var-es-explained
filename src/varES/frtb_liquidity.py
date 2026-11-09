"""
FRTB liquidity-horizon scaling and simple capital helpers.

Educational implementation of the cascading formula from BCBS d457.
"""

from typing import Dict
import numpy as np


# Standard FRTB liquidity horizons (days)
LIQUIDITY_HORIZONS = [10, 20, 40, 60, 120]


def liquidity_horizon_scaling(
    es_10d: float,
    liquidity_horizon: int,
    base_horizon: int = 10,
) -> float:
    """
    Scale a 10-day ES to a longer liquidity horizon using the FRTB square-root rule
    with the cascading adjustment (simplified teaching version).

    The full cascading formula is more involved; this is the basic √(LH/10) scaling
    that appears in the standard approach and as a building block of the internal models approach.
    """
    if liquidity_horizon < base_horizon:
        raise ValueError("liquidity_horizon must be ≥ base_horizon")
    return es_10d * np.sqrt(liquidity_horizon / base_horizon)


def frtb_es_capital(
    es_by_horizon: Dict[int, float],
    multiplier: float = 1.5,
) -> float:
    """
    Aggregate ES across liquidity horizons into a capital number (simplified).

    In the real FRTB IMA the aggregation is more complex (constrained / unconstrained ES,
    NMRF, etc.). This function simply sums the horizon-scaled ES figures and applies
    a multiplier — useful for teaching the order of magnitude.
    """
    total = sum(es_by_horizon.values())
    return float(total * multiplier)
