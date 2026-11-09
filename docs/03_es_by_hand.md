# 3. Expected Shortfall (ES) by hand

## Tiny numerical example (same 10 losses)

Sorted losses again:

```
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

From the previous page, **90 % VaR = 8**.

ES asks a different question:

> “When we *do* exceed the VaR, how bad is the loss on average?”

The losses that are **greater than or equal to 8** are: **8 and 9**.

Average of the tail:

\[
\frac{8 + 9}{2} = 8.5
\]

**90 % ES = 8.5** (₹ crore)

ES is always at least as large as VaR, and usually larger.

## Plain-English intuition

- VaR = the fence  
- ES = the average height of everything that jumped over the fence  

Regulators prefer ES because it cares about *how bad* the bad days are, not just whether they crossed a line.

## Formal equation (mapped back)

\[
\text{ES}_\alpha = \mathbb{E}[\text{Loss} \mid \text{Loss} \ge \text{VaR}_\alpha]
\]

- \(\text{VaR}_{0.90} = 8\)
- Conditional expectation = average of {8, 9} = 8.5

Same numbers you already calculated by hand.

---

### Check yourself

Using the same list, compute **95 % ES**.  
(You only have one observation beyond the 95 % VaR.)
