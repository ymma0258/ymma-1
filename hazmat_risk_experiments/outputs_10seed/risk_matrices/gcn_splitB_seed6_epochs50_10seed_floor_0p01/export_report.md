# Risk Matrix Export Report

## Model

- Model: `gcn`; split: `B`; seed: `6`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6361, MAE=0.8695, QWK=0.6712, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.7999, MAE=0.7359, QWK=0.8003, Recall@6-8=0.8800.
- `data_2021_test`: Macro-F1=0.3335, MAE=1.2248, QWK=0.3080, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020341, P75=0.003624, P90=0.008491, P95=0.123455, P99=0.428775, max=0.882254, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018267, P75=0.003760, P90=0.008289, P95=0.098823, P99=0.419894, max=0.854266, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
