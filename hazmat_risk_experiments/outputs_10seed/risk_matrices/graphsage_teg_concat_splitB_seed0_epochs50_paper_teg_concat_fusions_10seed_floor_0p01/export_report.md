# Risk Matrix Export Report

## Model

- Model: `graphsage_teg_concat`; split: `B`; seed: `0`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\graphsage_teg_concat_splitB_seed0_epochs50_paper_teg_concat_fusions_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.3503, MAE=0.7936, QWK=0.6857, Recall@6-8=0.8500.
- `data_2021_train`: Macro-F1=0.3804, MAE=0.6168, QWK=0.8090, Recall@6-8=1.0000.
- `data_2021_val`: Macro-F1=0.2468, MAE=1.0837, QWK=0.6015, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2776, MAE=1.2185, QWK=0.3859, Recall@6-8=0.3846.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020073, P75=0.004047, P90=0.008653, P95=0.079407, P99=0.436967, max=0.870397, zero_ratio=0.000151.
- `data_2021`: edges=7647, mean=0.017309, P75=0.003827, P90=0.008445, P95=0.066813, P99=0.426493, max=0.865180, zero_ratio=0.001046.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
