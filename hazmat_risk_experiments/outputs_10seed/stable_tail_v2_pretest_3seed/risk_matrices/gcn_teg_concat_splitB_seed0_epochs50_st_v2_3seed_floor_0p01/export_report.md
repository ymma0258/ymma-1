# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `B`; seed: `0`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\stable_tail_v2_pretest_3seed\models\checkpoints\gcn_teg_concat_splitB_seed0_epochs50_st_v2_3seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4804, MAE=0.6563, QWK=0.7773, Recall@6-8=0.8500.
- `data_2021_train`: Macro-F1=0.4995, MAE=0.4559, QWK=0.8841, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.4280, MAE=1.0044, QWK=0.6221, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.3181, MAE=1.1223, QWK=0.2728, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018815, P75=0.003724, P90=0.008407, P95=0.081538, P99=0.434239, max=0.860808, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.015162, P75=0.003454, P90=0.008173, P95=0.070040, P99=0.397786, max=0.852205, zero_ratio=0.000131.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
