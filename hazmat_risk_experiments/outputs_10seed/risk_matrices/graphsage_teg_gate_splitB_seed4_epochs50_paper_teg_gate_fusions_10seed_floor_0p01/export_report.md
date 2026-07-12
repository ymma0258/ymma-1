# Risk Matrix Export Report

## Model

- Model: `graphsage_teg_gate`; split: `B`; seed: `4`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_teg_gate_splitB_seed4_epochs50_paper_teg_gate_fusions_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3015, MAE=0.7813, QWK=0.6421, Recall@6-8=0.7000.
- `data_2021_train`: Macro-F1=0.3406, MAE=0.6572, QWK=0.7464, Recall@6-8=0.8500.
- `data_2021_val`: Macro-F1=0.2334, MAE=1.2177, QWK=0.1208, Recall@6-8=0.2000.
- `data_2021_test`: Macro-F1=0.2254, MAE=1.2286, QWK=0.2035, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018884, P75=0.003857, P90=0.008354, P95=0.094801, P99=0.433107, max=0.858648, zero_ratio=0.001666.
- `data_2021`: edges=7647, mean=0.016676, P75=0.003779, P90=0.007744, P95=0.069395, P99=0.432286, max=0.863523, zero_ratio=0.001308.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
