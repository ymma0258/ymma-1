# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 8.687382 | 0.000% | 0.267523 | 2.588228 | 0.141061 | 0.847332 | 87.672% |
| 1 | 0 | 161521.1 | 20.540% | 3.658036 | 57.893% | 0.086245 | 1.305158 | 0.307141 | 0.746536 | 73.784% |
| 1 | 1 | 173637.5 | 29.583% | 2.894011 | 66.687% | 0.053783 | 1.129074 | 0.303675 | 0.689786 | 66.650% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
