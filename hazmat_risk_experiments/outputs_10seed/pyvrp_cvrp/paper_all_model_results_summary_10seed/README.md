# All model results summary (10 seeds)

Source: paper_model_comparison_with_gate_10seed plus focused SGFormer-TEG-Gate vs Stable-Tail GNN tests.

This directory consolidates current results for all 12 evaluated models: upstream node-risk metrics, fixed-budget downstream validation, B=10%-40% budget sweep, Common/CVaR/LoadRisk AUBRC, concentration metrics, pairwise significance, and complexity/runtime comparison.

## Files

| file | rows | cols |
| --- | --- | --- |
| all_model_auc_paired_significance_holm.csv | 22 | 10 |
| all_model_average_rankings.csv | 12 | 16 |
| all_model_budget20_extended_metrics.csv | 24 | 13 |
| all_model_budget_sweep_10_40.csv | 168 | 26 |
| all_model_budget_win_rates.csv | 24 | 6 |
| all_model_cost_risk_aubrc.csv | 24 | 12 |
| all_model_fixed_budget_20_25_30.csv | 72 | 26 |
| all_model_fixed_budget_risk_10_40.csv | 168 | 26 |
| all_model_gate_pairwise_significance.csv | 48 | 13 |
| all_model_paired_significance_holm.csv | 154 | 12 |
| all_model_results_summary.csv | 12 | 32 |
| all_model_targeted_common_cvar_significance.csv | 84 | 13 |
| all_model_upstream_node_metrics.csv | 12 | 7 |
| sgformer_gate_vs_stable_aubrc_significance.csv | 9 | 12 |
| sgformer_gate_vs_stable_complexity.csv | 2 | 18 |
| sgformer_gate_vs_stable_risk20_significance.csv | 12 | 13 |
| sgformer_gate_vs_stable_summary.csv | 4 | 11 |

## Headline average ranking across Set A and Set B

| model | avg_risk20 | avg_cvar90_20 | avg_load_risk20 | avg_common_risk_aubrc | avg_cvar90_aubrc | avg_load_risk_aubrc | avg_win_rate_10_40 | rank_avg_common_aubrc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SGFormer-TEG-Gate | 4.216921 | 0.104294 | 2.106040 | 4.973469 | 0.129786 | 2.507258 | 0.121429 | 1.000000 |
| Stable-Tail GNN | 4.193984 | 0.102055 | 2.131599 | 4.979531 | 0.129846 | 2.535055 | 0.078571 | 2.000000 |
| GraphSAGE-TEG-Gate | 4.433315 | 0.108959 | 2.219040 | 4.996629 | 0.130273 | 2.509091 | 0.150000 | 3.000000 |
| SGFormer-TEG-Concat | 4.318288 | 0.105517 | 2.144159 | 5.008437 | 0.131142 | 2.512087 | 0.078571 | 4.000000 |
| SGFormer-adapted | 4.296046 | 0.104807 | 2.167649 | 5.040370 | 0.130686 | 2.532360 | 0.128571 | 5.000000 |
| GraphSAGE | 4.259482 | 0.105269 | 2.194650 | 5.054796 | 0.132416 | 2.573337 | 0.035714 | 6.000000 |
| GraphSAGE-TEG-Concat | 4.555337 | 0.111676 | 2.335269 | 5.089253 | 0.133374 | 2.579526 | 0.185714 | 7.000000 |
| Stable-Tail w/o Tail Loss | 4.551103 | 0.113409 | 2.346765 | 5.089805 | 0.133970 | 2.603154 | 0.028571 | 8.000000 |
| TEG-only | 4.620684 | 0.114181 | 2.384177 | 5.093985 | 0.134104 | 2.580412 | 0.057143 | 9.000000 |
| GCN | 4.715944 | 0.116755 | 2.356345 | 5.127383 | 0.134864 | 2.590034 | 0.050000 | 10.000000 |
| Gradformer-adapted | 4.878482 | 0.123332 | 2.470442 | 5.302193 | 0.140813 | 2.673363 | 0.078571 | 11.000000 |
| GAT | 4.808154 | 0.118684 | 2.457635 | 5.322725 | 0.140263 | 2.695306 | 0.007143 | 12.000000 |

