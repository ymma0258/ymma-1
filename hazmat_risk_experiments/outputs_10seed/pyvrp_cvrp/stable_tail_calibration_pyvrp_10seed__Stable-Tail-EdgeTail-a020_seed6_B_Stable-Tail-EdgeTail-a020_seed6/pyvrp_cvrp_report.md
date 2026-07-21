# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 9.139589 | 0.000% | 0.283566 | 2.970734 | 0.219059 | 0.870967 | 89.339% |
| 0.25 | 0 | 157649.3 | 7.344% | 7.892246 | 13.648% | 0.192116 | 2.547598 | 0.241307 | 0.869181 | 89.291% |
| 0.5 | 0 | 167994.0 | 14.388% | 6.095980 | 33.301% | 0.152535 | 1.981422 | 0.253479 | 0.855845 | 86.450% |
| 1 | 0 | 181381.6 | 23.503% | 4.178709 | 54.279% | 0.103450 | 1.532413 | 0.295131 | 0.825951 | 80.943% |
| 2 | 0 | 201517.5 | 37.214% | 3.752650 | 58.941% | 0.095405 | 1.459244 | 0.334600 | 0.817442 | 79.332% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
