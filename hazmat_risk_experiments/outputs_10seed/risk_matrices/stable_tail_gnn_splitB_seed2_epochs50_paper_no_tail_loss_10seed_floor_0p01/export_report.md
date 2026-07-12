# Risk Matrix Export Report

## Model

- Model: `stable_tail_gnn`; split: `B`; seed: `2`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gnn_splitB_seed2_epochs50_paper_no_tail_loss_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3403, MAE=0.8249, QWK=0.4047, Recall@6-8=0.3500.
- `data_2021_train`: Macro-F1=0.4376, MAE=0.6109, QWK=0.5315, Recall@6-8=0.4000.
- `data_2021_val`: Macro-F1=0.2575, MAE=1.3549, QWK=-0.1191, Recall@6-8=0.0000.
- `data_2021_test`: Macro-F1=0.2263, MAE=1.1190, QWK=0.1664, Recall@6-8=0.1154.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.016531, P75=0.003098, P90=0.008109, P95=0.070411, P99=0.417113, max=0.866256, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.015649, P75=0.002901, P90=0.007784, P95=0.056672, P99=0.393085, max=0.907593, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
