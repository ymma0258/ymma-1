# Risk Matrix Export Report

## Model

- Model: `stable_tail_ua_gnn`; split: `B`; seed: `9`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.2963, MAE=0.9771, QWK=0.4922, Recall@6-8=0.5000.
- `data_2021_train`: Macro-F1=0.3656, MAE=0.8326, QWK=0.6029, Recall@6-8=0.6800.
- `data_2021_test`: Macro-F1=0.2241, MAE=1.2996, QWK=0.1737, Recall@6-8=0.1538.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.032104, P75=0.006285, P90=0.010000, P95=0.234248, P99=0.623426, max=1.000000, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.030191, P75=0.006142, P90=0.009963, P95=0.199041, P99=0.578584, max=1.000000, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
