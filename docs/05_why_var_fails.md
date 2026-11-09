# 5. Why VaR fails

## Tiny numerical counter-example (subadditivity)

Imagine two tiny desks, each with the following 10 possible daily losses (₹ crore).  
We look at **95 % VaR** (worst 5 % → the single worst loss in each list of 10).

**Desk A losses:** 1, 1, 1, 1, 1, 1, 1, 1, 1, **10**  
→ 95 % VaR_A = **10**

**Desk B losses:** 1, 1, 1, 1, 1, 1, 1, 1, 1, **10**  
→ 95 % VaR_B = **10**

**Portfolio (A+B) losses** (sum each day):  
2, 2, 2, 2, 2, 2, 2, 2, 2, **20**  
→ 95 % VaR_{A+B} = **20**

VaR(A) + VaR(B) = 20 = VaR(A+B)

Now change the timing so the big losses never happen on the same day:

**Desk A:** 1,1,1,1,1,1,1,1,1,**10**  
**Desk B:** **10**,1,1,1,1,1,1,1,1,1  

**Portfolio losses:** 11, 2, 2, 2, 2, 2, 2, 2, 2, 11  

Sorted portfolio: 2,2,2,2,2,2,2,2,11,11  
→ 95 % VaR_{A+B} = **11**

But VaR(A) + VaR(B) = 20  

**VaR(A+B) = 11 < 20 = VaR(A)+VaR(B)**

Diversification *reduced* the portfolio VaR by more than the sum — wait, no: 11 < 20, so VaR of the sum is *smaller* than the sum of VaRs. That is actually subadditive in this case? Wait.

Classic counter-example is the opposite direction for the violation.

Let me give the standard one where VaR *penalizes* diversification.

**Correct classic counter-example:**

Two bonds, each can default with 4 % probability, loss = 100 if default, 0 otherwise.  
99 % VaR of each bond = 0 (because 4 % < 1 %, so the 99 % quantile is still 0).

Portfolio of both: probability both default is small, but probability at least one defaults ≈ 8 %.  
99 % VaR of portfolio = 100.

VaR(A+B) = 100 > 0 + 0 = VaR(A)+VaR(B)

**VaR punishes diversification** — holding both is “riskier” according to VaR than holding one, which is absurd.

**ES does not have this problem.**  
ES of each bond ≈ 4 (average loss in the 1 % tail, but since default prob is 4 %, the tail average is positive).  
ES of the portfolio is less than the sum of the individual ES figures (subadditive).

## Plain-English intuition

VaR only looks at a single cutoff. It can ignore the severity of losses beyond the cutoff and can give non-intuitive results when risks are combined. ES looks at the average severity in the tail and is always subadditive (diversification never increases ES).

## Formal statement

A risk measure ρ is **subadditive** if

\[
\rho(X + Y) \le \rho(X) + \rho(Y)
\]

VaR is not always subadditive. ES is subadditive.

---

### Check yourself

In the bond default example, why does 99 % VaR of a single bond equal 0 even though there is a 4 % chance of losing 100?
