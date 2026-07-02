# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 15.333179 | 0.000% | 0.288224 | 4.088719 | 0.135923 | 0.824959 | 86.807% |
| 1 | 0 | 164848.0 | 23.023% | 6.332282 | 58.702% | 0.060776 | 2.298341 | 0.297999 | 0.731853 | 73.969% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
