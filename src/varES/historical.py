"""
Historical simulation VaR and Expected Shortfall.

Teaching implementation: sort the losses and pick the quantile.
"""

from typing import Tuple
import numpy as np


def historical_var(losses: np.ndarray, confidence: float = 0.99) -> float:
    """
    Historical VaR at the given confidence level.

    Parameters
    ----------
    losses : array of daily P&L (negative = loss). We work with losses so higher = worse.
    confidence : e.g. 0.99 for 99 % VaR

    Returns
    -------
    VaR as a positive number (the loss threshold)
    """
    if not 0 < confidence < 1:
        raise ValueError("confidence must be between 0 and 1")
    losses = np.asarray(losses, dtype=float)
    # We treat the series as losses (flip sign if the user passed P&L)
    # Convention in this library: positive number = loss
    sorted_losses = np.sort(losses)  # ascending: smallest loss first
    # We want the upper quantile (worst losses)
    # Position from the right
    n = len(sorted_losses)
    k = int(np.ceil((1 - confidence) * n))
    idx = n - k
    idx = max(0, min(idx, n - 1))
    return float(sorted_losses[idx])


def historical_es(losses: np.ndarray, confidence: float = 0.975) -> float:
    """
    Historical Expected Shortfall (average of losses beyond VaR).

    Parameters
    ----------
    losses : array of daily losses (positive = loss)
    confidence : e.g. 0.975 for 97.5 % ES (FRTB)

    Returns
    -------
    ES as a positive number
    """
    var = historical_var(losses, confidence)
    tail = losses[losses >= var]
    if len(tail) == 0:
        return var
    return float(np.mean(tail))
