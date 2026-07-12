# Risk Matrix Export Report

## Model

- Model: `sgformer_teg_concat`; split: `B`; seed: `2`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_teg_concat_splitB_seed2_epochs50_paper_teg_concat_fusions_10seed.pt`; selected epoch: `43`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4715, MAE=0.7323, QWK=0.7222, Recall@6-8=0.8750.
- `data_2021_train`: Macro-F1=0.5551, MAE=0.5691, QWK=0.8081, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.2182, MAE=1.4357, QWK=-0.0668, Recall@6-8=0.0000.
- `data_2021_test`: Macro-F1=0.2842, MAE=1.1402, QWK=0.4260, Recall@6-8=0.5000.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019676, P75=0.005050, P90=0.008601, P95=0.066943, P99=0.442021, max=0.909143, zero_ratio=0.000151.
- `data_2021`: edges=7647, mean=0.017492, P75=0.005060, P90=0.008545, P95=0.056145, P99=0.433920, max=0.872846, zero_ratio=0.000262.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
