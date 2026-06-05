# Risk Matrix Export Report

## Model

- Model: `weighted_gcn`; split: `B`; seed: `0`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5337, MAE=1.2821, QWK=0.6300, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.6592, MAE=1.1643, QWK=0.7332, Recall@6-8=0.8000.
- `data_2021_test`: Macro-F1=0.2924, MAE=1.5891, QWK=0.3042, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021095, P75=0.004917, P90=0.008493, P95=0.120593, P99=0.428892, max=0.854361, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018119, P75=0.004716, P90=0.007254, P95=0.103988, P99=0.365026, max=0.854114, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
