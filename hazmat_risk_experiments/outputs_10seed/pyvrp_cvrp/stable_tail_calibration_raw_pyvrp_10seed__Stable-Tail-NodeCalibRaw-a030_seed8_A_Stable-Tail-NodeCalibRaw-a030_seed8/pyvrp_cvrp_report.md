# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.2 | 0.000% | 7.960526 | 0.000% | 0.246397 | 2.437330 | 0.178179 | 0.866478 | 88.178% |
| 0.25 | 0 | 143080.5 | 6.619% | 5.764688 | 27.584% | 0.169510 | 1.773305 | 0.228221 | 0.859961 | 87.326% |
| 0.5 | 0 | 149741.4 | 11.582% | 3.916711 | 50.798% | 0.106050 | 1.305844 | 0.218325 | 0.822472 | 81.749% |
| 1 | 0 | 158839.0 | 18.361% | 2.957174 | 62.852% | 0.067882 | 0.778135 | 0.145218 | 0.788652 | 76.803% |
| 2 | 0 | 173974.0 | 29.640% | 2.233679 | 71.941% | 0.049659 | 0.689455 | 0.219314 | 0.742193 | 69.453% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
