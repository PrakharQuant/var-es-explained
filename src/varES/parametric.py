"""
Parametric (normal) VaR and Expected Shortfall.

Teaching implementation only — real markets have fat tails.
"""

import numpy as np
from scipy.stats import norm


def parametric_var(losses: np.ndarray, confidence: float = 0.99) -> float:
    """
    Parametric VaR assuming normal distribution of losses.

    Parameters
    ----------
    losses : array of daily losses (positive = loss)
    confidence : e.g. 0.99

    Returns
    -------
    VaR (positive)
    """
    mu = np.mean(losses)
    sigma = np.std(losses, ddof=1)
    z = norm.ppf(confidence)
    return float(mu + z * sigma)


def parametric_es(losses: np.ndarray, confidence: float = 0.975) -> float:
    """
    Parametric Expected Shortfall under normality.

    ES = μ + σ * φ(z) / (1-α)   where z = Φ^{-1}(α), α = confidence
    """
    mu = np.mean(losses)
    sigma = np.std(losses, ddof=1)
    z = norm.ppf(confidence)
    phi = norm.pdf(z)
    es = mu + sigma * phi / (1 - confidence)
    return float(es)
