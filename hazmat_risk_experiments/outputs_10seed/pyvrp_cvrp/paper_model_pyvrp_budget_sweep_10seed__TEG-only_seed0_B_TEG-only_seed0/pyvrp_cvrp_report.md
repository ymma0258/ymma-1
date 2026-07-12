# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.0 | 0.000% | 8.214998 | 0.000% | 0.239215 | 2.538980 | 0.211523 | 0.832388 | 86.283% |
| 0.25 | 0 | 157409.2 | 6.889% | 7.118781 | 13.344% | 0.191257 | 2.113348 | 0.187165 | 0.823831 | 85.018% |
| 0.5 | 0 | 166565.0 | 13.106% | 5.487306 | 33.204% | 0.133158 | 1.890254 | 0.235946 | 0.791886 | 80.707% |
| 1 | 0 | 179574.7 | 21.941% | 4.161240 | 49.346% | 0.084347 | 1.410740 | 0.238061 | 0.740308 | 74.332% |
| 2 | 0 | 198052.9 | 34.488% | 3.042547 | 62.964% | 0.056909 | 1.178014 | 0.260354 | 0.667066 | 65.200% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
