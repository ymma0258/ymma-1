# Risk Matrix Export Report

## Model

- Model: `stable_tail_ec_gnn`; split: `B`; seed: `0`; epochs: `1`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.0714, MAE=2.7966, QWK=0.0086, Recall@6-8=0.2000.
- `data_2021_train`: Macro-F1=0.0953, MAE=2.7577, QWK=0.0923, Recall@6-8=0.2000.
- `data_2021_test`: Macro-F1=0.0744, MAE=2.7884, QWK=-0.0195, Recall@6-8=0.1923.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.026858, P75=0.004920, P90=0.004952, P95=0.244147, P99=0.488832, max=0.495872, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.026102, P75=0.004918, P90=0.004948, P95=0.245010, P99=0.488427, max=0.496106, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
