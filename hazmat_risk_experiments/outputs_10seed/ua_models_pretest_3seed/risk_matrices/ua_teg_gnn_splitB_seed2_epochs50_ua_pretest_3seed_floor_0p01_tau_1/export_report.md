# Risk Matrix Export Report

## Model

- Model: `ua_teg_gnn`; split: `B`; seed: `2`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.2052, MAE=1.1501, QWK=0.0957, Recall@6-8=0.0750.
- `data_2021_train`: Macro-F1=0.1923, MAE=1.1111, QWK=0.1851, Recall@6-8=0.1600.
- `data_2021_test`: Macro-F1=0.1626, MAE=1.3378, QWK=0.0356, Recall@6-8=0.0385.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.051690, P75=0.010000, P90=0.010000, P95=0.505000, P99=1.000000, max=1.000000, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.048910, P75=0.010000, P90=0.010000, P95=0.505000, P99=1.000000, max=1.000000, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
