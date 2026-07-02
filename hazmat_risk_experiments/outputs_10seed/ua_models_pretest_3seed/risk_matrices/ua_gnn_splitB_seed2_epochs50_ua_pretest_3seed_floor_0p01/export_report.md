# Risk Matrix Export Report

## Model

- Model: `ua_gnn`; split: `B`; seed: `2`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3441, MAE=1.1299, QWK=0.3946, Recall@6-8=0.3500.
- `data_2021_train`: Macro-F1=0.3449, MAE=1.0168, QWK=0.4100, Recall@6-8=0.3600.
- `data_2021_test`: Macro-F1=0.2371, MAE=1.3722, QWK=0.1224, Recall@6-8=0.1154.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018181, P75=0.003276, P90=0.006410, P95=0.132865, P99=0.366912, max=0.833097, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017189, P75=0.003322, P90=0.006583, P95=0.125755, P99=0.337125, max=0.847045, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
