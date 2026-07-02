# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 12.004003 | 0.000% | 0.293538 | 3.340024 | 0.137755 | 0.845145 | 88.237% |
| 1 | 0 | 162906.7 | 21.574% | 5.068058 | 57.780% | 0.110445 | 1.642948 | 0.227256 | 0.761082 | 76.724% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
