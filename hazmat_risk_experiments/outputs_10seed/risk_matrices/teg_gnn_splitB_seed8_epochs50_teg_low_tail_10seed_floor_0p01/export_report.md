# Risk Matrix Export Report

## Model

- Model: `teg_gnn`; split: `B`; seed: `8`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5396, MAE=1.2427, QWK=0.6364, Recall@6-8=0.6500.
- `data_2021_train`: Macro-F1=0.7325, MAE=1.0163, QWK=0.7485, Recall@6-8=0.7200.
- `data_2021_test`: Macro-F1=0.2905, MAE=1.5594, QWK=0.3939, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020063, P75=0.004813, P90=0.008571, P95=0.100287, P99=0.432687, max=0.968340, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017992, P75=0.004686, P90=0.008569, P95=0.085789, P99=0.398078, max=0.927195, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
