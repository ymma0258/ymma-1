# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146931.0 | 0.000% | 9.696913 | 0.000% | 0.292918 | 3.056694 | 0.205861 | 0.883725 | 90.526% |
| 0.25 | 0 | 156218.0 | 6.321% | 8.206527 | 15.370% | 0.236574 | 2.591538 | 0.223616 | 0.881725 | 89.716% |
| 0.5 | 0 | 164188.0 | 11.745% | 6.362438 | 34.387% | 0.175087 | 2.423741 | 0.335691 | 0.868613 | 87.141% |
| 1 | 0 | 174548.9 | 18.797% | 4.224946 | 56.430% | 0.108869 | 1.845957 | 0.360803 | 0.833550 | 81.549% |
| 2 | 0 | 190335.9 | 29.541% | 3.588614 | 62.992% | 0.076616 | 1.422390 | 0.295750 | 0.821951 | 79.525% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
