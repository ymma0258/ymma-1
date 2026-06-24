# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.087394 | 0.000% | 0.239417 | 2.377408 | 0.159303 | 0.864635 | 89.138% |
| 1 | 0 | 159022.1 | 18.675% | 3.145461 | 61.107% | 0.080400 | 1.179146 | 0.291559 | 0.786355 | 76.895% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
