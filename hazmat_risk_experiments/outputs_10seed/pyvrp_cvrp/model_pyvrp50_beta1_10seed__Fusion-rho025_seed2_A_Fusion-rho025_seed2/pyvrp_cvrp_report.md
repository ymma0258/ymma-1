# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.692878 | 0.000% | 0.270140 | 2.466840 | 0.145377 | 0.861740 | 89.184% |
| 1 | 0 | 160276.1 | 19.611% | 3.841697 | 55.806% | 0.105536 | 1.134260 | 0.227615 | 0.799095 | 79.429% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
