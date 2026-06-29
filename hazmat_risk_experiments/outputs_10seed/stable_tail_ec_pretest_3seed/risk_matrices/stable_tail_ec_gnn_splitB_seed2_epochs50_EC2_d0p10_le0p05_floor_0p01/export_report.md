# Risk Matrix Export Report

## Model

- Model: `stable_tail_ec_gnn`; split: `B`; seed: `2`; epochs: `50`.
- Risk mode: `exposure_floor`; exposure delta: `0.01`.

## Metrics

- `data_2020_train`: Macro-F1=0.2563, MAE=1.1474, QWK=0.4196, Recall@6-8=0.4500.
- `data_2021_train`: Macro-F1=0.2798, MAE=1.0401, QWK=0.4321, Recall@6-8=0.4400.
- `data_2021_test`: Macro-F1=0.2338, MAE=1.3345, QWK=0.2688, Recall@6-8=0.3077.

## Edge Risk Summary

- `data_2020`: edges=6603, mean=0.019198, P75=0.004132, P90=0.007140, P95=0.117876, P99=0.374421, max=0.739270, zero_ratio=0.057701.
- `data_2021`: edges=7647, mean=0.017977, P75=0.004299, P90=0.007191, P95=0.094334, P99=0.406755, max=0.768303, zero_ratio=0.056885.

The 5x8 matrices are written as CSV files and are used for explanation only; downstream path and VRP validation should use continuous `R_ij`.
