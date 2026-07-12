# Risk Matrix Export Report

## Model

- Model: `sgformer_teg_gate`; split: `B`; seed: `1`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_teg_gate_splitB_seed1_epochs50_paper_teg_gate_fusions_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6936, MAE=0.6420, QWK=0.8115, Recall@6-8=1.0000.
- `data_2021_train`: Macro-F1=0.7615, MAE=0.4735, QWK=0.9092, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.3131, MAE=1.2882, QWK=0.5332, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.3230, MAE=1.3181, QWK=0.3072, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020194, P75=0.005195, P90=0.008589, P95=0.093460, P99=0.433749, max=0.941666, zero_ratio=0.000303.
- `data_2021`: edges=7647, mean=0.018456, P75=0.004753, P90=0.008480, P95=0.087336, P99=0.428092, max=0.857048, zero_ratio=0.000131.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
