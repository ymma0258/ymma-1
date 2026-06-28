# Risk Matrix Export Report

## Model

- Model: `stable_tail_ua_gnn`; split: `B`; seed: `7`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3385, MAE=0.9375, QWK=0.5089, Recall@6-8=0.5250.
- `data_2021_train`: Macro-F1=0.4137, MAE=0.7388, QWK=0.6124, Recall@6-8=0.6800.
- `data_2021_test`: Macro-F1=0.2283, MAE=1.3571, QWK=0.2556, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.029233, P75=0.006200, P90=0.010000, P95=0.177067, P99=0.547785, max=1.000000, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.026814, P75=0.006106, P90=0.009879, P95=0.147404, P99=0.567820, max=1.000000, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
