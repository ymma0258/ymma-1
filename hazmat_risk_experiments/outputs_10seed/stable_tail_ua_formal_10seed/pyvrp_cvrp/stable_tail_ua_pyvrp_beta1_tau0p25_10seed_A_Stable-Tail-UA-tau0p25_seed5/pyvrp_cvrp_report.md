# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 10.484908 | 0.000% | 0.255078 | 3.034653 | 0.152398 | 0.852508 | 88.503% |
| 1 | 0 | 162959.1 | 21.613% | 4.143246 | 60.484% | 0.086901 | 1.548113 | 0.305938 | 0.760387 | 75.840% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
