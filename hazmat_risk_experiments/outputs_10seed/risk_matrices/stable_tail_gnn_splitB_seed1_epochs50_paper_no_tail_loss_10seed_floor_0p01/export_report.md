# Risk Matrix Export Report

## Model

- Model: `stable_tail_gnn`; split: `B`; seed: `1`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gnn_splitB_seed1_epochs50_paper_no_tail_loss_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.2919, MAE=0.8118, QWK=0.5005, Recall@6-8=0.5000.
- `data_2021_train`: Macro-F1=0.3437, MAE=0.6482, QWK=0.4939, Recall@6-8=0.4500.
- `data_2021_val`: Macro-F1=0.2199, MAE=1.1304, QWK=0.3885, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2198, MAE=1.1816, QWK=0.2835, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.017095, P75=0.003247, P90=0.007732, P95=0.063361, P99=0.419488, max=0.840127, zero_ratio=0.001514.
- `data_2021`: edges=7647, mean=0.015009, P75=0.003406, P90=0.007564, P95=0.045128, P99=0.414484, max=0.832004, zero_ratio=0.001308.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
