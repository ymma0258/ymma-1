# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.7 | 0.000% | 7.979581 | 0.000% | 0.234142 | 2.295587 | 0.157397 | 0.873649 | 89.593% |
| 0.25 | 0 | 143868.8 | 7.367% | 5.224242 | 34.530% | 0.138818 | 1.739146 | 0.264768 | 0.858204 | 86.413% |
| 0.5 | 0 | 150689.9 | 12.457% | 4.204405 | 47.310% | 0.120390 | 1.348668 | 0.242752 | 0.836455 | 83.335% |
| 1 | 0 | 160298.5 | 19.628% | 2.982331 | 62.625% | 0.081266 | 1.069375 | 0.314271 | 0.799311 | 77.540% |
| 2 | 0 | 175645.6 | 31.081% | 2.293867 | 71.253% | 0.042350 | 0.902686 | 0.303814 | 0.760008 | 71.399% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
