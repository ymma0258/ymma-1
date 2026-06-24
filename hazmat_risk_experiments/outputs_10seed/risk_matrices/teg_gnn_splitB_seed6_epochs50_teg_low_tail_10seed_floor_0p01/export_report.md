# Risk Matrix Export Report

## Model

- Model: `teg_gnn`; split: `B`; seed: `6`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5590, MAE=1.1862, QWK=0.6110, Recall@6-8=0.6750.
- `data_2021_train`: Macro-F1=0.7386, MAE=1.0307, QWK=0.7795, Recall@6-8=0.8000.
- `data_2021_test`: Macro-F1=0.3214, MAE=1.5370, QWK=0.4066, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019832, P75=0.004956, P90=0.008527, P95=0.094436, P99=0.429811, max=0.889419, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018000, P75=0.004945, P90=0.008321, P95=0.086450, P99=0.418493, max=0.853817, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
