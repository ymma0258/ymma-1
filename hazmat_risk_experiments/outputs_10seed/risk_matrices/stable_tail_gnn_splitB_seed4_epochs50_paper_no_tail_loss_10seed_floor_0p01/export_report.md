# Risk Matrix Export Report

## Model

- Model: `stable_tail_gnn`; split: `B`; seed: `4`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gnn_splitB_seed4_epochs50_paper_no_tail_loss_10seed.pt`; selected epoch: `30`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.2277, MAE=1.0682, QWK=0.1211, Recall@6-8=0.0750.
- `data_2021_train`: Macro-F1=0.3440, MAE=1.0408, QWK=0.3101, Recall@6-8=0.2500.
- `data_2021_val`: Macro-F1=0.1750, MAE=1.2092, QWK=0.2203, Recall@6-8=0.0000.
- `data_2021_test`: Macro-F1=0.1930, MAE=1.2704, QWK=0.0800, Recall@6-8=0.0769.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.014995, P75=0.002660, P90=0.007361, P95=0.079086, P99=0.371720, max=0.812088, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.014527, P75=0.002767, P90=0.008195, P95=0.080500, P99=0.359574, max=0.821943, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
