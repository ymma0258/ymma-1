# Risk Matrix Export Report

## Model

- Model: `graphsage_teg_concat`; split: `B`; seed: `6`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_teg_concat_splitB_seed6_epochs50_paper_teg_concat_fusions_10seed.pt`; selected epoch: `45`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.2833, MAE=0.9460, QWK=0.5925, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.3115, MAE=0.9076, QWK=0.5775, Recall@6-8=0.7500.
- `data_2021_val`: Macro-F1=0.2222, MAE=1.1425, QWK=0.6806, Recall@6-8=0.8000.
- `data_2021_test`: Macro-F1=0.2183, MAE=1.2221, QWK=0.3882, Recall@6-8=0.4231.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020032, P75=0.004644, P90=0.007561, P95=0.092884, P99=0.443962, max=0.801797, zero_ratio=0.000151.
- `data_2021`: edges=7647, mean=0.017842, P75=0.004612, P90=0.007507, P95=0.069622, P99=0.393502, max=0.819968, zero_ratio=0.000785.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
