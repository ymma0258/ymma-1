# Risk Matrix Export Report

## Model

- Model: `weighted_gcn`; split: `B`; seed: `9`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5687, MAE=1.2547, QWK=0.6610, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.7388, MAE=0.9928, QWK=0.8203, Recall@6-8=0.8800.
- `data_2021_test`: Macro-F1=0.2298, MAE=1.6973, QWK=0.3025, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019946, P75=0.004639, P90=0.008549, P95=0.087759, P99=0.430907, max=0.936584, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.016874, P75=0.004568, P90=0.008458, P95=0.069324, P99=0.400574, max=0.853156, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
