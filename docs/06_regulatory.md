# 6. Regulatory norms (with numbers)

> **Educational only.** Verify every figure against the latest official documents.  
> Sources: BCBS d352 (Basel 2.5/III), BCBS d457 (FRTB), and RBI circulars on market risk.

## Basel 2.5 / Basel III (VaR world)

- **99 % 10-day VaR**
- Plus **stressed VaR** (VaR calculated on a crisis period)
- Capital = max( VaR_t , m × average VaR ) + same for stressed VaR
- Multiplier **m = 3 + plus-factor** (plus-factor between 0 and 1 depending on backtesting)

Example (fictional numbers for Bharat Demo Bank):

| Component          | ₹ crore |
|--------------------|---------|
| 99 % 10-day VaR    | 85      |
| Stressed VaR       | 140     |
| Multiplier         | 3.2     |
| **Market-risk capital** | **≈ 720** |

## FRTB (Expected Shortfall world) — BCBS d457

- **97.5 % ES** (instead of 99 % VaR)
- **Stressed calibration**: ES calculated on the worst 12-month window
- **Liquidity horizons**: 10, 20, 40, 60, 120 days
- Cascading scaling (simplified):

\[
\text{ES}(LH) = \text{ES}(10) \times \sqrt{\frac{LH}{10}}
\]

(The full formula has more terms to avoid double-counting; see the notebook.)

Example liquidity scaling (fictional 10-day ES = 40 ₹ cr):

| Horizon | Scaling factor | Scaled ES (₹ cr) |
|---------|----------------|------------------|
| 10 d    | 1.00           | 40               |
| 20 d    | 1.41           | 56               |
| 40 d    | 2.00           | 80               |
| 60 d    | 2.45           | 98               |
| 120 d   | 3.46           | 138              |

## Backtesting

- 250-day rolling window
- Count exceptions (days loss > VaR)
- Traffic-light zones (classic Basel):
  - Green: 0–4 exceptions
  - Amber: 5–9
  - Red: ≥ 10

Also P&L attribution tests and desk-level model approval under FRTB.

## Standardized vs Internal Models

- **Standardized Approach (SA)**: regulator gives risk weights → simpler, usually higher capital
- **Internal Models Approach (IMA)**: bank uses its own ES model → must pass tough approval and backtesting

## Indian banks (RBI)

RBI has adopted the Basel market-risk framework with local timelines and some national discretions.  
**Flag: verify against the latest RBI circulars** (search “RBI FRTB” or “RBI market risk capital”).

---

### Check yourself

Why did regulators move from 99 % VaR to 97.5 % ES?
