# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.921122 | 0.000% | 0.230336 | 2.781520 | 0.187972 | 0.836034 | 86.972% |
| 0.5 | 0 | 166244.8 | 13.299% | 6.154648 | 31.010% | 0.152014 | 1.853647 | 0.206893 | 0.802941 | 82.204% |
| 1 | 0 | 177702.0 | 21.107% | 3.599174 | 59.656% | 0.080974 | 1.169411 | 0.230311 | 0.700024 | 69.527% |
| 1.5 | 0 | 186181.4 | 26.886% | 3.279162 | 63.243% | 0.068661 | 1.005637 | 0.232831 | 0.677032 | 66.537% |
| 2 | 0 | 193727.0 | 32.029% | 2.961846 | 66.800% | 0.056437 | 0.992069 | 0.238992 | 0.649912 | 62.986% |
| 3 | 0 | 207810.8 | 41.627% | 2.903939 | 67.449% | 0.051882 | 0.991435 | 0.260741 | 0.647951 | 62.459% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
