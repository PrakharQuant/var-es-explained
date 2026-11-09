# var-es-explained

**A beginner-friendly, hands-on tutorial that teaches Value-at-Risk (VaR) and Expected Shortfall (ES) through the fictional “Bharat Demo Bank”.**

All numbers, returns, and regulatory figures in this repository are **completely synthetic and for educational purposes only**. This is **not** compliance, regulatory, or investment advice. Always verify against the latest official BCBS / RBI circulars.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/MkDocs-Material-blue?style=for-the-badge&logo=materialdesign&logoColor=white" alt="MkDocs">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT">
  <img src="https://img.shields.io/badge/Status-Educational-orange?style=for-the-badge" alt="Educational">
</p>

---

## Why this project?

Most VaR/ES tutorials jump straight to equations. Here we follow a strict teaching rule:

1. **Worked numerical example** with tiny dummy numbers first  
2. **Plain-English intuition**  
3. **Only then** the formal equation, with every symbol mapped back to the numbers you already saw  

You will calculate VaR and ES by hand on 10 sorted losses, then scale up to the full bank, compare three methods, see why VaR can punish diversification, walk through Basel III / FRTB capital numbers, and run a backtest that produces traffic-light results — all on the same fictional trading book.

## Dummy bank — Bharat Demo Bank

| Desk       | Notional          | Instruments                          |
|------------|-------------------|--------------------------------------|
| Equities   | ₹ 400 crore      | 5 Nifty-like stocks                  |
| FX         | ₹ 250 crore      | USD/INR, EUR/INR                     |
| Rates      | ₹ 350 crore      | Government bonds                     |
| **Total**  | **₹ 1,000 crore**|                                      |

Daily returns are generated from a Student-t distribution (fat tails) with one injected “crisis” period. Fixed random seed so every run is reproducible. Data ships as CSV in `data/`.

## Learning path

| # | Topic                                      | Notebook                  | Docs page                          |
|---|--------------------------------------------|---------------------------|------------------------------------|
| 1 | Why risk capital exists                    | `01_why_risk_capital`     | Why risk capital                   |
| 2 | VaR by hand                                | `02_var_by_hand`          | VaR by hand                        |
| 3 | ES by hand                                 | `03_es_by_hand`           | ES by hand                         |
| 4 | Three methods side-by-side                 | `04_three_methods`        | Historical / Parametric / MC       |
| 5 | Why VaR fails (subadditivity)              | `05_why_var_fails`        | Why VaR fails                      |
| 6 | Regulatory norms (Basel & FRTB)            | `06_regulatory`           | Regulatory norms                   |
| 7 | Capital calculation walkthrough            | `07_capital`              | From ES to capital                 |
| 8 | Backtesting demo                           | `08_backtesting`          | Backtesting & traffic lights       |
| 9 | Limitations                                | `09_limitations`          | Limitations                        |
| 10| Exercises + Glossary                       | `10_exercises`            | Exercises & Glossary               |

## Quickstart

```bash
# Clone
git clone https://github.com/YOUR_USERNAME/var-es-explained.git
cd var-es-explained

# Install
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Generate / verify data (already included)
python data/generate_data.py

# Run tests
pytest

# Launch the tutorial site
mkdocs serve
# → http://127.0.0.1:8000

# Or open the notebooks
jupyter lab notebooks/
```

## Project layout

```
var-es-explained/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── requirements.txt
├── mkdocs.yml
├── .github/workflows/ci.yml
├── data/                    # synthetic CSVs + generator
├── src/varES/               # clean library (historical, parametric, MC, backtest, FRTB)
├── tests/                   # pytest — checks code against hand-computed answers
├── notebooks/               # 01–10 executed notebooks
└── docs/                    # MkDocs Material source (deploys to GitHub Pages)
```

## “Check yourself” boxes

After every major section you will find a short **Check yourself** box. Try to answer before looking at the solution in the notebook or the next paragraph.

## Credits

Built as a teaching project by **Prakhar**.

<p align="center">
  <a href="mailto:bestofprakhar@gmail.com">
    <img src="https://img.shields.io/badge/Email-bestofprakhar%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email">
  </a>
  <a href="https://www.linkedin.com/search/results/all/?keywords=prakhar">
    <img src="https://img.shields.io/badge/LinkedIn-Prakhar-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  <a href="https://twitter.com/search?q=prakhar">
    <img src="https://img.shields.io/badge/Twitter-Prakhar-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter">
  </a>
</p>

**Disclaimer:** Educational material only. Not regulatory advice. Verify all capital rules against the latest BCBS and RBI publications.

---

*All data is fictional. Random seed fixed for full reproducibility.*
