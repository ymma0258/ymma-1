# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.822003 | 0.000% | 0.276107 | 2.488443 | 0.144711 | 0.877005 | 90.199% |
| 1 | 0 | 158104.6 | 17.991% | 3.567707 | 59.559% | 0.099053 | 1.108712 | 0.255742 | 0.827507 | 80.375% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
