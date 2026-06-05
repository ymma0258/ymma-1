# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `B`; seed: `9`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5171, MAE=0.7296, QWK=0.6918, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.7123, MAE=0.5423, QWK=0.8173, Recall@6-8=0.9200.
- `data_2021_test`: Macro-F1=0.2857, MAE=1.3013, QWK=0.2070, Recall@6-8=0.1538.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018739, P75=0.003642, P90=0.008717, P95=0.084816, P99=0.440154, max=0.880582, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.016510, P75=0.003683, P90=0.008518, P95=0.068984, P99=0.425982, max=0.877844, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
