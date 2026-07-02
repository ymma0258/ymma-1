# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.098507 | 0.000% | 0.256680 | 2.307121 | 0.150483 | 0.866001 | 89.671% |
| 1 | 0 | 161099.3 | 20.226% | 3.273958 | 59.573% | 0.080941 | 1.024941 | 0.225348 | 0.806027 | 79.107% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