## Full per-model summary

| model | set_a_risk20 | set_a_cvar90_20 | set_a_load_risk20 | set_a_top10_share20 | set_a_common_risk_aubrc | set_a_cvar90_aubrc | set_a_load_risk_aubrc | set_b_risk20 | set_b_cvar90_20 | set_b_load_risk20 | set_b_top10_share20 | set_b_common_risk_aubrc | set_b_cvar90_aubrc | set_b_load_risk_aubrc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GCN | 3.486999 | 0.090924 | 1.769110 | 0.765798 | 4.507325 | 0.121447 | 2.352620 | 5.944890 | 0.142586 | 2.943580 | 0.848583 | 5.747440 | 0.148280 | 2.827448 |
| GAT | 3.553383 | 0.091328 | 1.832971 | 0.771921 | 4.605272 | 0.124471 | 2.392510 | 6.062925 | 0.146039 | 3.082299 | 0.850255 | 6.040179 | 0.156056 | 2.998102 |
| GraphSAGE | 3.362821 | 0.085859 | 1.736378 | 0.759282 | 4.452183 | 0.118968 | 2.292794 | 5.156142 | 0.124679 | 2.652922 | 0.822310 | 5.657409 | 0.145863 | 2.853880 |
| GraphSAGE-TEG-Concat | 3.571489 | 0.091086 | 1.813838 | 0.771755 | 4.484355 | 0.120227 | 2.312920 | 5.539184 | 0.132266 | 2.856699 | 0.836740 | 5.694150 | 0.146520 | 2.846132 |
| GraphSAGE-TEG-Gate | 3.409998 | 0.086363 | 1.692575 | 0.763755 | 4.401359 | 0.115888 | 2.271843 | 5.456632 | 0.131556 | 2.745506 | 0.833473 | 5.591899 | 0.144659 | 2.746338 |
| SGFormer-adapted | 3.573099 | 0.090473 | 1.787216 | 0.772120 | 4.511834 | 0.119692 | 2.279590 | 5.018993 | 0.119142 | 2.548082 | 0.820331 | 5.568905 | 0.141680 | 2.785129 |
| SGFormer-TEG-Concat | 3.423872 | 0.085890 | 1.722559 | 0.762687 | 4.425400 | 0.117607 | 2.261364 | 5.212704 | 0.125145 | 2.565759 | 0.823284 | 5.591475 | 0.144677 | 2.762811 |
| SGFormer-TEG-Gate | 3.507450 | 0.090159 | 1.738768 | 0.767668 | 4.426548 | 0.117101 | 2.286088 | 4.926391 | 0.118429 | 2.473312 | 0.813794 | 5.520390 | 0.142471 | 2.728429 |
| Gradformer-adapted | 4.001552 | 0.105603 | 2.008850 | 0.794839 | 4.722249 | 0.127816 | 2.433578 | 5.755412 | 0.141062 | 2.932035 | 0.843044 | 5.882138 | 0.153810 | 2.913149 |
| TEG-only | 3.513902 | 0.090612 | 1.792207 | 0.766367 | 4.538018 | 0.123300 | 2.338059 | 5.727466 | 0.137750 | 2.976147 | 0.840612 | 5.649951 | 0.144907 | 2.822765 |
| Stable-Tail w/o Tail Loss | 3.498773 | 0.089786 | 1.800046 | 0.767277 | 4.538872 | 0.122775 | 2.356504 | 5.603433 | 0.137032 | 2.893483 | 0.838000 | 5.640739 | 0.145164 | 2.849804 |
| Stable-Tail GNN | 3.272557 | 0.081407 | 1.656334 | 0.754948 | 4.407365 | 0.117093 | 2.295638 | 5.115411 | 0.122702 | 2.606863 | 0.821273 | 5.551698 | 0.142598 | 2.774472 |

