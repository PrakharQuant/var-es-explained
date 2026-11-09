# 4. Three methods side by side

We now calculate VaR and ES for the whole Bharat Demo Bank (₹ 1 000 crore notional) using three classic methods on the same synthetic data.

## Tiny reminder of the methods

| Method              | What it does                                      | Strength                  | Weakness                     |
|---------------------|---------------------------------------------------|---------------------------|------------------------------|
| Historical          | Sorts the actual past losses and picks the quantile | No distribution assumption | Needs long history           |
| Parametric (normal) | Assumes losses are normal, uses mean + z × std    | Fast, closed form         | Underestimates fat tails     |
| Monte Carlo         | Simulates thousands of Student-t scenarios        | Flexible                  | Needs a good model           |

## Results on Bharat Demo Bank (illustrative)

*(Exact numbers are produced by the notebook / library; the table below shows the typical pattern you will see.)*

| Method         | 99 % 1-day VaR (₹ cr) | 97.5 % 1-day ES (₹ cr) |
|----------------|-----------------------|------------------------|
| Historical     | 36.6                  | 41.5                   |
| Parametric     | 25.4                  | 25.6                   |
| Monte Carlo    | 28.3                  | 29.4                   |

**Observation:** The normal parametric method gives the smallest numbers because it ignores the fat tails we deliberately put into the data. Historical and Monte Carlo (Student-t) are closer to each other and larger.

All figures in ₹ crore. Confidence levels shown in the column headers.

## Check yourself

Why is the parametric (normal) VaR smaller than the historical VaR on this data set?
