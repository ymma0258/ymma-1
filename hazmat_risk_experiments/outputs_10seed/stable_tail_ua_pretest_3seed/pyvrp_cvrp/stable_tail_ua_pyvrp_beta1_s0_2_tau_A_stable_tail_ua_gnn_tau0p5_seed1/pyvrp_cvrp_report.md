# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 15.208442 | 0.000% | 0.278225 | 4.029643 | 0.132952 | 0.823223 | 86.496% |
| 1 | 0 | 165266.7 | 23.336% | 6.577000 | 56.754% | 0.057934 | 1.858683 | 0.153802 | 0.727171 | 73.561% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
