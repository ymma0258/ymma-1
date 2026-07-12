# Risk Matrix Export Report

## Model

- Model: `graphsage_teg_concat`; split: `B`; seed: `9`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_teg_concat_splitB_seed9_epochs50_paper_teg_concat_fusions_10seed.pt`; selected epoch: `49`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3531, MAE=0.8391, QWK=0.6679, Recall@6-8=0.8000.
- `data_2021_train`: Macro-F1=0.4626, MAE=0.6134, QWK=0.8029, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.2461, MAE=1.4043, QWK=0.3702, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2394, MAE=1.3394, QWK=0.2138, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019275, P75=0.004006, P90=0.008143, P95=0.086183, P99=0.425229, max=0.856183, zero_ratio=0.001212.
- `data_2021`: edges=7647, mean=0.017628, P75=0.004114, P90=0.008017, P95=0.071917, P99=0.418148, max=0.841807, zero_ratio=0.001046.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
