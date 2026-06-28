# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `B`; seed: `8`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4639, MAE=0.7484, QWK=0.6555, Recall@6-8=0.6500.
- `data_2021_train`: Macro-F1=0.5863, MAE=0.5778, QWK=0.8247, Recall@6-8=0.8800.
- `data_2021_test`: Macro-F1=0.2325, MAE=1.1968, QWK=0.1929, Recall@6-8=0.1538.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.017271, P75=0.003324, P90=0.008603, P95=0.071882, P99=0.433493, max=0.895263, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.014695, P75=0.003060, P90=0.008326, P95=0.061076, P99=0.420465, max=0.869568, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
