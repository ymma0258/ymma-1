# Risk Matrix Export Report

## Model

- Model: `gcn`; split: `B`; seed: `3`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6002, MAE=0.8233, QWK=0.7200, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.7151, MAE=0.6313, QWK=0.8008, Recall@6-8=0.8400.
- `data_2021_test`: Macro-F1=0.2932, MAE=1.3363, QWK=0.1606, Recall@6-8=0.0769.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020485, P75=0.003614, P90=0.008570, P95=0.118413, P99=0.432798, max=0.885945, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017302, P75=0.003512, P90=0.008508, P95=0.103335, P99=0.390665, max=0.857011, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
