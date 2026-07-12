# Risk Matrix Export Report

## Model

- Model: `gradformer_adapted`; split: `B`; seed: `8`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gradformer_adapted_splitB_seed8_epochs50_paper_strong_baselines_10seed.pt`; selected epoch: `48`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5094, MAE=1.0032, QWK=0.6420, Recall@6-8=0.6500.
- `data_2021_train`: Macro-F1=0.6692, MAE=0.7077, QWK=0.5964, Recall@6-8=0.5500.
- `data_2021_val`: Macro-F1=0.3248, MAE=1.3427, QWK=0.6103, Recall@6-8=0.8000.
- `data_2021_test`: Macro-F1=0.2999, MAE=1.3056, QWK=0.3345, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019924, P75=0.004438, P90=0.008252, P95=0.123289, P99=0.431459, max=0.896952, zero_ratio=0.016659.
- `data_2021`: edges=7647, mean=0.018144, P75=0.004382, P90=0.008157, P95=0.103923, P99=0.430038, max=0.856859, zero_ratio=0.009023.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
