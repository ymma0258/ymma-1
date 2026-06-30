# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 8.226247 | 0.000% | 0.274604 | 2.495590 | 0.167984 | 0.874854 | 89.927% |
| 1 | 0 | 159289.0 | 18.875% | 3.209758 | 60.982% | 0.077439 | 1.142389 | 0.279283 | 0.823022 | 79.788% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
