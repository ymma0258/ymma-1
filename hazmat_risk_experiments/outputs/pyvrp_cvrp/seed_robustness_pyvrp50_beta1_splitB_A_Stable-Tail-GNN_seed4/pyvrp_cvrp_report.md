# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 8.407228 | 0.000% | 0.258768 | 2.470254 | 0.140371 | 0.872389 | 89.766% |
| 1 | 0 | 160005.2 | 19.409% | 3.378905 | 59.810% | 0.072680 | 1.307560 | 0.366832 | 0.809496 | 78.718% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
