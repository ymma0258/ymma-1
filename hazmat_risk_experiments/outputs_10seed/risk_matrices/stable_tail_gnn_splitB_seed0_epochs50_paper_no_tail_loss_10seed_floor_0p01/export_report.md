# Risk Matrix Export Report

## Model

- Model: `stable_tail_gnn`; split: `B`; seed: `0`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gnn_splitB_seed0_epochs50_paper_no_tail_loss_10seed.pt`; selected epoch: `49`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3647, MAE=0.7672, QWK=0.5315, Recall@6-8=0.4500.
- `data_2021_train`: Macro-F1=0.4097, MAE=0.5872, QWK=0.5027, Recall@6-8=0.4000.
- `data_2021_val`: Macro-F1=0.2064, MAE=0.9492, QWK=0.6104, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2757, MAE=1.0662, QWK=0.3654, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.015953, P75=0.003041, P90=0.007770, P95=0.075317, P99=0.392382, max=0.833419, zero_ratio=0.000151.
- `data_2021`: edges=7647, mean=0.014439, P75=0.003011, P90=0.006517, P95=0.062832, P99=0.386557, max=0.844414, zero_ratio=0.000654.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
