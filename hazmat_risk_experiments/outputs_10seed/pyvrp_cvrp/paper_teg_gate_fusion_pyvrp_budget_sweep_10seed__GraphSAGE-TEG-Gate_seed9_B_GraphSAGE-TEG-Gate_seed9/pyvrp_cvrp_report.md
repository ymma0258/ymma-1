# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 7.514705 | 0.000% | 0.232323 | 2.466552 | 0.219601 | 0.878201 | 88.837% |
| 0.25 | 0 | 155861.2 | 6.126% | 6.231869 | 17.071% | 0.179396 | 2.314569 | 0.264219 | 0.870316 | 87.695% |
| 0.5 | 0 | 163938.4 | 11.626% | 4.435606 | 40.974% | 0.101374 | 1.533098 | 0.242951 | 0.845882 | 83.985% |
| 1 | 0 | 173561.5 | 18.178% | 3.003602 | 60.030% | 0.070059 | 1.018267 | 0.257130 | 0.816978 | 78.534% |
| 2 | 0 | 187052.4 | 27.364% | 2.240765 | 70.182% | 0.049820 | 0.738997 | 0.221629 | 0.774581 | 71.505% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
