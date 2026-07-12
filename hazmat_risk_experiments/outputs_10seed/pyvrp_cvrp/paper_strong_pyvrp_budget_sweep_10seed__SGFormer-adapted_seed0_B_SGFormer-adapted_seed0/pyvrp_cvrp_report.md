# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147397.2 | 0.000% | 9.584135 | 0.000% | 0.289807 | 2.909316 | 0.191589 | 0.855214 | 88.602% |
| 0.25 | 0 | 158804.2 | 7.739% | 8.106781 | 15.415% | 0.197971 | 2.332970 | 0.165062 | 0.854683 | 88.628% |
| 0.5 | 0 | 169923.5 | 15.283% | 5.996493 | 37.433% | 0.146833 | 2.168614 | 0.276561 | 0.829861 | 84.806% |
| 1 | 0 | 183496.9 | 24.491% | 4.436374 | 53.711% | 0.106433 | 1.632768 | 0.302820 | 0.800464 | 79.972% |
| 2 | 0 | 205375.7 | 39.335% | 3.660343 | 61.808% | 0.078879 | 1.235892 | 0.287152 | 0.775633 | 75.733% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
