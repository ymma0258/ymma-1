# Risk Matrix Export Report

## Model

- Model: `gcn`; split: `B`; seed: `9`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6218, MAE=0.9352, QWK=0.7004, Recall@6-8=0.7500.
- `data_2021_train`: Macro-F1=0.7826, MAE=0.7370, QWK=0.7649, Recall@6-8=0.8400.
- `data_2021_test`: Macro-F1=0.2681, MAE=1.4022, QWK=0.2465, Recall@6-8=0.1923.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020997, P75=0.003669, P90=0.008565, P95=0.127262, P99=0.432729, max=0.926362, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018574, P75=0.003538, P90=0.008508, P95=0.109333, P99=0.418317, max=0.856916, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
