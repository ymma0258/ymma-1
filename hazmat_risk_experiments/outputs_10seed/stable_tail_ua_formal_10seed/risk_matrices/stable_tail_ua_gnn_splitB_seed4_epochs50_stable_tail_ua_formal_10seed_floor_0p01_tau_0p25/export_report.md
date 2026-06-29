# Risk Matrix Export Report

## Model

- Model: `stable_tail_ua_gnn`; split: `B`; seed: `4`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3425, MAE=0.8770, QWK=0.5529, Recall@6-8=0.5500.
- `data_2021_train`: Macro-F1=0.5214, MAE=0.7701, QWK=0.6614, Recall@6-8=0.6400.
- `data_2021_test`: Macro-F1=0.2221, MAE=1.2395, QWK=0.2603, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.028896, P75=0.005637, P90=0.010000, P95=0.183974, P99=0.505000, max=1.000000, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.025789, P75=0.005169, P90=0.010000, P95=0.150661, P99=0.505000, max=1.000000, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
