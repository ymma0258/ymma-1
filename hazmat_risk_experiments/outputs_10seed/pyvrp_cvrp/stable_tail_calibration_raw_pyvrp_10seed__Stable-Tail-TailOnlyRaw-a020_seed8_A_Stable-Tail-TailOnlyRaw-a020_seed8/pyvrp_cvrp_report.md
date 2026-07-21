# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.2 | 0.000% | 8.549392 | 0.000% | 0.270649 | 2.568823 | 0.185169 | 0.875277 | 89.705% |
| 0.25 | 0 | 142922.2 | 6.501% | 5.584379 | 34.681% | 0.157014 | 1.690366 | 0.215263 | 0.857574 | 86.914% |
| 0.5 | 0 | 149364.5 | 11.301% | 4.251839 | 50.267% | 0.124346 | 1.495190 | 0.243872 | 0.836011 | 83.469% |
| 1 | 0 | 158161.9 | 17.857% | 3.084387 | 63.923% | 0.081942 | 0.978833 | 0.210144 | 0.794497 | 77.430% |
| 2 | 0 | 172334.0 | 28.418% | 2.416285 | 71.737% | 0.046561 | 0.738172 | 0.223980 | 0.760891 | 72.112% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
