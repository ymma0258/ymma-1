# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146797.4 | 0.000% | 7.965583 | 0.000% | 0.252584 | 2.593843 | 0.219117 | 0.880205 | 90.455% |
| 2 | 1 | 204343.8 | 39.201% | 2.201115 | 72.367% | 0.046111 | 1.011835 | 0.346313 | 0.774595 | 71.240% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
