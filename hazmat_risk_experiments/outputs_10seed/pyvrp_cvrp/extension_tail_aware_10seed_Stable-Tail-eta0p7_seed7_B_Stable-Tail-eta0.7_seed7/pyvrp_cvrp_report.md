# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 13.899356 | 0.000% | 0.260998 | 4.377161 | 0.186557 | 0.879443 | 90.839% |
| 1 | 0 | 179273.9 | 22.179% | 5.388516 | 61.232% | 0.067715 | 1.884626 | 0.286361 | 0.828755 | 79.675% |
| 2 | 0 | 197390.4 | 34.525% | 4.718209 | 66.054% | 0.058255 | 1.574267 | 0.290973 | 0.814544 | 76.959% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
