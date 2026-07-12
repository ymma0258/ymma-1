# Risk Matrix Export Report

## Model

- Model: `graphsage_teg_gate`; split: `B`; seed: `2`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_teg_gate_splitB_seed2_epochs50_paper_teg_gate_fusions_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3226, MAE=0.8284, QWK=0.6369, Recall@6-8=0.8000.
- `data_2021_train`: Macro-F1=0.3925, MAE=0.5765, QWK=0.7645, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.2858, MAE=1.4164, QWK=0.1088, Recall@6-8=0.2000.
- `data_2021_test`: Macro-F1=0.2557, MAE=1.1745, QWK=0.3157, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020506, P75=0.004440, P90=0.008709, P95=0.090896, P99=0.446671, max=0.884496, zero_ratio=0.000151.
- `data_2021`: edges=7647, mean=0.017677, P75=0.004045, P90=0.008756, P95=0.067325, P99=0.442172, max=0.882926, zero_ratio=0.000131.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
