# Risk Matrix Export Report

## Model

- Model: `graphsage_teg_gate`; split: `B`; seed: `6`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_teg_gate_splitB_seed6_epochs50_paper_teg_gate_fusions_10seed.pt`; selected epoch: `48`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3316, MAE=0.9088, QWK=0.6265, Recall@6-8=0.7500.
- `data_2021_train`: Macro-F1=0.4008, MAE=0.7909, QWK=0.7525, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.2742, MAE=1.1970, QWK=0.4685, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2419, MAE=1.1874, QWK=0.3883, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019464, P75=0.004093, P90=0.007442, P95=0.105646, P99=0.411445, max=0.831734, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.016959, P75=0.003981, P90=0.007016, P95=0.075450, P99=0.391190, max=0.831053, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
