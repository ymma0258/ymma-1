# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147131.1 | 0.000% | 7.156809 | 0.000% | 0.219951 | 2.823313 | 0.338968 | 0.872141 | 88.006% |
| 0.25 | 0 | 154505.4 | 5.012% | 5.935895 | 17.059% | 0.176344 | 2.142131 | 0.306716 | 0.864523 | 86.170% |
| 0.5 | 0 | 160202.8 | 8.884% | 4.351272 | 39.201% | 0.120649 | 1.382598 | 0.256089 | 0.835272 | 81.807% |
| 1 | 0 | 168109.2 | 14.258% | 2.895497 | 59.542% | 0.066911 | 1.027133 | 0.296451 | 0.784522 | 74.008% |
| 2 | 0 | 179016.8 | 21.672% | 2.142033 | 70.070% | 0.036357 | 0.718722 | 0.241034 | 0.729292 | 65.589% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
