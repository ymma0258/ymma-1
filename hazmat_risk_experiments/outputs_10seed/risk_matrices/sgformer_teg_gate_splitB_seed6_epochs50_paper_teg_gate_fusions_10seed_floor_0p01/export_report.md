# Risk Matrix Export Report

## Model

- Model: `sgformer_teg_gate`; split: `B`; seed: `6`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_teg_gate_splitB_seed6_epochs50_paper_teg_gate_fusions_10seed.pt`; selected epoch: `29`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4049, MAE=1.3272, QWK=0.5045, Recall@6-8=0.5250.
- `data_2021_train`: Macro-F1=0.5398, MAE=1.2281, QWK=0.4940, Recall@6-8=0.5500.
- `data_2021_val`: Macro-F1=0.2691, MAE=1.3975, QWK=0.4926, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2247, MAE=1.5640, QWK=0.3211, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.023637, P75=0.004494, P90=0.008407, P95=0.163224, P99=0.431542, max=0.854538, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.021756, P75=0.004229, P90=0.007610, P95=0.153835, P99=0.419056, max=0.856655, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
