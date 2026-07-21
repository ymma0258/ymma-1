# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.707655 | 0.000% | 0.237704 | 2.525842 | 0.217574 | 0.862230 | 88.519% |
| 0.25 | 0 | 156658.0 | 6.766% | 6.674029 | 13.410% | 0.161075 | 2.085192 | 0.215986 | 0.858572 | 87.992% |
| 0.5 | 0 | 166039.1 | 13.159% | 4.502573 | 41.583% | 0.103322 | 1.507221 | 0.244716 | 0.822348 | 82.621% |
| 1 | 0 | 177053.8 | 20.666% | 3.389584 | 56.023% | 0.081673 | 1.236685 | 0.309363 | 0.794320 | 78.010% |
| 2 | 0 | 193918.0 | 32.159% | 2.747427 | 64.355% | 0.064437 | 0.868010 | 0.234114 | 0.758537 | 73.010% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
