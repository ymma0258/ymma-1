# Risk Matrix Export Report

## Model

- Model: `stable_tail_gate`; split: `B`; seed: `7`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gate_splitB_seed7_epochs50_paper_stable_tail_gate_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5135, MAE=0.9275, QWK=0.6596, Recall@6-8=0.6750.
- `data_2021_train`: Macro-F1=0.7773, MAE=0.5907, QWK=0.8460, Recall@6-8=0.9000.
- `data_2021_val`: Macro-F1=0.2374, MAE=1.2154, QWK=0.3301, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2348, MAE=1.3870, QWK=0.1907, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020080, P75=0.004199, P90=0.008541, P95=0.104489, P99=0.431864, max=0.902754, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017450, P75=0.004174, P90=0.008389, P95=0.080526, P99=0.417515, max=0.887668, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
