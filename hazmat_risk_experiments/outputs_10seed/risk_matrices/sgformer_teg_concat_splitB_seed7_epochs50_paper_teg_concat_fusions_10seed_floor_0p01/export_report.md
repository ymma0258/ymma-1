# Risk Matrix Export Report

## Model

- Model: `sgformer_teg_concat`; split: `B`; seed: `7`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_teg_concat_splitB_seed7_epochs50_paper_teg_concat_fusions_10seed.pt`; selected epoch: `49`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4875, MAE=0.5452, QWK=0.7869, Recall@6-8=1.0000.
- `data_2021_train`: Macro-F1=0.5913, MAE=0.3110, QWK=0.8973, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.2389, MAE=1.0796, QWK=0.5149, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2150, MAE=1.4010, QWK=0.2439, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018307, P75=0.006640, P90=0.008615, P95=0.049467, P99=0.435047, max=0.895028, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.016598, P75=0.006450, P90=0.008572, P95=0.049384, P99=0.430295, max=0.873627, zero_ratio=0.000131.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
