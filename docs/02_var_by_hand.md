# 2. VaR by hand

## Tiny numerical example

Here are **10 daily losses** (in ₹ crore) for a miniature desk. Positive number = loss.

```
3, 1, 7, 2, 9, 4, 6, 0, 8, 5
```

**Step 1 – Sort them from smallest to largest loss:**

```
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

**Step 2 – Pick a confidence level.**  
Let’s take **90 %** VaR. That means we want the loss that is only exceeded 10 % of the time.

With 10 observations the 10 % tail is the **worst 1 observation**.  
So the cutoff is the 9th number in the sorted list (or the start of the worst 10 %).

**90 % VaR = 8** (₹ crore)

(If we had 250 days we would look further into the tail; the logic is identical.)

## Scaling to 250 days (intuition)

With only 10 days the 90 % VaR is rough. With 250 days the same 90 % VaR is the loss that is exceeded on about 25 days. We simply sort all 250 losses and pick the appropriate cutoff. No new mathematics — just more data.

## Plain-English intuition

VaR answers the question:

> “What is the loss amount that we expect to exceed only X % of the time?”

It is a **cutoff**, not the average of the bad days. Everything worse than the cutoff is ignored by VaR.

## Formal equation (mapped to the numbers)

\[
\text{VaR}_\alpha = \text{the } (1-\alpha)\text{-quantile of the loss distribution}
\]

- \(\alpha = 0.90\) → we used the example above → VaR = 8
- In the sorted list of 10 losses the quantile sits at position \(\lceil 10 \times 0.10 \rceil\)

That is all VaR is.

---

### Check yourself

Using the same 10 losses, what is the **95 %** VaR?  
(Hint: 5 % of 10 = 0.5 → you look at the worst observation.)

*(Solution in the notebook.)*
