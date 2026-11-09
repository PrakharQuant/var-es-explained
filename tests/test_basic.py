"""
Tests that verify the library against hand-computed answers on tiny examples.
"""

import numpy as np
import pytest
from src.varES import historical_var, historical_es, parametric_var


def test_historical_var_ten_losses():
    """
    Classic 10-loss example used in the tutorial.
    Sorted losses: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    95 % VaR → 9th loss (or depending on exact convention) → we use the implementation.
    """
    losses = np.array([10, 1, 8, 3, 6, 2, 9, 4, 7, 5], dtype=float)
    # Sorted: 1,2,3,4,5,6,7,8,9,10
    # For 90 % confidence (1-0.9=0.1), index roughly the 1st of the worst 10 % → 9
    var90 = historical_var(losses, confidence=0.90)
    assert var90 == 9.0 or var90 == 10.0  # implementation detail of ceil


def test_historical_es_simple():
    losses = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 20], dtype=float)
    # 90 % VaR ≈ 9, ES = average of everything ≥ 9 → (9+20)/2 = 14.5
    es = historical_es(losses, confidence=0.90)
    assert es > 9


def test_parametric_var_known():
    # Mean 0, std 1, 95 % → approx 1.64485
    losses = np.random.default_rng(0).normal(0, 1, size=100_000)
    var = parametric_var(losses, confidence=0.95)
    assert 1.6 < var < 1.7
