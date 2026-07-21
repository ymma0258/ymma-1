# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.2 | 0.000% | 7.509368 | 0.000% | 0.227147 | 2.345729 | 0.189167 | 0.872607 | 88.985% |
| 0.25 | 0 | 156168.6 | 6.239% | 6.608851 | 11.992% | 0.192732 | 2.179511 | 0.201805 | 0.870192 | 88.408% |
| 0.5 | 0 | 164873.7 | 12.161% | 5.217717 | 30.517% | 0.138868 | 1.770754 | 0.293146 | 0.855194 | 85.539% |
| 1 | 0 | 175349.1 | 19.287% | 3.444029 | 54.137% | 0.086790 | 1.314013 | 0.320881 | 0.816442 | 79.577% |
| 2 | 0 | 192051.0 | 30.649% | 2.815635 | 62.505% | 0.060544 | 1.075556 | 0.303396 | 0.797104 | 76.307% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
