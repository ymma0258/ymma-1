# Risk Matrix Export Report

## Model

- Model: `graphsage_teg_concat`; split: `B`; seed: `1`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_teg_concat_splitB_seed1_epochs50_paper_teg_concat_fusions_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.2880, MAE=0.8921, QWK=0.6154, Recall@6-8=0.8250.
- `data_2021_train`: Macro-F1=0.3320, MAE=0.6813, QWK=0.7572, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.2542, MAE=1.2265, QWK=0.3861, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.1953, MAE=1.3177, QWK=0.2169, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020635, P75=0.004446, P90=0.008725, P95=0.080071, P99=0.442550, max=0.880413, zero_ratio=0.001514.
- `data_2021`: edges=7647, mean=0.016621, P75=0.003665, P90=0.008131, P95=0.059176, P99=0.410636, max=0.873807, zero_ratio=0.001700.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
