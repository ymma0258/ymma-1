# Risk Matrix Export Report

## Model

- Model: `gcn_teg_concat`; split: `B`; seed: `8`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\st_v1_formal_10seed\models\checkpoints\gcn_teg_concat_splitB_seed8_epochs50_st_v1_formal_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.4674, MAE=0.7482, QWK=0.6721, Recall@6-8=0.6750.
- `data_2021_train`: Macro-F1=0.5863, MAE=0.5778, QWK=0.8247, Recall@6-8=0.8800.
- `data_2021_test`: Macro-F1=0.2325, MAE=1.1965, QWK=0.1929, Recall@6-8=0.1538.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.017261, P75=0.003320, P90=0.008604, P95=0.071876, P99=0.433510, max=0.895618, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.014681, P75=0.003059, P90=0.008324, P95=0.061014, P99=0.420378, max=0.869672, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
