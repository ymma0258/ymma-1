# Risk Matrix Export Report

## Model

- Model: `sgformer_teg_gate`; split: `B`; seed: `7`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_teg_gate_splitB_seed7_epochs50_paper_teg_gate_fusions_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.7378, MAE=0.4267, QWK=0.8717, Recall@6-8=0.9750.
- `data_2021_train`: Macro-F1=0.9428, MAE=0.1735, QWK=0.9756, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.3538, MAE=1.0413, QWK=0.5324, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2934, MAE=1.3008, QWK=0.3479, Recall@6-8=0.4231.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018686, P75=0.006275, P90=0.008571, P95=0.045266, P99=0.436021, max=0.982746, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.016407, P75=0.006066, P90=0.008572, P95=0.033628, P99=0.431411, max=0.894074, zero_ratio=0.000131.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