## Upstream node-risk evaluation

| model | macro_f1 | mae | qwk | pr_auc | recall_at_6_8 | high_fn |
| --- | --- | --- | --- | --- | --- | --- |
| GCN | 0.288100 | 1.373900 | 0.256200 | 0.349500 | 0.215400 | 0.784600 |
| GAT | 0.254600 | 1.374400 | 0.203200 | 0.305900 | 0.176900 | 0.823100 |
| GraphSAGE | 0.296000 | 1.277300 | 0.299200 | 0.376300 | 0.280800 | 0.719200 |
| GraphSAGE-TEG-Concat | 0.233500 | 1.263300 | 0.320500 | 0.350300 | 0.353800 | 0.646200 |
| GraphSAGE-TEG-Gate | 0.242000 | 1.232500 | 0.266500 | 0.367500 | 0.280800 | 0.719200 |
| SGFormer-adapted | 0.321700 | 1.250900 | 0.371700 | 0.355700 | 0.369200 | 0.630800 |
| SGFormer-TEG-Concat | 0.266800 | 1.257500 | 0.351500 | 0.374400 | 0.361500 | 0.638500 |
| SGFormer-TEG-Gate | 0.300200 | 1.277600 | 0.353200 | 0.370100 | 0.369200 | 0.630800 |
| Gradformer-adapted | 0.261200 | 1.412500 | 0.255600 | 0.324200 | 0.234600 | 0.765400 |
| TEG-only | 0.287800 | 1.661700 | 0.299300 | 0.345500 | 0.300000 | 0.700000 |
| Stable-Tail w/o Tail Loss | 0.232300 | 1.187100 | 0.196400 | 0.331900 | 0.153800 | 0.846200 |
| Stable-Tail GNN | 0.289600 | 1.266600 | 0.290400 | 0.365900 | 0.246200 | 0.753800 |

## SGFormer-TEG-Gate vs Stable-Tail GNN focused downstream comparison

| model | customer_set | common_risk_aubrc | cvar90_aubrc | load_risk_aubrc | risk20 | cvar90_20 | load_risk20 | top10_share20 | edge_gini20 | max_vehicle_risk20 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SGFormer-TEG-Gate | A | 4.426548 | 0.117101 | 2.286088 | 3.507450 | 0.090159 | 1.738768 | 0.767668 | 0.764402 | 1.177430 |
| SGFormer-TEG-Gate | B | 5.520390 | 0.142471 | 2.728429 | 4.926391 | 0.118429 | 2.473312 | 0.813794 | 0.801575 | 1.631862 |
| Stable-Tail GNN | A | 4.407365 | 0.117093 | 2.295638 | 3.272557 | 0.081407 | 1.656334 | 0.754948 | 0.753786 | 1.063085 |
| Stable-Tail GNN | B | 5.551698 | 0.142598 | 2.774472 | 5.115411 | 0.122702 | 2.606863 | 0.821273 | 0.806113 | 1.729628 |

## Complexity and runtime

| model | parameters | checkpoint_size_mb | forward_ms_mean | train_step_ms_mean | param_ratio_vs_stable | forward_time_ratio_vs_stable | train_step_time_ratio_vs_stable |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SGFormer-TEG-Gate | 104457 | 0.418961 | 59.544020 | 135.923490 | 1.186903 | 1.348524 | 1.408417 |
| Stable-Tail GNN | 88008 | 0.353890 | 44.154956 | 96.508020 | 1.000000 | 1.000000 | 1.000000 |

## Interpretation notes

- Lower Risk@20, CVaR@20, LoadRisk, and AUBRC are better.
- Higher budget win rate is better.
- Complete raw tables are preserved as CSV in this directory; the Markdown report is a readable index, not a replacement for the CSVs.
- SGFormer-TEG-Gate is compared separately against Stable-Tail GNN on Set A AUBRC, Set B AUBRC, average AUBRC, and Risk@20; see the focused significance CSVs.
