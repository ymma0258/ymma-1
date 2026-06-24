# Risk Matrix Export Report

## Model

- Model: `teg_gnn`; split: `B`; seed: `4`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5379, MAE=1.3064, QWK=0.5851, Recall@6-8=0.6000.
- `data_2021_train`: Macro-F1=0.7014, MAE=1.1136, QWK=0.7705, Recall@6-8=0.8000.
- `data_2021_test`: Macro-F1=0.2753, MAE=1.6770, QWK=0.2474, Recall@6-8=0.1923.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020781, P75=0.004573, P90=0.008554, P95=0.111720, P99=0.431956, max=0.910427, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018976, P75=0.004591, P90=0.008316, P95=0.097582, P99=0.419972, max=0.855728, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
