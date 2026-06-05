# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `A`; seed: `3`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5409, MAE=0.5754, QWK=0.7837, Recall@6-8=0.9355.
- `data_2020_val`: Macro-F1=0.2709, MAE=1.2693, QWK=0.3357, Recall@6-8=0.3333.
- `data_2021_test`: Macro-F1=0.3325, MAE=1.1746, QWK=0.3715, Recall@6-8=0.3333.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018383, P75=0.003581, P90=0.008389, P95=0.087393, P99=0.424989, max=0.856029, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.016519, P75=0.003376, P90=0.007594, P95=0.083034, P99=0.389867, max=0.854510, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
