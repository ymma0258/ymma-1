# Risk Matrix Export Report

## Model

- Model: `edge_gat`; split: `B`; seed: `8`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6148, MAE=0.8514, QWK=0.7086, Recall@6-8=0.7500.
- `data_2021_train`: Macro-F1=0.7471, MAE=0.6846, QWK=0.8552, Recall@6-8=0.8800.
- `data_2021_test`: Macro-F1=0.2819, MAE=1.2898, QWK=0.2735, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019631, P75=0.003596, P90=0.008500, P95=0.118440, P99=0.429273, max=0.953539, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017658, P75=0.003659, P90=0.008344, P95=0.101719, P99=0.415104, max=0.861582, zero_ratio=0.000785.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
