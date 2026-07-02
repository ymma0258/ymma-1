# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `B`; seed: `1`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\stable_tail_v2_pretest_3seed\models\checkpoints\gcn_teg_concat_splitB_seed1_epochs50_st_v2_3seed.pt`; selected epoch: `41`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3767, MAE=0.9214, QWK=0.6414, Recall@6-8=0.6750.
- `data_2021_train`: Macro-F1=0.3953, MAE=0.7346, QWK=0.6229, Recall@6-8=0.6500.
- `data_2021_val`: Macro-F1=0.2431, MAE=1.2767, QWK=0.5647, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2456, MAE=1.3305, QWK=0.2644, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020551, P75=0.003950, P90=0.008342, P95=0.097951, P99=0.435302, max=0.862706, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017481, P75=0.003978, P90=0.007970, P95=0.078475, P99=0.425550, max=0.866275, zero_ratio=0.000654.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
