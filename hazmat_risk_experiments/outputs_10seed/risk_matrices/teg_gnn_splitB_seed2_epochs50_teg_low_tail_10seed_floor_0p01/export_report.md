# Risk Matrix Export Report

## Model

- Model: `teg_gnn`; split: `B`; seed: `2`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5889, MAE=1.2485, QWK=0.6328, Recall@6-8=0.7000.
- `data_2021_train`: Macro-F1=0.6919, MAE=1.1276, QWK=0.7252, Recall@6-8=0.7200.
- `data_2021_test`: Macro-F1=0.2783, MAE=1.5343, QWK=0.3523, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.022026, P75=0.004937, P90=0.008570, P95=0.126237, P99=0.432792, max=0.936002, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.019860, P75=0.004764, P90=0.008561, P95=0.106027, P99=0.426892, max=0.859787, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
