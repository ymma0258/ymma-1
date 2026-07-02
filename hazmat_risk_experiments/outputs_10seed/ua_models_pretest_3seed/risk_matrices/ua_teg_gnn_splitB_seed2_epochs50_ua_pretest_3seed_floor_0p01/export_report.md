# Risk Matrix Export Report

## Model

- Model: `ua_teg_gnn`; split: `B`; seed: `2`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.2052, MAE=1.1501, QWK=0.0957, Recall@6-8=0.0750.
- `data_2021_train`: Macro-F1=0.1923, MAE=1.1111, QWK=0.1851, Recall@6-8=0.1600.
- `data_2021_test`: Macro-F1=0.1626, MAE=1.3378, QWK=0.0356, Recall@6-8=0.0385.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.010156, P75=0.002133, P90=0.003208, P95=0.063477, P99=0.214850, max=0.708863, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.009812, P75=0.002129, P90=0.003168, P95=0.060709, P99=0.203935, max=0.768049, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
