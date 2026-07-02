# Risk Matrix Export Report

## Model

- Model: `ua_gnn`; split: `B`; seed: `1`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4892, MAE=0.8764, QWK=0.6397, Recall@6-8=0.6500.
- `data_2021_train`: Macro-F1=0.6104, MAE=0.7562, QWK=0.7093, Recall@6-8=0.7200.
- `data_2021_test`: Macro-F1=0.2453, MAE=1.3555, QWK=0.2433, Recall@6-8=0.1923.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.042497, P75=0.009109, P90=0.010000, P95=0.361956, P99=0.828580, max=1.000000, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.038071, P75=0.009073, P90=0.010000, P95=0.275352, P99=0.803445, max=1.000000, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
