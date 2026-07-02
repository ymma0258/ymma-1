# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 9.420742 | 0.000% | 0.276767 | 3.212709 | 0.249247 | 0.881159 | 90.995% |
| 1 | 0 | 178689.7 | 22.205% | 4.423053 | 53.050% | 0.119900 | 1.632296 | 0.280922 | 0.846488 | 82.810% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
