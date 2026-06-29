# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 15.211645 | 0.000% | 0.187700 | 4.658365 | 0.196752 | 0.858795 | 90.494% |
| 1 | 0 | 182868.3 | 25.063% | 7.783381 | 48.833% | 0.100371 | 2.743491 | 0.293038 | 0.821571 | 82.873% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
