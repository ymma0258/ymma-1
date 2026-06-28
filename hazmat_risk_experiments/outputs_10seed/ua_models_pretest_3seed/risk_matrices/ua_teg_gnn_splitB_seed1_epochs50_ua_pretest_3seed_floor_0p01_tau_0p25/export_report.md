# Risk Matrix Export Report

## Model

- Model: `ua_teg_gnn`; split: `B`; seed: `1`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3053, MAE=1.0361, QWK=0.4939, Recall@6-8=0.5000.
- `data_2021_train`: Macro-F1=0.3201, MAE=1.0012, QWK=0.5143, Recall@6-8=0.5200.
- `data_2021_test`: Macro-F1=0.1994, MAE=1.3722, QWK=0.2563, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.028208, P75=0.005779, P90=0.010000, P95=0.164944, P99=0.577852, max=1.000000, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.025609, P75=0.005501, P90=0.010000, P95=0.137274, P99=0.516025, max=1.000000, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
