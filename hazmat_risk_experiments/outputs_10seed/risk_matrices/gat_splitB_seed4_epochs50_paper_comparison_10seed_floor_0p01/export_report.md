# Risk Matrix Export Report

## Model

- Model: `gat`; split: `B`; seed: `4`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gat_splitB_seed4_epochs50_paper_comparison_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6038, MAE=0.8420, QWK=0.7249, Recall@6-8=0.7500.
- `data_2021_train`: Macro-F1=0.8637, MAE=0.6021, QWK=0.8474, Recall@6-8=0.9000.
- `data_2021_val`: Macro-F1=0.2016, MAE=1.3722, QWK=0.0529, Recall@6-8=0.0000.
- `data_2021_test`: Macro-F1=0.2617, MAE=1.2776, QWK=0.1286, Recall@6-8=0.1154.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019493, P75=0.003885, P90=0.008562, P95=0.100628, P99=0.432405, max=0.969627, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017170, P75=0.003693, P90=0.008570, P95=0.090513, P99=0.392652, max=0.956501, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
