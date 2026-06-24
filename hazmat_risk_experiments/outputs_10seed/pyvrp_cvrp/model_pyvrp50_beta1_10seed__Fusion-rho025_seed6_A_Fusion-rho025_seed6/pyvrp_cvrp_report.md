# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.933309 | 0.000% | 0.245692 | 2.282989 | 0.140308 | 0.863056 | 88.860% |
| 1 | 0 | 159371.7 | 18.936% | 3.250206 | 59.031% | 0.070182 | 1.076786 | 0.273953 | 0.787584 | 77.806% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
