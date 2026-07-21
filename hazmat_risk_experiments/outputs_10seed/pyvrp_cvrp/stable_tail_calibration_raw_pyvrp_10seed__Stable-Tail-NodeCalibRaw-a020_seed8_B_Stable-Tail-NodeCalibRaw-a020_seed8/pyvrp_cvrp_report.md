# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.8 | 0.000% | 7.314943 | 0.000% | 0.196558 | 2.421989 | 0.222362 | 0.858145 | 87.510% |
| 0.25 | 0 | 156767.9 | 6.550% | 6.089946 | 16.747% | 0.147005 | 1.942440 | 0.203909 | 0.853233 | 86.379% |
| 0.5 | 0 | 165586.0 | 12.543% | 4.936221 | 32.519% | 0.122724 | 1.616101 | 0.233665 | 0.837443 | 83.861% |
| 1 | 0 | 176552.3 | 19.997% | 3.066960 | 58.073% | 0.067530 | 1.034373 | 0.233184 | 0.782897 | 75.419% |
| 2 | 0 | 191757.6 | 30.331% | 2.467568 | 66.267% | 0.049000 | 0.732626 | 0.204252 | 0.751519 | 70.283% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
