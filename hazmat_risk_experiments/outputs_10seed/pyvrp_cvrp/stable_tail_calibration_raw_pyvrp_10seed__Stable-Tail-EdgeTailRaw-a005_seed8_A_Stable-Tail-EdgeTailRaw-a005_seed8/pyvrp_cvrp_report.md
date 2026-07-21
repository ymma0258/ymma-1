# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134397.9 | 0.000% | 8.142112 | 0.000% | 0.262570 | 2.372410 | 0.174664 | 0.867186 | 88.310% |
| 0.25 | 0 | 143293.0 | 6.618% | 5.259607 | 35.402% | 0.149817 | 1.662179 | 0.208861 | 0.853476 | 86.320% |
| 0.5 | 0 | 149826.4 | 11.480% | 3.980747 | 51.109% | 0.109733 | 1.419016 | 0.251887 | 0.827105 | 82.183% |
| 1 | 0 | 158874.5 | 18.212% | 2.933978 | 63.965% | 0.071070 | 0.758870 | 0.126315 | 0.787874 | 76.691% |
| 2 | 0 | 173509.9 | 29.102% | 2.189905 | 73.104% | 0.042551 | 0.675548 | 0.211537 | 0.741729 | 69.421% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
