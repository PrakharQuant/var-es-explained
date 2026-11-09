# 8. Backtesting demo

## Tiny example

Suppose over 250 days we forecast a 99 % VaR every day.  
We expect about 2.5 exceptions (1 % of 250).

If we observe:

- 3 exceptions → **green**
- 7 exceptions → **amber**
- 12 exceptions → **red**

## On Bharat Demo Bank data

The notebook runs a rolling 250-day historical VaR and counts how many times the next day’s loss exceeded that VaR.

Typical result you will see:

- Exceptions in the window: 6
- Traffic light: **amber**

(The exact count depends on the random seed and the crisis period we injected.)

## What the zones mean

| Zone  | Exceptions (250 days, 99 %) | Regulatory consequence          |
|-------|-----------------------------|---------------------------------|
| Green | 0–4                         | Multiplier stays at 3           |
| Amber | 5–9                         | Plus-factor increases           |
| Red   | ≥10                         | Model may be rejected / higher multiplier |

---

### Check yourself

If a bank has 11 exceptions in 250 days at 99 % VaR, what zone is it in and what is the rough implication?
