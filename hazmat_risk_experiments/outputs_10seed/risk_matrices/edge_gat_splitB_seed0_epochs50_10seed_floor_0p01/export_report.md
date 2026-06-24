# Risk Matrix Export Report

## Model

- Model: `edge_gat`; split: `B`; seed: `0`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6094, MAE=0.8789, QWK=0.7238, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.7595, MAE=0.6748, QWK=0.8042, Recall@6-8=0.8800.
- `data_2021_test`: Macro-F1=0.2941, MAE=1.2457, QWK=0.2930, Recall@6-8=0.1923.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019971, P75=0.003625, P90=0.008572, P95=0.112572, P99=0.432871, max=0.899117, zero_ratio=0.001666.
- `data_2021`: edges=7647, mean=0.017484, P75=0.003452, P90=0.008452, P95=0.102085, P99=0.400391, max=0.858141, zero_ratio=0.002485.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
