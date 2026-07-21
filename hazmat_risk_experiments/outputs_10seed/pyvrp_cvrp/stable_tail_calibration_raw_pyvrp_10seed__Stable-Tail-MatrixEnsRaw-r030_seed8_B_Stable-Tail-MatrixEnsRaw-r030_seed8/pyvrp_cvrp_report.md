# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.0 | 0.000% | 5.451080 | 0.000% | 0.164172 | 1.627020 | 0.186351 | 0.862971 | 88.039% |
| 0.25 | 0 | 156368.1 | 6.230% | 4.461226 | 18.159% | 0.108278 | 1.472601 | 0.211384 | 0.857881 | 87.108% |
| 0.5 | 0 | 165013.6 | 12.104% | 3.311538 | 39.250% | 0.081754 | 1.080881 | 0.230731 | 0.834356 | 83.351% |
| 1 | 0 | 175793.0 | 19.427% | 2.348488 | 56.917% | 0.055421 | 0.737242 | 0.216484 | 0.794601 | 77.430% |
| 2 | 0 | 190248.1 | 29.247% | 1.776715 | 67.406% | 0.039166 | 0.480370 | 0.165393 | 0.757841 | 71.349% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
