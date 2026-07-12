# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 9.528657 | 0.000% | 0.295294 | 3.075095 | 0.198450 | 0.875896 | 90.577% |
| 0.25 | 0 | 157060.7 | 6.943% | 7.802145 | 18.119% | 0.226198 | 2.309658 | 0.200149 | 0.877135 | 89.571% |
| 0.5 | 0 | 166131.6 | 13.119% | 6.031029 | 36.706% | 0.152116 | 1.859495 | 0.201727 | 0.870771 | 87.462% |
| 1 | 0 | 176956.5 | 20.490% | 3.839968 | 59.701% | 0.084274 | 1.330772 | 0.299526 | 0.837920 | 81.235% |
| 2 | 0 | 192172.7 | 30.851% | 2.927422 | 69.278% | 0.061624 | 0.927712 | 0.270799 | 0.808942 | 75.623% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
