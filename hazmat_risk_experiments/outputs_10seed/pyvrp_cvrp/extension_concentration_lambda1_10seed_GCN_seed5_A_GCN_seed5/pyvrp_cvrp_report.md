# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 6.942359 | 0.000% | 0.196245 | 2.193374 | 0.185055 | 0.866596 | 88.674% |
| 1 | 0 | 156669.3 | 16.920% | 2.573161 | 62.935% | 0.067494 | 0.943918 | 0.258365 | 0.770789 | 74.948% |
| 1 | 1 | 166946.6 | 24.589% | 2.183373 | 68.550% | 0.039185 | 0.757136 | 0.263593 | 0.743738 | 70.651% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
