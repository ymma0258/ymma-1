# Risk Matrix Export Report

## Model

- Model: `weighted_gcn`; split: `B`; seed: `1`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5793, MAE=1.2283, QWK=0.6736, Recall@6-8=0.8000.
- `data_2021_train`: Macro-F1=0.7269, MAE=1.0995, QWK=0.8110, Recall@6-8=0.8000.
- `data_2021_test`: Macro-F1=0.2456, MAE=1.6879, QWK=0.2330, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021594, P75=0.004674, P90=0.008549, P95=0.115816, P99=0.432085, max=0.925436, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018064, P75=0.004457, P90=0.008020, P95=0.088196, P99=0.394363, max=0.855172, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
