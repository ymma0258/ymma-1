# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 6.901845 | 0.000% | 0.199384 | 2.335080 | 0.226010 | 0.859819 | 88.450% |
| 1 | 0 | 156975.8 | 17.148% | 2.507068 | 63.675% | 0.052613 | 0.790557 | 0.218823 | 0.759431 | 74.105% |
| 1 | 0.5 | 162607.0 | 21.351% | 2.520839 | 63.476% | 0.052704 | 0.744843 | 0.176082 | 0.760127 | 74.009% |
| 1 | 1 | 167342.2 | 24.885% | 1.993224 | 71.120% | 0.036522 | 0.590738 | 0.224421 | 0.706101 | 66.722% |
| 1 | 2 | 174495.8 | 30.223% | 1.753740 | 74.590% | 0.029334 | 0.593179 | 0.267068 | 0.671749 | 61.984% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
