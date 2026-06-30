# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `B`; seed: `0`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\stable_tail_v2_pretest_3seed\models\checkpoints\gcn_teg_concat_splitB_seed0_epochs50_st_v2_std_3seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3017, MAE=0.9862, QWK=0.5339, Recall@6-8=0.5500.
- `data_2021_train`: Macro-F1=0.3491, MAE=1.0472, QWK=0.4294, Recall@6-8=0.4500.
- `data_2021_val`: Macro-F1=0.1899, MAE=1.5192, QWK=0.3905, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2385, MAE=1.3620, QWK=0.3560, Recall@6-8=0.3846.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.041314, P75=0.051395, P90=0.079707, P95=0.107839, P99=0.336018, max=0.769417, zero_ratio=0.000606.
- `data_2021`: edges=7647, mean=0.008760, P75=0.004168, P90=0.006734, P95=0.035255, P99=0.155024, max=0.707658, zero_ratio=0.004446.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
