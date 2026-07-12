# Risk Matrix Export Report

## Model

- Model: `sgformer_teg_gate`; split: `B`; seed: `8`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_teg_gate_splitB_seed8_epochs50_paper_teg_gate_fusions_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6107, MAE=0.7283, QWK=0.7535, Recall@6-8=0.9500.
- `data_2021_train`: Macro-F1=0.8175, MAE=0.3771, QWK=0.9332, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.3235, MAE=1.2739, QWK=0.4299, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.3082, MAE=1.2435, QWK=0.3873, Recall@6-8=0.4231.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020545, P75=0.005668, P90=0.008579, P95=0.088344, P99=0.434344, max=0.946767, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018025, P75=0.004752, P90=0.008573, P95=0.084539, P99=0.432937, max=0.902251, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
