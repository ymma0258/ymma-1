# Risk Matrix Export Report

## Model

- Model: `graphsage_teg_concat`; split: `B`; seed: `2`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_teg_concat_splitB_seed2_epochs50_paper_teg_concat_fusions_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3270, MAE=0.8181, QWK=0.6798, Recall@6-8=0.9000.
- `data_2021_train`: Macro-F1=0.3188, MAE=0.5975, QWK=0.7628, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.1984, MAE=1.5016, QWK=0.0136, Recall@6-8=0.0000.
- `data_2021_test`: Macro-F1=0.2720, MAE=1.1937, QWK=0.3648, Recall@6-8=0.4231.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020118, P75=0.004200, P90=0.008573, P95=0.075718, P99=0.450132, max=0.891350, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017417, P75=0.003824, P90=0.008263, P95=0.062137, P99=0.421764, max=0.891682, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
