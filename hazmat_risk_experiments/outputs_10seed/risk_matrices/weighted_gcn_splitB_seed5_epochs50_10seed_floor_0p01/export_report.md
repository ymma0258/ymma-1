# Risk Matrix Export Report

## Model

- Model: `weighted_gcn`; split: `B`; seed: `5`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5996, MAE=1.2001, QWK=0.7062, Recall@6-8=0.8250.
- `data_2021_train`: Macro-F1=0.7363, MAE=1.0883, QWK=0.7269, Recall@6-8=0.7600.
- `data_2021_test`: Macro-F1=0.2948, MAE=1.4737, QWK=0.4392, Recall@6-8=0.3846.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019701, P75=0.004572, P90=0.008563, P95=0.092251, P99=0.431570, max=0.910211, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.015464, P75=0.004394, P90=0.007409, P95=0.070279, P99=0.339587, max=0.855625, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
