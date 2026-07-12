# Risk Matrix Export Report

## Model

- Model: `sgformer_teg_concat`; split: `B`; seed: `3`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_teg_concat_splitB_seed3_epochs50_paper_teg_concat_fusions_10seed.pt`; selected epoch: `45`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5356, MAE=0.5109, QWK=0.7925, Recall@6-8=0.9250.
- `data_2021_train`: Macro-F1=0.8010, MAE=0.3156, QWK=0.9224, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.2313, MAE=0.9838, QWK=0.4121, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2794, MAE=1.1694, QWK=0.2654, Recall@6-8=0.1538.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018629, P75=0.004699, P90=0.008862, P95=0.057239, P99=0.450414, max=0.924130, zero_ratio=0.000454.
- `data_2021`: edges=7647, mean=0.015061, P75=0.004303, P90=0.008458, P95=0.049338, P99=0.414034, max=0.902014, zero_ratio=0.000523.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
