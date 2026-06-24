# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.381772 | 0.000% | 0.210761 | 2.364995 | 0.202312 | 0.857571 | 88.285% |
| 1 | 0 | 157560.3 | 17.584% | 2.657344 | 64.001% | 0.059726 | 0.843358 | 0.202777 | 0.743701 | 73.300% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
