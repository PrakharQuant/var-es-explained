# Synthetic data

All returns are **fictional**.

Generate (or regenerate) the CSVs with a fixed seed:

```bash
python generate_data.py
```

This produces:

- `equities_returns.csv`
- `fx_returns.csv`
- `rates_returns.csv`
- `portfolio_returns.csv`

The generator uses Student-t (df=5) plus one injected crisis period. Random seed = 42 for full reproducibility.

**Educational use only.**
