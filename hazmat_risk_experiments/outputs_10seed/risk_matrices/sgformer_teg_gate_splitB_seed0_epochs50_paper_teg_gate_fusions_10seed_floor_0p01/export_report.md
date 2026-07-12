# Risk Matrix Export Report

## Model

- Model: `sgformer_teg_gate`; split: `B`; seed: `0`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_teg_gate_splitB_seed0_epochs50_paper_teg_gate_fusions_10seed.pt`; selected epoch: `47`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6137, MAE=0.6310, QWK=0.7847, Recall@6-8=0.9500.
- `data_2021_train`: Macro-F1=0.7134, MAE=0.5013, QWK=0.8839, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.4847, MAE=1.0807, QWK=0.5486, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.3191, MAE=1.1217, QWK=0.3969, Recall@6-8=0.4615.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019398, P75=0.006034, P90=0.008633, P95=0.085190, P99=0.435961, max=0.947272, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.016532, P75=0.005522, P90=0.008568, P95=0.075292, P99=0.366424, max=0.870174, zero_ratio=0.000131.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
