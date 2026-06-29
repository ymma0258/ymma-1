# Risk Matrix Export Report

## Model

- Model: `stable_tail_ua_gnn`; split: `B`; seed: `2`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3143, MAE=1.0013, QWK=0.4950, Recall@6-8=0.5000.
- `data_2021_train`: Macro-F1=0.3595, MAE=0.8812, QWK=0.5338, Recall@6-8=0.5600.
- `data_2021_test`: Macro-F1=0.2551, MAE=1.2283, QWK=0.2891, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019920, P75=0.003973, P90=0.008258, P95=0.097689, P99=0.431985, max=0.855417, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018268, P75=0.003854, P90=0.008526, P95=0.084302, P99=0.430541, max=0.881515, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
