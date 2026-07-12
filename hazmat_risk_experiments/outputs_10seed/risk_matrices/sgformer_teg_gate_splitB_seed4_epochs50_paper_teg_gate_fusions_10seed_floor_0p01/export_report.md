# Risk Matrix Export Report

## Model

- Model: `sgformer_teg_gate`; split: `B`; seed: `4`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\sgformer_teg_gate_splitB_seed4_epochs50_paper_teg_gate_fusions_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5977, MAE=0.5095, QWK=0.7840, Recall@6-8=0.8750.
- `data_2021_train`: Macro-F1=0.7390, MAE=0.3223, QWK=0.8969, Recall@6-8=0.9500.
- `data_2021_val`: Macro-F1=0.3124, MAE=0.8944, QWK=0.5732, Recall@6-8=0.6000.
- `data_2021_test`: Macro-F1=0.3009, MAE=1.2900, QWK=0.2418, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.018117, P75=0.005369, P90=0.008657, P95=0.056746, P99=0.433058, max=0.982108, zero_ratio=0.000151.
- `data_2021`: edges=7647, mean=0.014964, P75=0.005315, P90=0.008628, P95=0.040070, P99=0.387459, max=0.956112, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
