# 9. Limitations

Even a perfect ES calculation has limits.

## 1. Elicitability

You can back-test VaR easily (just count exceptions).  
ES is harder to back-test directly because it is an average of a random number of tail events. Special techniques exist, but they are more complicated.

## 2. Data scarcity

A 97.5 % ES looks at the worst 2.5 % of days.  
In 10 years of data (~2 500 days) you only have about 60 observations in the tail.  
One or two extreme days can move the ES a lot.

## 3. Model risk

- Historical: “the future will look like the past” (including the crisis we injected)
- Parametric normal: ignores fat tails
- Monte Carlo: only as good as the distribution you simulate

## 4. Procyclicality

In good times volatility is low → ES is low → capital is low → banks take more risk.  
When a crisis hits, ES jumps → capital requirement jumps → banks may be forced to sell assets, making the crisis worse.

---

### Check yourself

Why is it harder to back-test ES than VaR?
