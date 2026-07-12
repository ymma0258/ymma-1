# Risk Matrix Export Report

## Model

- Model: `gradformer_adapted`; split: `B`; seed: `5`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gradformer_adapted_splitB_seed5_epochs50_paper_strong_baselines_10seed.pt`; selected epoch: `44`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5766, MAE=1.0797, QWK=0.6577, Recall@6-8=0.6750.
- `data_2021_train`: Macro-F1=0.7449, MAE=0.8906, QWK=0.6547, Recall@6-8=0.6500.
- `data_2021_val`: Macro-F1=0.3822, MAE=1.3430, QWK=0.3602, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2592, MAE=1.3023, QWK=0.3166, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.022134, P75=0.004153, P90=0.008460, P95=0.148963, P99=0.432415, max=0.916121, zero_ratio=0.007118.
- `data_2021`: edges=7647, mean=0.019487, P75=0.004088, P90=0.008480, P95=0.132465, P99=0.419675, max=0.995408, zero_ratio=0.002746.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
