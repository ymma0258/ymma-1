# Risk Matrix Export Report

## Model

- Model: `graphsage_teg_concat`; split: `B`; seed: `3`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_teg_concat_splitB_seed3_epochs50_paper_teg_concat_fusions_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3157, MAE=0.7246, QWK=0.7455, Recall@6-8=0.9000.
- `data_2021_train`: Macro-F1=0.3234, MAE=0.5881, QWK=0.8293, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.2767, MAE=0.9043, QWK=0.5915, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2134, MAE=1.1947, QWK=0.3183, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.017688, P75=0.004767, P90=0.007641, P95=0.075133, P99=0.405866, max=0.803696, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.015560, P75=0.003960, P90=0.006886, P95=0.058580, P99=0.390468, max=0.794154, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
