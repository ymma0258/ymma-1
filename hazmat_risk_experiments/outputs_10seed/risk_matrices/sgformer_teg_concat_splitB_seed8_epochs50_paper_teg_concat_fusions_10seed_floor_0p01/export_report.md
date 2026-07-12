# Risk Matrix Export Report

## Model

- Model: `sgformer_teg_concat`; split: `B`; seed: `8`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_teg_concat_splitB_seed8_epochs50_paper_teg_concat_fusions_10seed.pt`; selected epoch: `45`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4737, MAE=0.6429, QWK=0.8105, Recall@6-8=1.0000.
- `data_2021_train`: Macro-F1=0.6593, MAE=0.3831, QWK=0.9119, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.2761, MAE=1.2495, QWK=0.4548, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2809, MAE=1.2156, QWK=0.3629, Recall@6-8=0.3846.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018590, P75=0.004500, P90=0.008634, P95=0.069184, P99=0.436022, max=0.912795, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.015811, P75=0.004254, P90=0.008572, P95=0.067209, P99=0.408459, max=0.903532, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
