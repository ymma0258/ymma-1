# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 13.453350 | 0.000% | 0.289160 | 3.554351 | 0.136349 | 0.846539 | 88.439% |
| 1 | 0 | 162081.7 | 20.959% | 5.640266 | 58.075% | 0.076550 | 1.974601 | 0.263533 | 0.782033 | 77.762% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
