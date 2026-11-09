"""
Simple Monte Carlo VaR / ES using Student-t shocks (matches the data generator).

Fixed seed for reproducibility in teaching examples.
"""

import numpy as np


def monte_carlo_var(
    losses: np.ndarray,
    confidence: float = 0.99,
    n_sims: int = 10_000,
    df: int = 5,
    seed: int = 42,
) -> float:
    """
    Monte Carlo VaR by simulating Student-t returns scaled to historical vol.
    """
    rng = np.random.default_rng(seed)
    mu = np.mean(losses)
    sigma = np.std(losses, ddof=1)
    # Generate simulated losses
    t_draws = rng.standard_t(df, size=n_sims)
    t_draws = t_draws * (sigma / np.std(t_draws))
    sim_losses = mu + t_draws
    return float(np.quantile(sim_losses, confidence))


def monte_carlo_es(
    losses: np.ndarray,
    confidence: float = 0.975,
    n_sims: int = 10_000,
    df: int = 5,
    seed: int = 42,
) -> float:
    """
    Monte Carlo Expected Shortfall (average of simulated losses beyond the VaR).
    """
    rng = np.random.default_rng(seed)
    mu = np.mean(losses)
    sigma = np.std(losses, ddof=1)
    t_draws = rng.standard_t(df, size=n_sims)
    t_draws = t_draws * (sigma / np.std(t_draws))
    sim_losses = mu + t_draws
    var = np.quantile(sim_losses, confidence)
    tail = sim_losses[sim_losses >= var]
    return float(np.mean(tail)) if len(tail) else float(var)
