# Risk Matrix Export Report

## Model

- Model: `teg_gnn`; split: `B`; seed: `5`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4775, MAE=1.3420, QWK=0.5713, Recall@6-8=0.6000.
- `data_2021_train`: Macro-F1=0.6846, MAE=1.2417, QWK=0.6417, Recall@6-8=0.6800.
- `data_2021_test`: Macro-F1=0.2808, MAE=1.5877, QWK=0.3906, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020871, P75=0.004556, P90=0.008554, P95=0.107879, P99=0.431985, max=0.860549, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017257, P75=0.004459, P90=0.008338, P95=0.099268, P99=0.346385, max=0.853326, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
