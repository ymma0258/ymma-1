# Risk Matrix Export Report

## Model

- Model: `graphsage_teg_concat`; split: `B`; seed: `4`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_teg_concat_splitB_seed4_epochs50_paper_teg_concat_fusions_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3091, MAE=0.7940, QWK=0.7396, Recall@6-8=0.9250.
- `data_2021_train`: Macro-F1=0.3002, MAE=0.6622, QWK=0.8150, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.2230, MAE=1.1678, QWK=0.4576, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2217, MAE=1.2709, QWK=0.2531, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020030, P75=0.003957, P90=0.008937, P95=0.093055, P99=0.451305, max=0.909176, zero_ratio=0.000606.
- `data_2021`: edges=7647, mean=0.017437, P75=0.003904, P90=0.008581, P95=0.071568, P99=0.442437, max=0.909885, zero_ratio=0.000915.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
