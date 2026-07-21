# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.2 | 0.000% | 9.835285 | 0.000% | 0.329686 | 2.979248 | 0.183669 | 0.886453 | 91.031% |
| 0.25 | 0 | 141901.8 | 5.898% | 6.692515 | 31.954% | 0.200874 | 2.213884 | 0.240172 | 0.878611 | 89.206% |
| 0.5 | 0 | 147925.8 | 10.394% | 5.129219 | 47.849% | 0.154062 | 2.090399 | 0.307352 | 0.861754 | 86.422% |
| 1 | 0 | 156709.9 | 16.949% | 3.666580 | 62.720% | 0.101012 | 1.448918 | 0.324050 | 0.831100 | 81.559% |
| 2 | 0 | 170960.0 | 27.584% | 3.349671 | 65.942% | 0.087709 | 1.451100 | 0.345763 | 0.817756 | 79.378% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
