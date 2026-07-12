# Risk Matrix Export Report

## Model

- Model: `teg_only`; split: `B`; seed: `1`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\teg_only_splitB_seed1_epochs50_paper_comparison_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.6013, MAE=1.3081, QWK=0.6948, Recall@6-8=0.8500.
- `data_2021_train`: Macro-F1=0.7572, MAE=1.0637, QWK=0.8533, Recall@6-8=0.8500.
- `data_2021_val`: Macro-F1=0.2362, MAE=1.9471, QWK=0.3088, Recall@6-8=0.2000.
- `data_2021_test`: Macro-F1=0.2803, MAE=1.7114, QWK=0.2566, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019643, P75=0.004850, P90=0.008570, P95=0.096699, P99=0.430570, max=0.860275, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.016876, P75=0.004657, P90=0.008443, P95=0.082246, P99=0.368993, max=0.857006, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
