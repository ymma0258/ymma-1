# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.6 | 0.000% | 7.817855 | 0.000% | 0.245475 | 2.318063 | 0.192963 | 0.880664 | 89.985% |
| 0.25 | 0 | 142625.9 | 6.227% | 4.736436 | 39.415% | 0.141002 | 1.527969 | 0.210944 | 0.862003 | 86.491% |
| 0.5 | 0 | 148574.8 | 10.658% | 3.648210 | 53.335% | 0.101031 | 1.414877 | 0.283350 | 0.833372 | 82.480% |
| 1 | 0 | 156374.3 | 16.467% | 2.362372 | 69.782% | 0.051681 | 0.937105 | 0.270137 | 0.777096 | 74.092% |
| 2 | 0 | 168700.6 | 25.648% | 1.663237 | 78.725% | 0.031287 | 0.501031 | 0.201303 | 0.707455 | 63.476% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
