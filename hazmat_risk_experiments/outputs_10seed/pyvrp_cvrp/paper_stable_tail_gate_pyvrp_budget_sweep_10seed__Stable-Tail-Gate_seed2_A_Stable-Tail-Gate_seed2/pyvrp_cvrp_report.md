# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.4 | 0.000% | 9.212544 | 0.000% | 0.289461 | 2.523050 | 0.142992 | 0.864150 | 88.906% |
| 0.25 | 0 | 142610.7 | 6.322% | 6.083337 | 33.967% | 0.181813 | 1.956365 | 0.215759 | 0.851517 | 87.117% |
| 0.5 | 0 | 149044.2 | 11.118% | 4.968481 | 46.068% | 0.147749 | 1.817578 | 0.276330 | 0.839468 | 84.797% |
| 1 | 0 | 158577.3 | 18.225% | 3.528685 | 61.697% | 0.087785 | 1.212632 | 0.310061 | 0.798804 | 78.892% |
| 2 | 0 | 174097.8 | 29.796% | 3.273217 | 64.470% | 0.076164 | 1.149369 | 0.306360 | 0.787659 | 77.316% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
