# Risk Matrix Export Report

## Model

- Model: `graphsage_teg_concat`; split: `B`; seed: `5`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_teg_concat_splitB_seed5_epochs50_paper_teg_concat_fusions_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3078, MAE=0.7558, QWK=0.6632, Recall@6-8=0.7750.
- `data_2021_train`: Macro-F1=0.3545, MAE=0.6021, QWK=0.8103, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.1918, MAE=1.3883, QWK=0.2086, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.2946, MAE=1.1200, QWK=0.4844, Recall@6-8=0.5769.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019410, P75=0.004134, P90=0.008845, P95=0.083714, P99=0.447062, max=0.905630, zero_ratio=0.000151.
- `data_2021`: edges=7647, mean=0.017007, P75=0.004190, P90=0.008202, P95=0.064658, P99=0.442219, max=0.904427, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
