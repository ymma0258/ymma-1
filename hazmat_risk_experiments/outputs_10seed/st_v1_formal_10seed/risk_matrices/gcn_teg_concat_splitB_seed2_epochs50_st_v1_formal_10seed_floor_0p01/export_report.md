# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `B`; seed: `2`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\st_v1_formal_10seed\models\checkpoints\gcn_teg_concat_splitB_seed2_epochs50_st_v1_formal_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4013, MAE=0.8287, QWK=0.6606, Recall@6-8=0.7250.
- `data_2021_train`: Macro-F1=0.4723, MAE=0.6546, QWK=0.7137, Recall@6-8=0.8000.
- `data_2021_test`: Macro-F1=0.2982, MAE=1.1368, QWK=0.3644, Recall@6-8=0.3462.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019496, P75=0.003803, P90=0.008496, P95=0.080346, P99=0.429040, max=0.931048, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.017853, P75=0.004011, P90=0.008489, P95=0.071380, P99=0.427132, max=0.900986, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
