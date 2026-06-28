# Risk Matrix Export Report

## Model

- Model: `stable_tail_ua_gnn`; split: `B`; seed: `0`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3805, MAE=0.7937, QWK=0.6641, Recall@6-8=0.6750.
- `data_2021_train`: Macro-F1=0.5074, MAE=0.6597, QWK=0.7143, Recall@6-8=0.7200.
- `data_2021_test`: Macro-F1=0.2653, MAE=1.1279, QWK=0.3500, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.034633, P75=0.007155, P90=0.010000, P95=0.264413, P99=0.616709, max=1.000000, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.031839, P75=0.007028, P90=0.010000, P95=0.220392, P99=0.602308, max=1.000000, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
