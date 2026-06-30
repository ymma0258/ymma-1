# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 8.115282 | 0.000% | 0.276132 | 2.419989 | 0.159287 | 0.872390 | 89.741% |
| 1 | 0 | 158760.7 | 18.480% | 3.263643 | 59.784% | 0.083174 | 1.135064 | 0.274098 | 0.820946 | 79.771% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
