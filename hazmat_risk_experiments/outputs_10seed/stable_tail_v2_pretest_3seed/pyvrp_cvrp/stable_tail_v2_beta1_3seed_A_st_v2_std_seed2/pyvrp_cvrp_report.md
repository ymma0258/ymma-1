# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 4.373013 | 0.000% | 0.121991 | 1.251353 | 0.165782 | 0.689064 | 70.952% |
| 1 | 0 | 168282.3 | 25.586% | 2.832583 | 35.226% | 0.045963 | 0.912090 | 0.161341 | 0.583218 | 59.159% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
