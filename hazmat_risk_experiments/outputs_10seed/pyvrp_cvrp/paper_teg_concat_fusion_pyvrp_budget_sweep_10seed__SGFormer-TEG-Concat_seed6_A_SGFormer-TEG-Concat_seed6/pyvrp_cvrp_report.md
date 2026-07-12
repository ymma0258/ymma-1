# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.9 | 0.000% | 7.961059 | 0.000% | 0.233391 | 2.281526 | 0.163169 | 0.863236 | 88.432% |
| 0.25 | 0 | 144492.2 | 7.778% | 5.291880 | 33.528% | 0.153823 | 1.565770 | 0.217234 | 0.845277 | 85.538% |
| 0.5 | 0 | 151744.4 | 13.187% | 4.012497 | 49.598% | 0.118207 | 1.361117 | 0.247070 | 0.816745 | 81.248% |
| 1 | 0 | 162433.9 | 21.161% | 2.768695 | 65.222% | 0.070683 | 0.883856 | 0.251079 | 0.762682 | 73.185% |
| 2 | 0 | 178101.7 | 32.847% | 2.394415 | 69.923% | 0.056173 | 0.816701 | 0.281681 | 0.735236 | 69.303% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
