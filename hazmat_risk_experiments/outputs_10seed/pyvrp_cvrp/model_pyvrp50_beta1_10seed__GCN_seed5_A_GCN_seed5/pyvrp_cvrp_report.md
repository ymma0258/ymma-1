# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 6.793624 | 0.000% | 0.194298 | 2.078779 | 0.183395 | 0.864754 | 88.450% |
| 1 | 0 | 156669.3 | 16.919% | 2.573161 | 62.124% | 0.067494 | 0.943918 | 0.258365 | 0.770789 | 74.948% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
