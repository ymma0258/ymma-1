# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.3 | 0.000% | 9.577869 | 0.000% | 0.310038 | 2.840528 | 0.177432 | 0.879672 | 89.575% |
| 0.25 | 0 | 144264.4 | 7.394% | 6.482175 | 32.321% | 0.200246 | 2.249070 | 0.250374 | 0.871542 | 87.249% |
| 0.5 | 0 | 151337.3 | 12.660% | 4.622575 | 51.737% | 0.132236 | 1.599961 | 0.284291 | 0.841616 | 82.661% |
| 1 | 0 | 161379.3 | 20.135% | 3.371013 | 64.804% | 0.089559 | 1.088676 | 0.265499 | 0.800718 | 76.605% |
| 2 | 0 | 177182.2 | 31.899% | 2.870282 | 70.032% | 0.065522 | 1.131714 | 0.347668 | 0.779687 | 73.274% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
