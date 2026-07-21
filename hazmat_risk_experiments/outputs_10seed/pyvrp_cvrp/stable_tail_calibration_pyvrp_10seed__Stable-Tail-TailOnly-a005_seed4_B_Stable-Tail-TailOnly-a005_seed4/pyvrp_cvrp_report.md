# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.0 | 0.000% | 8.269512 | 0.000% | 0.256588 | 2.857483 | 0.239496 | 0.872232 | 88.973% |
| 0.25 | 0 | 156650.1 | 6.374% | 7.109733 | 14.025% | 0.208198 | 2.367379 | 0.262336 | 0.867660 | 87.941% |
| 0.5 | 0 | 165217.9 | 12.192% | 5.528433 | 33.147% | 0.145531 | 1.859495 | 0.238046 | 0.850850 | 84.984% |
| 1 | 0 | 175610.0 | 19.248% | 3.949905 | 52.235% | 0.101182 | 1.527373 | 0.299126 | 0.822630 | 80.240% |
| 2 | 0 | 191260.7 | 29.876% | 3.118365 | 62.291% | 0.065183 | 1.167568 | 0.286826 | 0.799316 | 76.581% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
