# Risk Matrix Export Report

## Model

- Model: `teg_gnn`; split: `B`; seed: `9`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5822, MAE=1.1517, QWK=0.6164, Recall@6-8=0.6250.
- `data_2021_train`: Macro-F1=0.7636, MAE=0.9216, QWK=0.8131, Recall@6-8=0.9200.
- `data_2021_test`: Macro-F1=0.2597, MAE=1.6199, QWK=0.2521, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019816, P75=0.004667, P90=0.008522, P95=0.086428, P99=0.430507, max=0.894198, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017464, P75=0.004676, P90=0.008289, P95=0.079302, P99=0.418586, max=0.855834, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
