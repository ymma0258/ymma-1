# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `B`; seed: `2`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\stable_tail_v2_pretest_3seed\models\checkpoints\gcn_teg_concat_splitB_seed2_epochs50_st_v2_3seed.pt`; selected epoch: `47`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4529, MAE=0.8425, QWK=0.6628, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.5113, MAE=0.5815, QWK=0.7873, Recall@6-8=0.8500.
- `data_2021_val`: Macro-F1=0.2562, MAE=1.4698, QWK=0.0324, Recall@6-8=0.0000.
- `data_2021_test`: Macro-F1=0.2851, MAE=1.1805, QWK=0.3349, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019392, P75=0.003931, P90=0.008436, P95=0.079398, P99=0.432179, max=0.943637, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017503, P75=0.003585, P90=0.008491, P95=0.070093, P99=0.428815, max=0.953485, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
