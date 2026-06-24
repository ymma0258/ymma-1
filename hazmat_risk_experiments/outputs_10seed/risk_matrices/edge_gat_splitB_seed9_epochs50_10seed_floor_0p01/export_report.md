# Risk Matrix Export Report

## Model

- Model: `edge_gat`; split: `B`; seed: `9`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6620, MAE=0.9098, QWK=0.7158, Recall@6-8=0.8000.
- `data_2021_train`: Macro-F1=0.7926, MAE=0.6623, QWK=0.7905, Recall@6-8=0.8800.
- `data_2021_test`: Macro-F1=0.2895, MAE=1.4034, QWK=0.2476, Recall@6-8=0.1538.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021153, P75=0.003904, P90=0.008566, P95=0.127809, P99=0.432693, max=0.958418, zero_ratio=0.002423.
- `data_2021`: edges=7647, mean=0.018692, P75=0.003796, P90=0.008548, P95=0.108495, P99=0.418649, max=0.856092, zero_ratio=0.001438.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
