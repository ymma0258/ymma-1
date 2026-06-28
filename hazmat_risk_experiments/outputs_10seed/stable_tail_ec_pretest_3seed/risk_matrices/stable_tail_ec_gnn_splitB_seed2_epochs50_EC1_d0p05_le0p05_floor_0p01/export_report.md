# Risk Matrix Export Report

## Model

- Model: `stable_tail_ec_gnn`; split: `B`; seed: `2`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.2563, MAE=1.1474, QWK=0.4196, Recall@6-8=0.4500.
- `data_2021_train`: Macro-F1=0.2798, MAE=1.0400, QWK=0.4321, Recall@6-8=0.4400.
- `data_2021_test`: Macro-F1=0.2338, MAE=1.3345, QWK=0.2688, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019457, P75=0.004152, P90=0.007316, P95=0.119162, P99=0.383925, max=0.760248, zero_ratio=0.044374.
- `data_2021`: edges=7647, mean=0.018204, P75=0.004286, P90=0.007373, P95=0.094936, P99=0.407765, max=0.793638, zero_ratio=0.043808.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
