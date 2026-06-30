# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 8.064866 | 0.000% | 0.257199 | 2.321310 | 0.141978 | 0.868153 | 89.504% |
| 1 | 0 | 156629.7 | 16.890% | 3.082411 | 61.780% | 0.066526 | 1.018187 | 0.201061 | 0.798747 | 77.809% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
