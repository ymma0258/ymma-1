# Risk Matrix Export Report

## Model

- Model: `stable_tail_gnn`; split: `B`; seed: `1`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gnn_splitB_seed1_epochs50_paper_comparison_10seed.pt`; selected epoch: `46`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5499, MAE=0.8586, QWK=0.7347, Recall@6-8=0.8750.
- `data_2021_train`: Macro-F1=0.6166, MAE=0.6500, QWK=0.8026, Recall@6-8=0.9000.
- `data_2021_val`: Macro-F1=0.2380, MAE=1.3521, QWK=0.5404, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2643, MAE=1.3537, QWK=0.2791, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020776, P75=0.004293, P90=0.008589, P95=0.089302, P99=0.441654, max=0.909404, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018308, P75=0.004190, P90=0.008582, P95=0.076552, P99=0.433374, max=0.873630, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
