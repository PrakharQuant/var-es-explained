# 10. Exercises & Glossary

## Exercises

**Exercise 1 (VaR by hand)**  
Losses (₹ cr): 4, 1, 6, 2, 9, 3, 5, 0, 8, 7  
Compute 90 % VaR and 90 % ES.

**Exercise 2 (Subadditivity)**  
Create your own two-desk example (10 days each) where 95 % VaR(A+B) > VaR(A) + VaR(B).

**Exercise 3 (Scaling)**  
A desk has 97.5 % 10-day ES = ₹ 15 crore.  
What is the approximate capital if we apply a 1.5 multiplier and the desk has a 40-day liquidity horizon?

**Exercise 4 (Backtesting)**  
In 250 days you observe 8 exceptions at 99 % VaR. What traffic-light zone? What happens to the multiplier?

*(Solutions are in the matching notebook `10_exercises.ipynb`.)*

---

## Glossary

| Term                  | Plain-English meaning                                      |
|-----------------------|------------------------------------------------------------|
| VaR                   | Loss cutoff exceeded only X % of the time                  |
| ES / Expected Shortfall | Average loss on the days that exceed VaR                |
| Confidence level      | 99 % means we look at the worst 1 %                        |
| Subadditive           | Risk of sum ≤ sum of risks (diversification helps)         |
| Liquidity horizon     | How many days it would take to exit the position           |
| Traffic-light         | Green / Amber / Red based on number of VaR exceptions      |
| FRTB                  | Fundamental Review of the Trading Book (BCBS d457)         |
| Stressed calibration  | Calculate the risk measure on a crisis period              |

---

**Credits**  
Prakhar · bestofprakhar@gmail.com  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/search/results/all/?keywords=prakhar)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/search?q=prakhar)
