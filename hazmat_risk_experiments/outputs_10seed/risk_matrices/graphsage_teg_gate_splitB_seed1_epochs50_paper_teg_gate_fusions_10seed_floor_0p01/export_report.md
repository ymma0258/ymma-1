# Risk Matrix Export Report

## Model

- Model: `graphsage_teg_gate`; split: `B`; seed: `1`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_teg_gate_splitB_seed1_epochs50_paper_teg_gate_fusions_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3669, MAE=0.8145, QWK=0.7066, Recall@6-8=0.8250.
- `data_2021_train`: Macro-F1=0.4750, MAE=0.6164, QWK=0.7785, Recall@6-8=0.9000.
- `data_2021_val`: Macro-F1=0.2465, MAE=1.1317, QWK=0.5459, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2086, MAE=1.3072, QWK=0.2906, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021225, P75=0.004463, P90=0.008685, P95=0.088242, P99=0.443222, max=0.877666, zero_ratio=0.000454.
- `data_2021`: edges=7647, mean=0.019116, P75=0.004342, P90=0.008617, P95=0.072045, P99=0.435572, max=0.870380, zero_ratio=0.001308.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
