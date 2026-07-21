# Current model result snapshot

Generated: 2026-07-14T22:51:39+08:00

Only current, validated aggregates are ranked below. Stale calibration downstream files are listed in the status table and excluded from comparisons.

## Result status

| Result group | Status | Rows | Reason |
|---|---:|---:|---|
| primary_node_test | valid | 13 | one 10-seed data_2021_test aggregate per formal model |
| primary_budget_sweep | valid | 13 A/B + 26 per-set | all 13 formal models present |
| primary_od_validation | valid | 26 | 13 models x 2 methods, each with 10 seeds |
| calibration_risk_matrices | valid | 170 | 17 configurations x 10 seeds; all schema v3 |
| calibration_od_validation | valid | 34 | 17 configurations x 2 methods; newer than schema-v3 exports; no failures |
| calibration_pyvrp | valid | 170 | fresh |
| calibration_common_route | valid | 1700 | fresh |
| calibration_load_aware | valid | 1700 | fresh |
| calibration_budget_sweep | valid | 34 | fresh |

## Node prediction (data_2021_test, 10 seeds)

| Model | Macro-F1 | MAE | QWK | High recall | High PR-AUC | High FN rate |
|---|---:|---:|---:|---:|---:|---:|
| SGFormer-adapted | 0.3217 | 1.2509 | 0.3717 | 0.3692 | 0.3557 | 0.6308 |
| SGFormer-TEG-Gate | 0.3002 | 1.2776 | 0.3532 | 0.3692 | 0.3701 | 0.6308 |
| Stable-Tail-Gate | 0.2990 | 1.3559 | 0.2639 | 0.2423 | 0.3557 | 0.7577 |
| GraphSAGE | 0.2960 | 1.2773 | 0.2992 | 0.2808 | 0.3763 | 0.7192 |
| Stable-Tail GNN | 0.2896 | 1.2666 | 0.2904 | 0.2462 | 0.3659 | 0.7538 |
| GCN | 0.2881 | 1.3739 | 0.2562 | 0.2154 | 0.3495 | 0.7846 |
| TEG-only | 0.2878 | 1.6617 | 0.2993 | 0.3000 | 0.3455 | 0.7000 |
| SGFormer-TEG-Concat | 0.2668 | 1.2575 | 0.3515 | 0.3615 | 0.3744 | 0.6385 |
| Gradformer-adapted | 0.2612 | 1.4125 | 0.2556 | 0.2346 | 0.3242 | 0.7654 |
| GAT | 0.2546 | 1.3744 | 0.2032 | 0.1769 | 0.3059 | 0.8231 |
| GraphSAGE-TEG-Gate | 0.2420 | 1.2325 | 0.2665 | 0.2808 | 0.3675 | 0.7192 |
| GraphSAGE-TEG-Concat | 0.2335 | 1.2633 | 0.3205 | 0.3538 | 0.3503 | 0.6462 |
| Stable-Tail w/o Tail Loss | 0.2323 | 1.1871 | 0.1964 | 0.1538 | 0.3319 | 0.8462 |

## PyVRP budget sweep (A/B average, 10 seeds)

Lower is better for every risk column.

| Model | Avg risk@B | Common AUBRC | CVaR90 AUBRC | CVaR95 AUBRC | Load CVaR90 | Max-vehicle CVaR90 | Core rank |
|---|---:|---:|---:|---:|---:|---:|---:|
| GraphSAGE-TEG-Gate | 4.0313 | 1.1853 | 0.02888 | 0.05217 | 0.01684 | 0.05185 | 1.67 |
| SGFormer-TEG-Gate | 4.0533 | 1.1855 | 0.02883 | 0.05285 | 0.01702 | 0.05194 | 2.00 |
| Stable-Tail GNN | 4.0571 | 1.1892 | 0.02883 | 0.05247 | 0.01725 | 0.05180 | 2.33 |
| SGFormer-TEG-Concat | 4.0872 | 1.2001 | 0.02888 | 0.05299 | 0.01694 | 0.05059 | 4.00 |
| GraphSAGE-TEG-Concat | 4.1187 | 1.2105 | 0.02955 | 0.05412 | 0.01757 | 0.05260 | 5.33 |
| Stable-Tail-Gate | 4.1335 | 1.2106 | 0.02977 | 0.05404 | 0.01742 | 0.05343 | 5.67 |
| GraphSAGE | 4.1458 | 1.2170 | 0.02981 | 0.05446 | 0.01790 | 0.05303 | 7.00 |
| SGFormer-adapted | 4.1511 | 1.2218 | 0.02983 | 0.05512 | 0.01752 | 0.05329 | 8.00 |
| TEG-only | 4.1927 | 1.2354 | 0.03029 | 0.05523 | 0.01816 | 0.05462 | 9.00 |
| Stable-Tail w/o Tail Loss | 4.1996 | 1.2350 | 0.03041 | 0.05585 | 0.01834 | 0.05421 | 10.00 |
| GCN | 4.2174 | 1.2433 | 0.03077 | 0.05645 | 0.01801 | 0.05530 | 11.00 |
| Gradformer-adapted | 4.3731 | 1.2899 | 0.03211 | 0.05941 | 0.01889 | 0.05737 | 12.00 |
| GAT | 4.4530 | 1.3162 | 0.03303 | 0.06075 | 0.01946 | 0.05960 | 13.00 |

