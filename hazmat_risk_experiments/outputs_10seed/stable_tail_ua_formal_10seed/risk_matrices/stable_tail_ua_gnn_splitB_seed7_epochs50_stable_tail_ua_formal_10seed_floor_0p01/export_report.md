# Risk Matrix Export Report

## Model

- Model: `stable_tail_ua_gnn`; split: `B`; seed: `7`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3385, MAE=0.9375, QWK=0.5089, Recall@6-8=0.5250.
- `data_2021_train`: Macro-F1=0.4137, MAE=0.7388, QWK=0.6124, Recall@6-8=0.6800.
- `data_2021_test`: Macro-F1=0.2283, MAE=1.3571, QWK=0.2556, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018996, P75=0.004186, P90=0.007599, P95=0.085791, P99=0.417022, max=0.825787, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017819, P75=0.004258, P90=0.007346, P95=0.075083, P99=0.417863, max=0.836604, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
