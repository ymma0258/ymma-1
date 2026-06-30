# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `B`; seed: `0`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\stable_tail_v2_pretest_3seed\models\checkpoints\gcn_teg_concat_splitB_seed0_epochs50_st_v1_3seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4799, MAE=0.6407, QWK=0.7544, Recall@6-8=0.8000.
- `data_2021_train`: Macro-F1=0.5706, MAE=0.5141, QWK=0.8380, Recall@6-8=0.8800.
- `data_2021_test`: Macro-F1=0.3212, MAE=1.1071, QWK=0.3031, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018306, P75=0.003473, P90=0.008543, P95=0.079441, P99=0.431998, max=0.875692, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.015652, P75=0.003444, P90=0.008376, P95=0.068652, P99=0.409259, max=0.849425, zero_ratio=0.000131.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
