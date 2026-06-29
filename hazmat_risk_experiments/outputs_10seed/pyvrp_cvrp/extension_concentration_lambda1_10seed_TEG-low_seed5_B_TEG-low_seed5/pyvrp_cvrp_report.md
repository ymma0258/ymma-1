# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.526416 | 0.000% | 0.223916 | 2.417209 | 0.198886 | 0.823515 | 85.201% |
| 1 | 0 | 176436.8 | 20.245% | 3.531081 | 53.084% | 0.076193 | 1.183479 | 0.231821 | 0.704968 | 70.822% |
| 1 | 1 | 190113.1 | 29.566% | 2.979633 | 60.411% | 0.063035 | 0.908269 | 0.219481 | 0.667069 | 65.535% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
