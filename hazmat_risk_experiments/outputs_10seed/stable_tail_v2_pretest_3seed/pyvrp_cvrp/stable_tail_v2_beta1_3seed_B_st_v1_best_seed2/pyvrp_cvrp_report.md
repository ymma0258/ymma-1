# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 8.481827 | 0.000% | 0.253784 | 3.071412 | 0.290763 | 0.879935 | 90.293% |
| 1 | 0 | 177571.3 | 21.441% | 4.278648 | 49.555% | 0.104338 | 1.535044 | 0.255516 | 0.843743 | 82.896% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
