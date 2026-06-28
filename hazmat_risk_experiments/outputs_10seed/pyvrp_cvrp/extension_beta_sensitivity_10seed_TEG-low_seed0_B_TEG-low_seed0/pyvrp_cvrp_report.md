# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.667610 | 0.000% | 0.252714 | 2.692394 | 0.194748 | 0.841308 | 87.391% |
| 0.5 | 0 | 166870.7 | 13.726% | 5.586627 | 35.546% | 0.136521 | 1.720278 | 0.208658 | 0.801599 | 81.563% |
| 1 | 0 | 178449.7 | 21.617% | 3.586248 | 58.625% | 0.075606 | 1.221459 | 0.237710 | 0.717435 | 71.381% |
| 1.5 | 0 | 187245.5 | 27.611% | 3.085002 | 64.408% | 0.059000 | 1.082445 | 0.256317 | 0.678740 | 66.515% |
| 2 | 0 | 195076.5 | 32.948% | 2.903355 | 66.503% | 0.054498 | 1.129956 | 0.279255 | 0.660968 | 64.411% |
| 3 | 0 | 208824.5 | 42.318% | 2.650324 | 69.423% | 0.047937 | 1.015731 | 0.293448 | 0.637705 | 61.344% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
