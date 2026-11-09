# 7. Capital calculation walkthrough

We now turn the ES numbers into a capital figure for each desk and for the whole bank.

## Tiny example first

Suppose a desk has:

- 97.5 % 10-day ES = ₹ 20 crore
- Liquidity horizon = 10 days (no scaling)
- Regulatory multiplier = 1.5 (simplified FRTB-style)

**Capital for the desk ≈ 20 × 1.5 = ₹ 30 crore**

## Desk-level numbers (illustrative, from the synthetic data)

| Desk     | 97.5 % 1-day ES (₹ cr) | ×√10 ≈ 10-day | × 1.5 multiplier | Desk capital (₹ cr) |
|----------|------------------------|---------------|------------------|---------------------|
| Equities | 22.1                   | 70            |                  | 105                 |
| FX       | 9.4                    | 30            |                  | 45                  |
| Rates    | 7.8                    | 25            |                  | 37                  |
| **Sum**  |                        |               |                  | **187**             |

## Diversification benefit

When we calculate ES on the **whole portfolio** (not the sum of desks) we get a lower number because losses do not all happen on the same day.

- Sum of desk capitals ≈ ₹ 187 crore
- Portfolio-level ES capital ≈ ₹ 155 crore
- **Diversification benefit ≈ ₹ 32 crore**

Final bank market-risk capital (this simplified walk-through) ≈ **₹ 155 crore**.

(Real FRTB has many more components: NMRF, default risk charge, etc.)

---

### Check yourself

Why is the portfolio capital lower than the sum of the three desk capitals?
