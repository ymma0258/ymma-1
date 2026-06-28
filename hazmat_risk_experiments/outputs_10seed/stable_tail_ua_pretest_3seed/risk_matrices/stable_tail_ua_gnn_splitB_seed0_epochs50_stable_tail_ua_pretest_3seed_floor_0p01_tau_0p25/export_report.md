# Risk Matrix Export Report

## Model

- Model: `stable_tail_ua_gnn`; split: `B`; seed: `0`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3795, MAE=0.7945, QWK=0.6626, Recall@6-8=0.6750.
- `data_2021_train`: Macro-F1=0.5074, MAE=0.6590, QWK=0.7143, Recall@6-8=0.7200.
- `data_2021_test`: Macro-F1=0.2644, MAE=1.1285, QWK=0.3410, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.027237, P75=0.005092, P90=0.010000, P95=0.175625, P99=0.505000, max=1.000000, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.024382, P75=0.005035, P90=0.010000, P95=0.150171, P99=0.505000, max=1.000000, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
