# Risk Matrix Export Report

## Model

- Model: `ua_gnn`; split: `B`; seed: `0`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3881, MAE=0.9745, QWK=0.5696, Recall@6-8=0.5500.
- `data_2021_train`: Macro-F1=0.5666, MAE=0.8284, QWK=0.6163, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2969, MAE=1.2746, QWK=0.2845, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019891, P75=0.003384, P90=0.008570, P95=0.123061, P99=0.432641, max=0.887072, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017589, P75=0.003370, P90=0.007441, P95=0.107100, P99=0.375752, max=0.857205, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
