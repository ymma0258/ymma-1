# Risk Matrix Export Report

## Model

- Model: `stable_tail_gnn`; split: `B`; seed: `5`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gnn_splitB_seed5_epochs50_paper_comparison_10seed.pt`; selected epoch: `49`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4733, MAE=0.7757, QWK=0.7230, Recall@6-8=0.8500.
- `data_2021_train`: Macro-F1=0.6174, MAE=0.5584, QWK=0.8738, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.2596, MAE=1.2907, QWK=0.2663, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.3240, MAE=1.2161, QWK=0.3895, Recall@6-8=0.4231.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019126, P75=0.003841, P90=0.008530, P95=0.085070, P99=0.438962, max=0.874067, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.014913, P75=0.003511, P90=0.007586, P95=0.066758, P99=0.381207, max=0.867312, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
