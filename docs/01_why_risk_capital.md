# 1. Why risk capital exists

## Tiny example first

Imagine you run a tiny shop that can lose at most ₹ 10 on a bad day.

- You keep ₹ 10 in a locked box “just in case”.
- That ₹ 10 is your **risk capital** (or risk buffer).
- It is **not** insurance (insurance pays you after the loss). It is money you already have so you can absorb the loss and still open the shop tomorrow.

Scale that idea up:

| Desk     | Worst single-day loss we want to survive | Capital we set aside |
|----------|------------------------------------------|----------------------|
| Equities | ₹ 12 crore                              | ₹ 12 crore          |
| FX       | ₹ 5 crore                               | ₹ 5 crore           |
| Rates    | ₹ 4 crore                               | ₹ 4 crore           |
| **Bank** |                                         | **₹ 21 crore**      |

(The real numbers will come later; this is just the logic.)

## Plain-English intuition

Banks are allowed to take risk, but they must hold enough capital so that even in a bad period they do not go bankrupt and hurt depositors or the financial system.

- **Capital** = the buffer that absorbs losses.
- **Insurance** = someone else pays you after the loss (you still need capital while you wait).
- Regulators force banks to hold capital calculated from risk measures (VaR or ES) so the buffer is large enough for the risks they actually take.

## Formal idea (after the example)

We can write the idea as:

\[
\text{Risk capital} \approx \text{a high quantile (or average of the tail) of the loss distribution}
\]

Every later page will turn this sentence into precise numbers for Bharat Demo Bank.

---

### Check yourself

1. Why is the ₹ 10 in the locked box called “capital” and not “insurance”?
2. If the equities desk can lose ₹ 12 crore on a very bad day, why might the bank still hold more than ₹ 12 crore for that desk?

*(Answers are in the matching notebook.)*
