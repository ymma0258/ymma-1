# Risk Matrix Export Report

## Model

- Model: `graphsage_teg_concat`; split: `B`; seed: `8`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_teg_concat_splitB_seed8_epochs50_paper_teg_concat_fusions_10seed.pt`; selected epoch: `44`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3160, MAE=0.9393, QWK=0.6189, Recall@6-8=0.8000.
- `data_2021_train`: Macro-F1=0.3962, MAE=0.7486, QWK=0.7122, Recall@6-8=0.8500.
- `data_2021_val`: Macro-F1=0.2624, MAE=1.4069, QWK=0.5281, Recall@6-8=0.8000.
- `data_2021_test`: Macro-F1=0.2065, MAE=1.2993, QWK=0.3389, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018963, P75=0.004397, P90=0.008379, P95=0.089667, P99=0.424475, max=0.857661, zero_ratio=0.001212.
- `data_2021`: edges=7647, mean=0.017153, P75=0.004272, P90=0.008246, P95=0.069230, P99=0.430037, max=0.857656, zero_ratio=0.001046.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
