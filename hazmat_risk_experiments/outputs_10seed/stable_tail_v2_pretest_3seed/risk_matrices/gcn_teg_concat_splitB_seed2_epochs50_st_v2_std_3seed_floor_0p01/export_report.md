# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `B`; seed: `2`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\stable_tail_v2_pretest_3seed\models\checkpoints\gcn_teg_concat_splitB_seed2_epochs50_st_v2_std_3seed.pt`; selected epoch: `1`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.0896, MAE=2.8467, QWK=0.0225, Recall@6-8=0.2250.
- `data_2021_train`: Macro-F1=0.0879, MAE=2.8105, QWK=0.1733, Recall@6-8=0.2500.
- `data_2021_val`: Macro-F1=0.0892, MAE=2.9603, QWK=0.2352, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.0676, MAE=2.8518, QWK=0.1541, Recall@6-8=0.1923.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.077599, P75=0.063654, P90=0.066878, P95=0.206873, P99=0.356516, max=0.519153, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.014165, P75=0.005019, P90=0.005475, P95=0.090432, P99=0.184056, max=0.501881, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
