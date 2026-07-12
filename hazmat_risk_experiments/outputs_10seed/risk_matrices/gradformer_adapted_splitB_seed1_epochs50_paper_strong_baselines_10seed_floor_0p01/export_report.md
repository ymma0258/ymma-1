# Risk Matrix Export Report

## Model

- Model: `gradformer_adapted`; split: `B`; seed: `1`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gradformer_adapted_splitB_seed1_epochs50_paper_strong_baselines_10seed.pt`; selected epoch: `33`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3700, MAE=1.1673, QWK=0.4017, Recall@6-8=0.3750.
- `data_2021_train`: Macro-F1=0.5374, MAE=1.0275, QWK=0.4573, Recall@6-8=0.4500.
- `data_2021_val`: Macro-F1=0.2947, MAE=1.3782, QWK=0.3910, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2494, MAE=1.4077, QWK=0.2251, Recall@6-8=0.1538.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019911, P75=0.003700, P90=0.007848, P95=0.136461, P99=0.407773, max=0.856404, zero_ratio=0.011056.
- `data_2021`: edges=7647, mean=0.018256, P75=0.003573, P90=0.006609, P95=0.113867, P99=0.400166, max=0.855549, zero_ratio=0.005492.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
