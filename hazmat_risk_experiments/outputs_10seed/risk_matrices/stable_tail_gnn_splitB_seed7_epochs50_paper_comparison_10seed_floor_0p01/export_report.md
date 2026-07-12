# Risk Matrix Export Report

## Model

- Model: `stable_tail_gnn`; split: `B`; seed: `7`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gnn_splitB_seed7_epochs50_paper_comparison_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5297, MAE=0.7002, QWK=0.7878, Recall@6-8=0.9250.
- `data_2021_train`: Macro-F1=0.6831, MAE=0.4010, QWK=0.8861, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.2494, MAE=1.0418, QWK=0.4335, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.3120, MAE=1.3305, QWK=0.2069, Recall@6-8=0.1923.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019314, P75=0.004801, P90=0.008675, P95=0.071370, P99=0.441193, max=0.891243, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017005, P75=0.004457, P90=0.008460, P95=0.059718, P99=0.422413, max=0.869753, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
