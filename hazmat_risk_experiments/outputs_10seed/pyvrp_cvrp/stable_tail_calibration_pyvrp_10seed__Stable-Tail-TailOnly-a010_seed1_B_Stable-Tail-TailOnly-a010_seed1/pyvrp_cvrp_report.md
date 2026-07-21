# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.6 | 0.000% | 9.701395 | 0.000% | 0.306465 | 3.377451 | 0.260237 | 0.873279 | 89.846% |
| 0.25 | 0 | 156181.6 | 6.152% | 7.925005 | 18.311% | 0.231045 | 2.631166 | 0.262616 | 0.868725 | 88.496% |
| 0.5 | 0 | 164608.4 | 11.879% | 6.275768 | 35.311% | 0.177299 | 1.991516 | 0.221482 | 0.857021 | 86.166% |
| 1 | 0 | 174711.1 | 18.746% | 4.071651 | 58.030% | 0.096188 | 1.369734 | 0.246425 | 0.817722 | 79.689% |
| 2 | 0 | 188147.8 | 27.878% | 3.325078 | 65.726% | 0.064726 | 1.165614 | 0.278074 | 0.797888 | 76.161% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
