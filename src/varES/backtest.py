"""
Backtesting utilities: exception counting and Basel traffic-light zones.
"""

from typing import Tuple
import numpy as np


def count_exceptions(actual_losses: np.ndarray, var_series: np.ndarray) -> int:
    """
    Count the number of days where actual loss exceeded the VaR forecast.

    Parameters
    ----------
    actual_losses : array of realized losses (positive = loss)
    var_series    : array of VaR forecasts for the same days (same length)

    Returns
    -------
    Number of exceptions (VaR breaches)
    """
    if len(actual_losses) != len(var_series):
        raise ValueError("actual_losses and var_series must have the same length")
    return int(np.sum(actual_losses > var_series))


def traffic_light(n_exceptions: int, n_days: int = 250, confidence: float = 0.99) -> str:
    """
    Basel traffic-light zones for 99 % VaR over a 250-day window.

    Green  : 0–4 exceptions
    Amber  : 5–9 exceptions
    Red    : ≥10 exceptions

    (Exact boundaries can vary slightly by jurisdiction; these are the classic Basel II numbers.)
    """
    if n_days != 250 or not np.isclose(confidence, 0.99):
        # Fallback message for non-standard windows
        expected = n_days * (1 - confidence)
        if n_exceptions <= expected * 2:
            return "green (informal)"
        elif n_exceptions <= expected * 4:
            return "amber (informal)"
        else:
            return "red (informal)"

    if n_exceptions <= 4:
        return "green"
    elif n_exceptions <= 9:
        return "amber"
    else:
        return "red"
