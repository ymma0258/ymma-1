# Risk Matrix Export Report

## Model

- Model: `stable_tail_gnn`; split: `B`; seed: `0`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gnn_splitB_seed0_epochs50_paper_comparison_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4872, MAE=0.6687, QWK=0.7802, Recall@6-8=0.9000.
- `data_2021_train`: Macro-F1=0.5348, MAE=0.4884, QWK=0.8666, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.3879, MAE=1.0215, QWK=0.5353, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.3273, MAE=1.1339, QWK=0.2854, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018522, P75=0.003792, P90=0.008636, P95=0.084419, P99=0.436544, max=0.899607, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.015311, P75=0.003474, P90=0.008297, P95=0.064955, P99=0.396516, max=0.865141, zero_ratio=0.000131.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
