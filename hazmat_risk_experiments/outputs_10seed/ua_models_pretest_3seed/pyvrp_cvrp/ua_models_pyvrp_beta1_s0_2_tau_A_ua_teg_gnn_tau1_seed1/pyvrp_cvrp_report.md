# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 15.743686 | 0.000% | 0.273761 | 4.302089 | 0.157082 | 0.833407 | 87.504% |
| 1 | 0 | 165656.0 | 23.626% | 6.683884 | 57.546% | 0.049998 | 2.263497 | 0.229808 | 0.754834 | 75.604% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
