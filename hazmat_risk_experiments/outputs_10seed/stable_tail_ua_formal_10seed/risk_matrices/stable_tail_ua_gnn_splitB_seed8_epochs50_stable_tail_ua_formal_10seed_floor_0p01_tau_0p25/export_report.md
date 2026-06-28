# Risk Matrix Export Report

## Model

- Model: `stable_tail_ua_gnn`; split: `B`; seed: `8`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.2807, MAE=1.0411, QWK=0.5174, Recall@6-8=0.5750.
- `data_2021_train`: Macro-F1=0.3632, MAE=0.9697, QWK=0.5488, Recall@6-8=0.5600.
- `data_2021_test`: Macro-F1=0.2274, MAE=1.2993, QWK=0.2658, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.031857, P75=0.006458, P90=0.010000, P95=0.223307, P99=0.645069, max=1.000000, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.029479, P75=0.006239, P90=0.009569, P95=0.197399, P99=0.526965, max=1.000000, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
