# Risk Matrix Export Report

## Model

- Model: `weighted_gcn`; split: `B`; seed: `8`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5758, MAE=1.2370, QWK=0.7423, Recall@6-8=0.8250.
- `data_2021_train`: Macro-F1=0.7426, MAE=1.0249, QWK=0.7850, Recall@6-8=0.8000.
- `data_2021_test`: Macro-F1=0.2805, MAE=1.5678, QWK=0.3584, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020107, P75=0.004922, P90=0.008581, P95=0.097713, P99=0.431804, max=0.946054, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017340, P75=0.004700, P90=0.008468, P95=0.081197, P99=0.405892, max=0.857347, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
