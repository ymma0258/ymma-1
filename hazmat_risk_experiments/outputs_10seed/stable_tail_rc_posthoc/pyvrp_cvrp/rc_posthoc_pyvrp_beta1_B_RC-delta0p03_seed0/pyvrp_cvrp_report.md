# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.6 | 0.000% | 8.055533 | 0.000% | 0.247404 | 2.530684 | 0.223965 | 0.881245 | 90.422% |
| 1 | 0 | 177435.9 | 20.598% | 3.355558 | 58.345% | 0.071909 | 1.318410 | 0.299374 | 0.825878 | 80.505% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
