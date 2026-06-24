# Risk Matrix Export Report

## Model

- Model: `teg_gnn`; split: `B`; seed: `1`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6090, MAE=1.2514, QWK=0.6839, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.6424, MAE=1.1238, QWK=0.7120, Recall@6-8=0.6800.
- `data_2021_test`: Macro-F1=0.2381, MAE=1.6685, QWK=0.2580, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020127, P75=0.004716, P90=0.008566, P95=0.103789, P99=0.430627, max=0.856974, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017387, P75=0.004565, P90=0.008471, P95=0.085197, P99=0.391730, max=0.855946, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
