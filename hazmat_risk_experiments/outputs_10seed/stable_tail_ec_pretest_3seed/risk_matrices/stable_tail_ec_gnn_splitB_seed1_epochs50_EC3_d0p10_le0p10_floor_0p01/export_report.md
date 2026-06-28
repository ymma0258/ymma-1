# Risk Matrix Export Report

## Model

- Model: `stable_tail_ec_gnn`; split: `B`; seed: `1`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.2518, MAE=1.0990, QWK=0.5150, Recall@6-8=0.6000.
- `data_2021_train`: Macro-F1=0.2559, MAE=1.0300, QWK=0.4852, Recall@6-8=0.5200.
- `data_2021_test`: Macro-F1=0.1996, MAE=1.3580, QWK=0.2628, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019356, P75=0.004473, P90=0.007407, P95=0.096226, P99=0.471979, max=0.778276, zero_ratio=0.102226.
- `data_2021`: edges=7647, mean=0.017882, P75=0.004496, P90=0.007036, P95=0.081307, P99=0.445233, max=0.783646, zero_ratio=0.090624.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
