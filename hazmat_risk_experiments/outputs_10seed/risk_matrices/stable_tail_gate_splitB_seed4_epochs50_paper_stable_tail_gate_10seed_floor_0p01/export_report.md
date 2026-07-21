# Risk Matrix Export Report

## Model

- Model: `stable_tail_gate`; split: `B`; seed: `4`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gate_splitB_seed4_epochs50_paper_stable_tail_gate_10seed.pt`; selected epoch: `47`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4579, MAE=1.0268, QWK=0.6359, Recall@6-8=0.6500.
- `data_2021_train`: Macro-F1=0.5450, MAE=0.8477, QWK=0.6537, Recall@6-8=0.7000.
- `data_2021_val`: Macro-F1=0.2048, MAE=1.3967, QWK=0.3103, Recall@6-8=0.2000.
- `data_2021_test`: Macro-F1=0.3345, MAE=1.3811, QWK=0.2197, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020548, P75=0.003754, P90=0.008570, P95=0.126361, P99=0.432801, max=0.940217, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018815, P75=0.003638, P90=0.008571, P95=0.111342, P99=0.426326, max=0.913146, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
