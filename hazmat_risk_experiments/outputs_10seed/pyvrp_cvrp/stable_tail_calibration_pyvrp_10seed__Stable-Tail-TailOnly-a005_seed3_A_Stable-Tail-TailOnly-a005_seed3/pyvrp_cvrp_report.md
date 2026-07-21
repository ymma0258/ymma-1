# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.5 | 0.000% | 7.252826 | 0.000% | 0.212258 | 2.336523 | 0.200571 | 0.876690 | 89.519% |
| 0.25 | 0 | 141615.8 | 5.580% | 4.918525 | 32.185% | 0.142256 | 1.444644 | 0.178269 | 0.857129 | 86.798% |
| 0.5 | 0 | 147314.5 | 9.828% | 3.672221 | 49.368% | 0.104657 | 1.240168 | 0.231785 | 0.833361 | 83.135% |
| 1 | 0 | 155029.5 | 15.580% | 2.455520 | 66.144% | 0.064338 | 0.741663 | 0.202119 | 0.773699 | 74.654% |
| 2 | 0 | 167022.8 | 24.522% | 2.140356 | 70.489% | 0.050895 | 0.696234 | 0.233463 | 0.751861 | 71.536% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
