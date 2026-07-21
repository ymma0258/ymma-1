# Risk Matrix Export Report

## Model

- Model: `stable_tail_gate`; split: `B`; seed: `2`; epochs: `50`.
- Source: `checkpoint`; checkpoint: `D:\PyVRP-main\hazmat_risk_experiments\outputs_10seed\models\checkpoints\stable_tail_gate_splitB_seed2_epochs50_paper_stable_tail_gate_10seed.pt`; selected epoch: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.5483, MAE=0.9672, QWK=0.6325, Recall@6-8=0.7000.
- `data_2021_train`: Macro-F1=0.6450, MAE=0.7410, QWK=0.7267, Recall@6-8=0.7500.
- `data_2021_val`: Macro-F1=0.2454, MAE=1.5854, QWK=-0.1237, Recall@6-8=0.0000.
- `data_2021_test`: Macro-F1=0.3122, MAE=1.3136, QWK=0.2402, Recall@6-8=0.2308.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.021215, P75=0.004125, P90=0.008576, P95=0.121851, P99=0.434240, max=0.964942, zero_ratio=0.000000.
- `data_2021`: edges=7647, mean=0.019089, P75=0.003890, P90=0.008597, P95=0.102364, P99=0.434147, max=0.898944, zero_ratio=0.000000.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
