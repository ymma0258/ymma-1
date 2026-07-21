# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 9.164544 | 0.000% | 0.283084 | 2.556293 | 0.155817 | 0.880932 | 90.531% |
| 0.25 | 0 | 142974.9 | 6.699% | 6.975590 | 23.885% | 0.215094 | 2.081698 | 0.210254 | 0.875007 | 89.215% |
| 0.5 | 0 | 149741.9 | 11.749% | 5.121437 | 44.117% | 0.155765 | 1.709438 | 0.248456 | 0.856763 | 86.045% |
| 1 | 0 | 159097.2 | 18.731% | 3.681484 | 59.829% | 0.098117 | 1.170691 | 0.264947 | 0.822235 | 80.958% |
| 2 | 0 | 173804.1 | 29.706% | 2.967171 | 67.623% | 0.072397 | 1.070810 | 0.338656 | 0.799149 | 77.229% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
