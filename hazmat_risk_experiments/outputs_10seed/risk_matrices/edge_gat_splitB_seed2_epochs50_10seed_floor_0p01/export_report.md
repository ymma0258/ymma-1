# Risk Matrix Export Report

## Model

- Model: `edge_gat`; split: `B`; seed: `2`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6305, MAE=0.8997, QWK=0.6858, Recall@6-8=0.7500.
- `data_2021_train`: Macro-F1=0.6995, MAE=0.7150, QWK=0.7791, Recall@6-8=0.8400.
- `data_2021_test`: Macro-F1=0.3481, MAE=1.3036, QWK=0.2783, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020785, P75=0.003865, P90=0.008563, P95=0.121728, P99=0.435115, max=0.927841, zero_ratio=0.000606.
- `data_2021`: edges=7647, mean=0.018263, P75=0.003874, P90=0.008446, P95=0.101860, P99=0.426501, max=0.879780, zero_ratio=0.000523.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
