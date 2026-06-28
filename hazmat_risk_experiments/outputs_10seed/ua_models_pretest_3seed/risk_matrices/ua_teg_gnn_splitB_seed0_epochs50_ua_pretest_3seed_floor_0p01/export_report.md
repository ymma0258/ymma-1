# Risk Matrix Export Report

## Model

- Model: `ua_teg_gnn`; split: `B`; seed: `0`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4118, MAE=0.7608, QWK=0.6110, Recall@6-8=0.6250.
- `data_2021_train`: Macro-F1=0.5171, MAE=0.6320, QWK=0.7107, Recall@6-8=0.7200.
- `data_2021_test`: Macro-F1=0.3307, MAE=1.1307, QWK=0.3609, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018980, P75=0.003588, P90=0.008243, P95=0.083543, P99=0.427408, max=0.851307, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.016331, P75=0.003678, P90=0.008146, P95=0.069544, P99=0.423815, max=0.843319, zero_ratio=0.000131.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
