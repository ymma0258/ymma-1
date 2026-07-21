# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147063.8 | 0.000% | 7.128189 | 0.000% | 0.217315 | 2.373311 | 0.238095 | 0.870602 | 89.162% |
| 0.25 | 0 | 155456.6 | 5.707% | 6.115704 | 14.204% | 0.149125 | 2.069399 | 0.253214 | 0.866948 | 88.465% |
| 0.5 | 0 | 163394.9 | 11.105% | 4.775926 | 32.999% | 0.119466 | 1.842501 | 0.268448 | 0.854844 | 85.835% |
| 1 | 0 | 175034.8 | 19.020% | 3.683443 | 48.326% | 0.093611 | 1.489583 | 0.306128 | 0.839789 | 82.790% |
| 2 | 0 | 192468.0 | 30.874% | 2.811634 | 60.556% | 0.069271 | 1.198124 | 0.304198 | 0.813233 | 77.966% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
