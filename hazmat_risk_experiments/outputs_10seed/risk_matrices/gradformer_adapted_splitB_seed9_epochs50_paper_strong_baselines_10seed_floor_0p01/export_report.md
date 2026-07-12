# Risk Matrix Export Report

## Model

- Model: `gradformer_adapted`; split: `B`; seed: `9`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gradformer_adapted_splitB_seed9_epochs50_paper_strong_baselines_10seed.pt`; selected epoch: `22`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3482, MAE=1.3064, QWK=0.4684, Recall@6-8=0.4500.
- `data_2021_train`: Macro-F1=0.5299, MAE=1.0829, QWK=0.5929, Recall@6-8=0.6000.
- `data_2021_val`: Macro-F1=0.1945, MAE=1.4844, QWK=0.4435, Recall@6-8=0.2000.
- `data_2021_test`: Macro-F1=0.2083, MAE=1.5453, QWK=0.1947, Recall@6-8=0.1923.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.022086, P75=0.003763, P90=0.008090, P95=0.152475, P99=0.429194, max=0.860422, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.019373, P75=0.003564, P90=0.007758, P95=0.135425, P99=0.400643, max=0.843278, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
