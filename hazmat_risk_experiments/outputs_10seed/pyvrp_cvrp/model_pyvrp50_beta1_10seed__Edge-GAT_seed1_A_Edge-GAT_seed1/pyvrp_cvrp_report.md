# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.391286 | 0.000% | 0.212742 | 2.195053 | 0.167035 | 0.861887 | 88.021% |
| 1 | 0 | 155279.1 | 15.882% | 2.769873 | 62.525% | 0.069437 | 0.871328 | 0.197875 | 0.758655 | 73.112% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
