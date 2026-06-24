# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 6.922293 | 0.000% | 0.198248 | 2.081292 | 0.172877 | 0.846670 | 87.143% |
| 1 | 0 | 157166.4 | 17.290% | 2.645530 | 61.782% | 0.066347 | 0.897057 | 0.248705 | 0.717077 | 70.998% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
