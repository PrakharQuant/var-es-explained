"""
varES — Educational library for Value-at-Risk and Expected Shortfall.

All calculations are for teaching purposes on synthetic data.
Not for production risk systems.
"""

from .historical import historical_var, historical_es
from .parametric import parametric_var, parametric_es
from .monte_carlo import monte_carlo_var, monte_carlo_es
from .backtest import count_exceptions, traffic_light
from .frtb_liquidity import liquidity_horizon_scaling, frtb_es_capital

__version__ = "0.1.0"
__all__ = [
    "historical_var",
    "historical_es",
    "parametric_var",
    "parametric_es",
    "monte_carlo_var",
    "monte_carlo_es",
    "count_exceptions",
    "traffic_light",
    "liquidity_horizon_scaling",
    "frtb_es_capital",
]
