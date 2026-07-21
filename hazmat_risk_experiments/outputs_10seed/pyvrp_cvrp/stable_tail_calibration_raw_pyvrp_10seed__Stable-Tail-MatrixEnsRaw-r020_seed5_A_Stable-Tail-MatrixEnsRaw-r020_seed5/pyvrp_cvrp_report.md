# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.6 | 0.000% | 5.837302 | 0.000% | 0.179654 | 1.811779 | 0.192369 | 0.874859 | 88.938% |
| 0.25 | 0 | 142522.5 | 6.256% | 3.601029 | 38.310% | 0.101318 | 1.205350 | 0.252325 | 0.847345 | 84.683% |
| 0.5 | 0 | 147971.2 | 10.318% | 2.910431 | 50.141% | 0.085118 | 1.087060 | 0.309154 | 0.828525 | 81.688% |
| 1 | 0 | 156067.8 | 16.354% | 2.089661 | 64.202% | 0.054402 | 0.812780 | 0.265833 | 0.773938 | 74.081% |
| 2 | 0 | 167362.1 | 24.775% | 1.454337 | 75.085% | 0.031236 | 0.487094 | 0.234292 | 0.710670 | 64.653% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
