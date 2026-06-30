# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `B`; seed: `1`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\stable_tail_v2_pretest_3seed\models\checkpoints\gcn_teg_concat_splitB_seed1_epochs50_st_v1_best_3seed.pt`; selected epoch: `40`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3749, MAE=0.9619, QWK=0.6336, Recall@6-8=0.7000.
- `data_2021_train`: Macro-F1=0.3808, MAE=0.7655, QWK=0.5834, Recall@6-8=0.6000.
- `data_2021_val`: Macro-F1=0.2431, MAE=1.3130, QWK=0.5647, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2420, MAE=1.3485, QWK=0.2766, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021069, P75=0.004338, P90=0.008422, P95=0.097935, P99=0.436486, max=0.864328, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018320, P75=0.003993, P90=0.008098, P95=0.080006, P99=0.425978, max=0.866907, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
