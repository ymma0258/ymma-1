# Risk Matrix Export Report

## Model

- Model: `graphsage_teg_gate`; split: `B`; seed: `8`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_teg_gate_splitB_seed8_epochs50_paper_teg_gate_fusions_10seed.pt`; selected epoch: `49`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3479, MAE=0.8533, QWK=0.5890, Recall@6-8=0.7000.
- `data_2021_train`: Macro-F1=0.4683, MAE=0.6217, QWK=0.6625, Recall@6-8=0.7500.
- `data_2021_val`: Macro-F1=0.2988, MAE=1.2757, QWK=0.6510, Recall@6-8=0.8000.
- `data_2021_test`: Macro-F1=0.2284, MAE=1.2646, QWK=0.2884, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019576, P75=0.004303, P90=0.008111, P95=0.085726, P99=0.426938, max=0.845422, zero_ratio=0.002120.
- `data_2021`: edges=7647, mean=0.017022, P75=0.004410, P90=0.007541, P95=0.063494, P99=0.419793, max=0.841069, zero_ratio=0.001831.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
