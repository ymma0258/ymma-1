# Risk Matrix Export Report

## Model

- Model: `gcn`; split: `B`; seed: `1`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5732, MAE=0.8324, QWK=0.6971, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.7007, MAE=0.6850, QWK=0.7975, Recall@6-8=0.8000.
- `data_2021_test`: Macro-F1=0.2939, MAE=1.3347, QWK=0.2922, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020398, P75=0.003573, P90=0.008495, P95=0.115379, P99=0.432367, max=0.887933, zero_ratio=0.001363.
- `data_2021`: edges=7647, mean=0.017088, P75=0.003612, P90=0.008345, P95=0.099877, P99=0.396196, max=0.854480, zero_ratio=0.001438.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
