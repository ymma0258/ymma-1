# Risk Matrix Export Report

## Model

- Model: `stable_tail_gnn`; split: `B`; seed: `9`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gnn_splitB_seed9_epochs50_paper_no_tail_loss_10seed.pt`; selected epoch: `36`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.2974, MAE=0.9271, QWK=0.3933, Recall@6-8=0.3250.
- `data_2021_train`: Macro-F1=0.3599, MAE=0.7883, QWK=0.3680, Recall@6-8=0.3000.
- `data_2021_val`: Macro-F1=0.2466, MAE=1.2811, QWK=0.4221, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2375, MAE=1.2301, QWK=0.1475, Recall@6-8=0.1154.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.015646, P75=0.003043, P90=0.005974, P95=0.084908, P99=0.343307, max=0.679816, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.014325, P75=0.003123, P90=0.005461, P95=0.069457, P99=0.354892, max=0.702757, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
