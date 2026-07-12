# Risk Matrix Export Report

## Model

- Model: `sgformer_teg_concat`; split: `B`; seed: `1`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_teg_concat_splitB_seed1_epochs50_paper_teg_concat_fusions_10seed.pt`; selected epoch: `47`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5627, MAE=0.5671, QWK=0.8021, Recall@6-8=0.9750.
- `data_2021_train`: Macro-F1=0.6867, MAE=0.3580, QWK=0.9135, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.2734, MAE=1.2197, QWK=0.5644, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2632, MAE=1.2463, QWK=0.3482, Recall@6-8=0.3846.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.017748, P75=0.004148, P90=0.008725, P95=0.069824, P99=0.440616, max=0.916072, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.016264, P75=0.004053, P90=0.008673, P95=0.058896, P99=0.432212, max=0.895887, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
