"""
Generate synthetic daily returns for Bharat Demo Bank.

All numbers are fictional. Fixed random seed for full reproducibility.
Uses Student-t (df=5) for fat tails + one injected crisis period of large losses.
"""

import numpy as np
import pandas as pd
from pathlib import Path

SEED = 42
N_DAYS = 500          # ~2 years of trading days
CRISIS_START = 200
CRISIS_LENGTH = 30
DF = 5                # Student-t degrees of freedom → fat tails

np.random.seed(SEED)

out_dir = Path(__file__).parent
out_dir.mkdir(parents=True, exist_ok=True)


def generate_desk(name: str, notional_cr: float, vol_daily: float, crisis_shock: float) -> pd.DataFrame:
    """Generate returns for one desk. Returns are daily percentage returns."""
    # Base Student-t returns
    t_draws = np.random.standard_t(df=DF, size=N_DAYS)
    # Scale to desired daily volatility (approx)
    returns = t_draws * (vol_daily / np.std(t_draws))

    # Inject crisis: large negative shocks
    crisis_idx = slice(CRISIS_START, CRISIS_START + CRISIS_LENGTH)
    crisis_shock_draws = -np.abs(np.random.standard_t(df=DF, size=CRISIS_LENGTH)) * crisis_shock
    returns[crisis_idx] += crisis_shock_draws

    # Simple P&L in crore (notional * return)
    pnl = notional_cr * returns

    df = pd.DataFrame({
        "date": pd.bdate_range(end="2026-11-09", periods=N_DAYS, freq="B"),
        "return": returns,
        "pnl_crore": pnl,
        "desk": name,
    })
    return df


# Desk parameters (all fictional)
# vol_daily ≈ daily std of returns; crisis_shock = extra negative multiple during crisis
equities = generate_desk("equities", 400, vol_daily=0.015, crisis_shock=0.04)
fx = generate_desk("fx", 250, vol_daily=0.008, crisis_shock=0.025)
rates = generate_desk("rates", 350, vol_daily=0.006, crisis_shock=0.02)

# Save individual desks
equities.to_csv(out_dir / "equities_returns.csv", index=False)
fx.to_csv(out_dir / "fx_returns.csv", index=False)
rates.to_csv(out_dir / "rates_returns.csv", index=False)

# Combined portfolio (simple sum of PnL — no diversification benefit yet)
portfolio = equities[["date"]].copy()
portfolio["pnl_equities"] = equities["pnl_crore"]
portfolio["pnl_fx"] = fx["pnl_crore"]
portfolio["pnl_rates"] = rates["pnl_crore"]
portfolio["pnl_total"] = portfolio[["pnl_equities", "pnl_fx", "pnl_rates"]].sum(axis=1)
portfolio["return_total"] = portfolio["pnl_total"] / 1000  # total notional 1000 cr

portfolio.to_csv(out_dir / "portfolio_returns.csv", index=False)

print("Synthetic data generated (seed=42):")
print(f"  equities_returns.csv  — {len(equities)} days")
print(f"  fx_returns.csv        — {len(fx)} days")
print(f"  rates_returns.csv     — {len(rates)} days")
print(f"  portfolio_returns.csv — {len(portfolio)} days")
print("All figures are fictional.")
