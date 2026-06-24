# Risk Matrix Export Report

## Model

- Model: `teg_gnn`; split: `B`; seed: `7`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5478, MAE=1.2638, QWK=0.6309, Recall@6-8=0.6750.
- `data_2021_train`: Macro-F1=0.7250, MAE=0.9715, QWK=0.7747, Recall@6-8=0.8000.
- `data_2021_test`: Macro-F1=0.1921, MAE=1.7977, QWK=0.2043, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021104, P75=0.005362, P90=0.008520, P95=0.111301, P99=0.432108, max=0.857051, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018700, P75=0.005176, P90=0.008449, P95=0.091945, P99=0.424586, max=0.857114, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
