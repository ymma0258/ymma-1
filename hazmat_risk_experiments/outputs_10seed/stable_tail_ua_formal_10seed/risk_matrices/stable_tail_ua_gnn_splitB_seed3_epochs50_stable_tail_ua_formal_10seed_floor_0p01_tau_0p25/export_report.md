# Risk Matrix Export Report

## Model

- Model: `stable_tail_ua_gnn`; split: `B`; seed: `3`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4631, MAE=0.8263, QWK=0.6202, Recall@6-8=0.6000.
- `data_2021_train`: Macro-F1=0.5429, MAE=0.6908, QWK=0.7373, Recall@6-8=0.8000.
- `data_2021_test`: Macro-F1=0.3168, MAE=1.2535, QWK=0.2054, Recall@6-8=0.1154.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.026973, P75=0.005091, P90=0.010000, P95=0.151668, P99=0.507325, max=1.000000, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.023742, P75=0.004915, P90=0.010000, P95=0.138435, P99=0.505000, max=1.000000, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
