# Risk Matrix Export Report

## Model

- Model: `graphsage_teg_gate`; split: `B`; seed: `5`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_teg_gate_splitB_seed5_epochs50_paper_teg_gate_fusions_10seed.pt`; selected epoch: `48`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3494, MAE=0.8331, QWK=0.6126, Recall@6-8=0.6500.
- `data_2021_train`: Macro-F1=0.4578, MAE=0.6854, QWK=0.7442, Recall@6-8=0.8000.
- `data_2021_val`: Macro-F1=0.2204, MAE=1.3102, QWK=0.2678, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2703, MAE=1.1651, QWK=0.3815, Recall@6-8=0.3846.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.017580, P75=0.003179, P90=0.007714, P95=0.096477, P99=0.389564, max=0.850511, zero_ratio=0.000606.
- `data_2021`: edges=7647, mean=0.015015, P75=0.003171, P90=0.007473, P95=0.066079, P99=0.378094, max=0.801156, zero_ratio=0.000654.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
