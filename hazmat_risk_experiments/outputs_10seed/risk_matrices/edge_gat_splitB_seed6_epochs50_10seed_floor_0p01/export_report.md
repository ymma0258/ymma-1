# Risk Matrix Export Report

## Model

- Model: `edge_gat`; split: `B`; seed: `6`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5647, MAE=0.9751, QWK=0.6131, Recall@6-8=0.6500.
- `data_2021_train`: Macro-F1=0.7121, MAE=0.8301, QWK=0.7438, Recall@6-8=0.8000.
- `data_2021_test`: Macro-F1=0.3089, MAE=1.3250, QWK=0.3670, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021048, P75=0.003921, P90=0.008406, P95=0.134506, P99=0.425273, max=0.910065, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.019832, P75=0.004006, P90=0.008189, P95=0.128028, P99=0.413535, max=0.852055, zero_ratio=0.000262.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
