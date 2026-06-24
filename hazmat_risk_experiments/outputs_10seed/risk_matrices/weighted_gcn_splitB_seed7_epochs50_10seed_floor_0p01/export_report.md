# Risk Matrix Export Report

## Model

- Model: `weighted_gcn`; split: `B`; seed: `7`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5480, MAE=1.2462, QWK=0.6660, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.6652, MAE=0.9493, QWK=0.8279, Recall@6-8=0.8400.
- `data_2021_test`: Macro-F1=0.1852, MAE=1.7741, QWK=0.2044, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020880, P75=0.004837, P90=0.008574, P95=0.100859, P99=0.433065, max=0.858383, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018443, P75=0.004895, P90=0.008485, P95=0.081889, P99=0.428473, max=0.858803, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
