# Risk Matrix Export Report

## Model

- Model: `stable_tail_gnn`; split: `B`; seed: `3`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gnn_splitB_seed3_epochs50_paper_no_tail_loss_10seed.pt`; selected epoch: `48`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4470, MAE=0.8180, QWK=0.4551, Recall@6-8=0.3250.
- `data_2021_train`: Macro-F1=0.5755, MAE=0.6427, QWK=0.5018, Recall@6-8=0.4000.
- `data_2021_val`: Macro-F1=0.3075, MAE=1.0537, QWK=0.5765, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2435, MAE=1.2075, QWK=0.1691, Recall@6-8=0.0385.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.014961, P75=0.003006, P90=0.006903, P95=0.067447, P99=0.355225, max=0.825554, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.013429, P75=0.003067, P90=0.005810, P95=0.063660, P99=0.339811, max=0.830861, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
