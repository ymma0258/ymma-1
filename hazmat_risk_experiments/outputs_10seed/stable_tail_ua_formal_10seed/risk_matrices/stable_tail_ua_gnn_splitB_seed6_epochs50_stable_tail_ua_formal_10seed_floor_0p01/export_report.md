# Risk Matrix Export Report

## Model

- Model: `stable_tail_ua_gnn`; split: `B`; seed: `6`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.2959, MAE=1.0288, QWK=0.4641, Recall@6-8=0.5250.
- `data_2021_train`: Macro-F1=0.3758, MAE=0.9217, QWK=0.5834, Recall@6-8=0.7200.
- `data_2021_test`: Macro-F1=0.2174, MAE=1.2868, QWK=0.3323, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020437, P75=0.004672, P90=0.008010, P95=0.109252, P99=0.486936, max=0.812815, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018905, P75=0.004391, P90=0.007106, P95=0.091042, P99=0.424282, max=0.840163, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
