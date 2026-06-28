# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.5 | 0.000% | 8.076139 | 0.000% | 0.260157 | 2.469701 | 0.205502 | 0.883330 | 90.469% |
| 1 | 0 | 157284.6 | 17.261% | 2.417339 | 70.068% | 0.051011 | 1.066701 | 0.327281 | 0.787828 | 74.951% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
