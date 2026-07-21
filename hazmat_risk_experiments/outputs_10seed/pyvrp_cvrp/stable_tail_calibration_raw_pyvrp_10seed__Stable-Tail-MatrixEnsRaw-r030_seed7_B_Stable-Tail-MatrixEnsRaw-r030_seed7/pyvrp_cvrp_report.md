# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.6 | 0.000% | 7.109173 | 0.000% | 0.211228 | 2.175640 | 0.199227 | 0.879903 | 90.724% |
| 0.25 | 0 | 157577.1 | 7.100% | 5.935045 | 16.516% | 0.168366 | 1.978518 | 0.229730 | 0.876975 | 89.898% |
| 0.5 | 0 | 166987.6 | 13.496% | 4.301725 | 39.491% | 0.125418 | 1.378180 | 0.226823 | 0.861392 | 86.203% |
| 1 | 0 | 178498.1 | 21.319% | 2.823837 | 60.279% | 0.073629 | 0.960795 | 0.250824 | 0.828679 | 80.454% |
| 2 | 0 | 195465.7 | 32.852% | 2.398102 | 66.267% | 0.052533 | 0.782996 | 0.236316 | 0.812353 | 77.491% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
