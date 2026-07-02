# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `B`; seed: `0`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\stable_tail_v2_pretest_3seed\models\checkpoints\gcn_teg_concat_splitB_seed0_epochs50_st_v1_best_3seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4663, MAE=0.6606, QWK=0.7266, Recall@6-8=0.8000.
- `data_2021_train`: Macro-F1=0.4941, MAE=0.4710, QWK=0.8475, Recall@6-8=0.9000.
- `data_2021_val`: Macro-F1=0.4232, MAE=0.9424, QWK=0.6395, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.3069, MAE=1.1056, QWK=0.2719, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018440, P75=0.003810, P90=0.008551, P95=0.077959, P99=0.432263, max=0.893675, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.015088, P75=0.003336, P90=0.008063, P95=0.065688, P99=0.378607, max=0.852339, zero_ratio=0.000392.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
