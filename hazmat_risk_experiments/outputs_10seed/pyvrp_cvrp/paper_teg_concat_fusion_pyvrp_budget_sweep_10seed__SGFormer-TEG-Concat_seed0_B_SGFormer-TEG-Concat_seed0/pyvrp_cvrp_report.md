# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.2 | 0.000% | 8.645324 | 0.000% | 0.259145 | 2.648889 | 0.208927 | 0.862313 | 88.435% |
| 0.25 | 0 | 158579.8 | 7.636% | 7.699272 | 10.943% | 0.212115 | 2.375073 | 0.198611 | 0.858486 | 87.991% |
| 0.5 | 0 | 169006.7 | 14.713% | 5.887290 | 31.902% | 0.159565 | 1.890975 | 0.252798 | 0.842843 | 85.394% |
| 1 | 0 | 183306.7 | 24.419% | 4.367754 | 49.478% | 0.101062 | 1.539347 | 0.278394 | 0.808121 | 80.129% |
| 2 | 0 | 204006.3 | 38.469% | 3.498666 | 59.531% | 0.073316 | 1.333363 | 0.324808 | 0.789603 | 76.349% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
