# Risk Matrix Export Report

## Model

- Model: `sgformer_adapted`; split: `B`; seed: `6`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_adapted_splitB_seed6_epochs50_paper_strong_baselines_10seed.pt`; selected epoch: `26`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4193, MAE=1.2272, QWK=0.5433, Recall@6-8=0.6250.
- `data_2021_train`: Macro-F1=0.5177, MAE=1.1312, QWK=0.5774, Recall@6-8=0.7000.
- `data_2021_val`: Macro-F1=0.3717, MAE=1.4089, QWK=0.5968, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2866, MAE=1.5104, QWK=0.3531, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.023460, P75=0.004458, P90=0.008537, P95=0.148078, P99=0.455021, max=0.901938, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.021342, P75=0.004390, P90=0.008201, P95=0.134885, P99=0.427726, max=0.853007, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
