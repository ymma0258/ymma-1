# Risk Matrix Export Report

## Model

- Model: `weighted_gcn`; split: `B`; seed: `4`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6279, MAE=1.3210, QWK=0.6868, Recall@6-8=0.8000.
- `data_2021_train`: Macro-F1=0.7433, MAE=1.1076, QWK=0.8163, Recall@6-8=0.8400.
- `data_2021_test`: Macro-F1=0.2973, MAE=1.6959, QWK=0.2326, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021753, P75=0.004964, P90=0.008559, P95=0.114483, P99=0.434114, max=0.919759, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.019442, P75=0.004880, P90=0.008171, P95=0.102905, P99=0.412617, max=0.861015, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
