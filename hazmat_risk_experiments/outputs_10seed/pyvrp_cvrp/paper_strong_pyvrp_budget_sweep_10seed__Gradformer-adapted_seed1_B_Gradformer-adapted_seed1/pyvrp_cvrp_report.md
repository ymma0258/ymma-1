# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.9 | 0.000% | 8.715727 | 0.000% | 0.255787 | 2.827580 | 0.221569 | 0.861919 | 89.046% |
| 0.25 | 0 | 158142.4 | 7.387% | 7.850669 | 9.925% | 0.220435 | 2.644279 | 0.226433 | 0.858195 | 88.580% |
| 0.5 | 0 | 168770.0 | 14.604% | 5.923703 | 32.034% | 0.151525 | 1.699963 | 0.191495 | 0.846276 | 86.487% |
| 1 | 0 | 181842.1 | 23.480% | 4.209257 | 51.705% | 0.112475 | 1.408510 | 0.272226 | 0.818834 | 81.866% |
| 2 | 0 | 201170.4 | 36.605% | 3.250960 | 62.700% | 0.077497 | 1.140935 | 0.289289 | 0.788549 | 76.368% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
