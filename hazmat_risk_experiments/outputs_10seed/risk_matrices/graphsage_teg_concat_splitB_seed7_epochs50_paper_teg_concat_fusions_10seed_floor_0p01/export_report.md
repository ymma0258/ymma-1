# Risk Matrix Export Report

## Model

- Model: `graphsage_teg_concat`; split: `B`; seed: `7`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_teg_concat_splitB_seed7_epochs50_paper_teg_concat_fusions_10seed.pt`; selected epoch: `44`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.2664, MAE=0.9823, QWK=0.5924, Recall@6-8=0.8000.
- `data_2021_train`: Macro-F1=0.2879, MAE=0.7038, QWK=0.7616, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.2315, MAE=1.1010, QWK=0.5101, Recall@6-8=0.8000.
- `data_2021_test`: Macro-F1=0.1965, MAE=1.4564, QWK=0.2408, Recall@6-8=0.2692.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020697, P75=0.005236, P90=0.008098, P95=0.095286, P99=0.425339, max=0.842256, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.019263, P75=0.005344, P90=0.008130, P95=0.079001, P99=0.416471, max=0.856508, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
