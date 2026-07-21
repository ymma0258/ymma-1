# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.3 | 0.000% | 9.395238 | 0.000% | 0.295316 | 3.064604 | 0.217557 | 0.871494 | 90.264% |
| 0.25 | 0 | 158804.0 | 7.885% | 8.178526 | 12.950% | 0.240566 | 2.650689 | 0.210963 | 0.873635 | 90.093% |
| 0.5 | 0 | 168150.1 | 14.235% | 5.178245 | 44.884% | 0.146298 | 1.798903 | 0.297178 | 0.853312 | 85.663% |
| 1 | 0 | 179474.7 | 21.928% | 3.527192 | 62.458% | 0.074351 | 1.136709 | 0.254785 | 0.813534 | 79.379% |
| 2 | 0 | 197528.4 | 34.193% | 3.233971 | 65.579% | 0.064966 | 1.017352 | 0.246425 | 0.799315 | 77.298% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
