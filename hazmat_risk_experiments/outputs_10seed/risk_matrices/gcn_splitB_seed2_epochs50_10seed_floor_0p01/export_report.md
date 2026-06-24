# Risk Matrix Export Report

## Model

- Model: `gcn`; split: `B`; seed: `2`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6148, MAE=0.8945, QWK=0.6694, Recall@6-8=0.7500.
- `data_2021_train`: Macro-F1=0.7621, MAE=0.7057, QWK=0.7969, Recall@6-8=0.8800.
- `data_2021_test`: Macro-F1=0.3107, MAE=1.2808, QWK=0.3267, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021392, P75=0.004042, P90=0.008534, P95=0.129519, P99=0.432279, max=0.956108, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.019261, P75=0.003916, P90=0.008522, P95=0.111578, P99=0.428953, max=0.895764, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
