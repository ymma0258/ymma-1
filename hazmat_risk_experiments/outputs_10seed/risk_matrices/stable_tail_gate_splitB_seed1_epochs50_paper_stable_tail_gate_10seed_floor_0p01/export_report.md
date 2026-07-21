# Risk Matrix Export Report

## Model

- Model: `stable_tail_gate`; split: `B`; seed: `1`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gate_splitB_seed1_epochs50_paper_stable_tail_gate_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6052, MAE=0.9836, QWK=0.7146, Recall@6-8=0.8250.
- `data_2021_train`: Macro-F1=0.7418, MAE=0.7941, QWK=0.7620, Recall@6-8=0.8500.
- `data_2021_val`: Macro-F1=0.2369, MAE=1.4257, QWK=0.3737, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.3236, MAE=1.4224, QWK=0.2844, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020589, P75=0.004235, P90=0.008533, P95=0.115522, P99=0.432905, max=0.894152, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017805, P75=0.003850, P90=0.008033, P95=0.102227, P99=0.392919, max=0.879965, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
