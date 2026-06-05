# Risk Matrix Export Report

## Model

- Model: `teg_gnn`; split: `B`; seed: `2`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6065, MAE=1.2768, QWK=0.6666, Recall@6-8=0.7750.
- `data_2021_train`: Macro-F1=0.7255, MAE=1.1468, QWK=0.7741, Recall@6-8=0.8400.
- `data_2021_test`: Macro-F1=0.2932, MAE=1.5581, QWK=0.3525, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.022447, P75=0.005096, P90=0.008571, P95=0.132104, P99=0.433090, max=0.930088, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.020167, P75=0.004819, P90=0.008558, P95=0.113319, P99=0.422048, max=0.865354, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
