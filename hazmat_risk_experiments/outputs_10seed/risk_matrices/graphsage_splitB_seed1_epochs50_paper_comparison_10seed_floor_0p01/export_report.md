# Risk Matrix Export Report

## Model

- Model: `graphsage`; split: `B`; seed: `1`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_splitB_seed1_epochs50_paper_comparison_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6921, MAE=0.5561, QWK=0.8365, Recall@6-8=0.9750.
- `data_2021_train`: Macro-F1=0.8685, MAE=0.3000, QWK=0.9568, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.3995, MAE=1.1599, QWK=0.4810, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2611, MAE=1.2339, QWK=0.2503, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018534, P75=0.003538, P90=0.008547, P95=0.071401, P99=0.432815, max=0.951028, zero_ratio=0.001363.
- `data_2021`: edges=7647, mean=0.015247, P75=0.003453, P90=0.008509, P95=0.062064, P99=0.408536, max=0.883484, zero_ratio=0.001438.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
