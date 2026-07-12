# Risk Matrix Export Report

## Model

- Model: `stable_tail_gnn`; split: `B`; seed: `5`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gnn_splitB_seed5_epochs50_paper_no_tail_loss_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3205, MAE=0.8265, QWK=0.3709, Recall@6-8=0.2500.
- `data_2021_train`: Macro-F1=0.4279, MAE=0.7206, QWK=0.3980, Recall@6-8=0.2500.
- `data_2021_val`: Macro-F1=0.2703, MAE=1.1847, QWK=0.3250, Recall@6-8=0.2000.
- `data_2021_test`: Macro-F1=0.2702, MAE=1.1045, QWK=0.2275, Recall@6-8=0.1538.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.016016, P75=0.003149, P90=0.006830, P95=0.075701, P99=0.381229, max=0.803629, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.014251, P75=0.003245, P90=0.006011, P95=0.063287, P99=0.384516, max=0.799533, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
