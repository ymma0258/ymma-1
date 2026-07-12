# Risk Matrix Export Report

## Model

- Model: `graphsage`; split: `B`; seed: `0`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_splitB_seed0_epochs50_paper_comparison_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6289, MAE=0.6447, QWK=0.7860, Recall@6-8=0.9250.
- `data_2021_train`: Macro-F1=0.7521, MAE=0.4646, QWK=0.8477, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.4555, MAE=0.9790, QWK=0.7557, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.3437, MAE=1.1105, QWK=0.3393, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018177, P75=0.004077, P90=0.008541, P95=0.077231, P99=0.428098, max=0.925564, zero_ratio=0.000151.
- `data_2021`: edges=7647, mean=0.015195, P75=0.003747, P90=0.008377, P95=0.072833, P99=0.364366, max=0.856147, zero_ratio=0.000785.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
