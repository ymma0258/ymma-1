# Risk Matrix Export Report

## Model

- Model: `teg_gnn`; split: `B`; seed: `3`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5238, MAE=1.2478, QWK=0.5951, Recall@6-8=0.5750.
- `data_2021_train`: Macro-F1=0.6623, MAE=1.0245, QWK=0.7459, Recall@6-8=0.7600.
- `data_2021_test`: Macro-F1=0.2547, MAE=1.6035, QWK=0.1651, Recall@6-8=0.0769.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020337, P75=0.004629, P90=0.008517, P95=0.102905, P99=0.432606, max=0.856981, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017400, P75=0.004560, P90=0.008376, P95=0.091474, P99=0.367938, max=0.856685, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
