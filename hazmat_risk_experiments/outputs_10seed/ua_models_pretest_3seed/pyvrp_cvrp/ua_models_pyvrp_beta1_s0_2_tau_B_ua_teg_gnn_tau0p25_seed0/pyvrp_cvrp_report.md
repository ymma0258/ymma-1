# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 10.121568 | 0.000% | 0.195850 | 3.547498 | 0.239774 | 0.871005 | 90.158% |
| 1 | 0 | 177554.0 | 21.429% | 4.845906 | 52.123% | 0.097749 | 1.874264 | 0.309018 | 0.817953 | 81.651% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
