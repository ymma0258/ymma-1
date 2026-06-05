# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 146531.2 | 0.000% | 13.187573 | 0.000% | 0.154568 | 3.997050 | 0.195155 | 0.836445 | 86.985% |
| 1 | 180823.8 | 23.403% | 6.195224 | 53.022% | 0.070084 | 2.095359 | 0.239297 | 0.725950 | 72.206% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
