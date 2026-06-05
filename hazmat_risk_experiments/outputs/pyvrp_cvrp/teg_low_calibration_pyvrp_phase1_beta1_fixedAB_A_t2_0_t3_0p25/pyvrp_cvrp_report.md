# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 8.297300 | 0.000% | 0.276488 | 2.668333 | 0.213890 | 0.839134 | 86.884% |
| 1 | 0 | 160249.6 | 19.592% | 3.334917 | 59.807% | 0.082551 | 1.229312 | 0.245418 | 0.715527 | 70.558% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
