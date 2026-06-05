# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.2 | 0.000% | 8.581750 | 0.000% | 0.288704 | 2.890479 | 0.228887 | 0.850653 | 87.765% |
| 1 | 0 | 158510.6 | 18.294% | 3.189174 | 62.838% | 0.076233 | 1.092227 | 0.261009 | 0.717608 | 70.576% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
