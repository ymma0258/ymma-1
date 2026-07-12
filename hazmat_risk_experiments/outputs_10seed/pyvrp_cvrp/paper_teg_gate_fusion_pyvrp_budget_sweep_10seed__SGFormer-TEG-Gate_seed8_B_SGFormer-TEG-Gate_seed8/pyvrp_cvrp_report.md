# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 8.706569 | 0.000% | 0.268255 | 2.641219 | 0.177644 | 0.865633 | 88.014% |
| 0.25 | 0 | 156995.1 | 6.801% | 7.275211 | 16.440% | 0.219780 | 2.317294 | 0.184198 | 0.861249 | 86.731% |
| 0.5 | 0 | 165733.0 | 12.746% | 5.202241 | 40.249% | 0.127014 | 1.818599 | 0.272193 | 0.832777 | 82.018% |
| 1 | 0 | 175359.3 | 19.294% | 3.128825 | 64.064% | 0.062906 | 1.145045 | 0.263206 | 0.764227 | 71.925% |
| 2 | 0 | 188502.2 | 28.235% | 2.584393 | 70.317% | 0.046022 | 0.771048 | 0.205270 | 0.737902 | 67.312% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
