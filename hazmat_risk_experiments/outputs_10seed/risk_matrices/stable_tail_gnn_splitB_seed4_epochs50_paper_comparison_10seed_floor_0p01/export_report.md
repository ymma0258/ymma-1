# Risk Matrix Export Report

## Model

- Model: `stable_tail_gnn`; split: `B`; seed: `4`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gnn_splitB_seed4_epochs50_paper_comparison_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5257, MAE=0.7529, QWK=0.7838, Recall@6-8=0.9000.
- `data_2021_train`: Macro-F1=0.6557, MAE=0.5627, QWK=0.8765, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.2806, MAE=1.1778, QWK=0.2288, Recall@6-8=0.2000.
- `data_2021_test`: Macro-F1=0.3429, MAE=1.2402, QWK=0.3090, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019117, P75=0.003793, P90=0.008773, P95=0.081476, P99=0.443025, max=0.922787, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.016639, P75=0.003690, P90=0.008654, P95=0.069695, P99=0.417141, max=0.902442, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
