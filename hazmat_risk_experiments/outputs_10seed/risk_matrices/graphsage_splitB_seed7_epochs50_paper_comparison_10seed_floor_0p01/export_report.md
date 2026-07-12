# Risk Matrix Export Report

## Model

- Model: `graphsage`; split: `B`; seed: `7`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_splitB_seed7_epochs50_paper_comparison_10seed.pt`; selected epoch: `48`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6704, MAE=0.6114, QWK=0.8345, Recall@6-8=0.9000.
- `data_2021_train`: Macro-F1=0.8727, MAE=0.3192, QWK=0.9603, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.2312, MAE=1.0983, QWK=0.5096, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.3184, MAE=1.4025, QWK=0.2323, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020948, P75=0.005212, P90=0.008605, P95=0.092016, P99=0.434577, max=0.959785, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018388, P75=0.004783, P90=0.008571, P95=0.077293, P99=0.431016, max=0.912341, zero_ratio=0.000131.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
