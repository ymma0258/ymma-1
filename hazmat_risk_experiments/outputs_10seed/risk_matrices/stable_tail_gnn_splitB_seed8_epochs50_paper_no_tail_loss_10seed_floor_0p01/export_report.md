# Risk Matrix Export Report

## Model

- Model: `stable_tail_gnn`; split: `B`; seed: `8`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gnn_splitB_seed8_epochs50_paper_no_tail_loss_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3070, MAE=0.8578, QWK=0.3862, Recall@6-8=0.2750.
- `data_2021_train`: Macro-F1=0.4454, MAE=0.6951, QWK=0.3517, Recall@6-8=0.2500.
- `data_2021_val`: Macro-F1=0.3750, MAE=1.1643, QWK=0.4449, Recall@6-8=0.2000.
- `data_2021_test`: Macro-F1=0.2142, MAE=1.1535, QWK=0.2489, Recall@6-8=0.1923.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.014630, P75=0.002876, P90=0.005918, P95=0.067122, P99=0.373146, max=0.775092, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.013047, P75=0.002917, P90=0.005545, P95=0.056580, P99=0.342390, max=0.765255, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
