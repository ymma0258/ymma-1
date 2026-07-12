# Risk Matrix Export Report

## Model

- Model: `stable_tail_gnn`; split: `B`; seed: `7`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gnn_splitB_seed7_epochs50_paper_no_tail_loss_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3491, MAE=0.7907, QWK=0.4970, Recall@6-8=0.4000.
- `data_2021_train`: Macro-F1=0.4678, MAE=0.5551, QWK=0.5989, Recall@6-8=0.5000.
- `data_2021_val`: Macro-F1=0.2222, MAE=0.9814, QWK=0.4673, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2595, MAE=1.2482, QWK=0.2661, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.016416, P75=0.003490, P90=0.006937, P95=0.064009, P99=0.396046, max=0.784249, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.015512, P75=0.003976, P90=0.006753, P95=0.048381, P99=0.397931, max=0.804139, zero_ratio=0.000262.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
