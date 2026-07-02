# Risk Matrix Export Report

## Model

- Model: `stable_tail_ec_gnn`; split: `B`; seed: `0`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.2660, MAE=1.0822, QWK=0.4824, Recall@6-8=0.4750.
- `data_2021_train`: Macro-F1=0.3213, MAE=1.0042, QWK=0.4669, Recall@6-8=0.4400.
- `data_2021_test`: Macro-F1=0.2327, MAE=1.2878, QWK=0.3600, Recall@6-8=0.3846.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018202, P75=0.003861, P90=0.006981, P95=0.108211, P99=0.394150, max=0.780496, zero_ratio=0.094200.
- `data_2021`: edges=7647, mean=0.017207, P75=0.003882, P90=0.007282, P95=0.091514, P99=0.400504, max=0.793077, zero_ratio=0.085262.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
