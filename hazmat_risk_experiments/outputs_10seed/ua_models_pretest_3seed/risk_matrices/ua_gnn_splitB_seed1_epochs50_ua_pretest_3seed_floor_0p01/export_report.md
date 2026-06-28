# Risk Matrix Export Report

## Model

- Model: `ua_gnn`; split: `B`; seed: `1`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4892, MAE=0.8764, QWK=0.6397, Recall@6-8=0.6500.
- `data_2021_train`: Macro-F1=0.6104, MAE=0.7562, QWK=0.7093, Recall@6-8=0.7200.
- `data_2021_test`: Macro-F1=0.2453, MAE=1.3555, QWK=0.2433, Recall@6-8=0.1923.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020401, P75=0.003632, P90=0.008378, P95=0.124844, P99=0.426333, max=0.864046, zero_ratio=0.001212.
- `data_2021`: edges=7647, mean=0.017648, P75=0.003508, P90=0.008162, P95=0.100207, P99=0.402922, max=0.869688, zero_ratio=0.001308.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
