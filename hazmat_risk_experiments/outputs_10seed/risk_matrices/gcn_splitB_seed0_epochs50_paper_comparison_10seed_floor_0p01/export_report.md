# Risk Matrix Export Report

## Model

- Model: `gcn`; split: `B`; seed: `0`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\gcn_splitB_seed0_epochs50_paper_comparison_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5559, MAE=0.9342, QWK=0.6720, Recall@6-8=0.7000.
- `data_2021_train`: Macro-F1=0.7460, MAE=0.7064, QWK=0.8392, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.2661, MAE=1.1602, QWK=0.5047, Recall@6-8=0.4000.
- `data_2021_test`: Macro-F1=0.3317, MAE=1.2919, QWK=0.2504, Recall@6-8=0.1923.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019192, P75=0.003510, P90=0.008544, P95=0.110889, P99=0.431476, max=0.879596, zero_ratio=0.000151.
- `data_2021`: edges=7647, mean=0.016547, P75=0.003499, P90=0.007692, P95=0.103603, P99=0.357748, max=0.848854, zero_ratio=0.000915.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
