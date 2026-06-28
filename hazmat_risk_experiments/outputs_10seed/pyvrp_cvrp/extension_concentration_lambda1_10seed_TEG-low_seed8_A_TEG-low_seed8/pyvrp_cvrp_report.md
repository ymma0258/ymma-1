# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.325140 | 0.000% | 0.252710 | 2.391842 | 0.135789 | 0.848338 | 87.650% |
| 1 | 0 | 161900.6 | 20.824% | 3.704421 | 55.503% | 0.092309 | 1.219703 | 0.265453 | 0.757616 | 75.247% |
| 1 | 1 | 175194.3 | 30.744% | 2.970049 | 64.324% | 0.058062 | 1.204555 | 0.282946 | 0.703980 | 68.464% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