## OD validation (CVaR-risk, 10 seeds)

Risk reductions are benefits; hop increase is routing cost.

| Model | Hop increase | Total-risk reduction | CVaR90 reduction | Max-risk reduction | RE reduction |
|---|---:|---:|---:|---:|---:|
| Stable-Tail w/o Tail Loss | 0.0956 | 0.8548 | 0.9007 | 0.9095 | 0.9198 |
| GraphSAGE-TEG-Concat | 0.0951 | 0.8503 | 0.8985 | 0.9069 | 0.9177 |
| GraphSAGE-TEG-Gate | 0.0975 | 0.8502 | 0.8995 | 0.9059 | 0.9174 |
| Stable-Tail GNN | 0.1023 | 0.8477 | 0.9008 | 0.9079 | 0.9195 |
| SGFormer-TEG-Concat | 0.1014 | 0.8443 | 0.9018 | 0.9109 | 0.9232 |
| GraphSAGE | 0.1039 | 0.8431 | 0.8984 | 0.9051 | 0.9185 |
| Gradformer-adapted | 0.0946 | 0.8429 | 0.9063 | 0.9121 | 0.9250 |
| GCN | 0.1002 | 0.8417 | 0.9004 | 0.9050 | 0.9203 |
| GAT | 0.0958 | 0.8402 | 0.8980 | 0.9040 | 0.9182 |
| SGFormer-adapted | 0.0975 | 0.8400 | 0.9034 | 0.9124 | 0.9221 |
| Stable-Tail-Gate | 0.1020 | 0.8395 | 0.8991 | 0.9043 | 0.9201 |
| SGFormer-TEG-Gate | 0.1041 | 0.8369 | 0.9005 | 0.9089 | 0.9223 |
| TEG-only | 0.1103 | 0.8061 | 0.8942 | 0.9036 | 0.9223 |

## Stable-Tail calibration OD (schema v3, CVaR-risk, 10 seeds)

| Configuration | Hop increase | Total-risk reduction | CVaR90 reduction | Max-risk reduction | RE reduction |
|---|---:|---:|---:|---:|---:|
| Stable-Tail-TailOnly-a030 | 0.1023 | 0.8574 | 0.9051 | 0.9115 | 0.9231 |
| Stable-Tail-TailOnly-a020 | 0.1023 | 0.8547 | 0.9039 | 0.9105 | 0.9221 |
| Stable-Tail-EdgeTail-a030 | 0.1023 | 0.8529 | 0.9032 | 0.9100 | 0.9215 |
| Stable-Tail-TailOnly-a010 | 0.1023 | 0.8517 | 0.9026 | 0.9094 | 0.9210 |
| Stable-Tail-EdgeTail-a020 | 0.1023 | 0.8515 | 0.9026 | 0.9095 | 0.9210 |
| Stable-Tail-MatrixEns-r040 | 0.1023 | 0.8502 | 0.9017 | 0.9087 | 0.9203 |
| Stable-Tail-EdgeTail-a010 | 0.1023 | 0.8499 | 0.9018 | 0.9088 | 0.9203 |
| Stable-Tail-TailOnly-a005 | 0.1023 | 0.8498 | 0.9017 | 0.9087 | 0.9203 |
| Stable-Tail-MatrixEns-r030 | 0.1023 | 0.8493 | 0.9014 | 0.9084 | 0.9200 |
| Stable-Tail-EdgeTail-a005 | 0.1023 | 0.8489 | 0.9013 | 0.9083 | 0.9199 |
| Stable-Tail-NodeCalib-a030 | 0.1025 | 0.8487 | 0.9014 | 0.9083 | 0.9194 |
| Stable-Tail-MatrixEns-r020 | 0.1023 | 0.8487 | 0.9011 | 0.9082 | 0.9198 |
| Stable-Tail-NodeCalib-a020 | 0.1025 | 0.8484 | 0.9013 | 0.9082 | 0.9195 |
| Stable-Tail-NodeCalib-a010 | 0.1027 | 0.8482 | 0.9010 | 0.9080 | 0.9196 |
| Stable-Tail-MatrixEns-r010 | 0.1023 | 0.8482 | 0.9010 | 0.9080 | 0.9197 |
| Stable-Tail-MatrixEns-r005 | 0.1023 | 0.8479 | 0.9009 | 0.9079 | 0.9196 |
| Stable-Tail-NodeCalib-a005 | 0.1026 | 0.8479 | 0.9010 | 0.9079 | 0.9195 |

## Complete tables

- `all_model_node_all_splits_results.csv`: all four node evaluation splits, means, and standard deviations.
- `all_model_node_test_results.csv`: the data_2021_test subset used in the comparison above.
- `all_model_budget_ab_results.csv`: all A/B-average budget metrics.
- `all_model_budget_by_set_results.csv`: all A and B metrics with standard deviations.
- `all_model_od_results.csv`: both OD methods and all means/standard deviations.
- `stable_tail_calibration_od_results_v3.csv`: all 17 calibration configurations and both OD methods.
- `all_30_models_budget_by_set_results.csv`: 13 formal models plus 17 post-processing configurations, split by Set A/B.
- `all_30_models_od_results.csv`: OD results for all 30 models/configurations and both routing methods.
- `all_30_models_inventory.csv`: result availability for every model/configuration.
- `result_status.csv`: validity and freshness audit.
