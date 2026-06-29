# Risk Matrix Export Report

## Model

- Model: `stable_tail_ec_gnn`; split: `B`; seed: `2`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.2563, MAE=1.1472, QWK=0.4196, Recall@6-8=0.4500.
- `data_2021_train`: Macro-F1=0.2798, MAE=1.0399, QWK=0.4321, Recall@6-8=0.4400.
- `data_2021_test`: Macro-F1=0.2338, MAE=1.3344, QWK=0.2688, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018743, P75=0.004099, P90=0.007130, P95=0.109849, P99=0.372707, max=0.738034, zero_ratio=0.101469.
- `data_2021`: edges=7647, mean=0.017521, P75=0.004170, P90=0.007112, P95=0.087281, P99=0.402523, max=0.766909, zero_ratio=0.089055.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
