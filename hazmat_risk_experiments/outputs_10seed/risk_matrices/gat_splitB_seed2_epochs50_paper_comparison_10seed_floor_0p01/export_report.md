# Risk Matrix Export Report

## Model

- Model: `gat`; split: `B`; seed: `2`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gat_splitB_seed2_epochs50_paper_comparison_10seed.pt`; selected epoch: `47`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5978, MAE=0.8595, QWK=0.6737, Recall@6-8=0.7500.
- `data_2021_train`: Macro-F1=0.8169, MAE=0.5173, QWK=0.9004, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.2454, MAE=1.5294, QWK=-0.1286, Recall@6-8=0.0000.
- `data_2021_test`: Macro-F1=0.2712, MAE=1.2557, QWK=0.1752, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020462, P75=0.003882, P90=0.008355, P95=0.117679, P99=0.450982, max=0.955158, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017544, P75=0.003409, P90=0.008095, P95=0.096974, P99=0.368396, max=0.973368, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
