# Risk Matrix Export Report

## Model

- Model: `edge_gat`; split: `B`; seed: `5`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6008, MAE=0.9820, QWK=0.6756, Recall@6-8=0.7000.
- `data_2021_train`: Macro-F1=0.7731, MAE=0.8726, QWK=0.7689, Recall@6-8=0.8000.
- `data_2021_test`: Macro-F1=0.3290, MAE=1.3553, QWK=0.2777, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.022202, P75=0.003891, P90=0.008522, P95=0.153046, P99=0.430419, max=0.911739, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.019143, P75=0.003715, P90=0.008052, P95=0.132217, P99=0.394678, max=0.852576, zero_ratio=0.000131.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
