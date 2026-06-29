# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 8.409278 | 0.000% | 0.237821 | 2.900677 | 0.219302 | 0.872361 | 90.257% |
| 1 | 0 | 177310.0 | 21.262% | 3.754984 | 55.347% | 0.085957 | 1.536419 | 0.346721 | 0.816019 | 80.554% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
