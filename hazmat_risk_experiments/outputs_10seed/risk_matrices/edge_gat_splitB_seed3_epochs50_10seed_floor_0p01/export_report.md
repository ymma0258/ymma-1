# Risk Matrix Export Report

## Model

- Model: `edge_gat`; split: `B`; seed: `3`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5516, MAE=0.8811, QWK=0.6941, Recall@6-8=0.7000.
- `data_2021_train`: Macro-F1=0.7158, MAE=0.6922, QWK=0.8125, Recall@6-8=0.8800.
- `data_2021_test`: Macro-F1=0.2534, MAE=1.3714, QWK=0.1688, Recall@6-8=0.0769.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020956, P75=0.003720, P90=0.008522, P95=0.124009, P99=0.432298, max=0.858287, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017804, P75=0.003570, P90=0.008511, P95=0.102770, P99=0.425537, max=0.856768, zero_ratio=0.000654.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
