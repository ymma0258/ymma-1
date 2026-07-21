# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 7.945409 | 0.000% | 0.244013 | 2.280409 | 0.167531 | 0.871042 | 89.011% |
| 0.25 | 0 | 142661.5 | 6.413% | 5.595374 | 29.577% | 0.157790 | 1.732468 | 0.235769 | 0.858739 | 87.125% |
| 0.5 | 0 | 148995.1 | 11.137% | 4.202310 | 47.110% | 0.124864 | 1.707758 | 0.273114 | 0.833508 | 83.363% |
| 1 | 0 | 157961.1 | 17.825% | 2.992111 | 62.342% | 0.073334 | 0.834298 | 0.142383 | 0.793150 | 77.346% |
| 2 | 0 | 172666.4 | 28.793% | 2.244106 | 71.756% | 0.043054 | 0.707411 | 0.214712 | 0.746624 | 70.150% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
