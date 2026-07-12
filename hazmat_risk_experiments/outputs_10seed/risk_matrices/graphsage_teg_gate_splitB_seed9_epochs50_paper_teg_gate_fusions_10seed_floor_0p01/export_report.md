# Risk Matrix Export Report

## Model

- Model: `graphsage_teg_gate`; split: `B`; seed: `9`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_teg_gate_splitB_seed9_epochs50_paper_teg_gate_fusions_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3224, MAE=0.7946, QWK=0.6181, Recall@6-8=0.7000.
- `data_2021_train`: Macro-F1=0.4098, MAE=0.5452, QWK=0.8037, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.1919, MAE=1.3817, QWK=0.1308, Recall@6-8=0.2000.
- `data_2021_test`: Macro-F1=0.2453, MAE=1.3151, QWK=0.1836, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020179, P75=0.003599, P90=0.008828, P95=0.100680, P99=0.455724, max=0.902456, zero_ratio=0.000909.
- `data_2021`: edges=7647, mean=0.016810, P75=0.003644, P90=0.007792, P95=0.082987, P99=0.433706, max=0.901860, zero_ratio=0.001046.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
