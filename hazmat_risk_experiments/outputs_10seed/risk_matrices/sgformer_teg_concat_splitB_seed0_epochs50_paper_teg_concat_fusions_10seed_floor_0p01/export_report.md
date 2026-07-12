# Risk Matrix Export Report

## Model

- Model: `sgformer_teg_concat`; split: `B`; seed: `0`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_teg_concat_splitB_seed0_epochs50_paper_teg_concat_fusions_10seed.pt`; selected epoch: `34`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.2941, MAE=0.9802, QWK=0.6313, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.4064, MAE=0.8837, QWK=0.7279, Recall@6-8=0.8000.
- `data_2021_val`: Macro-F1=0.1914, MAE=1.2252, QWK=0.5604, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.2612, MAE=1.2342, QWK=0.4760, Recall@6-8=0.4231.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.020991, P75=0.004477, P90=0.008334, P95=0.119392, P99=0.434178, max=0.862897, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.018806, P75=0.004276, P90=0.007858, P95=0.109044, P99=0.422307, max=0.861648, zero_ratio=0.000131.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
