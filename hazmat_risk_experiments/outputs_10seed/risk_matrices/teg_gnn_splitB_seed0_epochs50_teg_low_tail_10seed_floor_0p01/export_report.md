# Risk Matrix Export Report

## Model

- Model: `teg_gnn`; split: `B`; seed: `0`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5041, MAE=1.1733, QWK=0.6709, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.5834, MAE=1.0514, QWK=0.6967, Recall@6-8=0.7200.
- `data_2021_test`: Macro-F1=0.2917, MAE=1.4932, QWK=0.3488, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.022136, P75=0.005000, P90=0.008571, P95=0.114060, P99=0.432799, max=0.941406, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018834, P75=0.004848, P90=0.008540, P95=0.094276, P99=0.416404, max=0.857169, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
