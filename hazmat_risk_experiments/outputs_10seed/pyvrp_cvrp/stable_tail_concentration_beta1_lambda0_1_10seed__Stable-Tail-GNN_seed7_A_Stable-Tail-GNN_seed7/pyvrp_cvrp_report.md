# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.701649 | 0.000% | 0.270892 | 2.469651 | 0.147285 | 0.874652 | 89.737% |
| 1 | 0 | 158498.5 | 18.285% | 3.260477 | 62.530% | 0.072756 | 1.191802 | 0.291764 | 0.805873 | 77.756% |
| 1 | 1 | 167925.1 | 25.319% | 2.455267 | 71.784% | 0.047519 | 0.827664 | 0.273661 | 0.756087 | 70.062% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
