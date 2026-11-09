# Welcome to VaR & Expected Shortfall Explained

This site teaches **Value-at-Risk (VaR)** and **Expected Shortfall (ES)** the slow, clear way — using the fictional **Bharat Demo Bank**.

> **All numbers are fictional.** This is educational material, not compliance or investment advice. Always check the latest BCBS and RBI documents.

## Teaching rule we follow everywhere

1. **Tiny numerical example first** (you can do it with a pencil)
2. **Plain-English intuition**
3. **Only then the formal equation**, with every symbol pointing back to the numbers you already calculated

## The bank

| Desk     | Notional     | What it trades          |
|----------|--------------|-------------------------|
| Equities | ₹ 400 crore | 5 Nifty-like stocks     |
| FX       | ₹ 250 crore | USD/INR, EUR/INR        |
| Rates    | ₹ 350 crore | Government bonds        |
| **Total**| **₹ 1 000 crore** |                     |

Daily returns come from a fat-tailed Student-t distribution plus one crisis period. Data is in the `data/` folder and fully reproducible.

## How to use this site

Work through the pages in order. Each page has a matching Jupyter notebook in the `notebooks/` folder if you want to experiment.

Start here → **[1. Why risk capital exists](01_why_risk_capital.md)**

---

<p align="center">
  Built by Prakhar · <a href="mailto:bestofprakhar@gmail.com">bestofprakhar@gmail.com</a>
</p>
