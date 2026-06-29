# Risk Matrix Export Report

## Model

- Model: `ua_gnn`; split: `B`; seed: `0`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3881, MAE=0.9745, QWK=0.5696, Recall@6-8=0.5500.
- `data_2021_train`: Macro-F1=0.5666, MAE=0.8284, QWK=0.6163, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2969, MAE=1.2746, QWK=0.2845, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.041616, P75=0.008765, P90=0.010000, P95=0.326064, P99=0.842502, max=1.000000, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.039882, P75=0.008817, P90=0.010000, P95=0.310098, P99=0.751003, max=1.000000, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
