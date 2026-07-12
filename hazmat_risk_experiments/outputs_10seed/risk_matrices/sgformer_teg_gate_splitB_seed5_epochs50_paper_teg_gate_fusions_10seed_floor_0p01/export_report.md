# Risk Matrix Export Report

## Model

- Model: `sgformer_teg_gate`; split: `B`; seed: `5`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_teg_gate_splitB_seed5_epochs50_paper_teg_gate_fusions_10seed.pt`; selected epoch: `44`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5305, MAE=0.6807, QWK=0.7330, Recall@6-8=0.8750.
- `data_2021_train`: Macro-F1=0.8106, MAE=0.4904, QWK=0.8561, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.4226, MAE=1.2822, QWK=0.4947, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.3186, MAE=1.1833, QWK=0.4493, Recall@6-8=0.5000.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019708, P75=0.004863, P90=0.008502, P95=0.091075, P99=0.433723, max=0.941996, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017389, P75=0.004796, P90=0.008454, P95=0.089731, P99=0.398128, max=0.874099, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
