# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 7.703690 | 0.000% | 0.244752 | 2.198497 | 0.165860 | 0.871164 | 89.551% |
| 0.25 | 0 | 143158.6 | 6.783% | 5.342945 | 30.644% | 0.157180 | 1.629153 | 0.208606 | 0.859712 | 87.725% |
| 0.5 | 0 | 149557.2 | 11.556% | 4.060669 | 47.289% | 0.100126 | 1.626873 | 0.267582 | 0.831344 | 84.166% |
| 1 | 0 | 158561.0 | 18.272% | 2.602561 | 66.217% | 0.057484 | 0.930501 | 0.262196 | 0.773285 | 75.624% |
| 2 | 0 | 172730.3 | 28.841% | 2.169653 | 71.836% | 0.048623 | 0.647219 | 0.197163 | 0.743138 | 71.335% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
