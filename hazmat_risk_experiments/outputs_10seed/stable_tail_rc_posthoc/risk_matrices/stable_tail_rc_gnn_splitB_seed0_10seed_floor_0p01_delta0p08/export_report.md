# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `B`; seed: `0`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4799, MAE=0.6405, QWK=0.7544, Recall@6-8=0.8000.
- `data_2021_train`: Macro-F1=0.5706, MAE=0.5142, QWK=0.8380, Recall@6-8=0.8800.
- `data_2021_test`: Macro-F1=0.3212, MAE=1.1070, QWK=0.3031, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018314, P75=0.003473, P90=0.008544, P95=0.078976, P99=0.432016, max=0.875514, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.015658, P75=0.003450, P90=0.008378, P95=0.068943, P99=0.409232, max=0.849538, zero_ratio=0.000131.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
