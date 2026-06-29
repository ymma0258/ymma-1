# Risk Matrix Export Report

## Model

- Model: `stable_tail_ec_gnn`; split: `B`; seed: `0`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.2660, MAE=1.0824, QWK=0.4824, Recall@6-8=0.4750.
- `data_2021_train`: Macro-F1=0.3213, MAE=1.0045, QWK=0.4669, Recall@6-8=0.4400.
- `data_2021_test`: Macro-F1=0.2319, MAE=1.2880, QWK=0.3610, Recall@6-8=0.3846.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018631, P75=0.003956, P90=0.006939, P95=0.115242, P99=0.388578, max=0.769460, zero_ratio=0.046191.
- `data_2021`: edges=7647, mean=0.017647, P75=0.003969, P90=0.007771, P95=0.099920, P99=0.397140, max=0.782406, zero_ratio=0.042239.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
