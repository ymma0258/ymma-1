# Risk Matrix Export Report

## Model

- Model: `stable_tail_ec_gnn`; split: `B`; seed: `0`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.2676, MAE=1.0838, QWK=0.4825, Recall@6-8=0.4750.
- `data_2021_train`: Macro-F1=0.3160, MAE=1.0051, QWK=0.4656, Recall@6-8=0.4400.
- `data_2021_test`: Macro-F1=0.2303, MAE=1.2891, QWK=0.3479, Recall@6-8=0.3846.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018443, P75=0.003945, P90=0.006944, P95=0.110976, P99=0.394900, max=0.781979, zero_ratio=0.070877.
- `data_2021`: edges=7647, mean=0.017438, P75=0.004054, P90=0.007277, P95=0.095060, P99=0.405430, max=0.791606, zero_ratio=0.063947.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
