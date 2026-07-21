# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.4 | 0.000% | 8.556073 | 0.000% | 0.273215 | 2.490157 | 0.172631 | 0.881800 | 90.161% |
| 0.25 | 0 | 142590.5 | 6.148% | 5.900428 | 31.038% | 0.169771 | 2.013392 | 0.249460 | 0.873398 | 88.255% |
| 0.5 | 0 | 148353.4 | 10.438% | 3.922338 | 54.157% | 0.116453 | 1.514038 | 0.310338 | 0.837134 | 82.705% |
| 1 | 0 | 155926.3 | 16.076% | 2.798230 | 67.295% | 0.074910 | 1.055664 | 0.268657 | 0.792439 | 76.417% |
| 2 | 0 | 166592.4 | 24.016% | 1.910569 | 77.670% | 0.042225 | 0.630471 | 0.258382 | 0.720946 | 66.026% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
