# Risk Matrix Export Report

## Model

- Model: `gcn`; split: `B`; seed: `5`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gcn_splitB_seed5_epochs50_paper_comparison_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6542, MAE=0.8000, QWK=0.7350, Recall@6-8=0.7750.
- `data_2021_train`: Macro-F1=0.8236, MAE=0.5863, QWK=0.8767, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.3165, MAE=1.5159, QWK=0.2150, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2979, MAE=1.2456, QWK=0.3685, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020609, P75=0.003706, P90=0.008471, P95=0.122810, P99=0.436234, max=0.866741, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.016968, P75=0.003478, P90=0.007667, P95=0.096761, P99=0.387701, max=0.864340, zero_ratio=0.000262.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
