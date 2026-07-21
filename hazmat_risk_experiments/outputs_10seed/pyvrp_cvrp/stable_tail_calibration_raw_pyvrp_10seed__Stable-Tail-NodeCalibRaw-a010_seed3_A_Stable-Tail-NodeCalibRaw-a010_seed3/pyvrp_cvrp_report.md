# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134464.4 | 0.000% | 6.990543 | 0.000% | 0.211514 | 2.112887 | 0.177598 | 0.870480 | 88.641% |
| 0.25 | 0 | 141808.4 | 5.462% | 4.736131 | 32.249% | 0.138251 | 1.376189 | 0.176554 | 0.853487 | 86.300% |
| 0.5 | 0 | 147343.6 | 9.578% | 3.673282 | 47.454% | 0.108718 | 1.155490 | 0.204119 | 0.836392 | 83.443% |
| 1 | 0 | 155489.6 | 15.636% | 2.423229 | 65.336% | 0.063496 | 0.761538 | 0.221969 | 0.773006 | 74.799% |
| 2 | 0 | 168027.2 | 24.960% | 2.082516 | 70.210% | 0.049177 | 0.770636 | 0.287938 | 0.747864 | 70.579% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
