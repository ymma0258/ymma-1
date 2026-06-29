# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 8.192167 | 0.000% | 0.253325 | 2.299094 | 0.155220 | 0.880119 | 89.842% |
| 1 | 0 | 159004.2 | 18.662% | 2.917628 | 64.385% | 0.076356 | 1.001160 | 0.294183 | 0.804249 | 77.264% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
