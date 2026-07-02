# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `B`; seed: `1`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\stable_tail_v2_pretest_3seed\models\checkpoints\gcn_teg_concat_splitB_seed1_epochs50_st_v2_std_3seed.pt`; selected epoch: `40`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.1996, MAE=1.2847, QWK=0.2289, Recall@6-8=0.2250.
- `data_2021_train`: Macro-F1=0.2567, MAE=1.2791, QWK=0.4265, Recall@6-8=0.4500.
- `data_2021_val`: Macro-F1=0.1967, MAE=1.4689, QWK=0.5308, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.1519, MAE=1.5068, QWK=0.1188, Recall@6-8=0.1538.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.045039, P75=0.046198, P90=0.091594, P95=0.120574, P99=0.349273, max=0.801699, zero_ratio=0.002272.
- `data_2021`: edges=7647, mean=0.008341, P75=0.003591, P90=0.006261, P95=0.028102, P99=0.159478, max=0.841826, zero_ratio=0.004054.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
